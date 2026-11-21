# FAROL — Trilha AOCP Delegado Bahia

> Estado, tarefas e o que ficou rodando. Atualizado a cada ~15 min de trabalho e no fechamento.

**Última atualização:** 20/11/2026, 19h41.

## Estado

- 🆕 **20/11/2026, 19h41 — Discursivas em Stories ampliado para 9 blocos / 39 questões** (pedido do titular "amplie os
  blocos"). Acrescentados: **Administrativo** (poder de polícia, ato adm., improbidade, resp. civil do Estado,
  licitações 14.133), **Direitos Humanos** (características, status dos tratados, sistemas, convencionalidade), **Civil**
  (personalidade/incapacidade, prescrição×decadência, resp. civil, posse), **Criminologia** (escolas, labeling,
  prevenção, vitimologia) e **Medicina Legal** (energias/lesões, tanatologia, sexologia, documentos). Tudo autoral.
  `testar_discursivas_stories.cjs` verde + autoteste; Portão 43; pacote privado regenerado.

- 🆕 **20/11/2026, 11h24 — Novo módulo "Discursivas em Stories"** (pedido do titular: transformar o material em questões
  discursivas na metodologia dos Stories, em blocos). `discursiva/Discursivas_Stories.html` + `discursivas_stories_dados.js`,
  14ª aba do hub. Cada questão tem **enunciado fixo** e você toca para revelar **um ponto-chave da resposta por vez**
  (recordação da estrutura), com barrinhas de progresso, placar de bloco e retomada da posição. **4 blocos / 18 questões**
  autorais: Penal (5), Processo Penal (5), Constitucional (3), Legislação Penal Especial (5). Modo celular + grifo (tecla G).
  Provas: `docs/testar_discursivas_stories.cjs` 12/12 + autoteste; hub p/ 14 abas; **Portão 43**; pacote privado ganhou a tela.
  Conteúdo autoral (lei seca + doutrina), nada de terceiro. ⏳ Dá para ampliar blocos (Administrativo, Dir. Humanos, Civil…).

- 🆕 **20/11/2026, 10h30 — Lei Antifacção (15.358/26) na Lei na Íntegra + Modo celular reforçado.** (1) A pedido do
  titular ("uns Stories para decorar todo esse conteúdo"), a **Lei Antifacção** virou novo diploma `L.15.358` em
  `lei_integra_dados.js` — **34 cartas** autorais (crimes dos arts. 2º/3º, penas 20-40 e 12-20, facção = 3+ pessoas,
  insuscetibilidades, hediondez, prazos do IP 90/270, medidas assecuratórias, confisco ampliado, Banco de Dados e as
  alterações em CP/CPP/LEP). Vira uma capa nova na Biblioteca e estuda-se nos 4 modos, inclusive **Stories**. Fonte:
  PDF de terceiro (DD LEGIS); só o texto oficial/público entrou (ver `docs/PROCEDENCIA.md`). Módulo agora com **100
  artigos**. (2) Modo celular: o **conserto do Teste**, a **letra maior**, os **rótulos do Stories** e a **retomada
  do Stories** (continua de onde parou ao atualizar/sair) entraram ao longo de 19–20/11. `testar_lei_integra.cjs`
  verde + autoteste; Portão 41.

- 🆕 **19/11/2026, 16h57 — Kindle + Stories implementados na Lei na Íntegra** (titular: "Kindle pode fazer").
  A home virou **estilo Kindle**: "Retomar" (último artigo estudado, salvo em `leiintegra:v1.last`) + **Biblioteca em
  capas por diploma** (CF/CP/CPP/CC/CPC/CTN, com % estudado); tocar numa capa abre a lista do diploma. Novo **4º modo
  Stories** (pegada Instagram): tela cheia com barrinhas de progresso no topo, um slide por lacuna, toque à direita
  revela/avança, à esquerda volta, ✕ fecha, slide final de "fim". Entra por "▶ Stories deste artigo" (no leitor) e
  "▶ Treinar <diploma> em Stories" (na tela do diploma), puxando os 66 artigos reais. `testar_lei_integra.cjs` 19/19
  (home Kindle, capa→artigo, 3 modos, Stories) + autoteste; Portão 41; pacote privado regenerado (86,7 KB).

- 🆕 **19/11/2026, 16h19 — Modo Teste consertado + protótipo "Kindle + Stories".** (1) O Teste da Lei na Íntegra
  não funcionava (`render()` reiniciava o contador a cada toque — o titular "não consegui usar"); separei navegação
  (`abrir`) de re-render (`render`) e redesenhei como autoteste: lacuna a lacuna, "Revelar" → "Acertei/Errei" →
  placar (X de N, %) + "Refazer". `testar_lei_integra.cjs` cobre o fluxo; commit `5138502`, CI verde, Portão 41.
  (2) Protótipo aprovado p/ commit (`e9123a0`): `stories/kindle-stories.stories.js` — home estilo Kindle (Retomar +
  Biblioteca em capas + barra inferior) + modo **Stories** (tela cheia, barrinhas no topo, toque revela/avança),
  em "Aguardando Análise" no Storybook. ⏳ **Falta implementar de verdade** (home-launcher real + Stories como 4º
  modo na Lei na Íntegra puxando os 66 artigos) quando o titular aprovar.

