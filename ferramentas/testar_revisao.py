"""Teste do motor da Revisão Delegado PC-BA.

Uso:
  python ferramentas/testar_revisao.py              gera o módulo de exemplo (revisao/conteudo/_exemplo.json)
                                                    e abre o HTML no navegador headless (sem erro de JS,
                                                    progresso, essencial, fichas que errei, celular)
  python ferramentas/testar_revisao.py --prints     idem, e tira 4 prints em .scratch/revisao/
  python ferramentas/testar_revisao.py --autoteste  REGRA CINCO: planta defeitos (ponto com id inexistente,
                                                    ficha sem gabarito, lei sem artigo, juris sem data, lei
                                                    adulterada, referência proibida, erro de JS) e só sai 0
                                                    se o gerador e o teste de navegador ACUSAREM cada um

O autoteste não depende de revisao/conteudo/ nem de assets/lei_seca_oficial.json: monta um edital, uma lei
seca e súmulas de mentira numa pasta temporária e chama o gerador como o titular chamaria (subprocesso).
Saídas: 0 tudo certo · 1 algo falhou.
"""

import copy
import datetime as dt
import json
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

RAIZ = Path(__file__).resolve().parent.parent
GERADOR = RAIZ / "ferramentas" / "gerar_revisao.py"
NAVEGADOR = RAIZ / "ferramentas" / "testar_revisao_navegador.mjs"
PROIBIDAS = RAIZ / "ferramentas" / "referencias_proibidas.py"
EXEMPLO = RAIZ / "revisao" / "conteudo" / "_exemplo.json"
PRINTS = RAIZ / ".scratch" / "revisao"


def roda(cmd, timeout=300):
    r = subprocess.run(
        cmd, capture_output=True, text=True, encoding="utf-8", errors="replace", timeout=timeout, cwd=RAIZ
    )
    return r.returncode, (r.stdout or "") + (r.stderr or "")


def node():
    n = shutil.which("node")
    if not n:
        raise SystemExit(
            "[FALHA] node não encontrado (o teste de navegador usa o Node com fetch e WebSocket nativos)"
        )
    return n


# ------------------------------------------------------------------ fixtures do autoteste
HOJE = dt.date.today().strftime("%d/%m/%Y")
ITENS = [
    {
        "id": "TST-PEN-1",
        "label": "Ponto de teste",
        "priority": "Alta",
        "discipline": "DIREITO PENAL",
        "number": "1",
    }
]
LEI = {
    "CP:17": {
        "id": "CP:17",
        "sigla": "CP",
        "art": "17",
        "diploma": "Código Penal — Decreto-Lei 2.848/1940",
        "texto": "Art. 17 - Não se pune a tentativa quando, por ineficácia absoluta do\nmeio ou por absoluta impropriedade do objeto, é impossível consumar-se o crime.(Redação dada pela Lei nº 7.209, de 11.7.1984)",
        "url": "https://www.planalto.gov.br/ccivil_03/decreto-lei/del2848compilado.htm",
        "baixado_em": HOJE,
    }
}
SUMULAS = {
    "SUM-STF-145": {
        "texto": "Não há crime, quando a preparação do flagrante pela polícia torna impossível a sua consumação."
    }
}
MODULO = {
    "esquema": 1,
    "modulo": "autoteste",
    "titulo": "Autoteste",
    "conferido_em": HOJE,
    "blocos": [
        {
            "titulo": "Bloco de teste",
            "pontos": [
                {
                    "id": "TST-PEN-1",
                    "prioridade": {"nivel": "Alta", "escore": 5},
                    "o_que_cai": ["Crime impossível exige ineficácia <b>absoluta</b>."],
                    "lei_seca": [
                        {
                            "lei": "CP",
                            "art": "17",
                            "texto": "Não se pune a tentativa quando, por ineficácia absoluta do meio ou por absoluta impropriedade do objeto, é impossível consumar-se o crime.",
                        }
                    ],
                    "jurisprudencia": [
                        {
                            "tribunal": "STF",
                            "sumula": "STF-145",
                            "fonte": "STF, Súmula 145",
                            "data": "13/12/1963",
                            "texto": "Não há crime, quando a preparação do flagrante pela polícia torna impossível a sua consumação.",
                        }
                    ],
                    "pegadinhas": ["Ineficácia relativa é tentativa."],
                    "dia_a_dia": ["Flagrante esperado é válido."],
                    "fichas": [
                        {
                            "item": "Ineficácia relativa gera crime impossível.",
                            "gabarito": "E",
                            "fundamento": "Art. 17: só a absoluta.",
                        }
                    ],
                    "questoes": [
                        {
                            "enunciado": "Assinale a correta.",
                            "alternativas": {L: f"alternativa {L}" for L in "ABCDE"},
                            "gabarito": "C",
                            "comentario": "Comentário.",
                            "origem": "Revisão",
                        }
                    ],
                    "checklist": ["Sei o art. 17."],
                }
            ],
        }
    ],
}


