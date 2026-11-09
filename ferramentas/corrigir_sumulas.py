"""Correções do assets/sumulas.json conferidas na FONTE OFICIAL (STF e STJ), uma a uma, com registro.

Por que existe: o assets/sumulas.json (fora do Git) sai do ferramentas/construir_base.py, que o extrai de um
material de curso em PDF. A extração trouxe texto e datas divergentes do oficial (medido pelas frentes dos
módulos em 07/11/2026). Ninguém corrige à mão: cada troca está na lista CORRECOES abaixo, com o valor de antes, o
de depois, a URL oficial e a data da conferência, e é gravada também DENTRO da súmula corrigida (campo
"correcoes"), para quem ler o JSON saber de onde veio cada palavra. O construir_base.py chama este script depois
de regravar o sumulas.json, para a correção não se perder numa nova extração.

Uso:
  python ferramentas/corrigir_sumulas.py              aplica as correções (idempotente) e diz o que fez
  python ferramentas/corrigir_sumulas.py --estado     só confere: sai 1 se há correção pendente ou divergente,
                                                      2 se o sumulas.json não existe (fica fora do Git)
  python ferramentas/corrigir_sumulas.py --comparar-oficial STF.pdf STJ.pdf
                                                      compara TODAS as súmulas STF/STJ da base com os PDFs
                                                      oficiais e lista as divergências (não corrige nada)
  python ferramentas/corrigir_sumulas.py --autoteste  REGRA CINCO: prova que aplica, que não aplica duas vezes e
                                                      que RECUSA quando o valor de antes não confere
Saídas: 0 ok · 1 pendência, divergência ou falha · 2 pulado (sem a base).

O que NÃO se corrige aqui sem conferência oficial (REGRA ZERO): as outras súmulas com data colada no texto ou
tema trocado na extração. O --comparar-oficial mede essa classe; o que ele achar entra nesta lista só depois de
conferido, súmula a súmula.
"""

from __future__ import annotations

import copy
import json
import re
import sys
from pathlib import Path

RAIZ = Path(__file__).resolve().parent.parent
SUMULAS = RAIZ / "assets" / "sumulas.json"

STF_PDF = (
    "https://www.stf.jus.br/arquivo/cms/jurisprudenciaSumula/anexo/Enunciados_Sumulas_STF_1_a_736_Completo.pdf"
)
STJ_VERBETES = "https://scon.stj.jus.br/docs_internet/VerbetesSTJ.pdf"
STJ_REVISTA = "https://scon.stj.jus.br/docs_internet/revista/eletronica/stj-revista-sumulas-{}_capSumulas{}.pdf"
CONFERIDO = "07/11/2026"

