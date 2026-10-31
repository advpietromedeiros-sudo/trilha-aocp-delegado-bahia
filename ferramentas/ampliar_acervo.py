#!/usr/bin/env python3
"""ampliar_acervo.py — acrescenta ao índice de páginas (RAG) o acervo grande da pasta DELEGADO BA.

Por que existe (31/10/2026, docs/VIABILIDADE_BLOCOS_30.md): o gerador só lia 744 páginas de 26
arquivos; 7.034 páginas de resumos, informativos e súmulas da pasta DELEGADO BA não entravam. O
`construir_base.py` reconstrói TUDO a partir de uma pasta de PDFs renomeados que não existe nesta
máquina — por isso esta ferramenta é ADITIVA: não toca nas linhas que já estão no índice, só
acrescenta (ou substitui as de mesmo rótulo, para poder rodar de novo).

- Mesmo formato de linha do `construir_base.py` (file, page, text, posterior, disciplinas) e o mesmo
  filtro de marca d'água: a linha com o CPF do licenciado NÃO entra no índice.
- Os arquivos "RESUMO DESTACADO-DELEGADO PCPR-1..4.pdf" são ZIP renomeados: os PDFs de dentro são
  lidos direto do ZIP. PCPR-3 e PCPR-4 só entram se NÃO forem cópia do PCPR-2 (mesma lista de nomes).
- Antes de gravar, guarda o índice anterior em `.scratch/` (dado não se apaga, §F17).
- Trilha por arquivo (§F14): páginas lidas × páginas indexadas, impressa e gravada em
  `.scratch/ampliar_acervo_relatorio.json`.

Material de terceiro: o índice (`assets/fontes_paginas.json`) é local e fica FORA do Git (D-002).

Uso: python ferramentas/ampliar_acervo.py [PASTA_DELEGADO_BA] [--simular]
"""

from __future__ import annotations

import io
import json
import os
import pathlib
import re
import shutil
import subprocess
import sys
import tempfile
import zipfile
from datetime import datetime

RAIZ = pathlib.Path(__file__).resolve().parent.parent
INDICE = RAIZ / "assets" / "fontes_paginas.json"
PADRAO = pathlib.Path.home() / "OneDrive" / "Área de Trabalho" / "DELEGADO BA"

# Disciplinas com o nome EXATO do items.json (o servidor filtra por igualdade).
PEN, PP = "DIREITO PENAL", "DIREITO PROCESSUAL PENAL"
ADM, CON = "DIREITO ADMINISTRATIVO", "DIREITO CONSTITUCIONAL"
LPE = "LEGISLAÇÃO PENAL E PROCESSUAL PENAL EXTRAVAGANTE"
DH = CON + "|PROMOÇÃO DA IGUALDADE RACIAL E DE GÊNERO"

# arquivo da pasta -> disciplinas ('*' = todas). posterior=False: ver o aviso no relatório.
ARQUIVOS: dict[str, str] = {
    "RESUMO DESTACADO - DELEGADO PCPR - DIREITO ADMINISTRATIVO.pdf": ADM,
    "RESUMO DESTACADO - DELEGADO PCPR - DIREITO CONSTITUCIONAL.pdf": CON,
    "RESUMO DESTACADO - DELEGADO PCPR - DIREITO PENAL - PARTE ESPECIAL.pdf": PEN,
    "RESUMO DESTACADO - DELEGADO PCPR - DIREITO PENAL - PARTE GERAL.pdf": PEN,
    "RESUMO DESTACADO - DELEGADO PCPR - DIREITO PROCESSUAL PENAL.pdf": PP,
    "RESUMO DESTACADO - DELEGADO PCPR - DIREITOS HUMANOS.pdf": DH,
    "RESUMO DESTACADO - DELEGADO PCPR - LEGISLAÇÃO PENAL EXTRAVAGANTE.pdf": LPE,
    "RESUMO DESTACADO-CRIMINOLOGIA.pdf": "CRIMINOLOGIA",
    "RESUMO DESTACADO-MEDICINA LEGAL.pdf": "MEDICINA LEGAL",
    "JURISPRUDÊNCIA-INFORMATIVOS 2023.pdf": "*",
    "JURISPRUDÊNCIA-INFORMATIVOS 2024.pdf": "*",
    "JURISPRUDÊNCIA-INFORMATIVOS 2025.pdf": "*",
    "JURISPRUDÊNCIA-INFORMATIVOS 2026.pdf": "*",
    "JURISPRUDÊNCIA-SÚMULAS STF, STJ e TSE.pdf": "*",
    "JURISPRUDÊNCIA-TESES COM REPERCUSSÃO GERAL.pdf": "*",
    "JURISPRUDÊNCIA-TESES FIXADAS EM SEDE DE RECURSO REPETITIVO.pdf": "*",
}
# ZIP renomeado -> disciplinas dos PDFs de dentro
ZIPS: dict[str, str] = {
    "RESUMO DESTACADO-DELEGADO PCPR-1.pdf": LPE,
    "RESUMO DESTACADO-DELEGADO PCPR-2.pdf": PEN,
    "RESUMO DESTACADO-DELEGADO PCPR-3.pdf": PEN,
    "RESUMO DESTACADO-DELEGADO PCPR-4.pdf": PEN,
}

# O MESMO filtro do construir_base.py: linha com 11 dígitos seguidos ou CPF formatado sai.
WATERMARK = re.compile(r"^.*\b\d{11}\b.*$|^.*\d{3}\.\d{3}\.\d{3}-\d{2}.*$")


