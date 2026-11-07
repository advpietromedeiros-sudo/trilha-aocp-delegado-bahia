# Pente Fino de Criminologia — pontos CRI-3 e CRI-3.1 a CRI-3.6 (07/11/2026).
from base import I

CF = 'CF:'
LEP = 'L7210:'
JEC = 'L9099:'

# ======================= CRI-3 · Modelos teóricos da Criminologia =======================
P = 'DBA26-CRI-3'
I(P, 1, 'Consenso × conflito',
  'Entre as teorias do consenso costumam ser incluídas a Escola de Chicago, a associação diferencial, a anomia e a subcultura delinquente; entre as do conflito, o labelling approach e a Criminologia crítica.', 'C',
  'É a classificação mais cobrada: **consenso** (Chicago, associação diferencial, anomia, subcultura) × **conflito** (labelling, crítica). Há autores que a matizam, mas a banca segue esta.',
  kw=['teorias do consenso', 'teorias do conflito'])
I(P, 1, 'Premissa das teorias do conflito',
  'Para as teorias do consenso, a sociedade é composta por grupos com valores antagônicos, e a ordem se mantém pela força e pela coerção.', 'E',
  'Essa é a premissa das teorias do **conflito**. As do **consenso** veem a sociedade integrada por **valores compartilhados**, com instituições que funcionam.',
  peg='Trocar a premissa de uma família pela da outra.',
  kw=['teorias do conflito', 'valores compartilhados'])
I(P, 1, 'Paradigmas',
  'O paradigma etiológico busca as causas do crime, enquanto o paradigma da reação social estuda os processos de criminalização e a atuação das instâncias de controle.', 'C',
  '**Etiológico**: por que alguém delinque. **Reação social**: como e por que alguém é **definido** como criminoso.',
  kw=['paradigma etiológico', 'paradigma da reação social'])
I(P, 1, 'Modelos biológico, psicológico e sociológico',
  'Os modelos sociológicos têm enfoque predominantemente individual, ao passo que os biológicos e psicológicos tratam o crime como fenômeno social.', 'E',
  'Está trocado: modelos **individuais** são o biológico e o psicológico; os **sociológicos** tratam o crime como fenômeno coletivo, ligado à estrutura social.',
  peg='Inverter o enfoque dos modelos.',
  kw=['modelos sociológicos', 'enfoque individual'])
I(P, 1, 'Classificação da associação diferencial',
  'A teoria da associação diferencial, de Sutherland, integra as teorias do conflito.', 'E',
  'A **associação diferencial** costuma ser classificada entre as **teorias do consenso**, ao lado de Chicago, anomia e subcultura.',
  peg='Deslocar teoria do consenso para o conflito.',
  kw=['associação diferencial', 'teorias do consenso'])
I(P, 1, 'Coerção nas teorias do conflito',
  'Para as teorias do conflito, a ordem social se funda na força e na coerção, na dominação de alguns e na sujeição de outros.', 'C',
  'As teorias do **conflito** veem a ordem como resultado de **coerção** e **poder** — e o crime como definição de quem tem o poder.',
  kw=['coerção', 'teorias do conflito'])
I(P, 1, 'Perguntas dos paradigmas',
  'O paradigma da reação social pergunta por que o indivíduo delinque, ao passo que o paradigma etiológico pergunta quem é definido como delinquente e por quê.', 'E',
  'Está invertido: o **etiológico** pergunta **por que** se delinque; a **reação social** pergunta **quem é definido** como delinquente.',
  peg='Inverter as perguntas dos dois paradigmas.',
  kw=['paradigma etiológico', 'reação social'])

# --- CRI-3 · Rodada 2
I(P, 2, 'Funcionalismo',
  'Para as teorias do consenso, de matriz funcionalista, a sociedade funciona bem quando suas instituições operam e os indivíduos compartilham as metas sociais e as regras de convivência.', 'C',
  'O **funcionalismo** está na base das teorias do **consenso**: integração, valores comuns, instituições funcionando.',
  kw=['funcionalista', 'teorias do consenso'])
I(P, 2, 'Teorias multifatoriais',
  'As teorias multifatoriais combinam fatores biológicos, psicológicos e sociais, linha já presente em Ferri, que agrupou os fatores do crime em antropológicos, físicos e sociais.', 'C',
  '**Ferri** formulou a classificação **tripartida** dos fatores do crime: **antropológicos, físicos e sociais**.',
  kw=['multifatoriais', 'Ferri'])
I(P, 2, 'Classificação da Criminologia crítica',
  'A Criminologia crítica é teoria do consenso, de matriz funcionalista.', 'E',
  'A **Criminologia crítica** é teoria do **conflito**, de matriz **marxista**.',
  peg='Trocar a família teórica da crítica.',
  kw=['Criminologia crítica', 'conflito'])
