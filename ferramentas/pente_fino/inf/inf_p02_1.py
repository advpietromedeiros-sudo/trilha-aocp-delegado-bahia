# Pente Fino de Informática — INF-2 (Microsoft 365), INF-2.1 e INF-2.1.1 a INF-2.1.5 (Word) (08/11/2026).
# Redação própria. Versão de referência: Word do Microsoft 365 em português; LibreOffice Writer 7.x/24.x quando citado.
from base import I
from inf_fontes import FWD

# ======================= INF-2 · Pacote Office 365 =======================
P = 'DBA26-INF-2'
I(P, 1, 'Microsoft 365 como assinatura',
  'O Microsoft 365 é oferecido por assinatura e reúne aplicativos como Word, Excel, PowerPoint e Outlook, com armazenamento no OneDrive e atualizações contínuas.', 'C',
  'O antigo "Office 365" virou **Microsoft 365**: **assinatura** que inclui os aplicativos (para computador e web), **OneDrive** e atualizações frequentes — diferente das versões perpétuas (Office 2019, 2021, 2024), compradas uma vez.',
  kw=['Microsoft 365', 'assinatura'])
I(P, 1, 'Equivalentes no LibreOffice',
  'No LibreOffice, os equivalentes de Word, Excel e PowerPoint são, respectivamente, Calc, Impress e Writer.', 'E',
  'A ordem certa: **Word ↔ Writer**, **Excel ↔ Calc**, **PowerPoint ↔ Impress**. O LibreOffice é **livre e gratuito** e grava por padrão no formato **ODF** (.odt, .ods, .odp).',
  peg='Embaralhar os equivalentes do LibreOffice.',
  kw=['Writer', 'Calc', 'Impress'])
I(P, 1, 'Formatos padrão',
  'Os formatos padrão do Word, do Excel e do PowerPoint atuais são, respectivamente, .docx, .xlsx e .pptx, baseados em XML.', 'C',
  'Desde o Office 2007, os formatos padrão são os **Office Open XML**: **.docx**, **.xlsx** e **.pptx** (arquivos compactados com XML dentro). Os antigos .doc, .xls e .ppt ainda abrem, em modo de compatibilidade.',
  kw=['.docx', '.xlsx', '.pptx'])
I(P, 1, 'Formato com macro',
  'O documento do Word que contém macros pode ser salvo normalmente no formato .docx, que preserva o código das macros.', 'E',
  'O **.docx não guarda macros**: o formato habilitado para macro é o **.docm** (e .xlsm no Excel, .pptm no PowerPoint). Macro é código VBA e pode carregar **vírus de macro**.',
  peg='Supor que o .docx guarda macros.',
  kw=['.docm', 'macros'])
I(P, 1, 'Coautoria',
  'No Microsoft 365, a coautoria, edição simultânea por várias pessoas, só funciona com o arquivo salvo no disco local de cada coautor e enviado a eles por e-mail.', 'E',
  'É o contrário: a **coautoria** exige o arquivo na **nuvem** (OneDrive/SharePoint), compartilhado por link; ali a edição é **simultânea**, com o **Salvamento Automático** gravando as alterações. Cópias por e-mail viram versões separadas.',
  peg='Ligar a coautoria a cópias locais.',
  kw=['coautoria', 'OneDrive'])

# --- INF-2 · Rodada 2
I(P, 2, 'Salvamento Automático',
  'O Salvamento Automático do Microsoft 365 funciona da mesma forma para arquivos salvos apenas no disco local e para arquivos no OneDrive.', 'E',
  'O **Salvamento Automático** (botão no canto superior esquerdo) atua nos arquivos salvos no **OneDrive** ou no **SharePoint**; para arquivo só no disco local fica desligado, valendo a **AutoRecuperação** (cópias periódicas para recuperar após falha).',
  peg='Estender o Salvamento Automático a arquivo local.',
  kw=['Salvamento Automático', 'AutoRecuperação'])
