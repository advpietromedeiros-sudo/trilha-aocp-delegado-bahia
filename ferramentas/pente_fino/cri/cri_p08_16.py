# Pente Fino de Criminologia — pontos CRI-8 (com o tópico 9 do edital), CRI-10 a CRI-16 (07/11/2026).
from base import I

CF = 'CF:'
CPP = 'CPP:'
DEL = 'L12830:'

# ============ CRI-8 · Sociedade criminógena; Sociologia Criminal e desorganização social;
# ============ (9) subcultura delinquente e anomia; perspectiva interacionista
P = 'DBA26-CRI-8'
I(P, 1, 'Normalidade do crime em Durkheim',
  'Para Durkheim, o crime é fenômeno normal, presente em todas as sociedades, e pode ser funcional, reforçando a consciência coletiva e permitindo a evolução moral; torna-se patológico apenas quando excede certos níveis.', 'C',
  '**Durkheim**: o crime é **normal** e até **funcional**; patológico é o **excesso**.',
  kw=['fenômeno normal', 'Durkheim'])
I(P, 1, 'Crime como patologia',
  'Para Durkheim, o crime é fenômeno patológico, a ser erradicado da sociedade saudável.', 'E',
  'Para **Durkheim**, uma sociedade sem crime é impossível: o crime é **normal**.',
  peg='Inverter a tese central.',
  kw=['normal', 'Durkheim'])
I(P, 1, 'Anomia em Durkheim',
  'Em Durkheim, a anomia é o enfraquecimento ou a ausência de normas que regulem as condutas, situação típica de períodos de mudanças sociais bruscas.', 'C',
  'Anomia **durkheimiana** = **desregramento**, falta de normas em **crises**.',
  kw=['anomia', 'ausência de normas'])
I(P, 1, 'Anomia em Merton',
  'Para Merton, a anomia resulta da disjunção entre as metas culturais, como o sucesso econômico, e os meios institucionalizados para alcançá-las, acessíveis de forma desigual.', 'C',
  'Anomia **mertoniana** = **tensão estrutural** entre **metas** e **meios**.',
  kw=['metas culturais', 'meios institucionalizados'])
I(P, 1, 'Modos de adaptação',
  'Merton descreveu cinco modos de adaptação individual: conformidade, inovação, ritualismo, retraimento e rebelião.', 'C',
  'Os **cinco modos**: **conformidade** (aceita metas e meios), **inovação** (metas sim, meios não), **ritualismo** (abandona metas, segue meios), **retraimento** (rejeita ambos), **rebelião** (rejeita e substitui ambos).',
  kw=['modos de adaptação', 'inovação'])
I(P, 1, 'Ritualismo × inovação',
  'No modo de adaptação de Merton denominado ritualismo, o indivíduo aceita as metas culturais, mas rejeita os meios institucionalizados, recorrendo ao crime.', 'E',
  'Aceitar metas e rejeitar meios é a **inovação** (típica do crime patrimonial). No **ritualismo**, abandonam-se as metas e seguem-se os meios por rotina.',
  peg='Trocar inovação por ritualismo.',
  kw=['inovação', 'ritualismo'])
I(P, 1, 'Zonas concêntricas',
  'No modelo de zonas concêntricas da Escola de Chicago, a maior criminalidade concentra-se na zona de transição, independentemente do grupo étnico que a ocupe em cada época.', 'C',
  'Shaw e McKay mostraram que a criminalidade acompanha a **área** (**zona de transição**), não o grupo — prova da **desorganização social**.',
  kw=['zona de transição', 'desorganização social'])
I(P, 1, 'Desorganização social',
  'A desorganização social é o fortalecimento das instituições comunitárias de controle informal, como família, vizinhança e associações, em áreas marcadas por mobilidade e heterogeneidade.', 'E',
  'É o **enfraquecimento**, não o fortalecimento: a **desorganização social** debilita o **controle informal** e favorece o crime.',
  peg='Trocar enfraquecimento por fortalecimento.',
  kw=['desorganização social', 'controle informal'])
I(P, 1, 'Caráter da subcultura',
  'Para Albert Cohen, a subcultura delinquente é utilitária, voltada à obtenção de lucro, e reproduz os valores da classe média.', 'E',
  'A subcultura de **Cohen** é **não utilitária**, **maliciosa** e **negativista**: **inverte** os valores da classe média.',
  peg='Trocar "não utilitária" por "utilitária".',
  kw=['não utilitária', 'Albert Cohen'])
I(P, 1, 'Perspectiva interacionista',
  'A perspectiva interacionista, fundada no interacionismo simbólico, entende que comportamento e identidade se constroem nas interações e nos significados atribuídos pelos outros, e é a base do labelling approach.', 'C',
  'O **interacionismo simbólico** (Mead, Blumer) sustenta o **labelling**: o desvio nasce da **interação** e da **definição**.',
  kw=['interacionismo simbólico', 'labelling approach'])

# --- CRI-8 · Rodada 2
I(P, 2, 'Retraimento × rebelião',
  'Para Merton, no retraimento o indivíduo rejeita as metas e os meios e procura substituí-los por uma nova ordem social.', 'E',
  'Substituir metas e meios por nova ordem é a **rebelião**. No **retraimento**, o indivíduo apenas **foge** (rejeita ambos, sem propor nada).',
  peg='Trocar retraimento por rebelião.',
  kw=['retraimento', 'rebelião'])
I(P, 2, 'Anomia: Durkheim × Merton',
  'Em Durkheim, a anomia é falta de normas em períodos de crise; em Merton, é a disjunção entre fins culturais e meios institucionais, inerente à própria estrutura social.', 'C',
  '**Durkheim**: anomia **conjuntural** (crise). **Merton**: anomia **estrutural** (metas × meios).',
  kw=['Durkheim', 'Merton'])
I(P, 2, 'Sociedade criminógena',
  'A expressão sociedade criminógena remete à ideia de que fatores estruturais da própria sociedade, como desigualdade, exclusão e estímulo ao consumo, favorecem a criminalidade, e não apenas características individuais.', 'C',
  'A **sociedade criminógena** desloca o foco do indivíduo para a **estrutura social**.',
  kw=['sociedade criminógena', 'fatores estruturais'])
