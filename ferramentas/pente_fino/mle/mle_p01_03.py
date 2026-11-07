# Pente Fino de Medicina Legal — pontos MLE-1, MLE-1.1, MLE-2, MLE-2.1 e MLE-3 (07/11/2026).
# Doutrina em redação própria; lei recortada de assets/lei_seca_oficial.json pelo construir.py.
from base import I
from mle_juris import J

CPP = 'CPP:'
CP = 'CP:'

# ======================= MLE-1 · Conceito, importância e divisões =======================
P = 'DBA26-MLE-1'
I(P, 1, 'Conceito de Medicina Legal',
  'Medicina Legal é o conjunto de conhecimentos médicos e de outras ciências biológicas e exatas postos a serviço do Direito, tanto na elaboração quanto na interpretação e na execução das normas jurídicas.', 'C',
  'É o conceito mais cobrado: a **Medicina Legal** é ciência de aplicação, que reúne saberes médicos e paramédicos para responder a perguntas jurídicas — e não só no processo, mas também na feitura e na aplicação da lei.',
  regra='Ciência (método e sistematização) e arte (exposição lógica do achado ao jurista).',
  kw=['Medicina Legal', 'ciência aplicada ao Direito'])
I(P, 1, 'Importância e alcance',
  'Por servir à apuração de crimes, a Medicina Legal tem interesse exclusivo para o Direito Penal e o Processual Penal.', 'E',
  'A disciplina serve a **todos os ramos do Direito**: no cível (interdição, anulação de casamento, investigação de paternidade), no trabalhista (acidente e doença do trabalho), no previdenciário, no administrativo e no penal.',
  peg='Trocar "também" por "exclusivamente" — restringir a um ramo o que serve a todos.',
  kw=['todos os ramos do Direito', 'perícia cível'])
I(P, 1, 'Divisão didática: geral e especial',
  'Na divisão didática, a Medicina Legal geral trata da deontologia e da diceologia médicas, e a Medicina Legal especial reúne capítulos como antropologia, traumatologia, tanatologia, sexologia e psiquiatria forenses.', 'C',
  'Divisão clássica: a parte **geral** cuida do exercício da medicina (deveres e direitos do médico); a parte **especial** reúne os capítulos aplicados (antropologia, traumatologia, asfixiologia, tanatologia, toxicologia, sexologia, psicologia e psiquiatria forenses, criminalística, infortunística, genética forense).',
  kw=['Medicina Legal geral', 'Medicina Legal especial'])
I(P, 1, 'Tanatologia × traumatologia',
  'Cabe à tanatologia forense o estudo das lesões corporais causadas pelas diferentes energias vulnerantes.', 'E',
  'Lesões e energias vulnerantes são objeto da **traumatologia** forense. A **tanatologia** estuda a morte e o cadáver: diagnóstico da morte, fenômenos cadavéricos, tempo de morte, necropsia, exumação.',
  peg='Trocar o nome do capítulo: tanatologia (morte) por traumatologia (lesões).',
  kw=['tanatologia', 'traumatologia'])
I(P, 1, 'Antropologia forense',
  'A antropologia forense é o capítulo que se ocupa da identidade e da identificação, médico-legal e judiciária.', 'C',
  'A **antropologia forense** cuida de quem é a pessoa (viva, cadáver ou ossada): espécie, sexo, idade, estatura, sinais individuais, datiloscopia, odontologia e DNA.',
  kw=['antropologia forense', 'identificação'])
I(P, 1, 'Deontologia × diceologia',
  'Deontologia médica é a parte da Medicina Legal geral que estuda os direitos do médico no exercício da profissão.', 'E',
  'Os **direitos** do médico são objeto da **diceologia**; a **deontologia** estuda os **deveres** (o "dever ser" profissional).',
  peg='Inverter deveres (deontologia) e direitos (diceologia).',
  kw=['deontologia', 'diceologia'])
I(P, 1, 'Contribuição para a elaboração das leis',
  'A Medicina Legal também contribui para a elaboração das leis, como se vê na Lei de Transplantes, que remete a critérios técnicos fixados pelo Conselho Federal de Medicina para a constatação da morte encefálica.', 'C',
  'A lei usa conceitos médicos e os deixa para a técnica: a **morte encefálica** é constatada por critérios clínicos e tecnológicos definidos em resolução do CFM (Lei 9.434/1997, art. 3º).',
  lei=[('L9434:3', 'A retirada post mortem de tecidos', 'definidos por resolução do Conselho Federal de Medicina.', 'Lei 9.434/1997, art. 3º')],
  kw=['morte encefálica', 'elaboração das leis'])
