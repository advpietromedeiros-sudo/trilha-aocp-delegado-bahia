#!/usr/bin/env python3
"""Rotina contra conteúdo desatualizado na revisão por prioridade (D-018, docs/REVISAO_PLANO.md).

Uso:
  python ferramentas/verificar_atualidade.py --estado              data da última coleta da lei seca oficial;
                                                                   sai 1 se tiver mais de 30 dias, 2 se não houver base
  python ferramentas/verificar_atualidade.py --conferir ARQ        confere um módulo (.html) ou uma lista (.json)
  python ferramentas/verificar_atualidade.py --chaves              lista as chaves de lei disponíveis e as lacunas
  python ferramentas/verificar_atualidade.py --rotina              baixa a lei seca, compara com a anterior e grava
                                                                   revisao/relatorios/AAAA-MM-DD.txt
  python ferramentas/verificar_atualidade.py --autoteste           prova que ACUSA (REGRA CINCO) — sem depender da
                                                                   base baixada, que fica fora do Git

O formato que os módulos usam (fixado em 06/11/2026 com a frente do gerador):
  <meta name="conferido-em" content="dd/mm/aaaa">                                   obrigatório no topo
  <blockquote class="lei" data-lei="CP" data-art="121" data-par="§ 2º" data-inc="VI" data-ali="a">trecho</blockquote>
      data-lei = a MESMA chave (sigla) de assets/lei_seca_oficial.json; data-par, data-inc e data-ali opcionais.
      A conferência é a de ferramentas/localizar_lei.py — a MESMA régua do gerador (07/11/2026): trecho CONTIDO
      no artigo oficial vigente (anotações do Planalto, aspas, hífens, espaços e º/°/o normalizados) e
      parágrafo, inciso e alínea LOCALIZADOS na estrutura do artigo, um dentro do outro.
  <div class="juris" data-tribunal="STJ" data-fonte="Súmula 593 | REsp 1.234.567/BA | Tema 1.234"
       data-data="dd/mm/aaaa" data-sumula="STJ-593">…</div>
      data-fonte e data-data obrigatórios; data-sumula (STJ-n, STF-n, SV-n) é conferida em assets/sumulas.json.
O .json aceito por --conferir: {"conferido_em": "dd/mm/aaaa", "leis": [{"lei","art","par","inc","texto"}],
  "juris": [{"tribunal","fonte","data","sumula","texto"}]}.
"""
from __future__ import annotations

import html.parser
import json
import re
import subprocess
import sys
from datetime import date, datetime
from pathlib import Path

RAIZ = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(RAIZ / "ferramentas"))
import localizar_lei as LL  # noqa: E402  (régua comum com o gerador)
LEI_SECA = RAIZ / "assets" / "lei_seca_oficial.json"
SUMULAS = RAIZ / "assets" / "sumulas.json"
CATALOGO = RAIZ / "assets" / "catalogo_leis.json"
RELATORIOS = RAIZ / "revisao" / "relatorios"
LIMITE_DIAS = 30
RX_DATA = re.compile(r"^(\d{2})/(\d{2})/(\d{4})$")


# ------------------------------------------------------------------ normalização (régua comum)
normalizar = LL.normalizar


def data_valida(s: str | None) -> date | None:
    m = RX_DATA.match((s or "").strip())
    if not m:
        return None
    try:
        return date(int(m[3]), int(m[2]), int(m[1]))
    except ValueError:
        return None


id_sumula = LL.id_sumula
situacao_sumula = LL.situacao_sumula
RX_CANCELADA = LL.RX_CANCELADA


