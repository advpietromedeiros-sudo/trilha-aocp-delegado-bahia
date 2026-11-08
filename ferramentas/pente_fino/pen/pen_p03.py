# Pente Fino de Direito Penal (Parte Geral) — PEN-3 (teoria geral do crime, 3.1 a 3.6) (08/11/2026).
from base import I
from pen_juris import J

CP = 'CP:'
CF = 'CF:'
CAUSA = (CP + '13', 'O resultado, de que depende a existência do crime, somente é imputável a quem lhe deu causa.', 'sem a qual o resultado não teria ocorrido.', 'CP, art. 13, caput')
SUPERV = (CP + '13', 'A superveniência de causa relativamente independente exclui a imputação quando, por si só, produziu o resultado', 'imputam-se a quem os praticou', 'CP, art. 13, § 1º')
OMISSAO = (CP + '13', 'A omissão é penalmente relevante quando o omitente devia e podia agir para evitar o resultado.', 'criou o risco da ocorrência do resultado', 'CP, art. 13, § 2º')

# ======================= PEN-3 · Teoria geral do crime =======================
P = 'DBA26-PEN-3'
I(P, 1, 'Conceito analítico',
  'Pelo conceito analítico tripartido, crime é fato típico, ilícito e culpável.', 'C',
  'É a posição **majoritária** na doutrina. O CP trata a exclusão da **ilicitude** como "não há crime" (art. 23) e a da **culpabilidade** como "é isento de pena" (arts. 26 e 28, § 1º) — redação que os bipartidos usam para dizer que culpabilidade é pressuposto da pena.',
  lei=[(CP + '23', 'Não há crime quando o agente pratica o fato:', None, 'CP, art. 23, caput'),
       (CP + '26', 'É isento de pena o agente que, por doença mental', None, 'CP, art. 26, caput')],
  kw=['tripartido', 'fato típico, ilícito e culpável'])
I(P, 1, 'Crime e contravenção',
  'Entre crime e contravenção penal há diferença ontológica, pois só os crimes lesam bens jurídicos.', 'E',
  'A diferença é **axiológica/quantitativa** (escolha do legislador quanto à gravidade), não ontológica. Os efeitos práticos estão na lei: na contravenção a tentativa não é punível (LCP, art. 4º).',
  lei=[('DL3688:4', 'Não é punível a tentativa de contravenção.', None, 'LCP, art. 4º')],
  peg='Afirmar diferença de essência entre crime e contravenção.', kw=['axiológica', 'tentativa não é punível'])
I(P, 1, 'Contravenção: voluntariedade',
  'Para a existência da contravenção basta a ação ou omissão voluntária, devendo-se considerar o dolo ou a culpa apenas quando a lei fizer depender deles algum efeito jurídico.', 'C',
  'É a literalidade do art. 3º da LCP: basta a **ação ou omissão voluntária**. A doutrina relê a regra à luz do princípio da culpabilidade.',
  lei=[('DL3688:3', 'Para a existência da contravenção, basta a ação ou omissão voluntária.', 'qualquer efeito jurídico', 'LCP, art. 3º')],
  kw=['ação ou omissão voluntária'])
I(P, 1, 'Conceito material',
  'Sob o aspecto material, crime é toda conduta que a lei descreve como tal, independentemente de lesar ou expor a perigo bem jurídico.', 'E',
  'Isso é o conceito **formal**. O **material** exige lesão ou perigo de lesão a **bem jurídico** relevante — base da insignificância (HC 84.412/STF).',
  juris=[J['HC84412']], peg='Trocar conceito formal por material.', kw=['conceito material', 'bem jurídico'])
I(P, 1, 'Culpabilidade e "isento de pena"',
  'Quando o Código Penal diz que "é isento de pena" o agente inimputável, refere-se a causa de exclusão da ilicitude.', 'E',
  '"É isento de pena" indica exclusão da **culpabilidade** (arts. 21, 26 e 28, § 1º); "não há crime" é a fórmula da exclusão da **ilicitude** (art. 23). Por isso a **isenção de pena** do inimputável não torna o fato lícito.',
  lei=[(CP + '26', 'É isento de pena o agente que, por doença mental ou desenvolvimento mental incompleto ou retardado', None, 'CP, art. 26, caput')],
  kw=['isenção de pena', 'culpabilidade'])
# --- PEN-3 · Rodada 2
I(P, 2, 'Teoria bipartida',
  'Para a teoria bipartida, crime é fato típico e ilícito, sendo a culpabilidade mero pressuposto de aplicação da pena.', 'C',
  'É a corrente **bipartida** (minoritária na doutrina). A tripartida (fato típico, ilícito e culpável) prevalece; a quadripartida inclui a punibilidade, o que a maioria rejeita.',
  lei=[(CP + '23', 'Não há crime quando o agente pratica o fato:', None, 'CP, art. 23, caput')],
  kw=['bipartida', 'pressuposto de aplicação da pena'])
