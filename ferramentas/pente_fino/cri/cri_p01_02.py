# Pente Fino de Criminologia — pontos CRI-1, CRI-1.1, CRI-1.2, CRI-2, CRI-2.1 e CRI-2.2 (07/11/2026).
# Redação própria; doutrina na posição mais cobrada em concurso, divergências declaradas no comentário.
from base import I

CF = 'CF:'
CP = 'CP:'

# ======================= CRI-1 · Conceito, método, objeto, sistema e funções =======================
P = 'DBA26-CRI-1'
I(P, 1, 'Conceito de Criminologia',
  'Criminologia é a ciência empírica e interdisciplinar que se ocupa do crime, da pessoa do infrator, da vítima e do controle social do comportamento delitivo, buscando informação válida sobre a gênese e a dinâmica do crime, sobre sua prevenção eficaz e sobre os modelos de resposta ao delito.', 'C',
  'É o conceito consagrado por García-Pablos de Molina e o mais cobrado: **ciência empírica e interdisciplinar**, com quatro objetos (delito, delinquente, vítima e controle social) e voltada à prevenção e aos modelos de reação.',
  kw=['ciência empírica e interdisciplinar', 'controle social'])
I(P, 1, 'Ciência do ser',
  'A Criminologia é ciência normativa, que, como o Direito Penal, se ocupa do dever ser.', 'E',
  'A Criminologia é ciência do **ser** (empírica, fática): observa a realidade. O **dever ser** é próprio do Direito Penal, ciência normativa.',
  peg='Igualar Criminologia e Direito Penal quanto à natureza (ser × dever ser).',
  kw=['ciência do ser', 'dever ser'])
I(P, 1, 'Origem do termo',
  'Atribui-se a criação do termo "Criminologia" ao antropólogo francês Paul Topinard, e sua difusão à obra homônima de Raffaele Garofalo, publicada em 1885.', 'C',
  'É a versão mais repetida em concurso: **Topinard** cunhou o termo e **Garofalo** o popularizou com a obra *Criminologia* (1885). Há quem dê o mérito só a Garofalo — a banca, em regra, segue a versão acima.',
  kw=['Topinard', 'Garofalo'])
I(P, 1, 'Autonomia',
  'A Criminologia é mera ciência auxiliar do Direito Penal, a ele subordinada, sem objeto nem método próprios.', 'E',
  'A Criminologia é **ciência autônoma**, com objeto e método próprios; relaciona-se com o Direito Penal e a Política Criminal no chamado modelo integrado das ciências criminais, sem subordinação.',
  peg='Rebaixar a Criminologia a "auxiliar" do Direito Penal.',
  kw=['ciência autônoma', 'modelo integrado'])
I(P, 1, 'Método indutivo × dedutivo',
  'A Criminologia utiliza predominantemente o método empírico e indutivo, ao passo que o Direito Penal se vale do método lógico, abstrato e dedutivo.', 'C',
  'A Criminologia parte da **observação da realidade** para chegar a conclusões (**indução**); o Direito Penal parte da norma para resolver casos (**dedução**).',
  kw=['empírico e indutivo', 'dedutivo'])
I(P, 1, 'Natureza do saber criminológico',
  'Por ser ciência empírica, a Criminologia oferece leis universais e certezas absolutas sobre as causas do crime.', 'E',
  'O saber criminológico é **probabilístico, relativo e provisório**: ciência do ser não é ciência exata. Ele oferece diagnóstico e tendências, não leis universais.',
  peg='Confundir "empírico" com "exato".',
  kw=['probabilístico', 'ciência não exata'])
I(P, 1, 'Sistema: Criminologia geral e clínica',
  'A Criminologia geral aplica os conhecimentos criminológicos ao caso concreto, para diagnóstico e prognóstico do infrator, ao passo que a Criminologia clínica sistematiza, compara e classifica os resultados obtidos.', 'E',
  'Está trocado. Na divisão sistemática, a **Criminologia geral** organiza (sistematiza, compara, classifica) o conhecimento; a **Criminologia clínica** o aplica ao indivíduo (diagnóstico, prognóstico e tratamento) — muito ligada à execução penal.',
  peg='Inverter Criminologia geral e clínica.',
  kw=['Criminologia clínica', 'Criminologia geral'])

