# Pente Fino de Medicina Legal — pontos MLE-10, MLE-11, MLE-12 e MLE-13 (07/11/2026).
from base import I
from mle_juris import J

CPP = 'CPP:'
CP = 'CP:'
CC = 'L10406:'

# ======================= MLE-10 · Imputabilidade penal e capacidade civil =======================
P = 'DBA26-MLE-10'
I(P, 1, 'Critério biopsicológico',
  'Para a inimputabilidade por doença mental ou desenvolvimento mental incompleto ou retardado, o Código Penal adota o critério biopsicológico: exige a causa mental e a inteira incapacidade de entender o caráter ilícito do fato ou de determinar-se, ao tempo da conduta.', 'C',
  'O art. 26 soma o dado **biológico** (doença mental, DMIR) ao **psicológico** (incapacidade de entender ou de se autodeterminar) e ao **momento** da conduta — é o critério **biopsicológico**.',
  lei=[(CP + '26', 'É isento de pena o agente que, por doença mental', 'de determinar-se de acordo com esse entendimento.', 'CP, art. 26')],
  kw=['critério biopsicológico', 'doença mental'])
I(P, 1, 'Menoridade penal',
  'Para os menores de 18 anos, o Código Penal adota o critério biopsicológico, exigindo prova de que não entendiam o caráter ilícito do fato.', 'E',
  'Na **menoridade** o critério é puramente **biológico** (etário): menor de 18 é inimputável sem perguntar sobre entendimento.',
  lei=[(CP + '27', 'Os menores de 18 (dezoito) anos são penalmente inimputáveis', 'legislação especial.', 'CP, art. 27')],
  peg='Levar à idade o critério do art. 26.',
  kw=['critério biológico', 'menores de 18'])
I(P, 1, 'Semi-imputabilidade',
  'Se o agente, por perturbação de saúde mental ou desenvolvimento mental incompleto ou retardado, não era inteiramente capaz de entender o caráter ilícito do fato ou de determinar-se, a pena pode ser reduzida de um a dois terços.', 'C',
  'É a **semi-imputabilidade** do art. 26, parágrafo único: há crime e pena, reduzida — ou substituída por medida de segurança (art. 98).',
  lei=[(CP + '26', 'A pena pode ser reduzida de um a dois terços', 'de determinar-se de acordo com esse entendimento.', 'CP, art. 26, par. ún.')],
  kw=['semi-imputabilidade', 'perturbação de saúde mental'])
I(P, 1, 'Emoção e paixão',
  'A emoção e a paixão, quando intensas, excluem a imputabilidade penal.', 'E',
  'Pelo art. 28, I, **emoção e paixão não excluem** a imputabilidade; podem atenuar ou privilegiar (ex.: violenta emoção no homicídio), salvo se forem sintoma de doença mental.',
  lei=[(CP + '28', 'Não excluem a imputabilidade penal', 'I - a emoção ou a paixão;', 'CP, art. 28, I')],
  peg='Somar "quando intensas" para criar exceção que a lei não faz.',
  kw=['emoção', 'paixão'])
I(P, 1, 'Prazo do exame de insanidade',
  'O exame de insanidade mental não durará mais de quarenta e cinco dias, salvo se os peritos demonstrarem a necessidade de maior prazo.', 'C',
  'Literalidade do art. 150, § 1º: **45 dias**, prorrogáveis por necessidade demonstrada.',
  lei=[(CPP + '150', 'O exame não durará mais de quarenta e cinco dias', 'necessidade de maior prazo.', 'CPP, art. 150, § 1º')],
  kw=['quarenta e cinco dias', 'insanidade mental'])
I(P, 1, 'Insanidade no inquérito',
  'Havendo dúvida sobre a integridade mental do indiciado, o delegado de polícia pode determinar diretamente o exame médico-legal de insanidade no inquérito.', 'E',
  'No inquérito, o exame é ordenado **pelo juiz**, **mediante representação da autoridade policial** (art. 149, § 1º).',
  lei=[(CPP + '149', 'O exame poderá ser ordenado ainda na fase do inquérito', 'ao juiz competente.', 'CPP, art. 149, § 1º')],
  peg='Dar ao delegado o poder que é do juiz.',
  kw=['representação da autoridade policial', 'incidente de insanidade'])