def ponto(m):
    return m["blocos"][0]["pontos"][0]


DEFEITOS = [
    (
        "ponto com id inexistente no edital",
        lambda m: ponto(m).__setitem__("id", "TST-PEN-999"),
        "não existe em assets/items.json",
    ),
    ("ponto sem id do edital", lambda m: ponto(m).pop("id"), "ponto sem id do edital"),
    ("ficha sem gabarito", lambda m: ponto(m)["fichas"][0].pop("gabarito"), "ficha sem gabarito"),
    ("ficha sem fundamento", lambda m: ponto(m)["fichas"][0].pop("fundamento"), "ficha sem fundamento"),
    ("lei sem chave", lambda m: ponto(m)["lei_seca"][0].pop("lei"), "lei sem chave"),
    ("lei sem artigo", lambda m: ponto(m)["lei_seca"][0].pop("art"), "lei sem artigo"),
    (
        "lei com artigo que não existe no oficial",
        lambda m: ponto(m)["lei_seca"][0].__setitem__("art", "17-Z"),
        "não existe em assets/lei_seca_oficial.json",
    ),
    (
        "lei com texto adulterado",
        lambda m: ponto(m)["lei_seca"][0].__setitem__(
            "texto",
            "Não se pune a tentativa quando, por ineficácia relativa do meio, é impossível consumar-se o crime.",
        ),
        "não confere com o oficial",
    ),
    ("juris sem fonte", lambda m: ponto(m)["jurisprudencia"][0].pop("fonte"), "juris sem fonte"),
    ("juris sem data", lambda m: ponto(m)["jurisprudencia"][0].pop("data"), "juris sem data"),
    (
        "juris com data fora do padrão",
        lambda m: ponto(m)["jurisprudencia"][0].__setitem__("data", "1963-12-13"),
        "fora de dd/mm/aaaa",
    ),
    (
        "súmula com texto trocado",
        lambda m: ponto(m)["jurisprudencia"][0].__setitem__("texto", "Há crime no flagrante preparado."),
        "não confere com assets/sumulas.json",
    ),
    ("questão sem gabarito", lambda m: ponto(m)["questoes"][0].pop("gabarito"), "questão sem gabarito"),
    (
        "questão com 4 alternativas",
        lambda m: ponto(m)["questoes"][0]["alternativas"].pop("E"),
        "alternativas A, B, C, D e E",
    ),
    (
        "questão com origem livre",
        lambda m: ponto(m)["questoes"][0].__setitem__("origem", "site qualquer"),
        "origem fora do padrão",
    ),
    (
        "prioridade sem escore",
        lambda m: ponto(m).__setitem__("prioridade", {"nivel": "Alta"}),
        "prioridade.escore",
    ),
    (
        "HTML fora da lista",
        lambda m: ponto(m)["o_que_cai"].append('<img src=x onerror="alert(1)">'),
        "tag <img>",
    ),
    ("conferido_em ausente", lambda m: m.pop("conferido_em"), "conferido_em"),
    (
        "referência proibida no texto",
        lambda m: ponto(m)["dia_a_dia"].append("Como no simulado do Projeto em Delta."),
        "referências proibidas",
    ),
]


