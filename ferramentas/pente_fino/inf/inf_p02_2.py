# Pente Fino de Informática — INF-2.2 e INF-2.2.1 a INF-2.2.6 (Excel) (08/11/2026).
# Redação própria. Versão de referência: Excel do Microsoft 365 em português (separador de argumentos ";",
# vírgula decimal); LibreOffice Calc quando citado.
from base import I
from inf_fontes import FX, FXF

# ======================= INF-2.2 · Excel: área de trabalho, deslocamento, seleção =======================
P = 'DBA26-INF-2.2'
I(P, 1, 'Pasta de trabalho e planilha',
  'No Excel, o arquivo é chamado pasta de trabalho e pode conter várias planilhas, identificadas por guias na parte inferior da janela.', 'C',
  'O arquivo (.xlsx) é a **pasta de trabalho**; cada **planilha** é uma guia (Planilha1, Planilha2...). **Shift + F11** insere nova planilha.' + FX,
  kw=['pasta de trabalho', 'planilha'])
I(P, 1, 'Endereço da célula',
  'No Excel, a célula é identificada pelo número da linha seguido da letra da coluna, como em 3B.', 'E',
  'O endereço é **letra da coluna + número da linha**: **B3**. Ele aparece na **Caixa de Nome**, à esquerda da **barra de fórmulas**.',
  peg='Inverter a ordem coluna/linha.',
  kw=['letra da coluna', 'Caixa de Nome'])
I(P, 1, 'Limite de linhas e colunas',
  'Uma planilha do Excel atual tem 1.048.576 linhas e 16.384 colunas, a última delas a coluna XFD.', 'C',
  'Nas versões desde 2007: **1.048.576 linhas** × **16.384 colunas** (de A até **XFD**). O formato .xls antigo tinha 65.536 linhas e 256 colunas.',
  kw=['1.048.576 linhas', 'XFD'])
I(P, 1, 'Ir para A1',
  'O atalho Ctrl + End leva o cursor para a célula A1, início da planilha.', 'E',
  '**Ctrl + Home** vai para o **início** (A1, ou a primeira célula fora do painel congelado); **Ctrl + End** vai para a **última célula usada** da planilha.' + FX,
  peg='Trocar Ctrl + Home por Ctrl + End.',
  kw=['Ctrl + Home', 'Ctrl + End'])
I(P, 1, 'Selecionar coluna e linha',
  'No Excel, Ctrl + barra de espaço seleciona a coluna inteira da célula ativa, e Shift + barra de espaço seleciona a linha inteira.', 'C',
  '**Ctrl + Espaço** = **coluna** inteira; **Shift + Espaço** = **linha** inteira. Clicar no cabeçalho da coluna (letra) ou da linha (número) faz o mesmo com o mouse.' + FX,
  kw=['Ctrl + Espaço', 'Shift + Espaço'])
I(P, 1, 'Seleção de intervalos não adjacentes',
  'Para selecionar os intervalos A1:A5 e C1:C5 ao mesmo tempo, sem selecionar a coluna B, arrasta-se o primeiro intervalo e, mantendo Shift pressionada, arrasta-se o segundo.', 'E',
  'Intervalos **não adjacentes** se somam com **Ctrl**; **Shift + clique** estende a seleção até a célula clicada, formando um **retângulo** contínuo (A1:C5, com a coluna B).',
  peg='Trocar Ctrl por Shift na seleção múltipla.',
  kw=['não adjacentes', 'Ctrl'])
I(P, 1, 'Trocar de planilha',
  'O atalho Ctrl + Page Down volta para a planilha anterior da pasta de trabalho, e Ctrl + Page Up passa para a próxima.', 'E',
  'Está invertido: **Ctrl + Page Down** vai para a **próxima** planilha; **Ctrl + Page Up**, para a **anterior**.' + FX,
  peg='Inverter Page Down e Page Up.',
  kw=['Ctrl + Page Down', 'planilhas'])
