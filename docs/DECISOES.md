# DECISÕES — Trilha AOCP Delegado Bahia

> Registro de decisões do titular. Cada uma traz data, autor e o que trava enquanto estiver aberta.
> Decisão caduca quando a medição em que se apoiou muda (HARNESS §F49).

## Em aberto

| id | decisão pendente | aberta em | o que trava |
| --- | --- | --- | --- |
| D-003 | Aprovar (ou ajustar) a proposta de contraste e foco — story "Nesta sessão/Contraste e foco" | 31/10/2026 | Aplicar as cores no `index.html` |

## Tomadas

### D-001 — Repositório remoto privado (31/10/2026, titular)

Resposta do titular, escolhida entre opções, em 31/10/2026: *"Privado"*. O repositório
`advpietromedeiros-sudo/trilha-aocp-delegado-bahia` é **privado**. Motivo registrado no
`LEIA_PRIMEIRO.md`: o pacote não deve ser publicado.

### D-002 — Assets derivados de terceiros ficam fora do Git (31/10/2026, titular)

Resposta do titular, escolhida entre opções, em 31/10/2026: *"Deixar fora do Git"*. Os arquivos
`assets/fontes_paginas.json`, `assets/lei_seca_material.json`, `assets/juris_aocp.json` e
`assets/exemplo_aocp.json` ficam só no disco (`.gitignore`). Consequência: um clone do repositório
**não** tem a base local completa — ela se reconstrói com `ferramentas/` a partir dos materiais
originais, que também não estão no Git.