I(P, 1, 'Deficiência e capacidade civil',
  'A pessoa com deficiência tem assegurado o direito ao exercício de sua capacidade legal em igualdade de condições com as demais pessoas.', 'C',
  'Desde o Estatuto da Pessoa com Deficiência, a **deficiência não gera incapacidade** por si só; só menores de 16 anos são absolutamente incapazes.',
  lei=[('L13146:84', 'A pessoa com deficiência tem assegurado', 'igualdade de condições com as demais pessoas.', 'Lei 13.146/2015, art. 84')],
  kw=['capacidade legal', 'pessoa com deficiência'])
I(P, 1, 'Alcance da curatela',
  'A curatela da pessoa com deficiência alcança o direito ao matrimônio e ao voto, quando assim fixar a sentença.', 'E',
  'A **curatela** afeta **só atos patrimoniais e negociais** e **não alcança** corpo, sexualidade, matrimônio, privacidade, educação, saúde, trabalho e voto.',
  lei=[('L13146:85', 'A curatela afetará tão somente', 'ao trabalho e ao voto.', 'Lei 13.146/2015, art. 85, caput e § 1º')],
  peg='Ampliar a curatela além do patrimonial.',
  kw=['curatela', 'patrimonial e negocial'])

# --- MLE-10 · Rodada 2
I(P, 2, 'Medida para o inimputável',
  'Se o agente for inimputável, o juiz determinará sua internação; se o fato for punível com detenção, poderá submetê-lo a tratamento ambulatorial.', 'C',
  'É o art. 97: **internação** como regra; **tratamento ambulatorial** se o crime for punido com detenção.',
  lei=[(CP + '97', 'Se o agente for inimputável', 'tratamento ambulatorial.', 'CP, art. 97')],
  kw=['internação', 'tratamento ambulatorial'])
I(P, 2, 'Prazo mínimo da medida de segurança',
  'O prazo mínimo da internação ou do tratamento ambulatorial é de seis meses a um ano, após o que se realiza a perícia de cessação de periculosidade.', 'E',
  'O prazo mínimo é de **1 a 3 anos**; a perícia se faz ao fim dele e se repete **de ano em ano**.',
  lei=[(CP + '97', 'A internação, ou tratamento ambulatorial, será por tempo indeterminado', 'O prazo mínimo deverá ser de 1 (um) a 3 (três) anos.', 'CP, art. 97, § 1º')],
  peg='Encurtar o prazo mínimo.',
  kw=['prazo mínimo', 'cessação de periculosidade'])
I(P, 2, 'Doença mental superveniente',
  'Se a doença mental sobreveio à infração, o processo continuará suspenso até que o acusado se restabeleça.', 'C',
  'Doença **posterior** ao fato não afeta a imputabilidade, mas impede a defesa: **suspende** o processo (art. 152).',
  lei=[(CPP + '152', 'Se se verificar que a doença mental sobreveio à infração', 'até que o acusado se restabeleça', 'CPP, art. 152')],
  kw=['sobreveio à infração', 'processo suspenso'])
I(P, 2, 'Inimputável ao tempo da infração',
  'Se os peritos concluírem que o acusado era inimputável ao tempo da infração, o processo ficará suspenso até que ele recupere a saúde mental.', 'E',
  'Inimputável **ao tempo do fato**: o processo **prossegue**, com **curador** (art. 151), e pode terminar em absolvição imprópria. Suspensão é para a doença **superveniente**.',
  lei=[(CPP + '151', 'Se os peritos concluírem que o acusado era', 'com a presença do curador.', 'CPP, art. 151')],
  peg='Trocar as consequências dos arts. 151 e 152.',
  kw=['curador', 'ao tempo da infração'])
I(P, 2, 'Transtorno de personalidade antissocial',
  'No transtorno de personalidade antissocial, em regra a capacidade de entendimento está preservada, e a perícia costuma concluir pela imputabilidade ou, no máximo, pela semi-imputabilidade.', 'C',
  'Posição majoritária: o **transtorno de personalidade** não é doença mental psicótica; a crítica está preservada. O juízo é **caso a caso**, pela perícia.',
  kw=['transtorno de personalidade', 'semi-imputabilidade'])
