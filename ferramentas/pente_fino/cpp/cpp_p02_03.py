# Pente Fino de Direito Processual Penal — CPP-2 (inquérito), 2.1 (inquérito em detalhe), 2.2 (jurisdição, competência,
# conexão, continência, prevenção, questões e processos incidentes) e CPP-3 (processo: finalidade, pressupostos, sistemas)
# (08/11/2026).
from base import I
from cpp_juris import J

CPP = 'CPP:'
CF = 'CF:'
DEL = 'L12830:'

# ======================= CPP-2 · Inquérito policial =======================
P = 'DBA26-CPP-2'
I(P, 1, 'Polícia judiciária',
  'A polícia judiciária será exercida pelas autoridades policiais no território de suas respectivas circunscrições e terá por fim a apuração das infrações penais e da sua autoria.', 'C',
  'Literal no **art. 4º** do CPP. O parágrafo único admite que outras autoridades administrativas tenham a mesma função por lei.',
  lei=[(CPP + '4', 'A polícia judiciária será exercida pelas autoridades policiais', 'apuração das infrações penais e da sua autoria', 'CPP, art. 4º, caput')],
  kw=['polícia judiciária', 'circunscrições'])
I(P, 1, 'Natureza das funções do delegado',
  'As funções de polícia judiciária e a apuração de infrações penais exercidas pelo delegado de polícia são de natureza jurídica, essenciais e exclusivas de Estado.', 'C',
  'É o **art. 2º da Lei 12.830/2013**.',
  lei=[(DEL + '2', 'As funções de polícia judiciária e a apuração de infrações penais exercidas pelo delegado de polícia', 'exclusivas de Estado', 'Lei 12.830/2013, art. 2º')],
  kw=['natureza jurídica', 'exclusivas de Estado'])
I(P, 1, 'Exclusividade da investigação',
  'A investigação criminal é monopólio da polícia judiciária, de modo que o Ministério Público não pode conduzir procedimento investigatório próprio.', 'E',
  'O STF (**Tema 184**) reconheceu o poder de investigação do **MP**, por autoridade própria e prazo razoável, com controle jurisdicional. Além disso, o art. 4º, par. ún., do CPP admite outras autoridades administrativas.',
  lei=[(CPP + '4', 'A competência definida neste artigo não excluirá a de autoridades administrativas', None, 'CPP, art. 4º, par. ún.')],
  juris=[J['RG184']],
  peg='Afirmar monopólio policial da investigação.',
  kw=['Tema 184', 'poder de investigação do MP'])
I(P, 1, 'Dispensabilidade',
  'O inquérito policial é indispensável ao oferecimento da denúncia, que não pode ser apresentada com base em outras peças de informação.', 'E',
  'O inquérito é **dispensável**: acompanha a denúncia "sempre que servir de base" (art. 12); o MP pode denunciar com outras **peças de informação** (art. 39, § 5º).',
  lei=[(CPP + '12', 'O inquérito policial acompanhará a denúncia ou queixa, sempre que servir de base a uma ou outra', None, 'CPP, art. 12')],
  peg='Tratar o inquérito como condição da ação.',
  kw=['dispensável', 'peças de informação'])
I(P, 1, 'Avocação e redistribuição',
  'O inquérito policial em curso somente poderá ser avocado ou redistribuído por superior hierárquico, mediante despacho fundamentado, por motivo de interesse público ou nas hipóteses de inobservância dos procedimentos previstos em regulamento da corporação que prejudique a eficácia da investigação.', 'C',
  'Garantia do **delegado natural** na Lei 12.830/2013, art. 2º, § 4º.',
  lei=[(DEL + '2', 'O inquérito policial ou outro procedimento previsto em lei em curso somente poderá ser avocado', 'prejudique a eficácia da investigação', 'Lei 12.830/2013, art. 2º, § 4º')],
  kw=['avocado ou redistribuído', 'despacho fundamentado'])
I(P, 1, 'Remoção do delegado',
  'A remoção do delegado de polícia pode ser feita livremente pela chefia, sem necessidade de motivação, por se tratar de ato discricionário.', 'E',
  'A Lei 12.830/2013 exige **ato fundamentado** para a remoção (art. 2º, § 5º).',
  lei=[(DEL + '2', 'A remoção do delegado de polícia dar-se-á somente por ato fundamentado', None, 'Lei 12.830/2013, art. 2º, § 5º')],
  peg='Trocar "somente por ato fundamentado" por "livremente".',
  kw=['remoção', 'ato fundamentado'])
