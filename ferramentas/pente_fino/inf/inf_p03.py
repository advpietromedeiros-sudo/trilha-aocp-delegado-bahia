# Pente Fino de Informática — INF-3 (redes) e INF-3.1 a INF-3.7 (internet e intranet, nuvem, navegadores, deep e dark
# web, correio eletrônico, segurança da informação, backup) (08/11/2026).
# Redação própria. Lei só onde o tema tem base no CP (crime informático e fraude eletrônica), recortada de
# assets/lei_seca_oficial.json; o resto é conceito técnico estável, com a fonte oficial no resumo quando é atalho ou recurso.
from base import I
from inf_fontes import FW, FG, FC, FN

CP = 'CP:'

# ======================= INF-3 · Redes de Computadores =======================
P = 'DBA26-INF-3'
I(P, 1, 'LAN, MAN e WAN',
  'Quanto à abrangência geográfica, LAN é a rede local (uma casa, um prédio), MAN a rede metropolitana e WAN a rede de longa distância, da qual a internet é o maior exemplo.', 'C',
  'Classificação por alcance: **LAN** (local), **MAN** (metropolitana), **WAN** (longa distância, como a **internet**); há também a **PAN**, rede pessoal (ex.: Bluetooth).',
  kw=['LAN', 'WAN'])
I(P, 1, 'Roteador × switch',
  'O switch interliga redes diferentes e escolhe o melhor caminho para os pacotes entre elas, enquanto o roteador apenas conecta computadores da mesma rede local.', 'E',
  'Está trocado: o **switch** conecta dispositivos **da mesma rede local**, entregando cada quadro à porta certa; o **roteador** interliga **redes diferentes** (ex.: a rede da casa e a internet) e encaminha pacotes pelo endereço IP.',
  peg='Inverter switch e roteador.',
  kw=['switch', 'roteador'])
I(P, 1, 'Endereço IP',
  'O endereço IPv4 tem 32 bits, normalmente escrito em quatro números de 0 a 255 separados por pontos, e o IPv6 tem 128 bits, escrito em hexadecimal.', 'C',
  '**IPv4** = **32 bits** (ex.: 192.168.0.1), cerca de 4,3 bilhões de endereços, já esgotados; **IPv6** = **128 bits** (ex.: 2001:db8::1).',
  kw=['IPv4', 'IPv6'])
I(P, 1, 'Wi-Fi',
  'As redes Wi-Fi seguem a família de padrões IEEE 802.3, a mesma das redes cabeadas Ethernet.', 'E',
  '**Wi-Fi** = família **IEEE 802.11** (a, b, g, n, ac, ax...); **Ethernet** cabeada = **IEEE 802.3**. Para proteger o Wi-Fi, usa-se **WPA2** ou **WPA3**; o WEP é obsoleto.',
  peg='Trocar 802.11 por 802.3.',
  kw=['IEEE 802.11', 'WPA2'])
I(P, 1, 'Topologia estrela',
  'Na topologia em estrela, todos os dispositivos se ligam a um equipamento central, como um switch, e a falha de um cabo derruba apenas o dispositivo ligado a ele.', 'C',
  'Na **estrela**, o ponto crítico é o **equipamento central**; a queda de um cabo isola só aquela máquina. É a topologia física mais comum nas LANs.',
  kw=['estrela', 'equipamento central'])

# --- INF-3 · Rodada 2
I(P, 2, 'TCP × UDP',
  'O TCP é protocolo orientado a conexão, que confirma a entrega e reordena os pacotes; o UDP não estabelece conexão nem garante a entrega, sendo usado onde a rapidez importa mais, como em chamadas de voz e vídeo.', 'C',
  'Na camada de **transporte**: **TCP** = confiável (conexão, confirmação, retransmissão); **UDP** = leve, sem garantia (voz, vídeo ao vivo, DNS).',
  kw=['TCP', 'UDP'])
I(P, 2, 'DHCP',
  'O DHCP é o protocolo que traduz nomes de domínio, como www.gov.br, em endereços IP.', 'E',
  '**DHCP** **atribui** automaticamente endereço IP, máscara, gateway e DNS às máquinas da rede. Quem traduz **nomes em IP** é o **DNS**.',
  peg='Trocar DHCP por DNS.',
  kw=['DHCP', 'DNS'])
I(P, 2, 'Modelo TCP/IP',
  'No modelo TCP/IP, HTTP, SMTP e DNS são protocolos da camada de transporte, e TCP e UDP pertencem à camada de aplicação.', 'E',
  'Está invertido. Camadas do **TCP/IP**: aplicação (**HTTP, SMTP, DNS, FTP**), transporte (**TCP, UDP**), internet/rede (**IP**) e acesso à rede (Ethernet, Wi-Fi).',
  peg='Trocar aplicação por transporte.',
  kw=['camada de aplicação', 'IP'])

# ======================= INF-3.1 · Internet e intranet =======================
P = 'DBA26-INF-3.1'
I(P, 1, 'Intranet',
  'Intranet é a rede privada de uma organização que usa as mesmas tecnologias e protocolos da internet (TCP/IP, HTTP, navegador), com acesso restrito aos usuários autorizados.', 'C',
  'A **intranet** é **privada** mas usa a **tecnologia da internet**; pode ser acessada de fora por VPN. A **extranet** abre parte da intranet a **parceiros externos** (fornecedores, clientes).',
  kw=['intranet', 'extranet'])
