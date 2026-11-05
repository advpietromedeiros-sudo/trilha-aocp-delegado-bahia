"""Importa as questões objetivas comentadas dos Simulados DPC-BA (Projeto em Delta) para o Treino de Discursiva.

Pedido do titular (04/11/2026, 16h36): "RODE ESSES SIMULADOS NA APLICAÇÃO TRILHA AOCP DISCURSIVA ... E MONTE
CONFORME ESTÃO NOS PDF'S DOS SIMULADOS A PARTE DAS QUESTÕES OBJETIVAS TODAS COMENTADAS".

Os PDFs são material de TERCEIRO (curso preparatório): o arquivo gerado, discursiva/simulados_delta.js, fica SÓ no
disco (.gitignore, D-002) e não entra no arquivo único de envio (empacotar_discursiva.py o retira). Este script é
autoral e vai para o Git: ele reconstrói a base a partir dos PDFs originais, que também não estão no Git.

🔴 Cada página dos PDFs traz marca d'água com o CPF e o código do comprador. Ela é RETIRADA aqui e o script falha se
sobrar qualquer número com forma de CPF no resultado.

Uso: python -I ferramentas/importar_simulados_delta.py [pasta-dos-pdfs]   (padrão: ~/Downloads)
Requer pdftotext e pdfimages (poppler) no PATH.
"""

import base64
import json
import re
import subprocess
import sys
import tempfile
from pathlib import Path

RAIZ = Path(__file__).resolve().parent.parent
SAIDA = RAIZ / "discursiva" / "simulados_delta.js"
PASTA_PADRAO = Path.home() / "Downloads"