I(P, 2, 'Ébrios habituais e viciados',
  'Os ébrios habituais e os viciados em tóxico são absolutamente incapazes para os atos da vida civil.', 'E',
  'São **relativamente** incapazes (CC, art. 4º, II) e podem ser submetidos a curatela.',
  lei=[(CC + '4', 'São incapazes, relativamente a certos atos', 'II - os ébrios habituais e os viciados em tóxico;', 'CC, art. 4º, caput e II')],
  peg='Trocar relativa por absoluta.',
  kw=['relativamente incapazes', 'ébrios habituais'])
I(P, 2, 'Desenvolvimento mental retardado',
  'A deficiência intelectual (oligofrenia) é exemplo de desenvolvimento mental retardado, enquanto o desenvolvimento mental incompleto abrange, por exemplo, o menor de idade.', 'C',
  '**Retardado**: o desenvolvimento não alcançará a maturidade (deficiência intelectual). **Incompleto**: ainda não se completou (menores; para parte da doutrina, indígena não adaptado ou surdo-mudo sem instrução).',
  kw=['desenvolvimento mental retardado', 'oligofrenia'])

# ======================= MLE-11 · Testemunho, confissão e acareação =======================
P = 'DBA26-MLE-11'
I(P, 1, 'Valor da confissão',
  'O valor da confissão se aferirá pelos critérios adotados para os outros elementos de prova, e o juiz deverá confrontá-la com as demais provas do processo.', 'C',
  'A **confissão** não é a "rainha das provas": vale o que valer no confronto com o resto (art. 197).',
  lei=[(CPP + '197', 'O valor da confissão se aferirá', 'compatibilidade ou concordância.', 'CPP, art. 197')],
  kw=['confissão', 'confrontá-la'])
I(P, 1, 'Características da confissão',
  'A confissão é indivisível e irretratável.', 'E',
  'A confissão é **divisível e retratável**, sem prejuízo do livre convencimento do juiz (art. 200).',
  lei=[(CPP + '200', 'A confissão será divisível e retratável', 'exame das provas em conjunto.', 'CPP, art. 200')],
  peg='Inverter os dois atributos.',
  kw=['divisível', 'retratável'])
I(P, 1, 'Quem pode testemunhar',
  'Toda pessoa poderá ser testemunha.', 'C',
  'Art. 202: a regra é a **capacidade** para testemunhar; o que muda é o compromisso e o valor do depoimento.',
  lei=[(CPP + '202', 'Toda pessoa poderá ser testemunha.', None, 'CPP, art. 202')],
  kw=['testemunha', 'toda pessoa'])
I(P, 1, 'Compromisso',
  'Os doentes mentais e os menores de 14 anos prestam o compromisso de dizer a verdade, como as demais testemunhas.', 'E',
  'Não se defere o **compromisso** aos **doentes e deficientes mentais**, aos **menores de 14 anos** e aos parentes do art. 206: são **informantes**.',
  lei=[(CPP + '208', 'Não se deferirá o compromisso', 'nem às pessoas a que se refere o art. 206.', 'CPP, art. 208')],
  peg='Estender o compromisso a quem a lei dispensa.',
  kw=['compromisso', 'menores de 14'])
I(P, 1, 'Cabimento da acareação',
  'A acareação é admitida entre acusados, entre acusado e testemunha, entre testemunhas, entre acusado ou testemunha e o ofendido, e entre ofendidos, sempre que divergirem sobre fatos ou circunstâncias relevantes.', 'C',
  'A **acareação** confronta declarações divergentes sobre ponto **relevante** (art. 229); é também diligência do inquérito (art. 6º, VI).',
  lei=[(CPP + '229', 'A acareação será admitida entre acusados', 'sobre fatos ou circunstâncias relevantes.', 'CPP, art. 229')],
  kw=['acareação', 'divergirem'])
I(P, 1, 'Confissão como atenuante',
  'Ter o agente confessado espontaneamente, perante a autoridade, a autoria do crime é circunstância agravante.', 'E',
  'A **confissão espontânea** é **atenuante** (art. 65, III, d).',
  lei=[(CP + '65', 'd) confessado espontaneamente', 'a autoria do crime;', 'CP, art. 65, III, d')],
  peg='Trocar atenuante por agravante.',
  kw=['confissão espontânea', 'atenuante'])
