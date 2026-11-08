# Pente Fino de Direito Penal (Parte Geral) — PEN-8 (teoria geral da pena, 8.1 a 8.13) (08/11/2026).
from base import I
from pen_juris import J

CP = 'CP:'
LEP = 'L7210:'
PENAS = (CP + '32', 'As penas são:', 'de multa.', 'CP, art. 32')
REGIME = (CP + '33', 'A pena de reclusão deve ser cumprida em regime fechado, semi-aberto ou aberto.', 'salvo necessidade de transferência a regime fechado', 'CP, art. 33, caput')
SUBST = (CP + '44', 'As penas restritivas de direitos são autônomas e substituem as privativas de liberdade, quando:', 'se o crime for culposo', 'CP, art. 44, I')
ART59 = (CP + '59', 'O juiz, atendendo à culpabilidade', 'para reprovação e prevenção do crime', 'CP, art. 59, caput')
TRIF = (CP + '68', 'A pena-base será fixada atendendo-se ao critério do art. 59 deste Código', 'as causas de diminuição e de aumento', 'CP, art. 68, caput')
SURSIS = (CP + '77', 'A execução da pena privativa de liberdade, não superior a 2 (dois) anos, poderá ser suspensa, por 2 (dois) a 4 (quatro) anos', None, 'CP, art. 77, caput')
LC = (CP + '83', 'O juiz poderá conceder livramento condicional ao condenado a pena privativa de liberdade igual ou superior a 2 (dois) anos', None, 'CP, art. 83, caput')
MULTA = (CP + '49', 'A pena de multa consiste no pagamento ao fundo penitenciário da quantia fixada na sentença e calculada em dias-multa.', 'de 360 (trezentos e sessenta) dias-multa', 'CP, art. 49, caput')

# ======================= PEN-8 · Teoria geral da pena =======================
P = 'DBA26-PEN-8'
I(P, 1, 'Espécies de pena',
  'As penas previstas no Código Penal são privativas de liberdade, restritivas de direitos e de multa.', 'C',
  'Art. 32. A CF (art. 5º, XLVI) acrescenta, entre outras, perda de bens e suspensão ou interdição de direitos.',
  lei=[PENAS], kw=['privativas de liberdade', 'restritivas de direitos', 'multa'])
I(P, 1, 'Penas vedadas',
  'A Constituição admite pena de caráter perpétuo para crimes hediondos cometidos com resultado morte.', 'E',
  'Não haverá penas **de caráter perpétuo** (CF, art. 5º, XLVII, b), sem exceção. O teto de cumprimento é de **40 anos** (CP, art. 75).',
  lei=[('CF:5', 'não haverá penas:', 'cruéis', 'CF, art. 5º, XLVII'),
       (CP + '75', 'O tempo de cumprimento das penas privativas de liberdade não pode ser superior a 40 (quarenta) anos.', None, 'CP, art. 75, caput')],
  peg='Criar exceção à vedação da prisão perpétua.', kw=['caráter perpétuo', '40 anos'])
I(P, 1, 'Limite de 40 anos',
  'O tempo de cumprimento das penas privativas de liberdade não pode ser superior a 40 anos, e as penas cuja soma o ultrapasse devem ser unificadas para atender a esse limite.', 'C',
  'Art. 75, caput e § 1º (Lei 13.964/2019; antes, 30 anos).',
  lei=[(CP + '75', 'Quando o agente for condenado a penas privativas de liberdade cuja soma seja superior a 40 (quarenta) anos', None, 'CP, art. 75, § 1º')],
  kw=['40 anos', 'unificadas'])
I(P, 1, 'Unificação e benefícios',
  'A pena unificada no limite máximo de cumprimento serve de base para o cálculo do livramento condicional e da progressão de regime.', 'E',
  'A **Súmula 715/STF** diz que a pena unificada **não** é considerada para outros benefícios: livramento e progressão se calculam sobre a pena **total** aplicada.',
  juris=[J['STF715']], peg='Calcular benefícios sobre a pena unificada.', kw=['Súmula 715/STF', 'pena total'])
I(P, 1, 'Detração',
  'Computam-se, na pena privativa de liberdade e na medida de segurança, o tempo de prisão provisória, no Brasil ou no estrangeiro, o de prisão administrativa e o de internação.', 'C',
  'É a **detração** (art. 42).',
  lei=[(CP + '42', 'Computam-se, na pena privativa de liberdade e na medida de segurança, o tempo de prisão provisória', None, 'CP, art. 42')],
  kw=['detração', 'prisão provisória'])
# --- PEN-8 · Rodada 2
I(P, 2, 'Nova unificação',
  'Sobrevindo condenação por fato posterior ao início do cumprimento da pena, faz-se nova unificação, desprezando-se o período de pena já cumprido.', 'C',
  'Art. 75, § 2º: por isso, crime cometido durante a execução pode levar o total a ultrapassar 40 anos de cumprimento efetivo.',
  lei=[(CP + '75', 'Sobrevindo condenação por fato posterior ao início do cumprimento da pena', None, 'CP, art. 75, § 2º')],
  kw=['nova unificação'])
I(P, 2, 'Ordem de execução',
  'No concurso de infrações, executa-se primeiramente a pena menos grave, para favorecer o condenado.', 'E',
  'Art. 76: executa-se **primeiramente a mais grave**. E, havendo reclusão e detenção cumulativas, primeiro a reclusão (art. 69).',
  lei=[(CP + '76', 'No concurso de infrações, executar-se-á primeiramente a pena mais grave.', None, 'CP, art. 76')],
  peg='Inverter a ordem.', kw=['mais grave'])
I(P, 2, 'Direitos do preso',
  'O preso conserva todos os direitos não atingidos pela perda da liberdade, e seu trabalho será sempre remunerado.', 'C',
  'Arts. 38 e 39 do CP.',
  lei=[(CP + '38', 'O preso conserva todos os direitos não atingidos pela perda da liberdade', None, 'CP, art. 38'),
       (CP + '39', 'O trabalho do preso será sempre remunerado', None, 'CP, art. 39')],
  kw=['direitos não atingidos', 'remunerado'])

# ======================= PEN-8.1 · Cominação das penas =======================
P = 'DBA26-PEN-8.1'
I(P, 1, 'Limites da sanção',
  'As penas privativas de liberdade têm seus limites estabelecidos na sanção correspondente a cada tipo legal de crime.', 'C',
  'Art. 53: a **cominação** é feita no preceito secundário de cada tipo.',
  lei=[(CP + '53', 'As penas privativas de liberdade têm seus limites estabelecidos na sanção correspondente a cada tipo legal de crime.', None, 'CP, art. 53')],
  kw=['cominação', 'preceito secundário'])
I(P, 1, 'Restritivas e cominação',
  'As penas restritivas de direitos só podem ser aplicadas quando expressamente cominadas no tipo penal da Parte Especial.', 'E',
  'As restritivas aplicam-se **independentemente de cominação na Parte Especial**, em substituição à privativa (art. 54).',
  lei=[(CP + '54', 'As penas restritivas de direitos são aplicáveis, independentemente de cominação na parte especial', None, 'CP, art. 54')],
  peg='Exigir cominação expressa da restritiva.', kw=['independentemente de cominação'])
I(P, 1, 'Multa e limites',
  'A multa prevista em cada tipo legal de crime tem os limites fixados no art. 49 do Código Penal.', 'C',
  'Art. 58: o tipo só diz "e multa"; o cálculo segue o sistema de **dias-multa** (10 a 360).',
  lei=[(CP + '58', 'A multa, prevista em cada tipo legal de crime, tem os limites fixados no art. 49', None, 'CP, art. 58, caput'), MULTA],
  kw=['dias-multa'])
I(P, 1, 'Cominação cumulativa em lei especial',
  'Cominadas cumulativamente, em lei especial, penas privativa de liberdade e pecuniária, é possível substituir a prisão por multa.', 'E',
  'A **Súmula 171/STJ** veda a substituição da prisão por multa nesse caso.',
  juris=[J['S171']], peg='Admitir a substituição por multa quando a lei especial já comina multa cumulativa.', kw=['Súmula 171/STJ'])
I(P, 1, 'Formas de cominação',
  'A cominação pode ser isolada, cumulativa ou alternativa, como no crime cuja pena é detenção ou multa.', 'C',
  'Classificação doutrinária do preceito secundário. Ex.: art. 132 (detenção isolada) e art. 140 (detenção **ou** multa).',
  lei=[(CP + '140', 'Injuriar alguém, ofendendo-lhe a dignidade ou o decoro', None, 'CP, art. 140, caput')],
  kw=['cominação alternativa', 'cumulativa'])
# --- PEN-8.1 · Rodada 2
I(P, 2, 'Medida provisória e pena',
  'Medida provisória pode alterar o preceito secundário de tipo penal para reduzir a pena, por se tratar de norma benéfica.', 'E',
  'A vedação do art. 62, § 1º, I, b, da CF abrange **direito penal**, sem ressalva textual. Há debate doutrinário sobre MP benéfica, mas a assertiva ignora a vedação constitucional expressa.',
  lei=[('CF:62', 'É vedada a edição de medidas provisórias sobre matéria', 'direito penal, processual penal e processual civil', 'CF, art. 62, § 1º, I, b')],
  peg='Liberar MP penal "benéfica".', kw=['medida provisória', 'vedada'])