# --- CRI-1 · Rodada 2
I(P, 2, 'Crime como problema social',
  'Para a Criminologia, um fato é tratado como problema criminal quando apresenta incidência massiva na população, incidência aflitiva, persistência espaço-temporal e inequívoco consenso sobre sua etiologia e sobre as técnicas eficazes de intervenção.', 'C',
  'São os quatro requisitos do **crime como problema social e comunitário**, na formulação de García-Pablos: **incidência massiva**, **aflitiva**, **persistência espaço-temporal** e **consenso** quanto à etiologia e à intervenção.',
  kw=['incidência massiva', 'persistência espaço-temporal'])
I(P, 2, 'Marco científico',
  'Costuma-se apontar a publicação de O Homem Delinquente, de Lombroso, em 1876, como marco da fase científica da Criminologia, por introduzir o método empírico-indutivo no estudo do crime.', 'C',
  'A fase **pré-científica** (clássica, especulativa) dá lugar à **científica** com o positivismo de **Lombroso** (1876), que leva ao crime o método da observação.',
  kw=['Lombroso', 'fase científica'])
I(P, 2, 'Interdisciplinaridade × multidisciplinaridade',
  'A interdisciplinaridade da Criminologia significa a mera justaposição dos saberes da biologia, da psicologia e da sociologia, sem integração entre eles.', 'E',
  'Justaposição sem síntese é **multidisciplinaridade**. A **interdisciplinaridade** exige **integração** dos saberes num conhecimento próprio da Criminologia.',
  peg='Trocar interdisciplinar por multidisciplinar.',
  kw=['interdisciplinaridade', 'integração'])
I(P, 2, 'Enfoque moderno',
  'O moderno enfoque criminológico desloca a ênfase da prevenção do delito e da reparação do dano para o castigo exemplar do infrator, compreendendo o crime como problema individual.', 'E',
  'O movimento é o inverso: a Criminologia contemporânea passa do castigo para a **prevenção** e a **reparação**, e vê o crime como **problema comunitário**.',
  peg='Inverter a direção do deslocamento.',
  kw=['prevenção', 'reparação do dano'])
I(P, 2, 'Fase pré-científica',
  'Na fase pré-científica, o estudo do crime já se fazia pela observação sistemática de delinquentes reais, com estatísticas e exames antropométricos.', 'E',
  'A fase **pré-científica** é marcada pela especulação filosófica e jurídica (método **lógico-abstrato**); observação sistemática e medições chegam com o **positivismo**.',
  peg='Antecipar o método positivista para a fase clássica.',
  kw=['fase pré-científica', 'lógico-abstrato'])

# ======================= CRI-1.1 · Métodos: empirismo e interdisciplinaridade =======================
P = 'DBA26-CRI-1.1'
I(P, 1, 'Empirismo',
  'O método empírico significa que a Criminologia apoia suas conclusões na observação e na análise da realidade, e não em silogismos abstratos.', 'C',
  'O **empirismo** é a marca da Criminologia: conhecimento a partir da **observação** e da **experiência**, verificável e contrastável.',
  kw=['empirismo', 'observação'])
I(P, 1, 'Técnicas de pesquisa',
  'O método empírico da Criminologia afasta o uso de técnicas quantitativas, admitindo apenas técnicas qualitativas, como entrevistas e histórias de vida.', 'E',
  'A Criminologia usa **técnicas quantitativas** (estatísticas, inquéritos de vitimização, autodenúncia) e **qualitativas** (entrevista, observação participante, estudo de caso).',
  peg='Excluir uma das famílias de técnicas.',
  kw=['técnicas quantitativas', 'técnicas qualitativas'])
I(P, 1, 'Inquéritos de vitimização',
  'As pesquisas de vitimização, que perguntam a uma amostra da população se foi vítima de crimes, servem para estimar a criminalidade não registrada, a chamada cifra negra.', 'C',
  'Os **inquéritos de vitimização** comparam o que as pessoas relatam com o que foi registrado; a diferença revela a **cifra negra**.',
  kw=['pesquisas de vitimização', 'cifra negra'])