I(P, 2, 'Exportar PDF',
  'Word, Excel e PowerPoint do Microsoft 365 salvam ou exportam o arquivo diretamente em PDF, sem necessidade de programa adicional.', 'C',
  'Em **Arquivo > Salvar como** (tipo PDF) ou **Arquivo > Exportar > Criar PDF/XPS**, o Office gera **PDF** nativamente. O LibreOffice também exporta PDF (Arquivo > Exportar como).',
  kw=['PDF', 'Exportar'])
I(P, 2, 'Abrir arquivos ODF',
  'O Microsoft Word não abre nem salva arquivos no formato .odt, próprio do LibreOffice.', 'E',
  'O Word **abre e salva** no formato **ODF** (.odt, Texto OpenDocument), podendo perder alguma formatação. Do mesmo modo, o LibreOffice abre e salva .docx.',
  peg='Negar a compatibilidade com ODF.',
  kw=['.odt', 'OpenDocument'])

# ======================= INF-2.1 · Word: área de trabalho, faixa de opções e menus =======================
P = 'DBA26-INF-2.1'
I(P, 1, 'Faixa de opções',
  'No Word do Microsoft 365, os comandos ficam organizados na Faixa de Opções, dividida em guias, que por sua vez se dividem em grupos.', 'C',
  'A **Faixa de Opções** tem **guias** (Página Inicial, Inserir, Design, Layout, Referências, Correspondências, Revisão, Exibir...) e cada guia tem **grupos** (ex.: Fonte, Parágrafo, Estilos).',
  kw=['Faixa de Opções', 'guias', 'grupos'])
I(P, 1, 'Guia Arquivo',
  'A guia Arquivo do Word abre o modo Backstage, com comandos como Novo, Abrir, Salvar como, Imprimir, Compartilhar, Exportar e Opções.', 'C',
  'A guia **Arquivo** não mostra uma faixa: abre o **Backstage**, área de gestão do arquivo (salvar, imprimir, exportar, informações, opções do programa).',
  kw=['Backstage', 'Arquivo'])
I(P, 1, 'Mala direta',
  'Os recursos de mala direta, como Iniciar Mala Direta, Selecionar Destinatários e Inserir Campo de Mesclagem, ficam na guia Revisão do Word.', 'E',
  'A **mala direta** está na guia **Correspondências**. A guia **Revisão** reúne ortografia e gramática, contar palavras, comentários, **Controlar Alterações** e comparar documentos.',
  peg='Pôr a mala direta na guia Revisão.',
  kw=['Correspondências', 'mala direta'])
I(P, 1, 'Sumário',
  'O sumário automático é inserido pela guia Correspondências e é montado a partir das palavras marcadas em negrito no texto.', 'E',
  'O sumário fica em **Referências > Sumário**, onde o Word lista os parágrafos com **estilos de título** (Título 1, Título 2...). Mudou o texto, usa-se **Atualizar Sumário**. Notas de rodapé, citações e legendas também ficam em Referências.',
  peg='Trocar a guia e a base do sumário (estilos de título, não negrito).',
  kw=['Referências', 'Sumário', 'estilos de título'])
I(P, 1, 'Barra de status',
  'A barra de status do Word mostra apenas o nome do arquivo e não pode ser personalizada.', 'E',
  'A **barra de status** (rodapé da janela) mostra **página atual e total**, **contagem de palavras**, idioma, os botões de **modo de exibição** e o **zoom**; clicando nela com o botão direito escolhe-se o que exibir.',
  peg='Reduzir a barra de status ao nome do arquivo.',
  kw=['barra de status', 'contagem de palavras'])
I(P, 1, 'Verificar ortografia',
  'No Word, a tecla F7 inicia a verificação de ortografia e gramática (painel Editor), e F12 abre a caixa Salvar como.', 'C',
  '**F7** abre a revisão de **ortografia e gramática** (painel **Editor**); **F12** abre **Salvar como**.' + FWD,
  kw=['F7', 'F12', 'Salvar como'])