I(P, 2, 'Multa substitutiva',
  'A multa substitutiva aplica-se independentemente de cominação na Parte Especial.', 'C',
  'Art. 58, par. ún.',
  lei=[(CP + '58', 'aplica-se independentemente de cominação na parte especial', None, 'CP, art. 58, par. ún.')],
  kw=['multa substitutiva'])
I(P, 2, 'Reserva legal da pena',
  'A pena cominada pode ser fixada por decreto, desde que a conduta esteja descrita em lei.', 'E',
  'Pela **reserva legal**, não há pena sem **prévia cominação legal** (CF, art. 5º, XXXIX; CP, art. 1º): a sanção também exige lei.',
  lei=[(CP + '1', 'Não há pena sem prévia cominação legal.', None, 'CP, art. 1º, 2ª parte')],
  peg='Admitir pena por decreto.', kw=['prévia cominação legal'])

# ======================= PEN-8.2 · Penas privativas de liberdade =======================
P = 'DBA26-PEN-8.2'
I(P, 1, 'Reclusão e detenção',
  'A pena de reclusão deve ser cumprida em regime fechado, semiaberto ou aberto; a de detenção, em regime semiaberto ou aberto, salvo necessidade de transferência a regime fechado.', 'C',
  'Art. 33, caput: a **detenção não começa no fechado**, mas pode chegar a ele por **regressão**.',
  lei=[REGIME], kw=['reclusão', 'detenção'])
I(P, 1, 'Detenção e regime inicial fechado',
  'O juiz pode fixar regime inicial fechado para pena de detenção quando o réu for reincidente.', 'E',
  'Para a **detenção** o regime **inicial** é semiaberto ou aberto (art. 33, caput); o fechado só por **transferência** (regressão) na execução.',
  lei=[REGIME], peg='Regime inicial fechado em detenção.', kw=['detenção', 'regime inicial'])
I(P, 1, 'Exame criminológico',
  'O condenado será submetido, no início do cumprimento da pena, a exame criminológico de classificação para individualização da execução.', 'C',
  'Art. 34, caput (fechado), estendido ao semiaberto pelo art. 35.',
  lei=[(CP + '34', 'O condenado será submetido, no início do cumprimento da pena, a exame criminológico de classificação', None, 'CP, art. 34, caput')],
  kw=['exame criminológico de classificação'])
I(P, 1, 'Trabalho externo no fechado',
  'No regime fechado, o trabalho externo é admissível em qualquer empresa privada, desde que haja vigilância.', 'E',
  'Art. 34, § 3º: no fechado, o **trabalho externo** só é admissível em **serviços ou obras públicas**.',
  lei=[(CP + '34', 'O trabalho externo é admissível, no regime fechado, em serviços ou obras públicas.', None, 'CP, art. 34, § 3º')],
  kw=['trabalho externo', 'obras públicas'])
I(P, 1, 'Regime aberto',
  'O regime aberto baseia-se na autodisciplina e no senso de responsabilidade do condenado, que trabalha fora sem vigilância e se recolhe à noite e nos dias de folga.', 'C',
  'Art. 36, caput e § 1º.',
  lei=[(CP + '36', 'O regime aberto baseia-se na autodisciplina e senso de responsabilidade do condenado.', None, 'CP, art. 36, caput')],
  kw=['autodisciplina'])
I(P, 1, 'Transferência do aberto',
  'O condenado só será transferido do regime aberto se praticar fato definido como crime doloso.', 'E',
  'Também se **frustrar os fins da execução** ou se, podendo, **não pagar a multa** cumulativamente aplicada (art. 36, § 2º).',
  lei=[(CP + '36', 'O condenado será transferido do regime aberto, se praticar fato definido como crime doloso', 'não pagar a multa cumulativamente aplicada', 'CP, art. 36, § 2º')],
  peg='Reduzir as hipóteses ao crime doloso.', kw=['frustrar os fins da execução'])
I(P, 1, 'Mulheres',
  'As mulheres cumprem pena em estabelecimento próprio, observados os deveres e direitos inerentes à sua condição pessoal.', 'C',
  'Art. 37 do CP; CF, art. 5º, XLVIII (estabelecimentos distintos conforme natureza do delito, idade e sexo).',
  lei=[(CP + '37', 'As mulheres cumprem pena em estabelecimento próprio', None, 'CP, art. 37')],
  kw=['estabelecimento próprio'])
# --- PEN-8.2 · Rodada 2
I(P, 2, 'Falta de vaga',
  'A falta de estabelecimento penal adequado autoriza manter o condenado em regime mais gravoso até o surgimento de vaga.', 'E',
  'A **Súmula Vinculante 56** veda isso: observam-se os parâmetros do RE 641.320 (saída antecipada, monitoração, domiciliar etc.).',
  juris=[J['SV56']], peg='Manter no regime mais grave por falta de vaga.', kw=['Súmula Vinculante 56'])
I(P, 2, 'Remição por trabalho e estudo',
  'O condenado em regime fechado ou semiaberto pode remir um dia de pena a cada três dias de trabalho ou a cada doze horas de frequência escolar, divididas em no mínimo três dias.', 'C',
  'É a **remição** da LEP, art. 126, § 1º: 1 dia por 12 horas de estudo (em ao menos 3 dias) ou por **três dias de trabalho**.',
  lei=[(LEP + '126', '1 (um) dia de pena a cada 12 (doze) horas de frequência escolar', '1 (um) dia de pena a cada 3 (três) dias de trabalho', 'LEP, art. 126, § 1º, I e II')],
  kw=['remição', 'três dias de trabalho'])
I(P, 2, 'Remição extramuros',
  'O trabalho externo (extramuros) do condenado em regime fechado ou semiaberto não gera remição, que exige trabalho intramuros.', 'E',
  'A **Súmula 562/STJ** admite a remição pelo trabalho **ainda que extramuros**.',
  juris=[J['S562']], peg='Exigir trabalho intramuros.', kw=['Súmula 562/STJ', 'extramuros'])
I(P, 2, 'Remição em prisão domiciliar',
  'O cumprimento da pena em regime domiciliar impede a remição, que pressupõe trabalho ou estudo em estabelecimento penal.', 'E',
  'Pela **Lei 15.402/2026**, o art. 126, § 9º, da LEP diz que o **regime domiciliar** **não impede** a remição.',
  lei=[(LEP + '126', 'O cumprimento da pena restritiva de liberdade em regime domiciliar não impede a remição da pena.', None, 'LEP, art. 126, § 9º')],
  kw=['regime domiciliar', 'Lei 15.402/2026'])
I(P, 2, 'Progressão: crimes contra a administração',
  'O condenado por crime contra a administração pública terá a progressão de regime condicionada à reparação do dano que causou ou à devolução do produto do ilícito.', 'C',
  'Art. 33, § 4º, do CP.',
  lei=[(CP + '33', 'O condenado por crime contra a administração pública terá a progressão de regime do cumprimento da pena condicionada à reparação do dano', None, 'CP, art. 33, § 4º')],
  kw=['administração pública', 'reparação do dano'])

# ======================= PEN-8.3 · Penas restritivas de direitos =======================
P = 'DBA26-PEN-8.3'
I(P, 1, 'Requisitos da substituição',
  'Cabe substituição da pena privativa por restritiva de direitos quando aplicada pena não superior a quatro anos, sem violência ou grave ameaça à pessoa, ou, qualquer que seja a pena, se o crime for culposo.', 'C',
  'Art. 44, I. Somam-se: não reincidência em crime **doloso** (II) e circunstâncias judiciais favoráveis (III).',
  lei=[SUBST], kw=['quatro anos', 'crime culposo'])
I(P, 1, 'Crime culposo e pena alta',
  'No crime culposo, a substituição por restritiva de direitos só é possível se a pena aplicada não superar quatro anos.', 'E',
  'No **culposo**, a substituição cabe "**qualquer que seja a pena aplicada**" (art. 44, I, parte final).',
  lei=[SUBST], peg='Aplicar o teto de 4 anos ao culposo.', kw=['qualquer que seja a pena'])
I(P, 1, 'Espécies',
  'São penas restritivas de direitos a prestação pecuniária, a perda de bens e valores, a prestação de serviço à comunidade, a interdição temporária de direitos e a limitação de fim de semana.', 'C',
  'Art. 43, I, II, IV, V e VI.',
  lei=[(CP + '43', 'prestação de serviço à comunidade ou a entidades públicas', None, 'CP, art. 43, IV'),
       (CP + '43', 'VI - limitação de fim de semana.', None, 'CP, art. 43, VI')],
  kw=['prestação pecuniária', 'limitação de fim de semana'])
I(P, 1, 'Prestação de serviços: pena mínima',
  'A prestação de serviços à comunidade é aplicável a qualquer condenação, ainda que inferior a seis meses de privação da liberdade.', 'E',
  'Art. 46, caput: só às condenações **superiores a seis meses**.',
  lei=[(CP + '46', 'A prestação de serviços à comunidade ou a entidades públicas é aplicável às condenações superiores a seis meses de privação da liberdade.', None, 'CP, art. 46, caput')],
  kw=['superiores a seis meses'])
