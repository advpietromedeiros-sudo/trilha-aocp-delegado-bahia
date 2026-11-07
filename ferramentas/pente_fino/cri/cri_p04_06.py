# Pente Fino de Criminologia — pontos CRI-4 (Escolas), CRI-5 (Vitimologia) e CRI-6 (homem delinquente) (07/11/2026).
from base import I

CF = 'CF:'
CP = 'CP:'
CPP = 'CPP:'
ESC = 'L13431:'

# ======================= CRI-4 · Crime, criminoso e pena nas Escolas =======================
P = 'DBA26-CRI-4'
I(P, 1, 'Crime na Escola Clássica',
  'Para a Escola Clássica, especialmente em Carrara, o crime é ente jurídico: a infração da lei do Estado, promulgada para proteger a segurança dos cidadãos, resultante de ato externo do homem, moralmente imputável e politicamente danoso.', 'C',
  'Na **Escola Clássica**, o crime é **ente jurídico** (Carrara), e não fato natural.',
  kw=['ente jurídico', 'Carrara'])
I(P, 1, 'Criminoso e pena na Escola Clássica',
  'Para a Escola Clássica, o criminoso é ser livre, dotado de livre-arbítrio e moralmente responsável, e a pena é retribuição proporcional ao mal praticado.', 'C',
  'Clássicos: **livre-arbítrio**, **responsabilidade moral**, **pena retributiva e proporcional**, método **lógico-abstrato**.',
  kw=['livre-arbítrio', 'responsabilidade moral'])
I(P, 1, 'Fundamento da pena clássica',
  'Para a Escola Clássica, a pena tem por fundamento a periculosidade do agente e deve ser indeterminada, até sua cura.', 'E',
  '**Periculosidade** e **indeterminação** são marcas **positivistas**. Para os clássicos, a pena é **retribuição** pela culpa, **determinada** e **proporcional** ao crime.',
  peg='Levar à Escola Clássica a periculosidade positivista.',
  kw=['periculosidade', 'retribuição'])
I(P, 1, 'Escola Positiva',
  'Para a Escola Positiva, o crime é fato natural e social, o criminoso é determinado por fatores que não controla, a responsabilidade é social e a sanção é defesa social, proporcional à periculosidade.', 'C',
  'Positivismo: **determinismo**, **responsabilidade social**, sanção como **defesa social** medida pela **periculosidade**, método **empírico-indutivo**.',
  kw=['determinismo', 'defesa social'])
I(P, 1, 'Fases do positivismo',
  'Costuma-se dividir a Escola Positiva em três fases: antropológica, com Ferri; sociológica, com Lombroso; e jurídica, com Garofalo.', 'E',
  'Ferri e Lombroso estão trocados. Trindade positivista: **Lombroso** (antropológica), **Ferri** (sociológica) e **Garofalo** (jurídica).',
  peg='Trocar os autores das fases.',
  kw=['Lombroso', 'Ferri'])
I(P, 1, 'Delito natural',
  'Carrara concebeu o delito natural como a violação dos sentimentos altruísticos fundamentais de piedade e probidade, na medida média em que se encontram na comunidade.', 'E',
  'O **delito natural** é de **Garofalo** (positivista). **Carrara**, clássico, via o crime como **ente jurídico**.',
  peg='Trocar o autor do conceito.',
  kw=['delito natural', 'piedade e probidade'])
I(P, 1, 'Ferri e a responsabilidade',
  'Para Enrico Ferri, a responsabilidade penal funda-se no livre-arbítrio do agente.', 'E',
  '**Ferri** negou o livre-arbítrio e defendeu a **responsabilidade social** (legal): o indivíduo responde porque vive em sociedade.',
  peg='Atribuir a um positivista a premissa clássica.',
  kw=['responsabilidade social', 'Ferri'])