I(P, 1, 'Sexologia forense',
  'A sexologia forense limita-se ao estudo dos crimes contra a dignidade sexual.', 'E',
  'A **sexologia forense** é mais ampla: abrange crimes sexuais, mas também questões de casamento (erro essencial, impotência), gravidez, parto, puerpério, aborto, infanticídio e transtornos da sexualidade.',
  peg='Reduzir a um tema ("limita-se") o capítulo que cobre vários.',
  kw=['sexologia forense', 'obstetrícia forense'])

# --- MLE-1 · Rodada 2
I(P, 2, 'Energias vulnerantes: asfixias',
  'Na classificação das energias vulnerantes, as asfixias mecânicas são enquadradas como energia de ordem físico-química.', 'C',
  'As **asfixias** impedem a troca gasosa por meio mecânico (constrição, obstrução, meio irrespirável) com efeito químico no sangue — por isso a doutrina as classifica como energia **físico-química**.',
  regra='Ordens das energias: mecânica, física, química, físico-química, bioquímica, biodinâmica e mista.',
  kw=['físico-química', 'asfixias'])
I(P, 2, 'Energias de ordem física',
  'Calor, frio, eletricidade, pressão atmosférica e radiações são energias de ordem química.', 'E',
  'Todas essas são energias de **ordem física**. A ordem **química** reúne cáusticos e venenos.',
  peg='Trocar "física" por "química" num rol que a banca copia inteiro.',
  kw=['ordem física', 'energias vulnerantes'])
I(P, 2, 'Infortunística',
  'Infortunística é o capítulo da Medicina Legal que estuda os acidentes do trabalho e as doenças profissionais.', 'C',
  'A **infortunística** cuida do infortúnio laboral: nexo entre trabalho e dano, incapacidade e sua extensão.',
  kw=['infortunística', 'acidente do trabalho'])
I(P, 2, 'Criminalística',
  'A criminalística ocupa-se, por excelência, dos vestígios intrínsecos, isto é, daqueles encontrados no corpo da vítima.', 'E',
  'A **criminalística** estuda os vestígios **extrínsecos** (local, armas, documentos, veículos). Os vestígios no corpo (intrínsecos) são objeto da perícia médico-legal.',
  peg='Trocar extrínseco por intrínseco.',
  kw=['criminalística', 'vestígios extrínsecos'])
I(P, 2, 'Diceologia',
  'Diceologia médica é o capítulo da Medicina Legal geral que trata dos direitos do médico.', 'C',
  '**Diceologia** = direitos; deontologia = deveres. Ambos compõem a Medicina Legal geral.',
  kw=['diceologia', 'direitos do médico'])
I(P, 2, 'Energia de ordem bioquímica',
  'Venenos e cáusticos são exemplos de energia de ordem bioquímica.', 'E',
  'Venenos e cáusticos são energia de ordem **química**. A ordem **bioquímica** abrange perturbações como inanição, carências alimentares, infecções e autointoxicações.',
  peg='Confundir química (venenos, cáusticos) com bioquímica (fome, infecção).',
  kw=['ordem química', 'ordem bioquímica'])

# ======================= MLE-1.1 · Corpo de delito, perícia e peritos =======================
P = 'DBA26-MLE-1.1'
I(P, 1, 'Exame indispensável e confissão',
  'Quando a infração deixar vestígios, a confissão do acusado pode suprir o exame de corpo de delito, desde que prestada perante a autoridade judicial.', 'E',
  'O art. 158 do CPP não deixa margem: havendo vestígio, o **exame de corpo de delito** não se dispensa e a confissão não o substitui, venha ela de onde vier.',
  lei=[(CPP + '158', 'Quando a infração deixar vestígios', 'não podendo supri-lo a confissão do acusado.', 'CPP, art. 158')],
  peg='Acrescentar uma condição ("perante o juiz") que torne a confissão suficiente.',
  kw=['exame de corpo de delito', 'confissão'])
I(P, 1, 'Corpo de delito direto e indireto',
  'Corpo de delito é o conjunto dos vestígios materiais deixados pela infração; o exame é direto quando o perito examina o próprio vestígio e indireto quando a conclusão se apoia em outros elementos, e, desaparecidos os vestígios, a prova testemunhal pode suprir a falta.', 'C',
  'O **exame direto** recai sobre o vestígio; o **indireto** se faz a partir de dados mediatos (prontuário, fotos, relatos). Sumidos os vestígios, a **prova testemunhal** supre (art. 167).',
  lei=[(CPP + '167', 'Não sendo possível o exame de corpo de delito', 'poderá suprir-lhe a falta.', 'CPP, art. 167')],
  kw=['corpo de delito', 'exame indireto'])
I(P, 1, 'Perito oficial',
  'O exame de corpo de delito e as outras perícias serão realizados por perito oficial, portador de diploma de curso superior.', 'C',
  'Desde a Lei 11.690/2008 basta **um perito oficial** com diploma superior.',
  lei=[(CPP + '159', 'O exame de corpo de delito e outras perícias', 'portador de diploma de curso superior.', 'CPP, art. 159')],
  kw=['perito oficial', 'diploma de curso superior'])