I(P, 1, 'Modos de exibição',
  'Os modos de exibição do Word são apenas dois: Layout de Impressão e Rascunho.', 'E',
  'A guia **Exibir** traz **Modo de Leitura**, **Layout de Impressão** (o padrão), **Layout da Web**, **Estrutura de Tópicos** e **Rascunho**.',
  peg='Omitir modos de exibição.',
  kw=['Modo de Leitura', 'Layout de Impressão', 'Estrutura de Tópicos'])

# --- INF-2.1 · Rodada 2
I(P, 2, 'Barra de Ferramentas de Acesso Rápido',
  'A Barra de Ferramentas de Acesso Rápido do Word tem comandos fixos, definidos pela Microsoft, e não admite inclusão nem retirada de botões pelo usuário.', 'E',
  'A **Barra de Ferramentas de Acesso Rápido** é personalizável, com comandos frequentes como Salvar, Desfazer e Impressão Rápida (seta ao lado dela ou Arquivo > Opções > Barra de Ferramentas de Acesso Rápido) e pode ficar acima ou abaixo da faixa.',
  peg='Negar a personalização da barra.',
  kw=['Barra de Ferramentas de Acesso Rápido', 'personalizável'])
I(P, 2, 'Controlar Alterações',
  'O recurso Controlar Alterações, ativado na guia Revisão, registra inserções, exclusões e mudanças de formatação, que depois podem ser aceitas ou rejeitadas uma a uma.', 'C',
  '**Controlar Alterações** (guia **Revisão**) marca cada mudança com o autor; o revisor **aceita** ou **rejeita** cada uma. Não confundir com **comentários**, que são observações à margem.',
  kw=['Controlar Alterações', 'Revisão'])
I(P, 2, 'Marca d\'água',
  'No Word do Microsoft 365, a marca d\'água fica na guia Inserir, no grupo Tabelas.', 'E',
  'A **marca d\'água** fica na guia **Design** (grupo Plano de Fundo da Página), ao lado de **Cor da Página** e **Bordas de Página**. Em versões antigas (2010) estava em Layout da Página.',
  peg='Situar a marca d\'água na guia Inserir.',
  kw=['marca d\'água', 'Design'])
I(P, 2, 'Localizar e substituir',
  'No Word, Ctrl + H abre a caixa Substituir, que troca um termo por outro em todo o documento, e Ctrl + F abre a pesquisa no painel de Navegação.', 'C',
  '**Ctrl + F** abre o **painel de Navegação** com a pesquisa; **Ctrl + H**, a caixa **Localizar e Substituir** (guia Substituir), que aceita também formatos e caracteres especiais.' + FWD,
  kw=['Ctrl + H', 'Substituir'])

# ======================= INF-2.1.1 · Formatação: margens, tabulação, recuo, espaçamento, fontes =======================
P = 'DBA26-INF-2.1.1'
I(P, 1, 'Negrito, itálico e sublinhado',
  'No Word em português, os atalhos de negrito, itálico e sublinhado são, respectivamente, Ctrl + N, Ctrl + I e Ctrl + S.', 'C',
  'Na versão em português: **Ctrl + N** (negrito), **Ctrl + I** (itálico), **Ctrl + S** (sublinhado). Cuidado: no Word em português **Ctrl + B** é **salvar**, não negrito (que é Ctrl + B na versão em inglês).' + FWD,
  kw=['Ctrl + N', 'Ctrl + I', 'Ctrl + S'])
I(P, 1, 'Alinhamento justificado',
  'Para alinhar o texto igualmente às margens esquerda e direita, usa-se o alinhamento centralizado (Ctrl + E).', 'E',
  'O alinhamento que encosta o texto nas **duas margens** é o **justificado** (**Ctrl + J**). **Ctrl + E** **centraliza** o parágrafo.' + FWD,
  peg='Confundir justificado com centralizado.',
  kw=['justificado', 'Ctrl + J'])