I(P, 1, 'Escola Técnico-Jurídica',
  'A Escola Técnico-Jurídica, inaugurada por Arturo Rocco em 1905, propôs que o Direito Penal se ocupasse do direito positivo vigente, com método técnico-jurídico, afastando de seu estudo as indagações antropológicas, sociológicas e filosóficas.', 'C',
  'A **Técnico-Jurídica** separa o **Direito Penal** (dogmática do direito positivo) da Criminologia e da filosofia; crime é fato jurídico; a pena mantém sentido retributivo, e a medida de segurança alcança os perigosos.',
  kw=['Técnico-Jurídica', 'Arturo Rocco'])
I(P, 1, 'Criminologia crítica',
  'Para a Criminologia crítica, o crime não é realidade ontológica, mas status atribuído por processos seletivos de criminalização que reproduzem desigualdades, e a pena atua na manutenção da estrutura social.', 'C',
  'Crítica: crime como **construção social**, criminoso como **selecionado**, pena como instrumento de **reprodução** da desigualdade; propõe **Direito Penal mínimo** e, no limite, abolição.',
  kw=['Criminologia crítica', 'status atribuído'])
I(P, 1, 'Criminoso na crítica',
  'Para a Criminologia crítica, o criminoso é um ser anormal, biologicamente predisposto ao delito.', 'E',
  'Essa é a visão **positivista biológica**. Para a **crítica**, o criminoso é o **selecionado** pelo sistema penal, em regra entre os vulneráveis.',
  peg='Atribuir à crítica o determinismo biológico.',
  kw=['selecionado', 'Criminologia crítica'])

# --- CRI-4 · Rodada 2
I(P, 2, 'Beccaria',
  'Em Dos Delitos e das Penas (1764), Beccaria defendeu a legalidade dos crimes e das penas, a proporcionalidade e a abolição da tortura, e combateu a pena de morte, admitindo-a apenas em hipóteses excepcionalíssimas.', 'C',
  '**Beccaria**: **legalidade**, **proporcionalidade**, **utilidade** da pena, contra a **tortura** e a **pena de morte** (salvo exceções extremas).',
  kw=['Beccaria', 'proporcionalidade'])
I(P, 2, 'Crime para Carrara',
  'Carrara concebeu o crime como ente de fato, natural, cuja existência independe da lei.', 'E',
  'Para **Carrara**, o crime é **ente jurídico** — só existe pela **lei**. Fato natural é a visão **positivista** (Garofalo).',
  peg='Trocar "ente jurídico" por "ente de fato".',
  kw=['ente jurídico', 'Carrara'])
I(P, 2, 'Terceira Escola',
  'A Terceira Escola italiana (Terza Scuola) buscou conciliar postulados clássicos e positivistas, distinguindo imputáveis, sujeitos à pena, e inimputáveis, sujeitos à medida de segurança.', 'C',
  'A **Terza Scuola** é **eclética**: aceita a responsabilidade moral, mas sem o livre-arbítrio absoluto, e separa **imputáveis** e **inimputáveis**.',
  kw=['Terza Scuola', 'imputáveis e inimputáveis'])
I(P, 2, 'Escola Moderna Alemã',
  'Para von Liszt, a pena deve atender à prevenção especial: corrigir os corrigíveis, intimidar os que não precisam de correção e neutralizar os incorrigíveis.', 'C',
  'A **Escola Moderna Alemã** (von Liszt) dá à pena fim de **prevenção especial**, com a tríade **correção, intimidação, inocuização**.',
  kw=['von Liszt', 'prevenção especial'])
I(P, 2, 'Sanção positivista',
  'Para a Escola Positiva, a sanção deve ser fixa e proporcional à gravidade objetiva do fato praticado.', 'E',
  'O **positivismo** mede a sanção pela **periculosidade** do agente e admite sanção **indeterminada**; proporcionalidade ao fato é ideia **clássica**.',
  peg='Levar ao positivismo a proporcionalidade clássica.',
  kw=['periculosidade', 'indeterminada'])