# (id, campo, antes, depois, fonte oficial, o que a fonte diz)
CORRECOES: list[tuple[str, str, object, object, str, str]] = [
    (
        "SUM-STF-610", "texto",
        "Há crime de latrocínio, quando o homicídio se consuma, ainda que não se realize o agente a subtração de "
        "bens da vítima.",
        "Há crime de latrocínio, quando o homicídio se consuma, ainda que não realize o agente a subtração de bens "
        "da vítima.",
        STF_PDF, "Súmula 610: enunciado; Sessão Plenária de 17/10/1984; DJ de 29/10/1984",
    ),
    ("SUM-STF-610", "aprovada_em", None, "17/10/1984", STF_PDF, "Data de Aprovação: Sessão Plenária de 17/10/1984"),
    ("SUM-STF-610", "publicada_em", None, "29/10/1984", STF_PDF, "Fonte de Publicação: DJ de 29/10/1984, p. 18114"),
    (
        "SUM-STF-603", "texto",
        "A competência para o processo e julgamento de latrocínio é do juiz singular e não do Tribunal do Júri.",
        "A competência para o processo e julgamento de latrocínio é do Juiz singular e não do Tribunal do Júri.",
        STF_PDF, "Súmula 603: enunciado com 'Juiz' maiúsculo",
    ),
    ("SUM-STF-603", "aprovada_em", None, "17/10/1984", STF_PDF, "Data de Aprovação: Sessão Plenária de 17/10/1984"),
    ("SUM-STF-603", "publicada_em", None, "29/10/1984", STF_PDF, "Fonte de Publicação: DJ de 29/10/1984, p. 18113"),
    (
        "SUM-STJ-502", "texto",
        "Presentes a materialidade e a autoria, afigura-se típica, em relação ao crime previsto no artigo 184, "
        "parágrafo 2º, do Código Penal, a conduta de expor à venda CDs e DVDs piratas.",
        "Presentes a materialidade e a autoria, afigura-se típica, em relação ao crime previsto no art. 184, § 2º, "
        "do CP, a conduta de expor à venda CDs e DVDs piratas.",
        STJ_VERBETES, "Súmula 502: enunciado (a lista oficial não traz a data)",
    ),
    (
        "SUM-STJ-441", "texto",
        "A falta grave não interrompe o prazo para obtenção do livramento condicional. - Aprovada em 28/04/2010, "
        "Dje 13/05/2010.",
        "A falta grave não interrompe o prazo para obtenção de livramento condicional.",
        STJ_VERBETES, "Súmula 441: enunciado; a data que vinha colada no texto saiu (não conferida em fonte oficial)",
    ),
    ("SUM-STJ-441", "tema", "compatível com a CF/88.", "Livramento condicional", STJ_VERBETES,
     "tema trocado na extração (era o fim do comentário anterior); o tema sai do enunciado oficial"),
    (
        "SUM-STJ-659", "texto",
        "A fração de aumento em razão da prática de crime continuado deve ser fixada de acordo com o número de "
        "delitos cometidos, aplicando-se 1/6 pela prática de duas infrações, 1/5 para três, ¼ para quatro, 1/3 para "
        "cinco, ½ para seis e 2/3 para sete ou mais infrações. (TERCEIRA SEÇÃO, julgado em 13/9/2023, Dje 8/9/2023)",
        "A fração de aumento em razão da prática de crime continuado deve ser fixada de acordo com o número de "
        "delitos cometidos, aplicando-se 1/6 pela prática de duas infrações, 1/5 para três, 1/4 para quatro, 1/3 "
        "para cinco, 1/2 para seis e 2/3 para sete ou mais infrações.",
        STJ_REVISTA.format("2023_49", 659), "Súmula 659: enunciado ('1/4' e '1/2', não '¼' e '½'); a data colada saiu",
    ),
    ("SUM-STJ-659", "aprovada_em", None, "13/09/2023", STJ_REVISTA.format("2023_49", 659),
     "Terceira Seção, em 13.09.2023"),
    ("SUM-STJ-659", "publicada_em", None, "18/09/2023", STJ_REVISTA.format("2023_49", 659),
     "DJe 18.09.2023 (a extração dizia 'Dje 8/9/2023')"),
    ("SUM-STJ-645", "tema", "em 8/11/2023, Dje de 13/11/2023)", "Fraude à licitação", STJ_REVISTA.format("2023_49", 645),
     "tema trocado na extração (era a data de outra súmula); o tema sai do enunciado oficial"),
    ("SUM-STJ-645", "aprovada_em", None, "10/02/2021", STJ_REVISTA.format("2023_49", 645),
     "Terceira Seção, em 10.2.2021"),
    ("SUM-STJ-645", "publicada_em", None, "18/02/2021", STJ_REVISTA.format("2023_49", 645), "DJe 18.2.2021"),
    ("SUM-STJ-641", "tema", "em 8/11/2023, Dje de 13/11/2023)", "Processo administrativo disciplinar",
     STJ_REVISTA.format("2021_48", 641),
     "tema trocado na extração (era a data de outra súmula); o tema sai do enunciado oficial"),
    ("SUM-STJ-641", "aprovada_em", None, "18/02/2020", STJ_REVISTA.format("2021_48", 641),
     "Primeira Seção, em 18.2.2020"),
    ("SUM-STJ-641", "publicada_em", None, "19/02/2020", STJ_REVISTA.format("2021_48", 641), "DJe 19.2.2020"),
]