I(P, 1, 'Recuo de primeira linha × deslocamento',
  'O recuo de primeira linha afasta da margem só a primeira linha do parágrafo; o recuo deslocado (deslocamento) afasta todas as linhas, menos a primeira.', 'C',
  '**Primeira linha**: só a 1ª linha entra (parágrafo tradicional). **Deslocamento**: a 1ª linha fica na margem e as demais entram (útil em referências bibliográficas). Ajustam-se na régua ou em Parágrafo.',
  kw=['recuo de primeira linha', 'deslocamento'])
I(P, 1, 'Espaçamento entre linhas',
  'No Word, Ctrl + 2 aplica espaçamento duplo entre linhas, Ctrl + 5 aplica 1,5 linha e Ctrl + 1 aplica espaçamento simples.', 'C',
  'Atalhos de **espaçamento entre linhas**: **Ctrl + 1** (simples), **Ctrl + 5** (1,5) e **Ctrl + 2** (duplo). O espaçamento **antes/depois** do parágrafo é outra medida, ajustada em Layout ou em Parágrafo.' + FWD,
  kw=['espaçamento entre linhas', 'Ctrl + 5'])
I(P, 1, 'Subscrito e sobrescrito',
  'Na fórmula da água, H₂O, o número 2 é formatado como sobrescrito, e, em x², o expoente é formatado como subscrito.', 'E',
  'Está trocado: o 2 de **H₂O** é **subscrito** (abaixo da linha); o expoente de **x²** é **sobrescrito** (acima). Os botões ficam no grupo Fonte da Página Inicial.',
  peg='Inverter subscrito e sobrescrito.',
  kw=['subscrito', 'sobrescrito'])
I(P, 1, 'Margens',
  'As margens do documento são definidas na guia Página Inicial, no grupo Parágrafo.', 'E',
  'As **margens** ficam na guia **Layout** (grupo Configurar Página), com modelos prontos (Normal, Estreita, Moderada...) e **Margens Personalizadas**. O grupo Parágrafo trata de recuos, alinhamento e espaçamento.',
  peg='Situar margens no grupo Parágrafo.',
  kw=['margens', 'Layout'])

# --- INF-2.1.1 · Rodada 2
I(P, 2, 'Tipos de tabulação',
  'O Word oferece tabulação à esquerda, centralizada, à direita, decimal e barra; a decimal alinha os números pela vírgula decimal.', 'C',
  'São os cinco tipos de **tabulação** da régua; a **decimal** alinha valores pela **vírgula** (ou ponto, conforme o idioma), útil em colunas de números. Os **caracteres de preenchimento** (pontilhado) aparecem em sumários.',
  kw=['tabulação', 'decimal'])
I(P, 2, 'Pincel de Formatação',
  'O Pincel de Formatação copia o texto selecionado para a área de transferência, para ser colado em outro ponto do documento.', 'E',
  'O **Pincel de Formatação** copia só a **formatação** (fonte, cor, tamanho, parágrafo) e a aplica a outro trecho; com **duplo clique**, fica ativo para vários trechos até se pressionar Esc.',
  peg='Confundir copiar formatação com copiar texto.',
  kw=['Pincel de Formatação', 'formatação'])
I(P, 2, 'Aumentar a fonte',
  'O atalho Ctrl + Shift + > aumenta o tamanho da fonte do texto selecionado, e Ctrl + Shift + < o diminui.', 'C',
  '**Ctrl + Shift + >** e **Ctrl + Shift + <** sobem e descem o tamanho da fonte pelos tamanhos da lista; **Ctrl + ]** e **Ctrl + [** mudam de 1 em 1 ponto.' + FWD,
  kw=['Ctrl + Shift + >', 'tamanho da fonte'])
I(P, 2, 'Limpar formatação',
  'O comando Limpar Toda a Formatação apaga o texto selecionado, deixando apenas os espaços em branco.', 'E',
  '**Limpar Toda a Formatação** (grupo Fonte) remove a formatação e devolve o trecho ao estilo **Normal**, **mantendo o texto**.',
  peg='Achar que limpar formatação apaga o texto.',
  kw=['Limpar Toda a Formatação', 'Normal'])

