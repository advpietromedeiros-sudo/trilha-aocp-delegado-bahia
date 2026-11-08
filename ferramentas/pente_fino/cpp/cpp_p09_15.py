# Pente Fino de Direito Processual Penal — CPP-9 (sentença), 9.1 (juiz, MP, defensor, assistentes, auxiliares), 9.2
# (citação, intimação, interdição de direito), 9.3 (efeitos, coisa julgada, HC, MS criminal), CPP-10 (processo dos crimes
# comuns), 11 (medidas assecuratórias), 12 (prisão domiciliar), 13 (outras cautelares), 14 (procedimento comum),
# 15 (impugnações e ações autônomas) e 15-B2 (jurisprudência aplicada dos tribunais superiores) (08/11/2026).
from base import I
from cpp_juris import J

CPP = 'CPP:'
CF = 'CF:'
JE = 'L9099:'

# ======================= CPP-9 · Sentença criminal =======================
P = 'DBA26-CPP-9'
I(P, 1, 'Emendatio libelli',
  'O juiz, sem modificar a descrição do fato contida na denúncia ou queixa, poderá atribuir-lhe definição jurídica diversa, ainda que, em consequência, tenha de aplicar pena mais grave.', 'C',
  'Art. 383: **emendatio libelli** — o réu se defende dos **fatos**, não da capitulação.',
  lei=[(CPP + '383', 'O juiz, sem modificar a descrição do fato contida na denúncia ou queixa', 'definição jurídica diversa', 'CPP, art. 383, caput')],
  kw=['emendatio libelli', 'definição jurídica diversa'])
I(P, 1, 'Mutatio libelli',
  'Encerrada a instrução, se entender cabível nova definição jurídica do fato por prova de elemento ou circunstância não contida na acusação, o próprio juiz poderá condenar o réu pela nova definição, independentemente de aditamento.', 'E',
  'Art. 384: na **mutatio libelli**, o **MP deve aditar** a denúncia em 5 dias; o juiz não pode condenar por fato não imputado (correlação).',
  lei=[(CPP + '384', 'Encerrada a instrução probatória, se entender cabível nova definição jurídica do fato', 'o Ministério Público deverá aditar a denúncia ou queixa', 'CPP, art. 384, caput')],
  peg='Dispensar o aditamento na mutatio.',
  kw=['mutatio libelli', 'aditamento'])
I(P, 1, 'Condenação contra o pedido do MP',
  'Nos crimes de ação pública, o juiz não pode proferir sentença condenatória se o Ministério Público tiver opinado pela absolvição.', 'E',
  'Art. 385: o juiz **poderá** condenar ainda que o MP opine pela absolvição e reconhecer agravantes não alegadas (dispositivo criticado pela doutrina acusatória, mas vigente).',
  lei=[(CPP + '385', 'Nos crimes de ação pública, o juiz poderá proferir sentença condenatória, ainda que o Ministério Público tenha opinado pela absolvição', None, 'CPP, art. 385')],
  peg='Vincular o juiz ao pedido de absolvição.',
  kw=['art. 385', 'absolvição'])
I(P, 1, 'Valor mínimo de reparação',
  'O juiz, ao proferir sentença condenatória, fixará valor mínimo para reparação dos danos causados pela infração, considerando os prejuízos sofridos pelo ofendido.', 'C',
  'Art. 387, IV. A jurisprudência exige pedido expresso e contraditório sobre o valor.',
  lei=[(CPP + '387', 'fixará valor mínimo para reparação dos danos causados pela infração', None, 'CPP, art. 387, IV')],
  kw=['valor mínimo', 'reparação dos danos'])
I(P, 1, 'Requisitos da sentença',
  'A sentença conterá, entre outros, a exposição sucinta da acusação e da defesa, a indicação dos motivos de fato e de direito em que se fundar e o dispositivo.', 'C',
  'Art. 381: relatório, fundamentação e dispositivo. (Na Lei 9.099/1995, o relatório é dispensado — art. 81, § 3º.)',
  lei=[(CPP + '381', 'a exposição sucinta da acusação e da defesa', None, 'CPP, art. 381, II')],
  kw=['relatório', 'fundamentação'])
# --- CPP-9 · Rodada 2
I(P, 2, 'Detração e regime',
  'O tempo de prisão provisória, de prisão administrativa ou de internação, no Brasil ou no estrangeiro, será computado para fins de determinação do regime inicial de pena privativa de liberdade.', 'C',
  'Art. 387, § 2º (Lei 12.736/2012): **detração** já na sentença.',
  lei=[(CPP + '387', 'O tempo de prisão provisória, de prisão administrativa ou de internação', 'regime inicial de pena privativa de liberdade', 'CPP, art. 387, § 2º')],
  kw=['detração', 'regime inicial'])
I(P, 2, 'Mutatio em segunda instância',
  'O tribunal pode, em apelação, aplicar a mutatio libelli, dando nova definição jurídica ao fato por circunstância elementar não contida na denúncia.', 'E',
  '**Súmula 453/STF**: não se aplica o art. 384 na **segunda instância** (supressão de instância e violação da correlação).',
  juris=[J['STF453']],
  peg='Levar a mutatio ao tribunal.',
  kw=['Súmula 453', 'segunda instância'])
I(P, 2, 'Embargos de declaração da sentença',
  'Qualquer das partes poderá, no prazo de 5 dias, pedir ao juiz que declare a sentença em caso de obscuridade, ambiguidade, contradição ou omissão.', 'E',
  'Art. 382: prazo de **2 dias** (os "embarguinhos").',
  lei=[(CPP + '382', 'Qualquer das partes poderá, no prazo de 2 (dois) dias, pedir ao juiz que declare a sentença', None, 'CPP, art. 382')],
  peg='Trocar 2 por 5 dias.',
  kw=['embarguinhos', '2 dias'])

# ======================= CPP-9.1 · Juiz, MP, acusado e defensor, assistentes e auxiliares =======================
P = 'DBA26-CPP-9.1'
I(P, 1, 'Poder de polícia do juiz',
  'Ao juiz incumbirá prover à regularidade do processo e manter a ordem no curso dos respectivos atos, podendo, para tal fim, requisitar a força pública.', 'C',
  'Art. 251 do CPP.',
  lei=[(CPP + '251', 'Ao juiz incumbirá prover à regularidade do processo e manter a ordem no curso dos respectivos atos', 'requisitar a força pública', 'CPP, art. 251')],
  kw=['regularidade do processo', 'força pública'])
I(P, 1, 'Juiz de outra instância',
  'O juiz pode exercer jurisdição no processo em que tiver funcionado como juiz de outra instância, pronunciando-se de fato ou de direito sobre a questão, desde que em órgão colegiado.', 'E',
  'Art. 252, III: é caso de **impedimento**.',
  lei=[(CPP + '252', 'tiver funcionado como juiz de outra instância, pronunciando-se, de fato ou de direito, sobre a questão', None, 'CPP, art. 252, III')],
  peg='Criar exceção ao impedimento.',
  kw=['impedimento', 'outra instância'])
