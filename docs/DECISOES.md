# DECISÕES — Trilha AOCP Delegado Bahia

> Registro de decisões do titular. Cada uma traz data, autor e o que trava enquanto estiver aberta.
> Decisão caduca quando a medição em que se apoiou muda (HARNESS §F49).

## Em aberto

Nenhuma em 31/10/2026, 17h36.

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

### D-003 — Contraste e foco aprovados (31/10/2026, titular)

Aberta às 15h47 de 31/10/2026; aprovada às 17h34, resposta textual do titular à pergunta *"Proposta
de contraste e foco (D-003): aprova como está no Storybook?"*: *"2- sim"*. Aplicada no
`index.html` (bloco `<style id="d003-contraste-foco">`) sem mudar uma cor da proposta; a story foi
para `Aprovados/Contraste e foco (D-003)`. Contrastes medidos pela fórmula WCAG 2.1: todos os pares
acusados na revisão passam de 4,5:1 (texto) e o anel de foco de 2,35 para 5,43:1. 🔑 **Caduca**
(§F49) se a paleta mudar: a medição é desta paleta.

### D-004 — O caderno de erros mostra as tentativas refeitas (31/10/2026, titular)

Resposta textual do titular, em 31/10/2026, 17h34, à pergunta *"Caderno de erros: quer que ele
passe a mostrar as tentativas refeitas?"*: *"1- sim"*. Os erros guardados em `state.attempts` pelo
botão Refazer entram no caderno, marcados *"Tentativa refeita em dd/mm/aaaa"*. **A taxa de acerto
não muda:** o placar continua sendo a resposta atual de cada item.

### D-005 — Blocos de 30: baixa por correlação AUTOMÁTICA (31/10/2026, titular)

Resposta textual do titular, 31/10/2026, 19h42, às 3 perguntas de `docs/VIABILIDADE_BLOCOS_30.md`:
*"1-AUTOMATICA    20 NO APP, HTML /PDF  3 AUDITORIA DUPLA"*. Item 1: quando o comentário de uma
questão cobre outro ponto do edital, esse ponto recebe baixa **sem confirmação**. Salvaguarda da
sessão (não do titular): só entram ids que existem no `items.json`, e a baixa por correlação fica
**visualmente distinta** de "respondido" — rótulo vira prova (§E5).

### D-006 — Histórico acumulado no app e em HTML/PDF (31/10/2026, titular)

Mesma resposta, item 2, lido como *"2 — no app, HTML/PDF"* (o titular escreveu "20"; leitura
declarada no chat, a corrigir se não for isso). O histórico fica no app e é exportado num único
arquivo HTML, **regravado a cada bloco com tudo**; o PDF sai da impressão desse HTML.

### D-007 — Auditoria dupla mantida nos blocos (31/10/2026, titular)

Mesma resposta, item 3: *"3 AUDITORIA DUPLA"*. `DEEP_AUDIT` segue ligado: mais lento e mais caro
por questão, menos erro. O custo real de um bloco é medido no primeiro (tempo, chamadas, tokens).

### D-008 — A aula vira Certo/Errado comentado; sem grifo azul na questão (31/10/2026, titular)

Textual, 31/10/2026, 21h28: *"os comentários ficam muito grandes e para manter o foco e estudo ativo
pensei o seguinte... permanece o comentario de cada alternativa... na elaboração da questão não
precisa botar nenhum termo griafdoo de azul... quero que depois de analisar cada alternativa
transforme a aula... os comentários... em questões certo e erradas comentadas... faz tanto da parte
doutrinária... da lei seca e da jurisprudência... ai veja que criei 30 questões... já ajusta essas
também e na proxima rodada continua com essa pegada... lembrando que a questão aocp permanece igual
o que vai mudar são os comentários"*.

- A questão AOCP (enunciado, alternativas, gabarito) **não muda**; o comentário de cada alternativa
  **permanece**.
- A aula, as pegadinhas e o mapa mental viram **8 a 15 itens Certo/Errado** (doutrina, lei seca,
  jurisprudência), com o comentário oculto até o aluno julgar.
- Leitura da sessão, a corrigir se não for isso: a letra da lei e os cartões de jurisprudência
  **ficam**, mas **recolhidos** ("📚 Consultar a letra da lei e a jurisprudência") — o pedido de
  29/10 era "ver a letra da lei da questão".
- As questões já geradas são **convertidas** (1 chamada ao modelo por questão, sobre o comentário
  existente); a aula antiga fica guardada no arquivo em `aula_original` (§F17).