# Notas de ATUALIZAÇÃO (texto autoral), da auditoria de 04/11/2026 contra o texto oficial (Planalto e legislabahia).
# "red" = pela lei vigente o gabarito não se sustenta (conferido pessoalmente na fonte oficial); "amarela" = comentário
# desatualizado ou com remissão errada, gabarito mantido. O texto do curso NÃO é alterado: a nota aparece ao lado.
ATUALIZACOES = {
    (1, 85): ("red", "Pela redação vigente, a questão tem duas respostas (A e B). Desde o Decreto 11.080/2022, o art. 5º, § 1º, do Decreto 6.514/2008 fala em \"multa consolidada\", não em \"multa máxima cominada\": a alternativa A também é incorreta. Obs.: a alternativa C (5 anos) segue o decreto (Decreto 12.189/2024), mas a Lei 9.605, art. 72, § 8º, V, ainda diz 3 anos."),
    (1, 84): ("amarela", "A LC 236/2026 incluiu no art. 151 do CTN os incisos VII a X (arbitragem, proposta de transação aceita, mediação, seguro-garantia ou fiança) e no art. 156 os incisos XII e XIII. O comentário usa o rol antigo; o gabarito se mantém."),
    (1, 26): ("amarela", "Lei 12.288/2010, art. 1º, parágrafo único: discriminação racial (I), desigualdade racial (II), desigualdade de gênero e raça (III), população negra (IV). O comentário troca a numeração; o gabarito se mantém."),
    (2, 34): ("red", "Pela lei vigente, nenhuma alternativa está correta (questão a anular). A Lei 14.580/2023 mudou o art. 22, III, da Lei 11.370/2009: hoje o Delegado-Geral Adjunto \"indica ao Delegado-Geral as providências necessárias ao aperfeiçoamento e à eficiência dos serviços\". \"Coordenar e supervisionar a execução dos serviços das unidades\" (alternativa C) é a redação original, revogada. E \"acompanhar projetos na Assembleia Legislativa\" está hoje no art. 21, V."),
    (2, 18): ("amarela", "Atualidades: a nota sobre 2026 está superada, segundo notícias (não conferido em fonte oficial). O adicional de 40% sobre café, carne e frutas caiu em 20/11/2025, e a Suprema Corte dos EUA derrubou as tarifas baseadas na IEEPA em fevereiro de 2026. O gabarito vale como fato histórico."),
    (2, 19): ("amarela", "Atualidades, segundo notícias (não conferido em fonte oficial): a vacina do Butantan contra a dengue já foi registrada pela Anvisa (26/11/2025; DOU de 08/12/2025), com previsão divulgada de mais de 30 milhões de doses. O gabarito se mantém."),
    (2, 36): ("amarela", "O enunciado manda responder à luz da Lei 12.209/2011, mas o conteúdo é da Lei 6.677/1994 (arts. 10, 11, 13 e 16). O gabarito E só está certo pela 6.677."),
    (2, 37): ("amarela", "A Lei 14.961/2025 incluiu o Delegado-Geral Adjunto de Operações no Conselho Superior da Polícia Civil (Lei 11.370/2009, art. 15, III). O comentário não registra; o gabarito se mantém."),
    (2, 81): ("amarela", "A redação do art. 16 da Lei 7.347/1985 (limite territorial) veio da Lei 9.494/1997, e não da MP 2.180-35/2001. O gabarito se mantém."),
    (2, 90): ("amarela", "Trecho do comentário corrompido no PDF. Lei 8.072/1990, art. 1º, II (redação da Lei 13.964/2019): roubo a) circunstanciado pela restrição de liberdade da vítima (art. 157, § 2º, V); b) circunstanciado pelo emprego de arma de fogo (art. 157, § 2º-A, I) ou de arma de fogo de uso proibido ou restrito (art. 157, § 2º-B); c) qualificado pelo resultado lesão corporal grave ou morte (art. 157, § 3º). O gabarito D está correto."),
    (3, 34): ("amarela", "A Lei 14.961/2025 levou o art. 9º da Lei 11.370/2009 a 6 incisos: o V passou a ser o Delegado-Geral Adjunto de Operações, e a Corregedoria foi para o VI. O gabarito se mantém."),
    (3, 40): ("amarela", "O art. 42 da Lei 6.677/1994 só prevê a recondução pela reintegração do anterior ocupante; a recondução por inabilitação em estágio probatório é da Lei 8.112/1990 (art. 29, I). O próprio simulado descreve o art. 42 corretamente na questão 43. O gabarito C se mantém, mas a alternativa E é discutível em recurso."),
    (3, 42): ("amarela", "A dispensa de licitação ligada à Lei 12.850 está no art. 75, IV, \"l\", da Lei 14.133/2021, e não no art. 75, XVI. O gabarito se mantém."),
    (3, 89): ("amarela", "A tortura \"mediante sequestro\" é causa de aumento do art. 1º, § 4º, III, da Lei 9.455/1997 (o parágrafo não tem inciso IV). O gabarito se mantém."),
    (4, 94): ("red", "Pela lei vigente, nenhuma alternativa está correta (questão a anular). A Lei 15.487/2026 deu nova redação ao art. 241-D do ECA: \"aliciar, assediar, convidar, instigar ou constranger, por qualquer meio, menor de 14 (quatorze) anos, com o fim de praticar ato libidinoso\". Saiu a expressão \"meio de comunicação\", que era justamente a interpretada pelo STJ no julgado do Informativo 860: hoje também o contato pessoal e presencial está no tipo."),
    (4, 79): ("amarela", "Sentença de improbidade não se sujeita a reexame necessário: \"Não haverá remessa necessária\" (Lei 8.429/1992, art. 17-C, § 3º, incluído em 2021). O comentário diz o contrário; o gabarito se mantém."),
}

DISCIPLINAS = [
    "Língua Portuguesa", "Raciocínio Lógico", "Informática", "Atualidades", "Legislação Geral/Estadual",
    "Promoção da Igualdade Racial e de Gênero", "Direito Constitucional", "Direito Administrativo", "Direito Penal",
    "Direito Processual Penal", "Legislação Penal e Processual Penal Extravagante", "Direito Civil e Empresarial",
    "Direito Processual Civil", "Direito Tributário", "Direito Ambiental", "Medicina Legal", "Criminologia",
]
# Conferidos à mão em 04/11/2026 contra os PDFs: (simulado, nº da questão) → correção
AJUSTES = {(1, 51): "alt-A-sem-letra"}
# (simulado, página da figura) → (questão, onde): s3 = gráfico do enunciado; s4 = diagrama do comentário
FIGURAS = {(3, 12): (14, "enun"), (4, 12): (13, "com")}
MARCA = re.compile(r"\d{3}\.\d{3}\.\d{3}-\d{2}(?:\.\d+)?|\b\d{6}\.\d{6}\b")
CPF = re.compile(r"\d{3}\.?\d{3}\.?\d{3}-\d{2}")
CAB_Q = re.compile(r"^\s*(\d{1,3})\s*[-–]\s*\((.+?)\)\s*(.*)$")
ALT = re.compile(r"^\s*([A-E])\)\s?(.*)$")
GAB = re.compile(r"Gabarito:\s*([A-E])\b\s*([-–]\s*ANULADA[^!]*!*)?", re.I)
TEXTO_BASE = re.compile(r"^\s*Texto base para as quest[õo]es\s+(\d+)\s+a\s+(\d+)", re.I)


