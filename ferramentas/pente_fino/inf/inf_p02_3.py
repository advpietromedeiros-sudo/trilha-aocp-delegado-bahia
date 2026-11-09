# Pente Fino de Informática — INF-2.3 e INF-2.3.1 a INF-2.3.6 (PowerPoint) (08/11/2026).
# Redação própria. Versão de referência: PowerPoint do Microsoft 365 em português; LibreOffice Impress quando citado.
from base import I
from inf_fontes import FPP

# ======================= INF-2.3 · PowerPoint =======================
P = 'DBA26-INF-2.3'
I(P, 1, 'Iniciar a apresentação',
  'No PowerPoint, F5 inicia a apresentação a partir do primeiro slide, e Shift + F5 a partir do slide atual.', 'C',
  '**F5** = do **começo**; **Shift + F5** = do **slide atual**; **Esc** encerra; **Alt + F5** abre o **Modo de Exibição do Apresentador**.' + FPP,
  kw=['F5', 'Shift + F5'])
I(P, 1, 'Formato .ppsx',
  'O arquivo salvo como Apresentação de Slides do PowerPoint (.ppsx) abre, por duplo clique, diretamente em modo de apresentação.', 'C',
  '**.ppsx** abre já **exibindo** os slides; **.pptx** abre para edição; **.potx** é **modelo**. No Impress, o formato padrão é **.odp**.',
  kw=['.ppsx', '.pptx'])
I(P, 1, 'Transição × animação',
  'Transição é o efeito aplicado a cada objeto dentro do slide, e animação é o efeito de passagem de um slide para o outro.', 'E',
  'Está trocado: **transição** = efeito na **passagem entre slides** (guia **Transições**); **animação** = efeito nos **objetos** do slide (guia **Animações**).',
  peg='Inverter transição e animação.',
  kw=['transição', 'animação'])
I(P, 1, 'Tela preta',
  'Durante a apresentação, a tecla B (ou ponto) exibe uma tela preta, e a tecla W (ou vírgula) exibe uma tela branca.', 'C',
  '**B** ou **.** = slide **preto**; **W** ou **,** = slide **branco**; outra tecla volta à apresentação.' + FPP,
  kw=['B', 'W', 'tela preta'])
I(P, 1, 'Ir para um slide',
  'Durante a apresentação, não há como ir diretamente a um slide específico pelo teclado; é preciso avançar um a um.', 'E',
  'Digitar o **número do slide + Enter** salta direto para ele; Home/End vão ao primeiro/último.' + FPP,
  peg='Negar o salto direto por número.',
  kw=['número + Enter', 'slide específico'])
I(P, 1, 'Anotações',
  'As anotações do orador, digitadas no painel abaixo do slide, aparecem para o público durante a apresentação.', 'E',
  'As **anotações** ficam para o **orador**: aparecem no **Modo de Exibição do Apresentador** (no monitor dele) e no modo **Anotações**, não na tela do público.',
  peg='Achar que o público vê as anotações.',
  kw=['anotações', 'Modo de Exibição do Apresentador'])

# --- INF-2.3 · Rodada 2
I(P, 2, 'Avançar e voltar',
  'Durante a apresentação, N, Enter, Page Down, seta para a direita e a barra de espaços avançam para a próxima animação ou para o próximo slide.', 'C',
  'Avançam: **N, Enter, Page Down, seta direita/baixo, espaço**. Voltam: **P, Page Up, seta esquerda/cima, Backspace**.' + FPP,
  kw=['avançar', 'Page Down'])
I(P, 2, 'Caneta',
  'Durante a apresentação, é possível desenhar sobre o slide com a caneta e, ao final, escolher entre manter ou descartar as anotações à tinta.', 'C',
  'A **caneta** (Ctrl + C, na lista oficial) e o **marca-texto** permitem anotar na apresentação; ao sair, o PowerPoint pergunta se **mantém** as anotações à tinta.' + FPP,
  kw=['caneta', 'anotações à tinta'])