I(P, 1, 'Prestação pecuniária: valores',
  'A prestação pecuniária consiste no pagamento em dinheiro à vítima, a seus dependentes ou a entidade com destinação social, não inferior a 1 nem superior a 360 salários mínimos.', 'C',
  'Art. 45, § 1º; o valor é **deduzido** de eventual condenação civil se coincidentes os beneficiários.',
  lei=[(CP + '45', 'A prestação pecuniária consiste no pagamento em dinheiro à vítima', 'trezentos e sessenta) salários mínimos', 'CP, art. 45, § 1º')],
  kw=['360 salários mínimos'])
I(P, 1, 'Reincidente',
  'O reincidente em crime doloso nunca pode ter a pena privativa substituída por restritiva de direitos.', 'E',
  'O § 3º do art. 44 permite a substituição ao **reincidente** se a medida for **socialmente recomendável** e a reincidência **não for no mesmo crime** (específica).',
  lei=[(CP + '44', 'Se o condenado for reincidente, o juiz poderá aplicar a substituição', 'não se tenha operado em virtude da prática do mesmo crime', 'CP, art. 44, § 3º')],
  peg='"Nunca" — esquecer o § 3º.', kw=['socialmente recomendável', 'mesmo crime'])
I(P, 1, 'Conversão',
  'A restritiva de direitos converte-se em privativa de liberdade quando ocorrer descumprimento injustificado, deduzido o tempo cumprido e respeitado o saldo mínimo de trinta dias.', 'C',
  'Art. 44, § 4º.',
  lei=[(CP + '44', 'A pena restritiva de direitos converte-se em privativa de liberdade quando ocorrer o descumprimento injustificado', 'saldo mínimo de trinta dias de detenção ou reclusão', 'CP, art. 44, § 4º')],
  kw=['conversão', 'trinta dias'])
I(P, 1, 'Violência doméstica',
  'A prática de crime ou contravenção contra a mulher com violência ou grave ameaça no ambiente doméstico impede a substituição da pena por restritiva de direitos.', 'C',
  '**Súmula 588/STJ**.',
  juris=[J['S588']], kw=['Súmula 588/STJ'])
# --- PEN-8.3 · Rodada 2
I(P, 2, 'Quantidade de restritivas',
  'Na condenação superior a um ano, a pena privativa pode ser substituída por uma restritiva de direitos e multa ou por duas restritivas de direitos.', 'C',
  'Art. 44, § 2º; até um ano, por multa **ou** uma restritiva.',
  lei=[(CP + '44', 'Na condenação igual ou inferior a um ano, a substituição pode ser feita por multa ou por uma pena restritiva de direitos', 'ou por duas restritivas de direitos', 'CP, art. 44, § 2º')],
  kw=['duas restritivas', 'um ano'])
I(P, 2, 'Execução da restritiva',
  'A pena restritiva de direitos pode ser executada logo após a condenação em segundo grau, antes do trânsito em julgado.', 'E',
  'A **Súmula 643/STJ** exige o **trânsito em julgado** da condenação.',
  juris=[J['S643']], peg='Execução provisória da restritiva.', kw=['Súmula 643/STJ', 'trânsito em julgado'])
I(P, 2, 'Substituição e regime aberto',
  'É inadmissível fixar pena substitutiva do art. 44 como condição especial do regime aberto.', 'C',
  '**Súmula 493/STJ**: seria dupla punição.',
  juris=[J['S493']], kw=['Súmula 493/STJ'])
I(P, 2, 'Interdição: concursos',
  'A proibição de inscrever-se em concurso, avaliação ou exame públicos é espécie de interdição temporária de direitos.', 'C',
  'Art. 47, V (Lei 12.550/2011).',
  lei=[(CP + '47', 'proibição de inscrever-se em concurso, avaliação ou exame públicos', None, 'CP, art. 47, V')],
  kw=['interdição temporária', 'concurso'])
I(P, 2, 'Limitação de fim de semana',
  'A limitação de fim de semana obriga o condenado a permanecer, aos sábados e domingos, por 8 horas diárias, em casa de albergado.', 'E',
  'São **5 horas diárias** (art. 48).',
  lei=[(CP + '48', 'A limitação de fim de semana consiste na obrigação de permanecer, aos sábados e domingos, por 5 (cinco) horas diárias', None, 'CP, art. 48, caput')],
  peg='Trocar o número de horas.', kw=['5 horas diárias'])

# ======================= PEN-8.4 · Regimes de pena =======================
P = 'DBA26-PEN-8.4'
I(P, 1, 'Regime fechado obrigatório',
  'O condenado a pena superior a 8 anos deverá começar a cumpri-la em regime fechado.', 'C',
  'Art. 33, § 2º, a.',
  lei=[(CP + '33', 'o condenado a pena superior a 8 (oito) anos deverá começar a cumpri-la em regime fechado', None, 'CP, art. 33, § 2º, a')],
  kw=['superior a 8 anos', 'regime fechado'])
I(P, 1, 'Semiaberto',
  'O condenado não reincidente cuja pena seja superior a 4 anos e não exceda a 8 deverá, obrigatoriamente, cumpri-la desde o início em regime semiaberto.', 'E',
  'O texto diz "**poderá**" (art. 33, § 2º, b): é o regime **máximo** possível ao primário nessa faixa; o juiz pode fixar mais grave com fundamentação concreta (Súmula 719/STF).',
  lei=[(CP + '33', 'o condenado não reincidente, cuja pena seja superior a 4 (quatro) anos e não exceda a 8 (oito), poderá, desde o princípio, cumpri-la em regime semi-aberto', None, 'CP, art. 33, § 2º, b')],
  peg='Trocar "poderá" por "deverá".', kw=['poderá', 'semiaberto'])
I(P, 1, 'Reincidente com pena até 4 anos',
  'É admissível o regime semiaberto ao reincidente condenado a pena igual ou inferior a quatro anos, se favoráveis as circunstâncias judiciais.', 'C',
  '**Súmula 269/STJ**.',
  juris=[J['S269']], kw=['Súmula 269/STJ'])
I(P, 1, 'Gravidade abstrata',
  'A gravidade em abstrato do crime, segundo a opinião do julgador, justifica a fixação de regime mais severo do que o permitido pela pena aplicada.', 'E',
  '**Súmulas 718 e 719/STF** e **440/STJ**: exige-se **motivação idônea** e concreta.',
  juris=[J['STF718'], J['S440']], peg='Fundamentar o regime na gravidade abstrata.', kw=['gravidade abstrata', 'motivação idônea'])
I(P, 1, 'Critérios do art. 59',
  'A determinação do regime inicial observa, além da quantidade de pena e da reincidência, os critérios do art. 59 do Código Penal.', 'C',
  'Art. 33, § 3º.',
  lei=[(CP + '33', 'A determinação do regime inicial de cumprimento da pena far-se-á com observância dos critérios previstos no art. 59 deste Código.', None, 'CP, art. 33, § 3º')],
  kw=['regime inicial', 'art. 59'])
# --- PEN-8.4 · Rodada 2
I(P, 2, 'Hediondos: regime',
  'Pela redação atual da Lei 8.072/1990, a pena por crime hediondo será cumprida integralmente em regime fechado.', 'E',
  'O § 1º do art. 2º fala em regime **inicialmente** fechado (Lei 11.464/2007). O "integralmente fechado" era a redação originária, cuja inconstitucionalidade a **SV 26** manda observar na progressão.',
  lei=[('L8072:2', 'A pena por crime previsto neste artigo será cumprida inicialmente em regime fechado.', None, 'Lei 8.072/1990, art. 2º, § 1º')],
  juris=[J['SV26']], peg='Trocar "inicialmente" por "integralmente".', kw=['inicialmente', 'Súmula Vinculante 26'])
I(P, 2, 'Soma de penas e regime',
  'Havendo condenação por mais de um crime, o regime é determinado pelo resultado da soma ou unificação das penas.', 'C',
  'LEP, art. 111: o regime resulta da **soma ou unificação** das penas, observada a detração ou remição; condenação nova no curso da execução soma-se ao restante.',
  lei=[(LEP + '111', 'Quando houver condenação por mais de um crime, no mesmo processo ou em processos distintos', 'observada, quando for o caso, a detração ou remição', 'LEP, art. 111, caput')],
  kw=['soma ou unificação'])
I(P, 2, 'Progressão per saltum',
  'O condenado em regime fechado pode progredir diretamente para o aberto se cumprir o dobro do tempo exigido.', 'E',
  'A **Súmula 491/STJ** veda a **progressão per saltum**.',
  juris=[J['S491']], peg='Admitir salto de regime.', kw=['Súmula 491/STJ', 'per saltum'])

# ======================= PEN-8.5 · Pena pecuniária =======================
P = 'DBA26-PEN-8.5'
I(P, 1, 'Dias-multa',
  'A pena de multa será, no mínimo, de 10 e, no máximo, de 360 dias-multa.', 'C',
  'Art. 49, caput.',
  lei=[MULTA], kw=['10', '360 dias-multa'])
I(P, 1, 'Valor do dia-multa',
  'O valor do dia-multa não pode ser inferior a um salário mínimo nem superior a dez vezes esse salário.', 'E',
  'O dia-multa vai de **1/30 do salário mínimo** a **5 vezes** esse salário (art. 49, § 1º), podendo a multa ser **triplicada** se ineficaz (art. 60, § 1º).',
  lei=[(CP + '49', 'O valor do dia-multa será fixado pelo juiz não podendo ser inferior a um trigésimo do maior salário mínimo', 'nem superior a 5 (cinco) vezes esse salário', 'CP, art. 49, § 1º')],
  peg='Trocar os limites.', kw=['um trigésimo', '5 vezes'])
