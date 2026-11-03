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

## Ampliação do índice `assets/fontes_paginas.json` (31/10/2026, 19h38)

Pedido do titular, 31/10/2026, textual: *"No Desktop tem a pasta DELEGADO BA... TEM UNS MATERIAIS
NOMEADOS COMO DO PARANÁ MAS O CONTEÚDO É O DA BA TAMBÉM... pode usar"*. Indexados por
`ferramentas/ampliar_acervo.py`, **só na máquina do titular** — o índice segue fora do Git (D-002).
O texto das páginas vai, em trechos, para a API de IA escolhida no momento da geração (como já
acontecia com o índice anterior; ver `LEIA_PRIMEIRO.md`, "Privacidade e custos").

| material (pasta `Área de Trabalho/DELEGADO BA`) | páginas indexadas | uso |
| --- | ---: | --- |
| 9 resumos de curso por disciplina ("Resumo Destacado") | 5.124 | local, autorizado pelo titular |
| Informativos 2023–2026, Súmulas STF/STJ/TSE, Teses RG, Repetitivos (compilações de curso) | 1.790 | local, autorizado pelo titular |
| ZIP "PCPR-1": 26 resumos de leis extravagantes | 1.136 | local, autorizado pelo titular |
| ZIP "PCPR-2": 16 resumos de Penal, parte geral (PCPR-3 e 4 são cópia e foram pulados) | 562 | local, autorizado pelo titular |

Total acrescentado: **8.612 páginas** (5.124 + 1.790 + 1.136 + 562, somado pelo relatório da
ferramenta); índice de 744 → **9.356**. A marca d'água com o CPF do
licenciado **não entra** no índice (mesmo filtro do `construir_base.py`; conferido: 0 linhas com
padrão de CPF). ⚠️ Os Informativos 2026 podem trazer julgados posteriores ao marco do edital
(29/07/2026); o servidor não os marca como posteriores — o prompt manda não aplicar norma posterior.

⚠️ **Pendência:** o `index.html` embute `items-data` e `official-curated` (cópias de
`items.json` e `acervo_oficial_curado.json`) e `seed-data`. Medido em 31/10/2026, por amostra de
até 50 trechos longos de cada arquivo fora do Git: `fontes_paginas` 0, `juris_aocp` 0 e
`exemplo_aocp` 0 trechos no HTML; `lei_seca_material` 18 de 50 — todos **URLs oficiais do
Planalto** presentes também em `official-curated`, não texto de terceiro. Amostra prova o que
apareceu, não o que não está (§F20): conferir de novo antes de cada mudança no bloco de dados.

## Apostilas atualizadas por tema (01/11/2026, 15h33)

Autorização do titular: D-009 (uso só nesta máquina, para estudo pessoal). Pasta
`Repositório/DELEGADO BA/` — apostilas de curso preparatório de terceiro, "Atualizado em 10/09/26",
material pago licenciado a outra pessoa, com marca d'água de identificação. Índice **local e fora do
Git** (D-002), como o restante.

| subpasta | PDFs | páginas lidas → indexadas | disciplina no índice |
| --- | ---: | ---: | --- |
| `DIREITO CONSTITUCIONAL` | 30 | → 796 | DIREITO CONSTITUCIONAL |
| `DIREITO ADMINISTRATIVO` | 19 | → 687 | DIREITO ADMINISTRATIVO |
| `DIREITO AMBIENTAL` | 7 | → 292 | DIREITO AMBIENTAL |

Total: 56 PDFs, 1.887 páginas lidas, **1.775 indexadas** (as de menos de 120 caracteres ficam de fora,
mesma regra de sempre). Índice: 9.356 → **11.131** páginas (744 + 10.387, somado pela ferramenta).

**Dado pessoal da marca d'água — medido antes de gravar:** o texto cru das 1.887 páginas tem 3.666
linhas de marca d'água com CPF (controle: o teste enxerga o dado); depois do filtro, **0** CPF, **0**
ocorrências do nome do licenciado e **0** e-mails. Conferido de novo no índice inteiro depois de
gravar: **0** número de CPF e **0** rodapé "Material protegido". O nome, o CPF e o e-mail do licenciado
**não foram escritos** em nenhum arquivo nem no chat. A ferramenta ganhou uma trava que recusa gravar
se o número de CPF ou o rodapé escaparem, com `--autoteste`.

⚠️ Material atualizado em 10/09/2026 pode trazer regra posterior ao marco do edital (29/07/2026); o
prompt do servidor já manda não aplicar norma posterior.

## 02/11/2026, 20h46 — Lei seca comentada usada só para conferência (Treino de Discursiva)

- **O quê:** 9 PDFs de lei seca comentada de curso preparatório, enviados pelo titular no chat.
- **Uso:** só para conferir o texto legal (público, Lei 9.610/98, art. 8º, IV) ao escrever `discursiva/leis.js`.
- **Não entrou:** nenhum comentário, quadro, esquema ou marca do material. Os PDFs não estão no repositório.

## 03/11/2026, 08h39 — Modelos de peça prática de curso preparatório usados só para conferência (Treino de Discursiva)

- **O quê:** 1 PDF de modelos de peças práticas de Delegado, enviado pelo titular no chat.
- **Uso:** só como lista de conferência dos tipos de peça e do que os espelhos pontuam (D-013); o texto legal foi conferido na lei.
- **Não entrou:** nenhum modelo, comentário, quadro, esquema ou marca do material. O PDF não está no repositório.

## 03/11/2026, 10h05 — O mesmo PDF de modelos de peça: uso do texto autorizado pelo titular (D-014)

- **Autorização:** do titular, por escrito no chat (texto em D-014). ⚠️ É autorização **do titular**, não do autor do
  material; o app é de uso pessoal, só nesta máquina e no repositório privado (D-009), e **não vai para o portal**.
- **O que entrou:** a estrutura das representações (sequência de tópicos e o tópico "inexistência de direitos fundamentais
  absolutos") e trechos de redação dos modelos, reescritos e corrigidos na lei. Enunciados, cartões e mnemônicos são autorais.
- **Não entrou:** quadros, comentários, marca, links e o PDF em si, que segue fora do repositório.