I(P, 1, 'Defensor nomeado',
  'Se o acusado não tiver defensor, ser-lhe-á nomeado defensor pelo juiz, ressalvado o seu direito de, a todo tempo, nomear outro de sua confiança, ou a si mesmo defender-se, caso tenha habilitação.', 'C',
  'Art. 263 do CPP.',
  lei=[(CPP + '263', 'Se o acusado não o tiver, ser-lhe-á nomeado defensor pelo juiz', 'caso tenha habilitação', 'CPP, art. 263, caput')],
  kw=['defensor nomeado', 'de sua confiança'])
I(P, 1, 'Defensor público ou dativo',
  'A defesa técnica, quando realizada por defensor público ou dativo, pode ser exercida por manifestação genérica, sem fundamentação.', 'E',
  'Art. 261, par. ún.: será **sempre** exercida por **manifestação fundamentada**.',
  lei=[(CPP + '261', 'A defesa técnica, quando realizada por defensor público ou dativo, será sempre exercida através de manifestação fundamentada', None, 'CPP, art. 261, par. ún.')],
  peg='Admitir defesa meramente formal.',
  kw=['manifestação fundamentada', 'defensor dativo'])
I(P, 1, 'Poderes do assistente',
  'Ao assistente será permitido propor meios de prova, requerer perguntas às testemunhas, participar do debate oral e arrazoar os recursos interpostos pelo MP ou por ele próprio.', 'C',
  'Art. 271 do CPP.',
  lei=[(CPP + '271', 'Ao assistente será permitido propor meios de prova', 'arrazoar os recursos interpostos pelo Ministério Público', 'CPP, art. 271, caput')],
  kw=['assistente', 'propor meios de prova'])
# --- CPP-9.1 · Rodada 2
I(P, 2, 'Renúncia do único defensor',
  'Após a renúncia do único defensor, o tribunal pode julgar a apelação sem intimar o réu para constituir outro, nomeando defensor dativo.', 'E',
  '**Súmula 708/STF**: é **nulo** o julgamento se o réu não foi previamente intimado para constituir outro defensor.',
  juris=[J['STF708']],
  peg='Suprir a intimação pela nomeação de dativo.',
  kw=['Súmula 708', 'renúncia do defensor'])
I(P, 2, 'Abandono e novo defensor',
  'Em caso de abandono do processo pelo defensor, o acusado será intimado para constituir novo defensor, se quiser, e, não localizado, será nomeado defensor público ou dativo.', 'C',
  'Art. 265, § 3º (Lei 14.752/2023).',
  lei=[(CPP + '265', 'Em caso de abandono do processo pelo defensor, o acusado será intimado para constituir novo defensor', 'advogado dativo para a sua defesa', 'CPP, art. 265, § 3º')],
  kw=['abandono', 'novo defensor'])
I(P, 2, 'Admissão do assistente',
  'O assistente pode ser admitido mesmo após o trânsito em julgado da sentença, para promover a execução do valor mínimo de reparação.', 'E',
  'Art. 269: o assistente é admitido **enquanto não passar em julgado** a sentença, recebendo a causa no estado em que se achar.',
  lei=[(CPP + '269', 'O assistente será admitido enquanto não passar em julgado a sentença', 'no estado em que se achar', 'CPP, art. 269')],
  peg='Admitir assistente depois do trânsito.',
  kw=['assistente', 'trânsito em julgado'])

# ======================= CPP-9.2 · Citação, intimação, interdição de direito =======================
P = 'DBA26-CPP-9.2'
I(P, 1, 'Réu preso',
  'Se o réu estiver preso, será pessoalmente citado.', 'C',
  'Art. 360. É **nula** a citação por edital de réu preso na mesma unidade da Federação (**Súmula 351/STF**).',
  lei=[(CPP + '360', 'Se o réu estiver preso, será pessoalmente citado', None, 'CPP, art. 360')],
  juris=[J['STF351']],
  kw=['citação pessoal', 'réu preso'])
I(P, 1, 'Edital',
  'Se o réu não for encontrado, será citado por edital, com o prazo de 30 dias.', 'E',
  'Art. 361: edital com prazo de **15 dias**.',
  lei=[(CPP + '361', 'Se o réu não for encontrado, será citado por edital, com o prazo de 15 (quinze) dias', None, 'CPP, art. 361')],
  peg='Trocar 15 por 30 dias.',
  kw=['edital', '15 dias'])
I(P, 1, 'Hora certa',
  'Verificando que o réu se oculta para não ser citado, o oficial de justiça certificará a ocorrência e procederá à citação com hora certa.', 'C',
  'Art. 362. Completada a citação com hora certa, se o acusado não comparecer, nomeia-se defensor dativo (par. ún.) — **não** há suspensão do art. 366.',
  lei=[(CPP + '362', 'Verificando que o réu se oculta para não ser citado, o oficial de justiça certificará a ocorrência e procederá à citação com hora certa', None, 'CPP, art. 362, caput')],
  kw=['hora certa', 'oculta'])
I(P, 1, 'Suspensão do art. 366',
  'Se o acusado, citado por edital, não comparecer nem constituir advogado, ficarão suspensos o processo e o curso do prazo prescricional.', 'C',
  'Art. 366. O período de suspensão da prescrição regula-se pelo **máximo da pena cominada** (**Súmula 415/STJ**).',
  lei=[(CPP + '366', 'Se o acusado, citado por edital, não comparecer, nem constituir advogado, ficarão suspensos o processo e o curso do prazo prescricional', None, 'CPP, art. 366')],
  juris=[J['S415']],
  kw=['art. 366', 'Súmula 415'])
I(P, 1, 'Revelia',
  'O processo seguirá sem a presença do acusado que, citado ou intimado pessoalmente para qualquer ato, deixar de comparecer sem motivo justificado, ou que, mudando de residência, não comunicar o novo endereço ao juízo.', 'C',
  'Art. 367: **revelia** no processo penal (não gera presunção de veracidade).',
  lei=[(CPP + '367', 'O processo seguirá sem a presença do acusado que, citado ou intimado pessoalmente para qualquer ato', 'não comunicar o novo endereço ao juízo', 'CPP, art. 367')],
  kw=['revelia', 'novo endereço'])
# --- CPP-9.2 · Rodada 2
I(P, 2, 'Réu no estrangeiro',
  'Estando o acusado no estrangeiro, em lugar sabido, será citado por edital, suspendendo-se o processo.', 'E',
  'Art. 368: citação por **carta rogatória**, suspendendo-se o curso da **prescrição** até o seu cumprimento.',
  lei=[(CPP + '368', 'Estando o acusado no estrangeiro, em lugar sabido, será citado mediante carta rogatória', 'até o seu cumprimento', 'CPP, art. 368')],
  peg='Trocar rogatória por edital.',
  kw=['carta rogatória', 'prescrição'])