def _pdftotext() -> str:
    exe = os.environ.get("PDFTOTEXT") or shutil.which("pdftotext")
    if not exe:
        sys.exit("pdftotext não encontrado: instale o Poppler ou defina PDFTOTEXT com o caminho.")
    return exe


def paginas(pdf: pathlib.Path, exe: str) -> list[str]:
    out = subprocess.run([exe, "-enc", "UTF-8", str(pdf), "-"], capture_output=True, check=True)
    return out.stdout.decode("utf8", "replace").split("\f")


def linhas(rotulo: str, disc: str, pags: list[str]) -> list[dict]:
    rows = []
    for pno, pg in enumerate(pags, 1):
        ls = [
            s for s in (ln.strip() for ln in pg.splitlines())
            if s and not WATERMARK.match(s) and not re.fullmatch(r"\d{1,3}", s)
        ]
        txt = re.sub(r"[ \t]+", " ", "\n".join(ls)).strip()
        if len(txt) < 120:  # mesmo corte do construir_base.py: página quase vazia não ajuda a busca
            continue
        rows.append({"file": rotulo, "page": pno, "text": txt, "posterior": False, "disciplinas": disc})
    return rows


def main() -> int:
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8")  # §A7
    args = [a for a in sys.argv[1:] if not a.startswith("--")]
    simular = "--simular" in sys.argv
    pasta = pathlib.Path(args[0]) if args else PADRAO
    if not pasta.is_dir():
        print(f"❌ pasta não encontrada: {pasta}")
        return 1
    exe = _pdftotext()
    novas: list[dict] = []
    trilha: list[dict] = []

    for nome, disc in ARQUIVOS.items():
        f = pasta / nome
        if not f.exists():
            trilha.append({"arquivo": nome, "situacao": "AUSENTE"})
            print(f"  ⚠️ ausente: {nome}")
            continue
        pags = paginas(f, exe)
        rows = linhas(nome, disc, pags)
        novas += rows
        trilha.append({"arquivo": nome, "paginas_lidas": len(pags), "indexadas": len(rows)})
        print(f"  ✅ {len(rows):5} de {len(pags):5} páginas · {nome}")

    listas_zip: dict[str, list[str]] = {}
    with tempfile.TemporaryDirectory() as tmp:
        for zipnome, disc in ZIPS.items():
            z = pasta / zipnome
            if not z.exists():
                trilha.append({"arquivo": zipnome, "situacao": "AUSENTE"})
                print(f"  ⚠️ ausente: {zipnome}")
                continue
            with zipfile.ZipFile(z) as zf:
                membros = sorted(m for m in zf.namelist() if m.lower().endswith(".pdf"))
                copia_de = next((k for k, v in listas_zip.items() if v == membros), None)
                listas_zip[zipnome] = membros
                if copia_de:
                    trilha.append({"arquivo": zipnome, "situacao": f"cópia de {copia_de} — pulado"})
                    print(f"  ↺ pulado (mesma lista de {len(membros)} PDFs que {copia_de}): {zipnome}")
                    continue
                for m in membros:
                    alvo = pathlib.Path(tmp) / pathlib.Path(m).name
                    alvo.write_bytes(zf.read(m))
                    pags = paginas(alvo, exe)
                    rotulo = f"{zipnome.removesuffix('.pdf')} › {pathlib.Path(m).name}"
                    rows = linhas(rotulo, disc, pags)
                    novas += rows
                    trilha.append({"arquivo": rotulo, "paginas_lidas": len(pags), "indexadas": len(rows)})
                print(f"  ✅ ZIP {zipnome}: {len(membros)} PDFs")

    atual = json.loads(INDICE.read_text("utf8")) if INDICE.exists() else []
    rotulos_novos = {r["file"] for r in novas}
    mantidas = [r for r in atual if r["file"] not in rotulos_novos]
    final = mantidas + novas
    relatorio = {
        "em": datetime.now().strftime("%d/%m/%Y %H:%M"),
        "pasta": str(pasta),
        "indice_antes": len(atual),
        "mantidas": len(mantidas),
        "acrescentadas": len(novas),
        "indice_depois": len(final),
        "arquivos": trilha,
        "aviso": "INFORMATIVOS 2026 pode trazer julgados posteriores ao marco do edital (29/07/2026); "
                 "o prompt do servidor já manda não aplicar norma posterior.",
    }
    print(f"\n  índice: {len(atual)} → {len(final)} páginas "
          f"({len(mantidas)} mantidas + {len(novas)} do acervo ampliado)")
    if simular:
        print("  🧪 SIMULAÇÃO: nada foi gravado.")
        return 0
    scratch = RAIZ / ".scratch"
    scratch.mkdir(exist_ok=True)
    if INDICE.exists():
        copia = scratch / f"fontes_paginas.antes_{datetime.now():%Y%m%d_%H%M}.json"
        shutil.copy2(INDICE, copia)
        print(f"  cópia do índice anterior: {copia.relative_to(RAIZ).as_posix()}")
    INDICE.write_text(json.dumps(final, ensure_ascii=False), "utf8")
    (scratch / "ampliar_acervo_relatorio.json").write_text(
        json.dumps(relatorio, ensure_ascii=False, indent=1), "utf8")
    print("  ✅ índice gravado; relatório em .scratch/ampliar_acervo_relatorio.json")
    return 0


if __name__ == "__main__":
    sys.exit(main())
