# Pente Fino de Direito Penal (Parte Geral) — PEN-1 (introdução, 1.1 a 1.4) e PEN-2 (a lei penal, 2.1 a 2.5) (08/11/2026).
from base import I
from pen_juris import J

CP = 'CP:'
CF = 'CF:'
LEG = (CF + '5', 'não há crime sem lei anterior que o defina, nem pena sem prévia cominação legal', None, 'CF, art. 5º, XXXIX')
LEG_CP = (CP + '1', 'Não há crime sem lei anterior que o defina. Não há pena sem prévia cominação legal.', None, 'CP, art. 1º')
RETRO = (CF + '5', 'a lei penal não retroagirá, salvo para beneficiar o réu', None, 'CF, art. 5º, XL')
UNIAO = (CF + '22', 'Compete privativamente à União legislar sobre', 'penal, processual', 'CF, art. 22, I')
MP = (CF + '62', 'É vedada a edição de medidas provisórias sobre matéria', 'direito penal, processual penal e processual civil', 'CF, art. 62, § 1º, I, b')

# ======================= PEN-1 · Introdução ao direito penal =======================
P = 'DBA26-PEN-1'
I(P, 1, 'Competência legislativa penal',
  'Compete privativamente à União legislar sobre direito penal, o que impede Estados e Municípios de criar crimes e cominar penas.', 'C',
  'É a **competência privativa da União** (CF, art. 22, I). Lei estadual que cria tipo penal é formalmente inconstitucional; a delegação por lei complementar (art. 22, par. ún.) só alcança questões específicas.',
  lei=[UNIAO], kw=['competência privativa da União', 'direito penal'])
I(P, 1, 'Medida provisória',
  'Medida provisória pode criar tipo penal em caso de relevância e urgência, desde que convertida em lei pelo Congresso Nacional.', 'E',
  'A EC 32/2001 **vedou medida provisória** sobre direito penal (CF, art. 62, § 1º, I, b). A conversão posterior não convalida a incriminação feita por MP.',
  lei=[MP], peg='Trocar "vedada" por "admitida se convertida em lei".', kw=['vedou medida provisória', 'direito penal'])
I(P, 1, 'Direito penal objetivo e subjetivo',
  'Direito penal subjetivo é o conjunto de normas que definem infrações e cominam sanções; direito penal objetivo é o poder de punir do Estado.', 'E',
  'Inverteu: o **direito penal objetivo** é o conjunto de normas; o **subjetivo** é o ius puniendi, limitado pela legalidade (CF, art. 5º, XXXIX).',
  lei=[LEG], kw=['direito penal objetivo', 'ius puniendi'])
I(P, 1, 'Direito penal do autor',
  'O ordenamento brasileiro adota o direito penal do autor, punindo a pessoa pelo que ela é ou pelo seu modo de vida, e não pelo fato praticado.', 'E',
  'O Brasil adota o **direito penal do fato**: pune-se a conduta descrita em lei (CF, art. 5º, XXXIX). Circunstâncias pessoais só modulam a pena (art. 59), nunca fundamentam a incriminação.',
  lei=[LEG, (CP + '59', 'O juiz, atendendo à culpabilidade, aos antecedentes', None, 'CP, art. 59, caput')],
  peg='Confundir a individualização da pena (que olha o autor) com o fundamento da punição (o fato).', kw=['direito penal do fato'])
I(P, 1, 'Regras gerais e legislação especial',
  'As regras gerais do Código Penal aplicam-se aos fatos incriminados por lei especial, se esta não dispuser de modo diverso.', 'C',
  'É o **princípio da especialidade** na relação CP × leis extravagantes: o art. 12 manda aplicar a Parte Geral **subsidiariamente**.',
  lei=[(CP + '12', 'As regras gerais deste Código aplicam-se aos fatos incriminados por lei especial', None, 'CP, art. 12')],
  kw=['subsidiariamente', 'lei especial'])
# --- PEN-1 · Rodada 2
I(P, 2, 'Contravenção e regras gerais',
  'As regras gerais do Código Penal não se aplicam às contravenções penais, que têm parte geral própria e completa na Lei das Contravenções.', 'E',
  'A LCP manda aplicar às contravenções as **regras gerais do CP**, salvo disposição diversa (DL 3.688/1941, art. 1º). Ela só tem regras próprias pontuais (ex.: tentativa não punível, art. 4º).',
  lei=[('DL3688:1', 'Aplicam-se as contravenções às regras gerais do Código Penal', None, 'LCP, art. 1º'),
       ('DL3688:4', 'Não é punível a tentativa de contravenção.', None, 'LCP, art. 4º')],
  kw=['regras gerais do CP', 'contravenções'])
I(P, 2, 'Delegação aos Estados',
  'Lei ordinária federal pode autorizar os Estados a legislar sobre questões específicas de direito penal.', 'E',
  'O parágrafo único do art. 22 da CF exige **lei complementar** para delegar **questões específicas** aos Estados.',
  lei=[(CF + '22', 'Lei complementar poderá autorizar os Estados a legislar sobre questões específicas', None, 'CF, art. 22, par. ún.')],
  kw=['lei complementar', 'questões específicas'])
I(P, 2, 'Lei penal em branco e competência',
  'Na norma penal em branco heterogênea, o complemento pode vir de ato administrativo federal, como a portaria que lista as substâncias tidas por drogas.', 'C',
  'Na **norma penal em branco heterogênea** (em sentido estrito) o complemento tem fonte diversa da lei: a Lei de Drogas remete à lista do Poder Executivo da União. O núcleo do tipo continua em lei federal (CF, art. 22, I).',
  lei=[UNIAO, ('L11343:1', 'consideram-se como drogas as substâncias ou os produtos capazes de causar dependência', None, 'Lei 11.343/2006, art. 1º, par. ún.')],
  kw=['norma penal em branco heterogênea', 'complemento'])

# ======================= PEN-1.1 · Conceito, caracteres e função =======================
P = 'DBA26-PEN-1.1'
I(P, 1, 'Conceito formal',
  'Sob o aspecto formal, direito penal é o conjunto de comportamentos socialmente danosos que lesam bens jurídicos relevantes, independentemente de previsão legal.', 'E',
  'Isso mistura o conceito **material** com uma negação da legalidade. O **conceito formal** é o conjunto de normas que qualificam comportamentos como infrações e cominam sanções — e nada é crime sem lei (CF, art. 5º, XXXIX).',
  lei=[LEG], kw=['conceito formal', 'infrações penais'])
I(P, 1, 'Caráter fragmentário',
  'O direito penal tem caráter fragmentário, pois protege todos os bens jurídicos contra todas as formas de lesão.', 'E',
  'É o contrário: **fragmentariedade** significa que o direito penal protege só **parte** dos bens jurídicos (os mais relevantes) e só contra os ataques mais graves. A doutrina extrai a ideia da legalidade e da intervenção mínima.',
  lei=[LEG], peg='Inverter a fragmentariedade ("todos os bens, todas as lesões").', kw=['fragmentariedade', 'parte dos bens jurídicos'])
I(P, 1, 'Caráter público',
  'O direito penal é ramo do direito público, porque o ius puniendi é monopólio do Estado, ainda que em certos crimes a iniciativa da ação penal caiba ao ofendido.', 'C',
  'Mesmo na **ação privada** o ofendido só tem o direito de acusar (ius accusationis); o **direito de punir** continua estatal. A ação é, em regra, pública (CP, art. 100).',
  lei=[(CP + '100', 'A ação penal é pública, salvo quando a lei expressamente a declara privativa do ofendido.', None, 'CP, art. 100, caput')],
  kw=['direito público', 'ius puniendi'])
I(P, 1, 'Função de proteção de bens jurídicos',
  'Para a doutrina majoritária, a missão mediata do direito penal é a proteção de bens jurídicos, e não a mera proteção da vigência da norma.', 'C',
  'Corrente dominante (funcionalismo teleológico): o direito penal existe para **proteger bens jurídicos** essenciais. A proteção da **vigência da norma** é a tese do funcionalismo sistêmico, minoritária. No CP, o fim da pena é "reprovação e prevenção" (art. 59).',
  lei=[(CP + '59', 'conforme seja necessário e suficiente para reprovação e prevenção do crime', None, 'CP, art. 59, caput')],
  kw=['proteger bens jurídicos', 'vigência da norma'])
