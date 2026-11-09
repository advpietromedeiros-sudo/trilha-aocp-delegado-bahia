# Pente Fino de Informática — INF-1 (Windows 11), INF-1.1, INF-1.2, INF-1.3 e INF-1.4 (08/11/2026).
# Redação própria. Versão de referência: Windows 11 em português, configuração padrão; divergência com o Windows 10 é dita.
from base import I
from inf_fontes import FW

# ======================= INF-1 · Sistema Operacional Windows 11 =======================
P = 'DBA26-INF-1'
I(P, 1, 'Função do sistema operacional',
  'O sistema operacional é o software básico que gerencia os recursos do hardware (processador, memória, armazenamento e periféricos) e oferece a interface entre o usuário, os aplicativos e a máquina.', 'C',
  'É a definição clássica: o **sistema operacional** é **software básico**, gerente de recursos e intermediário entre usuário, programas e hardware. Editores de texto e navegadores são **aplicativos**, que rodam sobre ele.',
  kw=['sistema operacional', 'software básico'])
I(P, 1, 'Licença do Windows',
  'O Windows 11 é um sistema operacional de código aberto, distribuído sob licença livre, o que permite a qualquer usuário alterar e redistribuir seu código-fonte.', 'E',
  'O Windows é **software proprietário** da Microsoft, distribuído sob licença de uso; o código-fonte não é aberto. Sistemas de **código aberto** são, por exemplo, as distribuições **Linux**.',
  peg='Atribuir ao Windows a licença livre do Linux.',
  kw=['software proprietário', 'código aberto'])
I(P, 1, 'Multitarefa',
  'O Windows 11 é sistema operacional monotarefa: para abrir um segundo programa, o primeiro precisa ser encerrado.', 'E',
  'O Windows é **multitarefa** (preemptivo): vários processos convivem, e o sistema distribui o tempo de processador. Também é **multiusuário**, com contas separadas no mesmo computador.',
  peg='Chamar de monotarefa um sistema multitarefa.',
  kw=['multitarefa', 'multiusuário'])
I(P, 1, 'Sistema de arquivos padrão',
  'O sistema de arquivos padrão da unidade em que o Windows 11 é instalado é o FAT32, que admite arquivos de qualquer tamanho.', 'E',
  'A unidade do sistema usa **NTFS**, com permissões, criptografia e arquivos muito grandes. O **FAT32** limita cada arquivo a **4 GB** e ainda aparece em pen drives, por compatibilidade.',
  peg='Trocar NTFS por FAT32 e ignorar o limite de 4 GB.',
  kw=['NTFS', 'FAT32'])
I(P, 1, 'Requisitos do Windows 11',
  'Entre os requisitos mínimos do Windows 11 estão o firmware UEFI com Inicialização Segura e o módulo TPM 2.0.', 'C',
  'A Microsoft exige, para o Windows 11, **UEFI com Inicialização Segura** e **TPM 2.0** (chip de segurança que guarda chaves criptográficas), além de processador compatível; por isso parte dos computadores do Windows 10 não atualiza.',
  kw=['TPM 2.0', 'Inicialização Segura'])

# --- INF-1 · Rodada 2
I(P, 2, 'Conta Microsoft × conta local',
  'No Windows 11, só é possível usar o computador com uma conta Microsoft; contas locais deixaram de existir em todas as edições.', 'E',
  'O Windows 11 incentiva (e, na instalação doméstica, quase impõe) a **conta Microsoft**, que sincroniza configurações e OneDrive; mas a **conta local** continua existindo, por exemplo criada depois em Configurações > Contas. A instalação inicial varia por edição e versão.',
  peg='Transformar a preferência da instalação em proibição da conta local.',
  kw=['conta Microsoft', 'conta local'])