I(P, 2, 'Ocultar slide',
  'O slide oculto é excluído da apresentação e do arquivo, não podendo mais ser recuperado.', 'E',
  '**Ocultar Slide** (guia Apresentação de Slides) só o **pula** na exibição; ele continua no arquivo, aparece esmaecido na lista e pode ser reexibido.',
  peg='Igualar ocultar a excluir.',
  kw=['Ocultar Slide', 'pula'])
I(P, 2, 'Ensaiar intervalos',
  'O recurso Testar Intervalos registra o tempo gasto em cada slide durante um ensaio, para que a apresentação avance sozinha depois.', 'C',
  '**Testar Intervalos** (Apresentação de Slides) grava o tempo de cada slide; com eles, a apresentação pode correr **automaticamente** (ex.: em quiosque).',
  kw=['Testar Intervalos', 'automaticamente'])

# ======================= INF-2.3.1 · Barras de ferramentas, botões e menus =======================
P = 'DBA26-INF-2.3.1'
I(P, 1, 'Guias do PowerPoint',
  'A faixa de opções do PowerPoint traz guias próprias, como Design, Transições, Animações e Apresentação de Slides, além de Página Inicial, Inserir, Revisão e Exibir.', 'C',
  'São as guias típicas do **PowerPoint**: **Design** (temas, tamanho do slide, plano de fundo), **Transições**, **Animações**, **Apresentação de Slides** (iniciar, configurar, ensaiar), além das comuns ao Office.',
  kw=['Transições', 'Animações', 'Apresentação de Slides'])
I(P, 1, 'Tamanho do slide',
  'O tamanho do slide (16:9 ou 4:3) é definido na guia Exibir, grupo Zoom.', 'E',
  '**Tamanho do Slide** fica na guia **Design** (grupo Personalizar), com **Widescreen (16:9)**, o padrão atual, **Padrão (4:3)** e tamanho personalizado.',
  peg='Pôr o tamanho do slide na guia Exibir.',
  kw=['Tamanho do Slide', 'Design'])
I(P, 1, 'Novo Slide',
  'O botão Novo Slide fica na guia Página Inicial (e também na guia Inserir) e permite escolher o layout do slide a inserir.', 'C',
  'A seta do **Novo Slide** abre a galeria de **layouts**; nela também estão Duplicar Slides selecionados e Reutilizar Slides.',
  kw=['Novo Slide', 'layout'])
I(P, 1, 'Configurar apresentação',
  'A guia Apresentação de Slides não permite configurar a apresentação para repetir continuamente até o Esc.', 'E',
  'Em **Configurar Apresentação de Slides** há tipo de apresentação (apresentador, indivíduo, quiosque), **Repetir até Esc**, slides a exibir e uso dos intervalos.',
  peg='Negar a repetição contínua.',
  kw=['Configurar Apresentação de Slides', 'Repetir até Esc'])
I(P, 1, 'Guias contextuais',
  'Ao selecionar uma imagem no slide, aparece uma guia contextual (Formato da Imagem) com comandos próprios para aquele objeto.', 'C',
  'As **guias contextuais** surgem com a seleção: **Formato da Imagem**, **Formato da Forma**, **Design da Tabela**, Design do Gráfico; somem quando o objeto deixa de estar selecionado.',
  kw=['guias contextuais', 'Formato da Imagem'])

# --- INF-2.3.1 · Rodada 2
I(P, 2, 'Pincel de Animação',
  'O Pincel de Animação copia a animação de um objeto e a aplica a outro.', 'C',
  'O **Pincel de Animação** (guia Animações) faz com animações o que o Pincel de Formatação faz com formatos.',
  kw=['Pincel de Animação', 'animação'])