I(P, 1, 'Perguntas sugestivas',
  'Por causa da sugestionabilidade da memória, o juiz não admitirá perguntas que puderem induzir a resposta da testemunha.', 'C',
  'A memória é **reconstrutiva** e sujeita a **falsas memórias**; a vedação de perguntas **indutivas** (art. 212) protege a qualidade do testemunho.',
  lei=[(CPP + '212', 'As perguntas serão formuladas pelas partes diretamente à testemunha', 'repetição de outra já respondida.', 'CPP, art. 212')],
  kw=['falsas memórias', 'induzir a resposta'])
I(P, 1, 'Silêncio do acusado',
  'O silêncio do acusado no interrogatório pode ser interpretado em prejuízo da defesa.', 'E',
  'O silêncio **não importa confissão** e **não pode ser interpretado em prejuízo da defesa** (art. 186, parágrafo único). A parte final do art. 198 é tida como não recepcionada.',
  lei=[(CPP + '186', 'O silêncio, que não importará em confissão', 'em prejuízo da defesa.', 'CPP, art. 186, par. ún.')],
  peg='Aplicar a redação antiga do art. 198.',
  kw=['silêncio', 'prejuízo da defesa'])

# --- MLE-11 · Rodada 2
I(P, 2, 'Fases do testemunho',
  'Na psicologia do testemunho, distinguem-se a percepção do fato, sua conservação na memória e sua evocação no depoimento, e cada fase pode sofrer distorções.', 'C',
  '**Percepção** (atenção, emoção, condições do local), **conservação** (tempo, interferências) e **evocação** (forma da pergunta, ambiente): erro de boa-fé não é mentira.',
  kw=['psicologia do testemunho', 'evocação'])
I(P, 2, 'Testemunho infantil',
  'O testemunho da criança, por ser espontâneo e desprovido de interesse, é imune à sugestão.', 'E',
  'A criança é **mais sugestionável** a perguntas indutivas e a pressões de adultos; daí a escuta especializada e o depoimento especial, com protocolos próprios.',
  peg='Confundir sinceridade com imunidade à sugestão.',
  kw=['testemunho infantil', 'sugestionável'])
I(P, 2, 'Autoacusação falsa',
  'Quadros psicopatológicos, como a depressão grave com ideias de culpa e os delírios, podem levar a confissões falsas, razão a mais para confrontar a confissão com as demais provas.', 'C',
  'A **autoacusação falsa** tem causas psíquicas, coação, sugestão ou proteção de terceiro; o art. 197 manda conferir a **compatibilidade** com o resto da prova.',
  lei=[(CPP + '197', 'O valor da confissão se aferirá', 'compatibilidade ou concordância.', 'CPP, art. 197')],
  kw=['autoacusação', 'confissões falsas'])
I(P, 2, 'Acareação com testemunha ausente',
  'Se a testemunha cujas declarações divergem estiver ausente, a acareação fica prejudicada e não pode ser realizada.', 'E',
  'O art. 230 prevê a **acareação por precatória**: dá-se à testemunha presente ciência dos pontos de divergência e, persistindo, ouve-se a ausente onde reside — se não houver demora prejudicial e o juiz entender conveniente.',
  lei=[(CPP + '230', 'Se ausente alguma testemunha', 'consignando-se no auto o que explicar ou observar.', 'CPP, art. 230')],
  peg='Negar a modalidade por precatória.',
  kw=['precatória', 'acareação'])
I(P, 2, 'Depoimento especial',
  'Depoimento especial é o procedimento de oitiva de criança ou adolescente vítima ou testemunha de violência perante autoridade policial ou judiciária.', 'C',
  'Literalidade do art. 8º da Lei 13.431/2017: oitiva **perante autoridade policial ou judiciária**.',
  lei=[('L13431:8', 'Depoimento especial é o procedimento de oitiva', 'autoridade policial ou judiciária.', 'Lei 13.431/2017, art. 8º')],
  kw=['depoimento especial', 'criança ou adolescente'])
I(P, 2, 'Apreciações pessoais',
  'O juiz deve permitir que a testemunha manifeste livremente suas apreciações pessoais sobre o fato.', 'E',
  'O juiz **não permitirá** apreciações pessoais, **salvo quando inseparáveis da narrativa** (art. 213): testemunha relata fatos, não opina.',
  lei=[(CPP + '213', 'O juiz não permitirá que a testemunha manifeste suas apreciações pessoais', 'inseparáveis da narrativa do fato.', 'CPP, art. 213')],
  peg='Trocar a vedação por permissão.',
  kw=['apreciações pessoais', 'narrativa do fato'])

