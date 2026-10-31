"""guarda_shell.py — os guard rails de shell como CODIGO, e nao como lembranca.

procedencia: copia de `~/.claude/hooks/guarda_shell.py` da estacao do titular (31/10/2026), com as
regras do roteiro de fundacao (HARNESS §P1, §P10, §P12) e a cessao de vez ao hook do usuario
(§P12.2, funcao `_usuario_ja_cobre`). A regra "escrita em producao" cita o servidor de producao de
proposito: e' ali que a IA so' pode ler. Testes: `testar_guarda.py`, ao lado (porta do portao).

📐 O QUE FAZ: roda como hook `PreToolUse` das ferramentas Bash e PowerShell, le o comando e NEGA
quando ele repete um erro que o HARNESS ja' proibe. A mensagem cita a regra e diz o caminho
certo — negar sem ensinar so' irrita.

⚠️ FALSO POSITIVO E' PIOR QUE FALSO NEGATIVO numa guarda de fluxo: a que barra o trabalho
legitimo e' desligada, e ai' nao guarda nada. Por isso cada regra e' ESTREITA — casa com o erro
exato.

🔑 CITAR NAO E' EXECUTAR. Mensagem de commit, here-string e heredoc sao TEXTO: descrever um comando
proibido nao e' roda-lo. As regras que olham o que sera' executado recebem o comando SEM esses
blocos (`sem_texto_literal`). No produto de origem, esquecer isto fez a guarda bloquear o proprio
autor doze vezes — inclusive o commit que criava a regra.

⚠️ COBERTURA DECLARADA (HARNESS §D2):
  · so' ve o que a IA executa por shell — nao o bloco que vai no chat para o titular colar;
  · nao ve a ferramenta Read, nem `docker exec ... env`, nem `docker inspect`;
  · nao ve defeito de CONTEUDO de arquivo — isso e' tarefa dos portoes do projeto.

Saida: JSON do protocolo de hook — `permissionDecision: "deny"` bloqueia a chamada.
"""

from __future__ import annotations

import json
import re
import sys
from typing import NamedTuple


class Regra(NamedTuple):
    nome: str
    ferramentas: frozenset[str]
    padrao: re.Pattern[str]
    fonte: str
    caminho_certo: str
    # True: julga so' o que sera' EXECUTADO (sem mensagem de commit, here-string, heredoc).
    so_execucao: bool


AMBAS = frozenset({"Bash", "PowerShell"})

# Arquivo que guarda segredo: `.env` e `.env.<qualquer>` — MENOS o `.env.exemplo`, que e' modelo e
# existe para ser lido (o .gitignore diz o mesmo) — e chave/certificado.
_SEGREDO = r"(?:[\w./\\~:-]*\.env(?:\.(?!exemplo\b)[\w-]+)?(?![\w.])|[\w./\\~:-]+\.(?:pem|key)\b)"

