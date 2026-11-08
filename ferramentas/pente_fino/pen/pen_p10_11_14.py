# Pente Fino de Direito Penal (Parte Especial) — PEN-10.11 (fé pública), 10.12 (administração pública), 10.13
# (finanças públicas) e 10.14 (Estado Democrático de Direito) (08/11/2026).
from base import I
from pen_juris import J

CP = 'CP:'

# ======================= PEN-10.11 · Crimes contra a fé pública =======================
P = 'DBA26-PEN-10.11'
I(P, 1, 'Moeda falsa',
  'Falsificar moeda metálica ou papel-moeda de curso legal no país ou no estrangeiro é punido com reclusão de três a doze anos, e multa.', 'C',
  'Art. **289**, caput; o § 1º pune quem importa, guarda ou introduz na circulação moeda falsa.',
  lei=[(CP + '289', 'Art. 289 - Falsificar, fabricando-a ou alterando-a, moeda metálica ou papel-moeda de curso legal no país ou no estrangeiro:', 'Pena - reclusão, de três a doze anos, e multa.', 'CP, art. 289, caput')],
  kw=['289'])
I(P, 1, 'Falsificação grosseira',
  'A utilização de papel-moeda grosseiramente falsificado configura o crime de moeda falsa, de competência da Justiça Federal.', 'E',
  '**Súmula 73/STJ**: falsificação grosseira não engana o homem médio e não ofende a fé pública — configura, em tese, **estelionato**, da competência da **Justiça Estadual**.',
  juris=[J['S73']], peg='Manter a moeda falsa na falsificação grosseira.', kw=['Súmula 73/STJ'])
I(P, 1, 'Moeda recebida de boa-fé',
  'Quem recebe de boa-fé moeda falsa como verdadeira e a restitui à circulação depois de conhecer a falsidade responde por forma privilegiada, punida com detenção.', 'C',
  'Art. 289, **§ 2º**: detenção de 6 meses a 2 anos, e multa.',
  lei=[(CP + '289', '§ 2º - Quem, tendo recebido de boa-fé, como verdadeira, moeda falsa ou alterada, a restitui à circulação', None, 'CP, art. 289, § 2º')],
  kw=['§ 2º', 'boa-fé'])
I(P, 1, 'Cartão de crédito',
  'Para efeitos penais, o cartão de crédito ou débito equipara-se a documento público.', 'E',
  'Equipara-se a documento **particular** (art. 298, par. ún.). Equiparam-se a público, entre outros, o título ao portador ou transmissível por endosso, os livros mercantis e o testamento particular (art. 297, § 2º).',
  lei=[(CP + '298', 'Parágrafo único. Para fins do disposto no caput, equipara-se a documento particular o cartão de crédito ou débito.', None, 'CP, art. 298, par. ún.')],
  peg='Equiparar o cartão a documento público.', kw=['documento particular'])
I(P, 1, 'Falsidade ideológica',
  'A falsidade ideológica consiste em omitir declaração que devia constar de documento ou nele inserir declaração falsa, com o fim de prejudicar direito, criar obrigação ou alterar a verdade sobre fato juridicamente relevante.', 'C',
  'Art. **299**: o documento é materialmente verdadeiro, o **conteúdo** é falso (na falsidade material, arts. 297 e 298, é a forma que é falsa).',
  lei=[(CP + '299', 'Art. 299 - Omitir, em documento público ou particular, declaração que dele devia constar', 'alterar a verdade sobre fato juridicamente relevante:', 'CP, art. 299, caput')],
  kw=['conteúdo'])
I(P, 1, 'Falso e estelionato',
  'Quando o falso se exaure no estelionato, sem mais potencialidade lesiva, há concurso material entre falsificação e estelionato.', 'E',
  '**Súmula 17/STJ**: o falso é **absorvido** pelo estelionato (consunção).',
  juris=[J['S17']], peg='Somar as penas.', kw=['Súmula 17/STJ', 'absorvido'])