I(P, 1, 'Multa como dívida de valor',
  'Transitada em julgado a sentença, a multa será executada perante o juiz da execução penal e considerada dívida de valor.', 'C',
  'Art. 51 (Lei 13.964/2019): aplica-se a legislação da dívida ativa, inclusive quanto às causas interruptivas e suspensivas da prescrição.',
  lei=[(CP + '51', 'Transitada em julgado a sentença condenatória, a multa será executada perante o juiz da execução penal e será considerada dívida de valor', None, 'CP, art. 51')],
  kw=['dívida de valor', 'juiz da execução penal'])
I(P, 1, 'Conversão da multa em prisão',
  'A multa não paga pelo condenado solvente converte-se em pena de detenção.', 'E',
  'A **conversão** da multa em prisão foi **revogada** (Lei 9.268/1996); hoje a multa é dívida de valor (art. 51).',
  lei=[(CP + '51', 'será considerada dívida de valor', None, 'CP, art. 51')],
  peg='Ressuscitar a conversão.', kw=['conversão revogada'])
I(P, 1, 'Situação econômica',
  'Na fixação da multa, o juiz deve atender principalmente à situação econômica do réu, podendo aumentá-la até o triplo se ineficaz, embora aplicada no máximo.', 'C',
  'Art. 60, caput e § 1º.',
  lei=[(CP + '60', 'Na fixação da pena de multa o juiz deve atender, principalmente, à situação econômica do réu.', None, 'CP, art. 60, caput'),
       (CP + '60', 'A multa pode ser aumentada até o triplo', None, 'CP, art. 60, § 1º')],
  kw=['situação econômica', 'triplo'])
# --- PEN-8.5 · Rodada 2
I(P, 2, 'Inadimplemento e extinção da punibilidade',
  'Cumprida a pena privativa de liberdade, o inadimplemento da multa por condenado hipossuficiente impede, em qualquer caso, a extinção da punibilidade.', 'E',
  'Pelo **Tema 931/STJ** (revisado em 2024), o inadimplemento **não obsta** a extinção ante a alegada hipossuficiência, **salvo** decisão motivada que indique concretamente a possibilidade de pagamento.',
  juris=[J['T931']], peg='"Em qualquer caso" — ignorar a tese revisada.', kw=['Tema 931/STJ', 'hipossuficiência'])
I(P, 2, 'Prescrição da multa isolada',
  'A prescrição da pena de multa ocorre em 2 anos quando ela for a única cominada ou aplicada.', 'C',
  'Art. 114, I; quando cumulada ou alternativa, segue o prazo da privativa (II).',
  lei=[(CP + '114', 'em 2 (dois) anos, quando a multa for a única cominada ou aplicada', None, 'CP, art. 114, I')],
  kw=['2 anos', 'única cominada'])
I(P, 2, 'Multa e doença mental',
  'Sobrevindo doença mental ao condenado, a execução da multa prossegue normalmente, por se tratar de dívida de valor.', 'E',
  'Art. 52: é **suspensa** a execução da multa se sobrevém doença mental.',
  lei=[(CP + '52', 'É suspensa a execução da pena de multa, se sobrevém ao condenado doença mental.', None, 'CP, art. 52')],
  peg='Ignorar a suspensão.', kw=['suspensa', 'doença mental'])
I(P, 2, 'Pagamento parcelado',
  'A multa deve ser paga em 10 dias do trânsito em julgado, mas o juiz pode permitir o pagamento em parcelas mensais.', 'C',
  'Art. 50, caput.',
  lei=[(CP + '50', 'A multa deve ser paga dentro de 10 (dez) dias depois de transitada em julgado a sentença.', 'em parcelas mensais', 'CP, art. 50, caput')],
  kw=['10 dias', 'parcelas mensais'])

# ======================= PEN-8.6 · Medidas de segurança =======================
P = 'DBA26-PEN-8.6'
I(P, 1, 'Espécies',
  'As medidas de segurança são a internação em hospital de custódia e tratamento psiquiátrico e a sujeição a tratamento ambulatorial.', 'C',
  'Art. 96, I e II.',
  lei=[(CP + '96', 'Internação em hospital de custódia e tratamento psiquiátrico', 'sujeição a tratamento ambulatorial', 'CP, art. 96, I e II')],
  kw=['internação', 'tratamento ambulatorial'])
I(P, 1, 'Detenção e ambulatorial',
  'Se o fato previsto como crime for punível com reclusão, o juiz pode submeter o inimputável a tratamento ambulatorial.', 'E',
  'Pela letra do art. 97, o ambulatorial é possível quando o fato é punível com **detenção**; na reclusão, a lei prevê **internação**.',
  lei=[(CP + '97', 'Se, todavia, o fato previsto como crime for punível com detenção, poderá o juiz submetê-lo a tratamento ambulatorial.', None, 'CP, art. 97, caput, 2ª parte')],
  peg='Trocar detenção por reclusão.', kw=['detenção', 'ambulatorial'])
I(P, 1, 'Prazo mínimo',
  'O prazo mínimo da internação ou do tratamento ambulatorial é de 3 a 5 anos.', 'E',
  'Art. 97, § 1º: a medida dura por **tempo indeterminado**, com prazo mínimo de **1 a 3 anos**.',
  lei=[(CP + '97', 'A internação, ou tratamento ambulatorial, será por tempo indeterminado', 'O prazo mínimo deverá ser de 1 (um) a 3 (três) anos.', 'CP, art. 97, § 1º')],
  kw=['tempo indeterminado', '1 a 3 anos'])
I(P, 1, 'Limite máximo',
  'Para o STJ, a duração da medida de segurança não deve ultrapassar o limite máximo da pena abstratamente cominada ao delito praticado.', 'C',
  '**Súmula 527/STJ**.',
  juris=[J['S527']], kw=['Súmula 527/STJ'])
I(P, 1, 'Perícia',
  'A perícia médica para verificar a cessação da periculosidade só pode ser realizada ao término do prazo mínimo fixado.', 'E',
  'Realiza-se ao termo do prazo mínimo e se repete **de ano em ano**, ou **a qualquer tempo**, se o juiz da execução determinar (art. 97, § 2º).',
  lei=[(CP + '97', 'A perícia médica realizar-se-á ao termo do prazo mínimo fixado', 'se o determinar o juiz da execução', 'CP, art. 97, § 2º')],
  peg='Apagar o "a qualquer tempo".', kw=['de ano em ano', 'a qualquer tempo'])
# --- PEN-8.6 · Rodada 2
I(P, 2, 'Desinternação condicional',
  'A desinternação do inimputável é definitiva, não podendo ser restabelecida a internação depois da liberação.', 'E',
  'Art. 97, § 3º: a desinternação é **sempre condicional**; restabelece-se a situação anterior se, antes de **1 ano**, o agente praticar fato indicativo de persistência da periculosidade.',
  lei=[(CP + '97', 'A desinternação, ou a liberação, será sempre condicional', 'persistência de sua periculosidade', 'CP, art. 97, § 3º')],
  kw=['sempre condicional', '1 ano'])
I(P, 2, 'Reformatio in pejus',
  'O tribunal pode aplicar medida de segurança em segunda instância, ainda que só o réu tenha recorrido.', 'E',
  '**Súmula 525/STF**: não se aplica medida de segurança em segunda instância quando **só o réu** recorreu.',
  juris=[J['STF525']], peg='Reformatio in pejus por medida de segurança.', kw=['Súmula 525/STF'])
I(P, 2, 'Conversão do ambulatorial',
  'Em qualquer fase do tratamento ambulatorial, o juiz pode determinar a internação, se necessária para fins curativos.', 'C',
  'Art. 97, § 4º.',
  lei=[(CP + '97', 'Em qualquer fase do tratamento ambulatorial, poderá o juiz determinar a internação do agente', None, 'CP, art. 97, § 4º')],
  kw=['internação', 'fins curativos'])

# ======================= PEN-8.7 · Aplicação da pena =======================
P = 'DBA26-PEN-8.7'
I(P, 1, 'Sistema trifásico',
  'A pena-base é fixada pelo art. 59; em seguida, consideram-se as atenuantes e agravantes; por último, as causas de diminuição e de aumento.', 'C',
  'É o **sistema trifásico** (Nélson Hungria), art. 68.',
  lei=[TRIF], kw=['sistema trifásico'])
I(P, 1, 'Atenuante abaixo do mínimo',
  'A incidência de circunstância atenuante pode conduzir a pena abaixo do mínimo legal, se houver mais de uma atenuante.', 'E',
  '**Súmula 231/STJ**: a atenuante **não** reduz a pena abaixo do mínimo legal (segunda fase).',
  juris=[J['S231']], peg='Romper o mínimo na segunda fase.', kw=['Súmula 231/STJ'])
I(P, 1, 'Inquéritos em curso',
  'Inquéritos policiais e ações penais em curso podem ser usados para agravar a pena-base como maus antecedentes.', 'E',
  '**Súmula 444/STJ**: é vedado. Maus antecedentes exigem condenação com trânsito em julgado (Tema 1.077/STJ).',
  juris=[J['S444'], J['T1077']], peg='Usar processos em curso como antecedentes.', kw=['Súmula 444/STJ'])