I(P, 1, 'Saberes integrados',
  'A interdisciplinaridade da Criminologia faz com que ela integre contribuições da biologia, da psicologia, da psiquiatria, da sociologia, da antropologia, da estatística e do Direito.', 'C',
  'A Criminologia é **interdisciplinar**: o crime é fenômeno biopsicossocial e precisa de vários saberes, integrados.',
  kw=['interdisciplinaridade', 'biopsicossocial'])
I(P, 1, 'Método da Escola Clássica',
  'Na Escola Clássica, o método predominante era o empírico-indutivo, baseado na observação de criminosos.', 'E',
  'A Escola Clássica usou o método **lógico-abstrato, dedutivo** (racionalismo jusnaturalista). O **empírico-indutivo** é do **positivismo**.',
  peg='Trocar os métodos entre clássicos e positivistas.',
  kw=['lógico-abstrato', 'Escola Clássica'])
I(P, 1, 'Objeto próprio',
  'A interdisciplinaridade torna a Criminologia um saber dependente de cada uma das ciências que a compõem, sem objeto próprio.', 'E',
  'Interdisciplinar não significa dependente: a Criminologia tem **objeto próprio** (delito, delinquente, vítima, controle social) e **autonomia** científica.',
  peg='Confundir interdisciplinaridade com falta de autonomia.',
  kw=['objeto próprio', 'autonomia'])

# --- CRI-1.1 · Rodada 2
I(P, 2, 'Observação participante',
  'Na observação participante, o pesquisador insere-se no grupo estudado para compreender, por dentro, seus valores e suas práticas — técnica muito usada pela Escola de Chicago.', 'C',
  'A **observação participante** é técnica **qualitativa**, marca da **Escola de Chicago** no estudo da cidade, das gangues e das comunidades.',
  kw=['observação participante', 'Escola de Chicago'])
I(P, 2, 'Estudos longitudinais',
  'Estudos transversais acompanham o mesmo grupo de indivíduos ao longo do tempo, ao passo que estudos longitudinais analisam um recorte num único momento.', 'E',
  'Está invertido: os estudos **longitudinais** (de coorte) acompanham o grupo ao longo do tempo e permitem observar carreiras criminais; os **transversais** são uma "fotografia" de um momento.',
  peg='Trocar longitudinal por transversal.',
  kw=['estudos longitudinais', 'estudos transversais'])
I(P, 2, 'Autodenúncia',
  'As pesquisas de autodenúncia (self-report) perguntam às pessoas se praticaram delitos e revelam que a criminalidade oculta se distribui apenas entre as classes sociais mais baixas.', 'E',
  'As pesquisas de **autodenúncia** revelaram justamente o contrário: a criminalidade oculta se espalha por **todas as classes sociais**, o que reforçou a tese da **seletividade** do sistema penal.',
  peg='Inverter o resultado mais célebre das pesquisas de autodenúncia.',
  kw=['autodenúncia', 'seletividade'])
I(P, 2, 'Limites da experimentação',
  'Em Criminologia, a experimentação em sentido estrito encontra limites éticos e práticos, razão pela qual predominam a observação, a estatística e os estudos de caso.', 'C',
  'Não se pode, por ética, provocar crimes para estudá-los: o **método empírico** se realiza sobretudo por **observação**, **estatística** e **estudo de caso**.',
  kw=['limites éticos', 'observação'])
I(P, 2, 'Interdisciplinaridade e Escola Clássica',
  'A interdisciplinaridade criminológica foi a marca da Escola Clássica, que já integrava biologia e sociologia ao estudo do crime.', 'E',
  'A Escola Clássica era **jurídico-filosófica**. A abertura a aportes **biológicos** e **sociológicos** começa com o **positivismo** (Lombroso, Ferri) e se consolida na Criminologia moderna.',
  peg='Atribuir à Escola Clássica o que é do positivismo.',
  kw=['interdisciplinaridade', 'positivismo'])

# ======================= CRI-1.2 · Objetos: delito, delinquente, vítima, controle social =======================
P = 'DBA26-CRI-1.2'
I(P, 1, 'Os quatro objetos',
  'São objetos da Criminologia moderna o delito, o delinquente, a vítima e o controle social.', 'C',
  'A Criminologia moderna trabalha com **quatro objetos**: **delito, delinquente, vítima e controle social**.',
  kw=['delito, delinquente, vítima e controle social', 'objetos'])