I(P, 1, 'Falsa identidade e autodefesa',
  'É típica a conduta de atribuir-se falsa identidade perante a autoridade policial, ainda que para evitar a própria prisão.', 'C',
  '**Súmula 522/STJ**: a autodefesa não alcança mentir sobre a identidade (art. 307).',
  lei=[(CP + '307', 'Art. 307 - Atribuir-se ou atribuir a terceiro falsa identidade para obter vantagem', None, 'CP, art. 307')],
  juris=[J['S522']], kw=['Súmula 522/STJ', 'autodefesa'])
I(P, 1, 'Uso de documento falso',
  'O uso de documento falso tem pena própria, inferior à da falsificação.', 'E',
  'Art. 304: a pena é **a cominada à falsificação** ou à alteração do papel usado.',
  lei=[(CP + '304', 'Art. 304 - Fazer uso de qualquer dos papéis falsificados ou alterados', 'Pena - a cominada à falsificação ou à alteração.', 'CP, art. 304')],
  peg='Atribuir pena autônoma ao uso.', kw=['a cominada à falsificação'])
I(P, 1, 'Sinal identificador de veículo',
  'Adulterar, remarcar ou suprimir placa de identificação de veículo automotor configura o crime do art. 311 do Código Penal.', 'C',
  'Art. **311** (Lei 14.562/2023 incluiu expressamente a placa, os veículos elétricos e híbridos e os reboques); reclusão de 3 a 6 anos.',
  lei=[(CP + '311', 'Art. 311. Adulterar, remarcar ou suprimir número de chassi, monobloco, motor, placa de identificação', None, 'CP, art. 311, caput')],
  kw=['311'])
# --- PEN-10.11 · Rodada 2
I(P, 2, 'Atestado médico falso',
  'O médico que, no exercício da profissão, dá atestado falso é punido com reclusão.', 'E',
  'Art. 302: **detenção** de 1 mês a 1 ano (multa se há fim de lucro).',
  lei=[(CP + '302', 'Art. 302 - Dar o médico, no exercício da sua profissão, atestado falso:', 'Pena - detenção, de um mês a um ano.', 'CP, art. 302')],
  peg='Trocar detenção por reclusão.', kw=['detenção'])
I(P, 2, 'Fraude em certame',
  'Na fraude em certames de interesse público, a pena aumenta-se de um terço se o fato é cometido por funcionário público.', 'C',
  'Art. 311-A, **§ 3º** (Lei 12.550/2011).',
  lei=[(CP + '311-A', '§ 3o Aumenta-se a pena de 1/3 (um terço) se o fato é cometido por funcionário público.', None, 'CP, art. 311-A, § 3º')],
  kw=['§ 3º'])
I(P, 2, 'Funcionário e documento público',
  'Se o funcionário público falsifica documento público prevalecendo-se do cargo, a pena aumenta-se de um terço.', 'E',
  'Art. 297, § 1º: aumento de **sexta parte**.',
  lei=[(CP + '297', '§ 1º - Se o agente é funcionário público, e comete o crime prevalecendo-se do cargo, aumenta-se a pena de sexta parte.', None, 'CP, art. 297, § 1º')],
  peg='Errar a fração.', kw=['sexta parte'])
I(P, 2, 'Documentos equiparados',
  'Para os efeitos penais, os livros mercantis e o testamento particular equiparam-se a documento público.', 'C',
  'Art. 297, **§ 2º**.',
  lei=[(CP + '297', '§ 2º - Para os efeitos penais, equiparam-se a documento público o emanado de entidade paraestatal', 'os livros mercantis e o testamento particular.', 'CP, art. 297, § 2º')],
  kw=['§ 2º'])