# ======================= INF-2.1.2 · Listas e colunas =======================
P = 'DBA26-INF-2.1.2'
I(P, 1, 'Tipos de lista',
  'O Word oferece listas com marcadores, listas numeradas e listas de vários níveis, todas no grupo Parágrafo da guia Página Inicial.', 'C',
  'No grupo **Parágrafo**: **Marcadores**, **Numeração** e **Lista de Vários Níveis**. Lista numerada se usa quando a ordem importa; marcadores, quando não.',
  kw=['marcadores', 'numeração', 'vários níveis'])
I(P, 1, 'Rebaixar nível na lista',
  'Numa lista, a tecla Tab no início do item eleva-o um nível, aproximando-o da margem, e Shift + Tab o rebaixa.', 'E',
  'É o contrário: **Tab** **rebaixa** o item (mais recuado, subnível) e **Shift + Tab** o **promove** (volta ao nível superior).',
  peg='Inverter Tab e Shift + Tab nas listas.',
  kw=['Tab', 'Shift + Tab'])
I(P, 1, 'Colunas',
  'O texto em colunas, como em jornal, é configurado na guia Layout, comando Colunas, que oferece modelos e a opção Mais Colunas.', 'C',
  'Em **Layout > Colunas** escolhem-se 1, 2, 3, esquerda, direita ou **Mais Colunas** (número, largura, espaçamento e linha entre colunas).',
  kw=['Colunas', 'Layout'])
I(P, 1, 'Colunas em parte do documento',
  'O Word só permite dividir em colunas o documento inteiro, não sendo possível ter um trecho em uma coluna e outro em duas na mesma página.', 'E',
  'Selecionando o trecho (ou usando **quebra de seção contínua**), as **colunas** valem só para aquela **seção**; numa mesma página pode haver título em 1 coluna e texto em 2.',
  peg='Negar colunas em parte do documento.',
  kw=['quebra de seção contínua', 'seção'])
I(P, 1, 'Quebra de coluna',
  'O atalho Ctrl + Shift + Enter insere uma quebra de coluna, forçando o texto seguinte a começar na próxima coluna.', 'C',
  '**Ctrl + Shift + Enter** = **quebra de coluna**; **Ctrl + Enter** = **quebra de página**. Também em Layout > Quebras.' + FWD,
  kw=['quebra de coluna', 'Ctrl + Shift + Enter'])

# --- INF-2.1.2 · Rodada 2
I(P, 2, 'Lista automática',
  'Ao digitar "1." seguido de espaço no início de um parágrafo, o Word pode iniciar automaticamente uma lista numerada, comportamento da AutoFormatação ao digitar.', 'C',
  'É a **AutoFormatação ao digitar**: "1." + espaço (ou "*" + espaço, para marcadores) vira lista. Pode-se desfazer na hora com Ctrl + Z ou desligar nas Opções de AutoCorreção.',
  kw=['AutoFormatação', 'lista numerada'])
I(P, 2, 'Reiniciar numeração',
  'Uma lista numerada no Word sempre continua a numeração da lista anterior, sem possibilidade de recomeçar em 1.', 'E',
  'Clicando com o botão direito no número, há **Reiniciar em 1** e **Continuar Numeração**, além de **Definir Valor de Numeração**.',
  peg='Negar o reinício da numeração.',
  kw=['Reiniciar em 1', 'Continuar Numeração'])
I(P, 2, 'Linha entre colunas',
  'Na caixa Mais Colunas, é possível exigir colunas de mesma largura e inserir uma linha vertical entre elas.', 'C',
  'Em **Mais Colunas** marcam-se **Colunas de mesma largura** e **Linha entre colunas**, e se escolhe a partir de onde aplicar (documento inteiro ou deste ponto em diante).',
  kw=['Linha entre colunas', 'Mais Colunas'])