# ======================= MLE-12 · Cadeia de custódia, vestígios e evidências =======================
P = 'DBA26-MLE-12'
I(P, 1, 'Conceito de cadeia de custódia',
  'Cadeia de custódia é o conjunto de todos os procedimentos utilizados para manter e documentar a história cronológica do vestígio coletado em locais ou em vítimas de crimes, para rastrear sua posse e manuseio desde o reconhecimento até o descarte.', 'C',
  'Conceito legal do art. 158-A (Pacote Anticrime): **história cronológica** do vestígio, do **reconhecimento ao descarte**.',
  lei=[(CPP + '158-A', 'Considera-se cadeia de custódia', 'a partir de seu reconhecimento até o descarte.', 'CPP, art. 158-A')],
  kw=['cadeia de custódia', 'história cronológica'])
I(P, 1, 'Início da cadeia',
  'A cadeia de custódia tem início com o recebimento do vestígio na central de custódia do instituto de criminalística.', 'E',
  'Começa com a **preservação do local de crime** ou com procedimentos policiais ou periciais em que se detecte o vestígio (§ 1º).',
  lei=[(CPP + '158-A', 'O início da cadeia de custódia dá-se', 'seja detectada a existência de vestígio.', 'CPP, art. 158-A, § 1º')],
  peg='Atrasar o marco inicial para o laboratório.',
  kw=['início da cadeia de custódia', 'preservação do local'])
I(P, 1, 'Conceito de vestígio',
  'Vestígio é todo objeto ou material bruto, visível ou latente, constatado ou recolhido, que se relaciona à infração penal.', 'C',
  'O **vestígio** é o dado **bruto**, ainda não analisado; pode ser **latente** (impressão digital, sangue lavado).',
  lei=[(CPP + '158-A', 'Vestígio é todo objeto ou material bruto', 'que se relaciona à infração penal.', 'CPP, art. 158-A, § 3º')],
  kw=['vestígio', 'latente'])
I(P, 1, 'Fixação × coleta',
  'Na cadeia de custódia, fixação é o ato de recolher o vestígio que será submetido à análise pericial.', 'E',
  'Recolher é a **coleta**. **Fixação** é a **descrição detalhada** do vestígio como se encontra no local ou no corpo, com fotos, filmagens ou croqui, indispensável no laudo.',
  lei=[(CPP + '158-B', 'III - fixação', 'perito responsável pelo atendimento;', 'CPP, art. 158-B, III')],
  peg='Trocar o nome das etapas.',
  kw=['fixação', 'coleta'])
I(P, 1, 'Abertura do recipiente',
  'O recipiente do vestígio só poderá ser aberto pelo perito que vai proceder à análise e, motivadamente, por pessoa autorizada.', 'C',
  'Art. 158-D, § 3º: abertura **restrita** e **motivada**.',
  lei=[(CPP + '158-D', 'O recipiente só poderá ser aberto pelo perito', 'motivadamente, por pessoa autorizada.', 'CPP, art. 158-D, § 3º')],
  kw=['recipiente', 'pessoa autorizada'])
I(P, 1, 'Lacre rompido',
  'Após o rompimento do lacre, o lacre antigo deve ser descartado, registrando-se apenas o número do novo lacre.', 'E',
  'O **lacre rompido** vai **dentro do novo recipiente** (§ 5º), e a ficha registra responsável, data, local, finalidade e novo lacre (§ 4º).',
  lei=[(CPP + '158-D', 'O lacre rompido deverá ser acondicionado', 'interior do novo recipiente.', 'CPP, art. 158-D, § 5º')],
  peg='Mandar descartar o que a lei manda guardar.',
  kw=['lacre rompido', 'novo recipiente'])
I(P, 1, 'Central de custódia',
  'Todos os Institutos de Criminalística deverão ter uma central de custódia destinada à guarda e controle dos vestígios, vinculada diretamente ao órgão central de perícia oficial de natureza criminal.', 'C',
  'Art. 158-E: **central de custódia** em todo Instituto de Criminalística.',
  lei=[(CPP + '158-E', 'Todos os Institutos de Criminalística deverão ter uma central de custódia', 'órgão central de perícia oficial de natureza criminal.', 'CPP, art. 158-E')],
  kw=['central de custódia', 'Institutos de Criminalística'])
