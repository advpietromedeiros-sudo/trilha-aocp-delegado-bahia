#!/usr/bin/env python3
"""Portão do Trilha AOCP: roda todas as portas e só abre com todas verdes.

Semente do roteiro de fundação §5 (HARNESS §P6, REGRA CINCO): cada porta tem nome, comando e o erro
que impede; cada verificador tem --autoteste; porta pulada sai 2 e se diz; erro novo vira porta nova.

Uso: python docs/verificar_antes_de_subir.py
"""

from __future__ import annotations

import shutil
import subprocess
import sys
from pathlib import Path

RAIZ = Path(__file__).resolve().parent.parent
PY = [
    "servidor.py",
    "ferramentas/atualizar_lei_seca.py",
    "ferramentas/construir_base.py",
]

# (nome, comando, o erro que esta porta impede)
PORTAS: list[tuple[str, list[str], str]] = [
    ("Python compila", [sys.executable, "-m", "py_compile", *PY],
     "servidor que não sobe por erro de sintaxe, descoberto só na hora de estudar"),
    ("nenhum segredo no índice do Git", [sys.executable, "docs/verificar_antes_de_subir.py", "--segredo"],
     "chave de API versionada (o .env existe na pasta)"),
    ("a régua de segredo acusa", [sys.executable, "docs/verificar_antes_de_subir.py", "--segredo-autoteste"],
     "régua frouxa acusa o inocente; régua cega deixa a chave passar (REGRA CINCO)"),
    ("guard rails de shell", [sys.executable, ".claude/hooks/testar_guarda.py"],
     "cada caso é um comando perigoso que já foi tentado"),
    ("relógio da sessão", [sys.executable, ".claude/hooks/relogio.py", "--autoteste"],
     "resposta datada pela memória, e não pelo relógio"),
    ("registros numerados em ordem", [sys.executable, "docs/verificar_sequencia.py"],
     "entrada nova ancorada no início da seguinte (§F62)"),
    ("o verificador de sequência acusa", [sys.executable, "docs/verificar_sequencia.py", "--autoteste"],
     "verificador que nunca falha passa por controle para sempre"),
    ("index.html: defeitos corrigidos não voltam", [sys.executable, "docs/verificar_regressoes.py"],
     "Refazer apagando a resposta sem rastro; Ctrl+C marcando a alternativa C (31/10/2026)"),
    ("o verificador de regressões acusa", [sys.executable, "docs/verificar_regressoes.py", "--autoteste"],
     "verificador que nunca falha passa por controle para sempre"),
    ("espera pela geração: comportamento", ["node", "docs/testar_espera.mjs"],
     "tela desistindo aos 240 s com o servidor ainda gerando; 100 consultas à toa em 'missing'"),
]

# Régua de segredo (31/10/2026): exige VALOR de 20+ caracteres depois do `=` — o LEIA_PRIMEIRO cita
# o nome da variável sem valor, e uma régua frouxa o acusava.
_REGUA = r"sk-(ant|proj)-|_API_KEY=[A-Za-z0-9_-]{20,}"


def _segredo() -> int:
    """Porta própria: `git grep` no índice. Imprime só NOMES de arquivo, nunca a linha (§F59)."""
    r = subprocess.run(["git", "grep", "-l", "--cached", "-E", _REGUA], cwd=RAIZ,
                       capture_output=True, text=True, encoding="utf-8")
    if r.returncode == 1:  # git grep: 1 = nada encontrado
        print("  nenhum arquivo do índice casa com a régua de segredo")
        return 0
    if r.returncode == 0:
        print("  arquivos com possível segredo (só o nome):\n" + r.stdout)
        return 1
    print(f"  git grep falhou (rc {r.returncode}): {r.stderr.strip()}")
    return 1


def _segredo_autoteste() -> int:
    """Prova que a régua acusa uma chave e deixa passar a citação do nome (REGRA CINCO).

    Os exemplos são MONTADOS em tempo de execução (§F54): escritos literais, seriam eles mesmos um
    "segredo" no índice e fariam a porta acusar este arquivo.
    """
    import re

    nome = "OPENAI" + "_API_KEY="
    casos = [
        (nome + "a" * 24, True),  # valor de chave: acusa
        ("sk-" + "ant-" + "x" * 10, True),  # prefixo de chave da Anthropic: acusa
        (nome + "` **ou** `", False),  # a linha do LEIA_PRIMEIRO: passa
        (nome, False),  # só o nome: passa
    ]
    falhas = 0
    for texto, deve in casos:
        acusou = re.search(_REGUA, texto) is not None
        falhas += acusou != deve
        print(f"  {'✅' if acusou == deve else '❌'} {'acusa' if deve else 'passa'}: {texto[:14]}…")
    return 1 if falhas else 0


def main() -> int:
    sys.stdout.reconfigure(encoding="utf-8")  # §A7 — o console do Windows é cp1252
    if "--segredo-autoteste" in sys.argv:
        return _segredo_autoteste()
    if "--segredo" in sys.argv:
        return _segredo()
    falhas, puladas = [], []
    for nome, comando, motivo in PORTAS:
        if comando[0] == "node" and shutil.which("node") is None:
            puladas.append(nome)
            print(f"  [PUL] {nome} — Node não encontrado: pulada, e isto não é verde")
            continue
        r = subprocess.run(comando, cwd=RAIZ, capture_output=True, text=True, encoding="utf-8")
        if r.returncode == 0:
            print(f"  [OK ] {nome}")
        elif r.returncode == 2:
            puladas.append(nome)
            print(f"  [PUL] {nome} — pulada, e isto não é verde")
        else:
            falhas.append(nome)
            print(f"  [ X ] {nome}\n        impede: {motivo}")
            for linha in (r.stdout + r.stderr).strip().splitlines()[-12:]:
                print(f"        │ {linha}")
    # py_compile deixa __pycache__ para trás; não é do repositório.
    for pasta in RAIZ.rglob("__pycache__"):
        if "node_modules" not in pasta.parts:
            for arq in pasta.iterdir():
                arq.unlink()
            pasta.rmdir()
    print()
    if falhas:
        print(f"  ❌ portão FECHADO: {len(falhas)} falha(s)")
        return 1
    if puladas:
        print(f"  ⚠️ portão aberto com {len(puladas)} porta(s) pulada(s) — dizer quais no commit")
        return 0
    print(f"  ✅ portão aberto — {len(PORTAS)} portas.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
