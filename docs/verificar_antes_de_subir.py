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
    "ferramentas/extrair_provas_aocp.py",
    "ferramentas/classificar_incidencia.py",
    "ferramentas/verificar_atualidade.py",
    "ferramentas/localizar_lei.py",
    "ferramentas/gerar_revisao.py",
    "ferramentas/testar_revisao.py",
    "ferramentas/corrigir_sumulas.py",
    "ferramentas/validar_revisao_material.py",
    "ferramentas/montar_revisao_material.py",
    "ferramentas/validar_aprofundamento.py",
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
    ("a trava de CPF do índice acusa", [sys.executable, "ferramentas/ampliar_acervo.py", "--autoteste"],
     "CPF do licenciado no índice; e a 1ª trava barrava a PALAVRA 'CPF' em texto jurídico (01/11/2026)"),
    ("espera pela geração: comportamento", ["node", "docs/testar_espera.mjs"],
     "tela desistindo aos 240 s com o servidor ainda gerando; 100 consultas à toa em 'missing'"),
    ("servidor: geração medida, bloco e histórico", [sys.executable, "docs/testar_servidor.py"],
     "custo sem medição; correlato inventado; histórico de MB descartado calado (D-005 a D-007)"),
    ("blocos de 30: comportamento", ["node", "docs/testar_blocos.mjs"],
     "bloco repetindo ponto; baixa por correlação de id inventado; histórico com <script> vivo"),
    ("a página carrega sem erro de JavaScript", ["node", "docs/testar_pagina.cjs"],
     "tela inteira em branco por nome errado ou script na ordem errada"),
    ("treino de discursiva: comportamento", ["node", "docs/testar_discursiva.cjs"],
     "peça sem modelo ou checklist; cartão sem artigo; nota fora das Tabelas 7.3/7.4; sem reagendar"),
    ("o teste da discursiva acusa", ["node", "docs/testar_discursiva.cjs", "--autoteste"],
     "teste que passa com a nota técnica da peça estragada (verde falso)"),
    ("simulados: leitor de blocos dos PDFs", ["node", "docs/testar_blocos_simulados.cjs"],
     "comentário em letra de máquina com rolagem lateral; parágrafo partido; caractere do PDF perdido"),
    ("o teste do leitor de blocos acusa", ["node", "docs/testar_blocos_simulados.cjs", "--autoteste"],
     "teste que passa com caractere perdido (verde falso)"),
    # Revisão por prioridade (D-018, 06/11/2026)
    ("o verificador de atualidade acusa",
     [sys.executable, "ferramentas/verificar_atualidade.py", "--autoteste"],
     "artigo citado fora do texto vigente, súmula cancelada, jurisprudência sem fonte e data (verde falso)"),
    ("a régua comum de lei seca acusa", [sys.executable, "ferramentas/localizar_lei.py", "--autoteste"],
     "alínea como inciso, 'Il' do Planalto, '§ 2°' com grau: "
     "gerador aprovando o que o verificador reprova (07/11/2026)"),
    ("o gerador da revisão acusa", [sys.executable, "ferramentas/gerar_revisao.py", "--autoteste"],
     "módulo com lei adulterada, súmula cancelada ou PDF não gravado saindo como gerado; "
     "régua dividida com o verificador"),
    ("o corretor de súmulas acusa", [sys.executable, "ferramentas/corrigir_sumulas.py", "--autoteste"],
     "troca às cegas de súmula sem o valor de antes conferido; correção aplicada duas vezes"),
    ("súmulas: correções oficiais aplicadas", [sys.executable, "ferramentas/corrigir_sumulas.py", "--estado"],
     "sumulas.json regravado pela extração sem as correções conferidas no STF/STJ; "
     "sai 2 (pulada) sem a base"),
    ("lei seca oficial com menos de 30 dias",
     [sys.executable, "ferramentas/verificar_atualidade.py", "--estado"],
     "módulo gerado sobre lei seca velha; sai 2 (pulada) onde a base não existe — fica fora do Git (D-015)"),
    ("a régua de incidência acusa", [sys.executable, "ferramentas/classificar_incidencia.py", "--autoteste"],
     "régua que casa 'tor' dentro de 'torre', perde o plural em -ões ou classifica sem termo (06/11/2026)"),
    # Aba Revisão: assertivas C/E de TODO o material anexado (D-022, 09/11/2026)
    ("a prova de cobertura da Revisão acusa",
     [sys.executable, "ferramentas/validar_revisao_material.py", "--autoteste"],
     "página do material sem assertiva, julgado perdido, CPF da marca d'água ou gabarito torto "
     "passando calados"),
    ("o montador da Revisão acusa", [sys.executable, "ferramentas/montar_revisao_material.py", "--autoteste"],
     "revisao_nfpss.js gravado com bloco sem cobertura provada ou sem assertivas"),
    ("o verificador do aprofundamento acusa",
     [sys.executable, "ferramentas/validar_aprofundamento.py", "--autoteste"],
     "comentário aprofundado com número que o item não tem, E sem o certo ao lado do erro "
     "ou CPF (09/11/2026)"),
    ("o leitor das provas AOCP acusa", [sys.executable, "ferramentas/extrair_provas_aocp.py", "--autoteste"],
     "gabarito ou cabeçalho da prova lidos errado em silêncio"),
    # Paleta de grifos com a tecla G em todas as telas (10/11/2026, pedido do titular)
    ("grifos: cópia embutida igual à fonte", [sys.executable, "ferramentas/embutir_grifa.py", "--conferir"],
     "tela sem a paleta ou com cópia velha de assets/grifa.js (cada tela grifando de um jeito)"),
    ("o conferidor dos grifos acusa", [sys.executable, "ferramentas/embutir_grifa.py", "--autoteste"],
     "conferidor que aprova tela sem o bloco, com cópia antiga ou com dois blocos (verde falso)"),
    ("grifos: comportamento", ["node", "docs/testar_grifa.cjs"],
     "G abrindo dentro de campo; grifo que some ao redesenhar; grifo no lugar errado em trecho repetido"),
    ("o teste dos grifos acusa", ["node", "docs/testar_grifa.cjs", "--autoteste"],
     "teste que passa com o contexto ignorado ou sem reaplicar o grifo (verde falso)"),
    ("olho de águia: comportamento", ["node", "docs/testar_olho_de_aguia.cjs"],
     "alternativa verdadeira grifada; grifo fora do trecho exato; bloco com mais de 100; meta que não conta"),
    ("o teste do olho de águia acusa", ["node", "docs/testar_olho_de_aguia.cjs", "--autoteste"],
     "teste que passa com o grifo do trecho errado sumido (verde falso)"),
    ("revisão Delegado-BA: comportamento", ["node", "docs/testar_revisao_ba.cjs"],
     "Bloco 1 com 50 assertivas C/E (gabarito e base); responder mostra veredito e comentário"),
    ("o teste da revisão Delegado-BA acusa", ["node", "docs/testar_revisao_ba.cjs", "--autoteste"],
     "teste que passa com um gabarito inválido (C/E corrompido) — verde falso"),
    ("treino de letra de lei: comportamento", ["node", "docs/testar_lei_seca_ba.cjs"],
     "artigos por lacunas (lacunas=respostas, base); revelar preenche e salva o progresso"),
    ("o teste do treino de letra de lei acusa", ["node", "docs/testar_lei_seca_ba.cjs", "--autoteste"],
     "teste que passa com lacunas sem resposta correspondente — verde falso"),
    ("lei na íntegra: comportamento", ["node", "docs/testar_lei_integra.cjs"],
     "artigo inteiro em 3 modos, palavras-chave {}, mnemônico e áudio; progresso salvo"),
    ("o teste da lei na íntegra acusa", ["node", "docs/testar_lei_integra.cjs", "--autoteste"],
     "teste que passa com um artigo sem palavra-chave {} — verde falso"),
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
            porque = (r.stdout + r.stderr).strip().splitlines()
            print(f"  [PUL] {nome} — pulada, e isto não é verde")
            if porque:
                print(f"        │ {porque[-1].strip()}")
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