I(P, 1, 'Caráter sancionador',
  'O direito penal tem caráter exclusivamente constitutivo, nunca protegendo bens jurídicos já tutelados por outros ramos do direito.', 'E',
  'A doutrina predominante vê o direito penal como **predominantemente sancionador**: reforça a tutela de bens já protegidos por outros ramos (patrimônio, administração), e só excepcionalmente é **constitutivo** (protege bem sem tutela anterior).',
  lei=[UNIAO], peg='Trocar "predominantemente sancionador" por "exclusivamente constitutivo".', kw=['predominantemente sancionador', 'constitutivo'])
I(P, 1, 'Função de garantia',
  'O direito penal tem também função de garantia, pois a lei que define o crime limita o poder punitivo e assegura ao cidadão que só será punido pelo que nela estiver previsto.', 'C',
  'É a **função de garantia** (a lei penal como "Magna Carta do delinquente"): reserva legal e anterioridade (CF, art. 5º, XXXIX; CP, art. 1º).',
  lei=[LEG_CP], kw=['função de garantia', 'reserva legal'])
I(P, 1, 'Responsabilidade penal da pessoa jurídica',
  'A Constituição não admite a responsabilidade penal da pessoa jurídica em hipótese alguma, pois o direito penal se dirige apenas a pessoas físicas.', 'E',
  'A CF prevê sanções **penais** à pessoa jurídica por condutas lesivas ao **meio ambiente** (art. 225, § 3º), e a Lei 9.605/1998 as regula (art. 3º).',
  lei=[(CF + '225', 'As condutas e atividades consideradas lesivas ao meio ambiente sujeitarão os infratores', None, 'CF, art. 225, § 3º'),
       ('L9605:3', 'As pessoas jurídicas serão responsabilizadas administrativa, civil e penalmente', None, 'Lei 9.605/1998, art. 3º, caput')],
  peg='Negar a previsão expressa nos crimes ambientais.', kw=['meio ambiente', 'pessoa jurídica'])
# --- PEN-1.1 · Rodada 2
I(P, 2, 'Pessoa jurídica: dupla imputação',
  'Pela letra da Lei 9.605/1998, a responsabilidade penal da pessoa jurídica não exclui a das pessoas físicas autoras, coautoras ou partícipes do mesmo fato.', 'C',
  'É o **parágrafo único do art. 3º**: as duas responsabilidades convivem. A letra da lei não condiciona a denúncia da pessoa jurídica à da pessoa física.',
  lei=[('L9605:3', 'A responsabilidade das pessoas jurídicas não exclui a das pessoas físicas', None, 'Lei 9.605/1998, art. 3º, par. ún.')],
  kw=['não exclui', 'pessoas físicas'])
I(P, 2, 'Pessoa jurídica: requisitos legais',
  'Para a Lei 9.605/1998, basta que a infração ambiental seja cometida por qualquer empregado da empresa para que a pessoa jurídica responda penalmente.', 'E',
  'A lei exige que a infração seja cometida **por decisão do representante legal ou contratual, ou do órgão colegiado**, e **no interesse ou benefício** da entidade (art. 3º, caput).',
  lei=[('L9605:3', 'nos casos em que a infração seja cometida por decisão de seu representante legal', 'no interesse ou benefício da sua entidade', 'Lei 9.605/1998, art. 3º, caput')],
  peg='Apagar os dois requisitos (decisão do representante + interesse da entidade).', kw=['por decisão', 'interesse ou benefício'])
I(P, 2, 'Direito penal subterrâneo',
  'A expressão "direito penal subterrâneo" designa o exercício arbitrário e ilegal do poder punitivo por agências estatais, como execuções e torturas, à margem da lei.', 'C',
  'Conceito da criminologia crítica: o **sistema penal subterrâneo** atua fora da legalidade (CF, art. 5º, XXXIX), em oposição ao sistema penal formal; o "paralelo" é o exercido por agências não penais.',
  lei=[LEG], kw=['sistema penal subterrâneo'])
I(P, 2, 'Velocidades do direito penal',
  'Na classificação das velocidades do direito penal, a segunda velocidade admite a flexibilização de garantias em troca de penas alternativas à prisão, como ocorre com os institutos despenalizadores da Lei 9.099/1995.', 'C',
  'Doutrina: **1ª velocidade** = prisão com todas as garantias; **2ª** = penas não privativas com garantias flexibilizadas (ex.: transação penal); **3ª** = prisão com garantias reduzidas (direito penal do inimigo).',
  lei=[('L9099:61', 'Consideram-se infrações penais de menor potencial ofensivo', None, 'Lei 9.099/1995, art. 61')],
  kw=['segunda velocidade', 'penas alternativas'])

# ======================= PEN-1.2 · Princípios =======================
P = 'DBA26-PEN-1.2'
I(P, 1, 'Legalidade: reserva legal e anterioridade',
  'Não há crime sem lei anterior que o defina, nem pena sem prévia cominação legal, garantia que abrange tanto a reserva legal quanto a anterioridade.', 'C',
  'O art. 5º, XXXIX, da CF (repetido no art. 1º do CP) traz a **reserva legal** (só lei em sentido estrito cria crime) e a **anterioridade** (a lei tem de ser anterior ao fato).',
  lei=[LEG, LEG_CP], kw=['reserva legal', 'anterioridade'])
I(P, 1, 'Pessoalidade da pena',
  'Nenhuma pena passará da pessoa do condenado, razão pela qual nem a obrigação de reparar o dano pode ser estendida aos sucessores.', 'E',
  'A **intranscendência** proíbe que a **pena** passe do condenado, mas a **obrigação de reparar o dano** e o **perdimento de bens** podem ser estendidos aos sucessores até o limite do patrimônio transferido (CF, art. 5º, XLV).',
  lei=[(CF + '5', 'nenhuma pena passará da pessoa do condenado', 'até o limite do valor do patrimônio transferido', 'CF, art. 5º, XLV')],
  peg='Estender a intranscendência aos efeitos civis.', kw=['intranscendência', 'reparar o dano'])
I(P, 1, 'Humanidade das penas',
  'A Constituição veda, sem exceção, a pena de morte, as penas de caráter perpétuo, de trabalhos forçados, de banimento e cruéis.', 'E',
  'A vedação da **pena de morte** tem exceção: **guerra declarada**, nos termos do art. 84, XIX (CF, art. 5º, XLVII, a). As demais (perpétua, trabalhos forçados, banimento, cruéis) não têm ressalva.',
  lei=[(CF + '5', 'não haverá penas:', 'cruéis', 'CF, art. 5º, XLVII')],
  exc=['Pena de morte em caso de guerra declarada (CF, art. 5º, XLVII, a)'],
  peg='"Sem exceção" — esquecer a guerra declarada.', kw=['pena de morte', 'guerra declarada'])
I(P, 1, 'Insignificância: vetores',
  'Para o STF, a aplicação do princípio da insignificância exige a mínima ofensividade da conduta, a nenhuma periculosidade social da ação, o reduzidíssimo grau de reprovabilidade do comportamento e a inexpressividade da lesão jurídica.', 'C',
  'São os **quatro vetores** fixados no HC 84.412 e reiterados desde então. A insignificância afasta a **tipicidade material**.',
  juris=[J['HC84412']], kw=['quatro vetores', 'tipicidade material'])
I(P, 1, 'Insignificância e administração pública',
  'Segundo súmula do STJ, o princípio da insignificância é aplicável aos crimes contra a administração pública quando o prejuízo ao erário for inferior a um salário mínimo.', 'E',
  'A **Súmula 599/STJ** diz que a insignificância é **inaplicável** aos crimes contra a administração pública, sem ressalva de valor (o bem protegido é também a moralidade administrativa).',
  juris=[J['S599']], peg='Inventar um teto de valor para a administração pública.', kw=['Súmula 599/STJ', 'inaplicável'])