I(P, 1, 'Intranet e TCP/IP',
  'A intranet, por ser rede privada, não pode usar o protocolo TCP/IP, exclusivo da internet.', 'E',
  'O que define a **intranet** é justamente usar **TCP/IP** e serviços web numa rede **restrita**. Ser privada diz respeito ao acesso, não ao protocolo.',
  peg='Negar o TCP/IP na intranet.',
  kw=['intranet', 'TCP/IP'])
I(P, 1, 'DNS',
  'O DNS é o serviço que traduz nomes de domínio, como www.ba.gov.br, nos endereços IP dos servidores correspondentes.', 'C',
  'O **DNS** (porta **53**) é a "lista telefônica" da internet: nome → **IP**. Envenenar esse serviço (pharming) leva o usuário a site falso mesmo digitando o endereço correto.',
  kw=['DNS', 'endereços IP'])
I(P, 1, 'HTTPS',
  'O HTTPS é o HTTP protegido por criptografia TLS e usa, por padrão, a porta 80.', 'E',
  '**HTTPS** = HTTP + **TLS** (sucessor do SSL), porta padrão **443**; o **HTTP** simples usa a **80**.',
  peg='Dar ao HTTPS a porta do HTTP.',
  kw=['HTTPS', 'porta 443'])
I(P, 1, 'URL',
  'Na URL https://www.policiacivil.ba.gov.br/servicos, "https" indica o protocolo, "www.policiacivil.ba.gov.br" o nome do domínio e "/servicos" o caminho do recurso no servidor.', 'C',
  'A **URL** tem **protocolo://domínio/caminho** (podendo vir porta, parâmetros e âncora). Em .gov.br, o domínio de primeiro nível é **.br** e o de segundo, **.gov**.',
  kw=['URL', 'domínio'])
I(P, 1, 'Pesquisa por frase exata',
  'No Google, colocar a expressão entre aspas, como "perdas de água", faz o buscador procurar exatamente aquela sequência de palavras.', 'C',
  '**Aspas** = **frase exata**; o **sinal de menos** exclui palavra (jaguar -carro); **site:** restringe a um site ou domínio (site:gov.br); **filetype:** busca tipo de arquivo (filetype:pdf).' + FG,
  kw=['aspas', 'frase exata'])
I(P, 1, 'Operador site:',
  'O operador filetype:gov.br restringe a busca do Google aos sites do governo brasileiro.', 'E',
  'Quem restringe a **domínio** é **site:** (site:gov.br). **filetype:** filtra **tipo de arquivo** (filetype:pdf).' + FG,
  peg='Trocar site: por filetype:.',
  kw=['site:', 'filetype:'])
I(P, 1, 'FTP',
  'O FTP é o protocolo para transferência de arquivos entre computadores e, na forma original, criptografa por padrão o usuário, a senha e os dados transferidos.', 'E',
  '**FTP** (portas **20/21**) transfere arquivos, mas trafega senha e dados **em claro**; as versões seguras são **SFTP** (sobre SSH) e **FTPS** (sobre TLS).',
  peg='Atribuir criptografia ao FTP original.',
  kw=['FTP', 'em claro'])

# --- INF-3.1 · Rodada 2
I(P, 2, 'Navegador e intranet',
  'O conteúdo de uma intranet só pode ser acessado por programa específico, pois o navegador comum não abre páginas internas da empresa.', 'E',
  'A intranet usa **navegador** comum e servidores web internos; o acesso é limitado pela **rede** (e por login), não pelo programa.',
  peg='Exigir programa especial para a intranet.',
  kw=['intranet', 'navegador'])
I(P, 2, 'VPN',
  'A VPN cria um túnel criptografado sobre uma rede pública, permitindo, por exemplo, que o servidor acesse de casa a intranet do órgão com segurança.', 'C',
  'A **VPN** (rede privada virtual) **encapsula e criptografa** o tráfego sobre a internet; é o modo usual de acesso remoto à intranet.',
  kw=['VPN', 'túnel criptografado'])
I(P, 2, 'Cookies',
  'Cookies são programas executáveis que os sites instalam no computador para acelerar o processador durante a navegação.', 'E',
  '**Cookies** são pequenos **arquivos de texto** gravados pelo navegador a pedido dos sites, **não** programas; guardam sessão (login), carrinho e preferências; os **de terceiros** servem a rastreamento e publicidade.',
  peg='Tratar cookie como programa.',
  kw=['cookies', 'rastreamento'])
I(P, 2, 'SSH × Telnet',
  'O Telnet é o protocolo indicado para administração remota segura, por criptografar toda a sessão, ao contrário do SSH.', 'E',
  'É o oposto: o **SSH** (porta **22**) é **criptografado**; o **Telnet** (porta 23) trafega **em claro** e está em desuso.',
  peg='Inverter SSH e Telnet.',
  kw=['SSH', 'Telnet'])
I(P, 2, 'Cache do navegador',
  'O cache do navegador armazena localmente cópias de páginas, imagens e scripts já visitados, acelerando o carregamento nas visitas seguintes.', 'C',
  'O **cache** guarda cópias locais para não baixar tudo de novo; limpar cache e cookies resolve páginas desatualizadas, ao custo de novo carregamento e novo login.',
  kw=['cache', 'cópias locais'])

# ======================= INF-3.2 · Computação em nuvem =======================
P = 'DBA26-INF-3.2'
I(P, 1, 'Características essenciais',
  'Segundo a definição do NIST, a computação em nuvem tem como características essenciais o autoatendimento sob demanda, o amplo acesso pela rede, o agrupamento de recursos, a elasticidade rápida e o serviço medido.', 'C',
  'São as **cinco características** do NIST: **autoatendimento sob demanda**, **amplo acesso à rede**, **pool de recursos**, **elasticidade rápida** e **serviço medido** (paga-se pelo uso).' + FN,
  kw=['elasticidade rápida', 'serviço medido'])