I(P, 2, 'Kernel',
  'O núcleo (kernel) é a parte do sistema operacional que roda com privilégio máximo e controla diretamente processos, memória e acesso ao hardware.', 'C',
  'O **kernel** é o núcleo do sistema, em modo privilegiado; os **drivers** são os módulos que permitem ao sistema conversar com cada dispositivo.',
  kw=['kernel', 'drivers'])
I(P, 2, 'Memória virtual',
  'Quando a memória RAM se esgota, o Windows deixa de abrir programas, pois não dispõe de mecanismo para usar o disco como extensão da memória.', 'E',
  'O Windows usa **memória virtual**: o **arquivo de paginação** (pagefile.sys) no disco serve de extensão da RAM. Funciona, mas é bem mais lento — daí a lentidão quando a RAM está no limite.',
  peg='Negar a existência da memória virtual.',
  kw=['memória virtual', 'arquivo de paginação'])

# ======================= INF-1.1 · Janelas, menus, barra de tarefas e área de trabalho =======================
P = 'DBA26-INF-1.1'
I(P, 1, 'Mostrar a área de trabalho',
  'No Windows 11, o atalho tecla do logotipo do Windows + D mostra e oculta a área de trabalho.', 'C',
  '**Windows + D** alterna entre mostrar a **área de trabalho** e restaurar as janelas; **Windows + M** minimiza todas as janelas.' + FW,
  kw=['Windows + D', 'área de trabalho'])
I(P, 1, 'Alternar janelas',
  'O atalho Alt + F4 alterna entre as janelas abertas, enquanto Alt + Tab fecha a janela ativa.', 'E',
  'Está invertido: **Alt + Tab** alterna entre as janelas abertas; **Alt + F4** fecha a janela ativa (e, sem janela aberta, oferece desligar).' + FW,
  peg='Inverter Alt + Tab e Alt + F4.',
  kw=['Alt + Tab', 'Alt + F4'])
I(P, 1, 'Visão de tarefas e áreas de trabalho virtuais',
  'O atalho Windows + Tab abre a Visão de Tarefas, na qual se podem ver as janelas abertas e criar áreas de trabalho virtuais; Windows + Ctrl + D cria nova área de trabalho virtual diretamente.', 'C',
  '**Windows + Tab** abre a **Visão de Tarefas**; **Windows + Ctrl + D** cria outra **área de trabalho virtual**, útil para separar grupos de janelas.' + FW,
  kw=['Visão de Tarefas', 'área de trabalho virtual'])
I(P, 1, 'Bloquear o computador',
  'O atalho Windows + L encerra a sessão do usuário e fecha todos os programas abertos, sem salvar o trabalho.', 'E',
  '**Windows + L** apenas **bloqueia** o computador: a sessão continua, com os programas abertos, e volta-se a ela com a senha ou o PIN. Encerrar a sessão (sair) é outra opção do menu Iniciar.' + FW,
  peg='Confundir bloquear com sair ou desligar.',
  kw=['Windows + L', 'bloquear'])
I(P, 1, 'Barra de tarefas centralizada',
  'No Windows 11, o botão Iniciar e os ícones da barra de tarefas vêm alinhados à esquerda por padrão, como no Windows 10, e não podem ser centralizados.', 'E',
  'É novidade visual do Windows 11: os ícones vêm **centralizados** por padrão; em Configurações > Personalização > Barra de tarefas > Comportamentos da barra de tarefas, o **alinhamento** pode passar para a **esquerda**, como no Windows 10.',
  peg='Atribuir ao Windows 11 o alinhamento padrão do Windows 10.',
  kw=['centralizados', 'alinhamento'])
I(P, 1, 'Encaixar janelas',
  'Com uma janela ativa, Windows + seta para a esquerda maximiza a janela e Windows + seta para cima encaixa-a na metade esquerda da tela.', 'E',
  'É o contrário: **Windows + seta para a esquerda** encaixa a janela na **metade esquerda**; **Windows + seta para cima** **maximiza**; Windows + seta para baixo minimiza/restaura.' + FW,
  peg='Trocar o efeito das setas no encaixe (Snap).',
  kw=['Windows + seta', 'encaixar'])