I(P, 1, 'Peritos não oficiais',
  'Na falta de perito oficial, o exame será realizado por uma pessoa idônea, portadora de diploma de curso superior, que prestará o compromisso de bem e fielmente desempenhar o encargo.', 'E',
  'Sem perito oficial, são **duas pessoas idôneas** com diploma superior, preferencialmente na área do exame, que prestam compromisso (art. 159, §§ 1º e 2º).',
  lei=[(CPP + '159', 'Na falta de perito oficial', 'relacionada com a natureza do exame.', 'CPP, art. 159, § 1º')],
  peg='Trocar "2 (duas) pessoas" por "uma pessoa".',
  kw=['duas pessoas idôneas', 'peritos não oficiais'])
I(P, 1, 'Prazo do laudo',
  'O laudo pericial será elaborado no prazo máximo de 10 dias, podendo esse prazo ser prorrogado, em casos excepcionais, a requerimento dos peritos.', 'C',
  'Literalidade do art. 160, parágrafo único: **10 dias**, prorrogáveis em casos excepcionais a pedido dos peritos.',
  lei=[(CPP + '160', 'O laudo pericial será elaborado no prazo máximo de 10 dias', 'a requerimento dos peritos.', 'CPP, art. 160, par. ún.')],
  kw=['10 dias', 'laudo pericial'])
I(P, 1, 'Momento da autópsia',
  'A autópsia será feita pelo menos doze horas depois do óbito, salvo se os peritos, pela evidência dos sinais de morte, julgarem que possa ser feita antes.', 'E',
  'O prazo legal é de **seis horas**, e pode ser encurtado se os sinais de morte forem evidentes, o que os peritos declaram no auto.',
  lei=[(CPP + '162', 'A autópsia será feita pelo menos seis horas depois do óbito', 'o que declararão no auto.', 'CPP, art. 162')],
  peg='Dobrar o número (seis → doze horas).',
  kw=['seis horas', 'autópsia'])
I(P, 1, 'Livre apreciação do laudo',
  'O juiz não ficará adstrito ao laudo, podendo aceitá-lo ou rejeitá-lo, no todo ou em parte.', 'C',
  'O CPP adota o **sistema liberatório**: o laudo é prova como as demais, e o juiz pode afastá-lo fundamentadamente.',
  lei=[(CPP + '182', 'O juiz não ficará adstrito ao laudo', 'no todo ou em parte.', 'CPP, art. 182')],
  kw=['sistema liberatório', 'não ficará adstrito ao laudo'])
I(P, 1, 'Assistente técnico',
  'O assistente técnico indicado pela parte acompanha os exames desde o início, atuando ao lado dos peritos oficiais já na fase do inquérito.', 'E',
  'O **assistente técnico** atua **após admitido pelo juiz** e **depois de concluídos os exames e elaborado o laudo** pelos peritos oficiais (art. 159, § 4º).',
  lei=[(CPP + '159', 'O assistente técnico atuará a partir de sua admissão pelo juiz', 'sendo as partes intimadas desta decisão.', 'CPP, art. 159, § 4º')],
  peg='Antecipar a atuação do assistente para durante o exame.',
  kw=['assistente técnico', 'após a conclusão dos exames'])

# --- MLE-1.1 · Rodada 2
I(P, 2, 'Exame complementar na lesão grave',
  'Se o exame complementar tiver por fim precisar a lesão grave por incapacidade para as ocupações habituais por mais de trinta dias, deverá ser feito logo que decorra o prazo de 30 dias, contado da data do crime, e sua falta pode ser suprida pela prova testemunhal.', 'C',
  'O **exame complementar** do art. 168, § 2º, conta os 30 dias **da data do crime**; a falta dele pode ser suprida por **testemunhas** (§ 3º).',
  lei=[(CPP + '168', 'Se o exame tiver por fim precisar a classificação do delito', 'contado da data do crime.', 'CPP, art. 168, § 2º'),
       (CPP + '168', 'A falta de exame complementar', 'prova testemunhal.', 'CPP, art. 168, § 3º')],
  peg='Contar os 30 dias do primeiro exame ou da notícia do crime, e não da data do crime.',
  kw=['exame complementar', '30 dias'])
I(P, 2, 'Prioridade do exame',
  'A prioridade legal na realização do exame de corpo de delito restringe-se aos crimes que envolvam violência doméstica e familiar contra a mulher.', 'E',
  'A **prioridade** do art. 158, parágrafo único, alcança também a violência contra **criança, adolescente, idoso ou pessoa com deficiência**.',
  lei=[(CPP + '158', 'Dar-se-á prioridade à realização do exame de corpo de delito', 'idoso ou pessoa com deficiência.', 'CPP, art. 158, par. ún.')],
  peg='Cortar o inciso II do rol.',
  kw=['prioridade', 'pessoa com deficiência'])