I(P, 2, 'Uso de documento alheio',
  'Usar como próprio passaporte ou documento de identidade alheio configura a falsa identidade do art. 307.', 'E',
  'É tipo **próprio**, o art. **308** (detenção de 4 meses a 2 anos, e multa), que também pune quem cede o documento.',
  lei=[(CP + '308', 'Art. 308 - Usar, como próprio, passaporte, título de eleitor, caderneta de reservista ou qualquer documento de identidade alheia', None, 'CP, art. 308')],
  peg='Confundir os arts. 307 e 308.', kw=['308'])
I(P, 2, 'Veículo adulterado',
  'Incorre nas penas do art. 311 quem adquire, recebe, conduz ou utiliza veículo com sinal identificador que devesse saber estar adulterado ou remarcado.', 'C',
  'Art. 311, **§ 2º, III** (Lei 14.562/2023).',
  lei=[(CP + '311', 'III – aquele que adquire, recebe, transporta, conduz, oculta, mantém em depósito', 'que devesse saber estar adulterado ou remarcado.', 'CP, art. 311, § 2º, III')],
  kw=['§ 2º, III'])

# ======================= PEN-10.12 · Crimes contra a administração pública =======================
P = 'DBA26-PEN-10.12'
I(P, 1, 'Funcionário público',
  'Considera-se funcionário público, para os efeitos penais, quem, embora transitoriamente ou sem remuneração, exerce cargo, emprego ou função pública.', 'C',
  'Art. **327**, caput: conceito amplo, que inclui o mesário e o jurado.',
  lei=[(CP + '327', 'Art. 327 - Considera-se funcionário público, para os efeitos penais', 'exerce cargo, emprego ou função pública.', 'CP, art. 327, caput')],
  kw=['327'])
I(P, 1, 'Funcionário por equiparação',
  'Não se equipara a funcionário público quem trabalha para empresa prestadora de serviço contratada para executar atividade típica da Administração Pública.', 'E',
  'Art. 327, **§ 1º**: equipara-se tanto quem atua em entidade paraestatal quanto quem trabalha para empresa **contratada ou conveniada** para atividade típica da Administração.',
  lei=[(CP + '327', '§ 1º - Equipara-se a funcionário público quem exerce cargo, emprego ou função em entidade paraestatal', 'atividade típica da Administração Pública.', 'CP, art. 327, § 1º')],
  peg='Negar a equiparação.', kw=['contratada ou conveniada'])
I(P, 1, 'Peculato-furto',
  'Comete peculato o funcionário que, embora não tendo a posse do bem, o subtrai, valendo-se da facilidade que lhe proporciona a qualidade de funcionário.', 'C',
  'Art. 312, **§ 1º** (peculato-furto ou impróprio).',
  lei=[(CP + '312', '§ 1º - Aplica-se a mesma pena, se o funcionário público, embora não tendo a posse do dinheiro, valor ou bem, o subtrai', None, 'CP, art. 312, § 1º')],
  kw=['peculato-furto'])
I(P, 1, 'Peculato culposo: reparação tardia',
  'No peculato culposo, a reparação do dano posterior à sentença irrecorrível também extingue a punibilidade.', 'E',
  'Art. 312, § 3º: **antes** da sentença irrecorrível, extingue; **depois**, **reduz de metade** a pena imposta.',
  lei=[(CP + '312', '§ 3º - No caso do parágrafo anterior, a reparação do dano, se precede à sentença irrecorrível, extingue a punibilidade; se lhe é posterior, reduz de metade a pena imposta.', None, 'CP, art. 312, § 3º')],
  peg='Extinguir a punibilidade depois do trânsito.', kw=['reduz de metade'])
I(P, 1, 'Concussão',
  'Comete concussão o funcionário que exige vantagem indevida, ainda que fora da função ou antes de assumi-la, mas em razão dela.', 'C',
  'Art. 316 (pena de 2 a 12 anos desde a Lei 13.964/2019): crime **formal** — consuma-se com a exigência.',
  lei=[(CP + '316', 'Art. 316 - Exigir, para si ou para outrem, direta ou indiretamente, ainda que fora da função ou antes de assumi-la, mas em razão dela, vantagem indevida:', None, 'CP, art. 316, caput')],
  kw=['formal'])