# --- INF-1.1 · Rodada 2
I(P, 2, 'Menu Link Rápido',
  'O atalho Windows + X abre a Visão de Tarefas, com as janelas abertas e as áreas de trabalho virtuais.', 'E',
  '**Windows + X** (ou o clique com o botão direito no botão Iniciar) abre o **menu Link Rápido** (Gerenciador de Dispositivos, Gerenciamento de Disco, Gerenciador de Tarefas, Terminal...). A Visão de Tarefas é **Windows + Tab**.' + FW,
  peg='Trocar Windows + X por Windows + Tab.',
  kw=['Windows + X', 'Link Rápido'])
I(P, 2, 'Gerenciador de Tarefas',
  'O atalho Ctrl + Shift + Esc abre a caixa de diálogo Executar, na qual se digita o nome do programa a iniciar.', 'E',
  '**Ctrl + Shift + Esc** abre direto o **Gerenciador de Tarefas** (processos, desempenho, inicialização). A caixa **Executar** abre com **Windows + R**.' + FW,
  peg='Trocar Gerenciador de Tarefas por Executar.',
  kw=['Ctrl + Shift + Esc', 'Windows + R'])
I(P, 2, 'Histórico da área de transferência',
  'O atalho Windows + V abre o histórico da área de transferência, que permite colar itens copiados anteriormente, e não apenas o último.', 'C',
  '**Windows + V** abre o **histórico da área de transferência** (na primeira vez, o Windows pede para ativá-lo). Ctrl + V cola só o último item copiado.' + FW,
  kw=['Windows + V', 'histórico da área de transferência'])
I(P, 2, 'Captura de tela',
  'No Windows 11, o atalho Windows + Shift + S salva automaticamente a tela inteira como arquivo na pasta Documentos, sem permitir a escolha de uma região.', 'E',
  '**Windows + Shift + S** abre a **Ferramenta de Captura** para selecionar uma **região** da tela e copiá-la para a área de transferência; a imagem pode depois ser anotada e salva.' + FW,
  peg='Atribuir ao atalho o salvamento automático da tela inteira.',
  kw=['Windows + Shift + S', 'Ferramenta de Captura'])

# ======================= INF-1.2 · Pastas e arquivos =======================
P = 'DBA26-INF-1.2'
I(P, 1, 'Excluir em pen drive',
  'No Windows, em configuração padrão, o arquivo excluído com a tecla Delete de um pen drive vai para a Lixeira, de onde pode ser restaurado.', 'E',
  'Arquivos apagados de **unidades removíveis** (pen drive, cartão) e de **pastas de rede** **não vão para a Lixeira**: são excluídos definitivamente. A Lixeira guarda o que se apaga das unidades internas.',
  peg='Supor que tudo o que se apaga passa pela Lixeira.',
  kw=['unidades removíveis', 'Lixeira'])
I(P, 1, 'Excluir permanentemente',
  'O atalho Shift + Delete exclui o item selecionado permanentemente, sem movê-lo para a Lixeira.', 'C',
  '**Shift + Delete** apaga **sem passar pela Lixeira** (o Windows pede confirmação). Delete ou Ctrl + D, sozinhos, mandam o item para a Lixeira.' + FW,
  kw=['Shift + Delete', 'permanentemente'])
I(P, 1, 'Arrastar na mesma unidade',
  'Ao arrastar um arquivo com o mouse de uma pasta para outra da mesma unidade, sem pressionar tecla alguma, o Windows cria uma cópia do arquivo no destino.', 'E',
  'Arrastar sem tecla: na **mesma unidade**, o Windows **move**; para **outra unidade**, **copia**. Com **Ctrl**, copia sempre; com **Shift**, move sempre; com **Alt**, cria **atalho**.',
  peg='Trocar mover por copiar no arraste dentro da mesma unidade.',
  kw=['mesma unidade', 'move'])