REGRAS: tuple[Regra, ...] = (
    Regra(
        "crase dentro de git commit -m",
        AMBAS,
        # So' a mensagem entre ASPAS DUPLAS numa linha: no Bash a crase ali e' executada; no
        # PowerShell ela e' escape. Aspas simples sao literais nos dois — passam. O heredoc
        # quotado (`-m "$(cat <<'FIM'`) passa: a crase fica em outra linha, e la' e' literal.
        re.compile(r"\bgit\b[^\n]*\bcommit\b[^\n]*\s-m\s*\"[^\"\n]*`"),
        "REGRA QUATRO / §A16 — a crase e' comando para o shell",
        'A crase dentro de `-m "..."` e\' executada (Bash) ou vira escape (PowerShell): a '
        "palavra SOME da mensagem e o commit sobe mutilado, com rc 0. Escreva a mensagem num "
        "arquivo com a ferramenta Write e use `git commit -F <arquivo>`.",
        so_execucao=False,
    ),
    Regra(
        "leitura de arquivo que guarda segredo",
        AMBAS,
        # Comandos que SEMPRE abrem o caminho recebido — em qualquer posicao do pipeline.
        re.compile(
            r"\b(?:cat|head|tail|less|more|bat|nl|tac|strings|xxd|od|base64|type|"
            r"Get-Content|gc|Copy-Item|cp|scp)\b[^|;&\n]*?" + _SEGREDO,
            re.I,
        ),
        "§F59 — segredo nao se le, nem com redacao",
        "Este comando LE um arquivo que guarda segredo. Nao existe leitura parcial segura, nem "
        "redacao boa o bastante: 'nao redigiu nada' e 'nao havia o que redigir' dao a MESMA "
        "saida. Precisa saber se uma variavel existe? Pergunte ao titular, ou confira o "
        "`.env.exemplo` (o modelo, sem valor). Precisa do valor? E' tarefa do titular, no terminal "
        "dele.",
        so_execucao=True,
    ),
    Regra(
        "busca dentro de arquivo que guarda segredo",
        AMBAS,
        # Irma da de cima, para quem toma PADRAO antes do caminho. Ancorada no INICIO do comando
        # (ou apos ; e &&), nunca depois de |: por pipe, o grep le' stdin e o token e' padrao.
        re.compile(
            r"(?:^|[;&]\s*)\s*\b(?:sed|awk|grep|egrep|fgrep|rg|findstr|Select-String|sls)\b"
            r"[^|;&\n]*?" + _SEGREDO,
            re.I | re.M,
        ),
        "§F59 — segredo nao se le, nem com redacao",
        "Este comando BUSCA dentro de um arquivo que guarda segredo — e a busca imprime a LINHA "
        "inteira, com o valor. Ate' a contagem (`-c`) entrega quais chaves existem. Se voce so' "
        "quer filtrar uma saida (`git ls-files | grep .env`), isso ja' passa: esta regra so' "
        "olha o inicio do comando.",
        so_execucao=True,
    ),
    Regra(
        "git add em massa",
        AMBAS,
        re.compile(
            r"\bgit\s+add\b[^\n;&|]*?(?:\s-A\b|\s--all\b|\s-u\b|\s--update\b|\s\.(?=[\s;&|]|$))"
            r"|\bgit\s+commit\b[^\n;&|]*?\s-[a-zA-Z]*a[a-zA-Z]*\b",
            re.M,
        ),
        "§G4.5 ② / §F53 — git add por caminho, nunca em massa",
        "`git add -A`, `git add .`, `git add -u` e `git commit -a` versionam o que estiver na "
        "arvore — inclusive arquivo alheio no meio da escrita e rascunho que nao era para subir. "
        "Liste os caminhos: `git add -- <arquivo1> <arquivo2>`.",
        so_execucao=True,
    ),
    Regra(
        "commit pulando o portao",
        AMBAS,
        re.compile(
            r"\bgit\b[^\n;&|]*\s--no-verify\b"
            r"|\bHUSKY\s*=\s*['\"]?0\b[^\n]*\bgit\b"
            r"|\$env:HUSKY\s*=\s*['\"]?0\b[^\n]*\bgit\b",
            re.I,
        ),
        "§G4.5 ① / §F23 — vermelho nao sobe",
        "O pre-commit e' o portao rapido do repositorio. "
        "Pular o hook e' subir sem ele. Se o portao reprovou, o defeito e' o que conserta — e se "
        "o portao estiver ERRADO, o conserto e' no portao, num commit proprio.",
        so_execucao=True,
    ),
    Regra(
        "apagar o banco de desenvolvimento",
        AMBAS,
        re.compile(
            r"\bdocker(?:-compose|\s+compose)\b[^\n;&|]*\bdown\b[^\n;&|]*\s(?:-v|--volumes)\b"
            r"|\bdocker\s+volume\s+(?:rm|prune)\b",
            re.I,
        ),
        "§F17 — dado faltando nao se apaga; e o compose avisa: APAGA O BANCO",
        "Isto destroi os volumes do compose: o banco de "
        "desenvolvimento some, com migracao e dado. Se for mesmo necessario, e' decisao do titular: "
        "proponha o comando no chat, com o motivo, e ele executa.",
        so_execucao=True,
    ),
    Regra(
        "portao atras de pipe decidindo commit",
        AMBAS,
        # 💥 Um portao seguido de `|` e, logo depois, do commit: o status do pipeline e' o do
        # ULTIMO comando (o filtro), nao o do portao — o vermelho passa por verde.
        re.compile(
            r"(?:\bnpm\s+run\s+[\w:-]+|\bpython\s+\S*(?:verificar|testar)_\w+\.py|\bruff\b|"
            r"\bmypy\b|\bgitleaks\b)[^\n;&]*\|[^|;&\n]*(?:&&|;)\s*git\s+(?:-C\s+\S+\s+)?commit\b"
        ),
        "§F31 / §G4.5 ① — o status do pipe e' o do filtro, nao o do portao",
        "O `|` entrega ao `&&` (ou ao `;`) o status do ULTIMO comando do pipe — o filtro, que "
        "quase sempre sai 0. O portao pode estar vermelho e o commit segue. Rode o portao sem "
        "pipe, guarde o status (`$LASTEXITCODE` no PowerShell, `rc=$?` no Bash) e so' commite "
        "se ele for 0.",
        so_execucao=True,
    ),
    Regra(
        "git add seguido de commit sem conferir o status",
        AMBAS,
        # 💥 12/09/2026: `git add <lista>; git commit` com um caminho ja' removido na lista.
        # O git add ABORTA a lista inteira, o `;` segue, e o commit leva so' o que ja' estava no
        # indice. Estreita: so' o `;` direto entre os dois; `&&` passa.
        re.compile(r"\bgit\s+add\b[^\n;&|]*;\s*git\s+(?:-C\s+\S+\s+)?commit\b"),
        "§F31 — quem escreve confirma lendo o status",
        "Com `;`, o commit roda mesmo que o `git add` tenha falhado — e um caminho inexistente na "
        "lista faz o add abortar INTEIRO, calado quanto ao resto. O commit sobe so' com o que ja' "
        "estava no indice. Use `git add -- <caminhos> && git commit ...`, ou confira "
        "`$LASTEXITCODE` (PowerShell) / `rc=$?` (Bash) antes do commit.",
        so_execucao=True,
    ),
    # ── Roteiro de fundação v1.0 (canônico desde 31/10/2026, HARNESS Parte IV) ────────────────
    Regra(
        "escrita em producao",
        AMBAS,
        # So' com ssh para o servidor de producao E um verbo que ESCREVE. Ler (docker ps, logs,
        # curl, psql de SELECT) passa: auditar e' da IA (§P1).
        re.compile(
            r"\bssh\b[^\n]*(?:159\.195\.200\.161|netcup)[^\n]*"
            r"(?:\bdocker(?:\s+compose|-compose)\b[^\n]*\b(?:up|down|restart|rm|stop|start|pull|build)\b"
            r"|\bdocker\s+(?:restart|rm|stop|start|kill|run)\b"
            r"|\bpsql\b[^\n]*\s-c\b[^\n]*\b(?:insert|update|delete|drop|alter|create|truncate|grant)\b"
            r"|\bgit\s+(?:pull|merge|fetch|reset|checkout)\b"
            r"|\bsystemctl\s+(?:start|restart|stop|reload)\b"
            r"|\bcaddy\s+reload\b)",
            re.I,
        ),
        "HARNESS §P1 / §F7 — producao e' so' auditoria para a IA",
        "Escrever no servidor de producao e' do operador do servidor. Leia o que quiser "
        "(docker ps, logs, curl, SELECT com papel de leitura); para MUDAR algo, entregue o comando "
        "no chat, colavel, dizendo a maquina e a pasta, e ele executa.",
        so_execucao=True,
    ),
    Regra(
        "docker compose sem nome de projeto",
        AMBAS,
        # So' os verbos que criam, derrubam ou mudam containers. `docker compose ps`/`logs`/
        # `config`/`version` passam.
        re.compile(
            r"\bdocker(?:\s+compose|-compose)\b(?![^\n;&|]*\s(?:-p|--project-name)[\s=])"
            r"[^\n;&|]*\b(?:up|down|restart|rm|stop|start|run|create|pull|build)\b",
            re.I,
        ),
        "HARNESS §P10 / §B6 — compose sem -p pega o projeto errado",
        "Sem `-p <projeto>`, o compose deduz o nome pela pasta: sobe stack orfa, pega container "
        "alheio ou perde o volume. Diga o projeto: `docker compose -p <projeto> ...` (e, no deploy, "
        "`--no-deps` para nao recriar o banco junto).",
        so_execucao=True,
    ),
    Regra(
        "push forcado",
        AMBAS,
        re.compile(r"\bgit\b[^\n;&|]*\bpush\b[^\n;&|]*\s(?:--force(?:-with-lease)?\b|-f\b|\+\S)"),
        "HARNESS §P12 — push forcado reescreve o historico de quem colabora",
        "O repositorio tem colaborador: reescrever o historico remoto apaga commit alheio e quebra "
        "o clone dele. Corrija com um commit novo (`git revert`, ou um commit que conserta). Se "
        "for mesmo indispensavel, e' decisao do titular, combinada com quem colabora.",
        so_execucao=True,
    ),
)