I(P, 1, 'Quebra da cadeia',
  'Para o STJ, a quebra da cadeia de custódia gera nulidade automática da prova, que deve ser desentranhada dos autos.', 'E',
  'A 6ª Turma do STJ (HC 653.515/RJ) decidiu que a quebra **não gera nulidade automática**: o juiz **sopesa** a irregularidade com os demais elementos para aferir a **confiabilidade** da prova.',
  juris=[J['HC653515']],
  peg='Transformar questão de valoração em nulidade automática.',
  kw=['quebra da cadeia de custódia', 'nulidade automática'])

# --- MLE-12 · Rodada 2
I(P, 2, 'Responsável pela preservação',
  'O agente público que reconhecer um elemento como de potencial interesse para a produção da prova pericial fica responsável por sua preservação.', 'C',
  'Art. 158-A, § 2º: quem reconhece, **preserva** — inclusive o policial que chega primeiro.',
  lei=[(CPP + '158-A', 'O agente público que reconhecer um elemento', 'fica responsável por sua preservação.', 'CPP, art. 158-A, § 2º')],
  kw=['responsável por sua preservação', 'agente público'])
I(P, 2, 'Destino após a perícia',
  'Após a realização da perícia, o material deverá ser encaminhado ao cartório judicial, onde permanecerá até o trânsito em julgado.', 'E',
  'O material **volta à central de custódia** e lá permanece (art. 158-F); sem espaço, a autoridade define outro depósito a pedido do diretor da perícia.',
  lei=[(CPP + '158-F', 'Após a realização da perícia', 'devendo nela permanecer.', 'CPP, art. 158-F')],
  peg='Trocar o destino legal do vestígio.',
  kw=['central de custódia', 'após a realização da perícia'])
I(P, 2, 'Coleta e exames complementares',
  'O perito oficial que coletar os vestígios dará o encaminhamento necessário para a central de custódia, mesmo quando for necessária a realização de exames complementares.', 'C',
  'Art. 158-C, caput: o fluxo passa **sempre** pela central de custódia.',
  lei=[(CPP + '158-C', 'A coleta dos vestígios deverá ser realizada preferencialmente', 'mesmo quando for necessária a realização de exames complementares.', 'CPP, art. 158-C')],
  kw=['central de custódia', 'exames complementares'])
I(P, 2, 'Alcance do isolamento',
  'O isolamento, etapa da cadeia de custódia, abrange apenas o ambiente imediato do local de crime.', 'E',
  'O **isolamento** alcança os ambientes **imediato, mediato e relacionado** aos vestígios e ao local de crime (art. 158-B, II).',
  lei=[(CPP + '158-B', 'II - isolamento', 'relacionado aos vestígios e local de crime;', 'CPP, art. 158-B, II')],
  peg='Encolher o alcance do isolamento.',
  kw=['isolamento', 'mediato'])
I(P, 2, 'Vestígio, evidência e indício',
  'Na doutrina, o vestígio é o material bruto; a evidência é o vestígio já analisado e relacionado tecnicamente ao fato; e o indício, definido no art. 239 do CPP, é circunstância já provada que, ligada ao fato, permite inferir por indução a existência de outra.', 'C',
  'A sequência é **vestígio → evidência → indício**: o laudo transforma o vestígio em evidência; o indício é categoria jurídica de prova (art. 239).',
  lei=[(CPP + '239', 'Considera-se indício a circunstância conhecida e provada', 'outra ou outras circunstâncias.', 'CPP, art. 239')],
  kw=['vestígio', 'evidência', 'indício'])
I(P, 2, 'Acesso à central de custódia',
  'Os servidores lotados na central de custódia estão dispensados de identificação e registro quando acessarem o vestígio armazenado.', 'E',
  '**Todas as pessoas** que acessarem o vestígio armazenado devem ser **identificadas**, com registro de data e hora (art. 158-E, § 3º).',
  lei=[(CPP + '158-E', 'Todas as pessoas que tiverem acesso ao vestígio armazenado', 'a data e a hora do acesso.', 'CPP, art. 158-E, § 3º')],
  peg='Criar exceção que a lei não traz.',
  kw=['todas as pessoas', 'registro de acesso'])

