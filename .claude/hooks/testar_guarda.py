#!/usr/bin/env python3
"""testar_guarda.py — prova que cada regra da guarda de shell ACUSA e que não barra o legítimo.

HARNESS REGRA CINCO (31/10/2026): todo verificador tem autoteste que prova que ele acusa. Para
cada regra de `guarda_shell.py` há **um caso que deve ser recusado e um que deve passar** — o
roteiro de fundação (§9.4) exige os dois, porque guarda que barra o trabalho legítimo é desligada
e aí não guarda nada.

Errou de novo? O erro vira CASO aqui e REGRA na guarda, na mesma correção.

Uso: python testar_guarda.py   (sai 0 com tudo certo, 1 com qualquer falha)
"""

from __future__ import annotations

import importlib.util
import sys
from pathlib import Path

_AQUI = Path(__file__).resolve().parent
_spec = importlib.util.spec_from_file_location("guarda_shell", _AQUI / "guarda_shell.py")
assert _spec and _spec.loader
guarda = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(guarda)

B, P = "Bash", "PowerShell"

# (regra esperada ou None, ferramenta, comando)
CASOS: list[tuple[str | None, str, str]] = [
    # crase dentro de git commit -m
    ("crase dentro de git commit -m", B, 'git commit -m "usa `npm` agora"'),
    (None, B, "git commit -F .scratch/msg_commit.txt"),
    # leitura de arquivo que guarda segredo
    ("leitura de arquivo que guarda segredo", B, "cat .env"),
    (None, B, "cat .env.exemplo"),
    # busca dentro de arquivo que guarda segredo
    ("busca dentro de arquivo que guarda segredo", B, "grep API_KEY .env"),
    (None, B, "git ls-files | grep .env"),
    # git add em massa
    ("git add em massa", B, "git add -A"),
    (None, B, "git add -- CLAUDE.md docs/FAROL.md"),
    # commit pulando o portão
    ("commit pulando o portao", B, "git commit --no-verify -F msg.txt"),
    (None, B, "git commit -F msg.txt"),
    # apagar o banco de desenvolvimento
    ("apagar o banco de desenvolvimento", B, "docker compose -p portal down -v"),
    (None, B, "docker compose -p portal down"),
    # portão atrás de pipe decidindo commit
    ("portao atras de pipe decidindo commit", B, "npm run lint | tail -3 && git commit -F m.txt"),
    (None, B, "npm run lint && git commit -F m.txt"),
    # git add seguido de commit sem conferir o status
    ("git add seguido de commit sem conferir o status", B, "git add a.txt; git commit -F m.txt"),
    (None, B, "git add a.txt && git commit -F m.txt"),
    # escrita em produção (roteiro §P1)
    ("escrita em producao", B, "ssh root@159.195.200.161 'cd /srv/portal && git pull'"),
    ("escrita em producao", P, "ssh netcup docker compose -p pietromedeiros up -d --no-deps webapp"),
    (None, B, "ssh root@159.195.200.161 docker ps --filter name=pietromedeiros"),
    (None, B, "ssh netcup 'docker logs --tail 50 pietromedeiros-webapp-prod'"),
    # docker compose sem nome de projeto (roteiro §P10)
    ("docker compose sem nome de projeto", B, "docker compose up -d"),
    (None, B, "docker compose -p pietromedeiros up -d"),
    (None, B, "docker compose --project-name=pietromedeiros up -d"),
    (None, B, "docker compose ps"),
    # push forçado (roteiro §P12)
    ("push forcado", B, "git push --force origin main"),
    ("push forcado", P, "git push -f"),
    ("push forcado", B, "git push --force-with-lease"),
    (None, B, "git push -u origin main"),
    # citar não é executar: descrever o comando proibido numa mensagem passa
    (None, B, "git commit -m 'nao use git push --force nem docker compose up sem -p'"),
]


def main() -> int:
    # §A7: com `python -I` o PYTHONIOENCODING é ignorado e o console do Windows cai no cp1252, que
    # não escreve ✅ — o teste quebrava pelo AMBIENTE e mentia vermelho (medido em 31/10/2026).
    sys.stdout.reconfigure(encoding="utf-8")
    falhas = 0
    for esperado, ferramenta, comando in CASOS:
        achada = guarda.avaliar(ferramenta, comando)
        obtido = achada.nome if achada else None
        ok = obtido == esperado
        falhas += not ok
        marca = "✅" if ok else "❌"
        alvo = f"recusa ({esperado})" if esperado else "passa"
        print(f"  {marca} [{ferramenta}] {comando}\n       esperado: {alvo} · obtido: {obtido or 'passa'}")
    # Toda regra da guarda precisa de pelo menos um caso que a vê recusar (REGRA CINCO).
    sem_caso = {r.nome for r in guarda.REGRAS} - {c[0] for c in CASOS if c[0]}
    for nome in sorted(sem_caso):
        falhas += 1
        print(f"  ❌ regra sem caso de recusa: {nome}")
    print()
    if falhas:
        print(f"❌ {falhas} falha(s) em {len(CASOS)} casos")
        return 1
    print(f"✅ guarda verde — {len(CASOS)} casos, {len(guarda.REGRAS)} regras, todas com caso de recusa")
    return 0


if __name__ == "__main__":
    sys.exit(main())