### D-009 — Trilha é estudo pessoal, local; materiais novos entram no índice (01/11/2026, titular)

Ordem do titular, 01/11/2026, textual: *"ISSO SÓ PARA MINHA MAQUINA NÃO IRÃO PARA PORTAL DO PROFESSOR...
ESSA TRILHA AOCP É PARA UM ESTUDO QUE ESTOU FAZENDO PARA UMA PROVA. O PORTAL DO PROFESSOR SERÁ OUTRA
COISA... PODE ATÉ COLOCAR TODO ESSE CONTEÚDO DENTRO DA PASTA DELEGADO BA E COLOCAR ESSA PASTA DENTRO DO
REPOSITÓRIO"*.

- A Trilha **não** é funcionalidade do portal. ⚠️ Divergência registrada, não apagada: o `CLAUDE.md` da
  pasta mãe (31/10/2026) diz que todo app da máquina vai para o portal; para a Trilha vence esta ordem,
  mais nova e específica.
- A pasta `DELEGADO BA` foi **copiada** de `OneDrive/Área de Trabalho/` para `Repositório/DELEGADO BA`
  (34 de 34 arquivos com SHA-256 igual). A original **ficou no OneDrive** — mover apagaria a cópia da
  nuvem; apagar de lá é decisão do titular. As pastas `DIREITO CONSTITUCIONAL` (30 PDFs),
  `DIREITO ADMINISTRATIVO` (19) e `DIREITO AMBIENTAL` (7) foram movidas para dentro dela.
- O `ferramentas/ampliar_acervo.py` passou a ler essa pasta e as três subpastas (ver PROCEDÊNCIA).

### D-010 — Montar o bloco por disciplina e assunto; revisão rápida C/E; letra da lei (01/11/2026, titular)

Ordem do titular, 01/11/2026, textual: *"queria que ao gerar ali 30 questões eu tivesse um local para
escolher a disciplina, o assunto e se aquele assunto eu quero revisar no formato certo e errado com os
comentários no mesmo padrão das objetivas ..pq tem temas que eu ja estudei bastante e quero passar mais
rápido... outros não eu preciso estudar mais... A ideia é passar por todos os pontos do edital e deixar o
conhecimento horizontalizado. Na verdade em todas as disciplinas a AOCP gosta muito de detalhes das
legislalção aplicada. Prazos... qualificadoras, aumento de pena..."*

- Painel de blocos ganha **🎯 Escolher disciplinas e assuntos**: cada ponto do edital fica em
  **Objetiva** (padrão), **C/E rápido** ou **Fora do bloco**; dá para mudar a disciplina inteira de uma vez.
  As escolhas ficam em `state.modos` (navegador e backup JSON).
- O bloco **intercala as disciplinas** por padrão (um ponto de cada por vez: estudo horizontal); a caixa
  "Intercalar" volta à ordem sequencial da trilha.
- **Revisão C/E** (servidor v10): 12 a 20 itens Certo/Errado do ponto, ao menos metade de lei seca quando
  há lei, item errado troca UM detalhe (prazo, fração, pena, qualificadora, majorante, competência…);
  cada item tem **título curto no padrão das alternativas** + comentário + fundamento; mesma base local
  (lei preenchida pelo servidor) e **mesma auditoria dupla** (D-007). Placar: acerto com **70%** ou mais
  (leitura da sessão, a ajustar se o titular quiser outro corte).
- O prompt da banca passou a exigir o **detalhe da letra da lei em todas as disciplinas** (prazos,
  quóruns, penas, qualificadoras, majorantes e minorantes com frações exatas, exceções, "poderá" × "deverá").
- ⚠️ Limite: a escolha vale para pontos **ainda não gerados**. O que já está pronto no cache (ou no banco
  inicial) não é gerado de novo — regerar gasta API e é decisão do titular, ponto a ponto.
- **Complemento, 01/11/2026, 21h34** — titular, textual: *"FALTOU COLOCAR A OPÇÃO DE EU ESCOLHER SE QUERO QUE ELABORE DE UMA SO
  DISCIPLINA... SE EU QUISER FAZER LOGO UM BLOCO SOMENTE DE PROCESSO CIVIL AI FAZ"*. Seletor "Bloco de:" (painel e diálogo),
  em `state.blocoDisc`. O bloco leva os pendentes da disciplina, até 30 — uma questão por ponto e rodada, como sempre.