I(P, 2, 'Divergência entre peritos',
  'Havendo divergência entre os peritos, cada um pode redigir separadamente o seu laudo, e a autoridade nomeará um terceiro; se este divergir de ambos, poderá ser determinado novo exame por outros peritos.', 'C',
  'É o art. 180: **terceiro perito** e, se a divergência persistir, **novo exame**.',
  lei=[(CPP + '180', 'Se houver divergência entre os peritos', 'novo exame por outros peritos.', 'CPP, art. 180')],
  kw=['divergência entre os peritos', 'terceiro perito'])
I(P, 2, 'Súmula 361 do STF e o perito oficial',
  'Por força da Súmula 361 do STF, ainda hoje é nulo o exame realizado por um único perito oficial.', 'E',
  'Depois da Lei 11.690/2008, **um só perito oficial** basta (art. 159, caput). Para a posição majoritária, a **Súmula 361** só conserva sentido para os **peritos não oficiais**, que continuam a ser dois.',
  lei=[(CPP + '159', 'O exame de corpo de delito e outras perícias', 'portador de diploma de curso superior.', 'CPP, art. 159')],
  juris=[J['STF361']],
  peg='Aplicar a súmula de 1963 ao perito oficial, ignorando a redação de 2008.',
  kw=['Súmula 361', 'um só perito oficial'])
I(P, 2, 'Perícia indeferível',
  'Salvo o exame de corpo de delito, o juiz ou a autoridade policial negará a perícia requerida pelas partes quando não for necessária ao esclarecimento da verdade.', 'C',
  'O art. 184 permite **indeferir perícia** desnecessária — **nunca** o exame de corpo de delito.',
  lei=[(CPP + '184', 'Salvo o caso de exame de corpo de delito', 'esclarecimento da verdade.', 'CPP, art. 184')],
  kw=['negará a perícia', 'exame de corpo de delito'])
I(P, 2, 'Perícia percipiendi × deducendi',
  'Perícia percipiendi é aquela em que o perito apenas interpreta fatos já documentados por outros, sem examinar diretamente o objeto.', 'E',
  'Na perícia **percipiendi** o perito **percebe e constata** diretamente (examina a pessoa, o cadáver, a coisa). Interpretar fatos já apurados é a perícia **deducendi**.',
  peg='Inverter as duas espécies.',
  kw=['percipiendi', 'deducendi'])
I(P, 2, 'Dia e hora do exame',
  'O exame de corpo de delito poderá ser feito em qualquer dia e a qualquer hora.', 'C',
  'Literalidade do art. 161: o vestígio não espera — **qualquer dia e qualquer hora**.',
  lei=[(CPP + '161', 'O exame de corpo de delito poderá ser feito', 'a qualquer hora.', 'CPP, art. 161')],
  kw=['qualquer dia', 'qualquer hora'])

# ======================= MLE-2 · Documentos médico-legais =======================
P = 'DBA26-MLE-2'
I(P, 1, 'Laudo × auto',
  'No relatório médico-legal, o laudo é redigido pelo próprio perito após o exame, enquanto o auto é ditado pelo perito ao escrivão, na presença da autoridade.', 'C',
  'Os dois são **relatórios**; muda a forma: o **laudo** é escrito pelo perito depois; o **auto** é ditado ao escrivão durante o ato, diante da autoridade.',
  kw=['laudo', 'auto'])
I(P, 1, 'Descrição no relatório',
  'A descrição é parte dispensável do relatório médico-legal quando a conclusão do perito for clara e objetiva.', 'E',
  'A **descrição** é a parte mais importante (o *visum et repertum*): a lei manda que os peritos descrevam **minuciosamente** o que examinarem.',
  lei=[(CPP + '160', 'Os peritos elaborarão o laudo pericial', 'responderão aos quesitos formulados.', 'CPP, art. 160')],
  peg='Inverter a hierarquia: a conclusão sem a descrição não se sustenta.',
  kw=['descrição', 'minuciosamente'])
I(P, 1, 'Parecer médico-legal',
  'No parecer médico-legal, a parte mais relevante é a discussão, pois o parecerista analisa fatos e documentos já produzidos, em resposta a uma consulta.', 'C',
  'O **parecer** responde a uma **consulta** a especialista e, por não partir de exame próprio, tem na **discussão** o seu núcleo.',
  kw=['parecer', 'discussão'])