I(P, 1, 'Caracteres proibidos no nome',
  'Nomes de arquivos e pastas no Windows não podem conter os caracteres \\ / : * ? " < > |.', 'C',
  'São os **nove caracteres reservados** do Windows: barra invertida, barra, dois-pontos, asterisco, interrogação, aspas, menor, maior e barra vertical. Espaço, hífen, acento e ponto são permitidos.',
  kw=['caracteres reservados', 'nome de arquivo'])
I(P, 1, 'Seleção de itens não adjacentes',
  'Para selecionar, no Explorador de Arquivos, apenas os arquivos 2, 5 e 8 de uma lista, basta clicar no arquivo 2 e, mantendo a tecla Shift pressionada, clicar nos arquivos 5 e 8.', 'E',
  '**Shift + clique** seleciona um **intervalo contínuo** (de 2 a 8, todos). Para itens **não adjacentes**, usa-se **Ctrl + clique** em cada um.',
  peg='Trocar Ctrl (itens avulsos) por Shift (intervalo).',
  kw=['Ctrl + clique', 'Shift + clique'])
I(P, 1, 'Renomear',
  'No Explorador de Arquivos, a tecla F5 permite renomear o arquivo ou a pasta selecionada.', 'E',
  '**F2** renomeia o item selecionado (**F5** atualiza a janela); ao renomear, alterar a **extensão** pode tornar o arquivo ilegível pelo programa associado (o Windows avisa).' + FW,
  peg='Trocar F2 por F5.',
  kw=['F2', 'renomear'])

# --- INF-1.2 · Rodada 2
I(P, 2, 'Criar atalho arrastando',
  'Ao arrastar um arquivo mantendo pressionada a tecla Alt, o Windows cria no destino um atalho para o arquivo, e não uma cópia.', 'C',
  'Com **Alt** (ou **Ctrl + Shift**) no arraste, o Windows cria **atalho**. O atalho é um pequeno arquivo que aponta para o original: apagá-lo não apaga o arquivo.',
  kw=['atalho', 'Alt'])
I(P, 2, 'Excluir atalho',
  'Excluir o atalho de um programa da área de trabalho desinstala o programa do computador.', 'E',
  'O **atalho** só aponta para o executável: apagá-lo **não desinstala** nada. A desinstalação se faz em Configurações > Aplicativos > Aplicativos instalados (ou no Painel de Controle).',
  peg='Confundir atalho com o programa.',
  kw=['atalho', 'desinstalar'])
I(P, 2, 'Pesquisa por arquivos',
  'No Windows 11, a pesquisa da barra de tarefas e a caixa de pesquisa do Explorador de Arquivos localizam arquivos pelo nome e, nos locais indexados, também pelo conteúdo.', 'C',
  'O Windows mantém um **índice** de pesquisa: nos locais indexados (por padrão, a pasta do usuário), a busca encontra arquivos pelo **nome** e pelo **conteúdo**; fora deles, a busca é mais lenta.',
  kw=['índice', 'pesquisa'])
I(P, 2, 'Capacidade da Lixeira',
  'A Lixeira do Windows tem capacidade ilimitada: qualquer arquivo excluído de uma unidade interna, de qualquer tamanho, sempre pode ser restaurado.', 'E',
  'A **Lixeira** tem **tamanho máximo** configurável por unidade (Propriedades da Lixeira). Arquivo maior que o espaço reservado é **excluído permanentemente**, com aviso; quando enche, os itens mais antigos saem primeiro.',
  peg='Atribuir capacidade ilimitada à Lixeira.',
  kw=['tamanho máximo', 'Lixeira'])