def aplicar(base: dict, correcoes=CORRECOES) -> tuple[list[str], list[str], list[str]]:
    """Aplica na base (em memória). Devolve (aplicadas, já_estavam, divergentes)."""
    feitas, ja, diverg = [], [], []
    for sid, campo, antes, depois, fonte, diz in correcoes:
        s = base.get(sid)
        rot = f"{sid}.{campo}"
        if s is None:
            diverg.append(f"{rot}: a súmula não está na base")
            continue
        atual = s.get(campo)
        if atual == depois:
            ja.append(rot)
            continue
        if atual != antes:
            diverg.append(f"{rot}: o valor atual não é o 'antes' registrado — não troco às cegas: {str(atual)[:90]!r}")
            continue
        s[campo] = depois
        reg = {"campo": campo, "antes": antes, "depois": depois, "fonte": fonte, "diz": diz, "conferido_em": CONFERIDO}
        s.setdefault("correcoes", []).append(reg)
        feitas.append(rot)
    return feitas, ja, diverg


def gravar(base: dict, caminho: Path = SUMULAS) -> None:
    caminho.write_text(json.dumps(base, ensure_ascii=False, indent=0), "utf8")


# ------------------------------------------------------------------ comparação com os PDFs oficiais
def _norm(t: str) -> str:
    t = t.replace("¼", "1/4").replace("½", "1/2").replace("¾", "3/4")
    t = re.sub(r"[\"“”'‘’]", "", t)
    t = re.sub(r"[‐‑‒–—―−]", "-", t)
    t = re.sub(r"\bfi\s+(?=[a-z])", "fi", t)
    return re.sub(r"\s+", " ", t).strip().rstrip(".")


def _oficiais(stf_pdf: Path, stj_pdf: Path) -> dict:
    import pymupdf

    out = {}
    stf = "\n".join(p.get_text() for p in pymupdf.open(stf_pdf))
    for m in re.finditer(r"SÚMULA (\d+)\s*\n(.+?)\n\s*\n?\s*Data de Aprovação", stf, re.S):
        out[f"SUM-STF-{m[1]}"] = m[2]
    stj = "\n".join(p.get_text() for p in pymupdf.open(stj_pdf))
    stj = re.sub(r"scon\.stj\.jus\.br/SCON/\s*\n\d+/\d+\s*\n", "\n", stj)
    for m in re.finditer(r"SÚMULA (\d+)\s*\nVEJA MAIS\s*\n(.+?)(?=\nSÚMULA \d+\s*\nVEJA MAIS|\Z)", stj, re.S):
        out.setdefault(f"SUM-STJ-{m[1]}", m[2])
    return out


def comparar(stf_pdf: Path, stj_pdf: Path) -> int:
    base = json.loads(SUMULAS.read_text("utf8"))
    of = _oficiais(stf_pdf, stj_pdf)
    iguais, difs, fora = 0, [], []
    for sid, s in sorted(base.items()):
        if sid.startswith("SV-"):
            continue
        o = of.get(sid)
        if o is None:
            fora.append(sid)
        elif _norm(o) == _norm(s.get("texto", "")):
            iguais += 1
        else:
            difs.append((sid, _norm(s.get("texto", "")), _norm(o)))
    print(f"  súmulas STF/STJ na base: {iguais + len(difs) + len(fora)} · iguais ao oficial: {iguais} · "
          f"divergentes: {len(difs)} · não achadas no PDF oficial: {len(fora)}")
    for sid, b, o in difs:
        print(f"  ≠ {sid}\n      base:    {b[:200]}\n      oficial: {o[:200]}")
    if fora:
        print("  não achadas: " + ", ".join(fora))
    print("  (súmulas vinculantes não comparadas: o PDF do STF usado aqui é o das súmulas comuns)")
    return 1 if difs or fora else 0