I(P, 1, 'Atestado',
  'O atestado médico é documento que exige compromisso legal do médico e destina-se sempre a instruir processo judicial.', 'E',
  'O **atestado** é afirmação simples e escrita de um fato médico e de suas consequências; **não exige compromisso legal** e pode ter fins oficiosos, administrativos ou judiciais.',
  peg='Atribuir ao atestado o compromisso e o destino exclusivo do laudo.',
  kw=['atestado', 'sem compromisso'])
I(P, 1, 'Notificação compulsória',
  'Os casos de suspeita ou confirmação de violência contra pessoa idosa são de notificação compulsória pelos serviços de saúde públicos e privados.', 'C',
  'A **notificação compulsória** é documento médico-legal: comunicação obrigatória à autoridade. O Estatuto da Pessoa Idosa a exige já na **suspeita**.',
  lei=[('L10741:19', 'Os casos de suspeita ou confirmação de violência praticada contra pessoas idosas', 'autoridade sanitária', 'Lei 10.741/2003, art. 19')],
  kw=['notificação compulsória', 'suspeita ou confirmação'])
I(P, 1, 'Prontuário',
  'O prontuário médico pertence ao médico que o elaborou, que pode negar ao paciente o acesso ao seu conteúdo.', 'E',
  'O **prontuário** pertence ao **paciente**; o médico e a instituição apenas o guardam. O paciente tem direito de acesso e de cópia.',
  peg='Trocar o titular (paciente) pelo guardião (médico).',
  kw=['prontuário', 'pertence ao paciente'])
I(P, 1, 'Depoimento oral do perito',
  'Durante o processo, as partes podem requerer a oitiva dos peritos para esclarecerem a prova, desde que o mandado e os quesitos sejam encaminhados com antecedência mínima de 10 dias.', 'C',
  'O **depoimento oral** do perito é documento médico-legal verbal; o CPP exige **10 dias** de antecedência e admite respostas em laudo complementar.',
  lei=[(CPP + '159', 'requerer a oitiva dos peritos', 'antecedência mínima de 10 (dez) dias', 'CPP, art. 159, § 5º, I')],
  kw=['depoimento oral', 'oitiva dos peritos'])
I(P, 1, 'Declaração de óbito na morte violenta',
  'Na morte violenta, ainda que ocorrida no hospital semanas após o fato, a declaração de óbito é emitida pelo médico assistente que acompanhou a internação.', 'E',
  'Morte **violenta** (ou suspeita) tem a declaração de óbito emitida pelo **perito do IML**, mesmo que tardia, pois o nexo causal com a lesão se mantém.',
  peg='Deslocar para o médico assistente o que é do IML.',
  kw=['declaração de óbito', 'IML'])

# --- MLE-2 · Rodada 2
I(P, 2, 'Partes do relatório',
  'O relatório médico-legal compõe-se, em regra, de preâmbulo, quesitos, histórico, descrição, discussão, conclusão e respostas aos quesitos.', 'C',
  'Ordem clássica das **partes do relatório**: preâmbulo → quesitos → histórico (comemorativo) → descrição → discussão → conclusão → respostas aos quesitos.',
  kw=['partes do relatório', 'preâmbulo'])
I(P, 2, 'Histórico',
  'O histórico do relatório médico-legal tem fé pública, pois os fatos nele narrados são constatados pelo perito.', 'E',
  'O **histórico** (comemorativo) registra o que o examinado ou terceiros **relatam**; o perito não o atesta. Fé técnica tem a **descrição**, que é o que o perito viu.',
  peg='Dar ao relato do periciando o valor da constatação do perito.',
  kw=['histórico', 'comemorativo'])
I(P, 2, 'Visum et repertum',
  'A expressão visum et repertum designa a descrição, parte do relatório em que o perito registra o que viu e encontrou.', 'C',
  '"Visto e achado": é a **descrição**, núcleo técnico do laudo.',
  kw=['visum et repertum', 'descrição'])
I(P, 2, 'Prova na Lei Maria da Penha',
  'Nos casos de violência doméstica e familiar contra a mulher, só o laudo do instituto médico-legal é admitido como prova da lesão, sendo inservíveis os prontuários hospitalares.', 'E',
  'A Lei 11.340/2006 admite como prova os **laudos ou prontuários médicos** fornecidos por **hospitais e postos de saúde**.',
  lei=[('L11340:12', 'Serão admitidos como meios de prova', 'hospitais e postos de saúde.', 'Lei 11.340/2006, art. 12, § 3º')],
  peg='Negar o que a lei expressamente admite.',
  kw=['prontuários médicos', 'meios de prova'])
I(P, 2, 'Parecer do assistente técnico',
  'No curso do processo, as partes podem indicar assistentes técnicos que poderão apresentar pareceres em prazo fixado pelo juiz ou ser inquiridos em audiência.', 'C',
  'O **parecer** do **assistente técnico** é documento médico-legal da parte (art. 159, § 5º, II).',
  lei=[(CPP + '159', 'indicar assistentes técnicos', 'inquiridos em audiência.', 'CPP, art. 159, § 5º, II')],
  kw=['assistente técnico', 'pareceres'])