I(P, 2, 'Aplicar a Todos',
  'Na guia Transições, o botão Aplicar a Todos replica a transição escolhida em todos os slides da apresentação.', 'C',
  '**Aplicar a Todos** estende a **transição** (com duração e som) aos demais slides; o avanço pode ser **ao clicar** ou **após** um tempo.',
  kw=['Aplicar a Todos', 'transição'])
I(P, 2, 'Revisão no PowerPoint',
  'O PowerPoint não tem guia Revisão nem verificação de ortografia, recursos exclusivos do Word.', 'E',
  'O PowerPoint tem guia **Revisão**, com **ortografia** (F7), comentários, comparar apresentações e idioma.',
  peg='Negar ortografia no PowerPoint.',
  kw=['Revisão', 'ortografia'])

# ======================= INF-2.3.2 · Criação, inserção de slides, elementos da tela e modos de exibição =======================
P = 'DBA26-INF-2.3.2'
I(P, 1, 'Modos de exibição',
  'Os modos de exibição do PowerPoint incluem Normal, Estrutura de Tópicos, Classificação de Slides, Anotações e Modo de Exibição de Leitura.', 'C',
  'Guia **Exibir**: **Normal** (edição), **Estrutura de Tópicos** (só textos), **Classificação de Slides** (miniaturas, bom para reordenar), **Anotações** e **Modo de Exibição de Leitura**; e os **modos mestres**.',
  kw=['Classificação de Slides', 'Estrutura de Tópicos'])
I(P, 1, 'Classificação de Slides',
  'O modo Classificação de Slides é o indicado para editar o texto de cada caixa de texto, por mostrar o slide em tamanho máximo.', 'E',
  'A **Classificação de Slides** mostra **miniaturas** de todos os slides, para **reordenar**, copiar, ocultar e aplicar transições; o texto se edita no modo **Normal**.',
  peg='Atribuir à Classificação de Slides a edição do texto.',
  kw=['Classificação de Slides', 'miniaturas'])
I(P, 1, 'Começar de modelo',
  'Ao criar uma apresentação a partir de um modelo, o arquivo novo já vem com layouts, cores, fontes e, às vezes, conteúdo de exemplo.', 'C',
  'Em **Arquivo > Novo**, os **modelos** e **temas** trazem o design pronto; a apresentação em branco começa com o slide de **Título**.',
  kw=['modelo', 'Arquivo > Novo'])
I(P, 1, 'Painel de miniaturas',
  'No modo Normal, o painel de miniaturas à esquerda não permite reordenar slides; isso só pode ser feito pela guia Inserir.', 'E',
  'No **painel de miniaturas** do modo Normal, basta **arrastar** o slide para nova posição; ali também se duplica, oculta e exclui (Delete).',
  peg='Negar a reordenação pelas miniaturas.',
  kw=['painel de miniaturas', 'arrastar'])
I(P, 1, 'Duplicar slide',
  'O comando Duplicar Slide cria uma cópia do slide selecionado logo após ele.', 'C',
  '**Duplicar Slide** (botão direito na miniatura ou seta do Novo Slide) insere a cópia em seguida, com conteúdo e formatação.',
  kw=['Duplicar Slide', 'cópia'])

# --- INF-2.3.2 · Rodada 2
I(P, 2, 'Modo do Apresentador',
  'O Modo de Exibição do Apresentador mostra ao orador o slide atual, o próximo, as anotações e um cronômetro, enquanto o público vê apenas o slide.', 'C',
  'No **Modo de Exibição do Apresentador** (Alt + F5, ou automático com dois monitores) o orador vê **slide atual, próximo, anotações e tempo**.' + FPP,
  kw=['Modo de Exibição do Apresentador', 'anotações'])
I(P, 2, 'Seções',
  'O PowerPoint não permite agrupar slides em seções nomeadas.', 'E',
  'Há **seções** (Página Inicial > Seção > Adicionar Seção): agrupam slides com nome, para recolher, mover e organizar apresentações longas.',
  peg='Negar as seções.',
  kw=['seções', 'Adicionar Seção'])