I(P, 2, 'Punibilidade como elemento do crime',
  'Para a doutrina majoritária, a punibilidade integra o conceito analítico de crime, de modo que a prescrição faz desaparecer o próprio crime.', 'E',
  'A punibilidade é **consequência** do crime, não elemento: a extinção da punibilidade (art. 107) apaga a possibilidade de punir, mas o fato continua típico, ilícito e culpável — por isso o art. 108 fala em crime cuja punibilidade se extinguiu.',
  lei=[(CP + '108', 'A extinção da punibilidade de crime que é pressuposto, elemento constitutivo ou circunstância agravante de outro não se estende a este.', None, 'CP, art. 108, 1ª parte')],
  peg='Incluir a punibilidade no conceito analítico.', kw=['consequência', 'extinção da punibilidade'])
I(P, 2, 'Sistema de dupla imputação ambiental',
  'A pessoa jurídica pode ser sujeito ativo de crime ambiental, e sua responsabilidade não exclui a das pessoas físicas autoras, coautoras ou partícipes.', 'C',
  'A **pessoa jurídica** pode ser **sujeito ativo** de crime ambiental (CF, art. 225, § 3º), sem excluir a pessoa física (Lei 9.605/1998, art. 3º, par. ún.).',
  lei=[('L9605:3', 'A responsabilidade das pessoas jurídicas não exclui a das pessoas físicas', None, 'Lei 9.605/1998, art. 3º, par. ún.')],
  kw=['sujeito ativo', 'pessoa jurídica'])

# ======================= PEN-3.1 · Conceito, objeto, sujeitos, conduta, tipicidade, culpabilidade =======================
P = 'DBA26-PEN-3.1'
I(P, 1, 'Sujeito passivo',
  'Sujeito passivo formal (ou constante) do crime é o Estado, titular do mandamento proibitivo; sujeito passivo material é o titular do bem jurídico lesado ou ameaçado.', 'C',
  'Classificação doutrinária. O **sujeito passivo material** pode ser pessoa física, jurídica ou a coletividade (crimes vagos).',
  lei=[(CP + '100', 'A ação penal é pública, salvo quando a lei expressamente a declara privativa do ofendido.', None, 'CP, art. 100, caput')],
  kw=['sujeito passivo formal', 'sujeito passivo material'])
I(P, 1, 'Autolesão',
  'Quem fere o próprio corpo, sem atingir interesse alheio, figura simultaneamente como autor e vítima de crime de lesão corporal.', 'E',
  'Pela **alteridade**, ninguém é punido por lesar só bem próprio: a autolesão não é crime. Quando a autolesão é punida, a vítima é outra — por exemplo, na fraude para receber seguro, o lesado é a seguradora (CP, art. 171, § 2º, V).',
  lei=[(CP + '171', 'lesa o próprio corpo ou a saúde, ou agrava as conseqüências da lesão ou doença, com o intuito de haver indenização ou valor de seguro', None, 'CP, art. 171, § 2º, V')],
  peg='Admitir crime em que o agente é vítima de si mesmo.', kw=['alteridade', 'autolesão'])
I(P, 1, 'Objeto material e jurídico',
  'Objeto material do crime é o bem jurídico tutelado pela norma; objeto jurídico é a pessoa ou coisa sobre a qual recai a conduta.', 'E',
  'Inverteu: **objeto jurídico** é o bem tutelado (no furto, o patrimônio); **objeto material** é a pessoa ou coisa atingida (a coisa subtraída).',
  lei=[(CP + '155', 'Subtrair, para si ou para outrem, coisa alheia móvel', None, 'CP, art. 155, caput')],
  kw=['objeto jurídico', 'objeto material'])
I(P, 1, 'Conduta: teoria finalista',
  'Para a teoria finalista, adotada pela reforma de 1984, dolo e culpa integram a conduta e, portanto, o fato típico.', 'C',
  'No **finalismo** o dolo e a culpa saem da culpabilidade e vão para o **tipo**. Prova no CP: o erro de tipo **exclui o dolo** (art. 20), e o erro de proibição só afeta a culpabilidade (art. 21).',
  lei=[(CP + '20', 'O erro sobre elemento constitutivo do tipo legal de crime exclui o dolo', None, 'CP, art. 20, caput')],
  kw=['finalismo', 'dolo e culpa no tipo'])
I(P, 1, 'Ausência de conduta',
  'Os atos reflexos, a coação física irresistível e o sonambulismo excluem a culpabilidade, mas não a conduta.', 'E',
  'Sem **voluntariedade** não há **conduta** — exclui-se o próprio **fato típico**. A coação **moral** irresistível é que exclui a culpabilidade (art. 22).',
  lei=[(CP + '22', 'Se o fato é cometido sob coação irresistível', 'só é punível o autor da coação ou da ordem', 'CP, art. 22')],
  exc=['Coação MORAL irresistível: exclui a culpabilidade (inexigibilidade), não a conduta (CP, art. 22)'],
  peg='Confundir coação física (sem conduta) com coação moral (sem culpabilidade).', kw=['voluntariedade', 'conduta'])