I(P, 1, 'Reincidência',
  'Verifica-se a reincidência quando o agente comete novo crime depois de transitar em julgado a sentença que, no País ou no estrangeiro, o tenha condenado por crime anterior.', 'C',
  'Art. 63; a sentença estrangeira **não precisa de homologação** para gerar reincidência.',
  lei=[(CP + '63', 'Verifica-se a reincidência quando o agente comete novo crime, depois de transitar em julgado a sentença', 'por crime anterior', 'CP, art. 63')],
  kw=['reincidência', 'trânsito em julgado'])
I(P, 1, 'Período depurador',
  'Não prevalece a condenação anterior, para efeito de reincidência, se entre o cumprimento ou extinção da pena e a infração posterior decorrer período superior a 5 anos.', 'C',
  'Art. 64, I: computa-se o período de prova do sursis e do livramento se não houver revogação.',
  lei=[(CP + '64', 'não prevalece a condenação anterior, se entre a data do cumprimento ou extinção da pena e a infração posterior', 'se não ocorrer revogação', 'CP, art. 64, I')],
  kw=['5 anos', 'período depurador'])
I(P, 1, 'Crime militar próprio',
  'Os crimes militares próprios e os políticos geram reincidência como qualquer outro crime.', 'E',
  'Art. 64, II: **não se consideram** para efeito de reincidência.',
  lei=[(CP + '64', 'não se consideram os crimes militares próprios e políticos', None, 'CP, art. 64, II')],
  peg='Contar militar próprio e político.', kw=['militares próprios e políticos'])
I(P, 1, 'Confissão espontânea',
  'Pela orientação atual do STJ, a confissão espontânea atenua a pena ainda que não tenha sido utilizada na formação do convencimento do julgador.', 'C',
  '**Súmula 545/STJ** revisada e **Tema 1.194/STJ** (10/09/2025): basta a confissão não retratada (ou retratada, se serviu à apuração).',
  juris=[J['S545'], J['T1194']], kw=['Súmula 545/STJ', 'Tema 1.194/STJ'])
# --- PEN-8.7 · Rodada 2
I(P, 2, 'Confissão: redação antiga',
  'Segundo a Súmula 545 do STJ, o réu só faz jus à atenuante da confissão quando ela for utilizada para a formação do convencimento do julgador.', 'E',
  'Essa era a **redação anterior**. Desde 10/09/2025 (Tema 1.194), a súmula diz que a confissão atenua **independentemente** de ser utilizada no convencimento.',
  juris=[J['S545']], peg='Cobrar a redação revisada como se valesse a antiga.', kw=['redação anterior', 'independentemente'])
I(P, 2, 'Compensação confissão x reincidência',
  'É possível compensar integralmente a atenuante da confissão com a agravante da reincidência, mas, na multirreincidência, prepondera a agravante, admitida a compensação proporcional.', 'C',
  '**Tema 585/STJ** (REsp 1.931.145/SP).',
  juris=[J['T585']], kw=['Tema 585/STJ', 'multirreincidência'])
I(P, 2, 'Fração da reincidência específica',
  'A reincidência específica, por si só, justifica sempre aumento de pena superior a um sexto na segunda fase.', 'E',
  '**Tema 1.172/STJ**: só em casos **excepcionais**, com fundamentação concreta e detalhada.',
  juris=[J['T1172']], peg='Automatizar fração maior.', kw=['Tema 1.172/STJ'])
I(P, 2, 'Condenação antiga',
  'Condenações transitadas em julgado não utilizadas para reincidência podem ser valoradas como maus antecedentes, mas não para desabonar a personalidade ou a conduta social.', 'C',
  '**Tema 1.077/STJ**.',
  juris=[J['T1077']], kw=['Tema 1.077/STJ', 'antecedentes'])
I(P, 2, 'Prova da reincidência',
  'A folha de antecedentes criminais é documento suficiente para comprovar maus antecedentes e reincidência, dispensando certidão cartorária.', 'C',
  '**Súmula 636/STJ**.',
  juris=[J['S636']], kw=['Súmula 636/STJ'])

# ======================= PEN-8.8 · Elementares e circunstâncias =======================
P = 'DBA26-PEN-8.8'
I(P, 1, 'Elementar x circunstância',
  'Elementares são dados essenciais do tipo cuja ausência leva à atipicidade ou à desclassificação; circunstâncias são dados acessórios que só influem na pena.', 'C',
  'A distinção entre **elementares** e **circunstâncias** é central para o art. 30 (comunicabilidade).',
  lei=[(CP + '30', 'Não se comunicam as circunstâncias e as condições de caráter pessoal, salvo quando elementares do crime.', None, 'CP, art. 30')],
  kw=['elementares', 'circunstâncias'])
I(P, 1, 'Agravantes e qualificadora',
  'As circunstâncias agravantes genéricas incidem mesmo quando já constituem ou qualificam o crime.', 'E',
  'O art. 61 diz que agravam a pena "**quando não constituem ou qualificam o crime**" — evita o bis in idem.',
  lei=[(CP + '61', 'São circunstâncias que sempre agravam a pena, quando não constituem ou qualificam o crime', None, 'CP, art. 61, caput')],
  peg='Duplicar qualificadora e agravante.', kw=['quando não constituem ou qualificam'])
I(P, 1, 'Agravante nova: instituição de ensino',
  'Constitui agravante genérica ter o agente cometido o crime nas dependências de instituição de ensino.', 'C',
  'Art. 61, II, m, **incluído pela Lei 15.159/2025**.',
  lei=[(CP + '61', 'nas dependências de instituição de ensino', None, 'CP, art. 61, II, m')],
  kw=['instituição de ensino', 'Lei 15.159/2025'])
I(P, 1, 'Agravante contra idoso',
  'É agravante genérica cometer o crime contra criança, maior de 70 anos, enfermo ou mulher grávida.', 'E',
  'A idade é **maior de 60 anos** (art. 61, II, h, redação do Estatuto do Idoso). O "maior de 70" é o da atenuante (art. 65, I, na data da sentença).',
  lei=[(CP + '61', 'contra criança, maior de 60 (sessenta) anos, enfermo ou mulher grávida', None, 'CP, art. 61, II, h')],
  peg='Trocar 60 por 70.', kw=['maior de 60 anos'])
I(P, 1, 'Circunstâncias preponderantes',
  'No concurso de agravantes e atenuantes, preponderam as que resultam dos motivos determinantes do crime, da personalidade do agente e da reincidência.', 'C',
  'Art. 67.',
  lei=[(CP + '67', 'No concurso de agravantes e atenuantes, a pena deve aproximar-se do limite indicado pelas circunstâncias preponderantes', 'da personalidade do agente e da reincidência', 'CP, art. 67')],
  kw=['circunstâncias preponderantes'])
# --- PEN-8.8 · Rodada 2
I(P, 2, 'Atenuante inominada',
  'A pena poderá ser atenuada em razão de circunstância relevante, anterior ou posterior ao crime, embora não prevista expressamente em lei.', 'C',
  'Art. 66 — **atenuante inominada** (base sugerida para a coculpabilidade).',
  lei=[(CP + '66', 'A pena poderá ser ainda atenuada em razão de circunstância relevante', None, 'CP, art. 66')],
  kw=['atenuante inominada'])
I(P, 2, 'Agravantes do concurso',
  'Agrava-se a pena de quem executa o crime mediante paga, mas não a de quem apenas participa dele mediante promessa de recompensa.', 'E',
  'Art. 62, IV: agrava-se a pena de quem "executa o crime, ou nele participa, mediante **paga ou promessa de recompensa**".',
  lei=[(CP + '62', 'executa o crime, ou nele participa, mediante paga ou promessa de recompensa', None, 'CP, art. 62, IV')],
  kw=['paga ou promessa de recompensa'])
I(P, 2, 'Reincidência como antecedente',
  'A reincidência pode ser valorada simultaneamente como agravante e como circunstância judicial negativa.', 'E',
  '**Súmula 241/STJ** veda.',
  juris=[J['S241']], peg='Bis in idem.', kw=['Súmula 241/STJ'])
I(P, 2, 'Privilégio e qualificadora objetiva',
  'É possível reconhecer o privilégio do furto no furto qualificado, se o agente for primário, a coisa de pequeno valor e a qualificadora for de ordem objetiva.', 'C',
  '**Súmula 511/STJ** (furto híbrido).',
  juris=[J['S511']], kw=['Súmula 511/STJ', 'furto híbrido'])

# ======================= PEN-8.9 · Causas de aumento e de diminuição =======================
P = 'DBA26-PEN-8.9'
I(P, 1, 'Terceira fase',
  'As causas de aumento e de diminuição incidem na terceira fase da dosimetria e podem levar a pena acima do máximo ou abaixo do mínimo cominados.', 'C',
  'Diferente das atenuantes/agravantes (Súmula 231/STJ), as **majorantes e minorantes** (frações) podem romper os limites — art. 68.',
  lei=[TRIF], kw=['terceira fase', 'romper os limites'])