I(P, 1, 'Insignificância e violência doméstica',
  'É inaplicável o princípio da insignificância aos crimes ou contravenções praticados contra a mulher no âmbito das relações domésticas.', 'C',
  'É a **Súmula 589/STJ**. Pelo mesmo fundamento, a Súmula 588/STJ veda a substituição por restritiva de direitos quando houver violência ou grave ameaça.',
  juris=[J['S589']], kw=['Súmula 589/STJ', 'relações domésticas'])
I(P, 1, 'Individualização da pena',
  'A individualização da pena ocorre apenas no momento judicial da dosimetria, não alcançando a cominação legal nem a execução.', 'E',
  'A **individualização da pena** (CF, art. 5º, XLVI) se dá em **três fases**: cominação (legislativa), aplicação (judicial, arts. 59 e 68 do CP) e execução (LEP).',
  lei=[(CF + '5', 'a lei regulará a individualização da pena', None, 'CF, art. 5º, XLVI')],
  kw=['individualização da pena', 'três fases'])
# --- PEN-1.2 · Rodada 2
I(P, 2, 'Insignificância e restituição do bem',
  'A restituição imediata e integral do bem furtado à vítima basta, por si só, para que se reconheça o princípio da insignificância.', 'E',
  'Tese do **Tema 1.205/STJ**: a restituição imediata e integral **não basta, por si só**. Os vetores do STF continuam a ser examinados no caso concreto.',
  juris=[J['T1205']], peg='Transformar a devolução do bem em causa automática de atipicidade.', kw=['Tema 1.205/STJ', 'não basta, por si só'])
I(P, 2, 'Insignificância e sinal clandestino de internet',
  'Não se aplica o princípio da insignificância à transmissão clandestina de sinal de internet via radiofrequência.', 'C',
  'É a **Súmula 606/STJ** (art. 183 da Lei 9.472/1997): o perigo à segurança das telecomunicações afasta a irrelevância.',
  juris=[J['S606']], kw=['Súmula 606/STJ', 'radiofrequência'])
I(P, 2, 'Legalidade e medida de segurança',
  'Por não ser pena, a medida de segurança não se submete ao princípio da legalidade, podendo ser imposta por analogia.', 'E',
  'A doutrina estende a **legalidade** à medida de segurança, espécie de **sanção penal**: só se aplica nas hipóteses e formas da lei (CP, art. 96 e seguintes). E o STJ limita sua duração ao máximo da pena cominada (Súmula 527/STJ).',
  lei=[(CP + '96', 'As medidas de segurança são:', None, 'CP, art. 96, caput')], juris=[J['S527']],
  peg='Afastar a legalidade porque "medida de segurança não é pena".', kw=['legalidade', 'sanção penal'])
I(P, 2, 'Taxatividade',
  'O princípio da legalidade contenta-se com a existência de lei anterior, admitindo tipos penais vagos desde que o juiz os concretize no caso.', 'E',
  'A **taxatividade** (lex certa) veda tipos vagos e indeterminados; ao lado dela estão lex scripta, lex stricta e lex praevia (CF, art. 5º, XXXIX).',
  lei=[LEG], kw=['taxatividade', 'lex certa'])
I(P, 2, 'Culpabilidade e responsabilidade objetiva',
  'Pelo resultado que agrava especialmente a pena, responde o agente ainda que não o tenha causado nem culposamente, bastando o nexo causal.', 'E',
  'O art. 19 do CP exige que o resultado agravador tenha sido causado **ao menos culposamente** — é o princípio da culpabilidade vedando a **responsabilidade penal objetiva**.',
  lei=[(CP + '19', 'Pelo resultado que agrava especialmente a pena, só responde o agente que o houver causado ao menos culposamente.', None, 'CP, art. 19')],
  peg='Bastar o nexo causal (versari in re illicita).', kw=['ao menos culposamente', 'responsabilidade penal objetiva'])

# ======================= PEN-1.3 · Relações com outros ramos =======================
P = 'DBA26-PEN-1.3'
I(P, 1, 'Direito penal e direito constitucional',
  'A Constituição é fonte de limites ao direito penal e também traz mandados expressos de criminalização, como o do racismo.', 'C',
  'A CF limita (legalidade, humanidade) e ordena criminalizar: **racismo** (art. 5º, XLII), tortura, tráfico, terrorismo e hediondos (XLIII), ação de grupos armados (XLIV).',
  lei=[(CF + '5', 'a prática do racismo constitui crime inafiançável e imprescritível', None, 'CF, art. 5º, XLII')],
  kw=['mandados expressos de criminalização', 'racismo'])
I(P, 1, 'Direito penal e direito civil: reparação',
  'A sentença penal condenatória não produz efeito na esfera civil, de modo que a vítima precisa provar novamente o fato e a autoria no juízo cível.', 'E',
  'Tornar certa a **obrigação de indenizar** é efeito genérico da condenação (CP, art. 91, I): a sentença é **título executivo** no cível, discutindo-se lá só o valor.',
  lei=[(CP + '91', 'tornar certa a obrigação de indenizar o dano causado pelo crime', None, 'CP, art. 91, I')],
  peg='Negar a eficácia civil da condenação penal.', kw=['obrigação de indenizar', 'título executivo'])
I(P, 1, 'Direito penal e direito processual',
  'O direito processual penal é o instrumento de realização do direito penal: não há pena sem o devido processo legal.', 'C',
  'Relação de **instrumentalidade**: a pena só se impõe por processo (CF, art. 5º, LIV). A competência para legislar sobre ambos é da União (art. 22, I).',
  lei=[(CF + '5', 'ninguém será privado da liberdade ou de seus bens sem o devido processo legal', None, 'CF, art. 5º, LIV'), UNIAO],
  kw=['instrumentalidade', 'devido processo legal'])
I(P, 1, 'Direito penal e direito administrativo',
  'Sanções administrativas e penais pelo mesmo fato são incompatíveis, de modo que a punição disciplinar do servidor impede a ação penal.', 'E',
  'Vigora a **independência das instâncias**: o mesmo fato pode gerar sanção administrativa, civil e penal. A própria Lei 9.605/1998 fala em responsabilidade "administrativa, civil e penalmente" (art. 3º).',
  lei=[('L9605:3', 'As pessoas jurídicas serão responsabilizadas administrativa, civil e penalmente', None, 'Lei 9.605/1998, art. 3º, caput')],
  peg='Ver bis in idem entre instâncias diferentes.', kw=['independência das instâncias'])
I(P, 1, 'Direito penal e execução',
  'A execução penal tem por objetivo exclusivo efetivar as disposições da sentença, sem preocupação legal com a integração social do condenado.', 'E',
  'O art. 1º da **LEP** soma à efetivação da sentença o objetivo de proporcionar a harmônica **integração social** do condenado e do internado.',
  lei=[('L7210:1', 'A execução penal tem por objetivo efetivar as disposições de sentença ou decisão criminal', None, 'LEP, art. 1º')],
  kw=['LEP', 'integração social'])
# --- PEN-1.3 · Rodada 2
I(P, 2, 'Direito penal e direito internacional',
  'A lei brasileira se aplica ao crime cometido no território nacional sem prejuízo de convenções, tratados e regras de direito internacional.', 'C',
  'É a **territorialidade temperada** do art. 5º do CP: tratados e regras internacionais (ex.: imunidades diplomáticas) podem afastar a lei brasileira.',
  lei=[(CP + '5', 'Aplica-se a lei brasileira, sem prejuízo de convenções, tratados e regras de direito internacional', None, 'CP, art. 5º, caput')],
  kw=['territorialidade temperada', 'tratados'])