I(P, 1, 'Tipicidade conglobante',
  'Para a teoria da tipicidade conglobante, a tipicidade penal exige, além da tipicidade formal, a antinormatividade e a tipicidade material, de modo que atos determinados ou fomentados pelo ordenamento são atípicos.', 'C',
  'Formulação doutrinária (Zaffaroni): o estrito cumprimento do dever legal e certas hipóteses de exercício regular de direito deixam de ser justificantes (art. 23, III) e passam a excluir a **tipicidade**.',
  lei=[(CP + '23', 'em estrito cumprimento de dever legal ou no exercício regular de direito', None, 'CP, art. 23, III')],
  kw=['tipicidade conglobante', 'antinormatividade'])
# --- PEN-3.1 · Rodada 2
I(P, 2, 'Teoria causal e dolo',
  'Na teoria causal-naturalista, o dolo e a culpa eram espécies ou elementos da culpabilidade, e não do tipo.', 'C',
  'No **causalismo** a conduta é movimento corporal voluntário causador de resultado; dolo e culpa ficavam na **culpabilidade** (psicológica). O finalismo os levou ao tipo (CP, art. 20).',
  lei=[(CP + '20', 'O erro sobre elemento constitutivo do tipo legal de crime exclui o dolo', None, 'CP, art. 20, caput')],
  kw=['causalismo', 'culpabilidade psicológica'])
I(P, 2, 'Crime vago',
  'Crime vago é aquele cujo sujeito passivo é ente sem personalidade jurídica, como a coletividade ou a família.', 'C',
  'Ex.: tráfico de drogas, ato obsceno. A **coletividade** é a vítima. Classificação doutrinária ligada ao sujeito passivo.',
  lei=[(CP + '233', 'Praticar ato obsceno em lugar público, ou aberto ou exposto ao público', None, 'CP, art. 233')],
  kw=['crime vago', 'coletividade'])
I(P, 2, 'Pessoa jurídica e fato típico',
  'Como a pessoa jurídica não tem vontade própria, a Lei 9.605/1998 só admite a sua responsabilização administrativa e civil, nunca a penal.', 'E',
  'A lei fala expressamente em responsabilidade "administrativa, **civil e penalmente**" (art. 3º).',
  lei=[('L9605:3', 'As pessoas jurídicas serão responsabilizadas administrativa, civil e penalmente', None, 'Lei 9.605/1998, art. 3º, caput')],
  peg='Retirar a esfera penal.', kw=['civil e penalmente'])

# ======================= PEN-3.2 · Bem jurídico =======================
P = 'DBA26-PEN-3.2'
I(P, 1, 'Exclusiva proteção de bens jurídicos',
  'Pelo princípio da exclusiva proteção de bens jurídicos, o direito penal não deve tutelar meras convicções morais, ideologias ou valores religiosos sem lesividade.', 'C',
  'É a função limitadora do **bem jurídico**: só condutas que lesam ou expõem a perigo valores essenciais podem ser criminalizadas. Mede-se pela **lesão jurídica** (vetor da insignificância).',
  juris=[J['HC84412']], kw=['exclusiva proteção de bens jurídicos'])
I(P, 1, 'Ofensividade',
  'Pelo princípio da ofensividade, não há crime sem lesão ou perigo de lesão ao bem jurídico, o que, segundo parte da doutrina, torna inconstitucionais os crimes de perigo abstrato.', 'C',
  'Assertiva certa no que afirma: **parte da doutrina** contesta os crimes de perigo abstrato. Na jurisprudência sumulada, crimes que dispensam resultado são aceitos (ex.: Súmula 500/STJ, corrupção de menores como delito formal).',
  juris=[J['S500']], kw=['ofensividade', 'perigo abstrato'])
I(P, 1, 'Bem jurídico e objeto material',
  'O bem jurídico e o objeto material do crime sempre coincidem.', 'E',
  'Normalmente se distinguem: no furto, o **bem jurídico** é o patrimônio; o **objeto material**, a coisa subtraída. Podem coincidir em casos raros, mas não "sempre".',
  lei=[(CP + '155', 'Subtrair, para si ou para outrem, coisa alheia móvel', None, 'CP, art. 155, caput')],
  peg='Usar "sempre".', kw=['bem jurídico', 'objeto material'])
I(P, 1, 'Bem jurídico difuso',
  'O meio ambiente ecologicamente equilibrado é bem jurídico de natureza difusa, protegido inclusive por sanções penais.', 'C',
  'O **meio ambiente** é **bem jurídico difuso**, de uso comum do povo (CF, art. 225, caput), tutelado penalmente contra pessoas físicas e jurídicas (§ 3º).',
  lei=[(CF + '225', 'Todos têm direito ao meio ambiente ecologicamente equilibrado', None, 'CF, art. 225, caput')],
  kw=['bem jurídico difuso', 'meio ambiente'])