I(P, 2, 'Micro × macro',
  'O labelling approach parte do interacionismo simbólico, de base microssociológica, enquanto a Criminologia crítica dá ênfase macrossociológica às estruturas econômicas e de poder.', 'C',
  'É a crítica clássica ao **labelling**: ficou no plano **micro**; a **Criminologia crítica** leva a análise às **estruturas** (macro).',
  kw=['microssociológica', 'macrossociológica'])
I(P, 2, 'Atividades rotineiras',
  'Para a teoria das atividades rotineiras, o crime predatório ocorre com a convergência, no tempo e no espaço, de um ofensor motivado, um alvo adequado e a presença de um guardião capaz.', 'E',
  'O terceiro elemento é a **ausência** de um **guardião capaz**. Ofensor motivado + alvo adequado + falta de guardião = oportunidade.',
  peg='Trocar "ausência" por "presença" do guardião.',
  kw=['atividades rotineiras', 'guardião capaz'])

# ======================= CRI-3.1 · Teorias sociológicas =======================
P = 'DBA26-CRI-3.1'
I(P, 1, 'Escola de Chicago',
  'A Escola de Chicago estudou a relação entre a cidade e o crime, identificando, no modelo de zonas concêntricas, maior criminalidade na chamada zona de transição.', 'C',
  'A **ecologia criminal** de Chicago (Park, Burgess, Shaw e McKay) liga o crime à **desorganização social** das áreas urbanas, sobretudo a **zona de transição**.',
  kw=['Escola de Chicago', 'zona de transição'])
I(P, 1, 'Associação diferencial',
  'Para a teoria da associação diferencial, o comportamento criminoso é aprendido na interação com outras pessoas, principalmente em grupos íntimos, incluindo técnicas, motivos e racionalizações.', 'C',
  '**Sutherland**: o crime é **aprendido** — técnicas e definições favoráveis à violação da lei, em **grupos íntimos**.',
  kw=['associação diferencial', 'aprendido'])
I(P, 1, 'Crime aprendido, não herdado',
  'Para Sutherland, o comportamento criminoso é herdado ou inventado pelo próprio indivíduo, e não aprendido.', 'E',
  'Sutherland afirma o oposto: o crime é **aprendido**, não herdado nem inventado.',
  peg='Negar o núcleo da teoria.',
  kw=['aprendido', 'Sutherland'])
I(P, 1, 'Anomia em Merton',
  'Para Merton, a anomia decorre da tensão entre as metas culturais de sucesso e os meios institucionalizados, que a estrutura social distribui de forma igualitária entre todas as classes.', 'E',
  'O núcleo de **Merton** é justamente o acesso **desigual** aos **meios institucionalizados**: a pressão sobre quem não tem acesso a eles favorece o desvio.',
  peg='Trocar "desigual" por "igualitária".',
  kw=['anomia', 'metas culturais'])
I(P, 1, 'Subcultura delinquente',
  'Para Albert Cohen, a subcultura delinquente surge da frustração de status de jovens das classes baixas e tem caráter não utilitário, malicioso e negativista.', 'C',
  'A **subcultura delinquente** (Cohen, 1955) é **não utilitária, maliciosa e negativista** — inverte os valores da classe média.',
  kw=['subcultura delinquente', 'frustração de status'])
I(P, 1, 'Labelling',
  'Para o labelling approach, o desvio não é qualidade intrínseca do ato, mas consequência da aplicação, por outros, de regras e sanções a quem é rotulado como desviante.', 'C',
  'É a tese de **Becker**: desviante é aquele a quem o **rótulo** foi aplicado com sucesso.',
  kw=['labelling approach', 'rótulo'])
I(P, 1, 'Criminologia crítica e definição de crime',
  'A Criminologia crítica aceita a definição legal de crime como dado natural e concentra-se nas causas individuais da delinquência.', 'E',
  'A **Criminologia crítica** questiona a definição legal: o crime é **construção social** ligada a relações de **poder** e de classe.',
  peg='Atribuir à crítica postura etiológica individual.',
  kw=['Criminologia crítica', 'construção social'])

# --- CRI-3.1 · Rodada 2
I(P, 2, 'Técnicas de neutralização',
  'Para Sykes e Matza, o delinquente usa técnicas de neutralização como a negação da responsabilidade, a negação do dano, a negação da vítima, a condenação dos que condenam e o apelo a lealdades superiores.', 'C',
  'As **cinco técnicas de neutralização** permitem ao jovem violar normas que, no fundo, reconhece.',
  kw=['técnicas de neutralização', 'Sykes e Matza'])