# --- CPP-2 · Rodada 2
I(P, 2, 'Requisições do delegado',
  'Durante a investigação criminal, a requisição de perícia, informações, documentos e dados pelo delegado depende sempre de prévia autorização judicial.', 'E',
  'Lei 12.830/2013, art. 2º, § 2º: o **poder requisitório** é do próprio delegado; só dados protegidos por reserva de jurisdição exigem ordem judicial.',
  lei=[(DEL + '2', 'Durante a investigação criminal, cabe ao delegado de polícia a requisição de perícia', 'apuração dos fatos', 'Lei 12.830/2013, art. 2º, § 2º')],
  peg='Submeter toda requisição à autorização judicial.',
  kw=['requisição', 'poder requisitório'])
I(P, 2, 'Termo circunstanciado e polícia militar',
  'Para o STF, a lavratura do termo circunstanciado é atividade investigativa privativa da polícia judiciária, sendo inconstitucional lei estadual que a atribua à polícia militar.', 'E',
  'O STF (ADI 5.637) entendeu que o **termo circunstanciado** não é atividade investigativa nem **privativa** da polícia judiciária, e validou lei estadual que o atribui à PM. Na Lei 9.099/1995, o TCO é lavrado pela "autoridade policial" (art. 69).',
  lei=[('L9099:69', 'A autoridade policial que tomar conhecimento da ocorrência lavrará termo circunstanciado', None, 'Lei 9.099/1995, art. 69')],
  juris=[J['ADI5637']],
  peg='Tratar o TCO como ato privativo do delegado.',
  kw=['termo circunstanciado', 'não privativo'])
I(P, 2, 'Valor probatório',
  'O juiz não pode fundamentar a condenação exclusivamente nos elementos informativos colhidos na investigação, ressalvadas as provas cautelares, não repetíveis e antecipadas.', 'C',
  'Art. 155 do CPP: o inquérito tem **valor probatório relativo**; os elementos informativos só reforçam a prova judicial.',
  lei=[(CPP + '155', 'não podendo fundamentar sua decisão exclusivamente nos elementos informativos colhidos na investigação', 'não repetíveis e antecipadas', 'CPP, art. 155')],
  kw=['elementos informativos', 'valor probatório relativo'])
I(P, 2, 'Vício do inquérito',
  'Eventual irregularidade ocorrida no inquérito policial contamina automaticamente a ação penal dele decorrente, gerando a nulidade do processo.', 'E',
  'Por ser **peça informativa**, o vício do inquérito em regra **não contamina** a ação penal; atinge o ato viciado (ex.: prova ilícita, que se desentranha — art. 157).',
  lei=[(CPP + '157', 'São inadmissíveis, devendo ser desentranhadas do processo, as provas ilícitas', None, 'CPP, art. 157, caput')],
  peg='Estender automaticamente o vício do inquérito ao processo.',
  kw=['peça informativa', 'não contamina'])

# ======================= CPP-2.1 · Inquérito em detalhe =======================
P = 'DBA26-CPP-2.1'
I(P, 1, 'Formas de instauração',
  'Nos crimes de ação pública incondicionada, o inquérito policial será iniciado de ofício, mediante requisição da autoridade judiciária ou do Ministério Público, ou a requerimento do ofendido ou de quem tiver qualidade para representá-lo.', 'C',
  'Art. 5º, I e II, do CPP. Com a estrutura acusatória (art. 3º-A), a **requisição judicial** é vista com reservas pela doutrina.',
  lei=[(CPP + '5', 'Nos crimes de ação pública o inquérito policial será iniciado:', 'quem tiver qualidade para representá-lo.', 'CPP, art. 5º, I e II')],
  kw=['de ofício', 'requisição'])
I(P, 1, 'Ação condicionada e inquérito',
  'Nos crimes de ação pública condicionada à representação, a autoridade policial pode instaurar o inquérito de ofício, colhendo depois a representação da vítima.', 'E',
  'Sem **representação**, o inquérito **não pode ser iniciado** (art. 5º, § 4º). Na ação privada, exige-se **requerimento** de quem pode intentá-la (§ 5º).',
  lei=[(CPP + '5', 'O inquérito, nos crimes em que a ação pública depender de representação, não poderá sem ela ser iniciado', None, 'CPP, art. 5º, § 4º')],
  exc=['A prisão em flagrante é possível, mas a lavratura do auto depende da manifestação da vítima ou de seu representante'],
  peg='Admitir instauração de ofício nos crimes condicionados.',
  kw=['representação', 'não poderá sem ela ser iniciado'])
I(P, 1, 'Recurso contra indeferimento',
  'Do despacho que indeferir o requerimento de abertura de inquérito caberá recurso para o chefe de Polícia.', 'C',
  'Art. 5º, § 2º: **recurso administrativo** ao chefe de Polícia.',
  lei=[(CPP + '5', 'Do despacho que indeferir o requerimento de abertura de inquérito caberá recurso para o chefe de Polícia', None, 'CPP, art. 5º, § 2º')],
  kw=['chefe de Polícia', 'indeferir o requerimento'])