def pdf_do_simulado(pasta: Path, n: int) -> Path:
    achados = sorted(p for p in pasta.glob(f"SIMULADO {n} - DPC-BA - Comentad*.pdf") if "(1)" not in p.name)
    if not achados:
        sys.exit(f"ERRO: não achei o PDF comentado do Simulado {n} em {pasta}")
    return achados[0]


def paginas(pdf: Path) -> list[list[str]]:
    txt = subprocess.run(["pdftotext", "-enc", "UTF-8", "-layout", str(pdf), "-"], capture_output=True, check=True).stdout
    saida = []
    for pag in txt.decode("utf-8").split("\f"):
        linhas = []
        for l in pag.split("\n"):
            l = MARCA.sub("", l).rstrip()
            if re.fullmatch(r"\s*\d{1,3}\s*", l):  # número da página
                continue
            if l.strip() in ("COMENTÁRIOS",) or not l.strip() and linhas and not linhas[-1].strip():
                if l.strip() == "COMENTÁRIOS":
                    linhas.append("§COMENTARIOS§")
                continue
            linhas.append(l)
        saida.append(linhas)
    return saida


def figuras(pdf: Path) -> dict[int, list[str]]:
    """Figuras reais (as que aparecem uma vez só e não são capa): {página: [data-uri png]}."""
    lista = subprocess.run(["pdfimages", "-list", str(pdf)], capture_output=True, check=True).stdout.decode().splitlines()[2:]
    tam = {}
    for l in lista:
        c = l.split()
        if c[2] == "image":
            tam.setdefault((c[3], c[4]), []).append((int(c[0]), int(c[1])))
    alvo = [(pg, num) for v in tam.values() if len(v) == 1 for pg, num in v if pg > 2]
    res: dict[int, list[str]] = {}
    with tempfile.TemporaryDirectory() as d:
        for pg, num in alvo:
            subprocess.run(["pdfimages", "-png", "-f", str(pg), "-l", str(pg), str(pdf), f"{d}/p"], check=True)
            # pdfimages numera a partir de 000 dentro da página: pega o maior arquivo (a figura; o resto é logo/marca)
            maior = max(Path(d).glob("p-*.png"), key=lambda p: p.stat().st_size)
            res.setdefault(pg, []).append("data:image/png;base64," + base64.b64encode(maior.read_bytes()).decode())
            for arq in Path(d).glob("p-*.png"):
                arq.unlink()
    return res


def juntar(a: str, b: str) -> str:
    """Junta duas linhas; hífen no fim da linha é quebra de palavra composta ("Reputa-" + "se" = "Reputa-se")."""
    a = a.rstrip()
    return a + b.strip() if a.endswith("-") else a + " " + b.strip()