I(P, 2, 'Edital sem transcrição',
  'É nula a citação por edital que indica o dispositivo da lei penal, mas não transcreve a denúncia nem resume os fatos.', 'E',
  '**Súmula 366/STF**: **não é nula**.',
  juris=[J['STF366']],
  peg='Inverter a Súmula 366.',
  kw=['Súmula 366', 'citação por edital'])
I(P, 2, 'Interdição provisória de direitos',
  'A aplicação provisória de interdições de direitos poderá ser determinada pelo juiz, de ofício ou a requerimento das partes ou do ofendido, entre outras ocasiões, na sentença condenatória recorrível.', 'C',
  'Art. 373, IV (arts. 373 a 380). Também durante a instrução, após a defesa, e na pronúncia.',
  lei=[(CPP + '373', 'A aplicação provisória de interdições de direitos poderá ser determinada pelo juiz', None, 'CPP, art. 373, caput'),
       (CPP + '373', 'na sentença condenatória recorrível', None, 'CPP, art. 373, IV')],
  kw=['interdição de direitos', 'aplicação provisória'])

# ======================= CPP-9.3 · Efeitos, coisa julgada, HC e MS em matéria criminal =======================
P = 'DBA26-CPP-9.3'
I(P, 1, 'Cabimento do habeas corpus',
  'Dar-se-á habeas corpus sempre que alguém sofrer ou se achar na iminência de sofrer violência ou coação ilegal na sua liberdade de ir e vir, inclusive nos casos de punição disciplinar.', 'E',
  'Art. 647: **salvo** nos casos de punição disciplinar (e CF, art. 142, § 2º, para militares). A jurisprudência admite HC para exame da **legalidade** formal da punição.',
  lei=[(CPP + '647', 'Dar-se-á habeas corpus sempre que alguém sofrer ou se achar na iminência de sofrer violência ou coação ilegal', 'salvo nos casos de punição disciplinar', 'CPP, art. 647')],
  peg='Retirar a ressalva da punição disciplinar.',
  kw=['habeas corpus', 'punição disciplinar'])
I(P, 1, 'Legitimidade para o HC',
  'O habeas corpus só pode ser impetrado por advogado, em favor do paciente, vedada a impetração pelo Ministério Público.', 'E',
  'Art. 654: **qualquer pessoa**, em seu favor ou de outrem, **e o MP** podem impetrar; dispensa advogado.',
  lei=[(CPP + '654', 'O habeas corpus poderá ser impetrado por qualquer pessoa, em seu favor ou de outrem, bem como pelo Ministério Público', None, 'CPP, art. 654, caput')],
  peg='Exigir capacidade postulatória.',
  kw=['qualquer pessoa', 'impetrado'])
I(P, 1, 'HC e multa',
  'Cabe habeas corpus contra decisão condenatória exclusivamente a pena de multa.', 'E',
  '**Súmula 693/STF**: não cabe (não há risco à liberdade de locomoção). Nem quando já extinta a pena privativa (**Súmula 695/STF**).',
  juris=[J['STF693'], J['STF695']],
  peg='Admitir HC sem risco à liberdade.',
  kw=['Súmula 693', 'pena de multa'])
I(P, 1, 'Coação ilegal',
  'A coação considerar-se-á ilegal, entre outras hipóteses, quando não houver justa causa e quando alguém estiver preso por mais tempo do que determina a lei.', 'C',
  'Art. 648, I e II.',
  lei=[(CPP + '648', 'quando não houver justa causa', None, 'CPP, art. 648, I'),
       (CPP + '648', 'quando alguém estiver preso por mais tempo do que determina a lei', None, 'CPP, art. 648, II')],
  kw=['coação ilegal', 'justa causa'])
I(P, 1, 'MS e efeito suspensivo',
  'O mandado de segurança é via adequada para atribuir efeito suspensivo a recurso criminal interposto pelo Ministério Público.', 'E',
  '**Súmula 604/STJ**: **não se presta**. Em MS do MP contra decisão em processo penal, o réu é **litisconsorte passivo** obrigatório (**Súmula 701/STF**).',
  juris=[J['S604'], J['STF701']],
  peg='Usar o MS como atalho para efeito suspensivo.',
  kw=['Súmula 604', 'mandado de segurança'])
# --- CPP-9.3 · Rodada 2
I(P, 2, 'HC de ofício',
  'Qualquer autoridade judicial, no âmbito de sua competência, poderá expedir de ofício ordem de habeas corpus, individual ou coletivo, quando verificar coação ilegal no curso de processo, ainda que não conhecidos a ação ou o recurso.', 'C',
  'Art. 647-A e par. ún. (Lei 14.836/2024): **HC de ofício**, inclusive **coletivo**.',
  lei=[(CPP + '647-A', 'qualquer autoridade judicial poderá expedir de ofício ordem de habeas corpus, individual ou coletivo', None, 'CPP, art. 647-A, caput')],
  kw=['HC de ofício', 'coletivo'])
I(P, 2, 'Liminar indeferida em tribunal superior',
  'Compete ao STF conhecer de habeas corpus impetrado contra decisão de relator que, em HC requerido a tribunal superior, indefere a liminar.', 'E',
  '**Súmula 691/STF**: **não compete** (supressão de instância), salvo flagrante ilegalidade, segundo a própria Corte.',
  juris=[J['STF691']],
  peg='Inverter a Súmula 691.',
  kw=['Súmula 691', 'supressão de instância'])
I(P, 2, 'Exceção de coisa julgada',
  'A exceção de coisa julgada somente poderá ser oposta em relação ao fato principal que tiver sido objeto da sentença.', 'C',
  'Art. 110, § 2º, do CPP.',
  lei=[(CPP + '110', 'A exceção de coisa julgada somente poderá ser oposta em relação ao fato principal', None, 'CPP, art. 110, § 2º')],
  kw=['coisa julgada', 'fato principal'])
I(P, 2, 'Renúncia à apelação',
  'A renúncia do réu ao direito de apelar, manifestada sem a assistência do defensor, impede o conhecimento da apelação interposta por este.', 'E',
  '**Súmula 705/STF**: **não impede** — prevalece a defesa técnica.',
  juris=[J['STF705']],
  peg='Fazer prevalecer a renúncia leiga.',
  kw=['Súmula 705', 'renúncia'])

# ======================= CPP-10 · Processo criminal de crimes comuns =======================
P = 'DBA26-CPP-10'
I(P, 1, 'Recebimento e citação',
  'Nos procedimentos ordinário e sumário, oferecida a denúncia, o juiz, se não a rejeitar liminarmente, recebê-la-á e ordenará a citação do acusado para responder à acusação, por escrito, no prazo de 10 dias.', 'C',
  'Art. 396, caput: **resposta à acusação** em 10 dias.',
  lei=[(CPP + '396', 'Nos procedimentos ordinário e sumário, oferecida a denúncia ou queixa', 'no prazo de 10 (dez) dias', 'CPP, art. 396, caput')],
  kw=['resposta à acusação', '10 dias'])