I(P, 1, 'Delatio criminis',
  'Qualquer pessoa do povo que tiver conhecimento de infração penal em que caiba ação pública poderá comunicá-la à autoridade policial, verbalmente ou por escrito, e esta, verificada a procedência das informações, mandará instaurar inquérito.', 'C',
  'É a **delatio criminis** simples (art. 5º, § 3º): faculdade de qualquer do povo, com **verificação de procedência** antes da instauração.',
  lei=[(CPP + '5', 'Qualquer pessoa do povo que tiver conhecimento da existência de infração penal', 'mandará instaurar inquérito.', 'CPP, art. 5º, § 3º')],
  kw=['delatio criminis', 'verificada a procedência'])
I(P, 1, 'Denúncia anônima',
  'A notícia anônima autoriza, por si só, a imediata instauração de inquérito policial e a decretação de medidas invasivas, como a interceptação telefônica.', 'E',
  'A **notícia anônima** exige **diligências preliminares** para verificar a procedência (art. 5º, § 3º); sozinha, não justifica inquérito nem medidas invasivas. A interceptação exige **indícios razoáveis** de autoria (Lei 9.296/1996, art. 2º, I).',
  lei=[(CPP + '5', 'verificada a procedência das informações, mandará instaurar inquérito', None, 'CPP, art. 5º, § 3º'),
       ('L9296:2', 'não houver indícios razoáveis da autoria ou participação em infração penal', None, 'Lei 9.296/1996, art. 2º, I')],
  peg='Dar à denúncia anônima força de justa causa imediata.',
  kw=['notícia anônima', 'diligências preliminares'])
I(P, 1, 'Prazos do inquérito',
  'O inquérito deverá terminar no prazo de 15 dias, se o indiciado estiver preso, e de 30 dias, quando estiver solto.', 'E',
  'Art. 10 do CPP: **10 dias** (preso) e **30 dias** (solto). Leis especiais trazem prazos próprios.',
  lei=[(CPP + '10', 'O inquérito deverá terminar no prazo de 10 dias', 'quando estiver solto, mediante fiança ou sem ela', 'CPP, art. 10, caput')],
  exc=['Lei 11.343/2006, art. 51: 30 dias (preso) e 90 dias (solto), duplicáveis', 'Inquérito federal (Lei 5.010/1966, art. 66): 15 dias, prorrogáveis por mais 15, com o indiciado preso'],
  peg='Trocar 10 por 15 dias (prazo do inquérito federal com preso).',
  kw=['10 dias', '30 dias'])
I(P, 1, 'Arquivamento pela autoridade policial',
  'A autoridade policial pode mandar arquivar autos de inquérito quando se convencer da atipicidade do fato.', 'E',
  'Art. 17: a autoridade policial **não poderá** mandar arquivar autos de inquérito (**indisponibilidade**).',
  lei=[(CPP + '17', 'A autoridade policial não poderá mandar arquivar autos de inquérito', None, 'CPP, art. 17')],
  peg='Dar ao delegado poder de arquivar.',
  kw=['indisponibilidade', 'arquivar'])
I(P, 1, 'Indiciamento',
  'O indiciamento pode ser requisitado pelo juiz ou pelo Ministério Público, cabendo ao delegado apenas formalizá-lo.', 'E',
  'Lei 12.830/2013, art. 2º, § 6º: o **indiciamento é privativo do delegado**, por ato fundamentado; juiz e MP não podem requisitá-lo.',
  lei=[(DEL + '2', 'O indiciamento, privativo do delegado de polícia', 'autoria, materialidade e suas circunstâncias', 'Lei 12.830/2013, art. 2º, § 6º')],
  peg='Retirar do delegado a privatividade do indiciamento.',
  kw=['indiciamento', 'privativo do delegado'])
I(P, 1, 'Sigilo e acesso do defensor',
  'Em razão do sigilo do inquérito, o defensor do investigado não tem acesso aos elementos de prova enquanto não concluída a investigação.', 'E',
  'O sigilo (art. 20) **não se opõe** ao defensor quanto aos elementos **já documentados** que digam respeito à defesa (**SV 14**). Diligências em curso podem ser mantidas em sigilo.',
  lei=[(CPP + '20', 'A autoridade assegurará no inquérito o sigilo necessário à elucidação do fato', None, 'CPP, art. 20, caput')],
  juris=[J['SV14']],
  exc=['Diligências ainda em andamento (ex.: interceptação em curso) não precisam ser franqueadas antes de documentadas'],
  peg='Opor o sigilo ao defensor quanto ao que já está documentado.',
  kw=['SV 14', 'já documentados'])