I(P, 1, 'SaaS',
  'No modelo SaaS, o cliente contrata a infraestrutura de servidores, redes e armazenamento e instala nela seus próprios sistemas operacionais e aplicações.', 'E',
  'Esse é o **IaaS** (infraestrutura como serviço). No **SaaS** (software como serviço) o cliente usa o **aplicativo pronto** pelo navegador ou app (webmail, Microsoft 365); no **PaaS** recebe a **plataforma** para desenvolver e implantar.' + FN,
  peg='Trocar SaaS por IaaS.',
  kw=['SaaS', 'IaaS', 'PaaS'])
I(P, 1, 'Modelos de implantação',
  'Segundo o NIST, os modelos de implantação da nuvem são apenas dois, pública e privada; a nuvem híbrida é termo comercial, sem lugar na definição.', 'E',
  'São **quatro**: **pública** (aberta ao público, do provedor), **privada** (de uma organização), **comunitária** (grupo com interesses comuns) e **híbrida** (combinação, com portabilidade de dados e aplicações).' + FN,
  peg='Omitir a comunitária e a híbrida.',
  kw=['pública', 'privada', 'híbrida'])
I(P, 1, 'Dependência da internet',
  'Na computação em nuvem, os dados e programas ficam sempre armazenados no disco local do usuário, e a internet é usada apenas para atualizações.', 'E',
  'Na nuvem, dados e processamento ficam nos **servidores do provedor**, acessados **pela rede**; por isso a conexão é essencial (alguns serviços mantêm cópia local sincronizada para uso offline).',
  peg='Inverter a lógica da nuvem.',
  kw=['servidores do provedor', 'pela rede'])
I(P, 1, 'Elasticidade',
  'A elasticidade permite aumentar ou reduzir os recursos contratados conforme a demanda, muitas vezes de forma automática.', 'C',
  '**Elasticidade**: os recursos crescem no pico e encolhem depois, e o **serviço medido** cobra o efetivamente usado — o contrário de comprar servidor para o pico.' + FN,
  kw=['elasticidade', 'demanda'])

# --- INF-3.2 · Rodada 2
I(P, 2, 'Responsabilidade compartilhada',
  'Ao contratar nuvem pública, toda a responsabilidade pela segurança dos dados passa ao provedor, inclusive a gestão das senhas e das permissões dos usuários do cliente.', 'E',
  'Vale a **responsabilidade compartilhada**: o provedor protege a infraestrutura; o cliente responde por **contas, senhas, permissões** e pelos dados que coloca lá — mais ainda no IaaS.',
  peg='Transferir toda a segurança ao provedor.',
  kw=['responsabilidade compartilhada', 'permissões'])
I(P, 2, 'PaaS',
  'No PaaS, o provedor fornece ambiente de desenvolvimento e execução (sistema, banco de dados, servidor de aplicação), e o cliente cuida apenas das aplicações que cria e dos seus dados.', 'C',
  '**PaaS** fica no meio: o cliente não administra servidores nem sistema operacional, mas **desenvolve e implanta** as próprias aplicações.' + FN,
  kw=['PaaS', 'aplicações'])
I(P, 2, 'Pool de recursos',
  'O agrupamento de recursos (pool) significa que cada cliente da nuvem pública recebe servidores físicos exclusivos e dedicados.', 'E',
  'No **pool de recursos**, a infraestrutura é **compartilhada** entre vários clientes (multilocatário), alocada dinamicamente; o cliente em geral nem sabe a localização exata.' + FN,
  peg='Confundir pool com servidor dedicado.',
  kw=['pool de recursos', 'multilocatário'])

# ======================= INF-3.3 · Navegadores: Edge, Chrome e Firefox =======================
P = 'DBA26-INF-3.3'
I(P, 1, 'Navegação anônima',
  'A navegação anônima do Chrome (janela anônima) e a InPrivate do Edge não gravam o histórico nem mantêm os cookies após fechar a janela, mas não escondem a navegação do provedor de internet nem do empregador.', 'C',
  'O modo **anônimo/InPrivate** só evita rastros **no próprio computador** (histórico, cookies e dados de formulário ao fechar). Sites, provedor e a rede do trabalho **ainda veem** o acesso; downloads e favoritos ficam.',
  kw=['navegação anônima', 'InPrivate'])
I(P, 1, 'Atalho da janela privada',
  'No Chrome e no Edge, Ctrl + Shift + N abre janela anônima/InPrivate; no Firefox, a janela privativa abre com Ctrl + Shift + P.', 'C',
  '**Ctrl + Shift + N** (Chrome e Edge) e **Ctrl + Shift + P** (Firefox). A banca troca os atalhos entre navegadores.',
  kw=['Ctrl + Shift + N', 'Ctrl + Shift + P'])
I(P, 1, 'Edge e o Chromium',
  'O Microsoft Edge atual usa o mesmo motor do Firefox, desenvolvido pela Mozilla.', 'E',
  'O **Edge** atual é baseado no **Chromium** (projeto aberto que também está por trás do Chrome) desde 2020; o **Firefox** usa o motor próprio **Gecko**, da Mozilla.',
  peg='Trocar Chromium por Gecko.',
  kw=['Chromium', 'Gecko'])