I(P, 1, 'Corrupção passiva',
  'A corrupção passiva só se configura com o efetivo recebimento da vantagem indevida pelo funcionário.', 'E',
  'Art. 317: também **solicitar** ou **aceitar promessa** — crime formal; a prática do ato de ofício só aumenta a pena (§ 1º).',
  lei=[(CP + '317', 'Art. 317 - Solicitar ou receber, para si ou para outrem', 'ou aceitar promessa de tal vantagem:', 'CP, art. 317, caput')],
  peg='Exigir o recebimento.', kw=['aceitar promessa'])
I(P, 1, 'Prevaricação',
  'A prevaricação exige que o funcionário retarde, deixe de praticar ou pratique contra a lei o ato de ofício para satisfazer interesse ou sentimento pessoal.', 'C',
  'Art. 319: o **especial fim de agir** distingue a prevaricação da corrupção passiva privilegiada (art. 317, § 2º, "cedendo a pedido ou influência de outrem").',
  lei=[(CP + '319', 'Art. 319 - Retardar ou deixar de praticar, indevidamente, ato de ofício', 'para satisfazer interesse ou sentimento pessoal:', 'CP, art. 319')],
  kw=['especial fim de agir'])
I(P, 1, 'Insignificância',
  'O princípio da insignificância aplica-se aos crimes contra a administração pública quando o prejuízo ao erário é ínfimo.', 'E',
  '**Súmula 599/STJ**: é **inaplicável** — o bem jurídico inclui a moralidade administrativa. Exceção reconhecida pelo próprio STJ: o **descaminho** (Tema 157).',
  juris=[J['S599']], peg='Aplicar a bagatela ao peculato.', kw=['Súmula 599/STJ'])
I(P, 1, 'Descaminho e bagatela',
  'Incide o princípio da insignificância no descaminho quando o débito tributário não ultrapassa R$ 20.000,00.', 'C',
  '**Tema 157/STJ** (revisado em 28/02/2018), com base no art. 20 da Lei 10.522/2002 e nas Portarias 75 e 130 do Ministério da Fazenda.',
  lei=[(CP + '334', 'Art. 334. Iludir, no todo ou em parte, o pagamento de direito ou imposto devido pela entrada, pela saída ou pelo consumo de mercadoria', None, 'CP, art. 334, caput')],
  juris=[J['T157']], kw=['Tema 157/STJ'])
I(P, 1, 'Desacato',
  'O STF declarou que o crime de desacato não foi recepcionado pela Constituição de 1988, por violar a liberdade de expressão.', 'E',
  'Na **ADPF 496** (sessão virtual finalizada em 19/06/2020), o STF decidiu que o desacato **foi recepcionado**, com interpretação restritiva.',
  lei=[(CP + '331', 'Art. 331 - Desacatar funcionário público no exercício da função ou em razão dela:', None, 'CP, art. 331')],
  juris=[J['ADPF496']], peg='Afirmar a não recepção.', kw=['ADPF 496'])
I(P, 1, 'Corrupção ativa',
  'Comete corrupção ativa quem oferece ou promete vantagem indevida a funcionário público para determiná-lo a praticar, omitir ou retardar ato de ofício.', 'C',
  'Art. 333 (pena de 2 a 12 anos): não há o verbo "dar" — dar vantagem **solicitada** pelo funcionário é atípico para o particular (doutrina).',
  lei=[(CP + '333', 'Art. 333 - Oferecer ou prometer vantagem indevida a funcionário público', 'para determiná-lo a praticar, omitir ou retardar ato de ofício:', 'CP, art. 333, caput')],
  kw=['oferece ou promete', 'Art. 333'])
