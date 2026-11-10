"""Monta discursiva/revisao_nfpss.js (aba 📚 Revisão) a partir das assertivas C/E de cada bloco do material.

O material de revisão é de TERCEIRO (anexado pelo titular em 09/11/2026): texto, blocos e assertivas ficam só no
disco, em revisao/material/<nome>/ (fora do Git), e o .js gerado também (data-local: não vai no arquivo de envio).
Só este montador e o verificador (validar_revisao_material.py) são autorais e versionados.

Entrada: <pasta>/blocos/<BLOCO>.txt e <pasta>/itens/<BLOCO>_NN.json, BLOCO = sigla da disciplina + nº (CPC01).
Recusa montar se algum bloco não passar no verificador — cobertura provada ou nada.

Uso: python -I ferramentas/montar_revisao_material.py [<pasta>]   (padrão: revisao/material/nfpss)
     python -I ferramentas/montar_revisao_material.py --autoteste
"""

from __future__ import annotations

import json
import re
import sys
import tempfile
from pathlib import Path

RAIZ = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(Path(__file__).resolve().parent))
import validar_revisao_material as V  # noqa: E402

PADRAO = RAIZ / "revisao" / "material" / "nfpss"
SAIDA = RAIZ / "discursiva" / "revisao_nfpss.js"
NOMES = {"CPC": "Processo Civil", "TRI": "Tributário", "CON": "Constitucional", "AMB": "Ambiental",
         "ADM": "Administrativo", "PEN": "Penal", "CPP": "Processo Penal", "LPE": "Legislação Penal Especial",
         "CRI": "Criminologia", "MLE": "Medicina Legal", "CIV": "Civil", "HUM": "Direitos Humanos",
         "EMP": "Empresarial", "ELE": "Eleitoral", "TRA": "Trabalho", "PRT": "Processo do Trabalho",
         "INF": "Estatuto da Criança e do Adolescente", "PRV": "Previdenciário", "FIN": "Financeiro",
         "IGR": "Igualdade Racial e de Gênero", "LEG": "Legislação Geral"}  # Parte 3, 10/11/2026


def _slug(s: str) -> str:
    s = re.sub(r"[^\w]+", "-", s.lower()).strip("-")
    return s[:60] or "secao"


CAMPOS_AP = ("correcao", "aprofundamento", "exemplo", "memorize")


def _aprofundamento(pasta: Path) -> dict:
    """Camada de aprofundamento (09/11/2026), por id; aprovada por ferramentas/validar_aprofundamento.py."""
    out: dict = {}
    for arq in sorted((pasta / "aprofundar").glob("*.json")):
        out.update(json.loads(arq.read_text(encoding="utf-8")))
    return out


def _item(bloco: str, k: int, it: dict, pid: str, ap: dict | None = None) -> dict:
    c = {"resumo": it["resumo"]}
    for campo in ("regra", "pegadinha", "divergencia"):
        if it.get(campo):
            c[campo] = it[campo]
    if it.get("juris"):
        c["juris"] = [{"tribunal": "", "fonte": "", "texto": it["juris"]}]
    for campo in CAMPOS_AP:
        if (ap or {}).get(f"{bloco}-{k:03d}", {}).get(campo):
            c[campo] = ap[f"{bloco}-{k:03d}"][campo]
    return {"id": f"{bloco}-{k:03d}", "ponto": pid, "tema": it.get("tema", ""), "pag": int(it["pag"]),
            "assertiva": it["assertiva"], "gabarito": it["gabarito"], "comentario": c}