I(P, 2, 'Neutralização × subcultura',
  'Na teoria da neutralização, o delinquente rejeita integralmente os valores dominantes, como na subcultura de Cohen.', 'E',
  'Para **Sykes e Matza**, o jovem **reconhece** os valores dominantes e por isso precisa **neutralizá-los** — crítica direta à ideia de valores totalmente invertidos.',
  peg='Igualar neutralização e subcultura.',
  kw=['neutralização', 'valores dominantes'])
I(P, 2, 'Janelas quebradas',
  'A teoria das janelas quebradas, de Wilson e Kelling, sustenta que a desordem não reparada sinaliza ausência de controle e favorece crimes mais graves, tendo inspirado políticas de tolerância zero.', 'C',
  '**Broken windows** (1982): a **desordem** não reparada estimula o crime — base da **tolerância zero** em Nova York.',
  kw=['janelas quebradas', 'tolerância zero'])
I(P, 2, 'Pequenas desordens',
  'A teoria das janelas quebradas considera as pequenas desordens irrelevantes para a criminalidade grave, devendo a polícia concentrar-se exclusivamente nos crimes violentos.', 'E',
  'É o oposto: para as **janelas quebradas**, as **pequenas desordens** importam porque sinalizam abandono e atraem crimes mais graves.',
  peg='Negar a premissa da teoria.',
  kw=['pequenas desordens', 'janelas quebradas'])
I(P, 2, 'Crime de colarinho branco',
  'Sutherland definiu o crime de colarinho branco como aquele cometido por pessoa de respeitabilidade e alto status social no curso de sua ocupação.', 'C',
  'O **white-collar crime** mostrou que a criminalidade não é exclusiva das classes baixas — reforço à **associação diferencial**.',
  kw=['colarinho branco', 'Sutherland'])
I(P, 2, 'Oportunidade diferencial',
  'Para Cloward e Ohlin, o acesso aos meios ilegítimos também é desigual, o que gera subculturas distintas: criminal, conflitiva e retraída.', 'C',
  'A **oportunidade diferencial** une anomia e associação diferencial: há **três subculturas** — **criminal, conflitiva** (violenta) e **retraída** (evasiva).',
  kw=['oportunidade diferencial', 'Cloward e Ohlin'])

# ======================= CRI-3.2 · Prevenção no Estado Democrático de Direito =======================
P = 'DBA26-CRI-3.2'
I(P, 1, 'Limites democráticos da prevenção',
  'No Estado Democrático de Direito, a prevenção do crime deve respeitar os direitos fundamentais, e a eficiência preventiva não legitima meios contrários à dignidade humana.', 'C',
  'A prevenção democrática é **limitada pelos direitos fundamentais** e pela **dignidade da pessoa humana**.',
  kw=['direitos fundamentais', 'dignidade'])
I(P, 1, 'Conceito clássico × moderno',
  'Para o conceito clássico, prevenir é dissuadir o infrator potencial com a ameaça da pena; para a Criminologia moderna, a prevenção deve atuar também sobre as causas e as oportunidades do crime.', 'C',
  'Do **dissuasório** (ameaça penal) ao **etiológico-situacional** (causas e oportunidades).',
  kw=['conceito clássico', 'causas e oportunidades'])
I(P, 1, 'Severidade da pena',
  'A Criminologia moderna demonstrou que o aumento da severidade das penas é o meio mais eficaz de prevenção.', 'E',
  'O que mais pesa é a **certeza** e a **rapidez** da resposta, não a **severidade** — lição que remonta a Beccaria.',
  peg='Superestimar o efeito da pena alta.',
  kw=['certeza', 'severidade'])
I(P, 1, 'Beccaria e a prevenção',
  'Já em Beccaria se encontra a ideia de que a severidade da punição tem maior efeito preventivo do que a sua certeza.', 'E',
  '**Beccaria** (1764) disse o contrário: **certeza > severidade**; e é melhor prevenir os crimes do que puni-los.',
  peg='Inverter certeza e severidade.',
  kw=['Beccaria', 'certeza da punição'])
I(P, 1, 'Origem da classificação',
  'A classificação da prevenção em primária, secundária e terciária foi importada pela Criminologia da medicina preventiva e da saúde pública.', 'C',
  'A tríade **primária, secundária e terciária** vem da **saúde pública** e foi adaptada à prevenção do crime.',
  kw=['saúde pública', 'primária, secundária e terciária'])