I(P, 1, 'Contrabando x descaminho',
  'Contrabando é iludir, no todo ou em parte, o pagamento de imposto devido pela entrada de mercadoria no País.', 'E',
  'Essa é a definição de **descaminho** (art. 334). **Contrabando** é importar ou exportar **mercadoria proibida** (art. 334-A, reclusão de 2 a 5 anos).',
  lei=[(CP + '334-A', 'Art. 334-A. Importar ou exportar mercadoria proibida:', None, 'CP, art. 334-A, caput')],
  peg='Trocar contrabando por descaminho.', kw=['mercadoria proibida', 'descaminho'])
# --- PEN-10.12 · Rodada 2
I(P, 2, 'Denunciação caluniosa',
  'Comete denunciação caluniosa quem dá causa à instauração de inquérito civil ou de ação de improbidade administrativa contra alguém, imputando-lhe ato ímprobo de que o sabe inocente.', 'C',
  'Art. 339, na redação da **Lei 14.110/2020** (inclui infração ético-disciplinar e ato ímprobo).',
  lei=[(CP + '339', 'instauração de inquérito policial, de procedimento investigatório criminal', 'imputando-lhe crime, infração ético-disciplinar ou ato ímprobo de que o sabe inocente:', 'CP, art. 339, caput')],
  kw=['Lei 14.110/2020'])
I(P, 2, 'Retratação no falso testemunho',
  'No falso testemunho, a retratação feita após a sentença no processo em que ocorreu o ilícito extingue a punibilidade.', 'E',
  'Art. 342, § 2º: a retratação deve ocorrer **antes da sentença** no processo em que se deu o falso.',
  lei=[(CP + '342', '§ 2o O fato deixa de ser punível se, antes da sentença no processo em que ocorreu o ilícito, o agente se retrata ou declara a verdade.', None, 'CP, art. 342, § 2º')],
  peg='Admitir retratação tardia.', kw=['antes da sentença'])
I(P, 2, 'Favorecimento pessoal e família',
  'No favorecimento pessoal, fica isento de pena quem presta o auxílio sendo ascendente, descendente, cônjuge ou irmão do criminoso.', 'C',
  'Art. 348, **§ 2º** (escusa absolutória).',
  lei=[(CP + '348', '§ 2º - Se quem presta o auxílio é ascendente, descendente, cônjuge ou irmão do criminoso, fica isento de pena.', None, 'CP, art. 348, § 2º')],
  kw=['escusa absolutória'])
I(P, 2, 'Exercício arbitrário',
  'O exercício arbitrário das próprias razões é sempre crime de ação penal privada.', 'E',
  'Art. 345, par. ún.: só se procede mediante queixa **se não há emprego de violência**; com violência, a ação é pública.',
  lei=[(CP + '345', 'Parágrafo único - Se não há emprego de violência, somente se procede mediante queixa.', None, 'CP, art. 345, par. ún.')],
  peg='Ignorar a violência.', kw=['se não há emprego de violência'])
I(P, 2, 'Descumprimento de protetivas no CP',
  'O descumprimento de decisão judicial que defere medidas protetivas de urgência é tipificado no Código Penal, com pena de reclusão de 2 a 5 anos, e só a autoridade judicial pode conceder fiança no flagrante.', 'C',
  'Art. **338-A**, incluído pela Lei 15.280/2025 (a base também mantém o art. 24-A da Lei 11.340/2006, com a mesma pena).',
  lei=[(CP + '338-A', 'Art. 338-A. Descumprir decisão judicial que defere medidas protetivas de urgência:', 'Pena – reclusão, de 2 (dois) a 5 (cinco) anos, e multa.', 'CP, art. 338-A, caput'),
       (CP + '338-A', '§ 2º Na hipótese de prisão em flagrante, apenas a autoridade judicial pode conceder fiança.', None, 'CP, art. 338-A, § 2º')],
  kw=['338-A', 'Lei 15.280/2025'])