I(P, 1, 'Resposta não apresentada',
  'Não apresentada a resposta no prazo legal, o processo segue à revelia, sem necessidade de nomear defensor.', 'E',
  'Art. 396-A, § 2º: o juiz **nomeará defensor** para oferecê-la, com vista por 10 dias (a resposta é **obrigatória**).',
  lei=[(CPP + '396-A', 'Não apresentada a resposta no prazo legal', 'concedendo-lhe vista dos autos por 10 (dez) dias', 'CPP, art. 396-A, § 2º')],
  peg='Tratar a resposta como facultativa.',
  kw=['resposta obrigatória', 'defensor nomeado'])
I(P, 1, 'Absolvição sumária',
  'O juiz absolverá sumariamente o acusado quando verificar a existência manifesta de causa excludente da culpabilidade, inclusive a inimputabilidade.', 'E',
  'Art. 397, II: **salvo inimputabilidade** (o inimputável precisa do processo para eventual medida de segurança).',
  lei=[(CPP + '397', 'a existência manifesta de causa excludente da culpabilidade do agente, salvo inimputabilidade', None, 'CPP, art. 397, II')],
  peg='Incluir a inimputabilidade, que a lei exclui.',
  kw=['absolvição sumária', 'salvo inimputabilidade'])
I(P, 1, 'Hipóteses de absolvição sumária',
  'Cabe absolvição sumária quando o fato narrado evidentemente não constituir crime ou quando estiver extinta a punibilidade do agente.', 'C',
  'Art. 397, III e IV (também excludente manifesta de ilicitude — I).',
  lei=[(CPP + '397', 'que o fato narrado evidentemente não constitui crime; ou', None, 'CPP, art. 397, III'),
       (CPP + '397', 'extinta a punibilidade do agente', None, 'CPP, art. 397, IV')],
  kw=['absolvição sumária', 'extinta a punibilidade'])
I(P, 1, 'Resposta preliminar do funcionário',
  'A resposta preliminar do art. 514 do CPP, nos crimes funcionais afiançáveis, é indispensável mesmo quando a ação penal estiver instruída por inquérito policial.', 'E',
  '**Súmula 330/STJ**: é **desnecessária** quando a ação está instruída por **inquérito policial**.',
  juris=[J['S330']],
  peg='Inverter a Súmula 330.',
  kw=['Súmula 330', 'art. 514'])
# --- CPP-10 · Rodada 2
I(P, 2, 'Rejeição da denúncia e contrarrazões',
  'Constitui nulidade a falta de intimação do denunciado para oferecer contrarrazões ao recurso interposto da rejeição da denúncia, não a suprindo a nomeação de defensor dativo.', 'C',
  '**Súmula 707/STF**. E o acórdão que provê o recurso vale, desde logo, pelo **recebimento** da denúncia (**Súmula 709/STF**).',
  juris=[J['STF707'], J['STF709']],
  kw=['Súmula 707', 'contrarrazões'])
I(P, 2, 'Disposições comuns a todos os procedimentos',
  'As regras de rejeição da denúncia, resposta à acusação e absolvição sumária aplicam-se a todos os procedimentos penais de primeiro grau, ainda que não regulados no CPP.', 'C',
  'Art. 394, § 4º (arts. 395 a 398).',
  lei=[(CPP + '394', 'As disposições dos arts. 395 a 398 deste Código aplicam-se a todos os procedimentos penais de primeiro grau', None, 'CPP, art. 394, § 4º')],
  kw=['todos os procedimentos', 'art. 394, § 4º'])
I(P, 2, 'Prioridade de tramitação',
  'Os processos que apurem crime hediondo ou violência contra a mulher terão prioridade de tramitação em todas as instâncias.', 'C',
  'Art. 394-A (Lei 14.994/2024), que também isenta de custas os processos de violência contra a mulher, salvo má-fé (§ 1º).',
  lei=[(CPP + '394-A', 'Os processos que apurem a prática de crime hediondo ou violência contra a mulher terão prioridade de tramitação', None, 'CPP, art. 394-A, caput')],
  kw=['prioridade de tramitação', 'violência contra a mulher'])

# ======================= CPP-11 · Medidas assecuratórias =======================
P = 'DBA26-CPP-11'
I(P, 1, 'Sequestro de imóveis',
  'Caberá o sequestro dos bens imóveis adquiridos pelo indiciado com os proventos da infração, salvo se já transferidos a terceiro.', 'E',
  'Art. 125: cabe o sequestro **ainda que já tenham sido transferidos a terceiro**.',
  lei=[(CPP + '125', 'dos bens imóveis, adquiridos pelo indiciado com os proventos da infração', 'transferidos a terceiro', 'CPP, art. 125')],
  peg='Proteger a transferência a terceiro, que a lei não protege.',
  kw=['sequestro', 'proventos da infração'])
I(P, 1, 'Prova para o sequestro',
  'Para a decretação do sequestro exige-se prova plena da origem ilícita dos bens.', 'E',
  'Art. 126: bastam **indícios veementes** da proveniência ilícita.',
  lei=[(CPP + '126', 'bastará a existência de indícios veementes da proveniência ilícita dos bens', None, 'CPP, art. 126')],
  peg='Exigir prova plena.',
  kw=['indícios veementes', 'sequestro'])
I(P, 1, 'Iniciativa do sequestro',
  'O sequestro pode ser ordenado pelo juiz, de ofício, a requerimento do MP ou do ofendido, ou mediante representação da autoridade policial, em qualquer fase do processo ou antes de oferecida a denúncia.', 'C',
  'Art. 127 (texto que admite atuação de ofício, discutida à luz do art. 3º-A).',
  lei=[(CPP + '127', 'mediante representação da autoridade policial', 'antes de oferecida a denúncia ou queixa', 'CPP, art. 127')],
  kw=['representação da autoridade policial', 'sequestro'])
I(P, 1, 'Levantamento',
  'O sequestro será levantado se a ação penal não for intentada no prazo de 60 dias, contado da data em que ficar concluída a diligência.', 'C',
  'Art. 131, I. Também se o terceiro prestar caução ou se houver extinção da punibilidade ou absolvição transitada em julgado.',
  lei=[(CPP + '131', 'se a ação penal não for intentada no prazo de sessenta dias', 'concluída a diligência', 'CPP, art. 131, I')],
  kw=['levantamento', 'sessenta dias'])
I(P, 1, 'Hipoteca legal',
  'A hipoteca legal recai sobre os bens imóveis de origem ilícita do indiciado e pode ser requerida desde que haja indícios veementes da proveniência criminosa.', 'E',
  'A **hipoteca legal** (art. 134) recai sobre imóveis de origem **lícita**, para garantir a reparação; exige **certeza da infração** e **indícios suficientes de autoria**. Bens ilícitos são objeto de **sequestro**.',
  lei=[(CPP + '134', 'A hipoteca legal sobre os imóveis do indiciado poderá ser requerida pelo ofendido em qualquer fase do processo', 'indícios suficientes da autoria', 'CPP, art. 134')],
  peg='Confundir hipoteca legal (bens lícitos) com sequestro (bens ilícitos).',
  kw=['hipoteca legal', 'certeza da infração'])