I(P, 1, 'Editar a célula',
  'A tecla F2, no Excel, exclui o conteúdo da célula ativa.', 'E',
  '**F2** entra em **modo de edição** da célula ativa, com o cursor no fim do conteúdo. Apagar o conteúdo é **Delete**.' + FX,
  peg='Atribuir a F2 a exclusão.',
  kw=['F2', 'modo de edição'])

# --- INF-2.2 · Rodada 2
I(P, 2, 'Ctrl + seta',
  'Ctrl + seta para baixo leva à borda da região de dados atual na coluna — a última célula preenchida antes de uma célula vazia —, e Ctrl + Shift + seta estende a seleção até lá.', 'C',
  '**Ctrl + seta** salta até a **borda da região** de dados; com **Shift**, **seleciona** o trajeto. É o modo rápido de selecionar uma coluna de dados inteira.' + FX,
  kw=['Ctrl + seta', 'borda da região'])
I(P, 2, 'Congelar painéis',
  'O comando Congelar Painéis fica na guia Dados e bloqueia a edição das células selecionadas, protegendo-as contra alteração.', 'E',
  'O comando fica em **Exibir > Congelar Painéis** (Congelar Painéis, Congelar Linha Superior, Congelar Primeira Coluna): o cabeçalho fica fixo na tela enquanto se rola o resto. Não protege nada: bloquear edição é **Proteger Planilha** (guia Revisão).',
  peg='Confundir congelar painéis com proteger planilha.',
  kw=['Congelar Painéis', 'Exibir'])
I(P, 2, 'Nova linha dentro da célula',
  'No Excel, pressionar Enter durante a digitação insere uma nova linha dentro da mesma célula.', 'E',
  '**Enter** confirma e desce para a célula de baixo. A quebra de linha **dentro** da célula é **Alt + Enter**.' + FX,
  peg='Trocar Alt + Enter por Enter.',
  kw=['Alt + Enter', 'mesma célula'])
I(P, 2, 'Ctrl + Enter',
  'Com um intervalo selecionado, digitar um valor e pressionar Ctrl + Enter preenche todas as células selecionadas com esse valor.', 'C',
  '**Ctrl + Enter** grava a entrada em **todas** as células selecionadas de uma vez (vale também para fórmulas, que se ajustam como numa cópia).' + FX,
  kw=['Ctrl + Enter', 'células selecionadas'])
I(P, 2, 'Ocultar × excluir',
  'Ocultar uma coluna do Excel exclui definitivamente os dados nela contidos, e as fórmulas que a referenciam passam a apresentar erro.', 'E',
  '**Ocultar** só esconde da tela: os dados permanecem e as fórmulas continuam funcionando. Quem gera **#REF!** é **excluir** a coluna referenciada.',
  peg='Igualar ocultar a excluir.',
  kw=['Ocultar', '#REF!'])

# ======================= INF-2.2.1 · Números, textos, fórmulas, datas; referência relativa e absoluta =======================
P = 'DBA26-INF-2.2.1'
I(P, 1, 'Início da fórmula',
  'No Excel, a fórmula começa com o sinal de igual (=); sem ele, o conteúdo é tratado como texto ou número digitado.', 'C',
  'A fórmula começa com **=** (o Excel aceita também + ou -, convertendo para =). Digitar "SOMA(A1:A3)" sem o sinal deixa o texto na célula.',
  kw=['sinal de igual', 'fórmula'])
I(P, 1, 'Referência relativa ao copiar',
  'A célula C1 contém =A1+B1. Copiada para C2, a fórmula continua =A1+B1, pois as referências relativas não se alteram na cópia.', 'E',
  'Referência **relativa** se **ajusta** na cópia: em C2 vira **=A2+B2** (uma linha abaixo). Só a referência **absoluta** ($A$1) fica fixa.',
  peg='Dizer que a referência relativa não se ajusta.',
  kw=['referência relativa', 'ajusta'])
I(P, 1, 'Referência absoluta',
  'Copiada de C1 para C5, a fórmula =$A$1*B1 passa a ser =$A$1*B5.', 'C',
  '**$A$1** é **absoluta** (linha e coluna travadas) e não muda; **B1** é relativa e desce 4 linhas, virando **B5**.',
  kw=['referência absoluta', '$A$1'])