I(P, 2, 'Saturação criminal',
  'Lombroso formulou a lei da saturação criminal, segundo a qual, em determinado meio físico e social, ocorre um número correspondente de delitos.', 'E',
  'A **lei da saturação criminal** é de **Ferri**, marco da **Sociologia Criminal** positivista; Lombroso é o expoente da fase antropológica.',
  peg='Trocar o autor.',
  kw=['saturação criminal', 'Ferri'])
I(P, 2, 'Alcance da subcultura',
  'A teoria da subcultura delinquente explica sobretudo a delinquência juvenil de grupos das classes baixas, e não a criminalidade das elites.', 'C',
  'A **subcultura** foi pensada para **gangues juvenis** de classes baixas — limitação apontada pelos críticos.',
  kw=['delinquência juvenil', 'subcultura'])
I(P, 2, 'Objeto do interacionismo',
  'A perspectiva interacionista ocupa-se prioritariamente das causas biológicas do comportamento desviante.', 'E',
  'O interacionismo estuda a **interação social** e os **processos de definição** — nada de causas biológicas.',
  peg='Atribuir ao interacionismo o enfoque biológico.',
  kw=['interação social', 'processos de definição'])
I(P, 2, 'Métodos e programas de Chicago',
  'A Escola de Chicago valeu-se de estatísticas, mapas e observação participante e inspirou programas comunitários de prevenção, como o Chicago Area Project.', 'C',
  'Chicago uniu **pesquisa empírica** e **intervenção comunitária** (Chicago Area Project).',
  kw=['Chicago Area Project', 'pesquisa empírica'])
I(P, 2, 'Transmissão cultural',
  'Para Shaw e McKay, a persistência da criminalidade nas mesmas áreas explica-se também pela transmissão cultural de valores delinquentes entre gerações de moradores.', 'C',
  '**Desorganização** + **transmissão cultural**: as áreas "ensinam" o crime às novas gerações.',
  kw=['transmissão cultural', 'Shaw e McKay'])

# ======================= CRI-10 · Paradigma da reação social =======================
P = 'DBA26-CRI-10'
I(P, 1, 'Labelling approach',
  'O labelling approach, também chamado teoria do etiquetamento, da rotulação ou da reação social, surgiu nos Estados Unidos nos anos 1960, com autores como Becker, Lemert, Goffman e Kitsuse.', 'C',
  '**Labelling** = etiquetamento = rotulação = reação social; anos **1960**, EUA.',
  kw=['labelling approach', 'etiquetamento'])
I(P, 1, 'Becker',
  'Para Becker, os grupos sociais criam o desvio ao fazer as regras cuja infração o constitui e ao aplicá-las a pessoas determinadas, rotulando-as como outsiders.', 'C',
  '**Becker** (Outsiders, 1963): desviante é quem recebeu o **rótulo** com sucesso.',
  kw=['Becker', 'outsiders'])
I(P, 1, 'Desvio primário e secundário',
  'Para Lemert, o desvio primário é o ato inicial, sem repercussão na identidade do agente, e o desvio secundário é a resposta à reação social, com a assunção do papel de desviante.', 'C',
  '**Lemert**: **primário** (ato inicial) × **secundário** (identidade desviante assumida após a reação social).',
  kw=['desvio primário', 'desvio secundário'])
I(P, 1, 'Ordem do desvio',
  'Para Lemert, o desvio secundário é o primeiro ato desviante, anterior a qualquer reação social.', 'E',
  'O primeiro ato é o desvio **primário**; o **secundário** é **posterior** e decorre da **reação social**.',
  peg='Inverter primário e secundário.',
  kw=['desvio primário', 'reação social'])
I(P, 1, 'Instituições totais',
  'Becker estudou as instituições totais, como prisões e manicômios, e os processos de mortificação do eu que nelas ocorrem.', 'E',
  'As **instituições totais** e a **mortificação do eu** são de **Goffman** (também autor da obra sobre **estigma**). Becker é o autor de Outsiders.',
  peg='Trocar o autor.',
  kw=['instituições totais', 'Goffman'])
I(P, 1, 'Mudança de enfoque',
  'O labelling approach desloca a investigação das causas do crime para os processos de criminalização e para a reação das instâncias de controle.', 'C',
  'Da pergunta "**por que** delinque?" para "**quem é definido** como delinquente?".',
  kw=['processos de criminalização', 'labelling approach'])
I(P, 1, 'Propostas político-criminais',
  'Ao labelling associam-se propostas político-criminais como descriminalização, diversão, desinstitucionalização e devido processo legal.', 'C',
  'É a política dos "**Ds**" — o número varia entre autores, mas o núcleo é **descriminalização, diversão, desinstitucionalização e devido processo**.',
  kw=['descriminalização', 'diversão'])
I(P, 1, 'Labelling e consenso',
  'O labelling approach é teoria do consenso, pois aceita a definição oficial do crime como neutra.', 'E',
  'O **labelling** é teoria do **conflito** e **questiona** a neutralidade das definições oficiais.',
  peg='Trocar a família teórica.',
  kw=['teoria do conflito', 'labelling'])

# --- CRI-10 · Rodada 2
I(P, 2, 'Crítica de Baratta ao labelling',
  'A Criminologia crítica reconhece o mérito do labelling, mas aponta que ele não explica por que certos grupos detêm o poder de definição, o que exige análise das estruturas econômicas e de poder.', 'C',
  '**Baratta**: o labelling ficou no plano **micro**; falta a **economia política** do poder de definir.',
  kw=['poder de definição', 'Baratta'])
I(P, 2, 'Profecia autorrealizável',
  'Segundo o labelling, o rótulo de criminoso tende a operar como profecia que se autorrealiza, favorecendo a carreira criminal.', 'C',
  'O rótulo vira **profecia autorrealizável**: a pessoa passa a agir conforme a etiqueta.',
  kw=['profecia autorrealizável', 'carreira criminal'])
I(P, 2, 'Cerimônias degradantes',
  'As cerimônias degradantes, descritas por Durkheim, são rituais pelos quais se rebaixa publicamente o status da pessoa, atribuindo-lhe identidade inferior.', 'E',
  'As **cerimônias degradantes** foram descritas por **Garfinkel**, autor ligado à perspectiva interacionista; processo penal e prisão funcionam como tais.',
  peg='Trocar o autor.',
  kw=['cerimônias degradantes', 'Garfinkel'])