- 🆕 **19/11/2026, 15h11 — Lei na Íntegra: Fase 3 (CC + CPC + CTN).** A pedido do titular ("faça, mas antes me envie
  o link"). Enviados e conferidos (HTTP 200, versão no ar) os links públicos do projeto. Depois ampliei a aba de 40
  para **66 artigos inteiros**: + CC 10 (personalidade, incapazes, atos ilícitos, abuso, responsabilidade civil),
  CPC 9 (normas fundamentais, inércia, poderes do juiz, tutela de urgência, ônus da prova, sentença, precedentes) e
  CTN 7 (tributo, imposto, taxa, legalidade, obrigação, lançamento, extinção). 0 duplicata; `testar_lei_integra.cjs`
  verde + autoteste; Portão 41/41. Pacote privado regenerado (Lei na Íntegra 76,3 KB). Links do app:
  https://advpietromedeiros-sudo.github.io/trilha-aocp-delegado-bahia/discursiva/Lei_na_Integra.html

- 🆕 **19/11/2026, 14h10 — Lei na Íntegra ampliada p/ o núcleo do Delegado + pacote privado com o projeto inteiro**
  (pedido do titular, 14h00: *"complete, pode fazer todo e gerar o HTML com todo projeto"*). `lei_integra_dados.js`
  foi de 6 para **40 artigos inteiros**: CF 14 (fundamentos, direitos do art. 5º, nacionalidade, direitos políticos,
  Judiciário/STF, MP, defesa do Estado, segurança pública), CP 16 (anterioridade, lei no tempo, causalidade, dolo/culpa,
  erro, excludentes, concurso, penas, dosimetria, extinção) e CPP 10 (IP, ANPP, prova, prova ilícita, cautelares,
  prisão, custódia, preventiva, absolvição sumária). `docs/testar_lei_integra.cjs` segue verde + autoteste; Portão 41/41.
  **Pacote privado agora traz o PROJETO INTEIRO:** `gerar_pacote_privado.py` ganhou Letra de Lei, Lei na Íntegra e
  Revisão (antes só Treino + Olho). Regenerado em `C:/Users/advpi/OneDrive/Trilha AOCP - versao completa (privada)/`:
  Treino 21,1 MB · Olho 7,6 MB · Letra de Lei 273,8 KB (c/ Bloco 16) · Lei na Íntegra 63,5 KB · Revisão 245,6 KB.
  ⏳ **OneDrive app não instalado nesta máquina** — a pasta existe mas não sincroniza sozinha; o titular sobe pelo
  onedrive.live.com ou instala o app. Rodar o gerador de novo a cada atualização dos dados.

- 🆕 **19/11/2026, 11h35 — Nova aba "Lei na Íntegra" no Treino de Letra de Lei** (pedido do titular às 08h47/11h16,
  a partir de telas de um app concorrente). Módulo próprio `discursiva/Lei_na_Integra.html` + `lei_integra_dados.js`,
  ligado como 13ª aba do hub (`Treino_Discursiva.html`). Estuda o **artigo inteiro** (caput + incisos + §) em **3
  modos** saindo do mesmo registro: 🙈 Esconder & lembrar, 🎯 Teste (uma lacuna por vez), 📖 Revisão (secundário
  apagado, essencial grifado + mnemônico). "!" nos incisos mais cobrados; **áudio** por `speechSynthesis` (nativo,
  sem terceiro). Fase 1 com **CF 1º, 2º, 3º, 4º, 5º e 37** (a maior lacuna medida). Paleta de grifos (tecla G)
  embutida. Provas: `docs/testar_lei_integra.cjs` 12/12 + autoteste acusa; hub ajustado p/ 13 abas; **as 8 portas
  `docs/testar_*.cjs` verdes** e `build-storybook` verde. Protótipo do visual ficou no Storybook (`stories/lei-integra.stories.js`,
  "Aguardando Análise"), aprovado pelo titular ("PODE IMPLEMENTAR"). ⏳ **Fase 2:** ampliar p/ CF alta incidência + CPP/CP.

- 🆕 **21/11/2026, 20h — Bloco 17 "Complementos AOCP" no Treino de Letra de Lei.** Pedido do titular: conferir se o
  anexo "LD - AOCP - Delegado" (135 págs, lei seca destacada — material de terceiro com marca d'água de CPF; só a
  seleção de temas serviu de guia, nada entra no Git; ver `docs/PROCEDENCIA.md`) já estava coberto, e pôr o que
  faltava no Bloco 17. Cruzei o índice das 849 cartas: quase tudo já estava (CP/CPP/CF/CTN, Leis 8.112/8.429/8.987,
  Maria da Penha, Drogas, Orcrim, Abuso, LEP, Tortura, Ambiental, LINDB, posse, súmulas). Faltava: **ECA
  proteção/socioeducativo, Empresarial (CC 978/991/1.039/1.147; Lei 11.101 art. 2º/3º/20-A/76), Súmula 606-STF,
  CF 5º §4º, CPP 401, julgados avulsos (Vicuña, concorrência de culpas, pertenças, corte de energia) e Direitos
  Humanos/tratados (SV 25, RE 466343, HC 171118, ADPF 496/347, ADI 3239, RE 511961, Convenção da ONU contra a
  Tortura, DUDH, Res. 34/169)**, mais um núcleo Eleitoral sinalizado como AOCP genérico. **+46 cartas** autorais de
  lacuna, 0 inválida, lacunas == respostas. Portão do teste ajustado de 16→17 blocos. **17 blocos / 895 cartas.**

- 🆕 **19/11/2026, 09h06 — Bloco 16 "Lei Seca AOCP III (Constitucional + Processo)" no Treino de Letra de Lei.**
  Pedido do titular (08h47: *"veja o que tem no DECORANDO A LEI SECA 02 que não tem ainda nos blocos e coloque no
  próximo bloco"*). Cruzei o guia de incidência "DECORANDO A LEI SECA 02" (584 págs, material de terceiro — só a
  incidência serviu de bússola, nada entra no Git; ver `docs/PROCEDENCIA.md`) contra as 724 cartas dos Blocos 1 a 15:
  a maior lacuna era a **Constituição**. Acrescentadas **125 cartas** autorais de lacuna (CF 92, CPC 11, CPP 9,
  CP 7, CC 3, CTN 3), 0 duplicata, lacunas == respostas. Portão do teste ajustado de 15→16 blocos. **16 blocos /
  849 cartas.** Cascata verde e medida: as 7 portas `docs/testar_*.cjs` em exit=0; autoteste acusa o defeito plantado.

- 🆕 **14/11/2026, 11h01 — Cópia privada completa (opção 1 do titular):** `ferramentas/gerar_pacote_privado.py` gera Treino (19,9 MB) e Olho de Águia (7,6 MB) em arquivo único em `C:/Users/advpi/OneDrive/Trilha AOCP - versao completa (privada)/` (fora do Git). Conferido no Chrome: 0 erro, dados presentes. ⏳ **O aplicativo do OneDrive não está instalado nesta máquina** (a pasta existe, o programa não): a pasta não sobe sozinha — o titular envia pelo onedrive.live.com ou instala o app. Rodar de novo o gerador depois de cada atualização dos dados.

- 🆕 **14/11/2026, 10h16 — Repositório público (D-025) e paleta de grifos ampliada.** Link: https://advpietromedeiros-sudo.github.io/trilha-aocp-delegado-bahia/ — Treino abre sem erro de JavaScript no link (conferido no Chrome), mas Simulados, Revisão e Olho de Águia ficam sem dados lá (material de terceiro fora do Git). Paleta (tecla G): 9 cores (+ lilás, vermelho, turquesa, cinza), Negrito (B) e Sublinhado (U), que se somam a uma cor; `docs/testar_grifa.cjs` 32 conferências, autoteste 3/3; commit 8ac6cd3, CI verde.

- 🆕 **12/11/2026, 22h43 — Olho de Águia: comentários mais fáceis de entender** (pedido do titular, 22h36). Só apresentação, sem mexer nos dados. Simulados: cada alternativa errada em três linhas (o erro está em / o certo é / por quê), a correta com "por que é a certa", aviso em destaque nas 57 que pedem a INCORRETA, esquema com rótulos ("em uma frase", "o que você precisa saber", "como a AOCP tenta te enganar"). Assertivas: tema acima da frase; versão errada da banca ao lado da certa, com as palavras trocadas destacadas (sem riscado); descrição da manobra separada de nota de detalhe; "Para memorizar" sempre visível. Prova: `docs/testar_olho_de_aguia.cjs` 18/18 (3 provas novas), prints conferidos; portão 35/35.

- 🆕 **12/11/2026, 08h05 — Olho de Águia (D-024), pedido do titular para a reta final** (prova 06/12, 3 h/dia):
  `discursiva/Olho_de_Aguia.html`, atalho "🦅 Olho de Águia" no Treino. Esquerda: os **400** simulados resolvidos, com o
  trecho errado grifado em cada alternativa errada (nas **57** que pedem a INCORRETA, só o gabarito) e o comentário
  esquematizado. Direita: **10.481** assertivas corretas da Revisão + Pente Fino em **105 blocos de 100**, por importância
  (peso da disciplina, lei atual, núcleo do Delegado, letra de lei, jurisprudência), com a pegadinha AOCP. Metas do dia
  recalculadas pelo ritmo medido. Prova: `docs/testar_olho_de_aguia.cjs` (14/14 com os dados reais; autoteste acusa);
  portão 35/35.
  - ⏳ **Falta:** pegadinhas dos blocos 21–105 (4.447), em ondas; conferir 6 gabaritos marcados "⚠ Conferir" e a S1 q12
    (frações perdidas na importação); story do Storybook.

- ✅ **10/11/2026, 22h23 — Simulados: quadro "Não esqueça as exceções" com frase cortada** (imagem do titular,
  22h18). Causa: a oração de exceção era cortada em 64 caracteres, limite pensado para o realce vermelho dentro do
  parágrafo; no quadro o trecho aparece sozinho. Agora o quadro leva a oração até a pontuação (acima de 260
  caracteres, termina em "…"), e tabela, fórmula e conta ficam fora do quadro (achatadas, davam frase embaralhada).
  Prova: `docs/testar_blocos_simulados.cjs` confere os 173 itens do quadro nos 400 comentários reais; portão 33/33
  e `testar_pente_fino.mjs` 28/28 às 22h23.

- ✅ **10/11/2026, 20h32 — Parte 3 da Revisão montada:** os 34 blocos com rc 0 no verificador (varredura das 20h28),
  **4.594 assertivas**; `discursiva/revisao_nfpss.js` regravado (6.942,5 KB) com **7.377** no total (Partes 1 a 3).
  - ✅ **22h48 — aprofundamento da Parte 3 concluído** (pedido do titular às 22h02): 22 lotes (4.594 itens) em
    `.scratch/aprofundar3/`, todos `[OK ]` no `validar_aprofundamento.py`; `juntar.py` gravou ADM, CIV, CPP, CRI, IGR,
    LEG, LPE e PEN em `revisao/material/nfpss/aprofundar/` (fora do Git); `revisao_nfpss.js` remontado (11.379,1 KB).
    Medido na saída montada: **7.377 de 7.377** assertivas com aprofundamento e **3.327 de 3.327** E com correção
    (`.scratch/aprofundar3/gen/conferir_saida.py`); `testar_discursiva.cjs` verde com o arquivo real.
    Pontos apontados pelos redatores no item original: `revisao/material/nfpss/CONFERIR_P3.md`.
  - ⏳ **Falta também:** conferir na fonte as
    divergências de `revisao/material/nfpss/CONFERIR_P3.md` (~60 itens; vários escritos "de memória" pelos redatores).
- 🆕 **10/11/2026, 20h17 — Paleta de grifos (tecla G), pedido do titular:** fonte única `assets/grifa.js`, embutida
  por `ferramentas/embutir_grifa.py` no `index.html`, no Treino de Discursiva, no molde da Revisão e nos 5 cadernos
  de `revisao/saida/`. Prova: `docs/testar_grifa.cjs` (24 conferências + 2 telas reais; autoteste com 3 defeitos);
  4 portas novas no portão (33 de 33 verdes às 20h27). Story: `Nesta sessão/Paleta de grifos (tecla G)`.
  - ✅ **Autorizado pelo titular às 20h36 (D-023)** e subido no Git. A story está em `Aguardando Análise` até a
    aprovação visual.
  - 🔧 **21h47 — barra vertical na borda direita** (pedido do titular: a caixa no canto de baixo ficava em cima das
    palavras). Só ícones, ajuda no `title`; aberta, a página reserva 54 px à direita para a barra não cobrir nada.
    Conferido em print do Chrome (1366 px) no `index.html` e no Treino. ⚠️ Celular **não conferido** (o Chrome
    headless do Windows não renderiza abaixo de ~500 px).
  - ⚠️ **Limites declarados:** grifo salvo por navegador e por tela (não vai no backup do app); o histórico
    acumulado (`historico/`) não tem a paleta; teste em jsdom, sem prova num Chrome real.

- 🆕 **10/11/2026 — Parte 3 da Revisão (D-022), EM ANDAMENTO.** O titular subiu o PDF às 13h22 (414 páginas,
  8 disciplinas) e escolheu gerar **tudo, em ondas** (15h1x).
  - ✅ Texto extraído (`revisao/material/nfpss/parte3.txt`, sem CPF) e dividido por
    `revisao/material/nfpss/limpar_parte3.py` em **34 blocos**: IGR01-02, LEG01, ADM01-05, CIV01-05, CRI01-03,
    PEN01-08, CPP01-05, LPE01-05. Brief: `revisao/material/nfpss/BRIEF_P3.md` (com o negrito da §G6.6).
  - ⏳ **Onda 1 (15h2x):** PEN01 a PEN08 e CPP01. **Medido às 20h04:** 5 de 9 prontos no verificador (rc 0) —
    CPP01 149, PEN01 149, PEN02 140, PEN03 159 e PEN07 114 itens (711); PEN04, PEN05, PEN06 e PEN08 **sem nenhum
    arquivo** (os redatores morreram com a sessão anterior).
  - ⏳ **Retomada às 20h05:** PEN04, PEN05, PEN06, PEN08 e a onda 2 de Processo Penal (CPP02 a CPP05), 8 redatores.
    **20h07:** onda 3 solta (LPE01 a LPE05) — 13 redatores em paralelo. **20h09:** PEN08 (73) e CPP05 (64) com
    rc 0, conferido pela sessão principal; CRI01 e CRI02 soltos.
  - **20h17 — 20 de 34 blocos concluídos com rc 0** (conferidos pela sessão principal): CPP01-05, PEN01-08,
    LPE01-03, LPE05, CRI01-03. Varredura dos 34 às 20h17: 21 com rc 0 e **2.584 itens** — o 21º é o LPE04, que passa
    mas o redator ainda escrevia (não conta como concluído, §F37). Rodando: LPE04, ADM01-05, CIV01-05, LEG01; IGR01-02
    soltos às 20h17. ⚠️ *Correção:* o relato das 20h14 dava 17 blocos (CPP04 incluso) — eram 16; o CPP04 só fechou
    às 20h17.
  - 📋 Divergências dos redatores em `revisao/material/nfpss/CONFERIR_P3.md` (fora do Git), a conferir na fonte.
  - ⏳ **Depois:** verificador em rc 0 por bloco, o montador (`montar_revisao_material.py`, com IGR e LEG novos)
    e a camada de aprofundamento.
- ✅ **10/11/2026 — Treino de Discursiva:** artigo, súmula e conceito do "Escrever a peça" abrem o Estudo completo
  (commit `2ef6eaa`); texto justificado e negrito (§G6.6, commit `ab175e9`).

- 🆕 **09/11/2026 — Comentários aprofundados (Pente Fino e Revisão)**, pedido do titular.
  - **Campos novos:** "Onde está o erro" (o que a assertiva diz ao lado do certo), "Aprofundando", "Na prática" e
    "Para memorizar"; layout novo no Storybook.
  - ✅ **Pente Fino:** os 3.128 itens têm aprofundamento, e todos os 1.525 E têm correção.
    - Camada em `ferramentas/pente_fino/aprofundar/`; `conferir.py` OK nas 8 disciplinas.
    - Trava: `ferramentas/validar_aprofundamento.py` (porta do portão) proíbe número que o item não tenha.
  - ✅ **Revisão (15h58):** os 2.783 itens têm aprofundamento, e todos os 1.270 E têm correção.
    - Camada em `revisao/material/nfpss/aprofundar/`, fora do Git; `revisao_nfpss.js` remontado (4.285 KB).
    - Lista do que conferir: `revisao/material/nfpss/CONFERIR_aprofundamento.md`, com CPC05-098 (gabarito C
      duvidoso), TRI01-075 (ADI 7066), CON04-015/022 (EC 139/2026) e vários itens da LC 236/2026.
  - ⚠️ **Itens do Pente Fino apontados pelos redatores, a CONFERIR:**
    - **MLE-5-R2-06:** o sinal de Winslow é o recipiente com água sobre o tórax, não o espelho.
    - **MLE-4-R1-02:** "trajetória" × "trajeto", em contradição com o próprio resumo.
    - **INF-2.3-R2-02:** atalho da caneta, Ctrl + C ou Ctrl + P.
    - **PEN-9-R2-02:** rótulo da lei com formato errado.
    - **PEN-4.4-R1-03 e PEN-1.1-R1-05:** o artigo citado não sustenta o tema.
    - **PEN-4.3-R2-03:** redação confusa.
    - **CPP-8.5-R2-01:** prisão especial do diplomado; a ADPF 334 a derrubou em 2023.
    - **Já conferidos na lei seca oficial:** 3 trechos escritos de memória, todos corretos (LPE-27, LPE-31 e LPE-36).

- 🆕 **09/11/2026 — Aba 📚 Revisão (D-022):** o material de revisão anexado pelo titular (Partes 1 e 2: Processo
  Civil, Tributário, Constitucional e Ambiental; 267 páginas) virou assertivas C/E comentadas, ~2.700 em 23 blocos.
  - **Tela:** reaproveita o motor do Pente Fino, com os blocos todos abertos e o progresso em `revisao:v1`.
  - **Cobertura provada:** `ferramentas/validar_revisao_material.py` confere página a página e número de julgado a
    número de julgado.
  - **Montagem:** `ferramentas/montar_revisao_material.py` grava `discursiva/revisao_nfpss.js`.
  - **Fora do Git:** o material e as assertivas, em `revisao/material/nfpss/`.
  - ⏳ **A Parte 3 vem depois, do titular.** Ela entra pelo mesmo caminho:
    1. extrair o texto, tirando a marca d'água de CPF;
    2. dividir em blocos com `revisao/material/nfpss/limpar_nfpss.py` (adaptar as divisas de disciplina);
    3. redator por bloco, guiado pelo brief em `revisao/material/nfpss/BRIEF.md`;
    4. o verificador em rc 0;
    5. o montador.
  - ⚠️ **~75 itens com "O material diverge"** (Lei 7.374 por 7.347, Súmula 509 do STF por STJ, arts. do CPC/73, EC
    69/2012...). Vários pedem conferência na fonte oficial: LC 236/2026, Lei 15.484/2026, Tema 1385, ADI 7066 e
    ADPF 973.
  - `docs/testar_pente_fino.mjs` (27 conferências, T25 a T27 da Revisão; autoteste com 5 defeitos plantados) roda
    só aqui: depende do Chrome do Windows e não é porta do portão.

- ✅ **09/11/2026, 10h48 — Conserto da revisão (régua única de lei seca, corretor de súmulas, PDF por CDP) no Git:**
  commit `9fa62b9`. Estava pausado fora do Git desde 07/11, ~15h. Portão 26 de 26 (rc 0); m01 a m04 validados pelo
  gerador novo (rc 0). Súmulas 641 e 645 do STJ corrigidas por `ferramentas/corrigir_sumulas.py`.
  ⚠️ Ainda em aberto: `servidor.py` mostra as leis da Bahia como "Planalto" (`merged_lei`); súmula STJ-582 (m03)
  fora de `assets/sumulas.json`; **módulos 5 a 13 da revisão não gerados** (o calendário previa todos até 13/11).
- ✅ **07/11 a 08/11/2026 — Pente Fino** (D-021) em 9 disciplinas, cada uma num commit: Processo Civil, Civil e
  Empresarial, Medicina Legal, Criminologia, Processo Penal, Penal Parte Geral e Parte Especial, Legislação Penal
  Extravagante, Informática (último: `3e44a29`, 08/11, 22h04). **Sem Pente Fino** (pontos no `items.json`, medido em
  09/11/2026): Administrativo 71, Constitucional 62, Tributário 36, Raciocínio Lógico 23, Legislação Geral da Bahia
  e Igualdade (PRG) 18, Ambiental 16, Português 10, Legislação Geral 5, Atualidades 2.
  📅 **Prova objetiva e discursiva: 06/12/2026 — faltam 27 dias** (contados de 09/11).

- ✅ **07/11/2026, 16h31 — Destaques didáticos nos comentários dos simulados:** termos jurídicos centrais em negrito; exceções e limitações em vermelho. Aplicados só na renderização dos comentários, sem reescrever o material. Testes cobrem destaques, escaping e preservação do renderizador padrão.
- ✅ **07/11/2026, 16h15 — Layout das abas da aplicação Discursiva:** hierarquia visual, leitura de enunciados, orientações, modelos e comentários mais claros; etapas, cartões e progresso com maior destaque; responsividade conferida sem rolagem horizontal em viewport móvel. Fluxos, dados e respostas não mudaram. Storybook compilado e portão aprovado nas 26 portas.
- ✅ **07/11/2026, 08h01 — Módulo 1 (piloto) PRONTO, aguardando a aprovação do formato pelo titular:**
  `revisao/saida/m01_igualdade_legislacao_atualidades.html` (+ PDF, 161 páginas), 25 de 25 pontos, 119 fichas,
  51 questões, 107 trechos de lei conferidos, 24 jurisprudências com data conferida na fonte; gerador, verificador
  de atualidade e referências proibidas com saída 0. Lei seca consertada no commit `60a8e70` (63 chaves falsas;
  Lei 11.340 voltou com 57 artigos; leis da Bahia pelo Legisla Bahia; 11.124 artigos de 87 diplomas).
  ⚠️ `servidor.py` ainda mostra as leis da Bahia como "Planalto" (`merged_lei`) — corrigir.
  ⚠️ `assets/sumulas.json` tem data trocada nas súmulas 641 e 645 do STJ.
- ⏳ **07/11/2026, 06h32 — Revisão (D-018):** Fase 0 e motor do caderno **prontos e no Git** (commit `522bfad`,
  CI verde). Ordem dos módulos **por rendimento** (D-019); discursiva no mesmo dia (06/12). **Gerando o piloto,
  Módulo 1** (Igualdade racial e de gênero, Legislação Geral da Bahia e Atualidades, 25 pontos), junto com o
  conserto da lei seca (chave `CP:3-A`, Lei 11.340 que não baixou, leis estaduais da Bahia). Próximo: o titular
  aprova o formato do piloto; depois os módulos 2 a 12, até 13/11.
- ⏳ **06/11/2026, 21h09 — Revisão de todo o edital por prioridade, estilo caderno (D-018), EM CONSTRUÇÃO.** Plano em
  `docs/REVISAO_PLANO.md`. Rodando em paralelo: **Fase 0** (provas AOCP extraídas para `revisao/dados/`, pesos do
  edital, mapa de prioridade dos 503 pontos em `revisao/mapa_prioridade.json`, verificador
  `ferramentas/verificar_atualidade.py`) e o **motor do caderno** (`revisao/molde/`, `ferramentas/gerar_revisao.py`).
  Depois: módulo piloto para aprovação do titular; ondas de 2 módulos. Módulos e conteúdo fora do Git (material de
  terceiro). ⚠️ O agendamento semanal da rotina foi recusado pelo sistema de permissões: fica para o titular decidir.
  📅 **Prova objetiva: 06/12/2026** (titular, 06/11/2026, 21h09) — **30 dias** contados de 06/11. Calendário em
  `docs/REVISAO_PLANO.md` (§Prazo): todos os módulos gerados até 13/11.
- 🆕 **05/11/2026, 11h17 — Simulados do Treino de Discursiva: leitura corrigida e tesoura.** O importador marcava como
  "tabela" (letra de máquina, rolagem lateral) 239 blocos; 89 eram texto corrido, e parágrafos saíam partidos ao meio.
  Novo leitor `discursiva/blocos.js` (texto → parágrafo e item; colunas → tabela HTML; fórmula → linhas centralizadas;
  emenda o parágrafo partido), provado em `docs/testar_blocos_simulados.cjs` (0 caractere perdido em 804 listas; porta
  no portão). Questões no padrão da Trilha: letra em selo, tesoura Eliminar/Repor salva por questão, texto
  justificado, A–E e ← →, zoom A−/A+ e, no modo Estudo, escolher e depois **Confirmar**. ⚠️ Limite conhecido: linhas
  de tabela em que o próprio PDF perdeu o espaço entre colunas saem como parágrafo (ex.: Simulado 3, Q85).

- 🆕 **04/11/2026, 16h52 — Simulados objetivos comentados DPC-BA no Treino de Discursiva (D-017):** aba 📝 Simulados com 4 × 100 questões dos PDFs (modo Prova e modo Estudo, nota por bloco e disciplina, revisão dos erros). Dados de terceiro só no disco (`discursiva/simulados_delta.js`, fora do Git e do arquivo de envio); refaz-se com `python -I ferramentas/importar_simulados_delta.py`.
- 🆕 **03/11/2026, 17h — Treino de Discursiva: condução "Entender o caso" e "Estudo completo" nas 18 peças (D-015):** 5 etapas por peça (peça, competência, crime, fundamentos, pedidos) com os artigos na redação oficial do Planalto (`discursiva/artigos.js`, gerado por `ferramentas/gerar_artigos_discursiva.py`); estudo por tema com lei, doutrina, jurisprudência, Medicina Legal e Criminologia. ⚠️ Lei 11.340 sem texto oficial (Planalto fora): rodar `atualizar_lei_seca.bat L11340` e o gerador.
- 🆕 **03/11/2026, 11h — Treino de Discursiva só com o que o edital admite (D-014):** saem 12-C e 13-A (viram cartões), entram 6 representações (captação ambiental, sigilo bancário e fiscal, 13-B, alienação antecipada, perfil genético, internação provisória); 18 peças, 215 cartões.
- 🆕 **03/11/2026, 09h — Treino de Discursiva: 5 peças complementares (D-013):** despacho do flagrante + conversão, cautelares diversas (319, VI), afastamento do lar pelo delegado (12-C), ofício do art. 13-A e relatório final — `discursiva/pecas_complementares.js`; 14 peças, 188 cartões.
- 🆕 **02/11/2026, 20h46 — Treino de Discursiva ampliado (D-012):** 8 baralhos por lei conferidos no texto legal
  (inclui Lei 15.358/2026), peça de facção e caso de TCO. 9 peças, 9 casos, 161 cartões.

- 🆕 **02/11/2026, 18h26 — Treino de Discursiva** (D-011): `discursiva/Treino_Discursiva.html` — 8 peças passo a passo,
  8 estudos de caso, 74 cartões de artigos em repetição espaçada + Certo/Errado. Abre com duplo clique (sem servidor).
  Próximo: mais peças/casos por disciplina do edital e a Lei 15.358/2026 depois de conferida.

- 🆕 **01/11/2026, 21h34 — bloco de UMA disciplina** (D-010, complemento do titular): seletor "Bloco de:" no painel
  e no diálogo (todas intercaladas ou só uma). ⚠️ Disciplina pequena dá bloco menor que 30 (Processo Civil: 12 pontos).

- 🆕 **01/11/2026, 20h23 — bloco montado por disciplina e assunto, revisão rápida C/E e letra da lei**
  (D-010, servidor v10): diálogo 🎯 no painel de blocos (Objetiva · C/E rápido · Fora do bloco, por ponto ou
  por disciplina), bloco intercalado por disciplina, revisão de 12 a 20 itens C/E com título no padrão das
  alternativas e auditoria dupla, prompt exigindo o detalhe legal em todas as disciplinas. Provas:
  `testar_servidor.py` (+8 casos), `testar_blocos.mjs` (+3), `testar_espera.mjs`, `testar_pagina.cjs`,
  conferência no Chrome com API simulada. ⚠️ **Camada:** o **servidor** só usa a v10 depois de
  **reiniciado**; a tela muda ao recarregar.

- 🆕 **01/11/2026, 15h33 — índice ampliado com Constitucional, Administrativo e Ambiental** (D-009):
  11.131 páginas (eram 9.356); 0 CPF no índice. ⚠️ **Camada:** gravado no **disco**; o servidor que
  estava aberto (desde 08h54, porta 8765) carrega o índice só na partida — **reiniciar o servidor**
  para as matérias novas valerem. A Trilha é **estudo pessoal, fora do portal** (D-009).

- Git iniciado em 31/10/2026; remoto privado (D-001). Governança do roteiro de fundação adotada
  (harness, hooks, portão, CI) — CI verde no commit `4794a16`.
- Storybook 10.6.5 instalado; stories em `stories/`. Node 26.13.0 instalado na máquina.
- Revisão completa do código feita em 31/10/2026: 25 itens. Os de severidade alta estão abaixo.
- ✅ **31/10/2026, 17h31 — corrigidos no `index.html`, com assertiva no portão
  (`docs/verificar_regressoes.py`, que acusa os dois no código antigo):**
  - **R-01** "Refazer" apagava a resposta sem rastro: agora a tentativa vai para `state.attempts`
    (salvo no navegador e no backup JSON) e o rótulo diz "a tentativa fica no histórico";
  - **R-02** atalhos A–E ignoram Ctrl/Cmd/Alt e só valem na aba Estudar.
  - **R-03** (D-004, 17h37) o caderno de erros mostra as tentativas refeitas, marcadas com a data;
    a taxa de acerto não muda. O **dashboard** continua lendo só a resposta atual.
  - ⚠️ **Camada:** corrigido no **arquivo**; o titular vê a mudança ao **recarregar** a página do app
    (o `servidor.py` serve o `index.html` do disco).
- ✅ **31/10/2026, 17h37 — contraste e foco aplicados** (D-003): bloco
  `<style id="d003-contraste-foco">` no `index.html`; story em `Aprovados/Contraste e foco (D-003)`.

- ✅ **31/10/2026, 17h42 — espera pela geração corrigida** (R-04): a tela espera enquanto o
  servidor disser `generating` (teto de 25 min), encerra na hora em `missing`, mostra "Gerando há
  X min Y s" (anunciado ao leitor de tela) e mantém um laço por vez. Provado por comportamento:
  `docs/testar_espera.mjs` roda a função **real** contra servidor simulado — 3 de 3 no código novo,
  0 de 3 no antigo.

## Próximas tarefas, em ordem

1. Servidor: `X-Frame-Options`/CSP `frame-ancestors`, `do_HEAD` bloqueado, validar `Content-Length`.
2. Stories: alternativa com estado acessível, modal com foco, menu lateral no celular.
3. README: `.env.exemplo` inexistente; seção "Arquivos" desatualizada.
4. **Blocos de 30 questões** — viável (`docs/VIABILIDADE_BLOCOS_30.md`, 31/10/2026). Decisões do
   titular às 19h42: baixa por correlação **automática** (D-005), histórico **no app e em HTML/PDF**
   (D-006), **auditoria dupla mantida** (D-007).
   - ✅ **31/10/2026, 19h58 — implementado** (servidor v8 + script v8 no `index.html`): painel
     "📦 Bloco N" (x de 30, prontos no servidor, ir ao próximo, gerar próximo bloco), pré-preparo do
     bloco seguinte aos 20 feitos, baixa por correlação validada contra o `items.json` (anel na
     árvore), progresso do edital = respondidos + correlação, histórico único regravado a cada bloco
     em `historico/Trilha_historico_acumulado.html` (fora do Git) + baixar HTML + imprimir em PDF, e
     **métricas por questão** (duração, chamadas, tokens) gravadas no cache.
     Provas: `testar_servidor.py` (11+1 casos, API simulada), `testar_blocos.mjs` (13 casos, script
     real), `testar_pagina.cjs` (página real carrega sem erro). ⚠️ `testar_servidor.py` passou em 29
     de 30 execuções locais: 1 falha intermitente não reproduzida.
   - ✅ **Prova real (31/10/2026, 20h10):** 1º bloco gerado com a API — 49,9 s por questão em média,
     2 chamadas (geração + auditoria, nenhuma reprovada), 18.127 tokens de entrada e 3.830 de saída
     por questão (12 primeiras medidas); bloco de 30 ≈ 12 a 13 min com 2 geradores.
   - ✅ **31/10/2026, 21h40 — Certo/Errado (D-008, servidor v9):** a aula, as pegadinhas e o mapa
     mental viram 8 a 15 itens C/E comentados (doutrina, lei seca, jurisprudência), com comentário
     oculto até julgar; lei seca e jurisprudência recolhidas; questão sem grifo azul. Rota
     `/api/converter_ce` converte as já geradas (questão intacta; aula guardada em `aula_original`).
     ⏳ **Falta:** o titular reiniciar o servidor e a conversão das 33 questões do cache rodar.
   - ✅ **31/10/2026, 19h38 — acervo grande indexado** (`ferramentas/ampliar_acervo.py`): índice de
     744 → **9.356 páginas** (+8.612, inclusive os 42 resumos dos ZIPs PCPR; PCPR-3 e 4 eram cópia).
     ⚠️ Camada: o **arquivo** do índice mudou; o servidor só usa o índice novo ao ser **reiniciado**.
   - ⏳ Falta: indexar as **provas AOCP de Direito e de Português** (Downloads, AOCP 01–06 e
     PORTUGUÊS 01–08 + Delegado) — hoje só as de Informática e Raciocínio Lógico estão no índice.

- ✅ **15/11/2026 — link extra "Revisão Dirigida — Delegado PC-BA"** (`discursiva/Revisao_Delegado_BA.html`
  + `discursiva/revisao_delegado_ba_dados.js`): assertivas Certo/Errado comentadas (comentário em mini-aula),
  estilo AOCP (letra de lei), foco em legislação LOCAL da Bahia (Constituição estadual, Lei 11.370/2009 — Lei
  Orgânica da PC-BA, Lei 6.677/1994 — Estatuto dos servidores), poderes do delegado e atualizações. Sem Português
  nem Informática. **Bloco 1 (prioridade máxima) com 50** assertivas (18 baianas, 16 "Errado"). Conteúdo autoral,
  fundado na letra de lei — vai no Git. Teste `docs/testar_revisao_ba.cjs` no portão (37 portas). CI verde.
  ✅ **Bloco 2 (mais 50) concluído em 15/11/2026** — total 100 assertivas (2 blocos).
  ✅ **16/11/2026 — Revisão Dirigida com 6 blocos / 350 assertivas:** Blocos 3-5 (mais 2×50 + 1×100 de
    Ambiental/Tributário/Medicina Legal/Criminologia/Civil/CPC) e **Bloco 6 — Reforma Tributária (EC 132/2023)**
    com 50 C/E (IBS, CBS, Imposto Seletivo, Comitê Gestor, cashback, cesta básica, ITCMD progressivo/exterior,
    calendário de transição). UX: Enter avança, ao marcar C/E a tela rola para a correção, ao reabrir o bloco
    **retoma na 1ª não respondida**. Grifo (G) ganhou botão **Negrito+Sublinhado**. Commit 6967f5d, CI verde.
  - ✅ **16/11/2026 — nova aba "⚖️ Letra de Lei"** (`discursiva/Lei_Seca_Delegado_BA.html` +
    `discursiva/lei_seca_delegado_ba_dados.js`): treino de memorização por **lacunas (cloze)** dos artigos mais
    batidos para delegado — 6 blocos, 82 cartas (Penal, Proc. Penal, Legislação Especial no centro; + Const./
    Tributário/Ambiental/Civil/CPC do edital), com ênfase nos **novos/atualizados** (Pacote Anticrime, feminicídio
    autônomo, Henry Borel, Abuso de Autoridade, EC 132). Revela a palavra‑chave, autoavalia e salva o progresso.
    Aba ligada no hub (Treino). Teste `docs/testar_lei_seca_ba.cjs` no portão (agora 39 portas).
  - 🆕 **Também em 14-15/11: abas "900 Discursivas" (penal/PP) e "PED — FGV"** no Treino (material de terceiro,
    só na cópia privada, fora do Git). Ver `docs/PROCEDENCIA.md`.

- ✅ **21/11/2026 — nova aba "📰 Atualidades"** (`discursiva/Atualidades_CE.html` +
  `discursiva/atualidades_dados.js`): **115 assertivas Certo/Errado comentadas** cobrindo todo o anexo de
  atualidades da prova (segurança pública, eleições 2026, gênero/DH, clima/COP30, saúde, economia, internacional,
  educação/cultura, tecnologia e Comunicação). Modos **Treino** (responde C/E → gabarito + comentário) e **Estudo**
  (tudo revelado), filtro por tema, placar, **Modo celular**, termos-chave em **negrito vermelho** e tabelas (Nobel,
  palavras do ano). A seleção de temas vem do anexo pessoal do titular; **as questões e os comentários são autorais,
  de fontes públicas** (ver `docs/PROCEDENCIA.md`). Aba ligada no hub, na paleta de grifos e no pacote privado.
  Teste `docs/testar_atualidades.cjs` + 2 portas no portão (**45 portas**). Prova em 06/12/2026.
  - ✅ **21/11/2026 — Revisão Guiada no módulo *Discursivas Stories*:** novo modo **📖 Revisão** (padrão) que mostra
    a resposta-modelo pronta para leitura, **sem o aluno escrever** (etapa de revisão), com os **pontos principais
    em negrito+sublinhado** (referências legais e ênfases `*...*`) e os **conectivos em vermelho** (realce
    automático), mais um roteiro de estrutura (tese → fundamento → aplicação → conclusão). O modo **🎯 Treino**
    antigo (revelar ponto a ponto) continua, alternável no cabeçalho e no palco. Teste
    `docs/testar_discursivas_stories.cjs` atualizado (cobre os dois modos). Portão 45 portas, CI a confirmar.

## O que fica rodando

- Storybook (`npm run storybook`), porta 6006, iniciado pela sessão de 31/10/2026.