I(P, 1, 'Referência mista',
  'Na referência A$1, a coluna fica fixa e a linha varia quando a fórmula é copiada.', 'E',
  'O **$** trava o que vem logo depois dele: em **A$1** fica fixa a **linha 1** e a **coluna** varia; em **$A1** fica fixa a **coluna A** e a linha varia.',
  peg='Ler o $ ao contrário na referência mista.',
  kw=['referência mista', 'A$1'])
I(P, 1, 'Alternar referências com F4',
  'Durante a edição de uma fórmula, a tecla F4 alterna a referência selecionada entre relativa, absoluta e mista.', 'C',
  '**F4** gira entre **A1 → $A$1 → A$1 → $A1**. Fora da edição, F4 repete o último comando.' + FX,
  kw=['F4', 'absolutas e relativas'])
I(P, 1, 'Data como número',
  'O Excel armazena datas como texto, razão pela qual não é possível subtrair uma data de outra para saber os dias entre elas.', 'E',
  'Datas são **números seriais** (no sistema padrão do Windows, 1 = 01/01/1900); por isso **=B1-A1** dá o número de **dias** entre as datas, e a formatação decide se aparece como data ou número.',
  peg='Dizer que data é texto.',
  kw=['números seriais', 'datas'])

# --- INF-2.2.1 · Rodada 2
I(P, 2, 'Alinhamento padrão',
  'Por padrão, o Excel alinha números e datas à direita da célula e textos à esquerda.', 'C',
  'É o **alinhamento geral**: **número/data à direita**, **texto à esquerda**. Um número alinhado à esquerda é sinal de que foi digitado como **texto** (ex.: com apóstrofo inicial).',
  kw=['alinhamento geral', 'número à direita'])
I(P, 2, 'Apóstrofo inicial',
  'Digitar um apóstrofo antes de um número, como \'00123, faz o apóstrofo aparecer na célula e o valor continuar sendo número, com os zeros à esquerda descartados.', 'E',
  'O **apóstrofo** força **texto**, **não aparece** na célula e **preserva** os zeros à esquerda; útil para CPF, CEP e códigos com zero à esquerda. O Excel sinaliza "número armazenado como texto".',
  peg='Ignorar que o apóstrofo converte em texto.',
  kw=['apóstrofo', 'texto'])
I(P, 2, 'Precedência e negação',
  'No Excel, a fórmula =-2^2 retorna -4, porque a potenciação é calculada antes da negação.', 'E',
  'No Excel, a **negação** (sinal de menos unário) tem **precedência maior** que a potência: =-2^2 = **4**. Para obter -4, escreve-se **=-(2^2)**. Depois vêm %, ^, * e /, + e -, & e as comparações.',
  peg='Aplicar a regra da matemática escolar à precedência do Excel.',
  kw=['negação', 'precedência'])
I(P, 2, 'Operadores de referência',
  'Em =SOMA(A1:A3;C1), os dois-pontos indicam intervalo e o ponto e vírgula une referências; assim, a fórmula soma A1, A2, A3 e C1.', 'C',
  'Operadores de referência: **:** (intervalo), **;** (união, no Excel em português) e **espaço** (interseção). A fórmula soma 4 células.',
  kw=['dois-pontos', 'ponto e vírgula'])

# ======================= INF-2.2.2 · Funções =======================
P = 'DBA26-INF-2.2.2'
I(P, 1, 'MED × MÉDIA',
  'A função MED retorna a média aritmética dos valores, e MÉDIA retorna o valor central do conjunto ordenado.', 'E',
  'Está trocado: **MÉDIA** = média aritmética; **MED** = **mediana** (valor central). **MODO** = valor mais frequente.' + FXF,
  peg='Inverter MED e MÉDIA.',
  kw=['MED', 'mediana', 'MÉDIA'])
