# FERRAMENTAS — Trilha AOCP Delegado Bahia

> Consultar **antes** de dizer "não dá". Versões medidas em 31/10/2026, na estação do titular.

| comando | o que faz |
| --- | --- |
| `iniciar_windows.bat` | sobe o app em `127.0.0.1:8765` (lê o `.env` — o titular, não a IA) |
| `atualizar_lei_seca.bat` | baixa a redação oficial das leis do edital no Planalto |
| `npm run storybook` | Storybook 10.6.5 na porta 6006 (⚠️ o roteiro fixa 10.5 — divergência anotada) |
| `npm run build-storybook` | compila as stories (porta do portão) |
| `python docs/verificar_antes_de_subir.py` | o portão: todas as portas |
| `python .claude/hooks/testar_guarda.py` | um caso que recusa e um que passa por regra da guarda |
| `gh run list --limit 3` | estado da CI |

Máquina: Node 26.13.0 (canônico 24) · Python 3.11.9 · gitleaks 8.30.1 · ruff 0.17.1 · `gh` logado
como `advpietromedeiros-sudo`.