I(P, 2, 'SVO × IML',
  'Os Serviços de Verificação de Óbito são competentes para esclarecer a causa da morte violenta, cabendo ao IML apenas as mortes naturais sem assistência médica.', 'E',
  'É o inverso: o **SVO** esclarece **mortes naturais** sem causa definida; o **IML** faz a necropsia nas mortes **violentas** ou suspeitas.',
  peg='Inverter as atribuições dos dois serviços.',
  kw=['SVO', 'IML'])

# ======================= MLE-2.1 · Identidade, identificação e reconhecimento =======================
P = 'DBA26-MLE-2.1'
I(P, 1, 'Identidade',
  'Identidade é o conjunto de caracteres próprios e exclusivos que individualizam uma pessoa, tornando-a igual apenas a si mesma.', 'C',
  'A **identidade** é o que a pessoa é; a **identificação** é o meio técnico de estabelecê-la.',
  kw=['identidade', 'caracteres próprios'])
I(P, 1, 'Identificação × reconhecimento',
  'Identificação e reconhecimento são expressões sinônimas, pois ambas se baseiam na comparação técnica de registros.', 'E',
  'O **reconhecimento** é ato **empírico**, apoiado na memória de quem reconhece; a **identificação** é **técnico-científica**, compara registros feitos em momentos distintos.',
  peg='Tratar como sinônimos o empírico e o científico.',
  kw=['reconhecimento', 'identificação'])
I(P, 1, 'Requisitos de um método de identificação',
  'Um bom método de identificação deve reunir requisitos biológicos — unicidade, imutabilidade e perenidade — e requisitos técnicos — praticabilidade e classificabilidade.', 'C',
  'São os cinco **requisitos** clássicos; a datiloscopia os reúne, por isso se impôs.',
  kw=['unicidade', 'imutabilidade', 'perenidade'])
I(P, 1, 'Perenidade × imutabilidade',
  'Imutabilidade é o requisito pelo qual o caractere existe desde a vida intrauterina e persiste até a putrefação.', 'E',
  'Essa é a **perenidade** (duração no tempo). **Imutabilidade** é o caractere não mudar de forma ao longo da vida.',
  peg='Trocar o nome de um requisito pelo de outro.',
  kw=['perenidade', 'imutabilidade'])
I(P, 1, 'Reconhecimento de pessoa',
  'No reconhecimento de pessoa, quem for reconhecer será primeiro convidado a descrever a pessoa que deva ser reconhecida.', 'C',
  'Primeiro passo do art. 226: **descrição prévia**; depois, a pessoa é posta, se possível, ao lado de outras semelhantes.',
  lei=[(CPP + '226', 'I - a pessoa que tiver de fazer o reconhecimento', 'que deva ser reconhecida;', 'CPP, art. 226, I')],
  kw=['reconhecimento de pessoa', 'descrever'])
I(P, 1, 'Identificação médico-legal × judiciária',
  'A identificação judiciária, também chamada policial, exige conhecimentos médicos, ao passo que a médico-legal pode ser feita por qualquer técnico treinado.', 'E',
  'É o inverso: a **identificação médico-legal** exige conhecimento médico (sexo, idade, estatura, lesões); a **judiciária** (policial) usa técnicas como a datiloscopia e dispensa formação médica.',
  peg='Inverter as duas espécies.',
  kw=['identificação médico-legal', 'identificação judiciária'])
I(P, 1, 'Civilmente identificado',
  'O civilmente identificado não será submetido a identificação criminal, salvo nas hipóteses previstas em lei.', 'C',
  'Garantia do art. 5º, LVIII, da CF, regulamentada pela **Lei 12.037/2009**.',
  lei=[('CF:5', 'LVIII - o civilmente identificado', 'salvo nas hipóteses previstas em lei;', 'CF, art. 5º, LVIII')],
  kw=['civilmente identificado', 'identificação criminal'])
I(P, 1, 'Identificação criminal e ordem judicial',
  'Mesmo apresentado documento de identificação, a identificação criminal só pode ocorrer por ordem judicial.', 'E',
  'Só a hipótese do art. 3º, IV (identificação **essencial às investigações**) depende de **despacho judicial**; as demais (rasura, documento insuficiente, documentos conflitantes, uso de outros nomes etc.) independem dele.',
  lei=[('L12037:3', 'Embora apresentado documento de identificação', 'o documento apresentar rasura ou tiver indício de falsificação;', 'Lei 12.037/2009, art. 3º, caput e I')],
  peg='Generalizar para todas as hipóteses a exigência de um só inciso.',
  kw=['identificação criminal', 'despacho judicial'])