I(P, 2, 'Sentença estrangeira e efeitos civis',
  'A sentença penal estrangeira pode ser homologada no Brasil para obrigar o condenado à reparação do dano, desde que haja pedido da parte interessada.', 'C',
  'Art. 9º, I, e par. ún., a, do CP: para **efeitos civis**, basta o **pedido da parte interessada**; para medida de segurança, exige-se tratado de extradição ou requisição do Ministro da Justiça.',
  lei=[(CP + '9', 'obrigar o condenado à reparação do dano', None, 'CP, art. 9º, I'),
       (CP + '9', 'para os efeitos previstos no inciso I, de pedido da parte interessada', None, 'CP, art. 9º, par. ún., a')],
  kw=['efeitos civis', 'pedido da parte interessada'])
I(P, 2, 'Direito penal e ECA',
  'Os menores de 18 anos que praticam fato descrito como crime respondem pelo Código Penal com pena reduzida, por serem relativamente imputáveis.', 'E',
  'Os menores de 18 são **penalmente inimputáveis** e sujeitos à **legislação especial** — o ECA, com medidas socioeducativas (CF, art. 228; CP, art. 27). Não há "pena reduzida".',
  lei=[(CF + '228', 'São penalmente inimputáveis os menores de dezoito anos', None, 'CF, art. 228'),
       (CP + '27', 'Os menores de 18 (dezoito) anos são penalmente inimputáveis', None, 'CP, art. 27')],
  peg='Tratar o adolescente como semi-imputável.', kw=['penalmente inimputáveis', 'legislação especial'])

# ======================= PEN-1.4 · Direito penal e política criminal =======================
P = 'DBA26-PEN-1.4'
I(P, 1, 'Conceito de política criminal',
  'Política criminal é o conjunto de estratégias e escolhas do Estado para prevenir e reagir ao crime, orientando a criação, a reforma e a aplicação das leis penais.', 'C',
  'Na tríade das ciências penais: a **criminologia** estuda o fenômeno (ser), a **política criminal** propõe as estratégias (valoração) e a **dogmática penal** interpreta o direito posto. O legislador as concretiza na cominação (CF, art. 5º, XLVI).',
  lei=[(CF + '5', 'a lei regulará a individualização da pena', None, 'CF, art. 5º, XLVI')],
  kw=['política criminal', 'criminologia'])
I(P, 1, 'Despenalização',
  'A Lei 9.099/1995, ao criar a transação penal e a composição civil para as infrações de menor potencial ofensivo, promoveu a descriminalização dessas condutas.', 'E',
  'Houve **despenalização** (medidas que evitam a pena de prisão), não **descriminalização**: o fato continua crime. São de menor potencial as contravenções e os crimes com pena máxima até 2 anos (art. 61).',
  lei=[('L9099:61', 'as contravenções penais e os crimes a que a lei comine pena máxima não superior a 2 (dois) anos', None, 'Lei 9.099/1995, art. 61')],
  peg='Confundir despenalização com descriminalização.', kw=['despenalização', 'descriminalização'])
I(P, 1, 'Porte de droga para consumo',
  'A Lei 11.343/2006 comina pena de detenção ao porte de drogas para consumo pessoal, substituível por advertência.', 'E',
  'O art. 28 **não comina prisão**: prevê **advertência**, prestação de serviços e medida educativa — exemplo de **despenalização**.',
  lei=[('L11343:28', 'Quem adquirir, guardar, tiver em depósito, transportar ou trouxer consigo, para consumo pessoal', 'medida educativa de comparecimento a programa ou curso educativo', 'Lei 11.343/2006, art. 28, caput')],
  kw=['advertência', 'despenalização'])
I(P, 1, 'Mandado de criminalização e omissão',
  'A Constituição determina que a lei considere inafiançáveis e insuscetíveis de graça ou anistia a tortura, o tráfico ilícito de entorpecentes, o terrorismo e os crimes hediondos.', 'C',
  'É o **mandado de criminalização** do art. 5º, XLIII, com a responsabilização de mandantes, executores e de quem, podendo evitar, se omitir.',
  lei=[(CF + '5', 'a lei considerará crimes inafiançáveis e insuscetíveis de graça ou anistia', None, 'CF, art. 5º, XLIII')],
  kw=['mandado de criminalização', 'insuscetíveis de graça ou anistia'])
I(P, 1, 'Hediondos e indulto',
  'Por política criminal, a Lei 8.072/1990 proíbe para os crimes hediondos a anistia, a graça e a fiança, mas admite expressamente o indulto.', 'E',
  'A Lei 8.072/1990 veda **anistia, graça e indulto** (art. 2º, I) e **fiança** (II). A CF só fala em graça e anistia, mas a lei foi além e incluiu o indulto.',
  lei=[('L8072:2', 'Os crimes hediondos, a prática da tortura, o tráfico ilícito de entorpecentes e drogas afins e o terrorismo são insuscetíveis de', 'anistia, graça e indulto', 'Lei 8.072/1990, art. 2º, I')],
  peg='Ler a lei pela CF e "liberar" o indulto.', kw=['anistia, graça e indulto', 'fiança'])
# --- PEN-1.4 · Rodada 2
I(P, 2, 'Direito penal do inimigo',
  'O direito penal do inimigo, associado à terceira velocidade, trata certos agentes como fontes de perigo e admite antecipação da punição e redução de garantias.', 'C',
  'Formulação doutrinária (Jakobs): punição de atos preparatórios, penas desproporcionais, garantias reduzidas. É incompatível com o **direito penal do fato** e com a legalidade (CF, art. 5º, XXXIX).',
  lei=[LEG], kw=['direito penal do inimigo', 'terceira velocidade'])
I(P, 2, 'Abolicionismo e minimalismo',
  'O minimalismo penal defende a abolição completa do sistema penal, substituindo-o por instâncias exclusivamente civis e administrativas.', 'E',
  'Quem prega a abolição é o **abolicionismo**. O **minimalismo** (direito penal mínimo, garantismo) mantém o sistema penal, mas restrito aos ataques mais graves aos bens jurídicos mais relevantes.',
  lei=[LEG], peg='Trocar minimalismo por abolicionismo.', kw=['abolicionismo', 'minimalismo'])
I(P, 2, 'Racismo: imprescritibilidade',
  'Por escolha constitucional de política criminal, o racismo e a ação de grupos armados contra a ordem constitucional são crimes inafiançáveis e imprescritíveis.', 'C',
  'Só esses dois são **imprescritíveis** na CF (art. 5º, XLII e XLIV). Tortura, tráfico, terrorismo e hediondos são inafiançáveis, mas **prescrevem**.',
  lei=[(CF + '5', 'constitui crime inafiançável e imprescritível a ação de grupos armados', None, 'CF, art. 5º, XLIV'),
       (CF + '5', 'a prática do racismo constitui crime inafiançável e imprescritível', None, 'CF, art. 5º, XLII')],
  exc=['Tortura, tráfico, terrorismo e hediondos: inafiançáveis, mas prescritíveis (CF, art. 5º, XLIII)'],
  kw=['imprescritíveis', 'grupos armados'])

# ======================= PEN-2 · A lei penal =======================
P = 'DBA26-PEN-2'
I(P, 1, 'Lei penal e costume',
  'O costume pode criar crimes e agravar penas, desde que reiterado e acompanhado da convicção de obrigatoriedade.', 'E',
  'Pela **reserva legal**, só **lei em sentido estrito** cria crime ou comina pena (CF, art. 5º, XXXIX). O costume serve apenas como fonte de interpretação (ex.: "ato obsceno").',
  lei=[LEG], peg='Admitir costume incriminador.', kw=['reserva legal', 'costume'])
I(P, 1, 'Normas penais não incriminadoras',
  'Além das normas incriminadoras, há normas penais permissivas, que afastam a ilicitude, e explicativas, que esclarecem conceitos, como as do art. 23 e do art. 327 do Código Penal.', 'C',
  'Classificação: **incriminadoras** (preceito + sanção), **permissivas** (justificantes, art. 23, ou exculpantes) e **explicativas/complementares**.',
  lei=[(CP + '23', 'Não há crime quando o agente pratica o fato:', None, 'CP, art. 23, caput')],
  kw=['normas permissivas', 'incriminadoras'])