# --- CPP-11 · Rodada 2
I(P, 2, 'Arresto de móveis',
  'Se o responsável não possuir bens imóveis ou os possuir de valor insuficiente, poderão ser arrestados bens móveis suscetíveis de penhora.', 'C',
  'Art. 137: **arresto** subsidiário de móveis.',
  lei=[(CPP + '137', 'Se o responsável não possuir bens imóveis ou os possuir de valor insuficiente', 'suscetíveis de penhora', 'CPP, art. 137, caput')],
  kw=['arresto', 'bens móveis'])
I(P, 2, 'Alienação antecipada',
  'A alienação antecipada de bens apreendidos só pode ocorrer após o trânsito em julgado da sentença condenatória.', 'E',
  'Art. 144-A: o juiz determinará a **alienação antecipada** sempre que os bens estiverem sujeitos a deterioração ou depreciação, ou houver dificuldade de manutenção — antes do trânsito.',
  lei=[(CPP + '144-A', 'O juiz determinará a alienação antecipada para preservação do valor dos bens', 'dificuldade para sua manutenção', 'CPP, art. 144-A, caput')],
  peg='Condicionar a alienação antecipada ao trânsito.',
  kw=['alienação antecipada', 'deterioração'])
I(P, 2, 'Leilão após o trânsito',
  'Transitada em julgado a sentença condenatória, o juiz determinará a avaliação e a venda em leilão público dos bens cujo perdimento tenha sido decretado.', 'C',
  'Art. 133, caput (Lei 13.964/2019); o valor vai ao Fundo Penitenciário Nacional, salvo previsão em lei especial (§ 2º).',
  lei=[(CPP + '133', 'Transitada em julgado a sentença condenatória, o juiz, de ofício ou a requerimento do interessado ou do Ministério Público', 'perdimento tenha sido decretado', 'CPP, art. 133, caput')],
  kw=['leilão público', 'perdimento'])

# ======================= CPP-12 · Prisão domiciliar =======================
P = 'DBA26-CPP-12'
I(P, 1, 'Conceito',
  'A prisão domiciliar consiste no recolhimento do indiciado ou acusado em sua residência, só podendo dela ausentar-se com autorização judicial.', 'C',
  'Art. 317: é **substitutiva da preventiva**, não cautelar autônoma.',
  lei=[(CPP + '317', 'A prisão domiciliar consiste no recolhimento do indiciado ou acusado em sua residência', 'autorização judicial', 'CPP, art. 317')],
  kw=['prisão domiciliar', 'autorização judicial'])
I(P, 1, 'Idade',
  'O juiz poderá substituir a prisão preventiva pela domiciliar quando o agente for maior de 70 anos.', 'E',
  'Art. 318, I: maior de **80 anos**.',
  lei=[(CPP + '318', 'maior de 80 (oitenta) anos', None, 'CPP, art. 318, I')],
  peg='Trocar 80 por 70 anos.',
  kw=['80 anos', 'prisão domiciliar'])
I(P, 1, 'Filhos',
  'A preventiva pode ser substituída pela domiciliar quando o agente for mulher com filho de até 12 anos incompletos ou homem, se for o único responsável pelos cuidados do filho nessa idade.', 'C',
  'Art. 318, V e VI.',
  lei=[(CPP + '318', 'mulher com filho de até 12 (doze) anos de idade incompletos', None, 'CPP, art. 318, V'),
       (CPP + '318', 'homem, caso seja o único responsável pelos cuidados do filho de até 12 (doze) anos de idade incompletos', None, 'CPP, art. 318, VI')],
  kw=['12 anos incompletos', 'único responsável'])
I(P, 1, 'Gestante — art. 318-A',
  'A preventiva imposta à gestante ou mãe de criança será substituída pela domiciliar mesmo que ela tenha cometido o crime com violência ou grave ameaça.', 'E',
  'Art. 318-A: substituição **desde que** não tenha cometido crime com **violência ou grave ameaça** e não o tenha cometido **contra o filho ou dependente**.',
  lei=[(CPP + '318-A', 'não tenha cometido crime com violência ou grave ameaça a pessoa', None, 'CPP, art. 318-A, I'),
       (CPP + '318-A', 'não tenha cometido o crime contra seu filho ou dependente', None, 'CPP, art. 318-A, II')],
  peg='Ignorar as condições do art. 318-A.',
  kw=['art. 318-A', 'violência ou grave ameaça'])
I(P, 1, 'Prova idônea',
  'Para a substituição da preventiva pela domiciliar, o juiz exigirá prova idônea dos requisitos legais.', 'C',
  'Art. 318, par. ún.',
  lei=[(CPP + '318', 'Para a substituição, o juiz exigirá prova idônea dos requisitos estabelecidos neste artigo', None, 'CPP, art. 318, par. ún.')],
  kw=['prova idônea', 'substituição'])
# --- CPP-12 · Rodada 2
I(P, 2, 'Domiciliar e cautelares',
  'A substituição da preventiva pela domiciliar dos arts. 318 e 318-A impede a aplicação concomitante de medidas cautelares do art. 319.', 'E',
  'Art. 318-B: a substituição pode ser feita **sem prejuízo** da aplicação **concomitante** das medidas do art. 319 (ex.: monitoração eletrônica).',
  lei=[(CPP + '318-B', 'poderá ser efetuada sem prejuízo da aplicação concomitante das medidas alternativas previstas no art. 319', None, 'CPP, art. 318-B')],
  peg='Negar a cumulação.',
  kw=['art. 318-B', 'concomitante'])
I(P, 2, 'Doença grave',
  'Cabe a substituição da preventiva pela domiciliar quando o agente estiver extremamente debilitado por motivo de doença grave.', 'C',
  'Art. 318, II.',
  lei=[(CPP + '318', 'extremamente debilitado por motivo de doença grave', None, 'CPP, art. 318, II')],
  kw=['doença grave', 'extremamente debilitado'])
I(P, 2, 'Domiciliar e recolhimento noturno',
  'A prisão domiciliar do art. 317 do CPP e o recolhimento domiciliar noturno do art. 319, V, são o mesmo instituto.', 'E',
  'A **prisão domiciliar** substitui a preventiva (recolhimento integral). O **recolhimento domiciliar noturno** e nos dias de folga é **cautelar diversa da prisão**, para quem tem residência e trabalho fixos.',
  lei=[(CPP + '319', 'recolhimento domiciliar no período noturno e nos dias de folga', None, 'CPP, art. 319, V')],
  peg='Igualar os dois institutos.',
  kw=['recolhimento domiciliar noturno', 'cautelar diversa'])