# ------------------------------------------------------------------ leitura do módulo
class _Leitor(html.parser.HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.meta_conferido = None
        self.leis, self.juris = [], []
        self._pilha = []  # (tag, registro) abertos de interesse

    def handle_starttag(self, tag, attrs):
        a = dict(attrs)
        classes = (a.get("class") or "").split()
        if tag == "meta" and a.get("name") == "conferido-em":
            self.meta_conferido = a.get("content")
        elif tag == "blockquote" and "lei" in classes:
            reg = {"lei": a.get("data-lei"), "art": a.get("data-art"), "par": a.get("data-par"),
                   "inc": a.get("data-inc"), "ali": a.get("data-ali"), "texto": "", "linha": self.getpos()[0]}
            self.leis.append(reg)
            self._pilha.append((tag, reg, 0))
            return
        elif tag == "div" and "juris" in classes:
            reg = {"tribunal": a.get("data-tribunal"), "fonte": a.get("data-fonte"), "data": a.get("data-data"),
                   "sumula": a.get("data-sumula"), "texto": "", "linha": self.getpos()[0]}
            self.juris.append(reg)
            self._pilha.append((tag, reg, 0))
            return
        if self._pilha and tag == self._pilha[-1][0]:
            t, r, n = self._pilha[-1]
            self._pilha[-1] = (t, r, n + 1)

    def handle_endtag(self, tag):
        if self._pilha and tag == self._pilha[-1][0]:
            t, r, n = self._pilha[-1]
            if n == 0:
                self._pilha.pop()
            else:
                self._pilha[-1] = (t, r, n - 1)

    def handle_data(self, data):
        for _, reg, _ in self._pilha:
            reg["texto"] += data


def ler_modulo(caminho: Path) -> dict:
    bruto = caminho.read_text(encoding="utf-8")
    if caminho.suffix.lower() == ".json":
        d = json.loads(bruto)
        return {"conferido_em": d.get("conferido_em"), "leis": d.get("leis", []), "juris": d.get("juris", [])}
    p = _Leitor()
    p.feed(bruto)
    return {"conferido_em": p.meta_conferido, "leis": p.leis, "juris": p.juris}


# ------------------------------------------------------------------ conferência
def conferir(mod: dict, oficial: dict, sumulas: dict) -> tuple[list[str], list[str]]:
    """Devolve (erros, avisos). Qualquer erro reprova o módulo."""
    erros, avisos = [], []
    if not data_valida(mod.get("conferido_em")):
        erros.append(f'falta <meta name="conferido-em" content="dd/mm/aaaa"> válido (achado: {mod.get("conferido_em")!r})')
    for c in mod["leis"]:
        onde = f"linha {c.get('linha', '?')}: {c.get('lei')} art. {c.get('art')}"
        e, a = LL.conferir_citacao(c, oficial)
        erros += [f"{onde} — {x}" for x in e]
        avisos += [f"{onde} — {x}" for x in a]
    for j in mod["juris"]:
        onde = f"linha {j.get('linha', '?')}: juris {j.get('tribunal') or '?'}"
        if not (j.get("fonte") or "").strip():
            erros.append(f"{onde} — jurisprudência sem data-fonte")
        if not data_valida(j.get("data")):
            erros.append(f"{onde} — jurisprudência sem data-data válida (dd/mm/aaaa), achado {j.get('data')!r}")
        if j.get("sumula"):
            sid = id_sumula(j["sumula"])
            if not sid:
                erros.append(f"{onde} — data-sumula {j['sumula']!r} fora do formato STJ-n / STF-n / SV-n")
            elif sid not in sumulas:
                avisos.append(f"{onde} — {sid} não está em assets/sumulas.json: situação não conferida")
            else:
                sit = situacao_sumula(sumulas[sid])
                if sit:
                    erros.append(f"{onde} — {sid} está marcada como {sit.upper()} em assets/sumulas.json")
    return erros, avisos


# ------------------------------------------------------------------ estado da lei seca
def carregar_oficial() -> dict | None:
    if not LEI_SECA.exists():
        return None
    return json.loads(LEI_SECA.read_text(encoding="utf-8"))


def coleta(oficial: dict) -> tuple[date | None, date | None]:
    datas = [data_valida(v.get("baixado_em")) for v in oficial.values()]
    datas = [d for d in datas if d]
    return (min(datas), max(datas)) if datas else (None, None)


def estado(hoje: date | None = None) -> int:
    hoje = hoje or date.today()
    oficial = carregar_oficial()
    if oficial is None:
        print(f"  pulada: {LEI_SECA.relative_to(RAIZ)} não existe nesta máquina (fica fora do Git, D-015). "
              "Rode atualizar_lei_seca.bat para baixá-la.")
        return 2
    mais_velha, mais_nova = coleta(oficial)
    if not mais_velha:
        print("  ❌ a base não tem nenhuma data de coleta legível (campo baixado_em)")
        return 1
    idade = (hoje - mais_velha).days
    siglas = sorted({v["sigla"] for v in oficial.values()})
    print(f"  lei seca oficial: {len(oficial)} artigos de {len(siglas)} diplomas; coleta mais antiga "
          f"{mais_velha:%d/%m/%Y}, mais recente {mais_nova:%d/%m/%Y} — {idade} dia(s)")
    if idade > LIMITE_DIAS:
        print(f"  ❌ mais de {LIMITE_DIAS} dias: rode atualizar_lei_seca.bat (ou ferramentas\\rotina_atualidade.bat) "
              "antes de gerar ou revisar qualquer módulo")
        return 1
    print(f"  ✅ dentro do prazo de {LIMITE_DIAS} dias")
    return 0


def chaves() -> int:
    oficial = carregar_oficial() or {}
    cat = json.loads(CATALOGO.read_text(encoding="utf-8"))["diplomas"]
    tem = {}
    for v in oficial.values():
        tem[v["sigla"]] = tem.get(v["sigla"], 0) + 1
    print("  chaves disponíveis (data-lei) e nº de artigos:")
    for s in sorted(tem):
        print(f"    {s:8} {tem[s]:5}")
    faltam = [d for d in cat if d["sigla"] not in tem]
    print(f"\n  diplomas do catálogo SEM texto oficial baixado: {len(faltam)} de {len(cat)}")
    for d in faltam:
        print(f"    {d['sigla']:8} {d['nome'][:70]}{'' if d.get('url') else '  (sem URL: lei estadual)'}")
    return 0


# ------------------------------------------------------------------ rotina (download + relatório)
def rotina() -> int:
    hoje = date.today()
    RELATORIOS.mkdir(parents=True, exist_ok=True)
    rel = RELATORIOS / f"{hoje:%Y-%m-%d}.txt"
    antes = carregar_oficial() or {}
    ini = datetime.now()
    r = subprocess.run([sys.executable, str(RAIZ / "ferramentas" / "atualizar_lei_seca.py")], cwd=RAIZ,
                       capture_output=True, text=True, encoding="utf-8", errors="replace")
    depois = carregar_oficial() or {}
    novos = sorted(set(depois) - set(antes))
    sumiram = sorted(set(antes) - set(depois))
    mudaram = sorted(k for k in set(antes) & set(depois)
                     if normalizar(antes[k]["texto"]) != normalizar(depois[k]["texto"]))
    alt26 = sorted(k for k, v in depois.items() if str(v.get("alteracao_2026")).lower() == "true")
    linhas = [
        f"Relatório da rotina contra conteúdo desatualizado — {hoje:%d/%m/%Y}, "
        f"{ini:%Hh%M} a {datetime.now():%Hh%M}",
        "Gerado por ferramentas/verificar_atualidade.py --rotina (ferramentas\\rotina_atualidade.bat).",
        "",
        f"1. Download da lei seca oficial (atualizar_lei_seca.py): saída {r.returncode}",
    ]
    linhas += ["   " + x for x in (r.stdout or "").strip().splitlines()[-60:]]
    if r.stderr.strip():
        linhas += ["   [erros]"] + ["   " + x for x in r.stderr.strip().splitlines()[-20:]]
    linhas += ["", "2. O que mudou na base (texto normalizado, artigo a artigo)",
               f"   antes: {len(antes)} artigos | depois: {len(depois)} artigos",
               f"   novos: {len(novos)} | sumiram: {len(sumiram)} | texto alterado: {len(mudaram)}"]
    for rot, lst in (("texto alterado", mudaram), ("novos", novos), ("sumiram", sumiram)):
        if lst:
            linhas.append(f"   {rot} (até 200): " + ", ".join(lst[:200]))
    linhas += ["", f"3. Artigos com nota de alteração em 2026 (conferir o marco de 29/07/2026): {len(alt26)}"]
    if alt26:
        linhas.append("   " + ", ".join(alt26[:200]))
    from io import StringIO
    import contextlib
    buf = StringIO()
    with contextlib.redirect_stdout(buf):
        rc_estado = estado()
        chaves()
    linhas += ["", f"4. Estado depois da rotina (--estado saiu {rc_estado})"] + ["   " + x for x in buf.getvalue().splitlines()]
    # o atualizar_lei_seca.py sai 0 mesmo quando um diploma falha: a falha se lê na saída dele
    falhou = re.search(r"Falharam[^:]*:\s*(.+)", r.stdout or "")
    falhas = [x.strip() for x in falhou[1].split(",")] if falhou else []
    linhas += ["", f"5. Diplomas que NÃO baixaram nesta rotina: {len(falhas)}"
               + (f" — {', '.join(falhas)} (corrigir a URL em assets/catalogo_leis.json; até lá, citação desses "
                  "diplomas não passa no --conferir)" if falhas else "")]
    linhas += ["", "6. Agendamento (DECISÃO DO TITULAR — nada foi agendado por esta rotina)",
               "   Para rodar toda segunda-feira às 08h00, cole no PowerShell (máquina do titular; volta na hora):",
               '   schtasks /Create /TN "Trilha AOCP - rotina de atualidade" /SC WEEKLY /D MON /ST 08:00 '
               f'/TR "\\"{RAIZ / "ferramentas" / "rotina_atualidade.bat"}\\""',
               '   Para desfazer: schtasks /Delete /TN "Trilha AOCP - rotina de atualidade" /F', ""]
    rel.write_text("\n".join(linhas), encoding="utf-8")
    print("\n".join(linhas))
    print(f"\n  relatório gravado: {rel}")
    return 0 if r.returncode == 0 and rc_estado == 0 and not falhas else 1


# ------------------------------------------------------------------ autoteste
def autoteste() -> int:
    """Base mínima embutida (o teste não depende da lei seca baixada, que fica fora do Git)."""
    oficial = {"CP:121": {"texto": "Art. 121. Matar alguém:\nPena - reclusão, de seis a vinte anos.\n§ 1º Se o agente "
                                   "comete o crime impelido por motivo de relevante valor social ou moral",
                          "baixado_em": "03/11/2026"},
               "CP:13": {"texto": "Art. 13 - O resultado somente é imputável a quem lhe deu causa.\n§ 2º - A omissão é "
                                  "penalmente relevante. O dever de agir incumbe a quem:(Incluído pela Lei nº 7.209)\n"
                                  "a) tenha por lei obrigação de cuidado, proteção ou vigilância;\nb) de outra forma",
                         "baixado_em": "07/11/2026"},
               "CPP:78": {"texto": "Art. 78. Regras:\nI - no concurso com o júri;\nIl - no concurso de jurisdições da "
                                   "mesma categoria:\na) preponderará a do lugar da infração;\nIII - de diversas "
                                   "categorias", "baixado_em": "07/11/2026"},
               "L7960:2": {"texto": "Art. 2° A prisão temporária será decretada pelo Juiz.\n§ 2° O despacho que "
                                    "decretar a prisão temporária deverá ser fundamentado.", "baixado_em": "07/11/2026"},
               "L11340:5": {"texto": "Art. 5º Para os efeitos desta Lei, configura violência doméstica e familiar "
                                     "contra a mulher qualquer ação ou omissão baseada no gênero que lhe cause morte, "
                                     "lesão, sofrimento físico, sexual ou psicológico e dano moral ou patrimonial:\n"
                                     "I - no âmbito da unidade doméstica", "baixado_em": "03/11/2026"}}
    sumulas = {"SUM-STJ-470": {"texto": "O Ministério Público não tem legitimidade ... • Cancelada. • O Plenário do "
                                        "STF decidiu ..."},
               "SUM-STJ-70": {"texto": "Os juros moratórios ... Superada em parte."},
               "SUM-STJ-593": {"texto": "O crime de estupro de vulnerável se configura com a conjunção carnal ..."}}
    topo = '<meta name="conferido-em" content="06/11/2026">'
    lei_ok = ('<blockquote class="lei" data-lei="CP" data-art="121" data-par="§ 1º">“Matar   alguém:” Pena – '
              'reclusão, de seis a vinte anos.</blockquote>')
    juris_ok = ('<div class="juris" data-tribunal="STJ" data-fonte="Súmula 593" data-data="25/10/2017" '
                'data-sumula="STJ-593"><p>O crime de <b>estupro</b> de vulnerável…</p></div>')
    # (nome, módulo, saída esperada, o MOTIVO que o erro tem de citar — acusar pelo motivo errado é falha)
    casos = [
        ("caso limpo passa (aspas, travessão e espaços tipográficos não acusam)", topo + lei_ok + juris_ok, 0, None),
        ("texto de artigo adulterado acusa", topo + lei_ok.replace("seis a vinte", "seis a doze") + juris_ok, 1,
         "DIFERE"),
        ("súmula CANCELADA citada acusa", topo + lei_ok + juris_ok.replace("STJ-593", "STJ-470"), 1, "CANCELADA"),
        ("súmula SUPERADA em parte citada acusa", topo + lei_ok + juris_ok.replace("STJ-593", "STJ-70"), 1,
         "SUPERADA"),
        ("jurisprudência sem data-fonte acusa", topo + lei_ok + juris_ok.replace('data-fonte="Súmula 593" ', ""), 1,
         "sem data-fonte"),
        ("jurisprudência sem data-data acusa", topo + lei_ok + juris_ok.replace('data-data="25/10/2017"', ""), 1,
         "sem data-data"),
        ("data-data em formato errado acusa", topo + juris_ok.replace("25/10/2017", "2017-10-25"), 1, "sem data-data"),
        ("módulo sem carimbo conferido-em acusa", lei_ok + juris_ok, 1, "conferido-em"),
        ("artigo que não está na base acusa (não confere = não passa)", topo + lei_ok.replace('"121"', '"999"'), 1,
         "não está no texto oficial"),
        ("data-par inexistente no artigo acusa", topo + lei_ok.replace("§ 1º", "§ 7º"), 1, "data-par"),
        ("inciso existente passa", topo + '<blockquote class="lei" data-lei="L11340" data-art="5" data-inc="I">'
                                          "no âmbito da unidade doméstica</blockquote>", 0, None),
        ("inciso inexistente acusa (a letra i solta no texto não engana)",
         topo + '<blockquote class="lei" data-lei="L11340" data-art="5" data-inc="IV">'
                "no âmbito da unidade doméstica</blockquote>", 1, "data-inc"),
        # 07/11/2026: os três casos em que o gerador aprovava e este verificador reprovava (régua agora comum)
        ("alínea em data-ali passa (CP 13, § 2º, a)",
         topo + '<blockquote class="lei" data-lei="CP" data-art="13" data-par="§ 2º" data-ali="a">'
                "tenha por lei obrigação de cuidado</blockquote>", 0, None),
        ("alínea marcada como data-inc acusa e diz o porquê",
         topo + '<blockquote class="lei" data-lei="CP" data-art="13" data-par="§ 2º" data-inc="a">'
                "tenha por lei obrigação de cuidado</blockquote>", 1, "ALÍNEA"),
        ("alínea inexistente acusa (CP 13, § 2º, c)",
         topo + '<blockquote class="lei" data-lei="CP" data-art="13" data-par="§ 2º" data-ali="c">'
                "tenha por lei obrigação de cuidado</blockquote>", 1, "data-ali"),
        ("data-inc II acha o 'Il' do Planalto (CPP 78)",
         topo + '<blockquote class="lei" data-lei="CPP" data-art="78" data-inc="II">'
                "no concurso de jurisdições da mesma categoria</blockquote>", 0, None),
        ("data-par § 2º acha o '§ 2°' do Planalto (Lei 7.960)",
         topo + '<blockquote class="lei" data-lei="L7960" data-art="2" data-par="§ 2º">'
                "O despacho que decretar a prisão temporária</blockquote>", 0, None),
        ("súmula vinculante SV-n é lida (fora da base só avisa)",
         topo + juris_ok.replace("STJ-593", "SV-14"), 0, None),
    ]
    falhas = 0
    for nome, html_txt, esperado, motivo in casos:
        p = _Leitor()
        p.feed(html_txt)
        erros, _ = conferir({"conferido_em": p.meta_conferido, "leis": p.leis, "juris": p.juris}, oficial, sumulas)
        rc = 1 if erros else 0
        ok = rc == esperado and (motivo is None or any(motivo in e for e in erros)) and \
            (esperado == 1 or not erros)
        falhas += not ok
        print(f"  {'✅' if ok else '❌'} {nome} (saída {rc}{'' if not erros else '; ' + str(len(erros)) + ' erro(s): ' + erros[0][:60]})")
    # a régua da situação nas súmulas reais da base (se existir): não pode marcar súmula viva por engano
    vivas = {"texto": "Da anotação irregular em cadastro de proteção ao crédito, não cabe indenização por dano moral, "
                      "quando preexistente legítima inscrição, ressalvado o direito ao cancelamento."}
    ok = situacao_sumula(vivas) is None
    falhas += not ok
    print(f"  {'✅' if ok else '❌'} súmula viva com a palavra 'cancelamento' no texto NÃO acusa")
    # o --estado acusa base velha e aprova base nova
    velha, nova = {"X:1": {"sigla": "X", "baixado_em": "01/01/2026", "texto": ""}}, \
        {"X:1": {"sigla": "X", "baixado_em": "03/11/2026", "texto": ""}}
    for rot, base, esperado in (("base de 01/01/2026 vista em 06/11/2026 acusa", velha, 1),
                                ("base de 03/11/2026 vista em 06/11/2026 passa", nova, 0)):
        mv, _ = coleta(base)
        rc = 1 if (date(2026, 11, 6) - mv).days > LIMITE_DIAS else 0
        ok = rc == esperado
        falhas += not ok
        print(f"  {'✅' if ok else '❌'} --estado: {rot}")
    return 1 if falhas else 0


def main() -> int:
    sys.stdout.reconfigure(encoding="utf-8")
    a = sys.argv[1:]
    if "--autoteste" in a:
        return autoteste()
    if "--estado" in a:
        return estado()
    if "--chaves" in a:
        return chaves()
    if "--rotina" in a:
        return rotina()
    if "--conferir" in a:
        arq = Path(a[a.index("--conferir") + 1])
        oficial = carregar_oficial()
        if oficial is None:
            print(f"  não há {LEI_SECA.relative_to(RAIZ)}: rode atualizar_lei_seca.bat antes de conferir")
            return 2
        sumulas = json.loads(SUMULAS.read_text(encoding="utf-8"))
        mod = ler_modulo(arq)
        erros, avisos = conferir(mod, oficial, sumulas)
        print(f"  {arq.name}: {len(mod['leis'])} citação(ões) de lei, {len(mod['juris'])} de jurisprudência")
        for x in avisos:
            print(f"  ⚠️ {x}")
        for x in erros:
            print(f"  ❌ {x}")
        if erros:
            print(f"  REPROVADO: {len(erros)} problema(s)")
            return 1
        print("  ✅ aprovado: todo artigo confere com o texto vigente e toda jurisprudência tem fonte e data")
        return 0
    print(__doc__)
    return 2


if __name__ == "__main__":
    sys.exit(main())