I(P, 1, 'Contagem de prazo penal',
  'Nos prazos penais, exclui-se o dia do começo e inclui-se o do vencimento, como no processo civil.', 'E',
  'No **prazo penal** (art. 10 do CP) o **dia do começo inclui-se** no cômputo, e os meses e anos seguem o calendário comum. É regra mais favorável ao réu (prescrição, decadência, pena).',
  lei=[(CP + '10', 'O dia do começo inclui-se no cômputo do prazo.', 'calendário comum', 'CP, art. 10')],
  peg='Aplicar a regra processual (exclui o dia do começo).', kw=['dia do começo inclui-se', 'prazo penal'])
I(P, 1, 'Frações de dia',
  'Computam-se, nas penas privativas de liberdade e nas restritivas de direitos, as frações de dia, contadas em horas.', 'E',
  'Art. 11: **desprezam-se** as **frações de dia** nas privativas e nas restritivas; na multa, as frações da moeda.',
  lei=[(CP + '11', 'Desprezam-se, nas penas privativas de liberdade e nas restritivas de direitos, as frações de dia', None, 'CP, art. 11')],
  kw=['frações de dia'])
I(P, 1, 'Lei penal e medida provisória benéfica',
  'Como a vedação constitucional abrange o direito penal, nenhuma norma penal, nem mesmo a não incriminadora, pode ser veiculada em lei ordinária.', 'E',
  'Lei **ordinária** é o veículo normal da lei penal. A vedação do art. 62, § 1º, I, b, atinge a **medida provisória**, não a lei ordinária.',
  lei=[MP], peg='Trocar "medida provisória" por "lei ordinária".', kw=['lei ordinária', 'medida provisória'])
# --- PEN-2 · Rodada 2
I(P, 2, 'Lei penal em branco ao avesso',
  'Na norma penal em branco inversa (ou ao avesso), o preceito primário é completo, mas o secundário (a pena) precisa ser complementado — e esse complemento só pode vir de lei.', 'C',
  'Na **norma penal em branco ao avesso** a lacuna está na **sanção**; pela **reserva legal** da pena (CF, art. 5º, XXXIX), o complemento tem de ser lei.',
  lei=[LEG], kw=['norma penal em branco ao avesso', 'sanção'])
I(P, 2, 'Lei especial e combinação de leis',
  'Na sucessão de leis penais, o STJ admite combinar a parte mais benéfica da lei nova com a parte mais benéfica da lei antiga, criando uma terceira norma.', 'E',
  'A **Súmula 501/STJ** veda a **combinação de leis** (lex tertia): aplica-se, na íntegra, a lei que for mais favorável ao réu.',
  juris=[J['S501']], peg='Admitir a lex tertia.', kw=['combinação de leis', 'Súmula 501/STJ'])
I(P, 2, 'Lei mais benigna após o trânsito',
  'Transitada em julgado a condenação, compete ao juízo da execução aplicar a lei posterior mais benigna.', 'C',
  'É a **Súmula 611/STF**, repetida no art. 66, I, da LEP.',
  lei=[('L7210:66', 'aplicar aos casos julgados lei posterior que de qualquer modo favorecer o condenado', None, 'LEP, art. 66, I')],
  juris=[J['STF611']], kw=['juízo da execução', 'Súmula 611/STF'])

# ======================= PEN-2.1 · Características, fontes, interpretação, vigência e aplicação =======================
P = 'DBA26-PEN-2.1'
I(P, 1, 'Analogia in malam partem',
  'É vedada a analogia em prejuízo do réu, mas admite-se a analogia in bonam partem, desde que haja lacuna involuntária.', 'C',
  'A **analogia** é integração, não interpretação. Contra o réu, ofende a reserva legal; a favor, é admitida (ex.: estender causa de isenção).',
  lei=[LEG], kw=['analogia', 'in bonam partem'])
I(P, 1, 'Interpretação analógica',
  'A interpretação analógica é vedada no direito penal, por equivaler à analogia em prejuízo do réu.', 'E',
  'A **interpretação analógica** é determinada pela própria lei (fórmula casuística + fórmula genérica), como em "ou outro meio insidioso ou cruel" (CP, art. 61, II, d). É permitida, inclusive contra o réu.',
  lei=[(CP + '61', 'com emprego de veneno, fogo, explosivo, tortura ou outro meio insidioso ou cruel', None, 'CP, art. 61, II, d')],
  peg='Igualar interpretação analógica a analogia.', kw=['interpretação analógica', 'fórmula genérica'])
I(P, 1, 'Interpretação autêntica',
  'Interpretação autêntica é a feita pelo próprio legislador, por meio de lei, como ocorre com o conceito de funcionário público para efeitos penais.', 'C',
  'Quanto ao sujeito: **autêntica** (legislador — contextual ou posterior), **doutrinária** e **judicial**. Exemplo de autêntica contextual: conceitos legais na própria lei, como "considera-se causa" (art. 13).',
  lei=[(CP + '13', 'Considera-se causa a ação ou omissão sem a qual o resultado não teria ocorrido.', None, 'CP, art. 13, caput')],
  kw=['interpretação autêntica'])
I(P, 1, 'Fontes formais imediatas',
  'Os costumes são fonte formal imediata do direito penal incriminador, ao lado da lei.', 'E',
  'Pela **reserva legal**, a única **fonte formal imediata** da norma incriminadora é a **lei** (CF, art. 5º, XXXIX); costumes só auxiliam a interpretação.',
  lei=[LEG], kw=['fonte formal imediata', 'lei'])
I(P, 1, 'Lei excepcional e temporária',
  'A lei temporária deixa de alcançar os fatos praticados durante sua vigência assim que encerrado o período de duração, por força da retroatividade benéfica.', 'E',
  'Leis **excepcionais e temporárias** são **ultrativas**: aplicam-se ao fato praticado durante a vigência mesmo depois de autorrevogadas (CP, art. 3º). Do contrário, perderiam a força intimidativa.',
  lei=[(CP + '3', 'A lei excepcional ou temporária, embora decorrido o período de sua duração', 'aplica-se ao fato praticado durante sua vigência', 'CP, art. 3º')],
  peg='Aplicar a retroatividade benéfica ao fim da lei temporária.', kw=['ultrativas', 'lei temporária'])
# --- PEN-2.1 · Rodada 2
I(P, 2, 'Abolitio criminis temporária',
  'A abolitio criminis temporária do Estatuto do Desarmamento alcança a posse de arma de uso permitido com numeração raspada praticada a qualquer tempo.', 'E',
  '**Súmula 513/STJ**: a **abolitio criminis temporária** vale só para a posse praticada **até 23/10/2005**.',
  juris=[J['S513']], kw=['abolitio criminis temporária', 'Súmula 513/STJ'])
I(P, 2, 'Vacatio legis',
  'Durante a vacatio legis, a lei penal nova mais benéfica já pode ser aplicada aos fatos anteriores.', 'E',
  'Posição prevalente na doutrina: na **vacatio legis** a lei ainda **não tem eficácia** e pode até ser revogada antes de entrar em vigor; a retroatividade benéfica (CF, art. 5º, XL) pressupõe lei vigente.',
  lei=[RETRO], peg='Antecipar a retroatividade para a vacatio.', kw=['vacatio legis', 'eficácia'])
I(P, 2, 'Interpretação extensiva',
  'A interpretação extensiva amplia o alcance das palavras da lei para que corresponda à vontade do texto, sem se confundir com a analogia, que pressupõe lacuna.', 'C',
  'Na **interpretação extensiva** há norma, e o intérprete ajusta seu alcance; na **analogia** não há norma, e se integra a lacuna. A reserva legal (CF, art. 5º, XXXIX) veda a analogia incriminadora.',
  lei=[LEG], kw=['interpretação extensiva', 'lacuna'])

