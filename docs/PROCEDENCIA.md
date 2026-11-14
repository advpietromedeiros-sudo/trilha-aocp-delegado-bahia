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

## 03/11/2026, 16h40 — Lei seca oficial do Planalto e súmulas oficiais no Treino de Discursiva (D-015)

- **O quê:** redação oficial de 16 leis federais, baixada de planalto.gov.br por `ferramentas/atualizar_lei_seca.py`, e o
  texto das súmulas do acervo oficial (`assets/sumulas.json`). Texto de lei e de ato oficial não tem proteção autoral
  (Lei 9.610/98, art. 8º, IV).
- **Onde:** `discursiva/artigos.js` (só os artigos e súmulas citados). O arquivo completo baixado fica fora do Git.
- **Material de terceiro:** nenhum. Doutrina, condução e pegadinhas são texto autoral desta sessão.

## 04/11/2026, 11h54 — Envio do Treino de Discursiva a um colega do titular, em arquivo único

- **Decisão do titular, por escrito no chat:** pediu *"um HTML para eu enviar para um colega aqui mas que funcione tudo
  localmente"*. Avisado de que o app contém a estrutura e trechos reescritos do PDF de modelos de peça (entrada de
  03/11/2026, 10h05, D-014), cuja autorização é dele e não do autor do material, escolheu a opção 1: **enviar completo,
  como está**, para uso pessoal do colega no estudo.
- **O que sai:** `Treino_Discursiva_Delegado_PCBA.html` (650.864 bytes), gerado por `ferramentas/empacotar_discursiva.py`
  a partir de `discursiva/`. Não leva o PDF, nem marca, nem dado pessoal. O envio é feito pelo titular, fora do repositório.
- ⚠️ A responsabilidade pelo trecho de terceiro no envio é do titular. O app continua fora do portal (D-009).

## 04/11/2026, 16h36 — Simulados DPC-BA comentados (Projeto em Delta), só na máquina do titular (D-017)

- **O quê:** questões objetivas e comentários dos Simulados 1 a 4 DPC-BA, curso preparatório de terceiro, transcritos
  dos PDFs por `ferramentas/importar_simulados_delta.py` para `discursiva/simulados_delta.js`.
- **Autorização:** ordem escrita do titular no chat, para seu estudo pessoal. **Sem** autorização do autor para
  distribuição: o arquivo fica **fora do Git** (`.gitignore`) e **fora do arquivo único de envio**.
- **Dado pessoal:** a marca d'água com CPF e código do comprador é retirada na importação; nada dela entra em arquivo do app.

## 06/11/2026, 22h07 — Provas AOCP e edital da PC-BA na revisão por prioridade (D-018, Fase 0)

- **Autorização:** pedido escrito do titular no chat (texto em D-018), para este material de estudo pessoal, que não vai
  para o portal (D-009).