I(P, 1, 'Reprodução simulada',
  'A autoridade policial pode proceder à reprodução simulada dos fatos, desde que esta não contrarie a moralidade ou a ordem pública, e o investigado não está obrigado a dela participar.', 'C',
  'Art. 7º do CPP. Pelo **nemo tenetur se detegere**, o investigado não é obrigado a colaborar ativamente.',
  lei=[(CPP + '7', 'a autoridade policial poderá proceder à reprodução simulada dos fatos', 'a moralidade ou a ordem pública', 'CPP, art. 7º')],
  kw=['reprodução simulada', 'nemo tenetur'])
# --- CPP-2.1 · Rodada 2
I(P, 2, 'Arquivamento — novo art. 28',
  'Ordenado o arquivamento do inquérito, o MP comunicará à vítima, ao investigado e à autoridade policial, e a vítima que não concordar poderá, em 30 dias do recebimento da comunicação, submeter a matéria à revisão da instância competente do órgão ministerial.', 'C',
  'Art. 28, caput e § 1º. O STF (ADI 6.298) acrescentou que o MP **submete a manifestação ao juiz competente**, que pode provocar a revisão ministerial se vir ilegalidade ou teratologia.',
  lei=[(CPP + '28', 'Se a vítima, ou seu representante legal, não concordar com o arquivamento', 'conforme dispuser a respectiva lei orgânica', 'CPP, art. 28, § 1º')],
  juris=[J['ADI6298ARQ']],
  kw=['revisão ministerial', '30 dias'])
I(P, 2, 'Desarquivamento',
  'Arquivado o inquérito por falta de base para a denúncia, a autoridade policial poderá proceder a novas pesquisas se de outras provas tiver notícia, mas a ação penal só poderá ser iniciada com novas provas.', 'C',
  'Art. 18 do CPP e **Súmula 524/STF**. O arquivamento por **atipicidade** ou **extinção da punibilidade** faz coisa julgada material e não admite reabertura.',
  lei=[(CPP + '18', 'a autoridade policial poderá proceder a novas pesquisas, se de outras provas tiver notícia', None, 'CPP, art. 18')],
  juris=[J['STF524']],
  exc=['Arquivamento por atipicidade ou por extinção da punibilidade: coisa julgada material (ressalvada, na jurisprudência, a certidão de óbito falsa)'],
  kw=['novas provas', 'Súmula 524'])
I(P, 2, 'Requerimento de diligências',
  'O ofendido e o indiciado poderão requerer qualquer diligência, que será obrigatoriamente realizada pela autoridade policial.', 'E',
  'Art. 14: a diligência será realizada **ou não, a juízo da autoridade** (discricionariedade). O exame de corpo de delito, porém, não pode ser negado (art. 184).',
  lei=[(CPP + '14', 'O ofendido, ou seu representante legal, e o indiciado poderão requerer qualquer diligência', 'a juízo da autoridade', 'CPP, art. 14')],
  peg='Trocar a discricionariedade por obrigatoriedade.',
  kw=['discricionariedade', 'a juízo da autoridade'])
I(P, 2, 'Defensor do agente de segurança',
  'Quando servidores das instituições do art. 144 da CF figurarem como investigados por fatos relacionados ao uso da força letal no exercício profissional, o indiciado poderá constituir defensor.', 'C',
  'Art. 14-A (Lei 13.964/2019): **citação** do investigado para constituir defensor em 48 horas; não o fazendo, a instituição é intimada a indicar defensor.',
  lei=[(CPP + '14-A', 'Nos casos em que servidores vinculados às instituições dispostas no art. 144 da Constituição Federal', 'o indiciado poderá constituir defensor', 'CPP, art. 14-A, caput')],
  kw=['força letal', 'constituir defensor'])
I(P, 2, 'Devolução do inquérito',
  'O Ministério Público pode requerer a devolução do inquérito à autoridade policial para quaisquer diligências que entender úteis.', 'E',
  'Art. 16: só para **novas diligências imprescindíveis** ao oferecimento da denúncia.',
  lei=[(CPP + '16', 'O Ministério Público não poderá requerer a devolução do inquérito à autoridade policial', 'imprescindíveis ao oferecimento da denúncia', 'CPP, art. 16')],
  peg='Ampliar para "quaisquer diligências úteis".',
  kw=['imprescindíveis', 'devolução'])
I(P, 2, 'Participação do MP na investigação',
  'A participação de membro do Ministério Público na fase investigatória criminal acarreta o seu impedimento para o oferecimento da denúncia.', 'E',
  '**Súmula 234/STJ**: **não** acarreta impedimento nem suspeição.',
  juris=[J['S234']],
  peg='Inverter a Súmula 234.',
  kw=['Súmula 234', 'impedimento'])