I(P, 1, 'CONT.NÚM × CONT.VALORES',
  'CONT.NÚM conta apenas as células com números, e CONT.VALORES conta as células não vazias, inclusive as que contêm texto.', 'C',
  '**CONT.NÚM** = só **números** (datas são números); **CONT.VALORES** = **não vazias** de qualquer tipo; **CONTAR.VAZIO** = vazias.' + FXF,
  kw=['CONT.NÚM', 'CONT.VALORES'])
I(P, 1, 'Função SE',
  'A sintaxe da função SE é =SE(teste_lógico;valor_se_verdadeiro;valor_se_falso).', 'C',
  '**SE** avalia o **teste** e devolve um valor se for verdadeiro e outro se for falso; ex.: =SE(B2>=7;"Aprovado";"Reprovado"). Combina com **E** e **OU** para testes compostos.' + FXF,
  kw=['SE', 'teste_lógico'])
I(P, 1, 'PROCV',
  'A função PROCV procura o valor em qualquer coluna da matriz e pode retornar valores de colunas situadas à esquerda da coluna pesquisada.', 'E',
  '**PROCV** procura na **primeira coluna** da matriz e devolve o valor da coluna indicada **à direita** (núm_índice_coluna); o último argumento **FALSO** pede correspondência **exata**. Para buscar "à esquerda", usa-se **PROCX** (Microsoft 365/2021) ou ÍNDICE com CORRESP.' + FXF,
  peg='Dizer que o PROCV olha à esquerda.',
  kw=['PROCV', 'primeira coluna'])
I(P, 1, 'HOJE × AGORA',
  'A função HOJE() retorna a data e a hora atuais, e AGORA() retorna apenas a hora, sem a data.', 'E',
  'Errado nas duas: **HOJE** = só a data; **AGORA** = data e hora; ambas são **voláteis**. Já **Ctrl + ;** insere a data como valor **fixo**.' + FXF,
  peg='Trocar o retorno de HOJE e AGORA.',
  kw=['HOJE', 'AGORA'])
I(P, 1, 'INT com número negativo',
  'A fórmula =INT(-3,7) retorna -3, pois a função INT simplesmente descarta a parte decimal.', 'E',
  '**INT** arredonda **para baixo** até o inteiro: =INT(-3,7) = **-4**. Quem descarta a parte decimal é **TRUNCAR**: =TRUNCAR(-3,7) = -3. Para positivos, as duas dão o mesmo.' + FXF,
  peg='Confundir INT com TRUNCAR nos negativos.',
  kw=['INT', 'TRUNCAR'])
I(P, 1, 'SOMASE',
  'A função SOMASE soma as células de um intervalo que atendem a um critério, como =SOMASE(A2:A10;"Salvador";B2:B10).', 'C',
  '**SOMASE**(intervalo; critério; [intervalo_soma]) soma o que atende ao **critério**; **SOMASES** aceita vários critérios; **CONT.SE** conta em vez de somar.' + FXF,
  kw=['SOMASE', 'critério'])

# --- INF-2.2.2 · Rodada 2
I(P, 2, 'MOD',
  'A fórmula =MOD(17;5) retorna 2, que é o resto da divisão de 17 por 5.', 'C',
  '**MOD** devolve o **resto** da divisão (17 = 3 × 5 + **2**). É usada, por exemplo, para saber se um número é par (=MOD(A1;2)=0).' + FXF,
  kw=['MOD', 'resto'])
I(P, 2, 'Funções de texto',
  'A fórmula =ESQUERDA("Delegado";3) retorna "ado", os três últimos caracteres do texto.', 'E',
  '**ESQUERDA** pega os primeiros caracteres: **"Del"**. Os últimos são de **DIREITA** ("ado"); do meio, **EXT.TEXTO** (=EXT.TEXTO("Delegado";3;4) = "lega"); **NÚM.CARACT** conta caracteres.',
  peg='Trocar ESQUERDA por DIREITA.',
  kw=['ESQUERDA', 'DIREITA'])
I(P, 2, 'Funções financeiras',
  'A função PGTO calcula o valor da prestação periódica de um empréstimo com pagamentos e taxa de juros constantes.', 'C',
  'Financeiras: **PGTO** (prestação), **VP** (valor presente), **VF** (valor futuro), **TAXA** (juros por período) e **NPER** (número de períodos). A taxa e o número de períodos têm de estar na mesma unidade (mensal com mensal).' + FXF,
  kw=['PGTO', 'VP', 'VF'])