I(P, 1, 'Responsabilidade de todos',
  'No Estado Democrático de Direito, a segurança pública e a prevenção do crime são tarefa exclusiva das instâncias formais de controle, sem responsabilidade da sociedade.', 'E',
  'A Constituição diz que a segurança pública é **dever do Estado, direito e responsabilidade de todos** — a prevenção envolve a **comunidade**.',
  lei=[(CF + '144', 'A segurança pública, dever do Estado, direito e responsabilidade de todos', 'incolumidade das pessoas e do patrimônio', 'CF, art. 144, caput')],
  peg='Apagar a "responsabilidade de todos".',
  kw=['responsabilidade de todos', 'comunidade'])

# --- CRI-3.2 · Rodada 2
I(P, 2, 'Prevenção situacional',
  'A prevenção situacional busca reduzir as oportunidades do crime, aumentando o esforço e os riscos do infrator e reduzindo as recompensas da conduta.', 'C',
  'A **prevenção situacional** (Clarke) atua sobre a **oportunidade**: mais **esforço**, mais **risco**, menos **recompensa**.',
  kw=['prevenção situacional', 'oportunidades'])
I(P, 2, 'Deslocamento',
  'Crítica frequente à prevenção situacional é o deslocamento da criminalidade para outros locais, horários ou alvos.', 'C',
  'É o **efeito deslocamento**; a resposta dos defensores é a **difusão de benefícios** às áreas vizinhas.',
  kw=['deslocamento', 'difusão de benefícios'])
I(P, 2, 'Espaço defensável',
  'A teoria do espaço defensável, de Wilson e Kelling, relaciona o desenho arquitetônico ao controle natural do território pelos próprios moradores.', 'E',
  'O **espaço defensável** é de **Oscar Newman**; Wilson e Kelling são os autores das **janelas quebradas**. O conteúdo (desenho urbano, vigilância natural, território) está correto.',
  peg='Trocar o autor da teoria.',
  kw=['espaço defensável', 'Oscar Newman'])
I(P, 2, 'Lei e ordem no Estado Democrático',
  'No Estado Democrático de Direito, a política de lei e ordem e a tolerância zero irrestrita são os modelos preventivos ideais, pois a eficiência da repressão prevalece sobre as garantias.', 'E',
  'Garantias são **limite** da prevenção; políticas de **lei e ordem** são criticadas pela **seletividade** e pelo custo em direitos.',
  peg='Pôr a eficiência acima das garantias.',
  kw=['lei e ordem', 'garantias'])
I(P, 2, 'Policiamento comunitário',
  'O policiamento comunitário parte da parceria entre polícia e comunidade na identificação e na solução dos problemas locais de segurança.', 'C',
  '**Policiamento comunitário**: **parceria** e foco em **problemas** locais, não só em ocorrências.',
  kw=['policiamento comunitário', 'parceria'])

# ======================= CRI-3.3 · Prevenção primária =======================
P = 'DBA26-CRI-3.3'
I(P, 1, 'Conceito',
  'A prevenção primária dirige-se às raízes do conflito criminal, por meio de educação, emprego, moradia, saúde e qualidade de vida, e tem como destinatária a população em geral.', 'C',
  '**Primária**: atua nas **causas**, para **todos**, a **médio e longo prazo**.',
  kw=['prevenção primária', 'população em geral'])
I(P, 1, 'Prazo e destinatário',
  'A prevenção primária opera a curto prazo e dirige-se a grupos específicos de risco.', 'E',
  'Curto prazo e **grupos de risco** caracterizam a **secundária**. A **primária** é de **médio e longo prazo** e alcança **toda a população**.',
  peg='Trocar as características da primária pelas da secundária.',
  kw=['médio e longo prazo', 'grupos de risco'])
I(P, 1, 'Exemplos',
  'Políticas públicas de educação, emprego, saneamento e moradia são exemplos de prevenção primária.', 'C',
  'Políticas **sociais** gerais = **prevenção primária**.',
  kw=['políticas sociais', 'prevenção primária'])
I(P, 1, 'Limites práticos',
  'Considerada a forma mais genuína de prevenção, a primária produz resultados imediatos, a curto prazo, e com baixo custo.', 'E',
  'É a prevenção **mais genuína**, mas **lenta** (médio e **longo prazo**) e **cara** (exige prestações sociais) — por isso pouco atraente politicamente.',
  peg='Atribuir à primária resultado imediato.',
  kw=['mais genuína', 'longo prazo'])
I(P, 1, 'Presídios',
  'A construção de presídios é exemplo de prevenção primária.', 'E',
  'Presídio relaciona-se à população **condenada** — campo da **prevenção terciária**, não da primária.',
  peg='Classificar medida carcerária como primária.',
  kw=['prevenção terciária', 'presídios'])
I(P, 1, 'Direitos sociais',
  'A prevenção primária relaciona-se à efetivação de direitos sociais, como educação, saúde, trabalho, moradia e lazer.', 'C',
  'A **primária** concretiza os **direitos sociais** do art. 6º da Constituição.',
  lei=[(CF + '6', 'São direitos sociais a educação, a saúde', 'a assistência aos desamparados', 'CF, art. 6º')],
  kw=['direitos sociais', 'prevenção primária'])