I(P, 2, 'Raízes da Criminologia crítica',
  'A Criminologia crítica tem raízes positivistas e foi desenvolvida, entre outros, por Taylor, Walton e Young, autores de A Nova Criminologia, e por Alessandro Baratta.', 'E',
  'As raízes da crítica são **marxistas**, não positivistas — ela é, aliás, crítica do positivismo. Os autores estão certos: **Nova Criminologia** (Taylor, Walton e Young, 1973) e **Baratta**.',
  peg='Trocar a matriz teórica.',
  kw=['Baratta', 'Nova Criminologia'])

# ======================= CRI-5 · Vitimologia =======================
P = 'DBA26-CRI-5'
I(P, 1, 'Marcos da Vitimologia',
  'Benjamin Mendelsohn é apontado como pai da Vitimologia, e Hans von Hentig, com The Criminal and His Victim (1948), contribuiu decisivamente para o estudo da vítima na gênese do crime.', 'C',
  '**Mendelsohn** (pai da Vitimologia) e **von Hentig** (1948) marcam a **redescoberta da vítima** no pós-guerra.',
  kw=['Mendelsohn', 'von Hentig'])
I(P, 1, 'Classificação de Mendelsohn',
  'Mendelsohn classificou as vítimas, segundo sua participação no crime, em completamente inocente, menos culpada que o infrator, tão culpada quanto o infrator, mais culpada que o infrator e unicamente culpada.', 'C',
  'As **cinco categorias** de Mendelsohn graduam a **culpabilidade** da vítima: da **ideal** (inocente) à **unicamente culpada**.',
  kw=['classificação de Mendelsohn', 'unicamente culpada'])
I(P, 1, 'Vítima unicamente culpada',
  'Na classificação de Mendelsohn, quem pratica agressão injusta e acaba ferido por quem age em legítima defesa é vítima completamente inocente.', 'E',
  'Quem agride e é repelido em legítima defesa é **vítima unicamente culpada** (infratora). Também nessa categoria estão a **simuladora** e a **imaginária**.',
  peg='Trocar a categoria extrema.',
  kw=['unicamente culpada', 'legítima defesa'])
I(P, 1, 'Dupla penal',
  'Von Hentig destacou a interação entre autor e vítima na gênese do crime, a chamada dupla penal, e a existência de vítimas com maior propensão à vitimização.', 'C',
  '**Dupla penal**: o crime como **interação** autor-vítima; há vítimas **propensas** (vulneráveis).',
  kw=['dupla penal', 'propensão'])
I(P, 1, 'Vitimização primária',
  'A vitimização primária decorre diretamente do crime e corresponde aos danos físicos, psíquicos e materiais sofridos pela vítima.', 'C',
  '**Primária**: o dano do **próprio crime**.',
  kw=['vitimização primária', 'danos'])
I(P, 1, 'Vitimização secundária',
  'A vitimização secundária, ou sobrevitimização, é causada pelo meio social da vítima, como família, amigos e vizinhos, que a isolam ou estigmatizam.', 'E',
  'Isso é a **terciária** (na posição mais cobrada). A **secundária** é causada pelas **instâncias formais** — polícia, MP, Judiciário — no curso da investigação e do processo.',
  peg='Trocar secundária por terciária.',
  kw=['vitimização secundária', 'instâncias formais'])
I(P, 1, 'Vitimização terciária',
  'A vitimização terciária decorre do próprio crime, nos danos materiais sofridos pela vítima.', 'E',
  'Dano do crime é **primária**. Na posição mais cobrada, a **terciária** vem do **meio social** (família, amigos, comunidade) e da falta de amparo, que isolam ou estigmatizam a vítima. Há quem use a expressão para os efeitos do sistema sobre o próprio **condenado** — divergência a conhecer.',
  peg='Trocar terciária por primária.',
  kw=['vitimização terciária', 'meio social'])
I(P, 1, 'Violência institucional',
  'A Lei 13.431/2017 define violência institucional como a praticada por instituição pública ou conveniada, inclusive quando gerar revitimização.', 'C',
  'A **violência institucional** da Lei 13.431/2017 é a **vitimização secundária** posta em lei.',
  lei=[(ESC + '4', 'IV - violência institucional, entendida como a praticada por instituição pública ou conveniada', 'inclusive quando gerar revitimização.', 'Lei 13.431/2017, art. 4º, IV')],
  kw=['violência institucional', 'revitimização'])