I(P, 1, 'Redescoberta da vítima',
  'A vítima sempre foi objeto central da Criminologia, desde a Escola Positiva, que a estudou ao lado do criminoso nato.', 'E',
  'O positivismo focou o **delinquente**. A vítima foi **redescoberta** depois da Segunda Guerra, com a **Vitimologia** (von Hentig, 1948; Mendelsohn).',
  peg='Antecipar a Vitimologia para o positivismo.',
  kw=['redescoberta da vítima', 'Vitimologia'])
I(P, 1, 'Ênfase de cada escola',
  'A Escola Clássica concentrou-se no delito como ente jurídico, e a Escola Positiva deslocou o foco para a pessoa do delinquente.', 'C',
  'Clássicos: **delito** (ente jurídico, livre-arbítrio). Positivistas: **delinquente** (determinismo, periculosidade).',
  kw=['delito como ente jurídico', 'delinquente'])
I(P, 1, 'Controle formal × informal',
  'A família, a escola e a igreja integram o controle social formal.', 'E',
  'Família, escola, igreja, trabalho e opinião pública são **controle social informal**. O **formal** é exercido pelas instâncias estatais: **polícia, Ministério Público, Judiciário e administração penitenciária**.',
  peg='Trocar as instâncias informais pelas formais.',
  kw=['controle social informal', 'controle social formal'])
I(P, 1, 'Controle social como objeto',
  'O controle social passou a integrar o objeto da Criminologia sobretudo a partir da Escola Clássica, no século XVIII.', 'E',
  'O controle social entra no objeto sobretudo com o **labelling approach** (paradigma da **reação social**), nos **anos 1960**, quando a Criminologia passa a estudar como as instâncias de controle definem e selecionam o crime.',
  peg='Antecipar para os clássicos o que é da reação social.',
  kw=['controle social', 'reação social'])
I(P, 1, 'O delinquente correcionalista',
  'Para a Escola Correcionalista, o delinquente é um ser débil, incapaz de dirigir livremente sua vida, que necessita da intervenção tutelar e pedagógica do Estado.', 'C',
  'Nas quatro imagens do delinquente: **clássica** (ser livre que escolhe), **positivista** (prisioneiro de sua patologia), **correcionalista** (ser **débil**, que precisa de **tutela**) e **marxista** (vítima das estruturas).',
  kw=['correcionalista', 'tutela'])
I(P, 1, 'Conceito criminológico de delito',
  'Para a Criminologia, o delito é exclusivamente o fato típico, ilícito e culpável definido pelo legislador.', 'E',
  'Esse é o conceito **jurídico-penal**. Para a Criminologia, o delito é **problema social e comunitário**, e ela pode estudar também condutas desviantes ainda não tipificadas.',
  peg='Reduzir o delito criminológico ao conceito analítico do Direito Penal.',
  kw=['problema social e comunitário', 'conceito jurídico-penal'])

# --- CRI-1.2 · Rodada 2
I(P, 2, 'Imagem marxista do delinquente',
  'Para a imagem marxista do delinquente, ele é vítima das estruturas econômicas, e a responsabilidade pelo crime se desloca para a sociedade.', 'C',
  'Na imagem **marxista**, o infrator é **vítima das estruturas** sociais e econômicas; a culpa recai sobre a organização social.',
  kw=['marxista', 'vítima das estruturas'])
I(P, 2, 'A vítima como objeto',
  'A vítima interessa à Criminologia não só pelo papel na gênese do delito, mas também pelos danos sofridos e pela relação com o sistema de justiça, que pode gerar vitimização secundária.', 'C',
  'A **vítima** é estudada na **dupla penal**, nos **danos** e no contato com as instâncias formais (**vitimização secundária**).',
  kw=['vitimização secundária', 'vítima'])
I(P, 2, 'Imagem positivista do delinquente',
  'Para a concepção positivista, o delinquente é um ser normal, igual aos demais, que opta livremente pelo crime.', 'E',
  'Essa é a imagem **clássica** (livre-arbítrio). Para o **positivismo**, o delinquente é **determinado** por fatores biológicos, psicológicos ou sociais — "prisioneiro" de sua patologia.',
  peg='Trocar as imagens clássica e positivista.',
  kw=['determinismo', 'livre-arbítrio'])
