# FAROL — Trilha AOCP Delegado Bahia

> Estado, tarefas e o que ficou rodando. Atualizado a cada ~15 min de trabalho e no fechamento.

**Última atualização:** 05/11/2026, 11h17.

## Estado

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

## O que fica rodando

- Storybook (`npm run storybook`), porta 6006, iniciado pela sessão de 31/10/2026.