# ======================= PEN-2.2 · Lei penal no tempo e no espaço =======================
P = 'DBA26-PEN-2.2'
I(P, 1, 'Abolitio criminis',
  'A lei posterior que deixa de considerar o fato como crime faz cessar a execução e os efeitos penais da condenação, mas não os efeitos civis.', 'C',
  'É a **abolitio criminis** (CP, art. 2º, caput, e art. 107, III): apaga os **efeitos penais** (inclusive reincidência), mas a obrigação de indenizar permanece.',
  lei=[(CP + '2', 'Ninguém pode ser punido por fato que lei posterior deixa de considerar crime', 'efeitos penais da sentença condenatória', 'CP, art. 2º, caput')],
  kw=['abolitio criminis', 'efeitos penais'])
I(P, 1, 'Novatio legis in mellius e coisa julgada',
  'A lei posterior que de qualquer modo favorecer o agente aplica-se aos fatos anteriores, salvo se já houver sentença condenatória transitada em julgado.', 'E',
  'A **lex mitior** retroage **ainda que** haja condenação **transitada em julgado** (CP, art. 2º, par. ún.); a coisa julgada não a barra.',
  lei=[(CP + '2', 'A lei posterior, que de qualquer modo favorecer o agente', 'ainda que decididos por sentença condenatória transitada em julgado', 'CP, art. 2º, par. ún.')],
  peg='Opor a coisa julgada à lei mais benéfica.', kw=['lex mitior', 'transitada em julgado'])
I(P, 1, 'Tempo do crime',
  'Quanto ao tempo do crime, o Código Penal adotou a teoria da atividade: considera-se praticado o crime no momento da ação ou omissão, ainda que outro seja o momento do resultado.', 'C',
  'Teoria da **atividade** (art. 4º). Consequência clássica: a imputabilidade se afere no momento da conduta.',
  lei=[(CP + '4', 'Considera-se praticado o crime no momento da ação ou omissão', None, 'CP, art. 4º')],
  kw=['teoria da atividade'])
I(P, 1, 'Lugar do crime',
  'Quanto ao lugar do crime, o Código Penal adotou a teoria do resultado, considerando praticado o crime apenas onde se produziu o resultado.', 'E',
  'Para o lugar o CP adotou a **ubiquidade** (mista): ação ou omissão, no todo ou em parte, **ou** resultado produzido ou que deveria produzir-se (art. 6º). Mnemônico: LUTA (Lugar-Ubiquidade, Tempo-Atividade).',
  lei=[(CP + '6', 'Considera-se praticado o crime no lugar em que ocorreu a ação ou omissão', 'deveria produzir-se o resultado', 'CP, art. 6º')],
  peg='Trocar ubiquidade por resultado.', kw=['ubiquidade', 'LUTA'])
I(P, 1, 'Extraterritorialidade incondicionada',
  'Nos crimes contra a vida ou a liberdade do Presidente da República cometidos no estrangeiro, o agente é punido segundo a lei brasileira, ainda que absolvido ou condenado no estrangeiro.', 'C',
  'É **extraterritorialidade incondicionada** (art. 7º, I, a, e § 1º): não depende de condição alguma. A pena cumprida lá é descontada (art. 8º).',
  lei=[(CP + '7', 'contra a vida ou a liberdade do Presidente da República', None, 'CP, art. 7º, I, a'),
       (CP + '7', 'Nos casos do inciso I, o agente é punido segundo a lei brasileira, ainda que absolvido ou condenado no estrangeiro.', None, 'CP, art. 7º, § 1º')],
  kw=['extraterritorialidade incondicionada'])
I(P, 1, 'Extraterritorialidade condicionada',
  'Para o crime praticado por brasileiro no estrangeiro, a aplicação da lei brasileira depende, entre outras condições, de o agente entrar no território nacional e de o fato ser punível também no país em que foi praticado.', 'C',
  'Crime de brasileiro no exterior é **extraterritorialidade condicionada** (art. 7º, II, b): exige o concurso de **todas** as condições do § 2º (entrada no território, dupla tipicidade, crime extraditável, não absolvição/cumprimento, não extinção da punibilidade).',
  lei=[(CP + '7', 'Nos casos do inciso II, a aplicação da lei brasileira depende do concurso das seguintes condições:', 'ser o fato punível também no país em que foi praticado', 'CP, art. 7º, § 2º, a e b')],
  kw=['extraterritorialidade condicionada', 'dupla tipicidade'])
I(P, 1, 'Território por extensão',
  'As embarcações e aeronaves brasileiras de natureza pública ou a serviço do governo só são extensão do território nacional quando em alto-mar ou no espaço aéreo correspondente.', 'E',
  'Art. 5º, § 1º: as de **natureza pública** ou a serviço do governo são **extensão do território nacional** onde quer que se encontrem; a limitação ao alto-mar e ao espaço aéreo correspondente vale para as mercantes ou privadas.',
  lei=[(CP + '5', 'Para os efeitos penais, consideram-se como extensão do território nacional', 'em alto-mar', 'CP, art. 5º, § 1º')],
  kw=['extensão do território nacional', 'natureza pública'])
# --- PEN-2.2 · Rodada 2
I(P, 2, 'Crime permanente e lei mais grave',
  'Se a lei penal mais grave entra em vigor durante a permanência do crime, aplica-se a lei anterior, mais benéfica, porque o crime começou sob sua vigência.', 'E',
  'Pela **Súmula 711/STF**, a lei mais grave aplica-se ao crime **permanente** ou **continuado** se a vigência é **anterior à cessação** da permanência ou da continuidade.',
  juris=[J['STF711']], peg='Aplicar a lei do início da conduta ao crime permanente.', kw=['Súmula 711/STF', 'permanente'])
I(P, 2, 'Extraterritorialidade e estrangeiro contra brasileiro',
  'A lei brasileira aplica-se ao crime cometido por estrangeiro contra brasileiro fora do Brasil, se reunidas as condições do art. 7º, § 2º, e, ainda, não pedida ou negada a extradição e havendo requisição do Ministro da Justiça.', 'C',
  'É a hipótese **hipercondicionada** do art. 7º, § 3º (princípio da defesa ou da personalidade passiva).',
  lei=[(CP + '7', 'A lei brasileira aplica-se também ao crime cometido por estrangeiro contra brasileiro fora do Brasil', 'houve requisição do Ministro da Justiça', 'CP, art. 7º, § 3º')],
  kw=['hipercondicionada', 'requisição do Ministro da Justiça'])
I(P, 2, 'Pena cumprida no estrangeiro',
  'A pena cumprida no estrangeiro não interfere na pena imposta no Brasil pelo mesmo crime, pois as soberanias são independentes.', 'E',
  'Art. 8º: a pena cumprida no estrangeiro **atenua** a imposta no Brasil pelo mesmo crime, quando **diversas**, ou nela é **computada**, quando **idênticas** — evita o bis in idem.',
  lei=[(CP + '8', 'A pena cumprida no estrangeiro atenua a pena imposta no Brasil pelo mesmo crime', None, 'CP, art. 8º')],
  peg='Ignorar o desconto do art. 8º.', kw=['atenua', 'computada'])
I(P, 2, 'Aeronave estrangeira privada',
  'A lei brasileira não se aplica a crime praticado a bordo de embarcação estrangeira de propriedade privada atracada em porto brasileiro, por ser território do país da bandeira.', 'E',
  'Art. 5º, § 2º: aplica-se a lei brasileira às **estrangeiras privadas** em porto ou mar territorial do Brasil (e às aeronaves em pouso ou voo no **espaço aéreo** correspondente).',
  lei=[(CP + '5', 'É também aplicável a lei brasileira aos crimes praticados a bordo de aeronaves ou embarcações estrangeiras de propriedade privada', 'porto ou mar territorial do Brasil', 'CP, art. 5º, § 2º')],
  kw=['estrangeiras privadas', 'espaço aéreo'])
I(P, 2, 'Genocídio no estrangeiro',
  'O crime de genocídio cometido no estrangeiro sujeita-se incondicionalmente à lei brasileira, qualquer que seja a nacionalidade ou o domicílio do agente.', 'E',
  'No genocídio a extraterritorialidade é incondicionada **quando o agente for brasileiro ou domiciliado no Brasil** (art. 7º, I, d). Fora disso, pode cair na hipótese de tratado (art. 7º, II, a), condicionada.',
  lei=[(CP + '7', 'de genocídio, quando o agente for brasileiro ou domiciliado no Brasil', None, 'CP, art. 7º, I, d')],
  peg='Retirar a exigência de brasileiro ou domiciliado.', kw=['genocídio', 'domiciliado no Brasil'])