I(P, 2, 'Delinquente na Criminologia moderna',
  'Na Criminologia moderna, o infrator é visto como ser real, histórico e concreto, influenciável pelo meio, sem a idealização clássica nem o determinismo positivista.', 'C',
  'É o **homem real e histórico**: nem o ser racional abstrato dos clássicos, nem o determinado dos positivistas.',
  kw=['homem real', 'histórico e concreto'])
I(P, 2, 'Alcance do controle social',
  'O controle social é objeto da Criminologia apenas em seu aspecto formal, pois o controle informal não interessa ao estudo científico do crime.', 'E',
  'Ambos interessam: o **controle informal** (família, escola, comunidade) é decisivo para a prevenção, e o **formal** é estudado sobretudo quanto à seletividade.',
  peg='Excluir o controle informal do objeto.',
  kw=['controle informal', 'controle formal'])

# ======================= CRI-2 · Funções da Criminologia =======================
P = 'DBA26-CRI-2'
I(P, 1, 'Função de informar',
  'A função básica da Criminologia é informar a sociedade e os poderes públicos sobre o delito, o delinquente, a vítima e o controle social, oferecendo um núcleo de conhecimentos seguros sobre o problema criminal.', 'C',
  'A Criminologia oferece **diagnóstico qualificado** da realidade criminal — base para a política criminal e para a prevenção.',
  kw=['informar', 'diagnóstico qualificado'])
I(P, 1, 'Quem cria tipos penais',
  'Cabe à Criminologia formular as normas penais incriminadoras, por ser a ciência que conhece as causas do crime.', 'E',
  'Quem cria tipos é o **legislador**; a **Política Criminal** converte o saber empírico em estratégias e o **Direito Penal** em normas. A Criminologia fornece o **substrato empírico**.',
  peg='Dar à Criminologia papel normativo.',
  kw=['substrato empírico', 'legislador'])
I(P, 1, 'Funções em espécie',
  'Entre as funções da Criminologia estão explicar e prevenir o crime, intervir na pessoa do infrator e avaliar os diferentes modelos de resposta ao delito.', 'C',
  'São funções clássicas: **explicar**, **prevenir**, **intervir** no infrator e **avaliar** os modelos de reação.',
  kw=['explicar e prevenir', 'avaliar os modelos'])
I(P, 1, 'Avaliação do sistema',
  'Por ser ciência, a Criminologia deve abster-se de avaliar a eficácia do sistema penal, limitando-se à explicação causal do crime.', 'E',
  'Avaliar a **eficácia dos modelos de reação** (dissuasório, ressocializador, integrador) é função própria da Criminologia.',
  peg='Retirar da Criminologia a função avaliativa.',
  kw=['eficácia', 'modelos de reação'])
I(P, 1, 'Prevenção',
  'A Criminologia moderna valoriza a prevenção do delito, sem concentrar-se apenas na repressão.', 'C',
  'A **prevenção** é eixo da Criminologia moderna: atuar sobre causas e oportunidades, e não só punir.',
  kw=['prevenção', 'repressão'])
I(P, 1, 'Alcance das funções',
  'A função da Criminologia restringe-se ao estudo do criminoso, objeto que justificou o seu surgimento.', 'E',
  'O estudo do criminoso foi o foco **positivista**; hoje a Criminologia abrange **delito, delinquente, vítima e controle social**.',
  peg='Reduzir as funções ao objeto positivista.',
  kw=['delinquente', 'controle social'])

# --- CRI-2 · Rodada 2
I(P, 2, 'Natureza da informação',
  'A informação criminológica tem natureza probabilística e provisória, não oferecendo verdades absolutas.', 'C',
  'É saber **probabilístico**, sujeito a revisão — característica de toda ciência empírica social.',
  kw=['probabilística', 'provisória'])
I(P, 2, 'Neutralidade',
  'A Criminologia é neutra e desinteressada dos efeitos do sistema punitivo sobre as pessoas que ele alcança.', 'E',
  'A Criminologia avalia os **efeitos do sistema penal** (estigmatização, prisionização, seletividade) — tarefa central do paradigma da **reação social** e da **Criminologia crítica**.',
  peg='Atribuir à Criminologia uma neutralidade que a moderna doutrina rejeita.',
  kw=['efeitos do sistema penal', 'reação social'])