# --- CRI-3.3 · Rodada 2
I(P, 2, 'Momento de atuação',
  'A prevenção primária atua no momento e no lugar em que o crime se manifesta ou se exterioriza.', 'E',
  'Atuar **onde e quando** o crime se manifesta é a **secundária**. A **primária** atua **antes**, nas **raízes**.',
  peg='Trocar o momento de atuação.',
  kw=['raízes', 'prevenção secundária'])
I(P, 2, 'Campanhas educativas',
  'Campanhas educativas de prevenção da violência doméstica voltadas ao público escolar e à sociedade em geral são exemplo de prevenção primária.', 'C',
  'Dirigem-se a **todos** e atuam na **cultura** — **prevenção primária**, prevista como diretriz da Lei Maria da Penha.',
  lei=[('L11340:8', 'V - a promoção e a realização de campanhas educativas de prevenção', 'voltadas ao público escolar e à sociedade em geral', 'Lei 11.340/2006, art. 8º, V')],
  kw=['campanhas educativas', 'prevenção primária'])
I(P, 2, 'Destinatário',
  'Na prevenção primária, o destinatário é o condenado.', 'E',
  'O **condenado** é destinatário da **terciária**; a **primária** dirige-se à **população em geral**.',
  peg='Trocar o destinatário.',
  kw=['população em geral', 'condenado'])
I(P, 2, 'Política social',
  'A prevenção primária parte da ideia de que o crime tem raízes sociais e exige política social de longo prazo, e não apenas política criminal.', 'C',
  'Prevenção primária é, sobretudo, **política social**.',
  kw=['política social', 'raízes sociais'])
I(P, 2, 'Objetivos constitucionais',
  'Erradicar a pobreza e a marginalização e reduzir as desigualdades sociais são objetivos fundamentais da República que dialogam com a prevenção primária.', 'C',
  'Os **objetivos fundamentais** do art. 3º, III, são o horizonte da **prevenção primária**.',
  lei=[(CF + '3', 'III - erradicar a pobreza e a marginalização', 'reduzir as desigualdades sociais e regionais;', 'CF, art. 3º, III')],
  kw=['erradicar a pobreza', 'prevenção primária'])

# ======================= CRI-3.4 · Prevenção secundária =======================
P = 'DBA26-CRI-3.4'
I(P, 1, 'Conceito',
  'A prevenção secundária atua mais tarde, onde e quando o crime se manifesta, a curto e médio prazo, e dirige-se a grupos e subgrupos que exibem maior risco.', 'C',
  '**Secundária**: **momento e lugar** do crime, **grupos de risco**, **curto e médio prazo**.',
  kw=['prevenção secundária', 'grupos de risco'])
I(P, 1, 'Policiamento em área de risco',
  'O reforço do policiamento ostensivo em área com alta incidência de roubos é exemplo de prevenção secundária.', 'C',
  'Atua **onde o crime aparece** — típico da **prevenção secundária**, ligada à ação policial.',
  kw=['policiamento ostensivo', 'prevenção secundária'])
I(P, 1, 'População reclusa',
  'A prevenção secundária dirige-se à população reclusa, visando evitar a reincidência.', 'E',
  'População **reclusa** e **reincidência** são campo da **terciária**.',
  peg='Trocar secundária por terciária.',
  kw=['prevenção terciária', 'reincidência'])
I(P, 1, 'Causas profundas',
  'A prevenção secundária atua sobre as causas profundas do crime, a longo prazo.', 'E',
  'Causas profundas e longo prazo são da **primária**. A **secundária** é **seletiva** e de **curto e médio prazo**.',
  peg='Trocar secundária por primária.',
  kw=['curto e médio prazo', 'prevenção primária'])
I(P, 1, 'Prevenção situacional como secundária',
  'Medidas de prevenção situacional, como iluminação e vigilância de áreas de risco, costumam ser classificadas como prevenção secundária.', 'C',
  'Atuam sobre **locais e oportunidades** concretas — em regra, **prevenção secundária**.',
  kw=['prevenção situacional', 'prevenção secundária'])
I(P, 1, 'Ordenação urbana',
  'A ordenação urbana e o controle dos espaços onde a criminalidade se concentra são instrumentos da prevenção terciária.', 'E',
  'São instrumentos da **prevenção secundária**, que usa **política policial**, **urbanística** e **legislativa** focadas nos locais de risco. A terciária cuida do condenado.',
  peg='Trocar secundária por terciária.',
  kw=['ordenação urbana', 'prevenção secundária'])