def blocos(linhas: list[str]) -> list[dict]:
    """Junta linhas em parágrafos. Tabela e fórmula (colunas: 3+ espaços internos; ou linha curta recuada) viram UM
    bloco pré-formatado, com as colunas alinhadas como no PDF; linhas em branco dentro dele somem. Parágrafo com recuo
    na primeira linha (texto-base) chega à margem direita e continua sendo texto."""
    out: list[dict] = []
    for l in linhas:
        cru = l.rstrip()
        if not cru.strip():
            out.append({"t": "br"})
            continue
        recuo = len(cru) - len(cru.lstrip())
        coluna = re.search(r"\S {3,}\S", cru)
        k = len(out) - 1
        while k >= 0 and out[k]["t"] == "br":
            k -= 1
        na_tabela = k >= 0 and out[k]["t"] == "pre"
        # dentro da tabela, só sai quem é texto corrido de margem a margem; fora dela, entra quem tem colunas ou é curta e recuada
        e_tabela = (not (recuo < 4 and len(cru) >= 90 and not coluna)) if na_tabela else (coluna or (recuo >= 4 and len(cru) < 90))
        if e_tabela:
            # bloco de tabela continua através de linhas em branco
            if k >= 0 and out[k]["t"] == "pre":
                del out[k + 1:]
                out[k]["x"] += "\n" + cru
            else:
                out.append({"t": "pre", "x": cru})
            continue
        s = cru.strip()
        ant = out[-1] if out else None
        if ant and ant["t"] == "p" and ant.get("aberto") and not re.match(r"^([A-Ea-e]\s*[-–)]|[IVX]+\s*[-–.)]|•|\d+\.)\s", s):
            ant["x"] = juntar(ant["x"], s)
        else:
            out.append({"t": "p", "x": s})
        # linha que chegou perto da margem direita continua no parágrafo seguinte
        out[-1]["aberto"] = len(cru) >= 95 and not s.endswith((":",))
    res = []
    for b in out:
        if b["t"] == "br":
            if res and res[-1][0] != "br":
                res.append(["br"])
            continue
        if b["t"] == "pre":  # tira o recuo comum, mantendo o alinhamento das colunas
            ls = b["x"].split("\n")
            m = min(len(x) - len(x.lstrip()) for x in ls if x.strip())
            b["x"] = "\n".join(x[m:] for x in ls)
        res.append([b["t"], b["x"]])
    while res and res[-1][0] == "br":
        res.pop()
    while res and res[0][0] == "br":
        res.pop(0)
    return res


def ler_simulado(pdf: Path, n: int) -> dict:
    pags = paginas(pdf)
    figs = figuras(pdf)
    sim = {"id": f"dpcba-{n}", "titulo": f"Simulado {n} — DPC-BA", "fonte": "Projeto em Delta (material de terceiro, uso pessoal)",
           "textos": [], "questoes": []}
    bloco = disc = None
    estado = None  # None | 'texto' | 'tema' | 'enun' | 'alt' | 'com'
    q = None
    tb = None
    def fecha():
        nonlocal q
        if q:
            sim["questoes"].append(q)
        q = None

    for ip, pag in enumerate(pags, start=1):
        for l in pag:
            s = l.strip()
            if s.startswith("BLOCO "):
                fecha(); bloco = s; estado = None; continue
            if s in DISCIPLINAS:
                fecha(); disc = s; estado = None; continue
            m = TEXTO_BASE.match(l)
            if m:
                fecha()
                tb = {"de": int(m.group(1)), "ate": int(m.group(2)), "linhas": [l]}
                sim["textos"].append(tb); estado = "texto"; continue
            if s.startswith("Tema:"):
                fecha()
                q = {"tema": s[5:].strip(), "disc": disc, "bloco": bloco, "pag": ip, "enun": [], "alts": {}, "com": [], "gab": None, "anulada": False}
                estado = "tema"; continue
            if estado == "texto":
                tb["linhas"].append(l); continue
            if q is None:
                continue
            if estado == "tema":
                m = CAB_Q.match(l)
                if m:
                    q["n"] = int(m.group(1)); q["origem"] = m.group(2).strip()
                    if m.group(3).strip():
                        q["enun"].append(m.group(3))
                    estado = "enun"
                else:
                    q["tema"] = juntar(q["tema"], s)
                continue
            if l == "§COMENTARIOS§":
                estado = "com"; continue
            if estado in ("enun", "alt"):
                m = ALT.match(l)
                if m and (estado == "alt" or m.group(1) == "A"):
                    q["alts"][m.group(1)] = m.group(2).strip(); q["_ult"] = m.group(1); estado = "alt"; continue
                if estado == "alt":
                    if s:
                        q["alts"][q["_ult"]] = juntar(q["alts"][q["_ult"]], s)
                else:
                    q["enun"].append(l)
                continue
            if estado == "com":
                g = GAB.search(l)
                if g and q["gab"] is None:
                    q["gab"] = g.group(1).upper(); q["anulada"] = bool(g.group(2))
                    resto = (l[:g.start()] + l[g.end():]).rstrip()
                    if resto.strip():
                        q["com"].append(resto)
                    continue
                q["com"].append(re.sub(r"^\s*Comentários:\s*", "", l) if not q["com"] else l)
                continue
    fecha()

    for q in sim["questoes"]:
        q.pop("_ult", None)
        ajuste = AJUSTES.get((n, q.get("n")))
        if ajuste == "alt-A-sem-letra":
            # no PDF a 1ª alternativa veio sem "A)" e as demais rotuladas A–D; comentário e gabarito contam a–e
            corte = max(i for i, l in enumerate(q["enun"]) if re.search(r"assinale a alternativa", l, re.I)) + 1
            primeira = " ".join(l.strip() for l in q["enun"][corte:] if l.strip())
            q["enun"] = q["enun"][:corte]
            antigas = [q["alts"][k] for k in "ABCD"]
            q["alts"] = dict(zip("ABCDE", [primeira] + antigas))
            q["nota"] = ("Ajuste da importação: no PDF a primeira alternativa veio sem a letra e as demais rotuladas de A a D; "
                         "aqui a ordem segue o comentário e o gabarito, que contam de a) a e).")
        if (n, q.get("n")) in ATUALIZACOES:
            nivel, texto = ATUALIZACOES[(n, q.get("n"))]
            q["atual"] = {"nivel": nivel, "texto": texto, "em": "04/11/2026"}
        q["enun"] = blocos(q["enun"])
        q["com"] = blocos(q["com"])
        for (sn, pg), (qn, onde) in FIGURAS.items():
            if sn == n and q.get("n") == qn:
                q["fig"] = {"onde": onde, "src": figs[pg][0]}
    for t in sim["textos"]:
        t["blocos"] = blocos(t.pop("linhas"))
    return sim