I(P, 1, 'Cadeado',
  'O cadeado na barra de endereços garante que o site é legítimo e confiável, afastando qualquer risco de phishing.', 'E',
  'O **cadeado** indica conexão **HTTPS criptografada** com aquele domínio — não que o site seja honesto. Sites de **phishing** também usam HTTPS: o que conta é **conferir o domínio**.',
  peg='Ler o cadeado como selo de idoneidade.',
  kw=['cadeado', 'phishing'])
I(P, 1, 'Reabrir guia fechada',
  'Nos navegadores Chrome, Edge e Firefox, Ctrl + Shift + T reabre a última guia fechada.', 'C',
  '**Ctrl + Shift + T** reabre a guia fechada; **Ctrl + T** abre nova guia; **Ctrl + W** fecha a atual; **Ctrl + H** histórico; **Ctrl + J** downloads; **Ctrl + D** favorita a página.',
  kw=['Ctrl + Shift + T', 'Ctrl + T'])
I(P, 1, 'Histórico e downloads',
  'Nos navegadores Chrome, Edge e Firefox, Ctrl + J abre o histórico de navegação, e Ctrl + H abre a lista de downloads.', 'E',
  'Está trocado: **Ctrl + H** = **histórico**; **Ctrl + J** = **downloads** (no Firefox, Ctrl + Shift + Y também abre os downloads).',
  peg='Inverter Ctrl + H e Ctrl + J.',
  kw=['Ctrl + H', 'Ctrl + J'])

# --- INF-3.3 · Rodada 2
I(P, 2, 'Modo Internet Explorer',
  'O Microsoft Edge oferece o modo Internet Explorer, para abrir sites antigos que dependem do motor do IE.', 'C',
  'O **Modo IE** do Edge mantém compatibilidade com sistemas legados (comuns em órgãos públicos), já que o Internet Explorer foi aposentado.',
  kw=['Modo IE', 'Internet Explorer'])
I(P, 2, 'Firefox e a Mozilla',
  'O Firefox é navegador proprietário da Microsoft, de código fechado.', 'E',
  'O **Firefox** é da **Mozilla**, de **código aberto**; destaca a **Proteção aprimorada contra rastreamento**, que bloqueia rastreadores e cookies de terceiros.',
  peg='Atribuir o Firefox à Microsoft.',
  kw=['Mozilla', 'código aberto'])
I(P, 2, 'Sincronização',
  'Ao entrar com a conta (Google no Chrome, Microsoft no Edge, Mozilla no Firefox), o navegador pode sincronizar favoritos, senhas, histórico e extensões entre dispositivos.', 'C',
  'A **sincronização** com a **conta** leva favoritos, senhas e histórico a outros aparelhos — conveniência que exige senha forte e verificação em duas etapas na conta.',
  kw=['sincronização', 'conta'])
I(P, 2, 'Extensões',
  'Extensões de navegador são sempre seguras, pois só podem ler a página aberta quando o usuário clica nelas.', 'E',
  'Extensões pedem **permissões** que podem incluir **ler e alterar dados de todos os sites**; extensão maliciosa rouba senhas e sessões. Instalar só das lojas oficiais e revisar permissões.',
  peg='Presumir que extensão é sempre inofensiva.',
  kw=['extensões', 'permissões'])

# ======================= INF-3.4 · Deep Web e Dark Web =======================
P = 'DBA26-INF-3.4'
I(P, 1, 'Deep web',
  'Deep web é a parte da web não indexada pelos buscadores comuns, como áreas que exigem login, bancos de dados, webmail e intranets.', 'C',
  'A **deep web** é tudo o que os **buscadores não indexam** (contas, sistemas internos, conteúdo dinâmico) — a **maior parte** da web e, em si, nada tem de ilícito. A parte indexada é a **surface web**.',
  kw=['deep web', 'não indexada'])
I(P, 1, 'Dark web × deep web',
  'Deep web e dark web são sinônimos: ambas designam o conjunto de sites ilegais da internet.', 'E',
  'A **dark web** é um **subconjunto** da deep web, formado por redes sobrepostas (**darknets**) que exigem **software específico** (Tor, I2P) e escondem a identidade de usuários e servidores. Nem a deep nem a dark web são, por definição, ilegais.',
  peg='Igualar deep e dark web.',
  kw=['dark web', 'darknets'])
I(P, 1, 'Tor',
  'O Tor faz o tráfego passar por vários nós (relays), com camadas sucessivas de criptografia — o roteamento em cebola —, e os serviços ocultos usam endereços terminados em .onion.', 'C',
  'No **roteamento em cebola**, cada nó só conhece o anterior e o seguinte; o de **saída** vê o destino, mas não a origem. Os **serviços ocultos** ficam em endereços **.onion**.',
  kw=['roteamento em cebola', '.onion'])
I(P, 1, 'Acesso à dark web',
  'Os sites da dark web são acessados normalmente por qualquer navegador comum, sem nenhum software adicional, digitando o endereço .onion.', 'E',
  'Endereço **.onion** só resolve dentro da rede **Tor**, pelo **Tor Browser** (ou software equivalente); navegador comum não o abre.',
  peg='Dispensar o software específico.',
  kw=['Tor Browser', '.onion'])
I(P, 1, 'Crime na dark web',
  'A invasão de dispositivo informático alheio para obter dados sem autorização é crime previsto no Código Penal, ainda que organizada ou praticada por meio da dark web.', 'C',
  'O meio não afasta o crime: a **invasão de dispositivo informático** está no **art. 154-A** do CP (Lei 12.737/2012, com penas da Lei 14.155/2021), e a anonimização só dificulta a investigação.',
  lei=[(CP + '154-A', 'Invadir dispositivo informático de uso alheio, conectado ou não à rede de computadores, com o fim de obter, adulterar ou destruir dados ou informações sem autorização expressa ou tácita do usuário do dispositivo', None, 'CP, art. 154-A, caput')],
  kw=['invasão de dispositivo informático', 'art. 154-A'])