I(P, 2, 'MAIOR × MÁXIMO',
  'A fórmula =MAIOR(A1:A10;2) retorna o maior valor do intervalo multiplicado por 2.', 'E',
  '**MAIOR**(matriz; k) devolve o **k-ésimo maior** valor: com k = 2, o **segundo maior**. O maior de todos é **MÁXIMO** (ou MAIOR com k = 1); **MENOR** funciona ao contrário.' + FXF,
  peg='Ler o k de MAIOR como multiplicador.',
  kw=['MAIOR', 'k-ésimo'])
I(P, 2, 'Concatenação',
  'O operador & une textos, de modo que =A1&" "&B1 junta o conteúdo de A1 e B1 com um espaço entre eles, com o mesmo efeito de CONCATENAR.', 'C',
  '**&** é o operador de **concatenação**; as funções **CONCATENAR**, **CONCAT** e **UNIRTEXTO** (esta com delimitador) fazem o mesmo de modo mais amplo.' + FXF,
  kw=['&', 'CONCATENAR'])

# ======================= INF-2.2.3 · Formatação: número, alinhamento, bordas, fontes, padrões =======================
P = 'DBA26-INF-2.2.3'
I(P, 1, 'Formatar Células',
  'O atalho Ctrl + 1 abre a caixa Formatar Células, com as guias Número, Alinhamento, Fonte, Borda, Preenchimento e Proteção.', 'C',
  '**Ctrl + 1** abre **Formatar Células**. O que editais antigos chamam de "padrões" corresponde hoje à guia **Preenchimento** (cor e padrão de fundo).' + FX,
  kw=['Ctrl + 1', 'Formatar Células'])
I(P, 1, 'Formato não muda o valor',
  'Ao formatar com zero casas decimais uma célula que contém 2,567, o Excel altera o valor armazenado para 3.', 'E',
  'O **formato** muda só a **exibição** (aparece 3), mas o **valor armazenado** continua **2,567** e é ele que entra nos cálculos. Para mudar o valor, usa-se **ARRED**.',
  peg='Confundir exibição com valor.',
  kw=['formato', 'valor armazenado'])
I(P, 1, 'Mesclar e Centralizar',
  'Ao mesclar células que contêm dados, o Excel mantém apenas o valor da célula superior esquerda e descarta os demais.', 'C',
  '**Mesclar e Centralizar** avisa que **só o valor superior esquerdo** permanece. Alternativa que não perde dados: **Centralizar na Seleção** (guia Alinhamento).',
  kw=['Mesclar e Centralizar', 'superior esquerda'])
I(P, 1, 'Quebrar texto',
  'O recurso Quebrar Texto Automaticamente faz o texto longo ocupar várias linhas dentro da mesma célula, aumentando a altura da linha.', 'C',
  '**Quebrar Texto Automaticamente** (grupo Alinhamento) distribui o texto em várias linhas **na célula**; Alt + Enter força a quebra em ponto escolhido.',
  kw=['Quebrar Texto Automaticamente', 'Alinhamento'])
I(P, 1, 'Formato de porcentagem',
  'Aplicar o formato de porcentagem a uma célula com o valor 0,25 faz aparecer 0,25%.', 'E',
  'O formato **porcentagem** multiplica a exibição por 100: **0,25 → 25%**. Para aparecer 0,25%, o valor teria de ser 0,0025. **Ctrl + Shift + %** aplica o formato sem casas decimais.' + FX,
  peg='Esquecer a multiplicação por 100 na exibição.',
  kw=['porcentagem', '25%'])

# --- INF-2.2.3 · Rodada 2
I(P, 2, 'Formatação condicional',
  'A formatação condicional aplica cor, ícone ou barra de dados às células conforme o valor delas, e fica na guia Página Inicial, grupo Estilos.', 'C',
  '**Formatação Condicional** (Página Inicial > Estilos): regras de realce (maior que, texto que contém...), barras de dados, escalas de cor e ícones. Muda com o valor da célula.',
  kw=['Formatação Condicional', 'Estilos'])