I(P, 1, 'Concurso de causas na Parte Especial',
  'No concurso de causas de aumento ou de diminuição previstas na Parte Especial, o juiz deve aplicar obrigatoriamente todas elas, em cascata.', 'E',
  'O art. 68, par. ún., **faculta** ao juiz limitar-se a um só aumento ou a uma só diminuição, prevalecendo a que mais aumente ou diminua.',
  lei=[(CP + '68', 'No concurso de causas de aumento ou de diminuição previstas na parte especial, pode o juiz limitar-se a um só aumento ou a uma só diminuição', None, 'CP, art. 68, par. ún.')],
  peg='Trocar faculdade por obrigação.', kw=['pode o juiz limitar-se'])
I(P, 1, 'Roubo: número de majorantes',
  'No roubo circunstanciado, o aumento na terceira fase pode ser fixado acima do mínimo apenas pela indicação do número de majorantes.', 'E',
  '**Súmula 443/STJ**: exige **fundamentação concreta**.',
  juris=[J['S443']], peg='Critério aritmético.', kw=['Súmula 443/STJ'])
I(P, 1, 'Minorante da tentativa',
  'A tentativa é causa de diminuição de pena, aplicada na terceira fase.', 'C',
  'Art. 14, par. ún. (1/3 a 2/3).',
  lei=[(CP + '14', 'pune-se a tentativa com a pena correspondente ao crime consumado, diminuída de um a dois terços', None, 'CP, art. 14, par. ún.')],
  kw=['tentativa', 'causa de diminuição'])
I(P, 1, 'Qualificadora x majorante',
  'Qualificadora e causa de aumento são expressões sinônimas, ambas incidindo na terceira fase da dosimetria.', 'E',
  'A **qualificadora** altera os **limites** da pena em abstrato (novo mínimo e máximo) e define o ponto de partida da pena-base; a **majorante** é fração aplicada na terceira fase.',
  lei=[TRIF], peg='Igualar qualificadora e majorante.', kw=['qualificadora', 'majorante'])
# --- PEN-8.9 · Rodada 2
I(P, 2, 'Semi-imputabilidade como minorante',
  'A semi-imputabilidade é causa de diminuição de um a dois terços, aplicada na terceira fase.', 'C',
  'Art. 26, par. ún.',
  lei=[(CP + '26', 'A pena pode ser reduzida de um a dois terços, se o agente, em virtude de perturbação de saúde mental', None, 'CP, art. 26, par. ún.')],
  kw=['semi-imputabilidade', 'um a dois terços'])
I(P, 2, 'Concurso: aumento até metade',
  'Na cooperação dolosamente distinta, a pena do crime menos grave é aumentada até o dobro, se previsível o resultado mais grave.', 'E',
  'Aumento de **até metade** (art. 29, § 2º).',
  lei=[(CP + '29', 'essa pena será aumentada até metade, na hipótese de ter sido previsível o resultado mais grave', None, 'CP, art. 29, § 2º')],
  peg='Trocar a fração.', kw=['até metade'])
I(P, 2, 'Arrependimento posterior como minorante',
  'O arrependimento posterior é causa obrigatória de diminuição de pena de um a dois terços.', 'C',
  'Art. 16: "a pena **será** reduzida".',
  lei=[(CP + '16', 'a pena será reduzida de um a dois terços', None, 'CP, art. 16')],
  kw=['causa obrigatória', 'será reduzida'])

# ======================= PEN-8.10 · Fins da pena =======================
P = 'DBA26-PEN-8.10'
I(P, 1, 'Teoria mista',
  'O Código Penal adotou a teoria mista (unificadora) da pena, ao exigir que ela seja necessária e suficiente para a reprovação e a prevenção do crime.', 'C',
  'Art. 59, caput: **retribuição** (reprovação) + **prevenção**.',
  lei=[ART59], kw=['teoria mista', 'reprovação e prevenção'])
I(P, 1, 'Prevenção geral positiva',
  'A prevenção geral negativa busca reafirmar a vigência da norma e a confiança da sociedade no direito.', 'E',
  'Isso é a prevenção geral **positiva** (integradora). A **negativa** é a **intimidação** da coletividade.',
  lei=[ART59], peg='Trocar positiva por negativa.', kw=['prevenção geral negativa', 'intimidação'])
I(P, 1, 'Prevenção especial',
  'A prevenção especial dirige-se ao próprio condenado: na forma negativa, neutralizá-lo; na positiva, ressocializá-lo.', 'C',
  'A LEP adota a ressocialização: "harmônica integração social do condenado" (art. 1º).',
  lei=[('L7210:1', 'proporcionar condições para a harmônica integração social do condenado e do internado', None, 'LEP, art. 1º')],
  kw=['prevenção especial', 'ressocialização'])
I(P, 1, 'Teoria absoluta',
  'Para as teorias absolutas, a pena se justifica por sua utilidade social na prevenção de novos crimes.', 'E',
  'As **absolutas** (retributivas, Kant e Hegel) justificam a pena como **retribuição** do mal do crime; a utilidade preventiva é das teorias **relativas**.',
  lei=[ART59], peg='Trocar absoluta por relativa.', kw=['teorias absolutas', 'retribuição'])
I(P, 1, 'Fins na execução',
  'A execução penal tem por objetivo efetivar as disposições da sentença e proporcionar condições para a harmônica integração social do condenado.', 'C',
  'É o art. 1º da LEP: efetivar a sentença e proporcionar a **integração social** do condenado e do internado.',
  lei=[('L7210:1', 'A execução penal tem por objetivo efetivar as disposições de sentença ou decisão criminal', None, 'LEP, art. 1º')],
  kw=['integração social'])
# --- PEN-8.10 · Rodada 2
I(P, 2, 'Teoria dialética unificadora',
  'Para a teoria dialética unificadora, a pena cumpre fins distintos em cada fase: prevenção geral na cominação, retribuição limitada pela culpabilidade e prevenção na aplicação, e prevenção especial na execução.', 'C',
  'A **teoria dialética unificadora** é formulação doutrinária (Roxin) que dialoga com a individualização em três momentos (CF, art. 5º, XLVI).',
  lei=[('CF:5', 'a lei regulará a individualização da pena', None, 'CF, art. 5º, XLVI')],
  kw=['dialética unificadora'])
I(P, 2, 'Perdão judicial e desnecessidade',
  'O perdão judicial expressa a ideia de que, em certos casos, a pena se torna desnecessária, como quando as consequências do crime culposo atingem gravemente o próprio agente.', 'C',
  'Art. 121, § 5º — a pena perde sentido preventivo.',
  lei=[(CP + '121', 'o juiz poderá deixar de aplicar a pena, se as conseqüências da infração atingirem o próprio agente', None, 'CP, art. 121, § 5º')],
  kw=['perdão judicial', 'desnecessária'])
I(P, 2, 'Prevenção geral e regime',
  'A gravidade abstrata do delito, ligada à prevenção geral, é fundamento suficiente para impor regime mais severo do que o permitido pela pena.', 'E',
  '**Súmula 718/STF**: a opinião sobre a gravidade em abstrato não é motivação idônea.',
  juris=[J['STF718']], peg='Usar prevenção geral abstrata no regime.', kw=['Súmula 718/STF'])

# ======================= PEN-8.11 · Livramento condicional e sursis =======================
P = 'DBA26-PEN-8.11'
I(P, 1, 'Sursis: requisitos',
  'A execução da pena privativa de liberdade não superior a 2 anos pode ser suspensa por 2 a 4 anos, desde que o condenado não seja reincidente em crime doloso e não seja cabível a substituição do art. 44.', 'C',
  'Art. 77, caput, I a III: o **sursis** é **subsidiário** à substituição por restritivas.',
  lei=[SURSIS, (CP + '77', 'Não seja indicada ou cabível a substituição prevista no art. 44 deste Código.', None, 'CP, art. 77, III')],
  kw=['sursis', 'subsidiário'])
I(P, 1, 'Sursis etário e humanitário',
  'O sursis etário alcança pena não superior a 4 anos, com período de prova de 2 a 4 anos, para o condenado maior de 60 anos.', 'E',
  'Art. 77, § 2º: período de prova de **quatro a seis anos** e condenado **maior de setenta anos** (ou razões de saúde) — é o **sursis etário**.',
  lei=[(CP + '77', 'A execução da pena privativa de liberdade, não superior a quatro anos, poderá ser suspensa, por quatro a seis anos', None, 'CP, art. 77, § 2º')],
  kw=['sursis etário', 'quatro a seis anos'])
I(P, 1, 'Condenação anterior a multa',
  'A condenação anterior a pena de multa impede a concessão do sursis.', 'E',
  'Art. 77, § 1º: **não impede**.',
  lei=[(CP + '77', 'A condenação anterior a pena de multa não impede a concessão do benefício.', None, 'CP, art. 77, § 1º')],
  peg='Ver obstáculo na multa anterior.', kw=['não impede'])
I(P, 1, 'Sursis e restritivas',
  'A suspensão condicional da pena estende-se às penas restritivas de direitos e à multa.', 'E',
  'Art. 80: a suspensão **não se estende** às restritivas nem à multa.',
  lei=[(CP + '80', 'A suspensão não se estende às penas restritivas de direitos nem à multa.', None, 'CP, art. 80')],
  peg='Estender o sursis à multa.', kw=['não se estende'])
I(P, 1, 'Revogação obrigatória do sursis',
  'A suspensão será revogada se, no curso do prazo, o beneficiário for condenado em sentença irrecorrível por crime doloso.', 'C',
  'Art. 81, I (revogação **obrigatória**). Crime culposo ou contravenção geram revogação **facultativa** (§ 1º).',
  lei=[(CP + '81', 'A suspensão será revogada se, no curso do prazo, o beneficiário:', 'é condenado, em sentença irrecorrível, por crime doloso', 'CP, art. 81, caput e I')],
  kw=['revogação obrigatória', 'crime doloso'])