# --- MLE-2.1 · Rodada 2
I(P, 2, 'Dois registros',
  'Identificar pressupõe ao menos dois registros: um anterior, de referência, e outro atual, que com ele é comparado.', 'C',
  'Sem o **registro prévio** não há identificação, só descrição. Por isso a ossada sem referência precisa de DNA de parentes, ficha odontológica ou datiloscópica.',
  kw=['dois registros', 'comparação'])
I(P, 2, 'Reconhecimento em juízo',
  'A providência para que a pessoa a ser reconhecida não veja quem a reconhece, por receio de intimidação, aplica-se também na instrução criminal e no plenário do júri.', 'E',
  'O parágrafo único do art. 226 **afasta** o inciso III na **fase da instrução** e no **plenário**.',
  lei=[(CPP + '226', 'O disposto no no III deste artigo', 'em plenário de julgamento.', 'CPP, art. 226, par. ún.')],
  peg='Estender ao juízo uma cautela que a lei limita ao inquérito.',
  kw=['reconhecimento', 'plenário'])
I(P, 2, 'Identificação criminal essencial',
  'A identificação criminal essencial às investigações depende de despacho da autoridade judiciária, que decide de ofício ou mediante representação da autoridade policial, do Ministério Público ou da defesa.', 'C',
  'Literalidade do art. 3º, IV, da Lei 12.037/2009: **despacho judicial**, de ofício ou provocado.',
  lei=[('L12037:3', 'IV – a identificação criminal for essencial', 'do Ministério Público ou da defesa;', 'Lei 12.037/2009, art. 3º, IV')],
  kw=['essencial às investigações', 'despacho da autoridade judiciária'])
I(P, 2, 'Banco de perfis genéticos',
  'As informações dos bancos de perfis genéticos podem revelar traços somáticos e comportamentais das pessoas, desde que necessários à investigação.', 'E',
  'O banco **não pode revelar traços somáticos ou comportamentais**, exceto a **determinação genética de gênero**.',
  lei=[('L12037:5-A', 'As informações genéticas contidas nos bancos', 'exceto determinação genética de gênero', 'Lei 12.037/2009, art. 5º-A, § 1º')],
  peg='Trocar a vedação por uma permissão condicionada.',
  kw=['perfis genéticos', 'traços somáticos'])
I(P, 2, 'Objeto da identificação médico-legal',
  'A identificação médico-legal pode recair sobre o vivo, o cadáver ou restos esqueléticos e inclui a estimativa de espécie, sexo, idade e estatura.', 'C',
  'A **identificação médico-legal** parte do geral (espécie, sexo, idade, estatura) para o individual (sinais particulares, arcada, DNA).',
  kw=['identificação médico-legal', 'estatura'])
I(P, 2, 'Identificação criminal após a denúncia',
  'A simples instauração de inquérito por crime contra a liberdade sexual autoriza, por si só, a identificação criminal do civilmente identificado.', 'E',
  'A hipótese incluída pela Lei 15.295/2025 exige o **recebimento da denúncia** por crime contra a liberdade sexual (ou sexual contra vulnerável), não a mera instauração do inquérito.',
  lei=[('L12037:3', 'VII – houver recebimento da denúncia pelo juiz por:', 'b) crime contra a liberdade sexual ou crime sexual contra vulnerável;', 'Lei 12.037/2009, art. 3º, VII, a e b')],
  peg='Antecipar o marco: inquérito no lugar do recebimento da denúncia.',
  kw=['recebimento da denúncia', 'liberdade sexual'])

# ======================= MLE-3 · Principais métodos de identificação =======================
P = 'DBA26-MLE-3'
I(P, 1, 'Datiloscopia de Vucetich',
  'O sistema datiloscópico adotado no Brasil classifica as impressões digitais em quatro tipos fundamentais: arco, presilha interna, presilha externa e verticilo.', 'C',
  'Os **quatro tipos fundamentais** de Vucetich distinguem-se pela presença e posição do **delta**.',
  kw=['tipos fundamentais', 'datiloscopia'])
I(P, 1, 'Arco',
  'O arco é o tipo fundamental que apresenta um delta, situado à direita do observador.', 'E',
  'O **arco** **não tem delta**: as linhas atravessam o desenho de um lado a outro. Um delta tem a presilha; dois, o verticilo.',
  peg='Dar ao arco o delta que é da presilha.',
  kw=['arco', 'sem delta'])
I(P, 1, 'Verticilo',
  'O verticilo apresenta dois deltas, um de cada lado do núcleo.', 'C',
  '**Verticilo** = **dois deltas**, com núcleo em espiral, círculos ou elipses.',
  kw=['verticilo', 'dois deltas'])