I(P, 2, 'Reutilizar slides',
  'O recurso Reutilizar Slides permite trazer slides de outra apresentação para a atual, mantendo ou não a formatação de origem.', 'C',
  '**Reutilizar Slides** (seta do Novo Slide) abre outra apresentação e insere os slides escolhidos; "Manter formatação original" decide se ficam com o tema de origem.',
  kw=['Reutilizar Slides', 'formatação original'])

# ======================= INF-2.3.3 · Objetos de texto: formatar, mover, copiar e excluir =======================
P = 'DBA26-INF-2.3.3'
I(P, 1, 'Caixa de texto',
  'No PowerPoint, o texto só pode ser digitado dentro de espaços reservados ou de caixas de texto (ou formas); não se digita texto solto no slide.', 'C',
  'O texto vive em **espaços reservados** (do layout), **caixas de texto** (Inserir > Caixa de Texto) ou **formas**. Diferente do Word, não há "página" para digitar livremente.',
  kw=['caixa de texto', 'espaços reservados'])
I(P, 1, 'Duplicar arrastando',
  'Arrastar um objeto mantendo Ctrl pressionada move o objeto sem criar cópia.', 'E',
  'Arrastar com **Ctrl** cria **cópia** do objeto; arrastar com **Shift** restringe o movimento à horizontal ou vertical (e, ao redimensionar, mantém a proporção).',
  peg='Inverter o papel da tecla Ctrl.',
  kw=['Ctrl', 'cópia'])
I(P, 1, 'Excluir objeto',
  'Para excluir uma caixa de texto inteira, seleciona-se a borda da caixa (e não o texto dentro dela) e pressiona-se Delete.', 'C',
  'Com o cursor **dentro** da caixa, Delete apaga caracteres; com a **borda** selecionada (linha contínua), Delete apaga o **objeto**.',
  kw=['borda', 'Delete'])
I(P, 1, 'Ordem dos objetos',
  'Objetos sobrepostos não podem ter sua ordem alterada: o objeto inserido por último fica sempre à frente.', 'E',
  'Os comandos **Trazer para a Frente** e **Enviar para Trás** (e Avançar/Recuar) mudam a **ordem** de empilhamento; o **Painel de Seleção** lista e reordena os objetos.',
  peg='Negar a reordenação de camadas.',
  kw=['Trazer para a Frente', 'Enviar para Trás'])
I(P, 1, 'Agrupar',
  'Agrupar objetos no PowerPoint os funde de modo definitivo numa única imagem, sem possibilidade de separá-los depois.', 'E',
  '**Agrupar** (Formato da Forma > Organizar > Agrupar) faz os objetos se moverem e redimensionarem **como um só**, mas **Desagrupar** os separa de novo, cada um com sua formatação.',
  peg='Achar que agrupar é irreversível.',
  kw=['Agrupar', 'Desagrupar'])

# --- INF-2.3.3 · Rodada 2
I(P, 2, 'Ajuste automático do texto',
  'Quando o texto excede o espaço reservado, o PowerPoint pode reduzir automaticamente o tamanho da fonte para caber, por meio das Opções de AutoAjuste.', 'C',
  'As **Opções de AutoAjuste** (ícone ao lado da caixa) permitem **ajustar o texto ao espaço reservado**, parar o ajuste, dividir em dois slides ou passar a duas colunas.',
  kw=['AutoAjuste', 'espaço reservado'])
I(P, 2, 'Alinhar objetos',
  'O PowerPoint não oferece comando para alinhar ou distribuir objetos uniformemente; isso só se faz a olho, arrastando.', 'E',
  'Em **Organizar > Alinhar** há alinhar à esquerda, centro, direita, topo, meio, base e **Distribuir Horizontal/Verticalmente**; as **guias inteligentes** também ajudam no arraste.',
  peg='Negar o comando Alinhar.',
  kw=['Alinhar', 'Distribuir'])