I(P, 2, 'Intervenção no infrator',
  'Entre as funções da Criminologia está a de orientar a intervenção positiva no infrator, buscando sua reinserção social, e não apenas sua neutralização.', 'C',
  'Função de **intervenção positiva**: programas que reduzam a reincidência e favoreçam a **reinserção**.',
  kw=['intervenção positiva', 'reinserção'])
I(P, 2, 'Criminologia e Política Criminal',
  'A Criminologia fornece à Política Criminal o substrato empírico a partir do qual se escolhem as estratégias de enfrentamento do crime.', 'C',
  'No modelo integrado, a Criminologia dá o **dado empírico**; a **Política Criminal** escolhe as **estratégias**; o Direito Penal as converte em **normas**.',
  kw=['substrato empírico', 'Política Criminal'])
I(P, 2, 'Paradigmas e função explicativa',
  'Em todas as correntes criminológicas, explicar o crime significa buscar suas causas na pessoa do delinquente.', 'E',
  'Isso é o **paradigma etiológico**. O paradigma da **reação social** explica a criminalidade pelos **processos de criminalização** e pela atuação das instâncias de controle.',
  peg='Generalizar o paradigma etiológico para todas as correntes.',
  kw=['paradigma etiológico', 'processos de criminalização'])

# ======================= CRI-2.1 · Criminologia e controle social =======================
P = 'DBA26-CRI-2.1'
I(P, 1, 'Conceito de controle social',
  'Controle social é o conjunto de mecanismos e sanções sociais que buscam submeter o indivíduo aos modelos e às normas comunitárias.', 'C',
  '**Controle social**: mecanismos e sanções que promovem a conformidade às normas do grupo — formais e informais.',
  kw=['controle social', 'normas comunitárias'])
I(P, 1, 'A polícia no controle social',
  'A polícia é agente de controle social informal.', 'E',
  'A polícia é instância de **controle social formal**, ao lado do Ministério Público, do Judiciário e da administração penitenciária.',
  peg='Classificar instância estatal como informal.',
  kw=['controle social formal', 'polícia'])
I(P, 1, 'Primeira seleção',
  'A polícia é, em regra, a primeira instância formal a selecionar condutas e pessoas que ingressarão no sistema penal.', 'C',
  'A **polícia** faz o primeiro **filtro** da criminalização secundária: decide o que registra, investiga e encaminha.',
  kw=['primeira instância formal', 'seleção'])
I(P, 1, 'Direito Penal e controle social',
  'O Direito Penal é o primeiro e principal instrumento de controle social.', 'E',
  'O Direito Penal é **ultima ratio**: instrumento **subsidiário** e **fragmentário**, que só atua quando os demais meios falham.',
  peg='Inverter a subsidiariedade do Direito Penal.',
  kw=['ultima ratio', 'subsidiário'])
I(P, 1, 'Seletividade',
  'A Criminologia crítica e o labelling approach apontam que o controle social formal atua de modo seletivo, recaindo com mais frequência sobre os grupos socialmente vulneráveis.', 'C',
  'A **seletividade** do controle formal é tese central do **labelling** e da **Criminologia crítica**.',
  kw=['seletividade', 'grupos vulneráveis'])
I(P, 1, 'Certeza × severidade',
  'Para a Criminologia, a eficácia preventiva depende mais do aumento das penas do que da efetividade do controle social informal.', 'E',
  'A eficácia preventiva depende muito mais do **controle informal** e da **certeza** da resposta do que da **severidade** das penas.',
  peg='Superestimar a severidade das penas.',
  kw=['controle informal', 'certeza'])

# --- CRI-2.1 · Rodada 2
I(P, 2, 'Criminalização primária e secundária',
  'A criminalização primária é a edição da lei penal que incrimina condutas; a criminalização secundária é a ação punitiva exercida sobre pessoas concretas pelas agências do sistema penal.', 'C',
  '**Primária**: o **legislador** define o crime. **Secundária**: **polícia, MP, juiz e prisão** aplicam a lei a pessoas concretas.',
  kw=['criminalização primária', 'criminalização secundária'])
I(P, 2, 'Capacidade operacional',
  'Na criminalização secundária, as agências, por sua limitada capacidade operacional, aplicam o programa da criminalização primária a todos os casos de forma igualitária.', 'E',
  'Justamente pela **limitada capacidade operacional**, as agências **selecionam** — e tendem a recair sobre os mais vulneráveis.',
  peg='Trocar "seletiva" por "igualitária".',
  kw=['capacidade operacional', 'seletividade'])