I(P, 2, 'Diversão',
  'A diversão (diversion) consiste em agravar a resposta penal para autores de infrações leves, evitando a impunidade.', 'E',
  '**Diversão** é **desviar** o caso do processo penal formal, por vias alternativas, para **evitar o estigma**.',
  peg='Inverter o sentido da diversão.',
  kw=['diversão', 'evitar o estigma'])
I(P, 2, 'Cifra dourada',
  'A cifra dourada designa a criminalidade das camadas privilegiadas, como crimes financeiros, tributários e ambientais, que raramente chega a ser punida.', 'C',
  'A **cifra dourada** é a criminalidade **das elites** que escapa ao sistema.',
  kw=['cifra dourada', 'elites'])
I(P, 2, 'Criminalização secundária',
  'Para o labelling, a criminalização secundária recai igualitariamente sobre todas as classes sociais.', 'E',
  'A criminalização secundária é **seletiva**: recai preferencialmente sobre os **vulneráveis**.',
  peg='Trocar seletiva por igualitária.',
  kw=['seletiva', 'criminalização secundária'])

# ======================= CRI-11 · América Latina e agências de controle =======================
P = 'DBA26-CRI-11'
I(P, 1, 'Criminologia crítica latino-americana',
  'A Criminologia crítica latino-americana, com autores como Lola Aniyar de Castro, Rosa del Olmo e Eugenio Raúl Zaffaroni, analisa o sistema penal a partir da realidade periférica da região.', 'C',
  'Uma **criminologia da região**, atenta à **periferia** e à **violência estrutural**.',
  kw=['América Latina', 'Zaffaroni'])
I(P, 1, 'Agências do sistema penal',
  'Para Zaffaroni, integram o sistema penal em sentido amplo não só as agências policiais, judiciais e penitenciárias, mas também as políticas, as de comunicação social e as de reprodução ideológica.', 'C',
  'As **agências de comunicação social** e de **reprodução ideológica** também constroem a realidade do crime.',
  kw=['agências', 'comunicação social'])
I(P, 1, 'Seletividade regional',
  'A crítica criminológica latino-americana aponta que as agências de controle selecionam preferencialmente pessoas vulneráveis, que correspondem ao estereótipo do criminoso.', 'C',
  '**Seletividade** e **estereótipo**: a criminalização recai sobre os **vulneráveis**.',
  kw=['seletividade', 'estereótipo'])
I(P, 1, 'Realismo marginal',
  'Para o realismo marginal de Zaffaroni, o sistema penal latino-americano é legítimo, pois opera conforme o discurso jurídico oficial.', 'E',
  'O **realismo marginal** sustenta a **deslegitimação** do sistema penal: a operação real é seletiva e violenta, distante do discurso oficial.',
  peg='Inverter a tese da deslegitimação.',
  kw=['realismo marginal', 'deslegitimação'])
I(P, 1, 'Importação de teorias',
  'Rosa del Olmo defendeu a importação, pela América Latina, das teorias criminológicas dos países centrais, especialmente do positivismo, como caminho para a modernização da região.', 'E',
  '**Rosa del Olmo** (A América Latina e sua Criminologia) **criticou** a **importação** acrítica de modelos centrais, sobretudo o positivismo.',
  peg='Inverter a posição da autora.',
  kw=['Rosa del Olmo', 'importação'])
I(P, 1, 'Positivismo no Brasil',
  'No Brasil, Nina Rodrigues difundiu ideias do positivismo biológico, com viés racial, hoje rejeitado pela Criminologia.', 'C',
  '**Nina Rodrigues** representa a recepção do **positivismo lombrosiano**, de marcado **viés racial**.',
  kw=['Nina Rodrigues', 'positivismo'])
I(P, 1, 'Estratégia regional',
  'A Criminologia crítica latino-americana defende o recrudescimento da atuação policial como principal estratégia de redução da violência.', 'E',
  'A crítica regional propõe **contenção do poder punitivo**, **redução de danos** e respeito a direitos.',
  peg='Atribuir à crítica uma bandeira de lei e ordem.',
  kw=['contenção do poder punitivo', 'redução de danos'])

# --- CRI-11 · Rodada 2
I(P, 2, 'Segurança nacional',
  'A doutrina da segurança nacional, nos regimes autoritários latino-americanos, influenciou as agências de controle, com militarização da segurança pública e a figura do inimigo interno.', 'C',
  'A **segurança nacional** deixou marcas: **militarização** e lógica do **inimigo interno**.',
  kw=['segurança nacional', 'militarização'])
I(P, 2, 'Sistema penal subterrâneo',
  'Zaffaroni chama de sistema penal subterrâneo as práticas punitivas ilegais das agências, como execuções sem processo, torturas e desaparecimentos.', 'C',
  'O **sistema penal subterrâneo** é a face **ilegal** do poder punitivo.',
  kw=['sistema penal subterrâneo', 'Zaffaroni'])
I(P, 2, 'Alvos preferenciais',
  'Na América Latina, a criminalização secundária atinge preferencialmente os autores de crimes de colarinho branco, por sua visibilidade social.', 'E',
  'Ela atinge preferencialmente os **vulneráveis**; a criminalidade das elites forma a **cifra dourada**.',
  peg='Inverter os alvos da seletividade.',
  kw=['vulneráveis', 'cifra dourada'])
I(P, 2, 'Criminologia da libertação',
  'Lola Aniyar de Castro propôs uma Criminologia da libertação, comprometida com a transformação das estruturas de dominação na América Latina.', 'C',
  '**Criminologia da libertação**: engajada na **transformação social** da região.',
  kw=['Criminologia da libertação', 'Lola Aniyar de Castro'])
I(P, 2, 'Criminologia midiática',
  'Zaffaroni denomina criminologia midiática a construção, pelos meios de comunicação, de uma realidade do crime que divide a sociedade entre "nós" e "eles", alimentando demandas punitivas.', 'C',
  'A **criminologia midiática** fabrica o medo e o **inimigo**, e pressiona por mais punição.',
  kw=['criminologia midiática', 'meios de comunicação'])