- **Provas AOCP:** 24 cadernos em PDF na pasta Downloads do titular (`AOCP 01` a `06`, `AOCP INFO 01` a `06`, `AOCP
  PORTUGUES 01` a `08` e `DELEGADO`, `AOCP RAC LOG 01` a `03`), exportados de uma plataforma comercial de questões
  (marca e endereço dela em cada página). As questões são de provas públicas da banca; a seleção, a classificação por
  assunto e a montagem dos cadernos são da plataforma — por isso tratadas como **material de terceiro**.
  - **Onde ficou:** `revisao/dados/` (questões, gabaritos, texto bruto e OCR por página), **fora do Git** (`.gitignore`).
    No Git entram só o extrator autoral (`ferramentas/extrair_provas_aocp.py`) e os números agregados: ids do edital,
    contagens e ids das questões na plataforma em `revisao/mapa_prioridade.json` e `docs/REVISAO_PRIORIDADE.md`. Nenhum
    enunciado, alternativa ou comentário entra no Git.
  - **Dado pessoal:** nenhum encontrado nos cadernos (não há marca d'água de comprador).
- **Edital:** `../DELEGADO BA/EDITAL DELEGADO BAHIA.pdf` (edital do concurso, ato oficial, Lei 9.610/98, art. 8º, IV).
  Usados a Tabela 7.1 (p. 10) e a divisão do Anexo I (pp. 26–31). O PDF não está no repositório.
- **Estimativa de peso por disciplina:** média das contagens por disciplina dos 4 simulados DPC-BA (D-017). Entra no Git
  **só a contagem** (números), não questão nem comentário.

## Pente Fino de Direito Civil e Empresarial (07/11/2026, D-021)

- **Guia de temas e profundidade (sem cópia de texto):** PDFs de `DELEGADO BA/DIREITO CIVIL/` — Pessoas Naturais,
  Pessoas Jurídicas, Domicílio, Bens jurídicos, Direitos Reais, Fatos e negócios jurídicos, Prescrição e Decadência,
  Atos unilaterais e contratos, Contratos em espécie, Prova. Responsabilidade civil (partes 01 e 02), Direito das
  coisas e posse, LINDB, Aspectos cíveis na tutela das minorias…, Est. Pessoa com Deficiência (partes 01 e 02).
  Material de terceiro, uso pessoal, autorizado pelo titular na D-018; as assertivas e os comentários de
  `discursiva/pente_fino_civ.js` são texto próprio (conferido em janelas de 8 palavras: as coincidências são só
  enunciados oficiais e letra de lei). ⚠️ Os PDFs trazem marca d'água com dados pessoais do comprador: nada disso foi
  para o conteúdo, e as extrações de texto foram apagadas ao fim.
- **Letra de lei:** `assets/lei_seca_oficial.json` (Planalto). **Jurisprudência:** SCON e repetitivos do STJ, PDF
  oficial de súmulas e notícias do STF, conferidos em 07/11/2026.

## Pente Fino — reforço de Empresarial e Medicina Legal (07/11/2026, D-021)

- **Empresarial (CIV-4 títulos de crédito, CIV-5, CIV-11):** guia de temas pelos PDFs de Empresarial que estão (salvos
  por engano) em `DELEGADO BA/CRIMINOLOGIA/` — Títulos de crédito, Teoria Geral do Direito Empresarial, Espécies de
  Empresário, Teoria Geral do Direito Societário, Tipos Societários, Estabelecimento Empresarial, Nome Empresarial,
  Recuperação judicial e extrajudicial, Falência. Não usados: Sociedade Anônima, Marcas e Patentes, Trabalho do Preso.
- **Medicina Legal:** guia de temas pelo `DELEGADO BA/RESUMO DESTACADO-MEDICINA LEGAL.pdf` e pela apostila do próprio
  titular (`APOSTILA_TEORICA_VISUAL_MEDICINA_LEGAL_PIETRO_MEDEIROS.docx`, Downloads).
- Material de terceiro, uso pessoal (D-018). Texto das assertivas e dos comentários é próprio: conferência de janelas
  de 8 palavras contra o material (frases coincidentes reescritas; restam só enunciados oficiais e letra de lei).
  ⚠️ Os PDFs trazem marca d'água com dados pessoais do comprador: nada disso entrou, e as extrações foram apagadas.

## Pente Fino de Direito Processual Penal (08/11/2026, D-021)

- **Guia de temas e profundidade (sem cópia de texto):** `DELEGADO BA/RESUMO DESTACADO - DELEGADO PCPR - DIREITO
  PROCESSUAL PENAL.pdf` (só o sumário dos capítulos foi lido para calibrar o que cai e o nível) e a incidência AOCP de
  `revisao/mapa_prioridade.json` (CPP-2.1, 2.2, 7.6 e 8.5 à frente). Material de terceiro, uso pessoal (D-018).
- Texto das assertivas e dos comentários de `discursiva/pente_fino_cpp.js` (gerado de `ferramentas/pente_fino/cpp/`) é
  próprio: conferência de janelas de 8 palavras contra o material — as coincidências que sobram fora da letra de lei e
  das súmulas oficiais são paráfrases do próprio texto legal (grafia "4 anos" × "4 (quatro) anos", trema) ou de tese
  oficial do STF. ⚠️ O PDF traz marca d'água com dados pessoais do comprador: nada disso entrou (busca por CPF no
  conteúdo: zero), e a extração de texto foi apagada ao fim.