I(P, 2, 'Subsidiariedade do controle formal',
  'O controle social formal entra em ação, em regra, quando as instâncias informais fracassam, e se caracteriza por maior formalização e efeitos mais estigmatizantes.', 'C',
  'O **controle formal** é **subsidiário** do informal e produz **estigmatização** — ponto explorado pelo labelling.',
  kw=['controle formal', 'estigmatizantes'])
I(P, 2, 'Teoria dos vínculos sociais',
  'Para a teoria dos vínculos sociais, de Travis Hirschi, a pergunta relevante é por que a maioria das pessoas não delinque, e a resposta está na intimidação gerada pela severidade das penas.', 'E',
  'Para Hirschi, a conformidade vem dos **laços** com a sociedade — **apego, compromisso, envolvimento e crença** —, e não da severidade penal. A pergunta invertida ("por que não delinquem?") está correta.',
  peg='Trocar os vínculos sociais pela intimidação penal.',
  kw=['vínculos sociais', 'Hirschi'])
I(P, 2, 'Vínculos × aprendizagem',
  'Para a teoria dos vínculos sociais, a delinquência decorre do aprendizado de técnicas e motivações criminosas em grupos íntimos.', 'E',
  'Aprendizado em grupos íntimos é a **associação diferencial** de **Sutherland**. Para Hirschi, o crime surge do **enfraquecimento dos vínculos** sociais.',
  peg='Trocar a explicação de Hirschi pela de Sutherland.',
  kw=['associação diferencial', 'enfraquecimento dos vínculos'])

# ======================= CRI-2.2 · Direito Penal e política criminal =======================
P = 'DBA26-CRI-2.2'
I(P, 1, 'Política Criminal como ponte',
  'A Política Criminal funciona como ponte entre o saber empírico da Criminologia e o Direito Penal, transformando a experiência criminológica em opções e estratégias assumíveis pelo legislador.', 'C',
  'No **modelo integrado**: Criminologia (**ser**), Política Criminal (**ponte**, estratégias) e Direito Penal (**dever ser**, normas).',
  kw=['modelo integrado', 'ponte'])
I(P, 1, 'Objeto e método',
  'Criminologia e Direito Penal coincidem quanto ao método e ao objeto.', 'E',
  'Diferem nos dois: o **método** criminológico é **empírico-indutivo** e o penal **lógico-dedutivo**; o **objeto** criminológico é mais amplo (delito, delinquente, vítima e controle social).',
  peg='Igualar ciências de natureza diversa.',
  kw=['método', 'objeto'])
I(P, 1, 'Tipificação e legalidade',
  'A escolha das condutas a tipificar é decisão político-criminal do legislador, que pode valer-se dos dados criminológicos, mas fica vinculada à legalidade: não há crime sem lei anterior que o defina.', 'C',
  'A **tipificação** (criminalização primária) é opção **político-criminal**, sempre submetida à **legalidade**.',
  lei=[(CP + '1', 'Não há crime sem lei anterior que o defina', 'Não há pena sem prévia cominação legal.', 'CP, art. 1º')],
  kw=['tipificação', 'legalidade'])
I(P, 1, 'Ilicitude e desvio',
  'Para o Direito Penal, a ilicitude é a contrariedade da conduta típica ao ordenamento jurídico; a Criminologia, por sua vez, pode estudar como desviantes comportamentos ainda não tipificados.', 'C',
  '**Ilicitude** é categoria **dogmática**; a Criminologia trabalha com o conceito mais amplo de **desvio**.',
  kw=['ilicitude', 'desvio'])
I(P, 1, 'Comportamento da vítima na pena',
  'O Código Penal manda o juiz considerar, na fixação da pena-base, o comportamento da vítima, o que reflete a influência da Vitimologia na aplicação da pena.', 'C',
  'O **comportamento da vítima** é **circunstância judicial** do art. 59 — reflexo da Vitimologia na dogmática.',
  lei=[(CP + '59', 'O juiz, atendendo à culpabilidade', 'bem como ao comportamento da vítima', 'CP, art. 59, caput')],
  kw=['comportamento da vítima', 'circunstância judicial'])