I(P, 2, 'Adaptação regional',
  'Para a Criminologia crítica latino-americana, as teorias produzidas nos países centrais devem ser aplicadas sem adaptações à realidade regional.', 'E',
  'A crítica regional exige **adequação** à realidade **periférica**.',
  peg='Negar a necessidade de adaptação.',
  kw=['realidade periférica', 'adaptação'])

# ======================= CRI-12 · Criminologia e proposta de Política Criminal =======================
P = 'DBA26-CRI-12'
I(P, 1, 'Conceito de Política Criminal',
  'Política Criminal é o conjunto de princípios e estratégias com que o Estado organiza a resposta ao fenômeno criminal, servindo de ponte entre a Criminologia e o Direito Penal.', 'C',
  '**Política Criminal**: **estratégias** de resposta ao crime; **ponte** entre o ser e o dever ser.',
  kw=['Política Criminal', 'estratégias'])
I(P, 1, 'Grandes movimentos',
  'Entre os movimentos de política criminal destacam-se o de lei e ordem, de recrudescimento punitivo; o do Direito Penal mínimo, de matriz garantista; e o abolicionismo penal.', 'C',
  'Três polos: **lei e ordem** (máximo), **Direito Penal mínimo** (garantismo) e **abolicionismo**.',
  kw=['lei e ordem', 'Direito Penal mínimo'])
I(P, 1, 'Abolicionismo',
  'O abolicionismo penal propõe o recrudescimento das penas privativas de liberdade.', 'E',
  'O **abolicionismo** (Hulsman, Christie, Mathiesen) propõe **abolir** o sistema penal e resolver conflitos por outras vias.',
  peg='Inverter a proposta abolicionista.',
  kw=['abolicionismo', 'Hulsman'])
I(P, 1, 'Garantismo',
  'O garantismo de Jakobs propõe um Direito Penal mínimo, limitado por garantias penais e processuais que condicionam a punição.', 'E',
  'O **garantismo** é de **Ferrajoli** (**Direito Penal mínimo**, axiomas de legalidade, lesividade, culpabilidade, contraditório...). Jakobs é o autor do Direito Penal do inimigo.',
  peg='Trocar o autor.',
  kw=['garantismo', 'Ferrajoli'])
I(P, 1, 'Direito Penal do inimigo',
  'O Direito Penal do inimigo, formulado por Jakobs, caracteriza-se pela antecipação da punição, por penas desproporcionais e pela relativização de garantias processuais em relação a quem é tratado como inimigo.', 'C',
  '**Jakobs**: **antecipação** da tutela, **penas altas**, **menos garantias** para o "inimigo".',
  kw=['Direito Penal do inimigo', 'Jakobs'])
I(P, 1, 'Velocidades do Direito Penal',
  'Para Silva Sánchez, a segunda velocidade do Direito Penal combina pena privativa de liberdade com flexibilização de garantias.', 'E',
  'Na formulação de **Silva Sánchez**: **1ª** — prisão com garantias plenas; **2ª** — penas **alternativas** com garantias flexibilizadas; **3ª** — **prisão** com garantias flexibilizadas (Direito Penal do inimigo).',
  peg='Trocar a segunda pela terceira velocidade.',
  kw=['segunda velocidade', 'Silva Sánchez'])
I(P, 1, 'Lei e ordem e tolerância zero',
  'O movimento de lei e ordem associa-se a políticas como a tolerância zero, aplicada em Nova York nos anos 1990 e inspirada na teoria das janelas quebradas.', 'C',
  '**Lei e ordem** + **tolerância zero** + **janelas quebradas** formam o pacote mais cobrado.',
  kw=['lei e ordem', 'tolerância zero'])
I(P, 1, 'Intervenção mínima',
  'O princípio da intervenção mínima faz do Direito Penal a ultima ratio, de caráter subsidiário e fragmentário.', 'C',
  '**Intervenção mínima**: **subsidiariedade** + **fragmentariedade**.',
  kw=['intervenção mínima', 'ultima ratio'])

# --- CRI-12 · Rodada 2
I(P, 2, 'Terceira velocidade',
  'Na classificação de Silva Sánchez, a terceira velocidade corresponde ao Direito Penal do inimigo, que combina pena de prisão com flexibilização de garantias.', 'C',
  '**3ª velocidade** = **prisão** + **garantias flexibilizadas** = Direito Penal do inimigo.',
  kw=['terceira velocidade', 'Direito Penal do inimigo'])
I(P, 2, 'Quarta velocidade',
  'Parte da doutrina fala em quarta velocidade, ou neopunitivismo, ligada à persecução, no plano internacional, de quem exerceu poder estatal e violou gravemente direitos humanos, com flexibilização de garantias.', 'C',
  'A **quarta velocidade** não é de Silva Sánchez: é acréscimo **doutrinário** posterior, sem consenso — mas aparece em provas com esse conteúdo.',
  kw=['quarta velocidade', 'neopunitivismo'])
I(P, 2, 'Status do inimigo',
  'O Direito Penal do inimigo sustenta que o inimigo conserva integralmente o status de cidadão e todas as garantias processuais.', 'E',
  'Para **Jakobs**, o inimigo é tratado como **não-pessoa**, com **garantias reduzidas** — daí as críticas de incompatibilidade com o Estado Democrático de Direito.',
  peg='Inverter o núcleo da teoria.',
  kw=['não-pessoa', 'garantias reduzidas'])
I(P, 2, 'Situações-problema',
  'Hulsman propôs substituir a noção de crime pela de situação-problema, a ser resolvida por mecanismos civis, administrativos ou comunitários.', 'C',
  '**Hulsman**: **situações-problema** em lugar de crime; solução fora do sistema penal.',
  kw=['situações-problema', 'Hulsman'])
I(P, 2, 'Política criminal atuarial',
  'A política criminal atuarial, de gestão de riscos, concentra-se na reabilitação individual do condenado.', 'E',
  'A lógica **atuarial** gerencia **grupos de risco** e privilegia a **incapacitação**, não a reabilitação individual.',
  peg='Trocar gestão de risco por reabilitação.',
  kw=['atuarial', 'gestão de riscos'])