I(P, 2, 'Cerquilhas',
  'A exibição de ##### numa célula com número indica que a fórmula contém erro de digitação no nome da função.', 'E',
  '**#####** indica, em regra, que a **coluna é estreita** para mostrar o número ou a data (ou data negativa). Nome de função errado gera **#NOME?**.',
  peg='Confundir ##### com #NOME?.',
  kw=['#####', '#NOME?'])
I(P, 2, 'Formato de moeda',
  'O atalho Ctrl + Shift + $ aplica o formato de moeda com duas casas decimais.', 'C',
  '**Ctrl + Shift + $** = **Moeda** com 2 casas (números negativos entre parênteses, conforme a configuração). O formato **Contábil** alinha o símbolo à esquerda.' + FX,
  kw=['Ctrl + Shift + $', 'Moeda'])

# ======================= INF-2.2.4 · Copiar, colar, recortar, limpar e selecionar =======================
P = 'DBA26-INF-2.2.4'
I(P, 1, 'Delete mantém a formatação',
  'Ao pressionar Delete em células selecionadas, o Excel remove o conteúdo e também a formatação das células.', 'E',
  '**Delete** remove o **conteúdo** (dados e fórmulas) e **mantém** formatos e comentários. O botão **Limpar** (Página Inicial > Edição) oferece Limpar Tudo, Formatos, Conteúdo, Comentários e Hiperlinks.' + FX,
  peg='Achar que Delete apaga a formatação.',
  kw=['Delete', 'Limpar'])
I(P, 1, 'Colar Especial',
  'O Colar Especial (Ctrl + Alt + V) permite colar apenas os valores, apenas as fórmulas, apenas os formatos, transpor linhas e colunas ou operar o conteúdo copiado com o do destino.', 'C',
  '**Colar Especial**: **Valores** (o resultado, sem a fórmula), Fórmulas, Formatos, Comentários, **Transpor** (linhas ↔ colunas) e operações (somar, multiplicar...).' + FX,
  kw=['Colar Especial', 'Transpor'])
I(P, 1, 'Recortar fórmula',
  'Ao recortar e colar uma fórmula em outra célula, as referências relativas se ajustam exatamente como na cópia.', 'E',
  'Na **cópia**, a referência relativa se ajusta; ao **recortar** (mover), a fórmula vai **intacta** e continua apontando para as mesmas células.',
  peg='Igualar recortar e copiar quanto às referências.',
  kw=['recortar', 'mover'])
I(P, 1, 'Alça de preenchimento',
  'Arrastar pela alça de preenchimento uma célula com o texto "jan" gera a sequência fev, mar, abr nas células seguintes.', 'C',
  'A **alça de preenchimento** (quadradinho no canto inferior direito) reconhece **listas** (meses, dias da semana) e **sequências** (1 e 2 selecionados → 3, 4, 5...). Um número sozinho, em regra, é só copiado.',
  kw=['alça de preenchimento', 'sequência'])
I(P, 1, 'Preencher abaixo',
  'O atalho Ctrl + D, no Excel, preenche a célula com o conteúdo e o formato da célula imediatamente acima.', 'C',
  '**Ctrl + D** = **preencher abaixo** (copia a célula de cima para a seleção).' + FX,
  kw=['Ctrl + D', 'preencher abaixo'])

# --- INF-2.2.4 · Rodada 2
I(P, 2, 'Colar valores',
  'Colar apenas os valores de uma célula que contém =A1*2 cola no destino a fórmula =A1*2, ajustada à nova posição.', 'E',
  '**Colar Valores** leva só o **resultado** (o número), sem a fórmula; é como "congelar" o cálculo.',
  peg='Confundir colar valores com colar fórmulas.',
  kw=['Colar Valores', 'resultado'])