# ======================= INF-1.3 · Configurações básicas =======================
P = 'DBA26-INF-1.3'
I(P, 1, 'Resolução da tela',
  'No Windows 11, a resolução da tela é ajustada em Configurações > Sistema > Tela, e a resolução marcada como recomendada costuma ser a nativa do monitor.', 'C',
  'Em **Configurações > Sistema > Tela** ficam **resolução**, **escala** (tamanho de texto e itens) e orientação. A **recomendada** é, em regra, a **nativa** do monitor, a de imagem mais nítida.',
  kw=['resolução', 'Sistema > Tela'])
I(P, 1, 'Abrir as Configurações',
  'O atalho Windows + I abre o Explorador de Arquivos.', 'E',
  '**Windows + I** abre as **Configurações**; o **Explorador de Arquivos** abre com **Windows + E**.' + FW,
  peg='Trocar Windows + I por Windows + E.',
  kw=['Windows + I', 'Configurações'])
I(P, 1, 'Plano de fundo e cores',
  'No Windows 11, plano de fundo, cores (inclusive os modos claro e escuro), temas e tela de bloqueio ficam reunidos em Configurações > Sistema > Sobre.', 'E',
  '**Sistema > Sobre** mostra as especificações do dispositivo e do Windows. **Personalização** concentra **plano de fundo**, **cores** (modo claro/escuro e cor de destaque), **temas**, **tela de bloqueio**, Iniciar e barra de tarefas.',
  peg='Situar a personalização em Sistema > Sobre.',
  kw=['Personalização', 'plano de fundo'])
I(P, 1, 'Proteção de tela',
  'A proteção de tela foi eliminada do Windows 11, não havendo mais como configurá-la.', 'E',
  'A **proteção de tela** continua existindo: chega-se a ela em **Personalização > Tela de bloqueio > Proteção de tela**, que abre a janela clássica de configuração (escolha da proteção e do tempo de espera).',
  peg='Dar por extinto recurso que só mudou de lugar.',
  kw=['proteção de tela', 'tela de bloqueio'])
I(P, 1, 'Impressora padrão',
  'No Windows 11, impressoras são adicionadas e gerenciadas em Configurações > Bluetooth e dispositivos > Impressoras e scanners, e todas as impressoras instaladas passam a ser padrão ao mesmo tempo.', 'E',
  'O caminho está certo, mas só **uma** impressora é a **padrão**. Com a opção "Permitir que o Windows gerencie minha impressora padrão" ligada, ela passa a ser a **última usada** naquele local.',
  peg='Admitir várias impressoras padrão simultâneas.',
  kw=['impressora padrão', 'Impressoras e scanners'])

# --- INF-1.3 · Rodada 2
I(P, 2, 'Fontes do sistema',
  'No Windows 11, as fontes instaladas podem ser vistas, instaladas e removidas em Configurações > Personalização > Fontes.', 'C',
  'Em **Personalização > Fontes** o usuário vê, instala (arrastando o arquivo da fonte) e remove **fontes**; a pasta clássica é C:\\Windows\\Fonts.',
  kw=['Fontes', 'Personalização'])
I(P, 2, 'Painel de Controle',
  'O Painel de Controle foi removido do Windows 11, e todas as configurações passaram exclusivamente para o aplicativo Configurações.', 'E',
  'O **Painel de Controle** ainda **existe** no Windows 11 (pela pesquisa, por exemplo), embora a Microsoft migre cada vez mais funções para o aplicativo **Configurações**.',
  peg='Dar por removido o Painel de Controle.',
  kw=['Painel de Controle', 'Configurações'])
I(P, 2, 'Escala × resolução',
  'Aumentar a escala da tela de 100% para 150% altera a resolução do monitor para um valor menor.', 'E',
  'A **escala** aumenta texto, ícones e janelas **mantendo a resolução**; a **resolução** é a quantidade de pixels exibidos. São ajustes distintos, ambos em Sistema > Tela.',
  peg='Igualar escala e resolução.',
  kw=['escala', 'resolução'])