I(P, 2, 'Garantismo e culpabilidade',
  'Para Ferrajoli, o garantismo admite pena sem culpabilidade quando necessária à prevenção.', 'E',
  'No garantismo, a **culpabilidade** é **axioma** (nulla poena sine culpa): não há pena sem culpa.',
  peg='Admitir exceção ao axioma da culpabilidade.',
  kw=['culpabilidade', 'garantismo'])

# ======================= CRI-13 · Criminologia e Ciências Criminais =======================
P = 'DBA26-CRI-13'
I(P, 1, 'Modelo tripartido',
  'No modelo integrado das ciências criminais, Criminologia, Política Criminal e Direito Penal são saberes autônomos e complementares.', 'C',
  'O **modelo tripartido** une **ser** (Criminologia), **estratégia** (Política Criminal) e **norma** (Direito Penal).',
  kw=['modelo integrado', 'ciências criminais'])
I(P, 1, 'Criminalística',
  'Criminalística e Criminologia são expressões sinônimas.', 'E',
  'A **Criminalística** é disciplina **técnica** de exame dos **vestígios materiais** do crime (prova pericial); a Criminologia é ciência empírica do fenômeno criminal.',
  peg='Confundir as duas disciplinas.',
  kw=['Criminalística', 'vestígios materiais'])
I(P, 1, 'Penologia',
  'A Penologia estuda as penas, sua finalidade e sua execução.', 'C',
  '**Penologia**: teoria e prática das **penas**.',
  kw=['Penologia', 'penas'])
I(P, 1, 'Crítica × dogmática',
  'A Criminologia pode questionar a legitimidade e a eficácia das normas penais, ao passo que a dogmática penal parte da norma vigente para interpretá-la e sistematizá-la.', 'C',
  'A **dogmática** trabalha **dentro** da norma; a Criminologia a observa **de fora**.',
  kw=['dogmática penal', 'eficácia'])
I(P, 1, 'Natureza da Política Criminal',
  'A Política Criminal é ciência empírica, de método idêntico ao da Criminologia.', 'E',
  'A **Política Criminal** é disciplina **valorativa** e estratégica: escolhe fins e meios a partir do dado criminológico.',
  peg='Igualar Política Criminal e Criminologia.',
  kw=['valorativa', 'Política Criminal'])
I(P, 1, 'Vitimologia: ramo ou ciência',
  'Há divergência sobre a natureza da Vitimologia: para a maioria, é ramo da Criminologia; para outros, como Mendelsohn, é ciência autônoma.', 'C',
  'Divergência clássica: **ramo da Criminologia** (majoritária) × **ciência autônoma** (Mendelsohn).',
  kw=['Vitimologia', 'ciência autônoma'])

# --- CRI-13 · Rodada 2
I(P, 2, 'Ciência total',
  'Von Liszt concebeu a ciência total do Direito Penal, integrando dogmática, Criminologia e Política Criminal, e afirmou que o Direito Penal é a barreira intransponível da Política Criminal.', 'C',
  '**Von Liszt**: **ciência total**; o Direito Penal é a **barreira intransponível** da Política Criminal.',
  kw=['ciência total', 'barreira intransponível'])
I(P, 2, 'Barreira invertida',
  'Para von Liszt, a Política Criminal é a barreira intransponível do Direito Penal.', 'E',
  'Está invertido: o **Direito Penal** é a barreira intransponível da **Política Criminal**.',
  peg='Inverter a frase célebre.',
  kw=['barreira intransponível', 'von Liszt'])
I(P, 2, 'Medicina Legal',
  'A Medicina Legal aplica conhecimentos médicos e biológicos aos fins da Justiça e integra o conjunto das ciências criminais auxiliares.', 'C',
  'A **Medicina Legal** é ciência **auxiliar**, voltada à prova.',
  kw=['Medicina Legal', 'ciências auxiliares'])
I(P, 2, 'Psicologia do testemunho',
  'A psicologia do testemunho, ao estudar as falsas memórias, contribui para reduzir erros judiciários decorrentes de reconhecimentos falhos.', 'C',
  '**Falsas memórias** e **reconhecimento**: diálogo da Psicologia com o processo penal.',
  kw=['falsas memórias', 'psicologia do testemunho'])
I(P, 2, 'Comunicação entre os saberes',
  'Criminologia e Direito Penal são ciências independentes e incomunicáveis.', 'E',
  'São **autônomas**, mas **complementares**: o dado criminológico informa a Política Criminal e o Direito Penal.',
  peg='Trocar "autônomas" por "incomunicáveis".',
  kw=['complementares', 'autônomas'])

# ======================= CRI-14 · Criminologia e Sistema de Justiça Criminal =======================
P = 'DBA26-CRI-14'
I(P, 1, 'Efeito funil',
  'No sistema de justiça criminal, verifica-se o efeito funil: dos crimes ocorridos, só parte é registrada, uma parcela menor é investigada e processada, e menos ainda resulta em condenação.', 'C',
  'O **efeito funil** mostra a perda de casos em cada etapa do sistema.',
  kw=['efeito funil', 'sistema de justiça criminal'])
I(P, 1, 'Cifra negra',
  'A cifra negra corresponde à diferença entre a criminalidade real e a registrada pelas instâncias formais de controle.', 'C',
  '**Cifra negra** = criminalidade **oculta**, que não chega ao conhecimento oficial.',
  kw=['cifra negra', 'criminalidade real'])
I(P, 1, 'Cifra negra por espécie',
  'A cifra negra tende a ser maior nos homicídios do que nos crimes patrimoniais de pequeno valor.', 'E',
  'É o contrário: o **homicídio** deixa vestígio evidente e tem **cifra negra baixa**; **furtos de pequeno valor** são pouco comunicados.',
  peg='Inverter a relação entre gravidade e registro.',
  kw=['cifra negra', 'homicídio'])
I(P, 1, 'Prisionização',
  'A prisionização, descrita por Clemmer, é a assimilação dos valores e costumes da cultura carcerária pelo preso, o que dificulta sua reinserção.', 'C',
  '**Prisionização**: o preso absorve a **cultura carcerária**.',
  kw=['prisionização', 'Clemmer'])