I(P, 1, 'Livramento: frações',
  'O livramento condicional exige o cumprimento de mais de um terço da pena se o condenado não for reincidente em crime doloso e tiver bons antecedentes, e de mais da metade se reincidente em crime doloso.', 'C',
  'Art. 83, I e II; pena aplicada **igual ou superior a 2 anos**.',
  lei=[LC, (CP + '83', 'cumprida mais de um terço da pena se o condenado não for reincidente em crime doloso e tiver bons antecedentes', 'cumprida mais da metade se o condenado for reincidente em crime doloso', 'CP, art. 83, I e II')],
  kw=['mais de um terço', 'mais da metade'])
I(P, 1, 'Livramento: falta grave recente',
  'Para o livramento condicional, exige-se comprovado bom comportamento e não cometimento de falta grave nos últimos 24 meses.', 'E',
  'São os **últimos 12 meses** (art. 83, III, b, Lei 13.964/2019).',
  lei=[(CP + '83', 'não cometimento de falta grave nos últimos 12 (doze) meses', None, 'CP, art. 83, III, b')],
  peg='Trocar 12 por 24 meses.', kw=['12 meses', 'falta grave'])
I(P, 1, 'Livramento nos hediondos',
  'Nos crimes hediondos, tortura, tráfico de drogas, tráfico de pessoas e terrorismo, o livramento exige mais de dois terços da pena, se o apenado não for reincidente específico.', 'C',
  'Art. 83, V. Atenção: a LEP **veda** o livramento em hipóteses do art. 112, VI, a, b e d, e VIII (hediondo com morte, comando de organização ultraviolenta, feminicídio e reincidente em hediondo com morte).',
  lei=[(CP + '83', 'cumpridos mais de dois terços da pena, nos casos de condenação por crime hediondo', 'se o apenado não for reincidente específico em crimes dessa natureza', 'CP, art. 83, V')],
  exc=['Vedação de livramento: LEP, art. 112, VI, a, b e d, e VIII (redação de 2019 e da Lei 15.358/2026)'],
  kw=['dois terços', 'reincidente específico'])
# --- PEN-8.11 · Rodada 2
I(P, 2, 'Falta grave e livramento',
  'A falta grave interrompe o prazo para obtenção do livramento condicional.', 'E',
  '**Súmula 441/STJ**: **não interrompe** (mas pode impedir o requisito do art. 83, III, b, nos 12 meses).',
  juris=[J['S441']], peg='Confundir com a progressão (que é interrompida).', kw=['Súmula 441/STJ'])
I(P, 2, 'Fim do período de prova',
  'Se o livramento não for suspenso ou revogado até o término do período de prova, extingue-se a pena pelo integral cumprimento.', 'C',
  '**Súmula 617/STJ** e art. 90 do CP.',
  juris=[J['S617']], lei=[(CP + '90', 'Se até o seu término o livramento não é revogado, considera-se extinta a pena privativa de liberdade.', None, 'CP, art. 90')],
  kw=['Súmula 617/STJ'])
I(P, 2, 'Revogação do livramento e desconto',
  'Revogado o livramento por crime cometido durante sua vigência, desconta-se da pena o tempo em que o condenado esteve solto.', 'E',
  'Art. 88: só se desconta quando a revogação resulta de condenação por crime **anterior** ao benefício; por crime **durante** a vigência, **não** se desconta e o benefício não pode ser novamente concedido.',
  lei=[(CP + '88', 'Revogado o livramento, não poderá ser novamente concedido', 'não se desconta na pena o tempo em que esteve solto o condenado', 'CP, art. 88')],
  peg='Descontar o tempo solto em revogação por crime durante o livramento.', kw=['não se desconta'])
I(P, 2, 'Prorrogação do sursis',
  'Se o beneficiário do sursis está sendo processado por outro crime ou contravenção, considera-se prorrogado o prazo da suspensão até o julgamento definitivo.', 'C',
  'Art. 81, § 2º.',
  lei=[(CP + '81', 'Se o beneficiário está sendo processado por outro crime ou contravenção, considera-se prorrogado o prazo da suspensão até o julgamento definitivo.', None, 'CP, art. 81, § 2º')],
  kw=['prorrogado'])
I(P, 2, 'Soma de penas no livramento',
  'Para o livramento condicional, cada pena é considerada isoladamente, vedada a soma das penas de infrações diversas.', 'E',
  'Art. 84: as penas de infrações diversas **devem somar-se** para efeito do livramento.',
  lei=[(CP + '84', 'As penas que correspondem a infrações diversas devem somar-se para efeito do livramento.', None, 'CP, art. 84')],
  kw=['somar-se'])

# ======================= PEN-8.12 · Efeitos da condenação =======================
P = 'DBA26-PEN-8.12'
I(P, 1, 'Efeitos genéricos',
  'São efeitos automáticos da condenação tornar certa a obrigação de indenizar e a perda, em favor da União, dos instrumentos ilícitos e do produto ou proveito do crime, ressalvado o direito do lesado ou do terceiro de boa-fé.', 'C',
  'Art. 91: **genéricos** e automáticos (não precisam ser declarados).',
  lei=[(CP + '91', 'São efeitos da condenação:', 'ressalvado o direito do lesado ou de terceiro de boa-fé', 'CP, art. 91, I e II')],
  kw=['efeitos genéricos', 'automáticos'])
I(P, 1, 'Perda do cargo: um ano',
  'A perda de cargo, função pública ou mandato eletivo é efeito da condenação a pena privativa por tempo igual ou superior a um ano nos crimes com abuso de poder ou violação de dever para com a Administração.', 'C',
  'Art. 92, I, a; nos demais casos, pena **superior a 4 anos** (b).',
  lei=[(CP + '92', 'quando aplicada pena privativa de liberdade por tempo igual ou superior a um ano', 'violação de dever para com a Administração Pública', 'CP, art. 92, I, a')],
  kw=['igual ou superior a um ano', 'perda de cargo'])
I(P, 1, 'Efeitos específicos: regra',
  'Os efeitos do art. 92 do Código Penal são, em regra, automáticos e independem de motivação na sentença.', 'E',
  'Pelo **§ 1º do art. 92** (Lei 14.994/2024) **não são automáticos**: devem ser **motivadamente declarados** na sentença, embora independam de pedido da acusação.',
  lei=[(CP + '92', 'Os efeitos de que trata este artigo não são automáticos, devendo ser motivadamente declarados na sentença pelo juiz', 'independem de pedido expresso da acusação', 'CP, art. 92, § 1º')],
  exc=['Crimes contra a mulher por razões da condição do sexo feminino e certos crimes sexuais contra criança/adolescente do ECA: efeitos dos incisos I e II AUTOMÁTICOS (art. 92, § 2º, III)'],
  peg='Inverter a regra.', kw=['não são automáticos', 'motivadamente declarados'])
I(P, 1, 'Inabilitação para dirigir',
  'A inabilitação para dirigir veículo é efeito da condenação nos crimes culposos de trânsito.', 'E',
  'Art. 92, III: a **inabilitação para dirigir** exige veículo usado como meio para **crime doloso**. Nos culposos de trânsito cabe a suspensão da habilitação como interdição temporária (arts. 47, III, e 57).',
  lei=[(CP + '92', 'a inabilitação para dirigir veículo, quando utilizado como meio para a prática de crime doloso', None, 'CP, art. 92, III')],
  kw=['inabilitação para dirigir', 'crime doloso'])
I(P, 1, 'Perda alargada',
  'Na condenação por infração com pena máxima superior a 6 anos de reclusão, pode ser decretada a perda dos bens correspondentes à diferença entre o patrimônio do condenado e o compatível com seu rendimento lícito.', 'C',
  'É o **confisco alargado** (art. 91-A, Lei 13.964/2019); exige **requerimento expresso do MP** na denúncia (§ 3º).',
  lei=[(CP + '91-A', 'Na hipótese de condenação por infrações às quais a lei comine pena máxima superior a 6 (seis) anos de reclusão', 'compatível com o seu rendimento lícito', 'CP, art. 91-A, caput')],
  kw=['confisco alargado', '6 anos'])
I(P, 1, 'Confisco alargado de ofício',
  'O juiz pode decretar de ofício a perda alargada de bens na sentença, mesmo sem requerimento do Ministério Público.', 'E',
  'O § 3º do art. 91-A exige que a perda seja **requerida expressamente pelo MP** por ocasião do oferecimento da denúncia, com indicação da diferença apurada.',
  lei=[(CP + '91-A', 'A perda prevista neste artigo deverá ser requerida expressamente pelo Ministério Público, por ocasião do oferecimento da denúncia', None, 'CP, art. 91-A, § 3º')],
  peg='Confisco alargado de ofício.', kw=['requerida expressamente'])