I(P, 2, 'Área de transferência do Office',
  'O painel da Área de Transferência do Office, aberto na guia Página Inicial, guarda vários itens copiados para colar depois.', 'C',
  'A **Área de Transferência** do Office (iniciador do grupo, na Página Inicial) guarda até **24 itens** copiados, compartilhados entre os aplicativos do Office.',
  kw=['Área de Transferência', '24 itens'])
I(P, 2, 'Selecionar tudo',
  'O botão Selecionar Tudo, no canto superior esquerdo da planilha, na interseção dos cabeçalhos de linha e de coluna, seleciona todas as células da planilha.', 'C',
  'O botão **Selecionar Tudo** (o triângulo entre a coluna A e a linha 1) seleciona a **planilha inteira**. O atalho de teclado varia com o idioma da instalação (a página oficial segue o teclado dos EUA), por isso a banca costuma perguntar pelo botão.',
  kw=['Selecionar Tudo', 'planilha inteira'])

# ======================= INF-2.2.5 · Classificação de dados =======================
P = 'DBA26-INF-2.2.5'
I(P, 1, 'Onde classificar',
  'A classificação de dados fica na guia Dados (Classificar e Filtrar) e também no botão Classificar e Filtrar da guia Página Inicial.', 'C',
  '**Dados > Classificar** (ou A→Z / Z→A) e **Página Inicial > Classificar e Filtrar**. A caixa **Classificar** permite vários **níveis** (ex.: por cidade e, dentro dela, por nome).',
  kw=['Classificar', 'níveis'])
I(P, 1, 'Classificar uma só coluna',
  'Ao classificar uma única coluna de uma tabela de dados, o Excel sempre reordena automaticamente as demais colunas, sem consultar o usuário.', 'E',
  'Se só uma coluna está selecionada e há dados ao lado, o Excel **avisa** e pergunta: **Expandir a seleção** ou **Continuar com a seleção atual**. Escolher a segunda **desalinha** os registros.',
  peg='Omitir o aviso de expandir a seleção.',
  kw=['Expandir a seleção', 'desalinha'])
I(P, 1, 'Células vazias na classificação',
  'Na classificação, crescente ou decrescente, as células em branco ficam sempre por último.', 'C',
  'Na ordem **crescente**: números, depois texto, depois valores lógicos, depois erros; e as **células em branco sempre por último** (também na decrescente).',
  kw=['células em branco', 'crescente'])
I(P, 1, 'Filtro × classificação',
  'Aplicar um filtro exclui da planilha as linhas que não atendem ao critério.', 'E',
  'O **Filtro** **oculta** temporariamente as linhas que não atendem ao critério; ao limpar o filtro, elas voltam. A **classificação**, por sua vez, reordena as linhas.',
  peg='Dizer que o filtro exclui linhas.',
  kw=['Filtro', 'oculta'])
I(P, 1, 'Cabeçalho na classificação',
  'Na caixa Classificar, a opção "Meus dados contêm cabeçalhos" impede que a primeira linha, com os títulos das colunas, seja ordenada junto com os dados.', 'C',
  'Marcada a opção **Meus dados contêm cabeçalhos**, a 1ª linha fica fixa e seus títulos aparecem como nomes de coluna nos níveis da classificação.',
  kw=['Meus dados contêm cabeçalhos', 'cabeçalho'])

# --- INF-2.2.5 · Rodada 2
I(P, 2, 'Classificação personalizada',
  'O Excel só ordena em ordem alfabética ou numérica, não sendo possível classificar pela cor da célula nem por lista personalizada.', 'E',
  'A caixa **Classificar** aceita **cor da célula**, **cor da fonte**, **ícone** de formatação condicional e **lista personalizada** (ex.: jan, fev, mar... ou baixa, média, alta).',
  peg='Limitar a classificação a A–Z e números.',
  kw=['lista personalizada', 'cor da célula'])
I(P, 2, 'Da esquerda para a direita',
  'Nas Opções da caixa Classificar, pode-se ordenar da esquerda para a direita, isto é, reordenar colunas com base nos valores de uma linha.', 'C',
  'Em **Opções**: **Orientação** de cima para baixo (padrão, por linhas) ou **da esquerda para a direita** (por colunas); e a opção de diferenciar maiúsculas de minúsculas.',
  kw=['da esquerda para a direita', 'Opções'])