I(P, 1, 'Estereótipos',
  'A seletividade do sistema de justiça criminal é orientada, em boa medida, por estereótipos que recaem sobre grupos vulneráveis.', 'C',
  'A **seletividade** é guiada por **estereótipos**.',
  kw=['seletividade', 'estereótipos'])
I(P, 1, 'Reparação na sentença',
  'O juiz não pode fixar, na sentença condenatória, valor mínimo para reparação dos danos causados pela infração, matéria reservada ao juízo cível.', 'E',
  'O art. 387, IV, do CPP manda o juiz **fixar valor mínimo** para reparação — atenção à **vítima** no processo penal.',
  lei=[(CPP + '387', 'IV - fixará valor mínimo para reparação dos danos causados pela infração', 'considerando os prejuízos sofridos pelo ofendido;', 'CPP, art. 387, IV')],
  peg='Negar a fixação do valor mínimo.',
  kw=['valor mínimo', 'reparação dos danos'])
I(P, 1, 'Estatísticas oficiais',
  'As estatísticas criminais oficiais refletem com fidelidade a criminalidade real, razão pela qual dispensam complementação por pesquisas de vitimização.', 'E',
  'As **estatísticas oficiais** medem a criminalidade **registrada** — e também a atividade das agências. As **pesquisas de vitimização** revelam a **cifra negra**.',
  peg='Igualar registrado e real.',
  kw=['estatísticas oficiais', 'pesquisas de vitimização'])

# --- CRI-14 · Rodada 2
I(P, 2, 'Primeiro filtro',
  'A polícia realiza a primeira e mais ampla seleção do sistema de justiça criminal, ao decidir o que registra e investiga.', 'C',
  'A polícia é o **primeiro filtro** da **criminalização secundária**.',
  kw=['primeiro filtro', 'criminalização secundária'])
I(P, 2, 'Sentido da prisionização',
  'A prisionização é o processo pelo qual o preso se readapta aos valores da sociedade livre.', 'E',
  'É o contrário: o preso **assimila a cultura carcerária**, afastando-se dos valores da sociedade livre.',
  peg='Inverter o sentido do conceito.',
  kw=['cultura carcerária', 'prisionização'])
I(P, 2, 'Compartimentalização',
  'A crítica criminológica aponta que as agências do sistema de justiça criminal atuam de forma compartimentalizada, com objetivos por vezes contraditórios.', 'C',
  'O "sistema" é pouco **integrado**: cada agência tem lógica e metas próprias.',
  kw=['compartimentalizada', 'agências'])
I(P, 2, 'Intimidade do ofendido',
  'O juiz tomará as providências necessárias à preservação da intimidade, da vida privada, da honra e da imagem do ofendido, podendo determinar segredo de justiça quanto aos dados a seu respeito.', 'C',
  'O art. 201, § 6º, do CPP combate a **vitimização secundária** pela **exposição**.',
  lei=[(CPP + '201', 'O juiz tomará as providências necessárias à preservação da intimidade', 'evitar sua exposição aos meios de comunicação.', 'CPP, art. 201, § 6º')],
  kw=['intimidade', 'segredo de justiça'])
I(P, 2, 'Espaço reservado à vítima',
  'O Código de Processo Penal não prevê espaço separado para o ofendido antes ou durante a audiência, cabendo-lhe aguardar com as demais pessoas.', 'E',
  'Pelo art. 201, § 4º, será **reservado espaço separado** para o ofendido antes e durante a audiência.',
  lei=[(CPP + '201', 'Antes do início da audiência e durante a sua realização', 'será reservado espaço separado para o ofendido.', 'CPP, art. 201, § 4º')],
  peg='Negar a garantia do espaço separado.',
  kw=['espaço separado', 'ofendido'])

# ======================= CRI-15 · O papel da Polícia Judiciária =======================
P = 'DBA26-CRI-15'
I(P, 1, 'Polícia judiciária na Constituição',
  'Às polícias civis, dirigidas por delegados de polícia de carreira, incumbem, ressalvada a competência da União, as funções de polícia judiciária e a apuração de infrações penais, exceto as militares.', 'C',
  'Literalidade do art. 144, § 4º: **funções de polícia judiciária** e apuração de infrações penais, salvo as militares e a competência da União.',
  lei=[(CF + '144', '§ 4º Às polícias civis, dirigidas por delegados de polícia de carreira', 'apuração de infrações penais, exceto as militares.', 'CF, art. 144, § 4º')],
  kw=['polícia judiciária', 'delegados de polícia de carreira'])
I(P, 1, 'Natureza das funções',
  'As funções de polícia judiciária e de apuração de infrações penais exercidas pelo delegado de polícia são de natureza administrativa, essenciais e delegáveis a particulares.', 'E',
  'Pelo art. 2º da Lei 12.830/2013, essas funções são de **natureza jurídica**, **essenciais** e **exclusivas de Estado** — logo, indelegáveis.',
  peg='Trocar a natureza e a exclusividade das funções.',
  lei=[(DEL + '2', 'As funções de polícia judiciária e a apuração de infrações penais', 'essenciais e exclusivas de Estado.', 'Lei 12.830/2013, art. 2º, caput')],
  kw=['natureza jurídica', 'exclusivas de Estado'])
I(P, 1, 'Polícia ostensiva',
  'Às polícias civis cabem a polícia ostensiva e a preservação da ordem pública.', 'E',
  '**Polícia ostensiva** e **preservação da ordem pública** cabem às **polícias militares**.',
  lei=[(CF + '144', '§ 5º Às polícias militares cabem a polícia ostensiva e a preservação da ordem pública', None, 'CF, art. 144, § 5º')],
  peg='Trocar polícia civil por militar.',
  kw=['polícias militares', 'polícia ostensiva'])
I(P, 1, 'Indiciamento',
  'O indiciamento, privativo do delegado de polícia, dar-se-á por ato fundamentado, mediante análise técnico-jurídica do fato, indicando autoria, materialidade e circunstâncias.', 'C',
  'O **indiciamento** é **privativo** e **fundamentado** (art. 2º, § 6º).',
  lei=[(DEL + '2', 'O indiciamento, privativo do delegado de polícia', 'deverá indicar a autoria, materialidade e suas circunstâncias.', 'Lei 12.830/2013, art. 2º, § 6º')],
  kw=['indiciamento', 'ato fundamentado'])
