#!/usr/bin/env python3
"""verificar_regressoes.py — defeitos já corrigidos no index.html não voltam (HARNESS §F25, §F23).

O index.html é um arquivo único de ~280 KB, sem suíte de testes de JavaScript. Cada defeito
corrigido vira aqui uma ASSERTIVA sobre o código, com um caso que a vê falhando (--autoteste):

  R-01 (31/10/2026) — "Refazer (não altera histórico)" APAGAVA a resposta sem rastro. A correção
       guarda a tentativa em state.attempts ANTES do `delete state.answers[k]`.
  R-02 (31/10/2026) — os atalhos A–E não olhavam Ctrl/Cmd/Alt nem a aba: Ctrl+C marcava a
       alternativa C, e as letras marcavam resposta nas abas em que a questão está oculta.
  JS   — o bloco <script> tem sintaxe válida (`node --check`); sem Node na máquina, a porta sai 2
       (pulada, e dita).

Uso: python docs/verificar_regressoes.py [--autoteste]   (0 = ok, 1 = regressão, 2 = pulada)
"""

from __future__ import annotations

import re
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

RAIZ = Path(__file__).resolve().parent.parent

# (id, descrição, função que devolve True quando o código ESTÁ CORRETO)
def _r01(js: str) -> bool:
    i = js.find("delete state.answers[k]")
    if i < 0:
        return True  # o apagamento sumiu do código: nada a proteger
    trecho = js[max(0, i - 600) : i]
    return "state.attempts" in trecho and ".push(" in trecho


def _r02(js: str) -> bool:
    m = re.search(r"if\(([^{]*)'ABCDE'\.includes\(letter\)", js)
    if not m:
        return False  # o atalho mudou de forma: a assertiva precisa ser revista, não ignorada
    cond = m.group(1)
    return all(s in cond for s in ("!e.ctrlKey", "!e.metaKey", "!e.altKey", "state.view==='study'"))


def _r03(js: str) -> bool:
    i = js.find("function renderErrorBook")
    corpo = js[i : i + 1500] if i >= 0 else ""
    # O caderno lê as tentativas refeitas E descarta as de item que não existe (senão a tela quebra
    # em `it.discipline`).
    return "state.attempts" in corpo and "BY_ID[k.split('|')[0]]" in corpo


ASSERTIVAS = [
    ("R-01", "Refazer guarda a tentativa antes de apagar a resposta", _r01),
    ("R-02", "atalhos A–E ignoram Ctrl/Cmd/Alt e só valem na aba Estudar", _r02),
    ("R-03", "caderno de erros mostra as tentativas refeitas, sem quebrar com item inexistente", _r03),
]


def _js(html: str) -> str:
    return "\n".join(re.findall(r"<script>([\s\S]*?)</script>", html))


def _autoteste() -> int:
    bom = (
        "state.attempts=state.attempts||{};(state.attempts[k]=state.attempts[k]||[]).push(x);"
        "delete state.answers[k];"
        "if(!e.ctrlKey&&!e.metaKey&&!e.altKey&&state.view==='study'&&'ABCDE'.includes(letter)){}"
        "function renderErrorBook(){const r=Object.entries(state.attempts||{})"
        ".filter(([k])=>BY_ID[k.split('|')[0]]);}"
    )
    casos = [
        ("código corrigido passa", bom, True, True, True),
        ("Refazer sem guardar a tentativa acusa", bom.replace(".push(x)", ""), False, True, True),
        ("atalho sem a guarda de Ctrl acusa", bom.replace("!e.ctrlKey&&", ""), True, False, True),
        ("atalho sem a guarda da aba acusa", bom.replace("&&state.view==='study'", ""), True, False, True),
        ("caderno sem o filtro de item inexistente acusa",
         bom.replace(".filter(([k])=>BY_ID[k.split('|')[0]])", ""), True, True, False),
    ]
    falhas = 0
    for desc, js, r01, r02, r03 in casos:
        ok = _r01(js) == r01 and _r02(js) == r02 and _r03(js) == r03
        falhas += not ok
        print(f"  {'✅' if ok else '❌'} {desc}")
    print("❌ autoteste com falha" if falhas else f"✅ autoteste verde — {len(casos)} casos")
    return 1 if falhas else 0


def main() -> int:
    sys.stdout.reconfigure(encoding="utf-8")  # §A7
    if "--autoteste" in sys.argv:
        return _autoteste()
    js = _js((RAIZ / "index.html").read_text(encoding="utf-8"))
    falhas = 0
    for ident, desc, correto in ASSERTIVAS:
        ok = correto(js)
        falhas += not ok
        print(f"  {'✅' if ok else '❌'} {ident} — {desc}")
    node = shutil.which("node")
    if node is None:
        print("  ⚠️ JS — Node não encontrado: sintaxe NÃO conferida (porta pulada)")
        return 1 if falhas else 2
    with tempfile.NamedTemporaryFile("w", suffix=".js", delete=False, encoding="utf-8") as f:
        f.write(js)
        caminho = f.name
    r = subprocess.run([node, "--check", caminho], capture_output=True, text=True, encoding="utf-8")
    Path(caminho).unlink(missing_ok=True)
    print(f"  {'✅' if r.returncode == 0 else '❌'} JS — sintaxe do <script> (node --check)")
    if r.returncode != 0:
        print("    " + r.stderr.strip().splitlines()[-1])
        falhas += 1
    return 1 if falhas else 0


if __name__ == "__main__":
    sys.exit(main())