I(P, 1, 'Insignificância e bem jurídico',
  'Reconhecida a insignificância, exclui-se a ilicitude da conduta, pois a lesão ao bem jurídico é tolerada pelo ordenamento.', 'E',
  'A insignificância exclui a **tipicidade material** (sem lesão relevante ao bem jurídico, não há tipo), não a ilicitude.',
  juris=[J['HC84412']], peg='Deslocar a insignificância para a ilicitude.', kw=['tipicidade material'])
# --- PEN-3.2 · Rodada 2
I(P, 2, 'Bem jurídico supraindividual e insignificância',
  'Nos crimes contra a administração pública, em que o bem jurídico abrange a moralidade administrativa, o STJ não admite a insignificância.', 'C',
  '**Súmula 599/STJ**. O fundamento costuma ser o caráter supraindividual do bem tutelado.',
  juris=[J['S599']], kw=['Súmula 599/STJ', 'moralidade administrativa'])
I(P, 2, 'Crime formal e bem jurídico',
  'Por ser delito formal, o crime de corrupção de menores do ECA exige a prova de que o adolescente efetivamente se corrompeu.', 'E',
  'A **Súmula 500/STJ** diz o contrário: o crime do art. 244-B do ECA **independe da prova da efetiva corrupção**, justamente por ser formal.',
  juris=[J['S500']], peg='Exigir resultado em crime formal.', kw=['Súmula 500/STJ', 'formal'])
I(P, 2, 'Espiritualização do bem jurídico',
  'A chamada espiritualização (ou desmaterialização) do bem jurídico consiste na crescente proteção penal de bens coletivos e difusos, como o meio ambiente e a ordem econômica.', 'C',
  'A **espiritualização do bem jurídico** é fenômeno apontado pela doutrina no direito penal moderno; exemplo positivo: a tutela penal ambiental (CF, art. 225, § 3º).',
  lei=[(CF + '225', 'As condutas e atividades consideradas lesivas ao meio ambiente sujeitarão os infratores', None, 'CF, art. 225, § 3º')],
  kw=['espiritualização do bem jurídico'])

# ======================= PEN-3.3 · Tempo e lugar do crime =======================
P = 'DBA26-PEN-3.3'
I(P, 1, 'Teoria da atividade e menoridade',
  'O agente que dispara contra a vítima um dia antes de completar 18 anos, sobrevindo a morte depois do aniversário, é inimputável quanto a esse fato.', 'C',
  'Pela **teoria da atividade** (art. 4º), o crime se considera praticado no momento da **conduta**, quando o agente ainda era menor (art. 27). Ele se sujeita ao ECA.',
  lei=[(CP + '4', 'Considera-se praticado o crime no momento da ação ou omissão, ainda que outro seja o momento do resultado.', None, 'CP, art. 4º'),
       (CP + '27', 'Os menores de 18 (dezoito) anos são penalmente inimputáveis', None, 'CP, art. 27')],
  kw=['teoria da atividade', 'momento da conduta'])
I(P, 1, 'Ubiquidade e crime à distância',
  'Pela teoria da ubiquidade, nos crimes à distância a lei brasileira se aplica se a conduta ou o resultado ocorrer no Brasil.', 'C',
  'O art. 6º considera lugar do crime tanto o da **ação ou omissão** (no todo ou em parte) quanto o do **resultado** (produzido ou que deveria produzir-se).',
  lei=[(CP + '6', 'Considera-se praticado o crime no lugar em que ocorreu a ação ou omissão', 'deveria produzir-se o resultado', 'CP, art. 6º')],
  kw=['ubiquidade', 'crime à distância'])
I(P, 1, 'Tentativa e ubiquidade',
  'Na tentativa, não há lugar do resultado, razão pela qual a lei brasileira só se aplica se a conduta tiver ocorrido no território nacional.', 'E',
  'O art. 6º abrange o lugar onde o resultado "**deveria** produzir-se": na tentativa iniciada no exterior para consumar-se no Brasil, aplica-se a lei brasileira.',
  lei=[(CP + '6', 'bem como onde se produziu ou deveria produzir-se o resultado', None, 'CP, art. 6º')],
  peg='Esquecer o "deveria produzir-se".', kw=['deveria produzir-se'])
I(P, 1, 'Crime permanente e lei nova',
  'No crime permanente, aplica-se a lei vigente ao tempo do início da conduta, mesmo que lei mais grave entre em vigor antes de cessada a permanência.', 'E',
  'Pela **Súmula 711/STF**, aplica-se a **lei mais grave** se sua vigência é anterior à **cessação da permanência** (o crime se renova a cada momento).',
  juris=[J['STF711']], peg='Congelar a lei no início da permanência.', kw=['Súmula 711/STF', 'cessação da permanência'])