I(P, 1, 'Comunicação ao ofendido',
  'O ofendido será comunicado dos atos processuais relativos ao ingresso e à saída do acusado da prisão, à designação de audiência e à sentença e aos acórdãos que a mantenham ou modifiquem.', 'C',
  'O art. 201, § 2º, do CPP é expressão do **protagonismo da vítima** no processo.',
  lei=[(CPP + '201', 'O ofendido será comunicado dos atos processuais', 'respectivos acórdãos que a mantenham ou modifiquem.', 'CPP, art. 201, § 2º')],
  kw=['ofendido', 'comunicado'])
I(P, 1, 'Crime de violência institucional',
  'A Lei de Abuso de Autoridade tipifica a conduta de submeter a vítima de infração penal ou a testemunha de crimes violentos a procedimentos desnecessários, repetitivos ou invasivos que a levem a reviver, sem estrita necessidade, a situação de violência.', 'C',
  'É o art. 15-A da Lei 13.869/2019, incluído pela Lei 14.321/2022: a **revitimização** virou **crime**.',
  lei=[('L13869:15-A', 'Submeter a vítima de infração penal ou a testemunha de crimes violentos', 'a situação de violência; ou', 'Lei 13.869/2019, art. 15-A, caput e I')],
  kw=['revitimização', 'violência institucional'])

# --- CRI-5 · Rodada 2
I(P, 2, 'Atendimento multidisciplinar',
  'Se o juiz entender necessário, poderá encaminhar o ofendido para atendimento multidisciplinar, nas áreas psicossocial, de assistência jurídica e de saúde, a expensas do ofensor ou do Estado.', 'C',
  'Art. 201, § 5º: **atendimento multidisciplinar** à vítima, custeado pelo **ofensor ou pelo Estado**.',
  lei=[(CPP + '201', 'Se o juiz entender necessário, poderá encaminhar o ofendido para atendimento multidisciplinar', 'a expensas do ofensor ou do Estado.', 'CPP, art. 201, § 5º')],
  kw=['atendimento multidisciplinar', 'ofendido'])
I(P, 2, 'Condução do ofendido',
  'O ofendido que, intimado, deixa de comparecer sem motivo justo não pode ser conduzido à presença da autoridade, pois não é testemunha.', 'E',
  'Pelo art. 201, § 1º, o ofendido **poderá ser conduzido** à presença da autoridade.',
  lei=[(CPP + '201', 'Se, intimado para esse fim, deixar de comparecer sem motivo justo', 'poderá ser conduzido à presença da autoridade.', 'CPP, art. 201, § 1º')],
  peg='Negar a condução do ofendido.',
  kw=['conduzido', 'ofendido'])
I(P, 2, 'Depoimento especial',
  'O depoimento especial de criança ou adolescente vítima ou testemunha de violência é procedimento exclusivo da autoridade judiciária, vedado na fase policial.', 'E',
  'O **depoimento especial** se faz perante **autoridade policial ou judiciária**.',
  lei=[(ESC + '8', 'Depoimento especial é o procedimento de oitiva', 'perante autoridade policial ou judiciária.', 'Lei 13.431/2017, art. 8º')],
  peg='Excluir a autoridade policial.',
  kw=['depoimento especial', 'autoridade policial'])
I(P, 2, 'Contato com o autor',
  'A criança ou o adolescente será resguardado de qualquer contato, ainda que visual, com o suposto autor ou acusado.', 'C',
  'O art. 9º da Lei 13.431/2017 evita a **revitimização** pelo contato com o agressor.',
  lei=[(ESC + '9', 'A criança ou o adolescente será resguardado de qualquer contato, ainda que visual', 'com o suposto autor ou acusado', 'Lei 13.431/2017, art. 9º')],
  kw=['ainda que visual', 'revitimização'])