I(P, 1, 'Arquivamento',
  'Concluindo pela atipicidade do fato, o delegado de polícia pode mandar arquivar os autos do inquérito.', 'E',
  'A autoridade policial **não pode** mandar arquivar autos de inquérito.',
  lei=[(CPP + '17', 'A autoridade policial não poderá mandar arquivar autos de inquérito.', None, 'CPP, art. 17')],
  peg='Dar ao delegado poder de arquivamento.',
  kw=['arquivar', 'autoridade policial'])
I(P, 1, 'Papel criminológico',
  'Sob o enfoque criminológico, a polícia judiciária é instância formal de controle que, além de investigar, produz dados sobre a criminalidade úteis ao planejamento da prevenção e da política de segurança.', 'C',
  'A polícia judiciária **seleciona** e **informa**: seus registros alimentam **diagnóstico** e **prevenção**.',
  kw=['instância formal de controle', 'prevenção'])
I(P, 1, 'Vida pregressa',
  'Ao investigar, a autoridade policial deve averiguar a vida pregressa do indiciado, sob o ponto de vista individual, familiar e social, sua condição econômica e sua atitude antes, durante e depois do crime.', 'C',
  'O art. 6º, IX, do CPP traz ao inquérito um olhar **criminológico** sobre o **autor**.',
  lei=[(CPP + '6', 'IX - averiguar a vida pregressa do indiciado', 'durante ele', 'CPP, art. 6º, IX')],
  kw=['vida pregressa', 'indiciado'])

# --- CRI-15 · Rodada 2
I(P, 2, 'Avocação e redistribuição',
  'O inquérito policial em curso somente poderá ser avocado ou redistribuído por superior hierárquico, mediante despacho fundamentado, por motivo de interesse público ou por inobservância de procedimentos que prejudique a eficácia da investigação.', 'C',
  'Garantia da **investigação** (art. 2º, § 4º, da Lei 12.830/2013).',
  lei=[(DEL + '2', 'O inquérito policial ou outro procedimento previsto em lei em curso somente poderá ser avocado', 'prejudique a eficácia da investigação.', 'Lei 12.830/2013, art. 2º, § 4º')],
  kw=['avocado', 'despacho fundamentado'])
I(P, 2, 'Avocação livre',
  'O inquérito em curso pode ser avocado livremente pelo superior hierárquico, independentemente de fundamentação.', 'E',
  'A avocação exige **despacho fundamentado** e motivo legal.',
  lei=[(DEL + '2', 'O inquérito policial ou outro procedimento previsto em lei em curso somente poderá ser avocado', 'mediante despacho fundamentado', 'Lei 12.830/2013, art. 2º, § 4º')],
  peg='Dispensar a fundamentação.',
  kw=['despacho fundamentado', 'avocação'])
I(P, 2, 'Atendimento especializado',
  'Entre as diretrizes da política de enfrentamento à violência doméstica está a implementação de atendimento policial especializado para as mulheres, em particular nas Delegacias de Atendimento à Mulher.', 'C',
  'O **atendimento especializado** previne a **vitimização secundária**.',
  lei=[('L11340:8', 'IV - a implementação de atendimento policial especializado para as mulheres', 'Delegacias de Atendimento à Mulher;', 'Lei 11.340/2006, art. 8º, IV')],
  kw=['atendimento policial especializado', 'vitimização secundária'])
I(P, 2, 'Mínima intervenção',
  'No atendimento à criança e ao adolescente vítima de violência, a Lei 13.431/2017 adota como diretriz a mínima intervenção dos profissionais envolvidos.', 'C',
  'A **mínima intervenção** evita a **revitimização** também na fase policial.',
  lei=[('L13431:14', 'VII - mínima intervenção dos profissionais envolvidos', None, 'Lei 13.431/2017, art. 14, § 1º, VII')],
  kw=['mínima intervenção', 'revitimização'])
I(P, 2, 'Requisição pelo delegado',
  'Durante a investigação, a requisição de perícia, informações, documentos e dados pelo delegado de polícia depende de prévia autorização judicial.', 'E',
  'Pelo art. 2º, § 2º, da Lei 12.830/2013, **cabe ao delegado** requisitar perícia, informações, documentos e dados — sem intermediação judicial, ressalvadas as matérias sob reserva de jurisdição.',
  lei=[(DEL + '2', 'Durante a investigação criminal, cabe ao delegado de polícia a requisição de perícia', 'que interessem à apuração dos fatos.', 'Lei 12.830/2013, art. 2º, § 2º')],
  exc=['Dados sob reserva de jurisdição (ex.: interceptação telefônica, quebra de sigilo bancário) exigem ordem judicial.'],
  peg='Condicionar a requisição a autorização judicial.',
  kw=['requisição', 'delegado de polícia'])
I(P, 2, 'Oitiva do ofendido',
  'Logo que tiver conhecimento da infração, a autoridade policial deverá ouvir o ofendido, o que, sob o enfoque vitimológico, exige cuidado para não gerar vitimização secundária.', 'C',
  '**Ouvir o ofendido** é dever (art. 6º, IV), a ser cumprido sem **revitimizar**.',
  lei=[(CPP + '6', 'IV - ouvir o ofendido;', None, 'CPP, art. 6º, IV')],
  kw=['ouvir o ofendido', 'vitimização secundária'])

# ======================= CRI-16 · Criminologia no Estado Democrático de Direito =======================
P = 'DBA26-CRI-16'
I(P, 1, 'Dignidade como limite',
  'A dignidade da pessoa humana, fundamento da República, é limite para a política criminal e para a atuação das agências de controle no Estado Democrático de Direito.', 'C',
  'A **dignidade da pessoa humana** (art. 1º, III) limita todo o poder punitivo.',
  lei=[(CF + '1', 'constitui-se em Estado Democrático de Direito e tem como fundamentos', 'III - a dignidade da pessoa humana;', 'CF, art. 1º, caput e III')],
  kw=['dignidade da pessoa humana', 'Estado Democrático de Direito'])