I(P, 1, 'Prescrição no crime permanente',
  'Nos crimes permanentes, a prescrição antes do trânsito em julgado começa a correr do dia em que se iniciou a permanência.', 'E',
  'Art. 111, III: corre do dia em que **cessou a permanência**.',
  lei=[(CP + '111', 'nos crimes permanentes, do dia em que cessou a permanência', None, 'CP, art. 111, III')],
  kw=['cessou a permanência'])
# --- PEN-3.3 · Rodada 2
I(P, 2, 'Lugar e competência',
  'A teoria da ubiquidade do art. 6º do Código Penal resolve, também, a competência territorial interna entre comarcas brasileiras.', 'E',
  'O art. 6º do CP define a **aplicação da lei brasileira** no espaço (crimes à distância). A competência interna segue o CPP, que adota, em regra, o lugar da **consumação** (art. 70).',
  lei=[('CPP:70', 'A competência será, de regra, determinada pelo lugar em que se consumar a infração', None, 'CPP, art. 70, caput')],
  peg='Usar a ubiquidade para fixar comarca.', kw=['consumação', 'competência interna'])
I(P, 2, 'Crime continuado e lei mais grave',
  'No crime continuado, se a lei mais grave entra em vigor antes de cessada a continuidade, ela se aplica a toda a série delitiva.', 'C',
  'É o mesmo raciocínio da **Súmula 711/STF**, que fala em crime continuado ou permanente.',
  juris=[J['STF711']], kw=['crime continuado', 'Súmula 711/STF'])
I(P, 2, 'Crimes contra a dignidade sexual de criança: prescrição',
  'Nos crimes contra a dignidade sexual de criança, a prescrição antes do trânsito em julgado corre da data do fato, ainda que a ação penal não tenha sido proposta.', 'E',
  'Art. 111, V: corre da data em que a vítima completar **18 anos**, salvo se já proposta a ação — regra dos crimes contra a **dignidade sexual** ou com violência contra criança e adolescente.',
  lei=[(CP + '111', 'nos crimes contra a dignidade sexual ou que envolvam violência contra a criança e o adolescente', 'salvo se a esse tempo já houver sido proposta a ação penal', 'CP, art. 111, V')],
  kw=['18 anos', 'dignidade sexual'])

# ======================= PEN-3.4 · Punibilidade =======================
P = 'DBA26-PEN-3.4'
I(P, 1, 'Conceito de punibilidade',
  'Punibilidade é a possibilidade jurídica de o Estado impor a sanção penal ao autor do crime, surgindo com a prática do fato típico, ilícito e culpável.', 'C',
  'É a **consequência jurídica** do crime. Pode ser afastada pelas causas extintivas (art. 107) ou por escusas absolutórias (ex.: art. 181).',
  lei=[(CP + '107', 'Extingue-se a punibilidade:', None, 'CP, art. 107, caput')],
  kw=['punibilidade', 'consequência jurídica'])
I(P, 1, 'Rol do art. 107',
  'O rol de causas extintivas da punibilidade do art. 107 do Código Penal é taxativo.', 'E',
  'É **exemplificativo**: há causas fora dele, como o ressarcimento do dano no peculato culposo (art. 312, § 3º) e o cumprimento da suspensão condicional do processo (Lei 9.099/1995, art. 89, § 5º).',
  lei=[(CP + '312', 'No caso do parágrafo anterior, a reparação do dano, se precede à sentença irrecorrível, extingue a punibilidade', None, 'CP, art. 312, § 3º'),
       ('L9099:89', 'Expirado o prazo sem revogação, o Juiz declarará extinta a punibilidade.', None, 'Lei 9.099/1995, art. 89, § 5º')],
  peg='Chamar o rol de taxativo.', kw=['exemplificativo'])
I(P, 1, 'Medida de segurança e extinção',
  'Extinta a punibilidade, não se impõe medida de segurança nem subsiste a que tenha sido imposta.', 'C',
  'Art. 96, par. ún., do CP: a medida de segurança também se submete às causas extintivas (inclusive a prescrição).',
  lei=[(CP + '96', 'Extinta a punibilidade, não se impõe medida de segurança nem subsiste a que tenha sido imposta.', None, 'CP, art. 96, par. ún.')],
  kw=['medida de segurança', 'extinta a punibilidade'])
I(P, 1, 'Perdão judicial e reincidência',
  'A sentença que concede perdão judicial gera reincidência caso o agente pratique novo crime nos cinco anos seguintes.', 'E',
  'O art. 120 do CP diz que a sentença do perdão judicial **não** será considerada para efeitos de reincidência; para o STJ, ela é **declaratória** da extinção da punibilidade (Súmula 18).',
  lei=[(CP + '120', 'A sentença que conceder perdão judicial não será considerada para efeitos de reincidência.', None, 'CP, art. 120')],
  juris=[J['S18']], peg='Dar efeito de condenação ao perdão judicial.', kw=['perdão judicial', 'reincidência'])