I(P, 2, 'WordArt',
  'WordArt é um estilo de texto decorativo, com preenchimento, contorno e efeitos, inserido pela guia Inserir.', 'C',
  '**WordArt** (Inserir > WordArt) e os **Estilos de WordArt** da guia contextual aplicam preenchimento, contorno e efeitos (sombra, brilho, 3D) ao texto.',
  kw=['WordArt', 'Inserir'])

# ======================= INF-2.3.4 · Listas e objetos de desenho =======================
P = 'DBA26-INF-2.3.4'
I(P, 1, 'Níveis da lista',
  'No PowerPoint, Tab no início de um item da lista rebaixa-o um nível, e Shift + Tab o promove.', 'C',
  'Como no Word: **Tab** **rebaixa** (subtópico), **Shift + Tab** **promove**. Cada nível tem marcador e tamanho próprios, definidos pelo slide mestre.',
  kw=['Tab', 'Shift + Tab'])
I(P, 1, 'Marcador personalizado',
  'Os marcadores de lista do PowerPoint só podem ser círculos pretos, sem opção de imagem ou símbolo.', 'E',
  'Em **Marcadores e Numeração** escolhe-se **símbolo**, **imagem**, cor e tamanho em relação ao texto; a numeração pode começar em qualquer número.',
  peg='Limitar os marcadores ao círculo preto.',
  kw=['Marcadores e Numeração', 'imagem'])
I(P, 1, 'Formas',
  'O PowerPoint oferece formas prontas (retângulos, setas, fluxogramas, textos explicativos), inseridas em Inserir > Formas, que podem receber texto.', 'C',
  '**Inserir > Formas**: linhas, retângulos, setas, fluxograma, estrelas, textos explicativos; clicando na forma e digitando, ela recebe **texto**.',
  kw=['Formas', 'Inserir'])
I(P, 1, 'Converter em SmartArt',
  'O texto de uma lista com marcadores não pode ser transformado em diagrama; é preciso redigitá-lo num SmartArt.', 'E',
  'O comando **Converter em SmartArt** (Página Inicial > Parágrafo) transforma a lista em **diagrama**, mantendo a hierarquia dos níveis.',
  peg='Negar a conversão de lista em SmartArt.',
  kw=['Converter em SmartArt', 'diagrama'])
I(P, 1, 'Forma perfeita',
  'Ao desenhar um retângulo com Shift pressionada, obtém-se um quadrado; com uma elipse, um círculo.', 'C',
  '**Shift** mantém a **proporção**: retângulo vira **quadrado**, elipse vira **círculo** e linhas ficam em ângulos de 15°.',
  kw=['Shift', 'proporção'])

# --- INF-2.3.4 · Rodada 2
I(P, 2, 'Mesclar Formas',
  'O recurso Mesclar Formas combina formas selecionadas por união, interseção, subtração, fragmentação ou combinação, criando formas personalizadas.', 'C',
  '**Mesclar Formas** (Formato da Forma > Inserir Formas): **Unir, Combinar, Fragmentar, Interseção, Subtrair**.',
  kw=['Mesclar Formas', 'Unir'])
I(P, 2, 'Editar Pontos',
  'Depois de desenhada, uma forma do PowerPoint não pode ter seu contorno alterado ponto a ponto.', 'E',
  '**Editar Forma > Editar Pontos** permite arrastar vértices e curvas do contorno; também se pode **Alterar Forma** por outra.',
  peg='Negar Editar Pontos.',
  kw=['Editar Pontos', 'Alterar Forma'])
I(P, 2, 'Lista numerada em algarismos romanos',
  'A numeração de lista do PowerPoint pode usar algarismos arábicos, romanos ou letras, e começar em valor diferente de 1.', 'C',
  'Em **Numeração** há 1. 2. 3., I. II. III., a) b) c) e outros, com o campo **Iniciar em**.',
  kw=['Numeração', 'Iniciar em'])