# ======================= CPP-13 · Outras medidas cautelares =======================
P = 'DBA26-CPP-13'
I(P, 1, 'Rol do art. 319',
  'São medidas cautelares diversas da prisão, entre outras, o comparecimento periódico em juízo, a proibição de acesso a determinados lugares, a proibição de contato com pessoa determinada e a monitoração eletrônica.', 'C',
  'Art. 319, I a III e IX.',
  lei=[(CPP + '319', 'São medidas cautelares diversas da prisão', None, 'CPP, art. 319, caput'),
       (CPP + '319', 'monitoração eletrônica', None, 'CPP, art. 319, IX')],
  kw=['cautelares diversas', 'monitoração eletrônica'])
I(P, 1, 'Suspensão de função pública',
  'A suspensão do exercício de função pública é cautelar que só pode ser aplicada após a sentença condenatória.', 'E',
  'Art. 319, VI: cabe a qualquer tempo, quando houver **justo receio** de sua utilização para a prática de infrações penais.',
  lei=[(CPP + '319', 'suspensão do exercício de função pública ou de atividade de natureza econômica ou financeira', None, 'CPP, art. 319, VI')],
  peg='Condicionar a cautelar à sentença.',
  kw=['suspensão de função pública', 'justo receio'])
I(P, 1, 'Internação provisória',
  'A internação provisória cabe nos crimes praticados com violência ou grave ameaça, quando os peritos concluírem ser o acusado inimputável ou semi-imputável e houver risco de reiteração.', 'C',
  'Art. 319, VII.',
  lei=[(CPP + '319', 'internação provisória do acusado nas hipóteses de crimes praticados com violência ou grave ameaça', 'risco de reiteração', 'CPP, art. 319, VII')],
  kw=['internação provisória', 'risco de reiteração'])
I(P, 1, 'Proibição de ausentar-se do País',
  'A proibição de ausentar-se do País será comunicada pelo juiz às autoridades encarregadas de fiscalizar as saídas do território nacional, intimando-se o investigado ou acusado a entregar o passaporte em 24 horas.', 'C',
  'Art. 320 do CPP.',
  lei=[(CPP + '320', 'A proibição de ausentar-se do País será comunicada pelo juiz', 'no prazo de 24 (vinte e quatro) horas', 'CPP, art. 320')],
  kw=['passaporte', '24 horas'])
I(P, 1, 'Recolhimento noturno — requisito',
  'O recolhimento domiciliar no período noturno e nos dias de folga pode ser imposto a qualquer investigado, independentemente de ter residência e trabalho fixos.', 'E',
  'Art. 319, V: exige que o investigado ou acusado **tenha residência e trabalho fixos**.',
  lei=[(CPP + '319', 'recolhimento domiciliar no período noturno e nos dias de folga quando o investigado ou acusado tenha residência e trabalho fixos', None, 'CPP, art. 319, V')],
  peg='Apagar o requisito de residência e trabalho fixos.',
  kw=['recolhimento noturno', 'residência e trabalho fixos'])
# --- CPP-13 · Rodada 2
I(P, 2, 'Protetivas nos crimes sexuais',
  'Desde a Lei 15.280/2025, constatados indícios de crime contra a dignidade sexual, o juiz pode aplicar de imediato ao autor medidas protetivas de urgência, como afastamento do lar e proibição de aproximação da vítima.', 'C',
  'Art. 350-A do CPP; o § 5º manda cumular a protetiva com **monitoração eletrônica**.',
  lei=[(CPP + '350-A', 'Constatada a existência de indícios da prática de crime contra a dignidade sexual, o juiz poderá aplicar, de imediato, ao autor', None, 'CPP, art. 350-A, caput')],
  kw=['Lei 15.280/2025', 'medidas protetivas'])
I(P, 2, 'Afastamento pelo delegado',
  'Na violência doméstica, verificada a existência de risco atual ou iminente à vida ou à integridade da mulher, o delegado de polícia pode afastar imediatamente o agressor do lar quando o Município não for sede de comarca.', 'C',
  'Lei 11.340/2006, art. 12-C, II: o **delegado** afasta quando o Município **não for sede de comarca**; o policial, quando também não houver delegado disponível. O juiz é comunicado em 24 horas.',
  lei=[('L11340:12-C', 'pelo delegado de polícia, quando o Município não for sede de comarca', None, 'Lei 11.340/2006, art. 12-C, II')],
  kw=['art. 12-C', 'afastamento do lar'])
I(P, 2, 'Cumulação',
  'As medidas cautelares diversas da prisão não podem ser aplicadas cumulativamente.', 'E',
  'Art. 282, § 1º: podem ser aplicadas **isolada ou cumulativamente**.',
  lei=[(CPP + '282', 'As medidas cautelares poderão ser aplicadas isolada ou cumulativamente', None, 'CPP, art. 282, § 1º')],
  peg='Vedar a cumulação.',
  kw=['isolada ou cumulativamente', 'cautelares'])

# ======================= CPP-14 · Procedimento comum: ordinário, sumário e sumaríssimo =======================
P = 'DBA26-CPP-14'
I(P, 1, 'Critério do procedimento',
  'O procedimento comum será ordinário quando o crime tiver sanção máxima igual ou superior a 4 anos, sumário quando inferior a 4 anos e sumaríssimo para as infrações de menor potencial ofensivo.', 'C',
  'Art. 394, § 1º: critério da **pena máxima**.',
  lei=[(CPP + '394', 'ordinário, quando tiver por objeto crime cuja sanção máxima cominada for igual ou superior a 4 (quatro) anos', None, 'CPP, art. 394, § 1º, I'),
       (CPP + '394', 'sumário, quando tiver por objeto crime cuja sanção máxima cominada seja inferior a 4 (quatro) anos', None, 'CPP, art. 394, § 1º, II')],
  kw=['pena máxima', 'ordinário'])
I(P, 1, 'Testemunhas no sumário',
  'No procedimento sumário, poderão ser inquiridas até 8 testemunhas arroladas pela acusação e 8 pela defesa.', 'E',
  'Art. 532: no **sumário**, até **5** testemunhas por parte (8 é o ordinário).',
  lei=[(CPP + '532', 'Na instrução, poderão ser inquiridas até 5 (cinco) testemunhas arroladas pela acusação e 5 (cinco) pela defesa', None, 'CPP, art. 532')],
  peg='Levar ao sumário o número do ordinário.',
  kw=['5 testemunhas', 'sumário'])
I(P, 1, 'Prazo da audiência',
  'No procedimento ordinário, a audiência de instrução e julgamento deve ser realizada no prazo máximo de 30 dias.', 'E',
  'Ordinário: **60 dias** (art. 400). **Sumário**: 30 dias (art. 531).',
  lei=[(CPP + '400', 'a ser realizada no prazo máximo de 60 (sessenta) dias', None, 'CPP, art. 400, caput')],
  peg='Trocar os prazos do ordinário e do sumário.',
  kw=['60 dias', '30 dias'])
I(P, 1, 'Alegações finais',
  'Não havendo diligências, serão oferecidas alegações finais orais por 20 minutos, pela acusação e pela defesa, prorrogáveis por mais 10, e o juiz poderá, pela complexidade, conceder prazo de 5 dias sucessivos para memoriais.', 'C',
  'Art. 403, caput e § 3º (sentença em 10 dias, no caso de memoriais).',
  lei=[(CPP + '403', 'serão oferecidas alegações finais orais por 20 (vinte) minutos', 'prorrogáveis por mais 10 (dez)', 'CPP, art. 403, caput')],
  kw=['alegações finais', 'memoriais'])