# ======================= PEN-2.3 · Imunidade =======================
P = 'DBA26-PEN-2.3'
I(P, 1, 'Imunidade material parlamentar',
  'Deputados e Senadores são invioláveis, civil e penalmente, por quaisquer de suas opiniões, palavras e votos.', 'C',
  'É a **imunidade material** (inviolabilidade) do art. 53, caput, da CF; exige relação com o mandato (nexo funcional).',
  lei=[(CF + '53', 'Os Deputados e Senadores são invioláveis, civil e penalmente, por quaisquer de suas opiniões, palavras e votos.', None, 'CF, art. 53, caput')],
  kw=['imunidade material', 'invioláveis'])
I(P, 1, 'Prisão de parlamentar',
  'Desde a posse, os membros do Congresso Nacional não poderão ser presos, salvo em flagrante de crime inafiançável.', 'E',
  'O marco é a **expedição do diploma**, não a posse (CF, art. 53, § 2º). Preso em flagrante de crime inafiançável, os autos vão à Casa em 24 horas para deliberar pela maioria de seus membros.',
  lei=[(CF + '53', 'Desde a expedição do diploma, os membros do Congresso Nacional não poderão ser presos', 'resolva sobre a prisão', 'CF, art. 53, § 2º')],
  peg='Trocar "diploma" por "posse".', kw=['expedição do diploma', 'crime inafiançável'])
I(P, 1, 'Vereadores',
  'Os vereadores têm inviolabilidade por suas opiniões, palavras e votos em todo o território nacional, desde que no exercício do mandato.', 'E',
  'CF, art. 29, VIII: a inviolabilidade é limitada à **circunscrição do Município**; e **vereadores** não têm imunidade formal.',
  lei=[(CF + '29', 'inviolabilidade dos Vereadores por suas opiniões, palavras e votos', None, 'CF, art. 29, VIII')],
  kw=['circunscrição do Município', 'vereadores'])
I(P, 1, 'Deputados estaduais',
  'Os deputados estaduais não gozam de imunidades, que a Constituição reserva aos membros do Congresso Nacional.', 'E',
  'A CF manda aplicar aos **deputados estaduais** as regras sobre **inviolabilidade e imunidades** dos congressistas (art. 27, § 1º).',
  lei=[(CF + '27', 'Será de quatro anos o mandato dos Deputados Estaduais', 'inviolabilidade, imunidades', 'CF, art. 27, § 1º')],
  peg='Negar a simetria do art. 27, § 1º.', kw=['deputados estaduais', 'imunidades'])
I(P, 1, 'Sustação do processo e prescrição',
  'A sustação, pela Casa legislativa, do processo contra parlamentar por crime ocorrido após a diplomação suspende a prescrição enquanto durar o mandato.', 'C',
  'CF, art. 53, §§ 3º e 5º: sustação por iniciativa de partido e maioria da Casa; a **prescrição fica suspensa** enquanto durar o mandato.',
  lei=[(CF + '53', 'A sustação do processo suspende a prescrição, enquanto durar o mandato.', None, 'CF, art. 53, § 5º')],
  kw=['sustação', 'suspende a prescrição'])
# --- PEN-2.3 · Rodada 2
I(P, 2, 'Sustação: crime anterior à diplomação',
  'A Casa legislativa pode sustar o andamento de ação penal contra parlamentar por crime praticado antes da diplomação.', 'E',
  'A sustação só alcança crime **ocorrido após a diplomação** (CF, art. 53, § 3º).',
  lei=[(CF + '53', 'Recebida a denúncia contra o Senador ou Deputado, por crime ocorrido após a diplomação', 'poderá, até a decisão final, sustar o andamento da ação', 'CF, art. 53, § 3º')],
  peg='Estender a sustação a crime anterior ao diploma.', kw=['após a diplomação', 'sustar'])
I(P, 2, 'Presidente da República',
  'Na vigência do mandato, o Presidente da República não pode ser responsabilizado por atos estranhos ao exercício de suas funções.', 'C',
  'É a **irresponsabilidade penal relativa** (CF, art. 86, § 4º): por crimes estranhos à função, a persecução fica para depois do mandato. E, nas infrações comuns, não está sujeito a prisão antes da sentença condenatória (§ 3º).',
  lei=[(CF + '86', 'O Presidente da República, na vigência de seu mandato, não pode ser responsabilizado por atos estranhos ao exercício de suas funções.', None, 'CF, art. 86, § 4º')],
  kw=['irresponsabilidade penal relativa', 'atos estranhos'])
I(P, 2, 'Imunidades no estado de sítio',
  'As imunidades parlamentares ficam automaticamente suspensas durante o estado de sítio.', 'E',
  'Elas **subsistem** no estado de sítio e só podem ser suspensas pelo voto de **dois terços** da Casa, para atos fora do recinto incompatíveis com a medida (CF, art. 53, § 8º).',
  lei=[(CF + '53', 'As imunidades de Deputados ou Senadores subsistirão durante o estado de sítio', 'incompatíveis com a execução da medida', 'CF, art. 53, § 8º')],
  peg='Suspensão automática.', kw=['subsistirão', 'dois terços'])

# ======================= PEN-2.4 · Condições de punibilidade =======================
P = 'DBA26-PEN-2.4'
I(P, 1, 'Condição objetiva de punibilidade',
  'Condição objetiva de punibilidade é acontecimento futuro e incerto, exterior ao tipo e ao dolo do agente, de que a lei faz depender a punição.', 'C',
  'Ex.: a **sentença de falência** nos crimes falimentares (Lei 11.101/2005, art. 180) e a entrada do agente no território na extraterritorialidade condicionada (CP, art. 7º, § 2º, a). Não precisa ser abrangida pelo dolo.',
  lei=[('L11101:180', 'A sentença que decreta a falência', 'é condição objetiva de punibilidade', 'Lei 11.101/2005, art. 180')],
  kw=['condição objetiva de punibilidade', 'sentença de falência'])
I(P, 1, 'Condição de punibilidade x de procedibilidade',
  'A representação do ofendido é condição objetiva de punibilidade, pois sem ela o fato não chega a ser crime.', 'E',
  'A **representação** é **condição de procedibilidade** (processual): o crime existe, mas a ação pública depende dela (CP, art. 100, § 1º). A condição objetiva de punibilidade é de direito material.',
  lei=[(CP + '100', 'A ação pública é promovida pelo Ministério Público, dependendo, quando a lei o exige, de representação do ofendido', None, 'CP, art. 100, § 1º')],
  peg='Confundir condição de procedibilidade com condição de punibilidade.', kw=['condição de procedibilidade', 'representação'])
I(P, 1, 'Escusas absolutórias',
  'As escusas absolutórias, como a imunidade do cônjuge nos crimes patrimoniais sem violência, afastam a punibilidade por razões de política criminal, embora o fato permaneça típico, ilícito e culpável.', 'C',
  'É a **imunidade penal absoluta** do art. 181 do CP: isenta de pena o cônjuge (na constância da sociedade conjugal) e o ascendente/descendente. Não se aplica se houver violência ou grave ameaça, a estranho que participa nem à vítima idosa (art. 183).',
  lei=[(CP + '181', 'É isento de pena quem comete qualquer dos crimes previstos neste título, em prejuízo:', None, 'CP, art. 181, caput')],
  kw=['escusas absolutórias', 'imunidade penal absoluta'])
I(P, 1, 'Extraterritorialidade e condições',
  'Na extraterritorialidade condicionada, a lei brasileira se aplica ainda que o agente já tenha cumprido a pena no estrangeiro, porque essa pena é apenas descontada da imposta aqui.', 'E',
  'Art. 7º, § 2º, d: é condição cumulativa **não ter sido o agente absolvido no estrangeiro** ou não ter aí cumprido a pena. O desconto do art. 8º opera quando a lei brasileira incide, como na extraterritorialidade incondicionada.',
  lei=[(CP + '7', 'não ter sido o agente absolvido no estrangeiro ou não ter aí cumprido a pena', None, 'CP, art. 7º, § 2º, d')],
  kw=['condições cumulativas', 'absolvido no estrangeiro'])