# ======================= INF-2.3.5 · Tabelas, gráficos, planilhas, organogramas; layout, cores, slide mestre, animação =======================
P = 'DBA26-INF-2.3.5'
I(P, 1, 'Slide mestre',
  'Alterar a fonte do título no Slide Mestre muda a fonte dos títulos de todos os slides que usam esse mestre e seus layouts.', 'C',
  'O **Slide Mestre** (Exibir > Slide Mestre) guarda fontes, cores, posição dos espaços reservados, plano de fundo e logotipo; mudar nele reflete em **todos** os slides vinculados.',
  kw=['Slide Mestre', 'todos os slides'])
I(P, 1, 'Organograma',
  'O organograma é inserido no PowerPoint pela galeria de Formas, grupo Fluxograma, não havendo recurso específico para hierarquias.', 'E',
  'O **organograma** se faz com **SmartArt**, categoria **Hierarquia** (Inserir > SmartArt), que acrescenta superiores, subordinados e assistentes.',
  peg='Trocar SmartArt por formas de fluxograma.',
  kw=['SmartArt', 'Hierarquia'])
I(P, 1, 'Gráfico no PowerPoint',
  'Ao inserir um gráfico no PowerPoint (Inserir > Gráfico), abre-se uma planilha do Excel para digitar os dados que o alimentam.', 'C',
  'O gráfico inserido traz uma **planilha de dados** do Excel embutida; em **Editar Dados** ela reabre.',
  kw=['Inserir > Gráfico', 'Editar Dados'])
I(P, 1, 'Efeitos de animação',
  'As categorias de efeitos de animação do PowerPoint são apenas Entrada e Saída.', 'E',
  'Há quatro: **Entrada**, **Ênfase**, **Saída** e **Trajetórias de Animação**. O **Painel de Animação** mostra a ordem e o disparo (ao clicar, com o anterior, após o anterior).',
  peg='Omitir Ênfase e Trajetórias.',
  kw=['Entrada', 'Ênfase', 'Trajetórias de Animação'])
I(P, 1, 'Plano de fundo',
  'O comando Formatar Plano de Fundo, na guia Design, permite aplicar cor sólida, gradiente, imagem ou textura ao slide atual ou a todos.', 'C',
  '**Design > Formatar Plano de Fundo**: preenchimento sólido, **gradiente**, **imagem ou textura**, padrão; com **Aplicar a Todos**, vale para toda a apresentação.',
  kw=['Formatar Plano de Fundo', 'Design'])

# --- INF-2.3.5 · Rodada 2
I(P, 2, 'Variantes do tema',
  'As Variantes, que trocam o esquema de cores, fontes e efeitos do tema aplicado, ficam na guia Animações.', 'E',
  'As **Variantes** ficam na guia **Design**, ao lado dos **Temas**. Os temas dão o visual; as **Variantes** mudam **cores**, **fontes**, **efeitos** e **estilos de plano de fundo** dentro do tema.',
  peg='Pôr as Variantes na guia Animações.',
  kw=['Variantes', 'esquema de cores'])
I(P, 2, 'Folheto mestre',
  'O Folheto Mestre define o layout dos slides exibidos na tela durante a apresentação.', 'E',
  'O **Folheto Mestre** define a aparência dos **folhetos impressos** (quantos slides por página, cabeçalho, rodapé); a tela segue o **Slide Mestre**. Há também as **Anotações Mestras**.',
  peg='Trocar folheto mestre por slide mestre.',
  kw=['Folheto Mestre', 'impressos'])
I(P, 2, 'Transformar',
  'A transição Transformar anima a passagem entre dois slides parecidos, movendo e redimensionando os objetos de um para o outro.', 'C',
  '**Transformar** (Morph), disponível no Microsoft 365 e versões recentes, cria movimento suave entre slides com objetos em comum.',
  kw=['Transformar', 'transição'])