I(P, 1, 'Crime pressuposto',
  'Extinta pela prescrição a punibilidade do furto, extingue-se também a do receptador, pois a receptação depende do crime anterior.', 'E',
  'Art. 108, 1ª parte: a extinção da punibilidade do **crime pressuposto** **não se estende** ao crime que dele depende; a receptação é punível ainda que isento de pena o autor do crime antecedente (art. 180, § 4º).',
  lei=[(CP + '108', 'A extinção da punibilidade de crime que é pressuposto, elemento constitutivo ou circunstância agravante de outro não se estende a este.', None, 'CP, art. 108, 1ª parte')],
  kw=['não se estende', 'crime pressuposto'])
# --- PEN-3.4 · Rodada 2
I(P, 2, 'Crimes conexos',
  'Nos crimes conexos, a extinção da punibilidade de um deles impede, quanto aos outros, a agravação da pena resultante da conexão.', 'E',
  'O art. 108, 2ª parte, diz o contrário: a extinção da punibilidade de um **não impede** a agravação resultante da conexão (ex.: homicídio qualificado para assegurar a impunidade de crime já prescrito).',
  lei=[(CP + '108', 'Nos crimes conexos, a extinção da punibilidade de um deles não impede, quanto aos outros, a agravação da pena resultante da conexão.', None, 'CP, art. 108, 2ª parte')],
  peg='Trocar "não impede" por "impede".', kw=['crimes conexos', 'não impede'])
I(P, 2, 'Concurso de crimes e extinção',
  'No concurso de crimes, a extinção da punibilidade incide sobre a pena de cada um, isoladamente.', 'C',
  'Art. 119 do CP. Por isso, no crime continuado a prescrição despreza o acréscimo da continuidade (Súmula 497/STF).',
  lei=[(CP + '119', 'No caso de concurso de crimes, a extinção da punibilidade incidirá sobre a pena de cada um, isoladamente.', None, 'CP, art. 119')],
  juris=[J['STF497']], kw=['isoladamente', 'concurso de crimes'])
I(P, 2, 'Perdão judicial: natureza',
  'Para o STJ, a sentença concessiva do perdão judicial é condenatória, subsistindo efeitos secundários como o lançamento do nome no rol dos culpados.', 'E',
  'A **Súmula 18/STJ** afirma que a sentença é **declaratória** da extinção da punibilidade, **não subsistindo qualquer efeito condenatório**.',
  juris=[J['S18']], peg='Ver condenação no perdão judicial.', kw=['Súmula 18/STJ', 'declaratória'])

# ======================= PEN-3.5 · Concurso de crimes e crime continuado =======================
P = 'DBA26-PEN-3.5'
I(P, 1, 'Concurso material',
  'No concurso material, o agente, mediante mais de uma ação ou omissão, pratica dois ou mais crimes, idênticos ou não, e as penas privativas de liberdade se somam.', 'C',
  'Art. 69, caput: **cúmulo material**. Se houver reclusão e detenção, executa-se primeiro a reclusão.',
  lei=[(CP + '69', 'Quando o agente, mediante mais de uma ação ou omissão, pratica dois ou mais crimes', 'executa-se primeiro aquela', 'CP, art. 69, caput')],
  kw=['cúmulo material', 'concurso material'])
I(P, 1, 'Concurso formal próprio',
  'No concurso formal próprio, aplica-se a mais grave das penas cabíveis, ou, se iguais, só uma delas, aumentada de um sexto até dois terços.', 'E',
  'No **concurso formal** o aumento é de **1/6 até metade** (art. 70). De 1/6 a 2/3 é o do **crime continuado** (art. 71).',
  lei=[(CP + '70', 'Quando o agente, mediante uma só ação ou omissão, pratica dois ou mais crimes', 'de um sexto até metade', 'CP, art. 70, caput, 1ª parte')],
  peg='Trocar as frações do formal e do continuado.', kw=['de um sexto até metade', 'concurso formal'])
I(P, 1, 'Concurso formal impróprio',
  'Se a ação é dolosa e os crimes concorrentes resultam de desígnios autônomos, as penas se aplicam cumulativamente, ainda que haja uma só ação.', 'C',
  'É o **concurso formal impróprio** (ou imperfeito), art. 70, caput, 2ª parte: segue o cúmulo material.',
  lei=[(CP + '70', 'As penas aplicam-se, entretanto, cumulativamente, se a ação ou omissão é dolosa e os crimes concorrentes resultam de desígnios autônomos', None, 'CP, art. 70, caput, 2ª parte')],
  kw=['desígnios autônomos', 'concurso formal impróprio'])
I(P, 1, 'Cúmulo material benéfico',
  'No concurso formal próprio, a pena resultante da exasperação pode superar a que resultaria da soma das penas, por ser regra legal especial.', 'E',
  'Art. 70, par. ún.: é o **cúmulo material benéfico** — a pena **não pode exceder** a que seria cabível pela regra do art. 69.',
  lei=[(CP + '70', 'Não poderá a pena exceder a que seria cabível pela regra do art. 69 deste Código.', None, 'CP, art. 70, par. ún.')],
  kw=['cúmulo material benéfico'])