- **Letra de lei:** `assets/lei_seca_oficial.json` (Planalto), sem lei nova acrescentada. Citadas as redações de
  2025–2026 já presentes na base oficial: Lei 15.272/2025 (CPP, arts. 310, §§ 5º–6º, e 312, §§ 3º–4º), Lei
  15.280/2025 (art. 350-A), Lei 15.358/2026 (custódia por videoconferência, arts. 3º-B, § 1º, 310, 78, I, 313, V, e
  584, § 4º), Lei 15.438/2026 (decadência de 12 meses na violência doméstica, art. 38, § 2º), Lei 15.487/2026 (art.
  313, VI) e Lei 15.397/2026 (revogação do § 5º do art. 171 do CP: o estelionato volta à ação pública incondicionada).
- **Jurisprudência (conferida em 08/11/2026):** súmulas do STJ no SCON (processo.stj.jus.br/SCON/sumstj); súmulas do
  STF no PDF oficial; súmulas vinculantes 11, 14, 35 e 45 no portal do STF (data = publicação no DJe, a única que a
  página traz); notícias oficiais do STF para as ADIs 6.298/6.299/6.300/6.305 (24/08/2023), ADIs 3.360 e 4.109
  (11/02/2022), ADPFs 395 e 444 (14/06/2018), ADI 5.637 (11/03/2022) e HC 185.913 (18/09/2024); andamento dos Temas
  184 e 280/RG; Informativos 684, 735 e 818 do STJ (HC 598.886, RHC 158.580, HC 877.943). A `assets/sumulas.json` não
  foi usada como fonte.

## Pente Fino de Direito Penal — Parte Geral (08/11/2026, D-021)

- **Guia de temas e profundidade (sem cópia de texto):** `DELEGADO BA/RESUMO DESTACADO - DELEGADO PCPR - DIREITO PENAL
  - PARTE GERAL.pdf` (lido só o sumário dos capítulos para calibrar o que cai e o nível) e a incidência AOCP de
  `revisao/mapa_prioridade.json` (PEN-9.1, 1.1, 7, 1.2, 2.2, 3.1, 4.10, 6.6, 8.2, 8.3 e 8.11 à frente). Material de
  terceiro, uso pessoal (D-018).