# ======================= INF-2.3.6 · Integração com Word e Excel =======================
P = 'DBA26-INF-2.3.6'
I(P, 1, 'Colar com vínculo',
  'Ao colar no PowerPoint um intervalo do Excel com a opção Colar Vínculo, as alterações feitas na planilha de origem podem ser refletidas no slide.', 'C',
  '**Colar Especial > Colar vínculo** cria **objeto vinculado**: ele acompanha a planilha de origem (atualizando ao abrir ou manualmente). Se o arquivo de origem mudar de lugar, o vínculo se quebra.',
  kw=['Colar vínculo', 'vinculado'])
I(P, 1, 'Objeto incorporado',
  'A planilha do Excel incorporada a um slide continua ligada ao arquivo de origem, de modo que alterar o arquivo original altera o slide.', 'E',
  'O **objeto incorporado** é uma **cópia** que vive dentro da apresentação: edita-se com duplo clique (com os recursos do Excel), mas **não acompanha** o arquivo original. Quem acompanha é o **vinculado**.',
  peg='Confundir incorporar com vincular.',
  kw=['incorporado', 'cópia'])
I(P, 1, 'Folhetos no Word',
  'Pelo comando Arquivo > Exportar > Criar Folhetos, o PowerPoint envia os slides e as anotações para um documento do Word.', 'C',
  '**Criar Folhetos** (Enviar para o Microsoft Word) monta no Word os slides com anotações ou linhas em branco, com opção de colar ou colar vínculo.',
  kw=['Criar Folhetos', 'Word'])
I(P, 1, 'Slides a partir de estrutura de tópicos',
  'O PowerPoint não aproveita documentos do Word para criar slides; o texto tem de ser digitado de novo.', 'E',
  'Em **Novo Slide > Slides da Estrutura de Tópicos**, o PowerPoint lê um documento do Word: cada parágrafo **Título 1** vira título de slide e o **Título 2**, primeiro nível de texto.',
  peg='Negar a importação de estrutura de tópicos.',
  kw=['Slides da Estrutura de Tópicos', 'Título 1'])
I(P, 1, 'Tabela do Excel no slide',
  'Copiar células do Excel e colar no PowerPoint com a opção padrão cria uma tabela do PowerPoint, editável no próprio slide.', 'C',
  'A colagem padrão transforma as células em **tabela** do PowerPoint (com a guia Design da Tabela); as **Opções de Colagem** permitem, em vez disso, incorporar, colar como imagem ou manter só o texto.',
  kw=['Opções de Colagem', 'tabela'])

# --- INF-2.3.6 · Rodada 2
I(P, 2, 'Colar como imagem',
  'Colar um gráfico do Excel no PowerPoint como imagem mantém a possibilidade de editar seus dados com duplo clique.', 'E',
  'Como **imagem**, o gráfico vira figura estática: não há dados por trás. Para editar os dados, cola-se como **gráfico** (incorporado ou vinculado).',
  peg='Achar que a imagem guarda os dados.',
  kw=['imagem', 'estática'])
I(P, 2, 'Atualizar vínculos',
  'Ao abrir uma apresentação com objetos vinculados a outros arquivos, o PowerPoint pode exibir aviso de segurança e perguntar se deve atualizar os vínculos.', 'C',
  'Por segurança, o PowerPoint **pergunta** antes de **atualizar vínculos**; editar os vínculos (Arquivo > Informações > Editar Links para Arquivos) permite mudar a origem ou quebrar o vínculo.',
  kw=['atualizar vínculos', 'Editar Links'])
I(P, 2, 'Inserir objeto',
  'O comando Inserir > Objeto permite inserir no slide um documento do Word ou uma planilha do Excel novos ou a partir de arquivo, como ícone ou conteúdo.', 'C',
  '**Inserir > Objeto**: Criar novo ou **Criar do arquivo**, com as caixas **Vincular** e **Exibir como ícone** — a banca combina essas opções com vinculado × incorporado.',
  kw=['Inserir > Objeto', 'Vincular'])