I(P, 1, 'Finalidades da pena no CP',
  'Ao mandar fixar a pena conforme seja necessário e suficiente para reprovação e prevenção do crime, o art. 59 do Código Penal adota exclusivamente a teoria absoluta, retributiva, da pena.', 'E',
  'Ao falar em **reprovação** e **prevenção**, o art. 59 revela a **teoria mista (unificadora)**: retribuição somada à prevenção.',
  lei=[(CP + '59', 'estabelecerá, conforme seja necessário e suficiente para reprovação e prevenção do crime', None, 'CP, art. 59, caput')],
  peg='Esquecer a palavra "prevenção" do art. 59.',
  kw=['teoria mista', 'reprovação e prevenção'])
I(P, 1, 'Individualização da pena',
  'A individualização da pena é garantia constitucional restrita à fase judicial, não alcançando a cominação legislativa nem a execução.', 'E',
  'A **individualização** se projeta em **três fases**: **cominação** (legislador), **aplicação** (juiz) e **execução** (LEP).',
  peg='Restringir a individualização a uma só fase.',
  lei=[(CF + '5', 'XLVI - a lei regulará a individualização da pena', None, 'CF, art. 5º, XLVI')],
  kw=['individualização da pena', 'fases'])

# --- CRI-2.2 · Rodada 2
I(P, 2, 'Culpabilidade do fato',
  'No Direito Penal do Estado Democrático de Direito, a culpabilidade é do fato, e não do autor: a personalidade e o modo de vida do agente não podem, por si sós, fundamentar a punição.', 'C',
  'Vigora a **culpabilidade do fato**; o **Direito Penal do autor** (punir pelo que a pessoa é) é incompatível com o Estado Democrático de Direito.',
  kw=['culpabilidade do fato', 'Direito Penal do autor'])
I(P, 2, 'Culpabilidade como limite',
  'A culpabilidade funciona como fundamento e limite da pena, impedindo que necessidades preventivas justifiquem pena superior à medida da culpabilidade.', 'C',
  'A **culpabilidade** é **fundamento** e **limite**: a prevenção não autoriza ultrapassá-la.',
  kw=['fundamento e limite', 'culpabilidade'])
I(P, 2, 'Prevenção geral negativa',
  'A prevenção geral negativa vê a pena como intimidação dirigida ao próprio condenado, para que não volte a delinquir.', 'E',
  'Intimidar o **próprio condenado** é **prevenção especial negativa**. A **geral negativa** intimida a **coletividade**.',
  peg='Trocar o destinatário (coletividade × condenado).',
  kw=['prevenção geral negativa', 'prevenção especial negativa'])
I(P, 2, 'Prevenção geral positiva',
  'Para a prevenção geral positiva, a pena reafirma a vigência da norma e a confiança da coletividade no ordenamento jurídico.', 'C',
  'A **geral positiva** (integradora) busca **reafirmar a norma** e a **confiança** no Direito.',
  kw=['prevenção geral positiva', 'vigência da norma'])
I(P, 2, 'Prevenção especial positiva na LEP',
  'A prevenção especial positiva, voltada à ressocialização, encontra expressão na Lei de Execução Penal, cujo objetivo inclui proporcionar condições para a harmônica integração social do condenado.', 'C',
  'O art. 1º da LEP fala em **harmônica integração social** — é a **prevenção especial positiva**.',
  lei=[('L7210:1', 'A execução penal tem por objetivo', 'harmônica integração social do condenado e do internado.', 'LEP, art. 1º')],
  kw=['prevenção especial positiva', 'harmônica integração social'])
I(P, 2, 'Política criminal e aplicação da pena',
  'A substituição da pena privativa de liberdade por outra espécie de pena não integra as decisões do juiz na fixação da pena, sendo matéria exclusiva da execução penal.', 'E',
  'O art. 59, IV, inclui entre as decisões do juiz na sentença a **substituição** da pena privativa, **se cabível** — expressão da política criminal de alternativas à prisão.',
  lei=[(CP + '59', 'IV - a substituição da pena privativa da liberdade aplicada, por outra espécie de pena, se cabível.', None, 'CP, art. 59, IV')],
  peg='Retirar do juiz da sentença a substituição da pena.',
  kw=['substituição', 'alternativas à prisão'])
