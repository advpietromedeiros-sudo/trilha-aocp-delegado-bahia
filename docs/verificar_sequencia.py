#!/usr/bin/env python3
"""verificar_sequencia.py — registro numerado tem de estar em ordem (HARNESS §F62).

💥 Reincidência em 31/10/2026: a regra R4 do `0 HARNESS.md` entrou ANTES da R3 — a edição se
ancorou no início da linha seguinte. Foi achada a olho; agora é porta do portão.

Confere, em cada arquivo vigiado, que os identificadores `**<prefixo><n>` aparecem em ordem
crescente e sem buraco (1, 2, 3 …), e as decisões `D-00n` do DECISOES, idem.

Uso: python docs/verificar_sequencia.py [--autoteste]   (0 = em ordem, 1 = fora de ordem)
"""

from __future__ import annotations

import re
import sys
from pathlib import Path

RAIZ = Path(__file__).resolve().parent.parent

# (arquivo, regex que captura o número, descrição, contígua?)
# Contígua: 1, 2, 3 sem buraco (as regras R). Só crescente: buraco permitido (as decisões tomadas —
# a D-003 pode seguir aberta enquanto a D-004 já foi tomada), mas nunca fora de ordem.
VIGIADOS: list[tuple[str, str, str, bool]] = [
    ("0 Readme First/0 HARNESS.md", r"^- \*\*R(\d+) ", "regras do projeto R<n>", True),
    ("docs/DECISOES.md", r"^### D-(\d+) ", "decisões tomadas D-<n>", False),
    # 💥 31/10/2026: duas vezes na mesma tarefa a lista de tarefas ficou 1, 4, 5, 6 e depois 1, 3, 4
    # — renumerou-se só a primeira linha. §F47: consertar o caso não conserta a classe.
    ("0 Readme First/FAROL.md", r"^(\d+)\. ", "tarefas numeradas do FAROL", True),
]


def fora_de_ordem(numeros: list[int], contigua: bool = True) -> str | None:
    """Pura: devolve o defeito, ou None se em ordem. Lista vazia é válida."""
    for i in range(1, len(numeros)):
        anterior, atual = numeros[i - 1], numeros[i]
        if (contigua and atual != anterior + 1) or (not contigua and atual <= anterior):
            return f"depois de {anterior} veio {atual} (sequência: {numeros})"
    return None


def _autoteste() -> int:
    casos = [
        ([1, 2, 3, 4], True, False),
        ([1, 2, 4, 3], True, True),
        ([1, 3], True, True),
        ([], True, False),
        ([2, 3], True, False),
        ([1, 2, 4], False, False),  # decisão com buraco: permitido
        ([1, 4, 2], False, True),  # decisão fora de ordem: acusa
        ([1, 1], False, True),  # decisão repetida: acusa
    ]
    falhas = 0
    for nums, contigua, deve_acusar in casos:
        acusou = fora_de_ordem(nums, contigua) is not None
        ok = acusou == deve_acusar
        falhas += not ok
        modo = "contígua" if contigua else "crescente"
        print(f"  {'✅' if ok else '❌'} {nums} ({modo}) → {'acusa' if acusou else 'passa'}")
    print()
    print("❌ autoteste com falha" if falhas else f"✅ autoteste verde — {len(casos)} casos")
    return 1 if falhas else 0


def main() -> int:
    sys.stdout.reconfigure(encoding="utf-8")  # §A7
    if "--autoteste" in sys.argv:
        return _autoteste()
    defeitos = 0
    for rel, padrao, desc, contigua in VIGIADOS:
        arq = RAIZ / rel
        if not arq.exists():
            print(f"  ❌ {rel}: arquivo vigiado não existe")
            defeitos += 1
            continue
        nums = [int(n) for n in re.findall(padrao, arq.read_text(encoding="utf-8"), re.M)]
        problema = fora_de_ordem(nums, contigua)
        if problema:
            defeitos += 1
            print(f"  ❌ {rel} ({desc}): {problema}")
        else:
            print(f"  ✅ {rel} ({desc}): {len(nums)} em ordem")
    return 1 if defeitos else 0


if __name__ == "__main__":
    sys.exit(main())