def autoteste():
    falhas = []
    with tempfile.TemporaryDirectory(prefix="revisao-autoteste-") as tmp:
        t = Path(tmp)
        (t / "items.json").write_text(json.dumps(ITENS, ensure_ascii=False), encoding="utf-8")
        (t / "lei.json").write_text(json.dumps(LEI, ensure_ascii=False), encoding="utf-8")
        (t / "sumulas.json").write_text(json.dumps(SUMULAS, ensure_ascii=False), encoding="utf-8")
        base = [
            sys.executable,
            str(GERADOR),
            "--itens",
            str(t / "items.json"),
            "--lei",
            str(t / "lei.json"),
            "--sumulas",
            str(t / "sumulas.json"),
            "--saida",
            str(t / "saida"),
            "--sem-pdf",
        ]

        def gera(mod, nome):
            arq = t / f"{nome}.json"
            arq.write_text(json.dumps(mod, ensure_ascii=False), encoding="utf-8")
            return roda(base + [str(arq)])

        # 1) o módulo limpo PASSA (senão o autoteste não prova nada)
        rc, out = gera(MODULO, "limpo")
        html = t / "saida" / "autoteste.html"
        if rc != 0 or not html.exists():
            print(f"[AUTOTESTE FALHOU] o módulo limpo foi recusado (rc={rc}):\n{out}")
            return 1
        tam = f"{html.stat().st_size:,}".replace(",", ".")
        print(f"  o módulo limpo passa (rc=0; {tam} bytes)")
        # 2) cada defeito plantado é RECUSADO com a mensagem certa
        for i, (rotulo, planta, espera) in enumerate(DEFEITOS, 1):
            m = copy.deepcopy(MODULO)
            planta(m)
            rc, out = gera(m, f"defeito{i}")
            if rc == 1 and espera in out:
                print(f"  acusou (rc=1): {rotulo}")
            else:
                falhas.append(f"{rotulo}: rc={rc}, sem '{espera}' na saída")
        # 3) o teste de navegador acusa erro de JS plantado no HTML gerado
        rc, out = roda([node(), str(NAVEGADOR), "--autoteste", str(html)], timeout=120)
        if rc == 0 and "AUTOTESTE OK" in out:
            print("  acusou (navegador): erro de JS plantado no HTML")
        else:
            falhas.append(f"navegador não acusou o erro de JS plantado (rc={rc}): {out[-300:]}")
        # 4) e o HTML limpo abre sem erro (o teste de navegador também aprova o que é bom)
        rc, out = roda([node(), str(NAVEGADOR), str(html)], timeout=120)
        if rc == 0:
            print("  o HTML limpo abre sem erro de JS no navegador")
        else:
            falhas.append(f"o HTML limpo foi reprovado no navegador (rc={rc}): {out[-400:]}")
    # 5) os autotestes próprios do gerador e do verificador de referências
    for rot, cmd in (
        ("gerador (em memória)", [sys.executable, str(GERADOR), "--autoteste"]),
        ("verificador de referências", [sys.executable, str(PROIBIDAS), "--autoteste"]),
    ):
        rc, out = roda(cmd)
        if rc == 0:
            print(f"  autoteste do {rot}: OK")
        else:
            falhas.append(f"autoteste do {rot} falhou (rc={rc}): {out[-300:]}")
    if falhas:
        print("[AUTOTESTE FALHOU]")
        for f in falhas:
            print(f"  - {f}")
        return 1
    print(
        f"[AUTOTESTE OK] {len(DEFEITOS)} defeitos de conteúdo recusados pelo gerador, erro de JS acusado no navegador, "
        "módulo limpo aprovado"
    )
    return 0


def normal(prints):
    if not EXEMPLO.exists():
        print(
            f"[FALHA] módulo de exemplo ausente: {EXEMPLO} (fica fora do Git; ver revisao/ESQUEMA_MODULO.md)"
        )
        return 1
    rc, out = roda([sys.executable, str(GERADOR), str(EXEMPLO)])
    print(out.rstrip())
    if rc != 0:
        print(f"[FALHA] o gerador saiu {rc}")
        return 1
    html = RAIZ / "revisao" / "saida" / "_exemplo.html"
    rc, out = roda([sys.executable, str(PROIBIDAS), str(html)])
    print(out.rstrip())
    if rc != 0:
        return 1
    cmd = [node(), str(NAVEGADOR), str(html)] + ([str(PRINTS)] if prints else [])
    rc, out = roda(cmd, timeout=180)
    print(out.rstrip())
    if rc != 0:
        print(f"[FALHA] teste de navegador saiu {rc}")
        return 1
    print(
        "[OK] motor da revisão: módulo de exemplo gerado (HTML e PDF), sem referência proibida e sem erro de JS"
    )
    return 0


if __name__ == "__main__":
    if "--autoteste" in sys.argv:
        sys.exit(autoteste())
    sys.exit(normal("--prints" in sys.argv))