# --- INF-3.4 · Rodada 2
I(P, 2, 'Anonimato absoluto',
  'O uso do Tor garante anonimato absoluto, pois é tecnicamente impossível identificar quem acessa serviços .onion.', 'E',
  'O Tor **dificulta**, mas não garante anonimato absoluto: erros do usuário (login com conta pessoal, arquivos baixados, metadados), falhas de software e correlação de tráfego já permitiram identificações em investigações.',
  peg='Tratar o anonimato como absoluto.',
  kw=['anonimato', 'correlação de tráfego'])
I(P, 2, 'Surface web',
  'A surface web, indexada pelos buscadores, corresponde à menor parcela do conteúdo da web.', 'C',
  'A **surface web** é a ponta do iceberg; a **deep web** (conteúdo não indexado) é muito maior. Os números exatos variam conforme o estudo — a banca pede só a proporção.',
  kw=['surface web', 'menor parcela'])
I(P, 2, 'Venda de programa de invasão',
  'Quem vende ou difunde programa de computador destinado a permitir a invasão de dispositivo informático alheio só responde se ele mesmo realizar a invasão.', 'E',
  'O **§ 1º do art. 154-A** pune com a mesma pena quem **produz, oferece, distribui, vende ou difunde** dispositivo ou programa com o intuito de permitir a invasão — mercado comum em fóruns da dark web.',
  lei=[(CP + '154-A', '§ 1o Na mesma pena incorre quem produz, oferece, distribui, vende ou difunde dispositivo ou programa de computador com o intuito de permitir a prática da conduta definida no caput.', None, 'CP, art. 154-A, § 1º')],
  peg='Exigir a invasão de quem só fornece a ferramenta.',
  kw=['art. 154-A', '§ 1º'])

# ======================= INF-3.5 · Correio eletrônico =======================
P = 'DBA26-INF-3.5'
I(P, 1, 'Endereço de e-mail',
  'No endereço delegado@pc.ba.gov.br, "delegado" identifica a caixa postal do usuário e "pc.ba.gov.br" o domínio do servidor de correio, separados pela arroba.', 'C',
  'Formato **usuário@domínio**: à esquerda da **@**, a caixa postal; à direita, o **domínio** que recebe as mensagens. Não pode haver espaço no endereço.',
  kw=['usuário@domínio', 'arroba'])
I(P, 1, 'Cco',
  'Os destinatários colocados no campo Cco (com cópia oculta) são vistos por todos os demais destinatários da mensagem.', 'E',
  'Em **Cco** ninguém vê quem está ali; em **Cc** e **Para**, todos se veem. Cco protege endereços em envios em massa; e **Responder a todos** não alcança quem estava em Cco.',
  peg='Inverter Cc e Cco.',
  kw=['Cco', 'cópia oculta'])
I(P, 1, 'SMTP, POP3 e IMAP',
  'O SMTP é o protocolo de envio de mensagens, enquanto POP3 e IMAP são protocolos de acesso às mensagens recebidas.', 'C',
  '**SMTP** = **envio** (porta 25 entre servidores; 587 na submissão pelo cliente); **POP3** (110) e **IMAP** (143) = **recebimento/leitura**.',
  kw=['SMTP', 'POP3', 'IMAP'])
I(P, 1, 'IMAP × POP3',
  'O IMAP, por padrão, baixa as mensagens para o computador e as apaga do servidor, ao passo que o POP3 mantém as mensagens sincronizadas no servidor entre vários dispositivos.', 'E',
  'Está trocado: o **IMAP** mantém as mensagens **no servidor**, sincronizadas entre celular, notebook e webmail; o **POP3** foi feito para **baixar** e, em regra, retirar do servidor (o cliente pode ser configurado para deixar cópia).',
  peg='Inverter IMAP e POP3.',
  kw=['IMAP', 'POP3'])
I(P, 1, 'Responder × encaminhar',
  'Ao encaminhar uma mensagem, os anexos originais vão junto; ao responder, em regra, os anexos originais não são reenviados.', 'C',
  '**Encaminhar** reenvia a mensagem **com os anexos** a terceiro; **Responder** e **Responder a todos** devolvem o texto citado, em regra **sem** os anexos.',
  kw=['encaminhar', 'anexos'])
I(P, 1, 'Webmail',
  'Para usar webmail é obrigatório instalar um cliente de e-mail, como o Outlook ou o Thunderbird.', 'E',
  'O **webmail** funciona no **navegador** (Gmail, Outlook.com, correio institucional); os **clientes de e-mail** (Outlook, Thunderbird) são a alternativa instalada, que fala SMTP/IMAP/POP3 com o servidor.',
  peg='Exigir cliente instalado para webmail.',
  kw=['webmail', 'cliente de e-mail'])

# --- INF-3.5 · Rodada 2
I(P, 2, 'Remetente falsificado',
  'O campo "De" de um e-mail pode ser falsificado (spoofing), razão pela qual o nome do remetente, sozinho, não prova a origem da mensagem.', 'C',
  'O **spoofing** forja o remetente; os mecanismos **SPF, DKIM e DMARC** ajudam os servidores a detectar a fraude. Para a prova da origem, valem os **cabeçalhos completos** da mensagem.',
  kw=['spoofing', 'cabeçalhos'])