# ======================= INF-1.4 · Windows Explorer (Explorador de Arquivos) =======================
P = 'DBA26-INF-1.4'
I(P, 1, 'Abrir o Explorador',
  'O Explorador de Arquivos, chamado Windows Explorer em versões antigas, é aberto pelo atalho Windows + E.', 'C',
  'O antigo **Windows Explorer** chama-se **Explorador de Arquivos** desde o Windows 8; abre com **Windows + E**.' + FW,
  kw=['Explorador de Arquivos', 'Windows + E'])
I(P, 1, 'Nova pasta',
  'No Explorador de Arquivos, o atalho Ctrl + Shift + N cria uma nova pasta no local aberto.', 'C',
  '**Ctrl + Shift + N** cria **nova pasta**; em seguida o nome fica pronto para ser digitado.' + FW,
  kw=['Ctrl + Shift + N', 'nova pasta'])
I(P, 1, 'Subir um nível',
  'No Explorador de Arquivos, Alt + seta para cima abre o painel de visualização do arquivo selecionado.', 'E',
  '**Alt + seta para cima** sobe **um nível** no caminho da pasta. O **painel de visualização** é mostrado ou ocultado com **Alt + P**.' + FW,
  peg='Trocar o efeito de Alt + seta para cima e Alt + P.',
  kw=['Alt + seta para cima', 'painel de visualização'])
I(P, 1, 'Extensões ocultas',
  'Por padrão, o Explorador de Arquivos exibe a extensão de todos os arquivos, inclusive dos tipos conhecidos.', 'E',
  'Por padrão, as **extensões** dos tipos **conhecidos** ficam **ocultas**; para vê-las: guia **Exibir > Mostrar > Extensões de nomes de arquivos**. Ocultar extensões facilita golpes como "foto.jpg.exe".',
  peg='Dizer que a extensão aparece por padrão.',
  kw=['extensões', 'Extensões de nomes de arquivos'])
I(P, 1, 'Barra de endereços',
  'No Explorador de Arquivos, Alt + D seleciona a barra de endereços, onde se pode digitar um caminho como C:\\Usuários.', 'C',
  '**Alt + D** põe o foco na **barra de endereços**; ali se digita o caminho ou se navega pelas "migalhas" (cada pasta do caminho é clicável).' + FW,
  kw=['Alt + D', 'barra de endereços'])

# --- INF-1.4 · Rodada 2
I(P, 2, 'Guias no Explorador',
  'O Explorador de Arquivos tem guias (abas) para abrir várias pastas na mesma janela desde o lançamento do Windows 10, recurso que se manteve no Windows 11.', 'E',
  'As **guias** (abas) chegaram ao Explorador só no Windows 11, com a atualização **22H2**; no Windows 10 elas não existem. Recurso de versão: a banca costuma dizer "versão atual".',
  peg='Antecipar ao Windows 10 recurso do Windows 11 22H2.',
  kw=['guias', '22H2'])
I(P, 2, 'Propriedades',
  'No Explorador de Arquivos, Alt + Enter exclui o item selecionado.', 'E',
  '**Alt + Enter** mostra as **propriedades** do item (tamanho, local, datas, atributos). Excluir é Delete (para a Lixeira) ou Shift + Delete (definitivo).' + FW,
  peg='Atribuir a Alt + Enter a exclusão.',
  kw=['Alt + Enter', 'propriedades'])
I(P, 2, 'Modos de exibição',
  'O Explorador de Arquivos oferece modos de exibição como ícones de vários tamanhos, Lista, Detalhes, Blocos e Conteúdo; no modo Detalhes, os itens podem ser classificados clicando no cabeçalho da coluna.', 'C',
  'Os **modos de exibição** ficam no botão Exibir; no modo **Detalhes**, clicar no **cabeçalho** (Nome, Data de modificação, Tipo, Tamanho) ordena a lista e um novo clique inverte a ordem.',
  kw=['modos de exibição', 'Detalhes'])