I(P, 2, 'Identificação criminal',
  'O civilmente identificado não será submetido a identificação criminal, salvo nas hipóteses previstas em lei.', 'C',
  'CF, art. 5º, LVIII; hipóteses na Lei 12.037/2009, art. 3º (ex.: documento rasurado, essencial às investigações por decisão judicial). A Súmula 568/STF é anterior à CF e ficou superada pela garantia constitucional.',
  lei=[(CF + '5', 'o civilmente identificado não será submetido a identificação criminal, salvo nas hipóteses previstas em lei', None, 'CF, art. 5º, LVIII')],
  kw=['identificação criminal', 'civilmente identificado'])
I(P, 2, 'Incomunicabilidade',
  'A incomunicabilidade do indiciado, prevista no art. 21 do CPP, por até três dias, é amplamente aplicada após a Constituição de 1988, inclusive em relação ao advogado.', 'E',
  'Prevalece que o **art. 21 não foi recepcionado**: a CF veda a incomunicabilidade até no estado de defesa (art. 136, § 3º, IV), e o preso tem direito à assistência de advogado (art. 5º, LXIII).',
  lei=[(CF + '136', 'é vedada a incomunicabilidade do preso', None, 'CF, art. 136, § 3º, IV')],
  peg='Apresentar como vigente dispositivo tido por não recepcionado.',
  kw=['incomunicabilidade', 'não recepcionado'])

# ======================= CPP-2.2 · Jurisdição, competência, conexão, continência, prevenção, incidentes =======================
P = 'DBA26-CPP-2.2'
I(P, 1, 'Lugar da infração',
  'A competência será, de regra, determinada pelo lugar em que se consumar a infração, ou, no caso de tentativa, pelo lugar em que for praticado o último ato de execução.', 'C',
  'Art. 70 do CPP: **teoria do resultado** como regra.',
  lei=[(CPP + '70', 'A competência será, de regra, determinada pelo lugar em que se consumar a infração', 'último ato de execução', 'CPP, art. 70, caput')],
  kw=['lugar da consumação', 'teoria do resultado'])
I(P, 1, 'Estelionato e domicílio da vítima',
  'No estelionato praticado mediante depósito, emissão de cheque sem fundos ou transferência de valores, a competência é sempre a do local da agência bancária do agente.', 'E',
  'Art. 70, § 4º (Lei 14.155/2021): **domicílio da vítima**; havendo pluralidade de vítimas, **prevenção**.',
  lei=[(CPP + '70', 'a competência será definida pelo local do domicílio da vítima', 'firmar-se-á pela prevenção', 'CPP, art. 70, § 4º')],
  peg='Repetir o entendimento anterior à Lei 14.155/2021.',
  kw=['domicílio da vítima', 'estelionato'])
I(P, 1, 'Lugar desconhecido',
  'Não sendo conhecido o lugar da infração, a competência regular-se-á pelo domicílio ou residência da vítima.', 'E',
  'Art. 72: **domicílio ou residência do réu** (foro supletivo). Domicílio da vítima é regra especial do estelionato (art. 70, § 4º).',
  lei=[(CPP + '72', 'Não sendo conhecido o lugar da infração', 'domicílio ou residência do réu', 'CPP, art. 72, caput')],
  peg='Trocar réu por vítima.',
  kw=['domicílio do réu', 'foro supletivo'])
I(P, 1, 'Crime permanente em várias comarcas',
  'Tratando-se de infração permanente praticada em território de duas ou mais jurisdições, a competência firmar-se-á pelo lugar onde cessou a permanência.', 'E',
  'Art. 71 do CPP: firma-se pela **prevenção**.',
  lei=[(CPP + '71', 'Tratando-se de infração continuada ou permanente', 'firmar-se-á pela prevenção', 'CPP, art. 71')],
  peg='Trocar a prevenção por critério inexistente.',
  kw=['prevenção', 'infração permanente'])
I(P, 1, 'Conexão intersubjetiva',
  'Há conexão quando, ocorrendo duas ou mais infrações, houverem sido praticadas ao mesmo tempo por várias pessoas reunidas, ou por várias pessoas em concurso, ainda que diverso o tempo e o lugar, ou por várias pessoas, umas contra as outras.', 'C',
  'Art. 76, I: conexão **intersubjetiva** por simultaneidade, por concurso e por reciprocidade.',
  lei=[(CPP + '76', 'se, ocorrendo duas ou mais infrações, houverem sido praticadas, ao mesmo tempo, por várias pessoas reunidas', 'umas contra as outras', 'CPP, art. 76, I')],
  kw=['conexão intersubjetiva', 'reciprocidade'])