# --- CRI-3.4 · Rodada 2
I(P, 2, 'Seletividade da secundária',
  'A prevenção secundária liga-se à política legislativa e à ação policial e tem caráter seletivo, por concentrar-se em áreas e grupos.', 'C',
  'Por ser **focalizada**, a secundária é **seletiva** — e pode estigmatizar áreas e grupos.',
  kw=['seletivo', 'ação policial'])
I(P, 2, 'Egressos',
  'Programas de reinserção de egressos do sistema prisional configuram prevenção secundária.', 'E',
  'Egresso já passou pela pena: programa para ele é **prevenção terciária**.',
  peg='Classificar programa de egresso como secundária.',
  kw=['egressos', 'prevenção terciária'])
I(P, 2, 'Riscos',
  'Crítica dirigida à prevenção secundária é o risco de estigmatizar bairros e grupos e de apenas deslocar a criminalidade.', 'C',
  '**Estigmatização** e **deslocamento** são as críticas recorrentes à prevenção **focalizada**.',
  kw=['estigmatização', 'deslocamento'])
I(P, 2, 'Jovens em situação de risco',
  'Programas dirigidos a jovens em situação de risco em bairros com altos índices de violência configuram prevenção secundária.', 'C',
  'Destinatário é **grupo de risco** em **área de risco** — **secundária**.',
  kw=['jovens em situação de risco', 'prevenção secundária'])
I(P, 2, 'Momento',
  'A prevenção secundária atua após a condenação definitiva do infrator.', 'E',
  'Após a condenação atua a **terciária**. A **secundária** atua quando e onde o crime **se manifesta**, antes de qualquer condenação.',
  peg='Trocar o momento de atuação.',
  kw=['prevenção terciária', 'condenação'])

# ======================= CRI-3.5 · Prevenção terciária =======================
P = 'DBA26-CRI-3.5'
I(P, 1, 'Conceito',
  'A prevenção terciária tem como destinatária a população reclusa e busca evitar a reincidência.', 'C',
  '**Terciária**: **população presa/condenada**, objetivo de evitar a **reincidência**.',
  kw=['prevenção terciária', 'reincidência'])
I(P, 1, 'Destinatário',
  'A prevenção terciária tem como destinatária a população em geral.', 'E',
  'População em geral é destinatária da **primária**. A **terciária** dirige-se ao **condenado**.',
  peg='Trocar o destinatário.',
  kw=['condenado', 'população em geral'])
I(P, 1, 'Objetivo da execução',
  'A Lei de Execução Penal tem por objetivo efetivar as disposições da sentença e proporcionar condições para a harmônica integração social do condenado e do internado.', 'C',
  'O art. 1º da LEP traduz a **prevenção terciária**: **integração social**.',
  lei=[(LEP + '1', 'A execução penal tem por objetivo', 'harmônica integração social do condenado e do internado.', 'LEP, art. 1º')],
  kw=['harmônica integração social', 'prevenção terciária'])
I(P, 1, 'Assistência ao preso',
  'A assistência ao preso e ao internado é dever do Estado, objetivando prevenir o crime e orientar o retorno à convivência em sociedade.', 'C',
  'A LEP liga expressamente a **assistência** à **prevenção do crime** — prevenção terciária.',
  lei=[(LEP + '10', 'A assistência ao preso e ao internado é dever do Estado', 'orientar o retorno à convivência em sociedade.', 'LEP, art. 10, caput')],
  kw=['assistência ao preso', 'prevenir o crime'])
I(P, 1, 'Egresso',
  'A assistência ao preso prevista na Lei de Execução Penal não se estende ao egresso.', 'E',
  'Pelo parágrafo único do art. 10, a **assistência estende-se ao egresso**.',
  lei=[(LEP + '10', 'A assistência estende-se ao egresso.', None, 'LEP, art. 10, par. ún.')],
  peg='Negar a extensão ao egresso.',
  kw=['egresso', 'assistência'])
I(P, 1, 'Alcance',
  'A prevenção terciária é a de resultados mais amplos, pois atua na raiz do problema criminal.', 'E',
  'É o contrário: a **terciária** é **tardia, parcial e insuficiente** — atua depois do crime, sobre quem já foi condenado.',
  peg='Atribuir à terciária a virtude da primária.',
  kw=['tardia', 'insuficiente'])