I(P, 2, 'Assistência a dependentes',
  'A Constituição prevê que a lei disporá sobre a assistência do Poder Público aos herdeiros e dependentes carentes de pessoas vitimadas por crime doloso, sem prejuízo da responsabilidade civil do autor.', 'C',
  'O art. 245 da Constituição é a base constitucional da **assistência às vítimas indiretas** de crime doloso.',
  lei=[(CF + '245', 'A lei disporá sobre as hipóteses e condições', 'sem prejuízo da responsabilidade civil do autor do ilícito.', 'CF, art. 245')],
  kw=['herdeiros e dependentes carentes', 'crime doloso'])
I(P, 2, 'Vitimodogmática',
  'A vitimodogmática estuda a contribuição da vítima para o delito e sua repercussão na responsabilidade do autor, o que se reflete no comportamento da vítima como circunstância judicial.', 'C',
  'A **vitimodogmática** leva a Vitimologia à dogmática — ex.: **comportamento da vítima** no art. 59 do CP.',
  lei=[(CP + '59', 'O juiz, atendendo à culpabilidade', 'bem como ao comportamento da vítima', 'CP, art. 59, caput')],
  kw=['vitimodogmática', 'comportamento da vítima'])
I(P, 2, 'Subnotificação',
  'A subnotificação de crimes sexuais costuma ser explicada, entre outros fatores, pelo medo, pela vergonha e pelo receio de vitimização secundária.', 'C',
  'Esses fatores elevam a **cifra negra** dos crimes sexuais.',
  kw=['subnotificação', 'cifra negra'])
I(P, 2, 'Síndrome de Estocolmo',
  'Na síndrome de Estocolmo, a vítima de sequestro ou cárcere desenvolve aversão intensa ao captor e passa a colaborar com a polícia contra ele.', 'E',
  'Na **síndrome de Estocolmo**, a vítima desenvolve **vínculo afetivo ou de simpatia** com o captor, às vezes até defendendo-o.',
  peg='Inverter o efeito psicológico.',
  kw=['síndrome de Estocolmo', 'vínculo afetivo'])

# ======================= CRI-6 · O homem delinquente =======================
P = 'DBA26-CRI-6'
I(P, 1, 'Lombroso',
  'Lombroso, em O Homem Delinquente (1876), sustentou a existência do criminoso nato, explicado pelo atavismo e reconhecível por estigmas físicos e psíquicos.', 'C',
  '**Lombroso**: **criminoso nato**, **atavismo** (regressão a estágio primitivo), **estigmas** anatômicos.',
  kw=['criminoso nato', 'atavismo'])
I(P, 1, 'Categorias lombrosianas',
  'Lombroso jamais admitiu outras categorias de criminosos além do nato.', 'E',
  'Nas edições posteriores, Lombroso admitiu outras categorias — **louco**, **epiléptico**, **ocasional**, **passional** —, reduzindo o peso do nato.',
  peg='Ignorar a evolução da obra.',
  kw=['categorias', 'Lombroso'])
I(P, 1, 'Biotipologia de Kretschmer',
  'Kretschmer associou tipos constitucionais — leptossômico, atlético e pícnico — a temperamentos e a tendências delitivas.', 'C',
  'A **biotipologia** de **Kretschmer** liga **constituição corporal** e **temperamento**.',
  kw=['Kretschmer', 'biotipologia'])
I(P, 1, 'Cromossomo XYY',
  'Estudos genéticos comprovaram que o cromossomo Y extra (síndrome XYY) é causa determinante da criminalidade violenta.', 'E',
  'A hipótese do **XYY** foi levantada nos anos 1960, mas **não se confirmou** como causa do crime; a genética trabalha com **predisposição** e interação com o meio.',
  peg='Transformar hipótese em causa comprovada.',
  kw=['XYY', 'predisposição'])