I(P, 2, 'Fraude eletrônica por e-mail',
  'A fraude cometida com informações fornecidas pela vítima induzida a erro por e-mail fraudulento é estelionato simples, sem pena própria no Código Penal.', 'E',
  'É a **fraude eletrônica** do **art. 171, § 2º-A**, do CP: **reclusão de 4 a 8 anos** e multa, quando a vítima é induzida a erro por redes sociais, telefone, **correio eletrônico fraudulento** e meios análogos.',
  lei=[(CP + '171', '§ 2º-A. A pena é de reclusão, de 4 (quatro) a 8 (oito) anos, e multa, se a fraude é cometida com a utilização de informações fornecidas pela vítima ou por terceiro induzido a erro por meio de redes sociais, contatos telefônicos, envio de correio eletrônico fraudulento', None, 'CP, art. 171, § 2º-A')],
  peg='Ignorar a qualificadora da fraude eletrônica.',
  kw=['fraude eletrônica', '§ 2º-A'])
I(P, 2, 'Spam',
  'Spam é a mensagem eletrônica não solicitada enviada em massa; os filtros antispam podem movê-la para a pasta de lixo eletrônico.', 'C',
  '**Spam** = mensagem **não solicitada** em massa (propaganda, golpes, boatos); os filtros enviam para **Lixo Eletrônico**, e marcar como spam ensina o filtro.' + FC,
  kw=['spam', 'Lixo Eletrônico'])
I(P, 2, 'Assinatura de e-mail',
  'A assinatura configurada no cliente de e-mail (nome, cargo, telefone ao fim da mensagem) tem o mesmo valor técnico de uma assinatura digital com certificado.', 'E',
  'A "**assinatura**" do cliente de e-mail é só **texto** padronizado no rodapé. **Assinatura digital** exige **certificado** e criptografia, e garante autoria e integridade.',
  peg='Igualar rodapé de e-mail e assinatura digital.',
  kw=['assinatura', 'assinatura digital'])

# ======================= INF-3.6 · Segurança da informação =======================
P = 'DBA26-INF-3.6'
I(P, 1, 'Pilares',
  'Os princípios básicos da segurança da informação são confidencialidade, integridade e disponibilidade, aos quais se somam autenticidade e não repúdio.', 'C',
  '**Confidencialidade** (só quem pode, acessa), **integridade** (não foi alterada), **disponibilidade** (acessível quando preciso); **autenticidade** (origem confirmada) e **não repúdio** (o autor não pode negar).',
  kw=['confidencialidade', 'integridade', 'disponibilidade'])
I(P, 1, 'Vírus × worm',
  'O worm precisa ser executado pelo usuário e se anexar a outro arquivo para se propagar, ao passo que o vírus se propaga sozinho pela rede explorando vulnerabilidades.', 'E',
  'Está trocado: o **vírus** se **anexa** a arquivos/programas e depende da **execução** do hospedeiro; o **worm** é **autônomo** e se **propaga sozinho** pela rede, explorando falhas, e consome muitos recursos.' + FC,
  peg='Inverter vírus e worm.',
  kw=['vírus', 'worm'])
I(P, 1, 'Cavalo de troia',
  'O cavalo de troia se apresenta como programa útil ou inofensivo para que o próprio usuário o instale, e, por trás dessa aparência, realiza ações maliciosas sem que ele perceba.', 'C',
  'O **cavalo de troia** (trojan) se **disfarça** de programa útil (jogo, cartão virtual, "atualização") e traz a carga maliciosa junto; costuma instalar backdoor ou spyware.' + FC,
  kw=['cavalo de troia', 'disfarça'])
I(P, 1, 'Ransomware',
  'Ransomware é o código malicioso que torna os dados inacessíveis, geralmente por criptografia, e exige resgate, normalmente em criptomoeda, para devolver o acesso.', 'C',
  'O **ransomware** **sequestra** dados pela **criptografia** e cobra **resgate**; a melhor defesa é **backup** atualizado e guardado **fora** do alcance da rede, além de atualizações.' + FC,
  kw=['ransomware', 'resgate'])
I(P, 1, 'Keylogger × screenlogger',
  'O screenlogger registra as teclas digitadas pelo usuário, e o keylogger captura imagens da tela ao redor do clique do mouse.', 'E',
  'Está trocado: o **keylogger** grava **teclas** digitadas; o **screenlogger** captura a **tela** (ou a área do clique), contornando teclados virtuais. Ambos são tipos de **spyware**; o **adware** mostra propaganda.' + FC,
  peg='Inverter keylogger e screenlogger.',
  kw=['keylogger', 'screenlogger', 'spyware'])
I(P, 1, 'Rootkit',
  'Rootkit é o conjunto de programas que esconde e assegura a presença do invasor ou de outro código malicioso no computador comprometido.', 'C',
  'O **rootkit** serve para **ocultar** processos, arquivos e acessos do atacante; **backdoor** é a porta dos fundos para voltar ao sistema; **bot** é a máquina controlada remotamente, que integra uma **botnet**.' + FC,
  kw=['rootkit', 'backdoor', 'botnet'])
I(P, 1, 'Firewall × antivírus',
  'O firewall é o programa que varre os arquivos do computador e remove os vírus já instalados.', 'E',
  'O **firewall** **filtra o tráfego** de rede segundo regras (bloqueia conexões não autorizadas); quem detecta e remove malware é o **antivírus/antimalware**. Um não substitui o outro.',
  peg='Atribuir ao firewall a remoção de vírus.',
  kw=['firewall', 'antivírus'])