# --- PEN-8.12 · Rodada 2
I(P, 2, 'Efeitos automáticos: violência contra a mulher',
  'Ao condenado por crime praticado contra a mulher por razões da condição do sexo feminino, a perda do cargo e a incapacidade para o poder familiar são efeitos automáticos.', 'C',
  'Art. 92, § 2º, I e III (Lei 14.994/2024; caput do § 2º com redação da **Lei 15.487/2026**, que estendeu o regime a crimes sexuais do ECA contra criança e adolescente).',
  lei=[(CP + '92', 'automáticos os efeitos dos incisos I e II do caput e do inciso II do § 2º deste artigo', None, 'CP, art. 92, § 2º, III')],
  kw=['efeitos automáticos', 'condição do sexo feminino'])
I(P, 2, 'Vedação de nomeação',
  'Ao condenado por feminicídio fica vedada a nomeação, designação ou diplomação em cargo, função pública ou mandato eletivo entre o trânsito em julgado e o efetivo cumprimento da pena.', 'C',
  'Art. 92, § 2º, II (Lei 14.994/2024).',
  lei=[(CP + '92', 'vedadas a sua nomeação, designação ou diplomação em qualquer cargo, função pública ou mandato eletivo', None, 'CP, art. 92, § 2º, II')],
  kw=['vedadas a sua nomeação'])
I(P, 2, 'CNPJ e receptação',
  'É efeito da condenação a suspensão, por 180 dias, da inscrição no CNPJ do estabelecimento utilizado para permitir, facilitar ou ocultar a receptação.', 'C',
  'Art. 92, IV, **incluído pela Lei 15.358/2026**; na reincidência, inaptidão do CNPJ e interdição do administrador por 5 anos (§§ 3º e 4º).',
  lei=[(CP + '92', 'a suspensão, pelo prazo de 180 (cento e oitenta) dias, da eficácia da inscrição no Cadastro Nacional da Pessoa Jurídica', None, 'CP, art. 92, IV')],
  kw=['CNPJ', 'Lei 15.358/2026'])
I(P, 2, 'Indulto e efeitos secundários',
  'O indulto extingue também os efeitos secundários da condenação, como a reincidência.', 'E',
  '**Súmula 631/STJ**: atinge só os efeitos **primários**.',
  juris=[J['S631']], peg='Estender o indulto aos efeitos secundários.', kw=['Súmula 631/STJ'])
I(P, 2, 'Instrumentos de organizações criminosas',
  'Os instrumentos usados por organizações criminosas e milícias devem ser declarados perdidos em favor da União, do Estado ou do Distrito Federal, ainda que não ponham em perigo a segurança das pessoas.', 'C',
  'Art. 91-A, § 5º, na **redação da Lei 15.358/2026** (o destino segue a Justiça onde tramita a ação).',
  lei=[(CP + '91-A', 'Os instrumentos utilizados para a prática de crimes por organizações criminosas e milícias deverão ser declarados perdidos', 'dependendo da Justiça onde tramita a ação penal', 'CP, art. 91-A, § 5º')],
  kw=['organizações criminosas', 'perdidos'])

# ======================= PEN-8.13 · Execução penal =======================
P = 'DBA26-PEN-8.13'
I(P, 1, 'Progressão: regra geral',
  'Pela redação vigente da LEP, a progressão exige, como regra, o cumprimento de ao menos 1/6 da pena no regime anterior e mérito, observadas as exceções percentuais.', 'C',
  'Art. 112, caput, na **redação da Lei 15.402/2026**, com os percentuais dos incisos (ex.: 25% primário com violência; 70% hediondo primário).',
  lei=[(LEP + '112', 'A pena privativa de liberdade será executada de forma progressiva com a transferência para regime menos rigoroso', 'observadas as seguintes exceções', 'LEP, art. 112, caput')],
  kw=['1/6', 'Lei 15.402/2026'])
I(P, 1, 'Hediondo primário',
  'O condenado primário por crime hediondo ou equiparado progride após cumprir 40% da pena.', 'E',
  'Pela **Lei 15.358/2026**, o inciso V passou a exigir **70%** para o primário condenado por hediondo ou equiparado (o antigo 40% é redação superada).',
  lei=[(LEP + '112', 'V - 70% (setenta por cento) da pena, se o apenado for condenado pela prática de crime hediondo ou equiparado, se for primário', None, 'LEP, art. 112, V')],
  peg='Cobrar o percentual de 2019 como vigente.', kw=['70%', 'Lei 15.358/2026'])
I(P, 1, 'Exame criminológico',
  'Em todos os casos, a progressão exige boa conduta carcerária comprovada pelo diretor e os resultados do exame criminológico.', 'C',
  'Art. 112, § 1º, na redação da **Lei 14.843/2024**, que tornou o exame criminológico requisito.',
  lei=[(LEP + '112', 'Em todos os casos, o apenado somente terá direito à progressão de regime se ostentar boa conduta carcerária', 'pelos resultados do exame criminológico', 'LEP, art. 112, § 1º')],
  kw=['exame criminológico', 'Lei 14.843/2024'])
I(P, 1, 'Falta grave e progressão',
  'O cometimento de falta grave interrompe o prazo para a progressão, reiniciando-se a contagem com base na pena remanescente.', 'C',
  'LEP, art. 112, § 6º, e **Súmula 534/STJ**.',
  lei=[(LEP + '112', 'O cometimento de falta grave durante a execução da pena privativa de liberdade interrompe o prazo', 'terá como base a pena remanescente', 'LEP, art. 112, § 6º')],
  juris=[J['S534']], kw=['falta grave', 'pena remanescente'])
I(P, 1, 'Falta grave e indulto',
  'A prática de falta grave interrompe o prazo para fins de comutação de pena e indulto.', 'E',
  '**Súmula 535/STJ**: **não interrompe**.',
  juris=[J['S535']], peg='Estender a interrupção ao indulto.', kw=['Súmula 535/STJ'])
I(P, 1, 'Saída temporária',
  'Não terá direito à saída temporária o condenado que cumpre pena por crime hediondo ou com violência ou grave ameaça contra pessoa.', 'C',
  'LEP, art. 122, § 2º (Lei 14.843/2024), que também restringiu a saída temporária à frequência a curso.',
  lei=[(LEP + '122', 'Não terá direito à saída temporária de que trata o caput deste artigo ou a trabalho externo sem vigilância direta', None, 'LEP, art. 122, § 2º')],
  kw=['saída temporária', 'Lei 14.843/2024'])
# --- PEN-8.13 · Rodada 2
I(P, 2, 'Feminicídio e progressão',
  'O condenado primário por feminicídio progride após cumprir 75% da pena, vedado o livramento condicional.', 'C',
  'LEP, art. 112, VI, d, **incluído pela Lei 15.358/2026**.',
  lei=[(LEP + '112', 'condenado pela prática de feminicídio, se for primário, vedado o livramento condicional', None, 'LEP, art. 112, VI, d')],
  kw=['feminicídio', '75%'])
I(P, 2, 'Tráfico privilegiado',
  'O tráfico privilegiado do art. 33, § 4º, da Lei de Drogas é considerado equiparado a hediondo para fins de progressão.', 'E',
  'LEP, art. 112, § 5º: **não se considera** hediondo ou equiparado.',
  lei=[(LEP + '112', 'Não se considera hediondo ou equiparado, para os fins deste artigo, o crime de tráfico de drogas previsto no § 4º do art. 33', None, 'LEP, art. 112, § 5º')],
  peg='Hediondez do tráfico privilegiado.', kw=['tráfico privilegiado'])
I(P, 2, 'Falta grave sem trânsito',
  'O reconhecimento de falta grave decorrente de crime doloso no cumprimento da pena exige o trânsito em julgado da condenação pelo novo crime.', 'E',
  '**Súmula 526/STJ**: **prescinde** do trânsito em julgado.',
  juris=[J['S526']], peg='Exigir trânsito para a falta grave.', kw=['Súmula 526/STJ'])
I(P, 2, 'Mãe ou responsável',
  'A mulher gestante, mãe ou responsável por criança ou pessoa com deficiência pode progredir após 1/8 da pena, entre outros requisitos cumulativos, como não ter cometido crime com violência ou grave ameaça.', 'C',
  'LEP, art. 112, § 3º (Lei 13.769/2018): requisitos **cumulativos**, entre eles **1/8** da pena, primariedade, bom comportamento e não integrar organização criminosa; nova falta grave revoga o benefício (§ 4º).',
  lei=[(LEP + '112', 'ter cumprido ao menos 1/8 (um oitavo) da pena no regime anterior', None, 'LEP, art. 112, § 3º, III')],
  kw=['1/8', 'gestante'])
I(P, 2, 'RDD: duração',
  'O regime disciplinar diferenciado tem duração máxima de 360 dias, vedada a repetição da sanção.', 'E',
  'Desde a Lei 13.964/2019, o **RDD** dura até **2 anos** (LEP, art. 52, I), sem prejuízo de repetição por nova falta grave da mesma espécie.',
  lei=[(LEP + '52', 'duração máxima de até 2 (dois) anos, sem prejuízo de repetição da sanção por nova falta grave de mesma espécie', None, 'LEP, art. 52, I')],
  kw=['RDD', '2 anos'])
I(P, 2, 'Lei mais benigna na execução',
  'Após o trânsito em julgado, a aplicação da lei mais benigna compete ao tribunal que proferiu a última decisão.', 'E',
  'Compete ao **juízo das execuções** (**Súmula 611/STF**; LEP, art. 66, I).',
  juris=[J['STF611']], peg='Deslocar a competência para o tribunal.', kw=['Súmula 611/STF'])