I(P, 1, 'Do JECrim ao juízo comum',
  'Quando o Juizado Especial Criminal encaminhar as peças ao juízo comum, observa-se o procedimento ordinário.', 'E',
  'Art. 538: observa-se o procedimento **sumário**.',
  lei=[(CPP + '538', 'observar-se-á o procedimento sumário previsto neste Capítulo', None, 'CPP, art. 538')],
  peg='Trocar sumário por ordinário.',
  kw=['procedimento sumário', 'art. 538'])
I(P, 1, 'Sumaríssimo — resposta antes do recebimento',
  'No rito sumaríssimo, aberta a audiência, a palavra é dada ao defensor para responder à acusação, após o que o juiz receberá, ou não, a denúncia ou queixa.', 'C',
  'Lei 9.099/1995, art. 81: defesa **antes do recebimento** (diferente do ordinário, em que a resposta vem depois).',
  lei=[(JE + '81', 'dada a palavra ao defensor para responder à acusação, após o que o Juiz receberá, ou não, a denúncia ou queixa', None, 'Lei 9.099/1995, art. 81, caput')],
  kw=['sumaríssimo', 'antes do recebimento'])
# --- CPP-14 · Rodada 2
I(P, 2, 'Aplicação subsidiária',
  'Aplicam-se subsidiariamente aos procedimentos especial, sumário e sumaríssimo as disposições do procedimento ordinário.', 'C',
  'Art. 394, § 5º.',
  lei=[(CPP + '394', 'Aplicam-se subsidiariamente aos procedimentos especial, sumário e sumaríssimo as disposições do procedimento ordinário', None, 'CPP, art. 394, § 5º')],
  kw=['subsidiariamente', 'procedimento ordinário'])
I(P, 2, 'Sumaríssimo e pena',
  'O procedimento sumaríssimo aplica-se aos crimes com pena máxima não superior a 4 anos.', 'E',
  'Sumaríssimo: infrações de **menor potencial ofensivo** — contravenções e crimes com pena máxima **não superior a 2 anos** (Lei 9.099/1995, art. 61).',
  lei=[(CPP + '394', 'sumaríssimo, para as infrações penais de menor potencial ofensivo, na forma da lei', None, 'CPP, art. 394, § 1º, III')],
  peg='Confundir o limite do sumaríssimo com o do sumário.',
  kw=['menor potencial ofensivo', '2 anos'])
I(P, 2, 'Prazo da audiência no sumário',
  'No procedimento sumário, a audiência de instrução e julgamento deve ser realizada no prazo máximo de 30 dias.', 'C',
  'Art. 531 do CPP.',
  lei=[(CPP + '531', 'a ser realizada no prazo máximo de 30 (trinta) dias', None, 'CPP, art. 531')],
  kw=['30 dias', 'procedimento sumário'])
I(P, 2, 'Memoriais e prazo da sentença',
  'Concedido prazo para memoriais, o juiz terá 30 dias para proferir a sentença.', 'E',
  'Art. 403, § 3º: **10 dias**.',
  lei=[(CPP + '403', 'Nesse caso, terá o prazo de 10 (dez) dias para proferir a sentença', None, 'CPP, art. 403, § 3º')],
  peg='Trocar 10 por 30 dias.',
  kw=['memoriais', '10 dias'])

# ======================= CPP-15 · Meios de impugnação e ações autônomas =======================
P = 'DBA26-CPP-15'
I(P, 1, 'Fungibilidade',
  'Ainda que haja má-fé, a parte não será prejudicada pela interposição de um recurso por outro.', 'E',
  'Art. 579: a **fungibilidade** só vale **salvo a hipótese de má-fé**.',
  lei=[(CPP + '579', 'Salvo a hipótese de má-fé, a parte não será prejudicada pela interposição de um recurso por outro', None, 'CPP, art. 579, caput')],
  peg='Retirar a ressalva da má-fé.',
  kw=['fungibilidade', 'má-fé'])
I(P, 1, 'Desistência do MP',
  'O Ministério Público pode desistir do recurso que haja interposto, se se convencer do acerto da decisão.', 'E',
  'Art. 576: o MP **não poderá desistir** de recurso que haja interposto (pode, porém, deixar de recorrer).',
  lei=[(CPP + '576', 'O Ministério Público não poderá desistir de recurso que haja interposto', None, 'CPP, art. 576')],
  peg='Confundir não recorrer com desistir.',
  kw=['não poderá desistir', 'recurso'])
I(P, 1, 'RESE — rejeição da denúncia',
  'Cabe apelação da decisão que não receber a denúncia ou a queixa no procedimento comum do CPP.', 'E',
  'Art. 581, I: cabe **recurso em sentido estrito**. Apelação é a via no JECrim (Lei 9.099/1995, art. 82).',
  lei=[(CPP + '581', 'que não receber a denúncia ou a queixa', None, 'CPP, art. 581, I')],
  peg='Trocar RESE por apelação fora do JECrim.',
  kw=['recurso em sentido estrito', 'rejeição da denúncia'])
I(P, 1, 'Prazo da apelação',
  'A apelação deve ser interposta no prazo de 8 dias, e as razões apresentadas em 5 dias.', 'E',
  'Inverteu: interposição em **5 dias** (art. 593) e razões em **8 dias** (art. 600).',
  lei=[(CPP + '593', 'Caberá apelação no prazo de 5 (cinco) dias', None, 'CPP, art. 593, caput')],
  peg='Inverter os prazos de interposição e de razões.',
  kw=['5 dias', 'apelação'])
I(P, 1, 'Reformatio in pejus',
  'Quando somente o réu houver apelado, o tribunal pode agravar a pena se constatar erro material na dosimetria.', 'E',
  'Art. 617: **não** pode ser agravada a pena quando **somente o réu** apelou (proibição da **reformatio in pejus**).',
  lei=[(CPP + '617', 'não podendo, porém, ser agravada a pena, quando somente o réu houver apelado da sentença', None, 'CPP, art. 617')],
  peg='Permitir agravamento em recurso exclusivo da defesa.',
  kw=['reformatio in pejus', 'somente o réu'])
I(P, 1, 'Revisão criminal — hipóteses',
  'A revisão dos processos findos será admitida quando a sentença condenatória for contrária ao texto expresso da lei penal ou à evidência dos autos, quando se fundar em provas comprovadamente falsas, ou quando surgirem novas provas de inocência.', 'C',
  'Art. 621, I a III: ação autônoma **pro reo**; não há revisão pro societate.',
  lei=[(CPP + '621', 'A revisão dos processos findos será admitida:', None, 'CPP, art. 621, caput')],
  kw=['revisão criminal', 'pro reo'])