# ======================= INF-2.1.3 · Estilos e modelos =======================
P = 'DBA26-INF-2.1.3'
I(P, 1, 'Estilos',
  'Estilo é um conjunto de formatações com nome (fonte, tamanho, cor, espaçamento, recuo), aplicado de uma vez a um trecho; alterar o estilo atualiza todos os trechos que o usam.', 'C',
  'O **estilo** padroniza: mudou-se a definição de "Título 1", todos os títulos 1 mudam. A galeria fica em **Página Inicial > Estilos**.',
  kw=['estilo', 'Título 1'])
I(P, 1, 'Modelo do Word',
  'O modelo do Word é salvo no formato .docx, o mesmo dos documentos comuns.', 'E',
  'O **modelo** usa **.dotx** (ou **.dotm**, com macros); abrir um modelo cria um **documento novo** baseado nele, preservando o modelo. O modelo padrão de todo documento em branco é o **Normal.dotm**.',
  peg='Trocar .dotx por .docx.',
  kw=['.dotx', 'Normal.dotm'])
I(P, 1, 'Estilo Normal',
  'Todo documento novo em branco do Word começa com o texto no estilo Normal.', 'C',
  'O **Normal** é o estilo de base do corpo do texto; vários estilos herdam dele. Alterá-lo "para novos documentos" mexe no Normal.dotm.',
  kw=['estilo Normal', 'documento em branco'])
I(P, 1, 'Estilos e navegação',
  'Os estilos de título não têm relação com o Painel de Navegação, que mostra apenas as páginas do documento em miniatura.', 'E',
  'O **Painel de Navegação** (Exibir > Painel de Navegação ou Ctrl + F) lista os **títulos** formatados com **estilos de título**, permitindo saltar e reorganizar seções; também mostra páginas e resultados de busca.',
  peg='Desligar estilos de título do Painel de Navegação.',
  kw=['Painel de Navegação', 'estilos de título'])
I(P, 1, 'Estilos no LibreOffice',
  'No LibreOffice Writer, a tecla F11 abre o painel de Estilos, onde há estilos de parágrafo, de caractere, de quadro, de página e de lista.', 'C',
  'No **Writer**, **F11** abre o **Estilos** na barra lateral; o Writer separa estilos de **parágrafo, caractere, quadro, página, lista** e tabela — o estilo de **página** é marca do LibreOffice. Atalho do LibreOffice 7.x/24.x em configuração padrão.',
  kw=['F11', 'estilos de página'])

# --- INF-2.1.3 · Rodada 2
I(P, 2, 'Estilo de caractere × parágrafo',
  'Estilo de parágrafo atinge o parágrafo inteiro, mesmo com só uma palavra selecionada; estilo de caractere atinge apenas o texto selecionado.', 'C',
  'Estilo de **parágrafo** (ex.: Título 1) vale para o parágrafo todo, inclusive recuo e espaçamento; estilo de **caractere** (ex.: Ênfase) vale só para as letras selecionadas. Há também o estilo **vinculado**, que age de um ou outro modo.',
  kw=['estilo de parágrafo', 'estilo de caractere'])
I(P, 2, 'Temas',
  'O tema do documento, escolhido na guia Design, altera apenas a cor da página, sem mudar fontes ou estilos.', 'E',
  'O **tema** (guia **Design**) é um pacote de **cores, fontes e efeitos**; mudá-lo altera a aparência dos **estilos** que usam as cores e fontes do tema. A cor da página é comando separado.',
  peg='Reduzir o tema à cor da página.',
  kw=['tema', 'Design'])
I(P, 2, 'Modelo e documento novo',
  'Ao dar duplo clique em um arquivo .dotx no Explorador, o Word abre o próprio modelo para edição, e salvar com Ctrl + B grava as alterações no .dotx.', 'E',
  'Não: o duplo clique no **.dotx** cria um **Documento1** baseado nele. Para editar o próprio **modelo**, abre-se pelo Word (Arquivo > Abrir) ou pelo menu de contexto "Abrir".',
  peg='Achar que o duplo clique abre o modelo para edição.',
  kw=['.dotx', 'documento novo'])