I(P, 1, 'Função legitimadora',
  'No Estado Democrático de Direito, a Criminologia deve servir à legitimação de qualquer política repressiva eficaz, independentemente dos direitos fundamentais.', 'E',
  'A Criminologia no Estado Democrático de Direito **avalia** e **limita**; a eficácia não se sobrepõe aos **direitos fundamentais**.',
  peg='Pôr a eficácia acima dos direitos.',
  kw=['direitos fundamentais', 'limita'])
I(P, 1, 'Integridade do preso',
  'É assegurado aos presos o respeito à integridade física e moral.', 'C',
  'Art. 5º, XLIX: **integridade física e moral** do preso — princípio da **humanidade**.',
  lei=[(CF + '5', 'XLIX - é assegurado aos presos o respeito à integridade física e moral;', None, 'CF, art. 5º, XLIX')],
  kw=['integridade física e moral', 'humanidade'])
I(P, 1, 'Penas cruéis',
  'A Constituição admite penas cruéis quando necessárias à prevenção geral.', 'E',
  'A Constituição **proíbe** penas **cruéis**, sem exceção.',
  lei=[(CF + '5', 'XLVII - não haverá penas:', 'e) cruéis;', 'CF, art. 5º, XLVII, e')],
  peg='Criar exceção à vedação de penas cruéis.',
  kw=['penas cruéis', 'humanidade'])
I(P, 1, 'Pessoalidade',
  'Nenhuma pena passará da pessoa do condenado, podendo a obrigação de reparar o dano e a decretação do perdimento de bens ser estendidas aos sucessores, até o limite do patrimônio transferido.', 'C',
  '**Pessoalidade da pena** (art. 5º, XLV), com a ressalva da **reparação** e do **perdimento**.',
  lei=[(CF + '5', 'XLV - nenhuma pena passará da pessoa do condenado', 'até o limite do valor do patrimônio transferido;', 'CF, art. 5º, XLV')],
  kw=['pessoalidade', 'reparar o dano'])
I(P, 1, 'Modelo democrático',
  'A Criminologia no Estado Democrático de Direito orienta-se por um modelo de prevenção e de resposta ao crime compatível com as garantias, que valoriza a vítima e a reparação sem sacrificar os direitos do investigado.', 'C',
  'Equilíbrio: **prevenção**, **vítima** e **garantias**.',
  kw=['garantias', 'vítima'])
I(P, 1, 'Legalidade',
  'No Estado Democrático de Direito, admite-se a criação de crimes por medida provisória, dada a urgência da política criminal.', 'E',
  'Vale a **legalidade estrita** (art. 5º, XXXIX): crime só por **lei**; a Constituição veda medida provisória sobre direito penal (art. 62, § 1º, I, b).',
  lei=[(CF + '5', 'XXXIX - não há crime sem lei anterior que o defina', 'nem pena sem prévia cominação legal;', 'CF, art. 5º, XXXIX')],
  peg='Admitir fonte normativa inidônea para criar crime.',
  kw=['legalidade', 'medida provisória'])

# --- CRI-16 · Rodada 2
I(P, 2, 'Objetivos da República',
  'Construir uma sociedade livre, justa e solidária e erradicar a pobreza e a marginalização são objetivos fundamentais da República, ligados à prevenção primária.', 'C',
  'O art. 3º da Constituição é o programa da **prevenção primária**.',
  lei=[(CF + '3', 'I - construir uma sociedade livre, justa e solidária;', None, 'CF, art. 3º, I'),
       (CF + '3', 'III - erradicar a pobreza e a marginalização', None, 'CF, art. 3º, III')],
  kw=['objetivos fundamentais', 'prevenção primária'])
I(P, 2, 'Direito Penal simbólico',
  'O chamado Direito Penal simbólico caracteriza-se por normas editadas para produzir sensação de segurança e responder a demandas emocionais, sem eficácia real na proteção de bens jurídicos.', 'C',
  'O **Direito Penal simbólico** busca **efeito político**, não proteção efetiva.',
  kw=['Direito Penal simbólico', 'sensação de segurança'])
I(P, 2, 'Populismo penal',
  'O populismo penal, que responde com recrudescimento punitivo à opinião pública amplificada pela mídia, é a política criminal recomendada pela Criminologia no Estado Democrático de Direito.', 'E',
  'O **populismo penal** é **criticado** pela Criminologia: ignora evidências e amplia a seletividade.',
  peg='Transformar o objeto da crítica em recomendação.',
  kw=['populismo penal', 'evidências'])
I(P, 2, 'Estabelecimentos distintos',
  'A pena será cumprida em estabelecimentos distintos, de acordo com a natureza do delito, a idade e a condição econômica do apenado.', 'E',
  'Os critérios do art. 5º, XLVIII, são **natureza do delito, idade e sexo** — não condição econômica.',
  lei=[(CF + '5', 'XLVIII - a pena será cumprida em estabelecimentos distintos', 'a idade e o sexo do apenado;', 'CF, art. 5º, XLVIII')],
  peg='Trocar "sexo" por "condição econômica".',
  kw=['estabelecimentos distintos', 'sexo do apenado'])
I(P, 2, 'Direitos não atingidos',
  'Ao condenado e ao internado são assegurados todos os direitos não atingidos pela sentença ou pela lei, sem distinção de natureza racial, social, religiosa ou política.', 'C',
  'O art. 3º da LEP traduz, na execução, o **Estado Democrático de Direito**.',
  lei=[('L7210:3', 'Ao condenado e ao internado serão assegurados todos os direitos não atingidos pela sentença ou pela lei.', None, 'LEP, art. 3º'),
       ('L7210:3', 'Não haverá qualquer distinção de natureza racial, social, religiosa ou política.', None, 'LEP, art. 3º, par. ún.')],
  kw=['direitos não atingidos', 'execução'])
I(P, 2, 'Proteção contra sensacionalismo',
  'Constitui direito do preso a proteção contra qualquer forma de sensacionalismo.', 'C',
  'Art. 41, VIII, da LEP: contra a exposição midiática que **estigmatiza**.',
  lei=[('L7210:41', 'VIII - proteção contra qualquer forma de sensacionalismo;', None, 'LEP, art. 41, VIII')],
  kw=['sensacionalismo', 'direito do preso'])