I(P, 1, 'Criminoso por sentimento de culpa',
  'Na perspectiva psicanalítica, Freud descreveu o criminoso por sentimento de culpa, que pratica o delito para obter punição e aliviar culpa preexistente.', 'C',
  'Teoria **psicodinâmica**: a culpa **antecede** o crime, que busca a **punição**.',
  kw=['sentimento de culpa', 'psicanalítica'])
I(P, 1, 'Psicopatia',
  'A psicopatia caracteriza-se por traços como ausência de empatia e de remorso, manipulação e impulsividade e, em regra, não suprime a capacidade de entender o caráter ilícito do fato.', 'C',
  'Na **psicopatia**, a **capacidade de entendimento** costuma estar preservada: a perícia tende a concluir pela **imputabilidade** ou, no máximo, pela semi-imputabilidade.',
  kw=['psicopatia', 'capacidade de entendimento'])
I(P, 1, 'Fatores biológicos hoje',
  'As teorias criminológicas contemporâneas abandonaram por completo o estudo dos fatores biológicos, hoje considerados irrelevantes.', 'E',
  'A **neurociência**, a **genética** e a **bioquímica** seguem estudadas, mas em modelo **biopsicossocial**, sem determinismo.',
  peg='Declarar irrelevante o que é apenas relativizado.',
  kw=['biopsicossocial', 'fatores biológicos'])
I(P, 1, 'Aprendizagem social',
  'Para a teoria da aprendizagem social, de Bandura, a agressividade pode ser aprendida pela observação e imitação de modelos, reforçada pelas consequências do comportamento.', 'C',
  '**Bandura**: **modelagem** — aprende-se a agressão observando e imitando.',
  kw=['aprendizagem social', 'Bandura'])

# --- CRI-6 · Rodada 2
I(P, 2, 'Lombroso e epilepsia',
  'Lombroso aproximou o criminoso nato do epiléptico e da chamada loucura moral, como manifestações de um mesmo fundo patológico.', 'C',
  'Lombroso ligou **criminoso nato**, **epilepsia** e **loucura moral** num mesmo tronco.',
  kw=['epilepsia', 'loucura moral'])
I(P, 2, 'Eysenck',
  'Eysenck relacionou a criminalidade a traços de personalidade e à menor condicionabilidade dos indivíduos introvertidos.', 'E',
  'Para **Eysenck**, os **extrovertidos** são menos condicionáveis — daí o risco maior. Dimensões: extroversão, neuroticismo, psicoticismo.',
  peg='Trocar extrovertidos por introvertidos.',
  kw=['Eysenck', 'condicionabilidade'])
I(P, 2, 'Sheldon',
  'Sheldon classificou os somatótipos em endomorfo, mesomorfo e ectomorfo, associando o ectomorfo à delinquência.', 'E',
  'Sheldon associou à delinquência o **mesomorfo** (musculoso, atlético).',
  peg='Trocar o somatótipo.',
  kw=['mesomorfo', 'Sheldon'])
I(P, 2, 'Psicanálise',
  'Na teoria psicanalítica, o crime é explicado sempre por fatores sociais externos, sem relação com conflitos psíquicos inconscientes.', 'E',
  'A psicanálise explica o crime por **conflitos inconscientes** e falhas na formação do **superego**.',
  peg='Retirar o inconsciente da psicanálise.',
  kw=['conflitos inconscientes', 'superego'])
I(P, 2, 'Goring',
  'Goring, ao comparar presos e não presos no início do século XX, confirmou integralmente as teses lombrosianas sobre estigmas físicos.', 'E',
  'Os estudos de **Goring** (1913) **não confirmaram** os estigmas lombrosianos.',
  peg='Inverter o resultado do estudo.',
  kw=['Goring', 'estigmas'])
I(P, 2, 'Frustração-agressão',
  'Segundo a hipótese frustração-agressão, a frustração de objetivos tende a gerar impulsos agressivos, que podem ser dirigidos à fonte da frustração ou deslocados para outros alvos.', 'C',
  'A hipótese **frustração-agressão** (Dollard e colaboradores, 1939) é teoria **psicológica** clássica.',
  kw=['frustração-agressão', 'impulsos agressivos'])