I(P, 2, 'Comunicação falsa de crime',
  'A comunicação falsa de crime exige que o agente impute o fato a pessoa determinada.', 'E',
  'Art. 340: basta provocar a ação da autoridade comunicando crime **que sabe não se ter verificado**. Imputar a pessoa determinada que se sabe inocente é **denunciação caluniosa** (art. 339).',
  lei=[(CP + '340', 'Art. 340 - Provocar a ação de autoridade, comunicando-lhe a ocorrência de crime ou de contravenção que sabe não se ter verificado:', None, 'CP, art. 340')],
  peg='Confundir os arts. 339 e 340.', kw=['denunciação caluniosa'])
I(P, 2, 'Fraude à licitação',
  'O crime de frustração do caráter competitivo de licitação é formal e se consuma independentemente de prejuízo ao erário.', 'C',
  'Art. **337-F** (Lei 14.133/2021, reclusão de 4 a 8 anos); **Súmula 645/STJ**, firmada para o antigo art. 90 da Lei 8.666/1993, de redação equivalente.',
  lei=[(CP + '337-F', 'Art. 337-F. Frustrar ou fraudar, com o intuito de obter para si ou para outrem vantagem decorrente da adjudicação do objeto da licitação', None, 'CP, art. 337-F')],
  juris=[J['S645']], kw=['Súmula 645/STJ', '337-F'])
I(P, 2, 'Aumento do art. 327, § 2º',
  'A pena dos crimes funcionais é aumentada da terça parte sempre que o autor for servidor efetivo.', 'E',
  'Art. 327, § 2º: aumento para ocupantes de **cargos em comissão** ou de **função de direção ou assessoramento** da administração direta ou indireta.',
  lei=[(CP + '327', '§ 2º - A pena será aumentada da terça parte quando os autores dos crimes previstos neste Capítulo forem ocupantes de cargos em comissão', None, 'CP, art. 327, § 2º')],
  peg='Estender a qualquer servidor.', kw=['cargos em comissão'])

# ======================= PEN-10.13 · Crimes contra as finanças públicas =======================
P = 'DBA26-PEN-10.13'
I(P, 1, 'Operação de crédito',
  'Ordenar, autorizar ou realizar operação de crédito, interno ou externo, sem prévia autorização legislativa é crime contra as finanças públicas.', 'C',
  'Art. **359-A** (Lei 10.028/2000, que concretizou penalmente a Lei de Responsabilidade Fiscal); reclusão de 1 a 2 anos.',
  lei=[(CP + '359-A', 'Art. 359-A. Ordenar, autorizar ou realizar operação de crédito, interno ou externo, sem prévia autorização legislativa:', None, 'CP, art. 359-A, caput')],
  kw=['359-A'])
I(P, 1, 'Restos a pagar sem empenho',
  'A inscrição em restos a pagar de despesa não empenhada é punida com reclusão.', 'E',
  'Art. 359-B: **detenção** de 6 meses a 2 anos.',
  lei=[(CP + '359-B', 'Art. 359-B. Ordenar ou autorizar a inscrição em restos a pagar', 'Pena – detenção, de 6 (seis) meses a 2 (dois) anos.', 'CP, art. 359-B')],
  peg='Trocar detenção por reclusão.', kw=['detenção'])
I(P, 1, 'Último ano do mandato',
  'Ordenar a assunção de obrigação nos dois últimos quadrimestres do último ano do mandato, cuja despesa não possa ser paga no mesmo exercício ou sem disponibilidade de caixa para a parcela seguinte, é crime.', 'C',
  'Art. **359-C** (reclusão de 1 a 4 anos).',
  lei=[(CP + '359-C', 'Art. 359-C. Ordenar ou autorizar a assunção de obrigação, nos dois últimos quadrimestres do último ano do mandato ou legislatura', None, 'CP, art. 359-C')],
  kw=['359-C'])