I(P, 1, 'Continência',
  'A continência ocorre quando duas ou mais infrações são praticadas para facilitar ou ocultar as outras.', 'E',
  'Isso é **conexão objetiva** (teleológica ou consequencial, art. 76, II). **Continência** é quando duas ou mais pessoas são acusadas pela **mesma infração** ou nos casos de concurso formal, erro na execução e resultado diverso (art. 77).',
  lei=[(CPP + '77', 'duas ou mais pessoas forem acusadas pela mesma infração', None, 'CPP, art. 77, I')],
  peg='Trocar conexão teleológica por continência.',
  kw=['continência', 'mesma infração'])
I(P, 1, 'Júri e jurisdição comum',
  'No concurso entre a competência do júri e a de outro órgão da jurisdição comum, prevalecerá a competência do juízo comum, se a ele for cominada pena mais grave.', 'E',
  'Art. 78, I: prevalece o **júri** — ressalvados, desde a Lei 15.358/2026, os homicídios cometidos por membros de organizações criminosas ultraviolentas, grupo paramilitar ou milícia privada.',
  lei=[(CPP + '78', 'no concurso entre a competência do júri e a de outro órgão da jurisdição comum, prevalecerá a competência do júri', 'milícia privada, ou sua tentativa', 'CPP, art. 78, I')],
  exc=['Homicídio (ou tentativa) por membro de organização criminosa ultraviolenta, grupo paramilitar ou milícia privada (art. 78, I, parte final, Lei 15.358/2026)'],
  peg='Aplicar ao júri o critério da pena mais grave, que vale entre órgãos da jurisdição comum de mesma categoria (art. 78, II).',
  kw=['prevalecerá a competência do júri', 'Lei 15.358/2026'])
I(P, 1, 'Separação obrigatória',
  'A conexão e a continência importam unidade de processo e julgamento, salvo no concurso entre a jurisdição comum e a militar e entre a jurisdição comum e a do juízo de menores.', 'C',
  'Art. 79, I e II: **separação obrigatória**.',
  lei=[(CPP + '79', 'A conexão e a continência importarão unidade de processo e julgamento, salvo:', 'jurisdição comum e a do juízo de menores', 'CPP, art. 79, caput, I e II')],
  kw=['separação obrigatória', 'jurisdição militar'])
I(P, 1, 'Crimes conexos federal e estadual',
  'Havendo conexão entre crime de competência federal e crime de competência estadual, cada um será julgado pela respectiva Justiça, pois não há prevalência entre elas.', 'E',
  '**Súmula 122/STJ**: compete à **Justiça Federal** o julgamento **unificado** dos crimes conexos federal e estadual.',
  juris=[J['S122']],
  peg='Separar os processos onde a súmula manda unificar na Justiça Federal.',
  kw=['Súmula 122', 'Justiça Federal'])
I(P, 1, 'Contravenção e União',
  'A contravenção penal praticada em detrimento de bens, serviços ou interesse da União é de competência da Justiça Federal.', 'E',
  'A CF exclui as **contravenções** da Justiça Federal (art. 109, IV). **Súmula 38/STJ**: Justiça **Estadual**.',
  lei=[(CF + '109', 'os crimes políticos e as infrações penais praticadas em detrimento de bens, serviços ou interesse da União', 'ressalvada a competência da Justiça Militar e da Justiça Eleitoral', 'CF, art. 109, IV')],
  juris=[J['S38']],
  peg='Esquecer que o art. 109, IV, exclui as contravenções.',
  kw=['contravenções', 'Súmula 38'])
I(P, 1, 'Questão prejudicial obrigatória',
  'Se a existência da infração depender de controvérsia séria e fundada sobre o estado civil das pessoas, o curso da ação penal ficará suspenso até que a controvérsia seja dirimida no juízo cível por sentença transitada em julgado.', 'C',
  'Art. 92: **prejudicial obrigatória** (estado civil), sem prejuízo da inquirição de testemunhas e provas urgentes. A do art. 93 (outras questões) é **facultativa**.',
  lei=[(CPP + '92', 'sobre o estado civil das pessoas, o curso da ação penal ficará suspenso', 'sentença passada em julgado', 'CPP, art. 92, caput')],
  kw=['questão prejudicial', 'estado civil'])
# --- CPP-2.2 · Rodada 2
I(P, 2, 'Prevenção',
  'A prevenção só se firma por ato praticado após o oferecimento da denúncia, pois antes dela não há processo.', 'E',
  'Art. 83: a **prevenção** pode decorrer de medida **anterior ao oferecimento da denúncia** (ex.: decretação de preventiva, busca).',
  lei=[(CPP + '83', 'Verificar-se-á a competência por prevenção toda vez que', 'anterior ao oferecimento da denúncia ou da queixa', 'CPP, art. 83')],
  peg='Negar a prevenção por medida da fase investigatória.',
  kw=['prevenção', 'medida anterior à denúncia'])