# ======================= MLE-13 · Violência doméstica e contra vulneráveis =======================
P = 'DBA26-MLE-13'
I(P, 1, 'Prioridade do exame',
  'Têm prioridade no exame de corpo de delito os crimes de violência doméstica e familiar contra a mulher e os cometidos com violência contra criança, adolescente, idoso ou pessoa com deficiência.', 'C',
  'Lei 13.721/2018, que incluiu o parágrafo único do art. 158: **prioridade** para os vulneráveis.',
  lei=[(CPP + '158', 'Dar-se-á prioridade à realização do exame de corpo de delito', 'idoso ou pessoa com deficiência.', 'CPP, art. 158, par. ún.')],
  kw=['prioridade', 'violência doméstica'])
I(P, 1, 'Coabitação',
  'Para a configuração da violência doméstica e familiar contra a mulher, exige-se coabitação entre autor e vítima.', 'E',
  'Basta **relação íntima de afeto**, **independentemente de coabitação** (art. 5º, III; Súmula 600/STJ).',
  lei=[('L11340:5', 'III - em qualquer relação íntima de afeto', 'independentemente de coabitação.', 'Lei 11.340/2006, art. 5º, III')],
  juris=[J['S600']],
  peg='Exigir requisito expressamente dispensado.',
  kw=['coabitação', 'relação íntima de afeto'])
I(P, 1, 'Exame da ofendida',
  'Na Lei Maria da Penha, a autoridade policial deve, de imediato, determinar que se proceda ao exame de corpo de delito da ofendida e requisitar outros exames periciais necessários.', 'C',
  'Art. 12, IV: providência **imediata** após o registro da ocorrência.',
  lei=[('L11340:12', 'IV - determinar que se proceda ao exame de corpo de delito da ofendida', 'outros exames periciais necessários;', 'Lei 11.340/2006, art. 12, IV')],
  kw=['exame de corpo de delito', 'ofendida'])
I(P, 1, 'Ação penal na lesão doméstica',
  'A ação penal no crime de lesão corporal resultante de violência doméstica contra a mulher é pública condicionada à representação, quando a lesão for leve.', 'E',
  'É **pública incondicionada**, qualquer que seja a extensão da lesão (Súmula 542/STJ).',
  juris=[J['S542']],
  peg='Aplicar a regra da lesão leve comum (Lei 9.099/1995).',
  kw=['pública incondicionada', 'lesão corporal'])
I(P, 1, 'Maus-tratos contra criança',
  'Os casos de suspeita ou confirmação de castigo físico, de tratamento cruel ou degradante e de maus-tratos contra criança ou adolescente serão obrigatoriamente comunicados ao Conselho Tutelar.', 'C',
  'ECA, art. 13: comunicação **obrigatória** já na **suspeita**, sem prejuízo de outras providências (inclusive policiais).',
  lei=[('L8069:13', 'Os casos de suspeita ou confirmação de castigo físico', 'sem prejuízo de outras providências legais.', 'ECA, art. 13')],
  kw=['Conselho Tutelar', 'maus-tratos'])
I(P, 1, 'Notificação de violência contra idoso',
  'A notificação compulsória de violência contra pessoa idosa só é exigida quando a violência estiver confirmada pelo serviço de saúde.', 'E',
  'A notificação alcança a **suspeita ou confirmação** e deve ser comunicada também à autoridade policial e ao MP, entre outros (art. 19).',
  lei=[('L10741:19', 'Os casos de suspeita ou confirmação de violência praticada contra pessoas idosas', 'I – autoridade policial;', 'Lei 10.741/2003, art. 19')],
  peg='Retirar a "suspeita" do texto.',
  kw=['suspeita ou confirmação', 'notificação compulsória'])
I(P, 1, 'Síndrome da criança espancada',
  'Lesões em diferentes estágios de evolução, fraturas em fases distintas de consolidação e história incompatível com os achados sugerem a síndrome da criança espancada.', 'C',
  'A **síndrome da criança espancada** se reconhece pela **repetição** (lesões de idades diferentes) e pela **incompatibilidade** entre relato e lesão.',
  kw=['síndrome da criança espancada', 'história incompatível'])
