# PROCEDÊNCIA — o que veio de fora (HARNESS §G8.3)

> Um registro por material. Origem, data, como o acesso foi obtido e sob qual cláusula.
> Classificação feita em 31/10/2026 pela sessão, a partir dos nomes dos arquivos e do
> `ferramentas/construir_base.py`; a origem exata de cada um **ainda não foi conferida com o titular**.

| arquivo | origem (como classificado em 31/10/2026) | no Git? | cláusula |
| --- | --- | --- | --- |
| `assets/items.json` | Anexo I do edital SAEB 02/2026 (verticalizado) — documento público | sim | ato oficial |
| `assets/sumulas.json` | Súmulas do STF e do STJ — texto oficial | sim | ato oficial |
| `assets/teses_rg.json` | Teses de repercussão geral — texto oficial | sim | ato oficial |
| `assets/catalogo_leis.json` | Catálogo de diplomas legais (títulos e URLs oficiais) | sim | ato oficial |
| `assets/acervo_oficial_curado.json` | Seleção curada de material oficial | sim | ato oficial — **conferir** |
| `assets/banco_inicial.json` | Questões autorais do projeto | sim | autoria do titular |
| `assets/fontes_paginas.json` | Índice de páginas de PDFs de cursos de terceiros | **não** (D-002) | sem autorização registrada |
| `assets/lei_seca_material.json` | Texto de lei extraído de material de estudo | **não** (D-002) | sem autorização registrada |
| `assets/juris_aocp.json` | Precedentes compilados de material de estudo | **não** (D-002) | sem autorização registrada |
| `assets/exemplo_aocp.json` | Exemplo de questão no padrão da banca | **não** (D-002) | sem autorização registrada |

⚠️ **Pendência:** o `index.html` embute `items-data` e `official-curated` (cópias de
`items.json` e `acervo_oficial_curado.json`) e `seed-data`. Medido em 31/10/2026, por amostra de
até 50 trechos longos de cada arquivo fora do Git: `fontes_paginas` 0, `juris_aocp` 0 e
`exemplo_aocp` 0 trechos no HTML; `lei_seca_material` 18 de 50 — todos **URLs oficiais do
Planalto** presentes também em `official-curated`, não texto de terceiro. Amostra prova o que
apareceu, não o que não está (§F20): conferir de novo antes de cada mudança no bloco de dados.