I(P, 1, 'Crime continuado: requisitos',
  'O crime continuado exige pluralidade de condutas, crimes da mesma espécie e condições semelhantes de tempo, lugar e maneira de execução, entre outras.', 'C',
  'Art. 71, caput: ficção jurídica que trata a série como continuação do primeiro crime, com aumento de **1/6 a 2/3**.',
  lei=[(CP + '71', 'Quando o agente, mediante mais de uma ação ou omissão, pratica dois ou mais crimes da mesma espécie', 'de um sexto a dois terços', 'CP, art. 71, caput')],
  kw=['mesma espécie', 'crime continuado'])
I(P, 1, 'Fração no crime continuado',
  'Segundo o STJ, no crime continuado a fração de aumento é fixada pelo número de infrações, aplicando-se 1/6 para duas e 2/3 para sete ou mais.', 'C',
  '**Súmula 659/STJ**: 1/6 (2), 1/5 (3), 1/4 (4), 1/3 (5), 1/2 (6) e 2/3 (7 ou mais).',
  juris=[J['S659']], kw=['Súmula 659/STJ', 'número de infrações'])
I(P, 1, 'Multa no concurso',
  'No concurso de crimes, a pena de multa segue a regra da exasperação, aplicando-se uma só multa aumentada.', 'E',
  'Art. 72: as multas são aplicadas **distinta e integralmente**, mesmo no concurso formal e no crime continuado.',
  lei=[(CP + '72', 'No concurso de crimes, as penas de multa são aplicadas distinta e integralmente.', None, 'CP, art. 72')],
  peg='Exasperar a multa.', kw=['distinta e integralmente'])
# --- PEN-3.5 · Rodada 2
I(P, 2, 'Continuidade específica',
  'No crime continuado específico, o juiz pode aumentar a pena até o quádruplo, sem o limite do cúmulo material.', 'E',
  'Art. 71, par. ún.: no **crime continuado específico** o aumento vai **até o triplo**, observados o cúmulo material benéfico (art. 70, par. ún.) e o art. 75.',
  lei=[(CP + '71', 'Nos crimes dolosos, contra vítimas diferentes, cometidos com violência ou grave ameaça à pessoa', 'do parágrafo único do art. 70 e do art. 75 deste Código', 'CP, art. 71, par. ún.')],
  kw=['crime continuado específico', 'até o triplo'])
I(P, 2, 'Prescrição no crime continuado',
  'No crime continuado, a prescrição regula-se pela pena total, incluído o acréscimo decorrente da continuação.', 'E',
  'A **Súmula 497/STF** manda desprezar o **acréscimo da continuação** — coerente com o art. 119 (extinção da punibilidade crime a crime).',
  juris=[J['STF497']], peg='Somar o acréscimo da continuidade na prescrição.', kw=['Súmula 497/STF', 'acréscimo'])
I(P, 2, 'Suspensão condicional do processo e continuidade',
  'Não cabe suspensão condicional do processo por crime continuado se a soma da pena mínima da infração mais grave com o aumento mínimo de um sexto for superior a um ano.', 'C',
  'É a **Súmula 723/STF**; a **Súmula 243/STJ** estende a regra ao concurso material e ao formal.',
  juris=[J['STF723'], J['S243']], kw=['Súmula 723/STF', 'aumento mínimo de um sexto'])
I(P, 2, 'Aberratio ictus com duplo resultado',
  'Se, por erro na execução, o agente atinge a pessoa visada e também terceiro, responde pelos dois crimes em concurso material.', 'E',
  'Na **aberratio ictus** com unidade de resultado múltiplo aplica-se a regra do **concurso formal** (art. 73, parte final, remetendo ao art. 70).',
  lei=[(CP + '73', 'No caso de ser também atingida a pessoa que o agente pretendia ofender, aplica-se a regra do art. 70 deste Código.', None, 'CP, art. 73, parte final')],
  peg='Trocar concurso formal por material.', kw=['aberratio ictus', 'concurso formal'])

# ======================= PEN-3.6 · Conduta, resultado, causalidade e imputação =======================
P = 'DBA26-PEN-3.6'
I(P, 1, 'Equivalência dos antecedentes',
  'Quanto à relação de causalidade, o Código Penal adotou como regra a teoria da causalidade adequada, reservando a equivalência dos antecedentes às causas supervenientes.', 'E',
  'É o inverso: a regra é a **equivalência dos antecedentes** (conditio sine qua non, art. 13, caput); a **causalidade adequada** aparece na causa superveniente relativamente independente (§ 1º).',
  lei=[CAUSA], kw=['conditio sine qua non', 'equivalência dos antecedentes'])