I(P, 2, 'Foro por prerrogativa e corréu',
  'A atração do processo do corréu ao foro por prerrogativa de função de um dos denunciados, por conexão ou continência, viola a garantia do juiz natural.', 'E',
  '**Súmula 704/STF**: **não viola** juiz natural, ampla defesa nem devido processo legal. O tribunal pode, porém, desmembrar.',
  juris=[J['STF704']],
  peg='Inverter a Súmula 704.',
  kw=['Súmula 704', 'corréu'])
I(P, 2, 'Prefeito e Justiça Federal',
  'Compete à Justiça Federal processar e julgar prefeito municipal por desvio de verba sujeita a prestação de contas perante órgão federal; se a verba foi transferida e incorporada ao patrimônio municipal, a competência é da Justiça Estadual.', 'C',
  '**Súmulas 208 e 209/STJ**. E a **Súmula 702/STF**: o TJ julga prefeitos nos crimes da Justiça comum estadual; nos demais, o tribunal de segundo grau respectivo (TRF, TRE).',
  juris=[J['S208'], J['S209'], J['STF702']],
  kw=['prefeito', 'verba incorporada'])
I(P, 2, 'Indígena',
  'Crime em que o indígena figure como autor ou vítima é sempre de competência da Justiça Federal.', 'E',
  '**Súmula 140/STJ**: regra é a **Justiça Estadual**. A Federal só atua quando houver **disputa sobre direitos indígenas** (CF, art. 109, XI).',
  lei=[(CF + '109', 'a disputa sobre direitos indígenas', None, 'CF, art. 109, XI')],
  juris=[J['S140']],
  peg='Federalizar todo crime que envolva indígena.',
  kw=['Súmula 140', 'direitos indígenas'])
I(P, 2, 'Documento falso',
  'A competência para o crime de uso de documento falso é firmada pelo órgão expedidor do documento, e não pela entidade a que ele foi apresentado.', 'E',
  '**Súmula 546/STJ**: importa a **entidade ou órgão a que foi apresentado**, não o órgão expedidor.',
  juris=[J['S546']],
  peg='Trocar "a quem foi apresentado" por "quem expediu".',
  kw=['Súmula 546', 'documento falso'])
I(P, 2, 'Exceções e autoridade policial',
  'Não se pode opor suspeição às autoridades policiais nos atos do inquérito, mas elas deverão declarar-se suspeitas quando ocorrer motivo legal.', 'C',
  'Art. 107 do CPP: não há **exceção de suspeição** contra o delegado; há dever de **autodeclaração**.',
  lei=[(CPP + '107', 'Não se poderá opor suspeição às autoridades policiais nos atos do inquérito', 'quando ocorrer motivo legal', 'CPP, art. 107')],
  kw=['suspeição', 'autoridade policial'])
I(P, 2, 'Restituição de coisas apreendidas',
  'A restituição das coisas apreendidas é ato privativo do juiz, vedada à autoridade policial em qualquer caso.', 'E',
  'Art. 120: a restituição pode ser ordenada pela **autoridade policial** ou pelo juiz, desde que **não haja dúvida** quanto ao direito do reclamante.',
  lei=[(CPP + '120', 'A restituição, quando cabível, poderá ser ordenada pela autoridade policial ou juiz', 'direito do reclamante', 'CPP, art. 120, caput')],
  peg='Negar ao delegado a restituição sem dúvida.',
  kw=['restituição', 'autoridade policial'])
I(P, 2, 'Insanidade na fase de inquérito',
  'O exame de insanidade mental pode ser ordenado ainda na fase do inquérito, diretamente pela autoridade policial, sem intervenção judicial.', 'E',
  'Art. 149, § 1º: na fase do inquérito, mediante **representação da autoridade policial ao juiz**. Quem ordena é o juiz.',
  lei=[(CPP + '149', 'O exame poderá ser ordenado ainda na fase do inquérito, mediante representação da autoridade policial ao juiz competente', None, 'CPP, art. 149, § 1º')],
  peg='Dar ao delegado a decisão que é do juiz.',
  kw=['incidente de insanidade', 'representação'])

# ======================= CPP-3 · Processo criminal: finalidade, pressupostos e sistemas =======================
P = 'DBA26-CPP-3'
I(P, 1, 'Rejeição da denúncia',
  'A denúncia ou queixa será rejeitada quando for manifestamente inepta, faltar pressuposto processual ou condição para o exercício da ação penal, ou faltar justa causa.', 'C',
  'Art. 395: **pressupostos processuais**, **condições da ação** e **justa causa** são filtros de admissibilidade.',
  lei=[(CPP + '395', 'A denúncia ou queixa será rejeitada quando:', 'faltar justa causa para o exercício da ação penal', 'CPP, art. 395')],
  kw=['pressuposto processual', 'justa causa'])