I(P, 1, 'Despesa com pessoal',
  'É crime ordenar ato que acarrete aumento de despesa total com pessoal nos noventa dias anteriores ao final do mandato.', 'E',
  'Art. 359-G: nos **cento e oitenta dias** anteriores ao final do mandato ou da legislatura.',
  lei=[(CP + '359-G', 'Art. 359-G. Ordenar, autorizar ou executar ato que acarrete aumento de despesa total com pessoal, nos cento e oitenta dias anteriores', None, 'CP, art. 359-G')],
  peg='Errar o prazo.', kw=['cento e oitenta dias'])
I(P, 1, 'Garantia graciosa',
  'Comete o crime de prestação de garantia graciosa quem presta garantia em operação de crédito tendo exigido contragarantia de valor igual ou superior ao da garantia.', 'E',
  'Art. 359-E: o crime é prestar a garantia **sem** que tenha sido constituída contragarantia igual ou superior.',
  lei=[(CP + '359-E', 'Art. 359-E. Prestar garantia em operação de crédito sem que tenha sido constituída contragarantia', None, 'CP, art. 359-E')],
  peg='Inverter o núcleo.', kw=['sem'])
# --- PEN-10.13 · Rodada 2
I(P, 2, 'Títulos da dívida',
  'Ordenar a oferta pública de títulos da dívida pública que não tenham sido criados por lei ou não estejam registrados em sistema centralizado de liquidação e custódia é crime.', 'C',
  'Art. **359-H** (reclusão de 1 a 4 anos).',
  lei=[(CP + '359-H', 'Art. 359-H. Ordenar, autorizar ou promover a oferta pública ou a colocação no mercado financeiro de títulos da dívida pública', None, 'CP, art. 359-H')],
  kw=['359-H'])
I(P, 2, 'Não cancelamento de restos a pagar',
  'O art. 359-F pune quem promove o cancelamento de restos a pagar inscritos em valor superior ao permitido em lei.', 'E',
  'O crime é **deixar de** ordenar, autorizar ou promover o cancelamento (omissivo próprio).',
  lei=[(CP + '359-F', 'Art. 359-F. Deixar de ordenar, de autorizar ou de promover o cancelamento do montante de restos a pagar', None, 'CP, art. 359-F')],
  peg='Transformar a omissão em ação.', kw=['deixar de'])
I(P, 2, 'Despesa não autorizada',
  'Ordenar despesa não autorizada por lei é punido com reclusão de 1 a 4 anos.', 'C',
  'Art. **359-D**.',
  lei=[(CP + '359-D', 'Art. 359-D. Ordenar despesa não autorizada por lei:', 'Pena – reclusão, de 1 (um) a 4 (quatro) anos.', 'CP, art. 359-D')],
  kw=['359-D'])

# ======================= PEN-10.14 · Crimes contra o Estado Democrático de Direito =======================
P = 'DBA26-PEN-10.14'
I(P, 1, 'Abolição violenta',
  'Tentar, com emprego de violência ou grave ameaça, abolir o Estado Democrático de Direito, impedindo ou restringindo o exercício dos poderes constitucionais, é crime.', 'C',
  'Art. **359-L** (Lei 14.197/2021, que revogou a Lei de Segurança Nacional); reclusão de 4 a 8 anos, além da pena da violência.',
  lei=[(CP + '359-L', 'Art. 359-L. Tentar, com emprego de violência ou grave ameaça, abolir o Estado Democrático de Direito', None, 'CP, art. 359-L')],
  kw=['359-L'])
I(P, 1, 'Golpe de Estado: consumação',
  'O crime de golpe de Estado só se consuma com a efetiva deposição do governo legitimamente constituído.', 'E',
  'O art. 359-M pune **tentar depor** o governo por violência ou grave ameaça: crime **de atentado** (ou de empreendimento), consumado com a tentativa — a deposição efetiva tornaria impossível a punição (doutrina). Pena: reclusão de 4 a 12 anos.',
  lei=[(CP + '359-M', 'Pena - reclusão, de 4 (quatro) a 12 (doze) anos, além da pena correspondente à violência.', None, 'CP, art. 359-M (pena)')],
  peg='Exigir a deposição.', kw=['de atentado'])