I(P, 1, 'Causa superveniente relativamente independente',
  'A superveniência de causa relativamente independente que, por si só, produz o resultado exclui a imputação do resultado, mas o agente responde pelos atos já praticados.', 'C',
  'Art. 13, § 1º: aqui o CP adota a **causalidade adequada**. Ex.: vítima ferida morre em incêndio no hospital — o agente responde por tentativa.',
  lei=[SUPERV], kw=['causalidade adequada', 'por si só'])
I(P, 1, 'Causa absolutamente independente',
  'Nas causas absolutamente independentes, o agente responde pelo resultado se a sua conduta for anterior à causa que o produziu.', 'E',
  'Nas **absolutamente independentes** (preexistentes, concomitantes ou supervenientes), o resultado **nunca** é imputado ao agente, que responde só pelos atos praticados (normalmente tentativa).',
  lei=[CAUSA], peg='Imputar o resultado causado por fonte totalmente autônoma.', kw=['absolutamente independentes'])
I(P, 1, 'Omissão imprópria: dever de agir',
  'O dever de agir para evitar o resultado incumbe a quem tenha por lei obrigação de cuidado, proteção ou vigilância, a quem de outra forma assumiu a responsabilidade de impedir o resultado e a quem, com seu comportamento anterior, criou o risco.', 'C',
  'São as três fontes do **dever de garantidor** (art. 13, § 2º, a, b e c). Exige-se ainda o **poder** de agir.',
  lei=[OMISSAO], kw=['garantidor', 'devia e podia agir'])
I(P, 1, 'Omissão: poder de agir',
  'O garantidor responde pelo resultado sempre que se omite, ainda que, nas circunstâncias, não tivesse possibilidade física de agir.', 'E',
  'A omissão só é relevante quando o omitente **devia e podia** agir (art. 13, § 2º). Sem possibilidade real, não há omissão penalmente relevante.',
  lei=[OMISSAO], peg='Apagar o "podia".', kw=['devia e podia'])
I(P, 1, 'Resultado naturalístico',
  'Nem todo crime possui resultado naturalístico, mas todo crime possui resultado jurídico (normativo), entendido como a lesão ou o perigo de lesão ao bem jurídico.', 'C',
  'Crimes **formais** e de **mera conduta** dispensam resultado naturalístico (ex.: extorsão, Súmula 96/STJ); o **resultado jurídico** está sempre presente.',
  juris=[J['S96']], kw=['resultado naturalístico', 'resultado jurídico'])
# --- PEN-3.6 · Rodada 2
I(P, 2, 'Causa relativamente independente e erro médico',
  'A morte da vítima por complicação cirúrgica ou infecção hospitalar decorrente dos ferimentos rompe o nexo causal, respondendo o agente apenas por tentativa.', 'E',
  'Para a doutrina majoritária, complicações que se inserem na **linha de desdobramento** da lesão (cirurgia, infecção) **não** produzem o resultado "por si só": o agente responde pelo crime consumado. Rompe o nexo o evento que foge ao desdobramento (incêndio, acidente da ambulância) — art. 13, § 1º.',
  lei=[SUPERV], peg='Tratar o desdobramento natural da lesão como causa que "por si só" produziu o resultado.', kw=['linha de desdobramento', 'por si só'])
I(P, 2, 'Imputação objetiva',
  'Para a teoria da imputação objetiva, não basta a causalidade física: o resultado só é imputado se o agente criou ou incrementou um risco proibido que se realizou no resultado, dentro do alcance do tipo.', 'C',
  'A **imputação objetiva** é formulação doutrinária (Roxin) que corrige excessos da conditio sine qua non (art. 13). **Risco permitido** e diminuição de risco excluem a imputação.',
  lei=[CAUSA], kw=['imputação objetiva', 'risco proibido'])
I(P, 2, 'Ingerência',
  'Quem, com seu comportamento anterior, criou o risco da ocorrência do resultado assume a posição de garantidor.', 'C',
  'É a **ingerência** (art. 13, § 2º, c): ex.: quem empurra outro na piscina por brincadeira deve socorrê-lo.',
  lei=[(CP + '13', 'com seu comportamento anterior, criou o risco da ocorrência do resultado', None, 'CP, art. 13, § 2º, c')],
  kw=['ingerência', 'comportamento anterior'])
I(P, 2, 'Omissão própria e garantidor',
  'Nos crimes omissivos próprios, o omitente responde pelo resultado naturalístico, como se o tivesse causado por ação.', 'E',
  'Nos **omissivos próprios** (ex.: omissão de socorro, art. 135) pune-se a mera inação, sem imputação do resultado; o eventual resultado só majora a pena. A imputação do resultado é própria dos **omissivos impróprios** (art. 13, § 2º).',
  lei=[(CP + '135', 'Deixar de prestar assistência, quando possível fazê-lo sem risco pessoal', None, 'CP, art. 135, caput')],
  peg='Imputar resultado no omissivo próprio.', kw=['omissivos próprios', 'omissivos impróprios'])