I(P, 2, 'Funções de classificação dinâmica',
  'No Microsoft 365, a função CLASSIFICAR devolve uma cópia ordenada de um intervalo, que se atualiza quando os dados de origem mudam.', 'C',
  '**CLASSIFICAR** (e FILTRO, ÚNICO) são funções de **matriz dinâmica** do Microsoft 365/2021: o resultado "derrama" nas células vizinhas e acompanha a origem, sem mexer nela.' + FXF,
  kw=['CLASSIFICAR', 'matriz dinâmica'])

# ======================= INF-2.2.6 · Gráficos =======================
P = 'DBA26-INF-2.2.6'
I(P, 1, 'Gráfico com F11',
  'No Excel, com os dados selecionados, a tecla F11 cria um gráfico em uma folha de gráfico separada.', 'C',
  '**F11** cria o gráfico padrão numa **folha de gráfico** própria; **Alt + F1** cria-o incorporado na própria planilha.' + FX,
  kw=['F11', 'folha de gráfico'])
I(P, 1, 'Pizza',
  'O gráfico de pizza é o mais indicado para comparar a evolução de várias séries de dados ao longo de vários anos.', 'E',
  'A **pizza** mostra partes de **um todo**, com **uma série** só. Evolução no tempo pede gráfico de **linhas** (ou colunas); várias séries, colunas agrupadas ou linhas.',
  peg='Usar pizza para série temporal.',
  kw=['pizza', 'uma série'])
I(P, 1, 'Atualização automática',
  'O gráfico do Excel fica vinculado aos dados de origem e se atualiza automaticamente quando eles são alterados.', 'C',
  'Alterou-se a célula, muda o **gráfico** — ele é **vinculado** ao intervalo de origem.',
  kw=['vinculado', 'dados de origem'])
I(P, 1, 'Dispersão',
  'O gráfico de dispersão (XY) é o indicado para mostrar partes de um todo em porcentagem.', 'E',
  'A **dispersão (XY)** mostra a **relação entre duas variáveis** numéricas (ex.: idade × renda). Partes de um todo é **pizza** ou **rosca**.',
  peg='Trocar dispersão por pizza.',
  kw=['dispersão', 'duas variáveis'])
I(P, 1, 'Minigráficos',
  'Minigráficos são pequenos gráficos exibidos dentro de uma única célula, para mostrar a tendência de uma linha de dados.', 'C',
  '**Minigráficos** (Inserir > Minigráficos: Linha, Coluna, Ganhos/Perdas) cabem **numa célula**, ao lado dos dados.',
  kw=['Minigráficos', 'célula'])

# --- INF-2.2.6 · Rodada 2
I(P, 2, 'Gráficos Recomendados',
  'O comando Gráficos Recomendados, na guia Inserir, sugere tipos de gráfico adequados aos dados selecionados.', 'C',
  '**Inserir > Gráficos Recomendados** analisa a seleção e propõe tipos. Depois de criado, surgem as guias contextuais **Design do Gráfico** e **Formatar**.',
  kw=['Gráficos Recomendados', 'Design do Gráfico'])
I(P, 2, 'Barras × colunas',
  'No Excel, gráfico de barras e gráfico de colunas são nomes do mesmo tipo, com retângulos verticais.', 'E',
  'São tipos diferentes: **colunas** = retângulos **verticais**; **barras** = **horizontais** (bons para rótulos longos).',
  peg='Igualar barras e colunas.',
  kw=['barras', 'colunas'])
I(P, 2, 'Alternar linha/coluna',
  'O comando Alternar Linha/Coluna do gráfico transpõe os dados na própria planilha de origem, trocando linhas por colunas nas células.', 'E',
  '**Design do Gráfico > Alternar Linha/Coluna** muda só o **gráfico**: as séries passam a categorias e vice-versa; a planilha fica **intacta**. Transpor células é o **Colar Especial > Transpor**.',
  peg='Achar que o comando mexe nas células.',
  kw=['Alternar Linha/Coluna', 'séries'])