def montar(pasta: Path) -> tuple[dict, list[str]]:
    """Devolve (dados por disciplina, erros). Com erro em qualquer bloco, os dados não servem."""
    erros: list[str] = []
    discs: dict[str, dict] = {}
    ap = _aprofundamento(pasta)
    for txt in sorted((pasta / "blocos").glob("*.txt")):
        bloco = txt.stem
        m = re.fullmatch(r"([A-Z]{2,4})(\d{2})", bloco)
        if not m:
            continue
        sigla, num = m.group(1), int(m.group(2))
        arqs = sorted((pasta / "itens").glob(f"{bloco}_*.json"))
        if not arqs:
            erros.append(f"{bloco}: sem assertivas")
            continue
        itens = []
        for a in arqs:
            itens += json.loads(a.read_text(encoding="utf-8"))["itens"]
        texto = txt.read_text(encoding="utf-8")
        e, *_ = V.validar(texto, {"itens": itens}, bloco)
        erros += [f"{bloco}: {x}" for x in e]
        D = discs.setdefault(sigla, {"disciplina": NOMES.get(sigla, sigla), "pontos": [], "rodadas": [], "_ids": {}})
        convertidos = []
        for k, it in enumerate(itens, 1):
            titulo = it["ponto"].strip()
            if titulo not in D["_ids"]:
                base, n = _slug(titulo), 2
                pid = base
                while pid in D["_ids"].values():
                    pid, n = f"{base}-{n}", n + 1
                D["_ids"][titulo] = pid
                D["pontos"].append({"id": pid, "titulo": titulo})
            convertidos.append(_item(bloco, k, it, D["_ids"][titulo], ap))
        pgs = [int(p) for p in re.findall(r"\[\[p\.(\d+)\]\]", texto)]
        faixa = f"p. {pgs[0]}–{pgs[-1]}" if pgs else ""
        D["rodadas"].append({"n": num, "titulo": f"Bloco {num} · {faixa}".strip(" ·"), "itens": convertidos})
    for D in discs.values():
        D.pop("_ids")
        tot = sum(len(r["itens"]) for r in D["rodadas"])
        D["fontes"] = f"{tot} assertivas, cobertura do material provada página a página e julgado a julgado."
    return discs, erros


def gravar(discs: dict, saida: Path) -> None:
    corpo = json.dumps(discs, ensure_ascii=False, separators=(",", ":"))
    saida.write_text(
        "/* GERADO por ferramentas/montar_revisao_material.py — NÃO edite à mão e NÃO suba ao Git:\n"
        "   assertivas sobre material de revisão de terceiro, uso pessoal do titular (D-022). */\n"
        f"window.REVISAO=Object.assign(window.REVISAO||{{}},{corpo});\n", encoding="utf-8")


def autoteste() -> int:
    falhas = 0
    with tempfile.TemporaryDirectory() as t:
        p = Path(t)
        (p / "blocos").mkdir()
        (p / "itens").mkdir()
        (p / "blocos" / "CPC01.txt").write_text("[[p.3]]\n" + "x" * 300 + " Info 1.234\n", encoding="utf-8")
        it = [{"ponto": "Tutela", "tema": "T", "pag": 3, "gabarito": g, "resumo": "Info 1234.",
               "assertiva": f"Assertiva de teste {k} com tamanho suficiente para passar."} for k, g in enumerate("CE")]
        (p / "itens" / "CPC01_01.json").write_text(json.dumps({"itens": it}), encoding="utf-8")
        d, e = montar(p)
        ok = not e and d["CPC"]["rodadas"][0]["itens"][1]["id"] == "CPC01-002" and d["CPC"]["pontos"][0]["id"] == "tutela"
        falhas += not ok
        print(f"  {'✅' if ok else '❌'} monta o bloco bom (ids e seções)")
        it[0]["resumo"] = "sem número"
        it[1]["resumo"] = "idem"
        (p / "itens" / "CPC01_01.json").write_text(json.dumps({"itens": it}), encoding="utf-8")
        _, e = montar(p)
        ok = any("1234" in x for x in e)
        falhas += not ok
        print(f"  {'✅' if ok else '❌'} recusa bloco com julgado perdido")
        (p / "blocos" / "TRI01.txt").write_text("[[p.9]]\n" + "y" * 300, encoding="utf-8")
        _, e = montar(p)
        ok = any("TRI01: sem assertivas" in x for x in e)
        falhas += not ok
        print(f"  {'✅' if ok else '❌'} recusa bloco sem assertivas")
    return 1 if falhas else 0


def main() -> int:
    sys.stdout.reconfigure(encoding="utf-8")
    if "--autoteste" in sys.argv:
        return autoteste()
    args = [a for a in sys.argv[1:] if not a.startswith("--")]
    pasta = Path(args[0]) if args else PADRAO
    if not (pasta / "blocos").is_dir():
        print(f"  sem o material em {pasta} (fica só na máquina do titular): pulado")
        return 2
    discs, erros = montar(pasta)
    if erros:
        print(f"  ❌ {len(erros)} problema(s); nada gravado:")
        for x in erros[:30]:
            print("     ", x)
        return 1
    gravar(discs, SAIDA)
    for k, D in discs.items():
        n = sum(len(r["itens"]) for r in D["rodadas"])
        print(f"  {k} {D['disciplina']}: {len(D['rodadas'])} blocos, {n} assertivas, {len(D['pontos'])} seções")
    kb = f"{SAIDA.stat().st_size / 1024:,.1f}".replace(",", "X").replace(".", ",").replace("X", ".")
    print(f"  ✅ gravado {SAIDA.relative_to(RAIZ).as_posix()} ({kb} KB)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