I(P, 1, 'Criptografia simétrica',
  'Na criptografia simétrica, usa-se a mesma chave para cifrar e decifrar, o que a torna rápida, mas exige que a chave seja compartilhada com segurança; na assimétrica, há um par de chaves, pública e privada.', 'C',
  '**Simétrica** (ex.: **AES**): **uma chave**, rápida, problema da distribuição da chave. **Assimétrica** (ex.: **RSA**): **par** de chaves; o que uma cifra, só a outra decifra.',
  kw=['criptografia simétrica', 'par de chaves'])
I(P, 1, 'Assinatura digital',
  'Na assinatura digital, o remetente assina com a chave pública do destinatário, o que garante a confidencialidade da mensagem.', 'E',
  'Assina-se com a **chave privada do remetente**; qualquer um confere com a **chave pública** dele. Garante **autenticidade, integridade e não repúdio**, **não** confidencialidade. Sigilo se obtém cifrando com a **pública do destinatário**.',
  peg='Trocar as chaves e atribuir sigilo à assinatura.',
  kw=['chave privada do remetente', 'não repúdio'])
I(P, 1, 'Invasão de dispositivo: ação penal',
  'Nos crimes de invasão de dispositivo informático, a ação penal é pública incondicionada em qualquer caso.', 'E',
  'Pelo **art. 154-B**, a regra é a ação pública **condicionada à representação**; será **incondicionada** se o crime for contra a **administração pública** direta ou indireta de qualquer dos Poderes e entes, ou contra **concessionárias de serviços públicos**.',
  lei=[(CP + '154-B', 'Nos crimes definidos no art. 154-A, somente se procede mediante representação, salvo se o crime é cometido contra a administração pública direta ou indireta de qualquer dos Poderes da União, Estados, Distrito Federal ou Municípios ou contra empresas concessionárias de serviços públicos.', None, 'CP, art. 154-B')],
  peg='Ignorar a representação do art. 154-B.',
  kw=['representação', 'art. 154-B'])

# --- INF-3.6 · Rodada 2
I(P, 2, 'Phishing × pharming',
  'No pharming, o usuário é levado a um site falso mesmo digitando o endereço correto, por causa da alteração do serviço de DNS; no phishing, a isca é uma mensagem que induz a vítima a clicar e entregar dados.', 'C',
  '**Phishing** = **isca** (e-mail, SMS, mensagem) que imita instituição para colher dados; **pharming** = **redirecionamento** por **DNS** envenenado (ou arquivo hosts alterado).' + FC,
  kw=['phishing', 'pharming', 'DNS'])
I(P, 2, 'Hash',
  'A função hash gera um resumo de tamanho fixo da mensagem e permite recuperar o texto original a partir desse resumo, desde que se conheça o algoritmo.', 'E',
  'O **hash** é **unidirecional**: não se volta ao original. Serve para verificar **integridade** (qualquer mudança altera o resumo) e é base da assinatura digital. Algoritmos atuais: **SHA-256**; o **MD5** é considerado inseguro.',
  peg='Achar que hash é reversível.',
  kw=['hash', 'unidirecional'])
I(P, 2, 'Certificado digital',
  'O certificado digital, emitido por uma Autoridade Certificadora, vincula uma chave pública a uma pessoa ou entidade; no Brasil, a cadeia oficial é a ICP-Brasil, cuja Autoridade Certificadora Raiz é o ITI.', 'C',
  'O **certificado** é o "documento de identidade" digital: traz a **chave pública**, os dados do titular, a validade e a **assinatura da AC**. Na **ICP-Brasil**, a **AC Raiz** é o **ITI**; o tipo **A1** fica no computador, o **A3** em **token ou cartão**.',
  kw=['certificado digital', 'ICP-Brasil'])
I(P, 2, 'Autenticação multifator',
  'Usar senha e, em seguida, uma segunda senha diferente constitui autenticação de dois fatores, pois envolve duas credenciais.', 'E',
  'Fatores são de **categorias diferentes**: o que se **sabe** (senha, PIN), o que se **tem** (celular, token) e o que se **é** (biometria). Duas senhas são o **mesmo fator**.' + FC,
  peg='Contar duas senhas como dois fatores.',
  kw=['autenticação multifator', 'algo que se tem'])
I(P, 2, 'Pena da invasão com prejuízo',
  'Na invasão de dispositivo informático, a pena aumenta de 1/3 a 2/3 se da invasão resulta prejuízo econômico.', 'C',
  'É o **§ 2º do art. 154-A**, na redação da Lei 14.155/2021; a pena base é de **reclusão, de 1 a 4 anos**, e multa.',
  lei=[(CP + '154-A', '§ 2º Aumenta-se a pena de 1/3 (um terço) a 2/3 (dois terços) se da invasão resulta prejuízo econômico.', None, 'CP, art. 154-A, § 2º')],
  kw=['prejuízo econômico', 'art. 154-A, § 2º'])
I(P, 2, 'Engenharia social',
  'A engenharia social explora falhas técnicas do sistema operacional, e por isso é integralmente evitada com a instalação de antivírus atualizado.', 'E',
  'A **engenharia social** explora a **confiança e o descuido das pessoas** (falso suporte técnico, falso parente pedindo PIX); antivírus não resolve — a defesa é **desconfiar e confirmar por outro canal**.' + FC,
  peg='Reduzir a engenharia social a falha técnica.',
  kw=['engenharia social', 'confirmar por outro canal'])