def conferir(sim: dict) -> list[str]:
    erros = []
    ns = [q.get("n") for q in sim["questoes"]]
    if ns != list(range(1, 101)):
        erros.append(f"{sim['id']}: numeração não é 1..100 ({len(ns)} questões)")
    for q in sim["questoes"]:
        if sorted(q["alts"]) != list("ABCDE"):
            erros.append(f"{sim['id']} q{q.get('n')}: alternativas {sorted(q['alts'])}")
        if q["gab"] not in list("ABCDE"):
            erros.append(f"{sim['id']} q{q.get('n')}: sem gabarito")
        if not q["com"]:
            erros.append(f"{sim['id']} q{q.get('n')}: sem comentário")
        if not q["disc"]:
            erros.append(f"{sim['id']} q{q.get('n')}: sem disciplina")
    return erros


def main() -> None:
    sys.stdout.reconfigure(encoding="utf-8")
    pasta = Path(sys.argv[1]) if len(sys.argv) > 1 else PASTA_PADRAO
    sims, erros = [], []
    for n in (1, 2, 3, 4):
        pdf = pdf_do_simulado(pasta, n)
        s = ler_simulado(pdf, n)
        erros += conferir(s)
        sims.append(s)
        anul = sum(q["anulada"] for q in s["questoes"])
        print(f"Simulado {n}: {len(s['questoes'])} questões, {len(s['textos'])} textos-base, {anul} anulada(s), "
              f"{sum('fig' in q for q in s['questoes'])} com figura  ← {pdf.name}")
    js = ("/* GERADO por ferramentas/importar_simulados_delta.py — NÃO edite à mão e NÃO suba ao Git (D-002, D-017).\n"
          "   Questões objetivas comentadas dos Simulados DPC-BA do Projeto em Delta: material de terceiro, uso pessoal. */\n"
          "const SIMULADOS = " + json.dumps(sims, ensure_ascii=False) + ";\n")
    if CPF.search(js):
        sys.exit("ERRO: sobrou número com forma de CPF no resultado; nada foi gravado")
    if "</script" in js.lower():
        sys.exit("ERRO: o texto contém </script")
    if erros:
        print("\n".join("  ⚠️ " + e for e in erros))
        sys.exit(f"ERRO: {len(erros)} problema(s) de estrutura; nada foi gravado")
    SAIDA.write_text(js, encoding="utf-8", newline="\n")
    print(f"gravado: {SAIDA} · {SAIDA.stat().st_size:,} bytes".replace(",", "."))


if __name__ == "__main__":
    main()