I(P, 1, 'Remição',
  'O condenado em regime fechado ou semiaberto pode remir, por trabalho ou estudo, parte do tempo de execução, à razão de um dia de pena a cada doze horas de frequência escolar ou a cada três dias de trabalho.', 'C',
  'A **remição** é instrumento de prevenção terciária: **12 horas de estudo** ou **3 dias de trabalho** = 1 dia de pena.',
  lei=[(LEP + '126', 'O condenado que cumpre a pena em regime fechado ou semiaberto poderá remir', 'parte do tempo de execução da pena.', 'LEP, art. 126, caput'),
       (LEP + '126', 'II - 1 (um) dia de pena a cada 3 (três) dias de trabalho.', None, 'LEP, art. 126, § 1º, II')],
  kw=['remição', 'doze horas'])

# --- CRI-3.5 · Rodada 2
I(P, 2, 'Proporção da remição',
  'Na remição pelo trabalho, desconta-se um dia de pena a cada dois dias de trabalho.', 'E',
  'A proporção é **1 dia de pena a cada 3 dias de trabalho**.',
  lei=[(LEP + '126', 'II - 1 (um) dia de pena a cada 3 (três) dias de trabalho.', None, 'LEP, art. 126, § 1º, II')],
  peg='Trocar o número de dias.',
  kw=['3 dias de trabalho', 'remição'])
I(P, 2, 'Assistência ao egresso',
  'A assistência ao egresso inclui, se necessário, alojamento e alimentação em estabelecimento adequado pelo prazo de dois meses.', 'C',
  'Art. 25, II: **alojamento e alimentação** por **dois meses**, prorrogável **uma única vez** se comprovado o empenho na obtenção de emprego.',
  lei=[(LEP + '25', 'II - na concessão, se necessário, de alojamento e alimentação', 'pelo prazo de dois meses.', 'LEP, art. 25, II')],
  kw=['egresso', 'dois meses'])
I(P, 2, 'Caráter',
  'A prevenção terciária, por ser posterior ao crime, tem caráter punitivo e é marcada por intervenção tardia, parcial e insuficiente, por não incidir nas causas do delito.', 'C',
  '**Terciária**: **punitiva**, **tardia**, **parcial** e **insuficiente** — expressões consagradas na doutrina.',
  kw=['tardia, parcial e insuficiente', 'caráter punitivo'])
I(P, 2, 'Classificação dos condenados',
  'Os condenados serão classificados segundo seus antecedentes e personalidade, para orientar a individualização da execução penal.', 'C',
  'A **classificação** (art. 5º da LEP) orienta a **individualização da execução** — ferramenta da Criminologia clínica.',
  lei=[(LEP + '5', 'Os condenados serão classificados', 'individualização da execução penal.', 'LEP, art. 5º')],
  kw=['classificação', 'individualização da execução'])
I(P, 2, 'Comunidade na execução',
  'A Lei de Execução Penal veda a participação da comunidade nas atividades de execução, atribuindo-as exclusivamente ao Estado.', 'E',
  'O art. 4º manda o Estado **recorrer à cooperação da comunidade** na execução da pena e da medida de segurança.',
  lei=[(LEP + '4', 'O Estado deverá recorrer à cooperação da comunidade', 'medida de segurança.', 'LEP, art. 4º')],
  peg='Trocar "deverá recorrer" por "veda".',
  kw=['cooperação da comunidade', 'execução penal'])

# ======================= CRI-3.6 · Modelos de reação ao crime =======================
P = 'DBA26-CRI-3.6'
I(P, 1, 'Os três modelos',
  'A doutrina identifica três modelos de reação ao crime: o dissuasório (clássico), o ressocializador e o integrador (restaurativo ou consensual).', 'C',
  'Os três modelos: **dissuasório**, **ressocializador** e **integrador/restaurativo**.',
  kw=['dissuasório', 'ressocializador'])
I(P, 1, 'Modelo dissuasório',
  'No modelo dissuasório, a resposta ao crime é a pena intimidatória, voltada à prevenção geral, e os protagonistas são a vítima e a comunidade, com o Estado à margem.', 'E',
  'O **dissuasório** aposta na **intimidação**, e os protagonistas são o **Estado** e o **infrator**; a **vítima** e a comunidade ficam à margem.',
  peg='Inverter os protagonistas do modelo.',
  kw=['modelo dissuasório', 'intimidação'])
I(P, 1, 'Modelo ressocializador',
  'No modelo ressocializador, o foco é a punição exemplar como meio de intimidar a coletividade.', 'E',
  'Intimidar a coletividade é o **dissuasório**. O **ressocializador** busca a **intervenção positiva** no condenado (**prevenção especial**).',
  peg='Trocar o modelo ressocializador pelo dissuasório.',
  kw=['ressocializador', 'prevenção especial'])
I(P, 1, 'Ressocialização',
  'O modelo ressocializador volta-se à intervenção positiva no condenado, para reinseri-lo na sociedade, e corresponde à prevenção especial positiva.', 'C',
  '**Ressocializador** = **prevenção especial positiva**, expressa na LEP.',
  kw=['ressocializador', 'prevenção especial positiva'])