I(P, 1, 'Presilha interna × externa',
  'Na presilha interna, o delta fica à esquerda do observador, e na presilha externa, à direita.', 'E',
  'É o contrário: **presilha interna** — delta à **direita** do observador; **presilha externa** — delta à **esquerda**.',
  peg='Inverter os lados do delta.',
  kw=['presilha interna', 'presilha externa'])
I(P, 1, 'Gêmeos univitelinos',
  'Gêmeos univitelinos compartilham o mesmo DNA nuclear, mas têm impressões digitais distintas.', 'C',
  'O **DNA nuclear** não distingue gêmeos monozigóticos; as **impressões digitais**, formadas no útero com influência do ambiente, distinguem.',
  kw=['gêmeos univitelinos', 'impressões digitais'])
I(P, 1, 'Bertillonagem',
  'O sistema antropométrico de Bertillon, baseado em medidas do corpo, continua sendo o método oficial de identificação civil no Brasil.', 'E',
  'A **antropometria** de Bertillon foi abandonada (medidas variam, falhas de individualização) e substituída pela **datiloscopia**.',
  peg='Dar como vigente um método histórico.',
  kw=['Bertillon', 'antropometria'])
I(P, 1, 'Identificação odontológica',
  'A identificação odontológica é especialmente útil em cadáveres carbonizados, pois dentes e restaurações resistem a altas temperaturas.', 'C',
  'Os **dentes** são o tecido mais resistente do corpo; comparados com a ficha do dentista, identificam carbonizados e esqueletizados.',
  kw=['identificação odontológica', 'carbonizados'])
I(P, 1, 'Queiloscopia',
  'Queiloscopia é o estudo das rugosidades do palato duro para fins de identificação.', 'E',
  '**Queiloscopia** estuda os sulcos dos **lábios**; o estudo das rugosidades do **palato** é a **palatoscopia** (rugoscopia palatina).',
  peg='Trocar lábios por palato.',
  kw=['queiloscopia', 'palatoscopia'])

# --- MLE-3 · Rodada 2
I(P, 2, 'Pontos característicos',
  'No Brasil, o critério tradicional para afirmar a identidade datiloscópica é a coincidência de pelo menos doze pontos característicos, sem nenhuma divergência.', 'C',
  'É o critério mais cobrado (**doze pontos**). Há divergência técnica — outros países e escolas usam critérios qualitativos ou números diferentes —, mas a banca costuma exigir os 12 pontos sem discrepância.',
  kw=['doze pontos', 'pontos característicos'])
I(P, 2, 'Poroscopia',
  'A poroscopia é o método que identifica a pessoa pela forma e direção das cristas papilares.', 'E',
  'A **poroscopia** estuda os **poros** (forma, número, posição) nas cristas; o desenho das cristas é a própria datiloscopia.',
  peg='Trocar poros por cristas.',
  kw=['poroscopia', 'poros'])
I(P, 2, 'Sexo no esqueleto',
  'No esqueleto adulto, a pelve é a peça óssea mais confiável para o diagnóstico do sexo.', 'C',
  'A **pelve** reflete a função reprodutiva (pelve feminina mais larga, ângulo subpúbico mais aberto); o crânio vem em seguida.',
  kw=['pelve', 'diagnóstico do sexo'])
I(P, 2, 'Fórmula datiloscópica',
  'Na fórmula datiloscópica de Vucetich, os polegares são representados por números e os demais dedos por letras.', 'E',
  'É o inverso: **polegares por letras** (A, I, E, V) e **demais dedos por números** (1, 2, 3, 4).',
  peg='Inverter letras e números.',
  kw=['fórmula datiloscópica', 'polegares'])
I(P, 2, 'DNA mitocondrial',
  'O DNA mitocondrial é herdado pela linha materna e é útil para identificar restos degradados, comparando-os com parentes do lado materno.', 'C',
  'O **DNA mitocondrial** existe em muitas cópias por célula (resiste melhor à degradação) e passa de **mãe** para os filhos.',
  kw=['DNA mitocondrial', 'linha materna'])
I(P, 2, 'Perfil genético na execução penal',
  'Todo condenado por crime doloso, qualquer que seja o regime inicial, será submetido obrigatoriamente à identificação do perfil genético ao ingressar no estabelecimento prisional.', 'E',
  'Pela redação vigente (Lei 15.295/2025), a coleta obrigatória atinge o condenado à pena de **reclusão em regime inicial fechado**.',
  lei=[('L7210:9-A', 'O condenado à pena de reclusão em regime inicial fechado', 'ingresso no estabelecimento prisional.', 'LEP, art. 9º-A')],
  peg='Ampliar o alcance subjetivo da norma ("todo condenado").',
  kw=['perfil genético', 'regime inicial fechado'])
