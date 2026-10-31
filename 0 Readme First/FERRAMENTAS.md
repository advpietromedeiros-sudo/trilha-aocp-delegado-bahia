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
| `python ferramentas/ampliar_acervo.py [pasta] [--simular]` | acrescenta PDFs da pasta DELEGADO BA ao índice de busca (aditivo; guarda cópia do índice anterior em `.scratch/`) |
| `python docs/testar_servidor.py` | servidor dos blocos com API simulada (sem gastar e sem ler o `.env`) |
| `node docs/testar_blocos.mjs` / `node docs/testar_espera.mjs` | comportamento real do script da tela, com servidor simulado |
| `node docs/testar_pagina.cjs` | a página real carrega sem erro de JavaScript (jsdom) |
| `cache/*.json` → campo `metricas` | duração, chamadas e tokens de cada questão gerada (desde a v8) |
| `historico/Trilha_historico_acumulado.html` | o histórico acumulado, regravado a cada bloco (fora do Git) |

Máquina: Node 26.13.0 (canônico 24) · Python 3.11.9 · gitleaks 8.30.1 · ruff 0.17.1 · `gh` logado
como `advpietromedeiros-sudo`.