# --- CPP-15 · Rodada 2
I(P, 2, 'Prazo da revisão',
  'A revisão criminal só pode ser requerida enquanto não extinta a pena.', 'E',
  'Art. 622: **em qualquer tempo**, antes da extinção da pena **ou após**.',
  lei=[(CPP + '622', 'A revisão poderá ser requerida em qualquer tempo, antes da extinção da pena ou após', None, 'CPP, art. 622, caput')],
  peg='Limitar a revisão no tempo.',
  kw=['em qualquer tempo', 'revisão'])
I(P, 2, 'Extensão',
  'No concurso de agentes, a decisão do recurso interposto por um dos réus, se fundada em motivos que não sejam de caráter exclusivamente pessoal, aproveitará aos outros.', 'C',
  'Art. 580: **efeito extensivo**.',
  lei=[(CPP + '580', 'a decisão do recurso interposto por um dos réus, se fundado em motivos que não sejam de caráter exclusivamente pessoal, aproveitará aos outros', None, 'CPP, art. 580')],
  kw=['efeito extensivo', 'concurso de agentes'])
I(P, 2, 'Embargos infringentes',
  'Os embargos infringentes e de nulidade cabem contra qualquer decisão não unânime de segunda instância, podendo ser opostos pela acusação ou pela defesa.', 'E',
  'Art. 609, par. ún.: só contra decisão não unânime **desfavorável ao réu** — recurso **exclusivo da defesa**, em 10 dias.',
  lei=[(CPP + '609', 'Quando não for unânime a decisão de segunda instância, desfavorável ao réu', 'dentro de 10 (dez) dias', 'CPP, art. 609, par. ún.')],
  peg='Abrir o recurso à acusação.',
  kw=['embargos infringentes', 'exclusivo da defesa'])
I(P, 2, 'Efeito suspensivo no RESE de cautelar',
  'Desde a Lei 15.358/2026, no RESE contra decisão sobre fiança, preventiva, liberdade provisória ou relaxamento do flagrante, o recorrente pode pedir ao tribunal efeito suspensivo ou ativo, demonstrando relevância, plausibilidade e risco de dano.', 'C',
  'Art. 584, § 4º (remete ao art. 581, V).',
  lei=[(CPP + '584', 'o recorrente poderá pedir ao Tribunal ad quem concessão de efeito suspensivo ou ativo ao recurso interposto', None, 'CPP, art. 584, § 4º')],
  kw=['efeito suspensivo', 'Lei 15.358/2026'])

# ======================= CPP-15-B2 · Jurisprudência aplicada dos tribunais superiores =======================
P = 'DBA26-CPP-15-B2'
I(P, 1, 'Desaforamento sem defesa',
  'É nula a decisão que determina o desaforamento de processo da competência do júri sem audiência da defesa.', 'C',
  '**Súmula 712/STF**.',
  juris=[J['STF712']],
  kw=['Súmula 712', 'desaforamento'])
I(P, 1, 'Quesito obrigatório',
  'É relativa a nulidade do julgamento pelo júri por falta de quesito obrigatório.', 'E',
  '**Súmula 156/STF**: nulidade **absoluta**.',
  juris=[J['STF156']],
  peg='Trocar absoluta por relativa.',
  kw=['Súmula 156', 'quesito obrigatório'])
I(P, 1, 'Viatura da PM',
  'Compete à Justiça Militar estadual o delito decorrente de acidente de trânsito envolvendo viatura da polícia militar, ainda que a vítima seja civil.', 'E',
  '**Súmula 6/STJ**: compete à **Justiça Comum Estadual**, salvo se autor e vítima forem policiais militares em situação de atividade.',
  juris=[J['S6']],
  peg='Levar à Justiça Militar caso com vítima civil.',
  kw=['Súmula 6', 'viatura'])
I(P, 1, 'Civil contra instituição militar estadual',
  'Compete à Justiça Comum Estadual processar e julgar civil acusado de crime contra instituições militares estaduais.', 'C',
  '**Súmula 53/STJ**: a Justiça Militar estadual não julga civis (CF, art. 125, § 4º).',
  juris=[J['S53']],
  kw=['Súmula 53', 'civil'])
I(P, 1, 'Falso testemunho trabalhista',
  'Compete à Justiça Estadual processar e julgar crime de falso testemunho cometido no processo trabalhista.', 'E',
  '**Súmula 165/STJ**: compete à **Justiça Federal** (ofensa à administração da Justiça do Trabalho, órgão federal).',
  juris=[J['S165']],
  peg='Trocar Federal por Estadual.',
  kw=['Súmula 165', 'falso testemunho'])
I(P, 1, 'Contrabando e prevenção',
  'A competência para o crime de contrabando ou descaminho define-se pelo domicílio do agente.', 'E',
  '**Súmula 151/STJ**: **prevenção do juízo federal do lugar da apreensão** dos bens.',
  juris=[J['S151']],
  peg='Trocar o critério da súmula.',
  kw=['Súmula 151', 'contrabando'])
# --- CPP-15-B2 · Rodada 2
I(P, 2, 'Funcionário público federal',
  'Compete à Justiça Federal processar e julgar crimes praticados contra funcionário público federal, quando relacionados com o exercício da função.', 'C',
  '**Súmula 147/STJ**.',
  juris=[J['S147']],
  kw=['Súmula 147', 'funcionário público federal'])
I(P, 2, 'Sociedade de economia mista',
  'Os crimes praticados em detrimento de sociedade de economia mista federal são de competência da Justiça Federal.', 'E',
  '**Súmula 42/STJ**: **Justiça Comum Estadual** (a sociedade de economia mista não está no art. 109, IV, da CF; empresa pública federal está).',
  juris=[J['S42']],
  peg='Equiparar sociedade de economia mista a empresa pública.',
  kw=['Súmula 42', 'sociedade de economia mista'])
I(P, 2, 'CTPS e empresa privada',
  'O crime de falsa anotação na CTPS atribuído a empresa privada é de competência da Justiça Federal.', 'E',
  '**Súmula 62/STJ**: **Justiça Estadual**.',
  juris=[J['S62']],
  peg='Federalizar a falsa anotação feita por empresa privada.',
  kw=['Súmula 62', 'CTPS'])
I(P, 2, 'Prerrogativa e exceção da verdade',
  'Na ação por ofensa à honra em que se admite exceção da verdade quanto ao desempenho de função pública, prevalece a competência por prerrogativa de função, ainda que já tenha cessado o exercício funcional do ofendido.', 'C',
  '**Súmula 396/STF**.',
  juris=[J['STF396']],
  kw=['Súmula 396', 'exceção da verdade'])
I(P, 2, 'Diploma de ensino particular',
  'A falsificação e o uso de documento falso relativo a estabelecimento particular de ensino são de competência da Justiça Federal, por fiscalização do MEC.', 'E',
  '**Súmula 104/STJ**: **Justiça Estadual**.',
  juris=[J['S104']],
  peg='Federalizar pelo argumento da fiscalização do MEC.',
  kw=['Súmula 104', 'ensino particular'])