- Texto das assertivas e dos comentários de `discursiva/pente_fino_pen.js` (gerado de `ferramentas/pente_fino/pen/`) é
  próprio: conferência de janelas de 8 palavras contra o material — 7 frases doutrinárias coincidentes foram reescritas;
  as que sobram fora da letra de lei e das súmulas/teses oficiais são paráfrase do texto legal ou de enunciado oficial
  (ex.: redação anterior da Súmula 545) ou vocabulário técnico corrente ("imputabilidade, potencial consciência da
  ilicitude e exigibilidade de conduta diversa"). ⚠️ O PDF traz marca d'água com dados pessoais do comprador: nada disso
  entrou (busca por CPF no conteúdo: zero), e as extrações de texto foram apagadas ao fim.
- **Letra de lei:** `assets/lei_seca_oficial.json` (Planalto), sem lei nova acrescentada. Citadas as redações de
  2024–2026 já presentes na base: Lei 14.994/2024 (CP, art. 92, §§ 1º e 2º), Lei 15.159/2025 (CP, art. 61, II, m; Lei
  8.072/1990, art. 1º, I-A), Lei 15.160/2025 (CP, arts. 65, I, e 115), Lei 15.358/2026 (CP, arts. 91-A, § 5º, e 92,
  IV; LEP, art. 112, V, VI e VIII), Lei 15.402/2026 (LEP, arts. 112, caput, e 126, § 9º), Lei 15.438/2026 (CP, art.
  103, par. ún.), Lei 15.487/2026 (CP, art. 92, § 2º) e Lei 14.843/2024 (LEP, arts. 112, § 1º, e 122, § 2º).
- **Jurisprudência (conferida em 08/11/2026):** 43 súmulas do STJ no SCON (processo.stj.jus.br/SCON/sumstj; a 545, e a
  630 só registrada em `pen_juris.py`, na redação revisada em 10/09/2025, Tema 1.194); 10 súmulas do STF no PDF
  oficial; Temas 585, 931, 1.077, 1.100, 1.172, 1.194 e 1.205 na página de repetitivos do STJ; Súmulas Vinculantes 26
  e 56 no portal do STF (data = publicação no DJe, a única que a página traz); notícias oficiais do STF para a ADPF
  779 (01/08/2023), o HC 176.473 (sessão virtual de 17 a 24/04/2020) e o Tema 788/RG (sessão virtual encerrada em
  30/06/2023); HC 84.412 (Segunda Turma, 19/10/2004, data citada nos acórdãos do STF). A `assets/sumulas.json` não foi
  usada como fonte.

## Pente Fino de Direito Penal — Parte Especial (08/11/2026, D-021)

- **Guia de temas e profundidade (sem cópia de texto):** `DELEGADO BA/RESUMO DESTACADO - DELEGADO PCPR - DIREITO PENAL
  - PARTE ESPECIAL.pdf` (lidos só os títulos dos capítulos para calibrar o que cai e o nível) e a incidência AOCP de
  `revisao/mapa_prioridade.json` (PEN-10.6, 10.7, 10.9, 10.10, 10.11 e 10.12 com incidência; os demais, zero).
  Material de terceiro, uso pessoal (D-018).
- Texto das 185 assertivas (PEN-10 a 10.14 e PEN-11) e dos comentários de `discursiva/pente_fino_pen.js` (gerado de
  `ferramentas/pente_fino/pen/pen_p10_01.py`, `pen_p10_02_06.py`, `pen_p10_07_10.py`, `pen_p10_11_14.py` e
  `pen_p11.py`) é próprio: conferência de janelas de 8 palavras contra o material — 1 frase coincidente fora da lei foi
  reescrita (privilégio da violenta emoção); as que sobram fora da letra de lei e das súmulas/teses oficiais são paráfrase
  do texto legal (penas escritas "1 a 4 anos" × "1 (um) a 4 (quatro) anos", tipos como "induzir alguém menor de 14
  anos a satisfazer a lascívia de outrem") ou o nome legal do crime ("induzimento a erro essencial e ocultação de
  impedimento", "registro não autorizado da intimidade sexual"). ⚠️ O PDF traz marca d'água com dados pessoais do
  comprador: nada disso entrou (busca por CPF e pelo nome do material nos arquivos novos: zero), e a extração de texto
  foi apagada ao fim. A Parte Geral não foi alterada (a reconstrução reproduz as 553 assertivas, item por item).
- **Letra de lei:** `assets/lei_seca_oficial.json` (Planalto), sem lei nova acrescentada; 177 citações de 118
  dispositivos (CP, Lei 8.072/1990, Lei 9.279/1996, Lei 9.609/1998, Lei 7.716/1989). Citadas as redações de 2023–2026
  já presentes na base: Lei 15.397/2026 (CP, arts. 155, caput e § 1º, 157, caput e § 3º, II, 171, § 2º, VII, e § 5º
  revogado, 180, caput, e 266), Lei 15.280/2025 (arts. 217-A, 218, 218-B, 218-C e 338-A), Lei 15.353/2026 (art.
  217-A, §§ 4º-A e 5º), Lei 15.384/2026 (art. 121-B; Lei 8.072/1990, art. 1º, I-C), Lei 15.358/2026 (art. 121, § 2º-D),
  Lei 15.402/2026 (art. 359-M-B), Lei 15.425/2026 (art. 282, §§ 3º e 5º), Lei 15.245/2025 (art. 288, §§ 1º e 2º), Lei
  Complementar 225/2026 (art. 168-A, § 5º), Lei 14.994/2024 (arts. 121-A, 129, § 13, e 147, §§ 1º e 2º), Lei
  14.811/2024 (Lei 8.072/1990, art. 1º, XI), Lei 15.035/2024 (art. 234-B, § 1º) e Lei 14.532/2023 (art. 140, § 3º; Lei
  7.716/1989, art. 2º-A).
- **Jurisprudência (conferida em 08/11/2026):** 33 julgados/súmulas na Parte Especial — 18 reaproveitados de
  `pen_juris.py` e 15 novos: Súmulas 24, 73, 502, 522, 542, 574 e 593 do STJ no SCON (processo.stj.jus.br/SCON/sumstj,
  data = "julgado em", nenhuma com indicação de cancelamento); Temas 157 (revisado, 28/02/2018), 934 (14/10/2015) e
  1.121 (08/06/2022) na página de repetitivos do STJ; Súmulas 603 e 714 do STF na página oficial de cada súmula
  (portal.stf.jus.br — a página traz só a publicação no DJ, e é essa a data usada, dita na fonte); notícias oficiais do
  STF para a ADPF 54 (12/04/2012) e a ADPF 496 (sessão virtual finalizada em 19/06/2020); andamento do Tema 1.003/RG
  (mérito em 24/03/2021, tese readequada nos embargos, sessão virtual de 02 a 12/06/2023). A `assets/sumulas.json` não
  foi usada como fonte.

## Pente Fino de Legislação Penal Extravagante (08/11/2026, D-021)

- **Guia de temas e profundidade (sem cópia de texto):** `DELEGADO BA/RESUMO DESTACADO - DELEGADO PCPR - LEGISLAÇÃO
  PENAL EXTRAVAGANTE.pdf` e `DELEGADO BA/Atualização - LPE - Lei 15.487 - 06 Ago 2026-1.pdf` (lidos só os títulos dos
  capítulos para calibrar o que cai e o nível) e a incidência AOCP de `revisao/mapa_prioridade.json` (LPE-8 à frente;
  LPE-4, 5, 9, 13, 16 e 30 com incidência; os demais, zero). Material de terceiro, uso pessoal (D-018).
- Texto das 430 assertivas e dos comentários de `discursiva/pente_fino_lpe.js` (gerado de `ferramentas/pente_fino/lpe/`)
  é próprio: conferência de janelas de 8 palavras contra os dois PDFs (11.237 janelas) — nenhuma frase doutrinária
  coincidente; as 79 janelas que sobram fora da letra de lei e dos enunciados oficiais são paráfrase do texto legal
  (penas escritas "reclusão de 2 a 5 anos e multa" × "2 (dois) a 5 (cinco) anos", tipos como "arma de fogo de uso
  permitido", "nota de culpa assinada pela autoridade", "menor de 14 anos com o fim de praticar ato libidinoso").
  ⚠️ Os PDFs trazem marca d'água com dados pessoais do comprador: nada disso entrou (busca por CPF e pelo nome do
  material nos arquivos novos: zero), e as extrações de texto foram apagadas ao fim.
- **Letra de lei:** `assets/lei_seca_oficial.json` (Planalto), **sem lei nova acrescentada** — as 40 leis do edital (e o
  Decreto 9.603/2018) já estavam na base; 418 citações de 276 dispositivos, em 43 diplomas. Citadas as redações de
  2025–2026 já presentes na base: Lei 15.358/2026, Lei 15.402/2026, Lei 15.487/2026, Leis 15.380, 15.383 e 15.384/2026,
  Lei 15.410/2026, Lei 15.517/2026, Lei 15.348/2026, Lei 15.355/2026, Lei 15.295/2025, Lei 15.234/2025, Lei
  15.163/2025, Lei 15.245/2025 e Lei Complementar 224/2025 (lista por dispositivo em `docs/PENTE_FINO_ESQUEMA.md`).
- **Jurisprudência (conferida em 08/11/2026):** 52 julgados/súmulas distintos — 23 reaproveitados de `pen_juris.py` e
  `cpp_juris.py` e 29 novos, em `lpe/lpe_juris.py`: Súmulas 108, 164, 265, 342, 492, 520, 533, 575, 587, 600, 605, 607 e
  639 do STJ no SCON (processo.stj.jus.br/SCON/sumstj, data = "julgado em", nenhuma com indicação de cancelamento; a
  439 também conferida, registrada e não usada); Súmulas 658, 660, 661 e 662 (notícia oficial do STJ de 15/09/2023,
  sessão de 13/09/2023), 664 (notícia de 09/11/2023, aprovada em 08/11/2023), 667 e 668 (notícia de 22/04/2024, sessão
  de 18/04/2024) e 669 (Livro de Súmulas do STJ, julgada em 12/06/2024); Súmulas 498, 703 e 720 do STF no PDF oficial;
  Súmula Vinculante 24 no portal do STF (data = publicação no DJe) e **SV 63** (notícia oficial de 30/09/2025 e
  Informativo 1.193 — PSV 125, sessão virtual finalizada em 25/09/2025); Tema 506/RG (Informativo 1.143, julgamento
  finalizado em 26/06/2024); Inq 4.435 AgR-quarto (notícia oficial, Plenário, 14/03/2019); RE 548.181 (Informativo 714,
  Primeira Turma, 06/08/2013). **Canceladas e não usadas como regra:** Súmula 512/STJ (SCON) e Súmula Vinculante 9
  (Informativo STF 1.193, PSV 60). A `assets/sumulas.json` não foi usada como fonte.

## Pente Fino de Informática (08/11/2026, D-021)

- **Guia de temas e profundidade (sem cópia de texto):** não há material de Informática em `DELEGADO BA/` (nenhum arquivo
  da disciplina na pasta; busca por Excel, PowerPoint, malware e navegador nos quatro resumos gerais e nos dois PDFs de
  lei seca anotada: zero). O nível e o estilo foram calibrados pelas 113 questões de
  Informática e Segurança da Informação dos cadernos AOCP em `revisao/dados/` (fora do Git; entrada de 06/11/2026) e
  pela incidência de `revisao/mapa_prioridade.json` (INF-3.6, 2.2, 3.1, 2.3 e 2.1 à frente). Nenhum enunciado entrou.
- Texto das 314 assertivas e dos comentários de `discursiva/pente_fino_inf.js` (gerado de `ferramentas/pente_fino/inf/`)
  é próprio: conferência de janelas de 8 palavras contra todos os 24 cadernos AOCP (78.680 janelas) — **zero**
  coincidências. Busca por dado pessoal de comprador nos arquivos novos: zero. A extração e o script de conferência
  ficaram em `.scratch/` e foram apagados ao fim.
- **Fontes técnicas oficiais (consultadas em 08/11/2026, WebFetch):** Suporte Microsoft em português — "Atalhos de
  teclado no Windows", "Atalhos de teclado no Word", "Atalhos de teclado no Excel", "Funções do Excel (por categoria)" e
  "Usar atalhos de teclado para fazer apresentações do PowerPoint"; Ajuda da Pesquisa Google, "Refinar pesquisas";
  Cartilha de Segurança para Internet (CERT.br/NIC.br); e a definição NIST SP 800-145 (2011). Cada item que depende
  delas traz a fonte e a data no resumo (77 itens).
- **Letra de lei:** `assets/lei_seca_oficial.json` (Planalto), **sem lei nova acrescentada**: CP, arts. 154-A (caput e
  §§ 1º e 2º, redação da Lei 14.155/2021), 154-B e 171, §§ 2º-A (redação da Lei 15.397/2026) e 2º-B — 6 citações de 3
  artigos. **Jurisprudência:** nenhuma. A `assets/sumulas.json` não foi usada.

## 09/11/2026, 11h2x — Material de revisão de curso (Partes 1 e 2) na aba Revisão (D-022)

- **O quê:** um material de revisão para a PC-BA, de um curso preparatório de terceiro: a "Parte 1" (Processo Civil e
  Tributário, 127 páginas) e a "Parte 2" (Constitucional e Ambiental, 140 páginas).
  - **Curso e nome do material:** a marca do curso e o nome do material constam do PDF; não se repetem aqui.
  - **Forma de chegada:** os PDFs vieram anexados no chat pelo titular; não estavam no disco.
- **Autorização:** pedido escrito do titular (texto em D-022), para seu estudo pessoal; o app não vai para o portal
  (D-009). **Sem** autorização do autor para distribuição.
- **Onde ficou, tudo fora do Git:**
  - PDFs, texto extraído, blocos e assertivas C/E derivadas: `revisao/material/nfpss/`;
  - o gerado: `discursiva/revisao_nfpss.js`;
  - nenhum dos dois vai no arquivo único de envio (`data-local`).
  - No Git entram só o verificador e o montador, que são autorais.
- **Dado pessoal:** toda página traz uma marca d'água com o CPF do comprador.
  - **Na extração:** a marca é retirada, e o verificador reprova qualquer número em formato de CPF nas assertivas.
  - **No repositório:** o CPF não está escrito em arquivo nenhum; o autoteste usa um número montado na execução.
- **As assertivas:** são texto novo, escrito sobre o conteúdo do material. Doutrina e julgados aparecem como o material
  os cita.

## 14/11/2026, 14h1x — Banco de questões discursivas (Penal e Processo Penal) na aba "900 Discursivas"

- **O quê:** um e-book de terceiro com ~900 **questões discursivas respondidas** de Direito Penal e Processual Penal
  (Parte 1 Penal, Parte 2 Processual, Parte 3 Legislação Especial em 20 temas). Dele extraímos **924 pares
  pergunta/espelho** para a aba "900 Discursivas" do Treino: o titular lê a pergunta, escreve a resposta e confere
  pelo espelho (a resposta modelo do autor).
  - **Autor e título:** constam do PDF; não se repetem aqui.
  - **Forma de chegada:** o PDF (protegido por senha) veio anexado no chat pelo titular; não estava no disco.
- **Autorização:** pedido escrito do titular (14/11/2026: *"QUERO QUE NO PROJETO DAS DISCURSIVAS ABRA UMA ABA SÓ PRA
  ESSE MATERIAL… EU LER A PERGUNTA E COM BASE NA RESPOSTA E NO ESPELHO FAZER A RESPOSTA"*), para seu estudo pessoal; o
  app não vai para o portal (D-009). **Sem** autorização do autor para distribuição.
- **Senha do PDF:** é do titular; **não** fica no repositório (§F59) — entra por `--senha` ou pela variável `QD_SENHA`
  na hora de importar.
- **Onde ficou, tudo fora do Git:**
  - PDF-fonte e texto extraído: `OneDrive/Trilha AOCP - versao completa (privada)/_fonte/` (fora do repositório);
  - o gerado: `discursiva/questoes_discursivas_penal.js` (no `.gitignore`, `data-local`);
  - não vai no arquivo único de envio nem no link público; entra só na cópia privada (embutido por
    `gerar_pacote_privado.py`).
  - No Git entram só o **importador** (`ferramentas/importar_discursivas.py`) e o **código da aba** no
    `Treino_Discursiva.html`, que são autorais.
- **Marca d'água (dado pessoal de terceiro):** toda página traz uma marca com o nome e o e-mail do licenciado do e-book.
  - **Na extração:** a marca é retirada (linhas com o identificador do licenciado são descartadas antes do parser).
  - **No repositório:** esse nome e esse e-mail **não** estão escritos em arquivo nenhum.
- **As perguntas e os espelhos** são conteúdo do autor do e-book (material de terceiro); ficam só na cópia privada.