I(P, 1, 'Pena da lesão doméstica',
  'A lesão corporal praticada no contexto de violência doméstica é punida com detenção, de três meses a três anos.', 'E',
  'Desde a Lei 14.994/2024, o § 9º do art. 129 prevê **reclusão, de 2 a 5 anos**.',
  lei=[(CP + '129', 'Pena – reclusão, de 2 (dois) a 5 (cinco) anos.', None, 'CP, art. 129, § 9º, pena')],
  peg='Usar a pena antiga, anterior a 2024.',
  kw=['reclusão', 'violência doméstica'])

# --- MLE-13 · Rodada 2
I(P, 2, 'Bebê sacudido',
  'Na síndrome do bebê sacudido, podem coexistir hematoma subdural, hemorragias retinianas e lesão encefálica com pouca ou nenhuma lesão externa.', 'C',
  'A aceleração e desaceleração da cabeça rompe veias pontes; a **falta de marca na pele** não exclui a agressão.',
  kw=['bebê sacudido', 'hemorragias retinianas'])
I(P, 2, 'Lesões de defesa',
  'Equimoses e feridas na face ulnar dos antebraços e nas mãos são a localização típica das quedas acidentais.', 'E',
  'Antebraços e mãos são sede típica das **lesões de defesa**. **Quedas acidentais** atingem proeminências (testa, queixo, cotovelos, joelhos).',
  peg='Trocar defesa por queda acidental.',
  kw=['lesões de defesa', 'quedas acidentais'])
I(P, 2, 'Violência psicológica',
  'Para a Lei Maria da Penha, violência psicológica é qualquer conduta que cause dano emocional e diminuição da autoestima, e sua demonstração pode contar com perícia psicológica ou psiquiátrica.', 'C',
  'O art. 7º, II, descreve a **violência psicológica**; o dano emocional pode ser objeto de **perícia** psíquica.',
  lei=[('L11340:7', 'II - a violência psicológica', 'dano emocional e diminuição da autoestima', 'Lei 11.340/2006, art. 7º, II')],
  kw=['violência psicológica', 'dano emocional'])
I(P, 2, 'Avaliação da deficiência',
  'A avaliação da deficiência, quando necessária, é exclusivamente médica, feita por perito médico.', 'E',
  'A avaliação é **biopsicossocial**, por **equipe multiprofissional e interdisciplinar** (Lei 13.146/2015, art. 2º, § 1º).',
  lei=[('L13146:2', 'A avaliação da deficiência, quando necessária, será biopsicossocial', 'equipe multiprofissional e interdisciplinar', 'Lei 13.146/2015, art. 2º, § 1º')],
  peg='Reduzir ao médico uma avaliação multiprofissional.',
  kw=['biopsicossocial', 'multiprofissional'])
I(P, 2, 'Cor das equimoses e agressões repetidas',
  'Equimoses de colorações diferentes no mesmo corpo sugerem lesões de idades distintas, compatíveis com agressões repetidas, embora a cor isolada não permita datar cada uma com precisão.', 'C',
  'É indício de **repetição** — dado valioso na violência doméstica —, mas a cronologia pela **cor** é imprecisa.',
  kw=['equimoses', 'agressões repetidas'])
I(P, 2, 'Criança que presencia violência',
  'A exposição da criança a crime violento contra membro de sua família, tornando-a testemunha, não é considerada violência psicológica contra ela pela Lei 13.431/2017.', 'E',
  'A Lei 13.431/2017 a define expressamente como **violência psicológica** (art. 4º, II, c).',
  lei=[('L13431:4', 'c) qualquer conduta que exponha a criança ou o adolescente', 'particularmente quando isto a torna testemunha;', 'Lei 13.431/2017, art. 4º, II, c')],
  peg='Negar hipótese expressa.',
  kw=['violência psicológica', 'testemunha'])
I(P, 2, 'Violência vicária',
  'A Lei Maria da Penha passou a prever a violência vicária, praticada contra descendente, ascendente, dependente ou pessoa da rede de apoio da mulher, com o objetivo de atingi-la.', 'C',
  'Inciso VI do art. 7º, incluído pela Lei 15.384/2026: a **violência vicária** atinge terceiros para ferir a mulher.',
  lei=[('L11340:7', 'VI – a violência vicária', 'com vistas a atingi-la.', 'Lei 11.340/2006, art. 7º, VI')],
  kw=['violência vicária', 'rede de apoio'])
