# CLAUDE.md — Trilha AOCP Delegado Bahia

> ANTES DE QUALQUER AÇÃO, leia nesta ordem (pasta `0 Readme First/`):
>
> 1. `0 HARNESS.md` — INTEIRO. As regras não se consultam: cumprem-se.
> 2. `FAROL.md` — o estado atual e todas as tarefas.
> 3. `FERRAMENTAS.md` — o que já sabemos fazer, antes de dizer "não dá".
>
> Depois, confirme em 1 linha que leu e relate cada bloqueio ativo. As regras gerais estão em
> `C:\Users\advpi\Repositório\CLAUDE.md` e no HARNESS da pasta-mãe — inclusive a **Parte IV**, o
> método do roteiro de fundação, canônico para todo projeto desde 31/10/2026.

- **O que é:** app de estudo para o concurso de Delegado da Polícia Civil da Bahia 2026 (banca
  AOCP). Leia o `LEIA_PRIMEIRO.md`.
- **Pilha:** `index.html` único (HTML/CSS/JS, dados embutidos) + `servidor.py` (Python, só
  biblioteca padrão) que chama a API OpenAI ou Anthropic. Ferramentas de base em `ferramentas/`.
  ⚠️ **Fora da pilha do roteiro (§P4)** — de propósito: ela entra quando o Trilha virar
  funcionalidade do portal. O método (governança, portão, CI) já vale.
- **Portas:** app em `127.0.0.1:8765` (sobe com `iniciar_windows.bat`, só quando o titular for
  estudar) · **Storybook em `localhost:6006`** (`npm run storybook`).
- **Containers:** nenhum.
- ⚠️ **Fora do portal desde 01/11/2026 (D-009):** estudo pessoal do titular, *"ISSO SÓ PARA MINHA MAQUINA NÃO
  IRÃO PARA PORTAL DO PROFESSOR"*. A linha abaixo fica como registro do que valia antes (corrigido em 06/11/2026).
- 🏛️ ~~**Destino:** será uma funcionalidade do portal Pietro Medeiros (`../pietromedeiros-portal`),
  por ordem do titular de 31/10/2026 — ver o `CLAUDE.md` da pasta-mãe.~~ Decisão de arquitetura aqui
  pergunta *"isso encaixa no portal?"*.
- **Remoto:** `advpietromedeiros-sudo/trilha-aocp-delegado-bahia`, **privado** (D-001).
- 🔴 **`.env` tem a chave de API — não se lê** (§F59). O Storybook não serve pasta do disco por
  isso: as stories leem o `index.html` como texto.
- 🔴 Quatro assets derivados de terceiros ficam **fora do Git** (D-002, `docs/PROCEDENCIA.md`).

## Antes de qualquer commit

1. `npm run build-storybook` → rc 0.
2. **Portão:** `python docs/verificar_antes_de_subir.py` — Python compila, nenhum segredo no índice
   (a régua exige um valor de 20+ caracteres após o `=`, porque o `LEIA_PRIMEIRO.md` cita o nome da
   variável sem valor), a régua de segredo acusa, guarda de shell, relógio, registros em ordem.
3. **Pronto = CI verde no GitHub** (`gh run list --limit 3`).