I(P, 1, 'Modelo integrador',
  'O modelo integrador, ou restaurativo, busca a reparação do dano e a pacificação do conflito, com participação da vítima, do infrator e da comunidade.', 'C',
  'O **integrador** devolve o conflito às partes: **reparação**, **conciliação** e **participação**.',
  kw=['modelo integrador', 'reparação do dano'])
I(P, 1, 'Justiça consensual nos Juizados',
  'O processo perante o Juizado Especial Criminal objetiva, sempre que possível, a reparação dos danos sofridos pela vítima e a aplicação de pena não privativa de liberdade.', 'C',
  'A Lei 9.099/1995 é expressão do modelo **consensual/integrador**: **reparação** e **pena não privativa**.',
  lei=[(JEC + '62', 'O processo perante o Juizado Especial orientar-se-á', 'aplicação de pena não privativa de liberdade.', 'Lei 9.099/1995, art. 62')],
  kw=['reparação dos danos', 'pena não privativa de liberdade'])
I(P, 1, 'Composição civil',
  'Na Lei 9.099/1995, o acordo de composição dos danos civis homologado, nos crimes de ação privada ou pública condicionada à representação, não afeta o direito de queixa ou representação.', 'E',
  'O acordo homologado **acarreta a renúncia** ao direito de queixa ou representação — a reparação encerra o conflito penal.',
  lei=[(JEC + '74', 'Tratando-se de ação penal de iniciativa privada', 'renúncia ao direito de queixa ou representação.', 'Lei 9.099/1995, art. 74, par. ún.')],
  peg='Negar o efeito de renúncia.',
  kw=['composição dos danos civis', 'renúncia'])

# --- CRI-3.6 · Rodada 2
I(P, 2, 'Vítima no modelo integrador',
  'No modelo integrador, a vítima é mera informante, sem participação no desfecho do conflito.', 'E',
  'No **integrador**, a vítima é **protagonista**: participa da solução e da **reparação**.',
  peg='Negar o protagonismo da vítima.',
  kw=['protagonista', 'modelo integrador'])
I(P, 2, 'Transação penal e reincidência',
  'A pena restritiva de direitos ou multa aplicada em transação penal importa reincidência.', 'E',
  'A transação **não importa reincidência**; só é registrada para impedir o mesmo benefício em **cinco anos**.',
  lei=[(JEC + '76', 'Acolhendo a proposta do Ministério Público aceita pelo autor da infração', 'no prazo de cinco anos.', 'Lei 9.099/1995, art. 76, § 4º')],
  peg='Atribuir reincidência à transação.',
  kw=['transação penal', 'não importará em reincidência'])
I(P, 2, 'Crise da ressocialização',
  'O modelo ressocializador entrou em crise a partir dos anos 1970, com pesquisas que questionaram a eficácia dos programas de tratamento, sintetizadas na expressão "nada funciona".', 'C',
  'O "**nothing works**" (Martinson, 1974) marcou a **crise do ideal ressocializador**, sem eliminá-lo.',
  kw=['nada funciona', 'crise do ideal ressocializador'])
I(P, 2, 'Reparação na suspensão do processo',
  'Na suspensão condicional do processo, a reparação do dano, salvo impossibilidade de fazê-lo, é condição imposta ao acusado.', 'C',
  'A **reparação do dano** é condição legal do **sursis processual** — traço integrador da Lei 9.099/1995.',
  lei=[(JEC + '89', 'I - reparação do dano, salvo impossibilidade de fazê-lo;', None, 'Lei 9.099/1995, art. 89, § 1º, I')],
  kw=['reparação do dano', 'suspensão condicional do processo'])
I(P, 2, 'Vítima no modelo dissuasório',
  'O modelo dissuasório clássico confere protagonismo à vítima, pois a pena se volta à reparação do dano.', 'E',
  'No **dissuasório**, a vítima fica **neutralizada**; a pena volta-se à **intimidação**, não à reparação.',
  peg='Atribuir ao dissuasório a marca do integrador.',
  kw=['modelo dissuasório', 'neutralização da vítima'])
I(P, 2, 'Acordo de não persecução penal',
  'Entre as condições do acordo de não persecução penal está reparar o dano ou restituir a coisa à vítima, exceto na impossibilidade de fazê-lo.', 'C',
  'O **ANPP** incorpora a **reparação** à vítima — lógica de justiça **negociada** e integradora.',
  lei=[('CPP:28-A', 'I - reparar o dano ou restituir a coisa à vítima, exceto na impossibilidade de fazê-lo;', None, 'CPP, art. 28-A, I')],
  kw=['acordo de não persecução penal', 'reparar o dano'])