# Blocos que sao TEXTO, nao comando.
_TEXTO_LITERAL = (
    re.compile(r"@'[\s\S]*?'@"),  # here-string literal do PowerShell
    re.compile(r'@"[\s\S]*?"@'),  # here-string expansivel do PowerShell
    re.compile(r"<<-?\s*'?(\w+)'?[^\n]*\n[\s\S]*?\n\s*\1\b", re.M),  # heredoc do Bash
    re.compile(r"\s-m\s*\"[^\"]*\""),  # mensagem de commit entre aspas duplas
    re.compile(r"\s-m\s*'[^']*'"),  # mensagem de commit entre aspas simples
)


def sem_texto_literal(comando: str) -> str:
    """Remove os blocos de texto, deixando so' o que sera' EXECUTADO."""
    limpo = comando
    for padrao in _TEXTO_LITERAL:
        limpo = padrao.sub(" ", limpo)
    return limpo


def avaliar(ferramenta: str, comando: str) -> Regra | None:
    """Devolve a primeira regra que o comando viola, ou None."""
    executado = sem_texto_literal(comando)
    for regra in REGRAS:
        if ferramenta not in regra.ferramentas:
            continue
        alvo = executado if regra.so_execucao else comando
        if regra.padrao.search(alvo):
            return regra
    return None