I(P, 2, 'Servidor no exterior',
  'Na fraude eletrônica, a pena aumenta de 1/3 a 2/3 se o crime é praticado mediante servidor mantido fora do território nacional, considerada a relevância do resultado gravoso.', 'C',
  'É o **art. 171, § 2º-B**, do CP (Lei 14.155/2021), que incide sobre a pena do § 2º-A.',
  lei=[(CP + '171', '§ 2º-B. A pena prevista no § 2º-A deste artigo, considerada a relevância do resultado gravoso, aumenta-se de 1/3 (um terço) a 2/3 (dois terços), se o crime é praticado mediante a utilização de servidor mantido fora do território nacional.', None, 'CP, art. 171, § 2º-B')],
  kw=['servidor mantido fora do território nacional', '§ 2º-B'])

# ======================= INF-3.7 · Backup e armazenamento em nuvem =======================
P = 'DBA26-INF-3.7'
I(P, 1, 'Backup incremental',
  'O backup incremental copia apenas os arquivos criados ou alterados desde o último backup, completo ou incremental.', 'C',
  '**Incremental**: só o que mudou desde o **último backup de qualquer tipo** — rápido e pequeno, mas a restauração exige o **completo + todos os incrementais** na ordem.',
  kw=['incremental', 'último backup'])
I(P, 1, 'Backup diferencial',
  'O backup diferencial copia somente o que mudou desde o último backup diferencial, e a restauração exige o completo e todos os diferenciais feitos depois dele.', 'E',
  'O **diferencial** copia tudo o que mudou desde o **último backup completo** (cresce a cada dia); para restaurar, bastam o **completo + o último diferencial**.',
  peg='Confundir diferencial com incremental.',
  kw=['diferencial', 'último backup completo'])
I(P, 1, 'Regra 3-2-1',
  'A regra 3-2-1 recomenda manter três cópias dos dados, em dois tipos de mídia diferentes, sendo uma delas fora do local principal.', 'C',
  '**3 cópias**, **2 mídias**, **1 fora do local** (outro prédio ou nuvem). Protege contra falha de disco, furto, incêndio e ransomware.',
  kw=['3-2-1', 'fora do local'])
I(P, 1, 'Sincronização não é backup',
  'A pasta sincronizada com a nuvem dispensa backup, pois se um arquivo for apagado ou criptografado por ransomware no computador, a cópia da nuvem permanece intacta.', 'E',
  'A **sincronização** **replica** a exclusão e a criptografia para a nuvem. Serviços como o OneDrive têm **lixeira** e **histórico de versões** que ajudam, por prazo limitado — mas backup de verdade guarda versões independentes.',
  peg='Igualar sincronização a backup.',
  kw=['sincronização', 'replica'])
I(P, 1, 'Testar a restauração',
  'Um procedimento de backup adequado inclui testar periodicamente a restauração das cópias, e não apenas gerá-las.', 'C',
  'Backup que nunca foi **restaurado** é aposta. Boas práticas: **testar a restauração**, guardar cópia **desconectada** (offline) e **proteger** as cópias (criptografia, acesso restrito).' + FC,
  kw=['testar a restauração', 'offline'])
I(P, 1, 'Backup completo',
  'O backup completo (total) é o mais rápido de executar e o que ocupa menos espaço, por isso é o indicado para ser feito várias vezes ao dia.', 'E',
  'O **completo** copia **tudo**: é o **mais lento** e o que **mais ocupa espaço**, mas o mais simples de restaurar. Por isso se combina com incrementais ou diferenciais entre um completo e outro.',
  peg='Inverter as vantagens do backup completo.',
  kw=['backup completo', 'mais lento'])

# --- INF-3.7 · Rodada 2
I(P, 2, 'Arquivos sob demanda',
  'No OneDrive, o recurso Arquivos Sob Demanda permite ver todos os arquivos da nuvem no Explorador sem baixá-los, ocupando espaço local só quando abertos ou marcados para ficar sempre no dispositivo.', 'C',
  'Com **Arquivos Sob Demanda**, o ícone de **nuvem** indica arquivo só online; ao abrir, ele é baixado; "Sempre manter neste dispositivo" o deixa disponível **offline**.',
  kw=['Arquivos Sob Demanda', 'offline'])
I(P, 2, 'Bit de arquivamento',
  'O backup incremental, ao final, mantém marcados os arquivos copiados como pendentes de backup, ao passo que o diferencial os desmarca.', 'E',
  'Pelo **atributo de arquivamento**: completo e **incremental** **desmarcam** os arquivos copiados; o **diferencial não desmarca** — por isso ele recopia tudo desde o último completo.',
  peg='Inverter o efeito sobre o atributo de arquivamento.',
  kw=['atributo de arquivamento', 'diferencial'])
I(P, 2, 'Histórico de Arquivos',
  'O Histórico de Arquivos do Windows faz cópias periódicas das versões dos arquivos das pastas do usuário para uma unidade externa ou de rede, permitindo restaurar versões anteriores.', 'C',
  'O **Histórico de Arquivos** (Painel de Controle) guarda **versões** de Documentos, Imagens e afins numa **unidade externa** ou de rede; difere da sincronização com a nuvem.',
  kw=['Histórico de Arquivos', 'versões'])
I(P, 2, 'Backup na mesma máquina',
  'Guardar o backup no mesmo disco dos dados originais protege a organização contra falha física desse disco.', 'E',
  'Se o **disco** falhar, vão-se dados e cópia juntos. A cópia deve ficar em **outra mídia** e, de preferência, em **outro local**.',
  peg='Achar que cópia no mesmo disco é backup suficiente.',
  kw=['outra mídia', 'mesmo disco'])