I(P, 1, 'Dolo e condição objetiva',
  'O dolo do agente deve abranger a condição objetiva de punibilidade, sob pena de atipicidade.', 'E',
  'A condição objetiva é **exterior ao tipo**: não precisa ser abrangida pelo **dolo** nem pela culpa. Por isso, sem ela o fato não é punido, mas a falta não gera atipicidade por erro (CF, art. 5º, XXXIX).',
  lei=[('L11101:180', 'A sentença que decreta a falência', 'é condição objetiva de punibilidade', 'Lei 11.101/2005, art. 180')],
  peg='Exigir dolo sobre a condição.', kw=['exterior ao tipo', 'dolo'])
# --- PEN-2.4 · Rodada 2
I(P, 2, 'Escusa absolutória e terceiro',
  'A imunidade do cônjuge nos crimes contra o patrimônio aproveita ao estranho que participa do crime.', 'E',
  'O art. 183, II, do CP afasta a imunidade **ao estranho que participa do crime** — é circunstância pessoal, incomunicável.',
  lei=[(CP + '183', 'Não se aplica o disposto nos dois artigos anteriores:', 'ao estranho que participa do crime', 'CP, art. 183, caput e II')],
  peg='Comunicar a escusa ao coautor estranho.', kw=['estranho que participa do crime'])
I(P, 2, 'Escusa absolutória e idoso',
  'A imunidade do descendente que furta o pai deixa de incidir se a vítima tiver 60 anos ou mais.', 'C',
  'Art. 183, III, do CP (Estatuto do Idoso): as imunidades dos arts. 181 e 182 não se aplicam se o crime é praticado contra pessoa com idade **igual ou superior a 60 anos**.',
  lei=[(CP + '183', 'se o crime é praticado contra pessoa com idade igual ou superior a 60 (sessenta) anos', None, 'CP, art. 183, III')],
  kw=['60 anos', 'imunidade'])
I(P, 2, 'Imunidade relativa',
  'Nos crimes patrimoniais sem violência praticados contra irmão, o agente fica isento de pena.', 'E',
  'Contra irmão incide a **imunidade relativa** do art. 182, II: procede-se mediante **representação**. A isenção (art. 181) é para o cônjuge na constância da sociedade conjugal e para ascendente ou descendente.',
  lei=[(CP + '182', 'Somente se procede mediante representação, se o crime previsto neste título é cometido em prejuízo:', None, 'CP, art. 182, caput')],
  kw=['imunidade relativa', 'representação'])

# ======================= PEN-2.5 · Concurso aparente de normas =======================
P = 'DBA26-PEN-2.5'
I(P, 1, 'Especialidade',
  'Pelo princípio da especialidade, a norma especial, que contém todos os elementos da geral e mais alguns especializantes, prevalece sobre esta, independentemente da gravidade da pena.', 'C',
  'A **especialidade** não depende de comparar penas: o infanticídio (especial) prevalece sobre o homicídio mesmo tendo pena menor. Base positiva da relação CP × lei especial: art. 12.',
  lei=[(CP + '12', 'As regras gerais deste Código aplicam-se aos fatos incriminados por lei especial, se esta não dispuser de modo diverso.', None, 'CP, art. 12')],
  kw=['especialidade', 'elementos especializantes'])
I(P, 1, 'Consunção: falso e estelionato',
  'Quando o falso se exaure no estelionato, sem mais potencialidade lesiva, o agente responde pelos dois crimes em concurso material.', 'E',
  'A **Súmula 17/STJ** manda aplicar a **consunção**: o falso exaurido no estelionato é por este **absorvido**.',
  juris=[J['S17']], peg='Somar falso e estelionato quando o falso se exaure.', kw=['consunção', 'Súmula 17/STJ'])
I(P, 1, 'Subsidiariedade expressa',
  'Na subsidiariedade expressa, o próprio tipo declara que só se aplica se o fato não constituir crime mais grave, como no perigo para a vida ou saúde de outrem.', 'C',
  'O art. 132 do CP comina a pena "se o fato não constitui crime mais grave" — **subsidiariedade expressa** (lex primaria derogat legi subsidiariae).',
  lei=[(CP + '132', 'Expor a vida ou a saúde de outrem a perigo direto e iminente', 'se o fato não constitui crime mais grave', 'CP, art. 132, caput')],
  kw=['subsidiariedade expressa', 'crime mais grave'])
I(P, 1, 'Concurso aparente x concurso de crimes',
  'No concurso aparente de normas há pluralidade de fatos e pluralidade de normas, aplicando-se cumulativamente as penas.', 'E',
  'No **concurso aparente** há **um só fato** e várias normas aparentemente aplicáveis; resolve-se por especialidade, subsidiariedade, consunção (e alternatividade), aplicando **uma só**. A soma de penas é do concurso material de crimes (art. 69).',
  lei=[(CP + '69', 'Quando o agente, mediante mais de uma ação ou omissão, pratica dois ou mais crimes', 'aplicam-se cumulativamente as penas privativas de liberdade', 'CP, art. 69, caput')],
  peg='Confundir concurso aparente de normas com concurso material.', kw=['concurso aparente', 'um só fato'])
I(P, 1, 'Alternatividade',
  'Nos tipos mistos alternativos, cada núcleo verbal praticado no mesmo contexto fático e sobre o mesmo objeto gera um crime autônomo, em concurso material.', 'E',
  'Pelo princípio da **alternatividade**, várias condutas do **tipo misto alternativo** (ex.: art. 28 da Lei de Drogas) no mesmo contexto e sobre o mesmo objeto são **um só crime**.',
  lei=[('L11343:28', 'Quem adquirir, guardar, tiver em depósito, transportar ou trouxer consigo, para consumo pessoal', None, 'Lei 11.343/2006, art. 28, caput')],
  kw=['alternatividade', 'tipo misto alternativo'])
# --- PEN-2.5 · Rodada 2
I(P, 2, 'Concurso de agentes no furto e majorante do roubo',
  'No furto qualificado pelo concurso de agentes, é possível aplicar, por analogia benéfica, a fração de aumento prevista para o roubo majorado, em vez de dobrar a pena.', 'E',
  'A **Súmula 442/STJ** declara **inadmissível** aplicar ao furto qualificado pelo concurso de agentes a majorante do roubo: cada tipo tem sua resposta penal.',
  juris=[J['S442']], peg='"Analogia in bonam partem" entre tipos diversos.', kw=['Súmula 442/STJ', 'inadmissível'])
I(P, 2, 'Antefato e pós-fato impuníveis',
  'O pós-fato impunível ocorre quando o agente, depois de consumado o crime, pratica nova lesão ao mesmo bem jurídico e contra a mesma vítima, como mero exaurimento — por exemplo, destruir a coisa que ele próprio furtou.', 'C',
  'É hipótese de **consunção** (post factum impunível): a nova conduta não amplia a lesão já causada. Destruir a coisa furtada não gera dano autônomo. A consunção do falso pelo estelionato (Súmula 17/STJ) segue a mesma lógica.',
  juris=[J['S17']], kw=['post factum impunível', 'consunção'])
I(P, 2, 'Especialidade e pena',
  'Pelo princípio da especialidade, prevalece sempre a norma que comina a pena mais grave.', 'E',
  'A especialidade é **lógica**, não valorativa: compara elementos, não penas. Infanticídio, mais brando, prevalece sobre homicídio. Regra de prevalência pela gravidade é a da **subsidiariedade** (art. 132: "se o fato não constitui crime mais grave").',
  lei=[(CP + '132', 'se o fato não constitui crime mais grave', None, 'CP, art. 132, caput')],
  peg='Confundir especialidade com subsidiariedade.', kw=['especialidade', 'subsidiariedade'])