def _usuario_ja_cobre(nome: str) -> bool:
    """HARNESS §P12.2: o hook do repositório cede a vez ao do usuário de mesmo nome.

    Numa máquina em que `~/.claude/settings.json` já registra este hook, os dois rodariam a cada
    chamada — e no relógio isso duplica a linha da hora a cada turno (§F22, ruído). Aqui sai calado;
    nas outras máquinas (sem o hook do usuário), este é o que vale.
    """
    from pathlib import Path

    try:
        texto = (Path.home() / ".claude" / "settings.json").read_text(encoding="utf-8")
    except OSError:
        return False
    aqui = Path(__file__).resolve().parent
    do_usuario = (Path.home() / ".claude" / "hooks").resolve()
    return aqui != do_usuario and f".claude/hooks/{nome}" in texto.replace("\\", "/")


def main() -> int:
    # §A7: a mensagem de recusa tem acento; fora do hook o console cp1252 a quebraria (31/10/2026).
    try:
        sys.stdout.reconfigure(encoding="utf-8")
    except Exception:  # noqa: BLE001 — a guarda nunca derruba a sessão por defeito dela
        pass
    if _usuario_ja_cobre("guarda_shell.py"):
        print(json.dumps({}))
        return 0
    try:
        dados = json.load(sys.stdin)
    except (json.JSONDecodeError, ValueError):
        # 🔑 Guarda que quebra NAO trava o trabalho: na duvida, deixa passar.
        print(json.dumps({}))
        return 0

    ferramenta = str(dados.get("tool_name", ""))
    comando = str((dados.get("tool_input") or {}).get("command", "") or "")
    regra = avaliar(ferramenta, comando)
    if regra is None:
        print(json.dumps({}))
        return 0

    print(
        json.dumps(
            {
                "hookSpecificOutput": {
                    "hookEventName": "PreToolUse",
                    "permissionDecision": "deny",
                    "permissionDecisionReason": (
                        f"BLOQUEADO — {regra.nome} ({regra.fonte}).\n\n{regra.caminho_certo}\n\n"
                        "(Guarda de shell do HARNESS: este erro ja' e' regra escrita — "
                        "`~/.claude/hooks/guarda_shell.py`.)"
                    ),
                }
            },
            ensure_ascii=False,
        )
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