# ======================= INF-2.1.4 · Cabeçalhos e rodapés =======================
P = 'DBA26-INF-2.1.4'
I(P, 1, 'Onde inserir',
  'Cabeçalho, rodapé e número de página são inseridos pela guia Inserir, no grupo Cabeçalho e Rodapé.', 'C',
  '**Inserir > grupo Cabeçalho e Rodapé**: **Cabeçalho**, **Rodapé** e **Número de Página**. Também se edita com **duplo clique** na área superior ou inferior da página.',
  kw=['Cabeçalho e Rodapé', 'Número de Página'])
I(P, 1, 'Repetição em todas as páginas',
  'O texto do cabeçalho precisa ser digitado em cada página, pois o Word não o repete automaticamente.', 'E',
  'O **cabeçalho** se **repete automaticamente** em todas as páginas da **seção**; é por isso que número de página e título do documento vão lá.',
  peg='Negar a repetição automática do cabeçalho.',
  kw=['repete automaticamente', 'seção'])
I(P, 1, 'Primeira página diferente',
  'A opção Primeira Página Diferente permite que a capa fique sem cabeçalho e sem número enquanto as demais páginas os exibem.', 'C',
  'Na guia contextual **Cabeçalho e Rodapé**, **Primeira Página Diferente** dá à primeira página cabeçalho/rodapé próprio (ou nenhum) — típico de capa.',
  kw=['Primeira Página Diferente', 'capa'])
I(P, 1, 'Páginas pares e ímpares',
  'O Word não permite cabeçalhos diferentes para páginas pares e ímpares no mesmo documento.', 'E',
  'Há a opção **Páginas Pares e Ímpares Diferentes**, usada em livros (número à direita nas ímpares e à esquerda nas pares).',
  peg='Negar cabeçalho par/ímpar.',
  kw=['Páginas Pares e Ímpares Diferentes', 'cabeçalho'])
I(P, 1, 'Número de página no Writer',
  'No LibreOffice Writer, o número de página costuma ser inserido como campo no cabeçalho ou no rodapé, para se repetir em todas as páginas do estilo de página.', 'C',
  'No **Writer**, ativa-se o cabeçalho/rodapé (Inserir > Cabeçalho e rodapé) e insere-se o **campo** Número da página (Inserir > Número de página ou Inserir > Campo); vale para as páginas do mesmo **estilo de página**.',
  kw=['campo', 'Número da página'])

# --- INF-2.1.4 · Rodada 2
I(P, 2, 'Vincular ao Anterior',
  'Para que uma nova seção tenha cabeçalho diferente da anterior, é preciso desativar o botão Vincular ao Anterior no cabeçalho da nova seção.', 'C',
  'Cada **seção** pode ter cabeçalho próprio, mas, por padrão, ela herda o da anterior (**Vincular ao Anterior** ativo). Desligando-o, a mudança não afeta a seção de trás.',
  kw=['Vincular ao Anterior', 'seção'])
I(P, 2, 'Número de página manual',
  'O número de página do Word é texto fixo, que deve ser corrigido manualmente sempre que páginas forem incluídas ou excluídas.', 'E',
  'O **número de página** é um **campo** (PAGE): atualiza-se sozinho. Pode-se mudar o **formato** (1, i, a...) e o número **inicial** em Formatar Números de Página.',
  peg='Tratar o número de página como texto fixo.',
  kw=['campo', 'Formatar Números de Página'])
I(P, 2, 'Fechar cabeçalho',
  'Para sair da edição do cabeçalho, basta clicar duas vezes no corpo do documento ou usar o botão Fechar Cabeçalho e Rodapé.', 'C',
  '**Duplo clique** no corpo do texto ou **Fechar Cabeçalho e Rodapé** (ou Esc) devolve à edição normal; o cabeçalho fica esmaecido no Layout de Impressão.',
  kw=['Fechar Cabeçalho e Rodapé', 'duplo clique'])

