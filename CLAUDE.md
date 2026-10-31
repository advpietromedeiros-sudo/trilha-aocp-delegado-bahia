# CLAUDE.md — Trilha AOCP Delegado Bahia

> As regras gerais estão em `C:\Users\advpi\Repositório\CLAUDE.md` e no HARNESS. Aqui só o que é
> deste projeto.

- **O que é:** app de estudo para o concurso de Delegado da Polícia Civil da Bahia 2026 (banca
  AOCP). Leia o `LEIA_PRIMEIRO.md`.
- **Pilha:** `index.html` único (HTML/CSS/JS, dados embutidos) + `servidor.py` (Python, só
  biblioteca padrão) que chama a API OpenAI ou Anthropic. Ferramentas de base em `ferramentas/`.
- **Portas:** app em `127.0.0.1:8765` (sobe com `iniciar_windows.bat`, só quando o titular for
  estudar) · **Storybook em `localhost:6006`** (`npm run storybook`).
- **Containers:** nenhum.
- 🏛️ **Destino:** será uma funcionalidade do portal Pietro Medeiros (`../pietromedeiros-portal`),
  por ordem do titular de 31/10/2026 — ver o `CLAUDE.md` da pasta-mãe. Decisão de arquitetura aqui
  pergunta *"isso encaixa no portal?"*.
- **Remoto:** `advpietromedeiros-sudo/trilha-aocp-delegado-bahia`, **privado** (D-001).
- 🔴 **`.env` tem a chave de API — não se lê** (§F59). O Storybook não serve pasta do disco por
  isso: as stories leem o `index.html` como texto.
- 🔴 Quatro assets derivados de terceiros ficam **fora do Git** (D-002, `docs/PROCEDENCIA.md`).

## Portões (cascata mínima, enquanto não houver `docs/CASCATA.md`)

1. `npm run build-storybook` → rc 0.
2. `python -I -m py_compile servidor.py ferramentas/*.py` → rc 0.
3. Nenhum segredo no índice:
   `git grep -l --cached -E "sk-(ant|proj)-|_API_KEY=[A-Za-z0-9_-]{20,}"` não lista nada (rc 1).
   A régua exige um valor de 20+ caracteres após o `=`: o `LEIA_PRIMEIRO.md` cita o nome da
   variável sem valor, e uma régua frouxa o acusava (31/10/2026).