I(P, 1, 'Manifestação crítica',
  'Não constitui crime contra o Estado Democrático de Direito a manifestação crítica aos poderes constitucionais nem a reivindicação de direitos por meio de passeatas, reuniões ou greves.', 'C',
  'Art. **359-T** (cláusula de exclusão).',
  lei=[(CP + '359-T', 'Art. 359-T. Não constitui crime previsto neste Título a manifestação crítica aos poderes constitucionais', None, 'CP, art. 359-T')],
  kw=['359-T'])
I(P, 1, 'Multidão e liderança',
  'Pela Lei 15.402/2026, a redução de pena dos crimes contra as instituições democráticas praticados em contexto de multidão alcança também o agente que exerceu papel de liderança.', 'E',
  'Art. 359-M-B: redução de **1/3 a 2/3** em contexto de multidão, **desde que** o agente **não** tenha financiado nem exercido **liderança**. A mesma lei (art. 359-M-A) manda aplicar, no mesmo contexto, o **concurso formal próprio**, vedado o cúmulo material.',
  lei=[(CP + '359-M', 'Art. 359-M-B. Quando os crimes previstos neste Capítulo forem praticados em contexto de multidão', 'desde que o agente não tenha praticado ato de financiamento ou exercido papel de liderança.', 'CP, art. 359-M-B')],
  peg='Estender a redução ao líder.', kw=['liderança', 'Lei 15.402/2026'])
I(P, 1, 'Espionagem e direitos humanos',
  'Não constitui espionagem a entrega ou a publicação de informações ou documentos com o fim de expor a prática de crime ou a violação de direitos humanos.', 'C',
  'Art. 359-K, **§ 4º**.',
  lei=[(CP + '359-K', '§ 4º Não constitui crime a comunicação, a entrega ou a publicação de informações ou de documentos', 'a violação de direitos humanos.', 'CP, art. 359-K, § 4º')],
  kw=['§ 4º'])
# --- PEN-10.14 · Rodada 2
I(P, 2, 'Violência política',
  'O crime de violência política só protege candidatos regularmente registrados na Justiça Eleitoral.', 'E',
  'Art. 359-P: protege o exercício de direitos políticos de **qualquer pessoa**, em razão de sexo, raça, cor, etnia, religião ou procedência nacional.',
  lei=[(CP + '359-P', 'Art. 359-P. Restringir, impedir ou dificultar, com emprego de violência física, sexual ou psicológica', 'em razão de seu sexo, raça, cor, etnia, religião ou procedência nacional:', 'CP, art. 359-P')],
  peg='Restringir a candidatos.', kw=['qualquer pessoa'])
I(P, 2, 'Processo eleitoral',
  'Impedir ou perturbar a eleição ou a aferição de seu resultado mediante violação indevida de mecanismos de segurança do sistema eletrônico de votação é crime contra o funcionamento das instituições democráticas no processo eleitoral.', 'C',
  'Art. **359-N** (reclusão de 3 a 6 anos, e multa).',
  lei=[(CP + '359-N', 'Art. 359-N. Impedir ou perturbar a eleição ou a aferição de seu resultado', None, 'CP, art. 359-N')],
  kw=['359-N'])
I(P, 2, 'Atentado à soberania',
  'No atentado à soberania, se declarada guerra em decorrência da conduta, a pena aumenta-se de um terço.', 'E',
  'Art. 359-I, § 1º: aumento **de metade até o dobro**.',
  lei=[(CP + '359-I', '§ 1º Aumenta-se a pena de metade até o dobro, se declarada guerra em decorrência das condutas previstas no caput deste artigo.', None, 'CP, art. 359-I, § 1º')],
  peg='Errar a fração.', kw=['de metade até o dobro'])