I(P, 1, 'Pressupostos de existência',
  'São tradicionalmente apontados como pressupostos de existência do processo a demanda veiculada por quem tenha capacidade postulatória, um órgão investido de jurisdição e as partes.', 'C',
  'Pressupostos de **existência**: demanda, jurisdição e partes. De **validade**: competência e imparcialidade do juiz, capacidade das partes, citação válida, ausência de litispendência e coisa julgada. Base legal das exceções: art. 95 do CPP.',
  lei=[(CPP + '95', 'Poderão ser opostas as exceções de:', None, 'CPP, art. 95, caput')],
  kw=['pressupostos de existência', 'jurisdição'])
I(P, 1, 'Litispendência e coisa julgada',
  'A litispendência e a coisa julgada não podem ser arguidas por exceção no processo penal, só por habeas corpus.', 'E',
  'Art. 95: cabem exceções de **suspeição, incompetência, litispendência, ilegitimidade de parte e coisa julgada** (pressupostos processuais negativos).',
  lei=[(CPP + '95', 'Poderão ser opostas as exceções de:', 'coisa julgada', 'CPP, art. 95')],
  peg='Negar a via da exceção.',
  kw=['litispendência', 'exceção'])
I(P, 1, 'Finalidade do processo',
  'O processo penal tem finalidade exclusivamente punitiva, servindo apenas à aplicação da pena ao culpado.', 'E',
  'O processo tem dupla função: instrumento de **aplicação do direito penal** e **garantia** do acusado contra o arbítrio (devido processo legal, CF, art. 5º, LIV). Pode terminar em absolvição.',
  lei=[(CF + '5', 'ninguém será privado da liberdade ou de seus bens sem o devido processo legal', None, 'CF, art. 5º, LIV')],
  peg='Reduzir o processo à função punitiva.',
  kw=['instrumentalidade garantista', 'devido processo legal'])
I(P, 1, 'Nulidade e prejuízo',
  'Nenhum ato será declarado nulo se da nulidade não resultar prejuízo para a acusação ou para a defesa.', 'C',
  'Art. 563: **pas de nullité sans grief**.',
  lei=[(CPP + '563', 'Nenhum ato será declarado nulo, se da nulidade não resultar prejuízo para a acusação ou para a defesa', None, 'CPP, art. 563')],
  kw=['pas de nullité sans grief', 'prejuízo'])
# --- CPP-3 · Rodada 2
I(P, 2, 'Nulidade provocada',
  'A parte pode arguir nulidade a que tenha dado causa, desde que demonstre o prejuízo.', 'E',
  'Art. 565: nenhuma das partes pode arguir nulidade **a que haja dado causa** ou para que tenha concorrido (vedação ao comportamento contraditório).',
  lei=[(CPP + '565', 'Nenhuma das partes poderá', 'a que haja dado causa', 'CPP, art. 565')],
  peg='Admitir que a parte se beneficie da própria torpeza.',
  kw=['nulidade provocada', 'a que haja dado causa'])
I(P, 2, 'Incompetência reconhecida de ofício',
  'Em qualquer fase do processo, o juiz que reconhecer motivo que o torne incompetente o declarará nos autos, haja ou não alegação da parte.', 'C',
  'Art. 109 do CPP. Prevalece que a incompetência **territorial** é relativa e preclui se não arguida no momento oportuno.',
  lei=[(CPP + '109', 'Se em qualquer fase do processo o juiz reconhecer motivo que o torne incompetente', 'haja ou não alegação da parte', 'CPP, art. 109')],
  kw=['incompetência', 'de ofício'])
I(P, 2, 'Nulidade não arguida pela acusação',
  'O tribunal pode acolher, contra o réu, nulidade não arguida no recurso da acusação, por se tratar de matéria de ordem pública.', 'E',
  '**Súmula 160/STF**: é **nula** a decisão que acolhe contra o réu nulidade não arguida no recurso da acusação, ressalvados os casos de recurso de ofício.',
  juris=[J['STF160']],
  peg='Invocar "ordem pública" contra o réu.',
  kw=['Súmula 160', 'reformatio in pejus'])
I(P, 2, 'Empate em órgão colegiado',
  'Em julgamento de matéria penal ou processual penal em órgão colegiado, havendo empate, prevalecerá a decisão mais favorável ao indivíduo imputado.', 'C',
  'Art. 615, § 1º (Lei 14.836/2024): **empate favorece o imputado**, proclamando-se de imediato o resultado.',
  lei=[(CPP + '615', 'havendo empate, prevalecerá a decisão mais favorável ao indivíduo imputado', None, 'CPP, art. 615, § 1º')],
  kw=['empate', 'mais favorável'])