# ------------------------------------------------------------------ autoteste
def autoteste() -> int:
    base0 = {
        "SUM-STF-610": {"texto": "Há crime de latrocínio, quando o homicídio se consuma, ainda que não se realize o "
                                 "agente a subtração de bens da vítima."},
        "SUM-STJ-645": {"tema": "em 8/11/2023, Dje de 13/11/2023)", "texto": "O crime de fraude à licitação é formal"},
    }
    corr = [c for c in CORRECOES if c[0] in base0]
    falhas = 0

    def caso(nome, ok):
        nonlocal falhas
        falhas += not ok
        print(f"  {'✅' if ok else '❌'} {nome}")

    b = copy.deepcopy(base0)
    feitas, ja, div = aplicar(b, corr)
    caso("aplica as correções registradas (STF 610: 'não realize o agente'; STJ 645: tema e datas)",
         len(feitas) == len(corr) and not div and "não realize o agente" in b["SUM-STF-610"]["texto"]
         and b["SUM-STJ-645"]["aprovada_em"] == "10/02/2021")
    caso("cada troca fica registrada na súmula, com a URL oficial",
         all(r["fonte"].startswith("https://") for r in b["SUM-STF-610"]["correcoes"]))
    feitas2, ja2, div2 = aplicar(b, corr)
    caso("rodar de novo não aplica duas vezes (idempotente)", not feitas2 and len(ja2) == len(corr) and not div2)
    b3 = copy.deepcopy(base0)
    b3["SUM-STF-610"]["texto"] = "Outro texto qualquer."
    _, _, div3 = aplicar(b3, corr)
    caso("valor de antes que não confere é RECUSADO (não troca às cegas)",
         any("SUM-STF-610.texto" in d for d in div3) and b3["SUM-STF-610"]["texto"] == "Outro texto qualquer.")
    _, _, div4 = aplicar({}, corr)
    caso("súmula ausente da base é acusada", len(div4) == len(corr))
    # o defeito antigo: o texto de antes (extração) tem de ser acusado como pendente pelo --estado
    caso("o texto antigo errado ('não se realize o agente') conta como pendência",
         "não se realize o agente" in base0["SUM-STF-610"]["texto"] and estado(base0, corr, calado=True) == 1)
    caso("a base corrigida passa no --estado", estado(b, corr, calado=True) == 0)
    print("[AUTOTESTE OK]" if not falhas else f"[AUTOTESTE FALHOU] {falhas} caso(s)")
    return 1 if falhas else 0


def estado(base: dict, correcoes=CORRECOES, calado=False) -> int:
    b = copy.deepcopy(base)
    feitas, ja, div = aplicar(b, correcoes)
    if not calado:
        print(f"  correções registradas: {len(correcoes)} · aplicadas: {len(ja)} · pendentes: {len(feitas)} · "
              f"divergentes: {len(div)}")
        for x in feitas:
            print(f"  ⏳ pendente: {x} (rode python ferramentas/corrigir_sumulas.py)")
        for x in div:
            print(f"  ❌ {x}")
    return 1 if feitas or div else 0


def main(argv) -> int:
    sys.stdout.reconfigure(encoding="utf-8")
    if "--autoteste" in argv:
        return autoteste()
    if not SUMULAS.exists():
        print(f"  pulada: {SUMULAS.relative_to(RAIZ)} não existe nesta máquina (fica fora do Git)")
        return 2
    if "--comparar-oficial" in argv:
        i = argv.index("--comparar-oficial")
        return comparar(Path(argv[i + 1]), Path(argv[i + 2]))
    base = json.loads(SUMULAS.read_text("utf8"))
    if "--estado" in argv:
        return estado(base)
    feitas, ja, div = aplicar(base)
    if feitas:
        gravar(base)
    for x in feitas:
        print(f"  ✅ corrigida: {x}")
    print(f"  {len(feitas)} aplicada(s) agora · {len(ja)} já estavam · {len(div)} divergente(s)")
    for x in div:
        print(f"  ❌ {x}")
    return 1 if div else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