# ======================= INF-2.1.5 · Configuração de página =======================
P = 'DBA26-INF-2.1.5'
I(P, 1, 'Orientação',
  'A orientação da página, retrato ou paisagem, é definida na guia Layout, grupo Configurar Página.', 'C',
  'Em **Layout > Configurar Página** ficam **Margens**, **Orientação** (retrato/paisagem), **Tamanho** (A4, Carta, Ofício...), **Colunas** e **Quebras**.',
  kw=['Orientação', 'Configurar Página'])
I(P, 1, 'Orientação mista',
  'Num mesmo documento do Word, todas as páginas têm de ter a mesma orientação; não é possível ter uma página em paisagem entre páginas em retrato.', 'E',
  'Com **quebras de seção** (Próxima página), cada **seção** pode ter **orientação**, margens e tamanho próprios — ex.: uma tabela larga em paisagem no meio de um texto em retrato.',
  peg='Negar orientações diferentes no mesmo documento.',
  kw=['quebras de seção', 'orientação'])
I(P, 1, 'Tamanho do papel',
  'O tamanho A4 mede 21 cm × 29,7 cm, e o tamanho Carta, menor na altura, é o padrão de muitas instalações em inglês.', 'C',
  '**A4** = **21 × 29,7 cm** (padrão no Brasil); **Carta** = 21,59 × 27,94 cm (padrão nos EUA). O tamanho padrão depende do idioma/região da instalação.',
  kw=['A4', 'Carta'])
I(P, 1, 'Quebra de página',
  'O atalho Ctrl + Enter insere uma quebra de seção contínua, sem passar à página seguinte.', 'E',
  '**Ctrl + Enter** insere **quebra de página** (o texto seguinte vai para a próxima página). **Quebra de seção contínua** só existe em Layout > Quebras.' + FWD,
  peg='Trocar quebra de página por quebra de seção.',
  kw=['Ctrl + Enter', 'quebra de página'])
I(P, 1, 'Medianiz',
  'A medianiz é o espaço extra acrescentado à margem para a encadernação do documento.', 'C',
  'Em **Margens Personalizadas** há a **medianiz** (margem de encadernação) e sua posição (esquerda ou superior); com **Margens espelhadas**, as margens interna e externa se alternam entre páginas pares e ímpares.',
  kw=['medianiz', 'encadernação'])

# --- INF-2.1.5 · Rodada 2
I(P, 2, 'Margens espelhadas',
  'A opção Margens Espelhadas faz com que as margens de páginas opostas fiquem simétricas, trocando a margem esquerda e a direita por "interna" e "externa".', 'C',
  'Em **Margens espelhadas** (Várias páginas), as margens passam a **interna** e **externa**, refletidas entre página par e ímpar, como em livro impresso frente e verso.',
  kw=['Margens espelhadas', 'interna e externa'])
I(P, 2, 'Configuração e impressão',
  'Alterar o tamanho do papel na impressora, na tela Imprimir, altera também, de forma permanente, as margens salvas no documento.', 'E',
  'Na tela **Imprimir** (Ctrl + P), a escolha de papel e escala vale para aquela impressão; as **margens** do documento ficam em Layout > Configurar Página. A banca testa a diferença entre configurar a página e configurar a impressão.',
  peg='Igualar configuração de impressão e de página.',
  kw=['Imprimir', 'Configurar Página'])
I(P, 2, 'Números de linha',
  'O Word pode exibir números de linha à margem esquerda, contínuos ou reiniciados a cada página ou seção, pelo comando Números de Linha da guia Layout.', 'C',
  '**Layout > Números de Linha**: contínuos, reiniciar a cada página, a cada seção, ou suprimir no parágrafo atual — usado em peças e contratos.',
  kw=['Números de Linha', 'Layout'])
