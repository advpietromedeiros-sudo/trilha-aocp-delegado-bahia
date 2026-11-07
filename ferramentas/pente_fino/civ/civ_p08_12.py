from base import I
from civ_juris import J

CC = 'L10406:'
CDC = 'L8078:'
ID = 'L10741:'
PD = 'L13146:'
RF = 'L11101:'
P = 'DBA26-CIV-8'
# ---------------- PONTO 8 · CDC — RODADA 1
I(P, 1, 'Conceito de consumidor',
  'Consumidor é toda pessoa física ou jurídica que adquire ou utiliza produto ou serviço como destinatário final, equiparando-se a consumidor a coletividade de pessoas, ainda que indetermináveis, que haja intervindo nas relações de consumo.', 'C',
  'Art. 2º e parágrafo único: **destinatário final** (o STJ adota a teoria finalista, mitigada diante de vulnerabilidade) e **consumidor por equiparação** (coletividade).',
  lei=[(CDC + '2', 'Consumidor é toda pessoa física ou jurídica', 'como destinatário final.', 'CDC, art. 2º'),
       (CDC + '2', 'Equipara-se a consumidor a coletividade de pessoas', 'relações de consumo.', 'CDC, art. 2º, par. ún.')],
  exc=['Também são consumidores por equiparação as vítimas do evento (art. 17) e as pessoas expostas às práticas comerciais (art. 29)'],
  kw=['destinatário final', 'coletividade'])
I(P, 1, 'Serviços bancários',
  'Serviço é qualquer atividade fornecida no mercado de consumo, mediante remuneração, inclusive as de natureza bancária, financeira, de crédito e securitária, salvo as decorrentes das relações de caráter trabalhista.', 'C',
  'Art. 3º, § 2º + **Súmula 297/STJ**: o CDC se aplica às **instituições financeiras**.',
  lei=[(CDC + '3', 'Serviço é qualquer atividade fornecida no mercado de consumo', 'caráter trabalhista.', 'CDC, art. 3º, § 2º')],
  juris=[J['S297']],
  kw=['serviço', 'natureza bancária'])
I(P, 1, 'Inversão do ônus da prova',
  'A inversão do ônus da prova em favor do consumidor, no processo civil, é automática e decorre da simples existência da relação de consumo.', 'E',
  'Art. 6º, VIII: a inversão é **ope judicis** — **a critério do juiz**, quando **verossímil** a alegação **ou** quando o consumidor for **hipossuficiente**.',
  lei=[(CDC + '6', 'VIII - a facilitação da defesa de seus direitos', 'regras ordinárias de experiências;', 'CDC, art. 6º, VIII')],
  exc=['Inversão ope legis: publicidade (art. 38) e excludentes do fato do produto/serviço (arts. 12, § 3º, e 14, § 3º)'],
  kw=['inversão do ônus da prova', 'a critério do juiz'])
I(P, 1, 'Fato do produto',
  'O fabricante, o produtor, o construtor e o importador respondem, independentemente da existência de culpa, pela reparação dos danos causados aos consumidores por defeitos de seus produtos.', 'C',
  'Art. 12: responsabilidade **objetiva** pelo **fato do produto** (acidente de consumo).',
  lei=[(CDC + '12', 'O fabricante, o produtor, o construtor', 'independentemente da existência de culpa', 'CDC, art. 12')],
  kw=['fato do produto', 'independentemente da existência de culpa'])
I(P, 1, 'Responsabilidade do comerciante',
  'Pelo fato do produto, o comerciante responde sempre solidariamente com o fabricante, em igualdade de condições.', 'E',
  'Art. 13: o comerciante responde **subsidiariamente**, só quando o fabricante não puder ser identificado, o produto vier sem identificação clara ou ele não conservar adequadamente os perecíveis.',
  lei=[(CDC + '13', 'O comerciante é igualmente responsável', 'produtos perecíveis.', 'CDC, art. 13')],
  peg='No vício do produto (art. 18) a solidariedade abrange o comerciante; no fato do produto, não.',
  kw=['comerciante', 'fato do produto'])
I(P, 1, 'Profissionais liberais',
  'A responsabilidade pessoal dos profissionais liberais será apurada mediante a verificação de culpa.', 'C',
  'Art. 14, § 4º: exceção **subjetiva** dentro do CDC.',
  lei=[(CDC + '14', 'A responsabilidade pessoal dos profissionais liberais', 'verificação de culpa.', 'CDC, art. 14, § 4º')],
  kw=['profissionais liberais', 'verificação de culpa'])
I(P, 1, 'Prazo para sanar o vício',
  'Não sendo o vício do produto sanado no prazo máximo de sessenta dias, pode o consumidor exigir a substituição do produto, a restituição imediata da quantia paga ou o abatimento proporcional do preço.', 'E',
  'Art. 18, § 1º: o prazo é de **trinta dias**. As partes podem convencionar entre 7 e 180 dias (§ 2º).',
  lei=[(CDC + '18', 'Não sendo o vício sanado no prazo máximo de trinta dias', 'abatimento proporcional do preço.', 'CDC, art. 18, § 1º')],
  kw=['vício do produto', 'trinta dias'])
I(P, 1, 'Decadência dos vícios aparentes',
  'O direito de reclamar pelos vícios aparentes ou de fácil constatação caduca em trinta dias, tratando-se de fornecimento de serviço e de produtos não duráveis, e em noventa dias, tratando-se de serviço e de produtos duráveis.', 'C',
  'Art. 26: **30 dias** (não duráveis) e **90 dias** (duráveis), contados da **entrega efetiva** ou do término da execução do serviço.',
  lei=[(CDC + '26', 'O direito de reclamar pelos vícios aparentes', 'produtos duráveis.', 'CDC, art. 26')],
  kw=['vícios aparentes', 'trinta dias', 'noventa dias'])
I(P, 1, 'Prescrição do fato do produto',
  'Prescreve em três anos a pretensão à reparação pelos danos causados por fato do produto ou do serviço, iniciando-se a contagem do prazo a partir do conhecimento do dano e de sua autoria.', 'E',
  'Art. 27: o prazo é de **cinco anos**. Três anos é o da reparação civil no CC (art. 206, § 3º, V).',
  lei=[(CDC + '27', 'Prescreve em cinco anos a pretensão à reparação', 'de sua autoria.', 'CDC, art. 27')],
  kw=['cinco anos', 'fato do produto'])
I(P, 1, 'Direito de arrependimento',
  'O consumidor pode desistir do contrato no prazo de sete dias a contar de sua assinatura ou do ato de recebimento do produto ou serviço, sempre que a contratação ocorrer fora do estabelecimento comercial.', 'C',
  'Art. 49: **7 dias**, contratação **fora do estabelecimento**; os valores pagos são devolvidos de imediato, monetariamente atualizados.',
  lei=[(CDC + '49', 'O consumidor pode desistir do contrato', 'a domicílio.', 'CDC, art. 49')],
  kw=['arrependimento', 'sete dias'])
I(P, 1, 'Produto enviado sem solicitação',
  'É prática abusiva enviar ou entregar ao consumidor, sem solicitação prévia, qualquer produto, e os produtos assim remetidos equiparam-se às amostras grátis, inexistindo obrigação de pagamento.', 'C',
  'Art. 39, III e parágrafo único + **Súmula 532/STJ** (cartão de crédito não solicitado é ato ilícito indenizável).',
  lei=[(CDC + '39', 'III - enviar ou entregar ao consumidor, sem solicitação prévia', 'qualquer serviço;', 'CDC, art. 39, III'),
       (CDC + '39', 'Os serviços prestados e os produtos remetidos ou entregues', 'inexistindo obrigação de pagamento.', 'CDC, art. 39, par. ún.')],
  juris=[J['S532']],
  kw=['prática abusiva', 'amostras grátis'])
I(P, 1, 'Desconsideração no CDC',
  'No Código de Defesa do Consumidor, a desconsideração da personalidade jurídica do fornecedor exige a prova de desvio de finalidade ou de confusão patrimonial.', 'E',
  'Art. 28, § 5º: adota-se a **teoria menor** — pode haver desconsideração **sempre que a personalidade for obstáculo ao ressarcimento** dos prejuízos do consumidor.',
  lei=[(CDC + '28', 'Também poderá ser desconsiderada a pessoa jurídica sempre que', 'causados aos consumidores.', 'CDC, art. 28, § 5º')],
  kw=['teoria menor', 'obstáculo ao ressarcimento'])

# ---------------- PONTO 8 — RODADA 2
I(P, 2, 'Prazo dos cadastros negativos',
  'Os cadastros e dados de consumidores não podem conter informações negativas referentes a período superior a cinco anos.', 'C',
  'Art. 43, § 1º + **Súmula 323/STJ**: máximo de **5 anos**, independentemente da prescrição da execução.',
  lei=[(CDC + '43', 'Os cadastros e dados de consumidores devem ser objetivos', 'período superior a cinco anos.', 'CDC, art. 43, § 1º')],
  juris=[J['S323']],
  kw=['cadastros', 'cinco anos'])
I(P, 2, 'Notificação prévia da negativação',
  'Cabe ao credor que solicitou a inscrição notificar o devedor antes de sua inclusão no cadastro de proteção ao crédito, por carta com aviso de recebimento.', 'E',
  'A notificação cabe ao **órgão mantenedor** do cadastro (**Súmula 359/STJ**), e é **dispensável o AR** (**Súmula 404/STJ**).',
  lei=[(CDC + '43', 'A abertura de cadastro, ficha, registro e dados pessoais', 'quando não solicitada por ele.', 'CDC, art. 43, § 2º')],
  juris=[J['S359'], J['S404']],
  kw=['órgão mantenedor', 'aviso de recebimento'])
I(P, 2, 'Repetição em dobro',
  'O consumidor cobrado em quantia indevida tem direito à repetição do indébito, por valor igual ao dobro do que pagou em excesso, acrescido de correção monetária e juros legais, salvo hipótese de engano justificável.', 'C',
  'Art. 42, parágrafo único: exige **pagamento** do indevido; afasta-se a dobra no **engano justificável**.',
  lei=[(CDC + '42', 'O consumidor cobrado em quantia indevida', 'engano justificável.', 'CDC, art. 42, par. ún.')],
  kw=['repetição do indébito', 'dobro'])
I(P, 2, 'Cláusula de não indenizar',
  'São nulas de pleno direito as cláusulas que impossibilitem, exonerem ou atenuem a responsabilidade do fornecedor por vícios de qualquer natureza; nas relações com consumidor pessoa jurídica, a indenização poderá ser limitada, em situações justificáveis.', 'C',
  'Art. 51, I: **nulidade** da cláusula de não indenizar, com a ressalva da **pessoa jurídica** consumidora.',
  lei=[(CDC + '51', 'I - impossibilitem, exonerem ou atenuem a responsabilidade do fornecedor', 'situações justificáveis;', 'CDC, art. 51, I')],
  kw=['nulas de pleno direito', 'pessoa jurídica'])
I(P, 2, 'Abusividade em contrato bancário',
  'Nos contratos bancários, o julgador pode reconhecer de ofício a abusividade das cláusulas, por se tratar de matéria de ordem pública prevista no CDC.', 'E',
  '**Súmula 381/STJ**: nos contratos bancários é **vedado** ao julgador conhecer **de ofício** da abusividade.',
  juris=[J['S381']],
  kw=['contratos bancários', 'de ofício'])
I(P, 2, 'Previdência complementar',
  'O Código de Defesa do Consumidor aplica-se tanto às entidades abertas quanto às entidades fechadas de previdência complementar.', 'E',
  '**Súmula 563/STJ**: aplica-se às **abertas**, **não** às **fechadas**.',
  juris=[J['S563']],
  kw=['previdência complementar', 'entidades fechadas'])
I(P, 2, 'Planos de saúde e autogestão',
  'Aplica-se o Código de Defesa do Consumidor aos contratos de plano de saúde, salvo os administrados por entidades de autogestão.', 'C',
  '**Súmula 608/STJ** (a antiga Súmula 469 foi cancelada e substituída por esta).',
  juris=[J['S608']],
  kw=['plano de saúde', 'autogestão'])
I(P, 2, 'Fortuito interno bancário',
  'As instituições financeiras respondem objetivamente pelos danos gerados por fortuito interno relativo a fraudes e delitos praticados por terceiros no âmbito de operações bancárias.', 'C',
  '**Súmula 479/STJ**: fraude de terceiro é **risco da atividade** (fortuito interno), que não rompe o nexo causal.',
  lei=[(CDC + '14', 'O fornecedor de serviços responde, independentemente da existência de culpa', 'fruição e riscos.', 'CDC, art. 14')],
  juris=[J['S479']],
  kw=['fortuito interno', 'objetivamente'])
I(P, 2, 'Vício oculto',
  'Tratando-se de vício oculto, o prazo decadencial para reclamar conta-se da entrega efetiva do produto.', 'E',
  'Art. 26, § 3º: no **vício oculto**, o prazo inicia-se **no momento em que ficar evidenciado o defeito**.',
  lei=[(CDC + '26', 'Tratando-se de vício oculto', 'evidenciado o defeito.', 'CDC, art. 26, § 3º')],
  kw=['vício oculto', 'evidenciado o defeito'])

P = 'DBA26-CIV-9'
# ---------------- PONTO 9 · Estatuto da Pessoa Idosa — RODADA 1
I(P, 1, 'Destinatários do Estatuto',
  'O Estatuto da Pessoa Idosa regula os direitos assegurados às pessoas com idade igual ou superior a sessenta anos.', 'C',
  'Art. 1º: **60 anos ou mais**.',
  lei=[(ID + '1', 'É instituído o Estatuto da Pessoa Idosa', 'igual ou superior a 60 (sessenta) anos.', 'Lei 10.741/2003, art. 1º')],
  kw=['sessenta anos'])
I(P, 1, 'Prioridade especial',
  'Entre as pessoas idosas, é assegurada prioridade especial aos maiores de setenta anos, atendendo-se suas necessidades sempre preferencialmente em relação às demais pessoas idosas.', 'E',
  'Art. 3º, § 2º: a **prioridade especial** é dos **maiores de 80 anos**.',
  lei=[(ID + '3', 'Entre as pessoas idosas, é assegurada prioridade especial', 'demais pessoas idosas.', 'Lei 10.741/2003, art. 3º, § 2º')],
  kw=['prioridade especial', 'oitenta anos'])
I(P, 1, 'Alimentos solidários',
  'A obrigação alimentar em favor da pessoa idosa é solidária, podendo ela optar entre os prestadores.', 'C',
  'Art. 12: **solidariedade** — exceção à regra civil da divisibilidade dos alimentos entre parentes.',
  lei=[(ID + '12', 'A obrigação alimentar é solidária', 'optar entre os prestadores.', 'Lei 10.741/2003, art. 12')],
  kw=['obrigação alimentar', 'solidária'])
I(P, 1, 'Dever do Poder Público',
  'Se a pessoa idosa ou seus familiares não possuírem condições econômicas de prover o seu sustento, impõe-se ao poder público esse provimento, no âmbito da assistência social.', 'C',
  'Art. 14: **subsidiariedade estatal** pela assistência social.',
  lei=[(ID + '14', 'Se a pessoa idosa ou seus familiares não possuírem condições econômicas', 'assistência social.', 'Lei 10.741/2003, art. 14')],
  kw=['poder público', 'assistência social'])
I(P, 1, 'Plano de saúde e idade',
  'É vedada a discriminação da pessoa idosa nos planos de saúde pela cobrança de valores diferenciados em razão da idade.', 'C',
  'Art. 15, § 3º. O STJ, porém, admite o reajuste por faixa etária dentro de limites (Tema 952).',
  lei=[(ID + '15', 'É vedada a discriminação da pessoa idosa nos planos de saúde', 'em razão da idade.', 'Lei 10.741/2003, art. 15, § 3º')],
  kw=['planos de saúde', 'discriminação'])
I(P, 1, 'Gratuidade no transporte urbano',
  'Às pessoas maiores de sessenta anos fica assegurada, em todo o território nacional, a gratuidade dos transportes coletivos públicos urbanos e semiurbanos, exceto nos serviços seletivos e especiais.', 'E',
  'Art. 39: a gratuidade obrigatória é para os **maiores de 65 anos**. Entre 60 e 65, fica a critério da **legislação local** (§ 3º).',
  lei=[(ID + '39', 'Aos maiores de 65 (sessenta e cinco) anos fica assegurada a gratuidade', 'regulares.', 'Lei 10.741/2003, art. 39')],
  kw=['gratuidade', 'sessenta e cinco anos'])
I(P, 1, 'Transporte interestadual',
  'No sistema de transporte coletivo interestadual, reserva-se uma vaga gratuita por veículo para pessoas idosas com renda igual ou inferior a dois salários mínimos.', 'E',
  'Art. 40, I: são **duas vagas** gratuitas por veículo; para os que excederem as vagas, **desconto de 50%**, no mínimo (inciso II).',
  lei=[(ID + '40', 'a reserva de 2 (duas) vagas gratuitas por veículo', '2 (dois) salários mínimos;', 'Lei 10.741/2003, art. 40, I')],
  kw=['interestadual', 'duas vagas'])
I(P, 1, 'Estacionamentos',
  'É assegurada a reserva, para as pessoas idosas, de cinco por cento das vagas nos estacionamentos públicos e privados, posicionadas de forma a garantir a melhor comodidade.', 'C',
  'Art. 41: **5%** das vagas.',
  lei=[(ID + '41', 'É assegurada a reserva para as pessoas idosas', 'melhor comodidade à pessoa idosa.', 'Lei 10.741/2003, art. 41')],
  kw=['estacionamentos', 'cinco por cento'])
I(P, 1, 'Benefício assistencial',
  'Às pessoas idosas, a partir de sessenta e cinco anos, que não possuam meios para prover sua subsistência, nem de tê-la provida por sua família, é assegurado o benefício mensal de um salário mínimo, nos termos da Lei Orgânica da Assistência Social.', 'C',
  'Art. 34: **65 anos** + ausência de meios → **BPC** de 1 salário mínimo.',
  lei=[(ID + '34', 'Às pessoas idosas, a partir de 65 (sessenta e cinco) anos', 'nos termos da Loas.', 'Lei 10.741/2003, art. 34')],
  kw=['benefício', 'sessenta e cinco anos'])
I(P, 1, 'Desconto em eventos culturais',
  'A participação das pessoas idosas em atividades culturais e de lazer será proporcionada mediante descontos de pelo menos trinta por cento nos ingressos.', 'E',
  'Art. 23: desconto de **pelo menos 50%** nos ingressos, e acesso preferencial aos locais.',
  lei=[(ID + '23', 'A participação das pessoas idosas em atividades culturais', 'acesso preferencial aos respectivos locais.', 'Lei 10.741/2003, art. 23')],
  kw=['ingressos', 'cinquenta por cento'])

# ---------------- PONTO 9 — RODADA 2
I(P, 2, 'Reajuste por faixa etária',
  'Segundo o STJ, é sempre ilegal o reajuste de mensalidade de plano de saúde individual fundado na mudança de faixa etária do beneficiário idoso.', 'E',
  'No **Tema 952**, o STJ admitiu o reajuste se houver **previsão contratual**, observância das **normas regulatórias** e **ausência de percentuais desarrazoados** que onerem excessivamente ou discriminem o idoso.',
  juris=[J['T952']],
  kw=['faixa etária', 'Tema 952'])
I(P, 2, 'Transação sobre alimentos',
  'As transações relativas a alimentos poderão ser celebradas perante o Promotor de Justiça ou Defensor Público, que as referendará, e passarão a ter efeito de título executivo extrajudicial nos termos da lei processual civil.', 'C',
  'Art. 13: acordo referendado por **MP ou Defensoria** = **título executivo extrajudicial**.',
  lei=[(ID + '13', 'As transações relativas a alimentos poderão ser celebradas', 'lei processual civil.', 'Lei 10.741/2003, art. 13')],
  kw=['transações', 'título executivo extrajudicial'])
I(P, 2, 'Entidade de longa permanência',
  'A entidade de longa permanência pode cobrar participação da pessoa idosa no custeio, não podendo exceder a cinquenta por cento de qualquer benefício previdenciário ou de assistência social percebido.', 'E',
  'Art. 35, § 2º: o teto é de **70%** do benefício.',
  lei=[(ID + '35', 'O Conselho Municipal da Pessoa Idosa ou o Conselho Municipal da Assistência Social estabelecerá a forma de participação', 'percebido pela pessoa idosa.', 'Lei 10.741/2003, art. 35, § 2º')],
  kw=['longa permanência', 'setenta por cento'])
I(P, 2, 'Prioridade processual',
  'É assegurada prioridade na tramitação dos processos em que figure como parte pessoa com idade igual ou superior a sessenta anos e, dentre esses, prioridade especial aos maiores de oitenta anos.', 'C',
  'Art. 71, caput e § 5º: **60 anos** e, com prioridade especial, **80 anos**.',
  lei=[(ID + '71', 'É assegurada prioridade na tramitação dos processos', 'em qualquer instância.', 'Lei 10.741/2003, art. 71'),
       (ID + '71', 'Dentre os processos de pessoas idosas, dar-se-á prioridade especial', 'maiores de 80 (oitenta) anos.', 'Lei 10.741/2003, art. 71, § 5º')],
  kw=['prioridade na tramitação', 'oitenta anos'])
I(P, 2, 'Benefício já concedido a familiar',
  'O benefício assistencial já concedido a qualquer membro da família não será computado para os fins do cálculo da renda familiar per capita a que se refere a Loas.', 'C',
  'Art. 34, parágrafo único: o BPC de um membro **não entra** na renda per capita do outro.',
  lei=[(ID + '34', 'O benefício já concedido a qualquer membro da família', 'Loas.', 'Lei 10.741/2003, art. 34, par. ún.')],
  kw=['renda familiar per capita'])
I(P, 2, 'Medidas de proteção',
  'As medidas de proteção à pessoa idosa são aplicáveis sempre que os direitos reconhecidos no Estatuto forem ameaçados ou violados por ação ou omissão da sociedade ou do Estado, por falta, omissão ou abuso da família, curador ou entidade de atendimento, ou em razão de sua condição pessoal.', 'C',
  'Art. 43: três hipóteses — **sociedade/Estado**, **família/curador/entidade** e **condição pessoal**.',
  lei=[(ID + '43', 'As medidas de proteção à pessoa idosa são aplicáveis', 'em razão de sua condição pessoal.', 'Lei 10.741/2003, art. 43')],
  kw=['medidas de proteção', 'condição pessoal'])
I(P, 2, 'Desempate em concurso',
  'O primeiro critério de desempate em concurso público é o maior tempo de serviço público, aplicando-se a idade mais elevada apenas em segundo lugar.', 'E',
  'Art. 27, parágrafo único: o **primeiro critério de desempate** é a **idade**, preferindo-se a **mais elevada**.',
  lei=[(ID + '27', 'O primeiro critério de desempate em concurso público será a idade', 'idade mais elevada.', 'Lei 10.741/2003, art. 27, par. ún.')],
  kw=['desempate', 'idade mais elevada'])
I(P, 2, 'Notificação compulsória da violência',
  'Os casos de suspeita ou confirmação de violência praticada contra pessoas idosas serão objeto de notificação facultativa pelos serviços de saúde, a critério do profissional que realizar o atendimento.', 'E',
  'Art. 19: a **notificação é compulsória** à autoridade sanitária, com **comunicação obrigatória** à autoridade policial, ao Ministério Público e aos Conselhos da Pessoa Idosa.',
  lei=[(ID + '19', 'Os casos de suspeita ou confirmação de violência praticada contra pessoas idosas', 'notificação compulsória', 'Lei 10.741/2003, art. 19')],
  kw=['notificação compulsória', 'violência'])

P = 'DBA26-CIV-10'
# ---------------- PONTO 10 · Estatuto da Pessoa com Deficiência — RODADA 1
I(P, 1, 'Conceito de pessoa com deficiência',
  'Considera-se pessoa com deficiência aquela que tem impedimento de longo prazo de natureza física, mental, intelectual ou sensorial, o qual, em interação com uma ou mais barreiras, pode obstruir sua participação plena e efetiva na sociedade em igualdade de condições com as demais pessoas.', 'C',
  'Art. 2º: **modelo social** (biopsicossocial) — o impedimento de **longo prazo** interage com **barreiras**.',
  lei=[(PD + '2', 'Considera-se pessoa com deficiência aquela que tem impedimento de longo prazo', 'em igualdade de condições com as demais pessoas.', 'Lei 13.146/2015, art. 2º')],
  kw=['impedimento de longo prazo', 'barreiras'])
I(P, 1, 'Plena capacidade civil',
  'A deficiência não afeta a plena capacidade civil da pessoa, inclusive para casar-se e constituir união estável, exercer direitos sexuais e reprodutivos e exercer o direito à guarda e à adoção.', 'C',
  'Art. 6º: a deficiência **não afeta a plena capacidade civil**.',
  lei=[(PD + '6', 'A deficiência não afeta a plena capacidade civil da pessoa', 'em igualdade de oportunidades com as demais pessoas.', 'Lei 13.146/2015, art. 6º')],
  kw=['plena capacidade civil'])
I(P, 1, 'Curatela como medida extraordinária',
  'Quando necessário, a pessoa com deficiência será submetida à curatela, que constitui medida protetiva extraordinária, proporcional às necessidades e às circunstâncias de cada caso, e durará o menor tempo possível.', 'C',
  'Art. 84, §§ 1º e 3º: curatela **excepcional**, **proporcional** e **pelo menor tempo possível**.',
  lei=[(PD + '84', 'Quando necessário, a pessoa com deficiência será submetida à curatela', 'conforme a lei.', 'Lei 13.146/2015, art. 84, § 1º'),
       (PD + '84', 'A definição de curatela de pessoa com deficiência constitui medida protetiva extraordinária', 'menor tempo possível.', 'Lei 13.146/2015, art. 84, § 3º')],
  kw=['curatela', 'medida protetiva extraordinária'])
I(P, 1, 'Alcance da curatela',
  'A curatela da pessoa com deficiência alcança os atos de natureza patrimonial e negocial e, quando a sentença o determinar, o direito ao matrimônio e ao voto.', 'E',
  'Art. 85: a curatela afeta **tão somente** atos **patrimoniais e negociais**; § 1º: **não alcança** corpo, sexualidade, **matrimônio**, privacidade, educação, saúde, trabalho e **voto**.',
  lei=[(PD + '85', 'A curatela afetará tão somente os atos relacionados aos direitos de natureza patrimonial e negocial.', None, 'Lei 13.146/2015, art. 85'),
       (PD + '85', 'A definição da curatela não alcança o direito ao próprio corpo', 'ao trabalho e ao voto.', 'Lei 13.146/2015, art. 85, § 1º')],
  kw=['curatela', 'patrimonial e negocial'])
I(P, 1, 'Tomada de decisão apoiada',
  'Na tomada de decisão apoiada, a pessoa com deficiência elege uma pessoa idônea, com a qual mantenha vínculos e que goze de sua confiança, para prestar-lhe apoio na tomada de decisão sobre atos da vida civil.', 'E',
  'CC, art. 1.783-A: são **pelo menos 2 (duas) pessoas** idôneas.',
  lei=[(CC + '1783-A', 'A tomada de decisão apoiada é o processo', 'exercer sua capacidade.', 'CC, art. 1.783-A')],
  kw=['tomada de decisão apoiada', 'duas pessoas'])
I(P, 1, 'Discriminação e adaptações razoáveis',
  'Considera-se discriminação em razão da deficiência toda forma de distinção, restrição ou exclusão que tenha o propósito ou o efeito de prejudicar direitos, incluindo a recusa de adaptações razoáveis e de fornecimento de tecnologias assistivas.', 'C',
  'Art. 4º, § 1º: a **recusa de adaptações razoáveis** é discriminação.',
  lei=[(PD + '4', 'Considera-se discriminação em razão da deficiência', 'tecnologias assistivas.', 'Lei 13.146/2015, art. 4º, § 1º')],
  kw=['adaptações razoáveis', 'tecnologias assistivas'])
I(P, 1, 'Especialmente vulneráveis',
  'Para os fins de proteção contra negligência, violência e tratamento desumano, são considerados especialmente vulneráveis a criança, o adolescente, a mulher e o idoso, com deficiência.', 'C',
  'Art. 5º, parágrafo único: **hipervulneráveis**.',
  lei=[(PD + '5', 'Para os fins da proteção mencionada no caput', 'com deficiência.', 'Lei 13.146/2015, art. 5º, par. ún.')],
  kw=['especialmente vulneráveis'])
I(P, 1, 'Escolas privadas',
  'As instituições privadas de ensino devem cumprir as obrigações de inclusão do Estatuto, sendo-lhes permitido repassar o custo das adaptações às mensalidades dos alunos com deficiência.', 'E',
  'Art. 28, § 1º: é **vedada a cobrança de valores adicionais** de qualquer natureza. O STF validou a regra na **ADI 5.357**.',
  lei=[(PD + '28', 'Às instituições privadas, de qualquer nível e modalidade de ensino', 'no cumprimento dessas determinações.', 'Lei 13.146/2015, art. 28, § 1º')],
  juris=[J['ADI5357']],
  kw=['instituições privadas', 'valores adicionais'])
I(P, 1, 'Tratamento forçado',
  'A pessoa com deficiência não poderá ser obrigada a se submeter a intervenção clínica ou cirúrgica, a tratamento ou a institucionalização forçada.', 'C',
  'Art. 11: **autonomia** sobre o próprio corpo; o consentimento prévio, livre e esclarecido é indispensável (art. 12).',
  lei=[(PD + '11', 'A pessoa com deficiência não poderá ser obrigada', 'institucionalização forçada.', 'Lei 13.146/2015, art. 11')],
  kw=['institucionalização forçada', 'consentimento'])
I(P, 1, 'Vagas de estacionamento',
  'Em todas as áreas de estacionamento aberto ao público devem ser reservadas vagas próximas aos acessos de circulação de pedestres, para veículos que transportem pessoa com deficiência com comprometimento de mobilidade, em percentual equivalente a cinco por cento do total.', 'E',
  'Art. 47, § 1º: **2% do total**, garantida no mínimo **1 vaga**. Os 5% são da pessoa idosa (Lei 10.741/2003, art. 41).',
  lei=[(PD + '47', 'Em todas as áreas de estacionamento aberto ao público', 'comprometimento de mobilidade', 'Lei 13.146/2015, art. 47'),
       (PD + '47', 'As vagas a que se refere o caput deste artigo devem equivaler a 2% (dois por cento) do total', 'normas técnicas vigentes de acessibilidade.', 'Lei 13.146/2015, art. 47, § 1º')],
  peg='Misturar o percentual do Estatuto da Pessoa com Deficiência (2%) com o do Estatuto da Pessoa Idosa (5%).',
  kw=['estacionamento', 'dois por cento'])
I(P, 1, 'Crime de discriminação',
  'Praticar, induzir ou incitar discriminação de pessoa em razão de sua deficiência é crime punido com detenção, de seis meses a dois anos.', 'E',
  'Art. 88: **reclusão, de 1 a 3 anos, e multa**; aumenta-se de 1/3 se a vítima estiver sob cuidado do agente.',
  lei=[(PD + '88', 'Praticar, induzir ou incitar discriminação de pessoa em razão de sua deficiência', 'e multa.', 'Lei 13.146/2015, art. 88')],
  kw=['discriminação', 'reclusão'])

# ---------------- PONTO 10 — RODADA 2
I(P, 2, 'Legitimidade na decisão apoiada',
  'O pedido de tomada de decisão apoiada será requerido pela pessoa a ser apoiada, com indicação expressa das pessoas aptas a prestarem o apoio.', 'C',
  'CC, art. 1.783-A, § 2º: legitimidade **exclusiva** da **pessoa a ser apoiada** (diferente da curatela).',
  lei=[(CC + '1783-A', 'O pedido de tomada de decisão apoiada será requerido pela pessoa a ser apoiada', 'aptas a prestarem o apoio', 'CC, art. 1.783-A, § 2º')],
  kw=['pessoa a ser apoiada'])
I(P, 2, 'Eficácia da decisão apoiada',
  'A decisão tomada por pessoa apoiada terá validade e efeitos sobre terceiros, sem restrições, desde que esteja inserida nos limites do apoio acordado.', 'C',
  'CC, art. 1.783-A, § 4º: a decisão vale perante **terceiros**, **sem restrições**, dentro dos limites do apoio acordado.',
  lei=[(CC + '1783-A', 'A decisão tomada por pessoa apoiada terá validade e efeitos sobre terceiros', 'limites do apoio acordado.', 'CC, art. 1.783-A, § 4º')],
  kw=['validade e efeitos', 'limites do apoio'])
I(P, 2, 'Fundamentação da curatela',
  'A curatela constitui medida extraordinária, devendo constar da sentença as razões e motivações de sua definição, preservados os interesses do curatelado.', 'C',
  'Art. 85, § 2º: **motivação reforçada** da sentença.',
  lei=[(PD + '85', 'A curatela constitui medida extraordinária', 'preservados os interesses do curatelado.', 'Lei 13.146/2015, art. 85, § 2º')],
  kw=['medida extraordinária', 'razões e motivações'])
I(P, 2, 'Prioridade do acompanhante',
  'O atendimento prioritário da pessoa com deficiência estende-se ao seu acompanhante ou atendente pessoal em todas as hipóteses, inclusive na tramitação processual.', 'E',
  'Art. 9º, § 1º: estende-se ao acompanhante, **exceto** quanto aos incisos **VI** (tramitação processual) e **VII** (restituição de imposto de renda).',
  lei=[(PD + '9', 'Os direitos previstos neste artigo são extensivos ao acompanhante', 'incisos VI e VII deste artigo.', 'Lei 13.146/2015, art. 9º, § 1º')],
  kw=['acompanhante', 'tramitação processual'])
I(P, 2, 'Programas habitacionais',
  'Nos programas habitacionais públicos ou subsidiados com recursos públicos, a pessoa com deficiência ou o seu responsável goza de prioridade na aquisição de imóvel, com reserva de, no mínimo, dez por cento das unidades habitacionais.', 'E',
  'Art. 32, I: reserva de, no mínimo, **3% (três por cento)** das unidades.',
  lei=[(PD + '32', 'I - reserva de, no mínimo, 3% (três por cento) das unidades habitacionais', None, 'Lei 13.146/2015, art. 32, I')],
  kw=['programas habitacionais', 'três por cento'])
I(P, 2, 'Locadoras de veículos',
  'As locadoras de veículos são obrigadas a oferecer um veículo adaptado para uso de pessoa com deficiência a cada conjunto de vinte veículos de sua frota.', 'C',
  'Art. 52: **1 a cada 20**.',
  lei=[(PD + '52', 'As locadoras de veículos são obrigadas a oferecer 1 (um) veículo adaptado', 'de sua frota.', 'Lei 13.146/2015, art. 52')],
  kw=['locadoras', 'veículo adaptado'])
I(P, 2, 'Terapias para pessoa com TEA',
  'Segundo o STJ, é abusiva a limitação, pelo plano de saúde, do número de sessões de terapia multidisciplinar prescritas ao paciente com Transtorno do Espectro Autista.', 'C',
  '**Tema 1.295/STJ**. A pessoa com TEA é considerada pessoa com deficiência para todos os efeitos legais (Lei 12.764/2012).',
  juris=[J['T1295']],
  kw=['Transtorno do Espectro Autista', 'sessões'])
I(P, 2, 'Fruição de ação afirmativa',
  'A pessoa com deficiência é obrigada a fruir dos benefícios decorrentes de ação afirmativa, como as cotas em concurso público.', 'E',
  'Art. 4º, § 2º: a pessoa com deficiência **não está obrigada** à fruição de benefícios de ação afirmativa.',
  lei=[(PD + '4', 'A pessoa com deficiência não está obrigada à fruição de benefícios decorrentes de ação afirmativa.', None, 'Lei 13.146/2015, art. 4º, § 2º')],
  kw=['ação afirmativa', 'não está obrigada'])

P = 'DBA26-CIV-11'
# ---------------- PONTO 11 · Lei 11.101/2005 — RODADA 1
I(P, 1, 'Objeto da lei',
  'A Lei 11.101/2005 disciplina a recuperação judicial, a recuperação extrajudicial e a falência do empresário e da sociedade empresária.', 'C',
  'Art. 1º: o regime alcança **empresário** e **sociedade empresária** (não as sociedades simples).',
  lei=[(RF + '1', 'Esta Lei disciplina a recuperação judicial', 'sociedade empresária', 'Lei 11.101/2005, art. 1º')],
  kw=['recuperação judicial', 'falência'])
I(P, 1, 'Exclusões da lei',
  'A Lei de Recuperação e Falência aplica-se às sociedades de economia mista, mas não às empresas públicas.', 'E',
  'Art. 2º, I: **nenhuma** das duas se sujeita à lei — nem empresa pública, nem sociedade de economia mista. Também ficam fora instituições financeiras, cooperativas de crédito, consórcios, previdência complementar, planos de saúde e seguradoras (inciso II).',
  lei=[(RF + '2', 'Esta Lei não se aplica a', 'sociedade de economia mista;', 'Lei 11.101/2005, art. 2º, I')],
  kw=['empresa pública', 'sociedade de economia mista'])
I(P, 1, 'Juízo competente',
  'É competente para homologar o plano de recuperação extrajudicial, deferir a recuperação judicial ou decretar a falência o juízo do local da sede estatutária do devedor.', 'E',
  'Art. 3º: é o juízo do **principal estabelecimento** do devedor (centro econômico) ou da filial de empresa com sede fora do Brasil.',
  lei=[(RF + '3', 'É competente para homologar o plano de recuperação extrajudicial', 'sede fora do Brasil.', 'Lei 11.101/2005, art. 3º')],
  kw=['principal estabelecimento'])
I(P, 1, 'Efeitos do deferimento',
  'A decretação da falência ou o deferimento do processamento da recuperação judicial implica a suspensão do curso da prescrição das obrigações do devedor sujeitas ao regime da lei.', 'C',
  'Art. 6º, I: **suspensão da prescrição**; também a **suspensão das execuções** e a proibição de constrições (incisos II e III).',
  lei=[(RF + '6', 'I - suspensão do curso da prescrição', 'regime desta Lei;', 'Lei 11.101/2005, art. 6º, I')],
  kw=['suspensão', 'prescrição'])
I(P, 1, 'Stay period',
  'O prazo de suspensão das execuções na recuperação judicial é de cento e oitenta dias, improrrogável.', 'E',
  'Art. 6º, § 4º: 180 dias, **prorrogáveis por igual período, uma única vez**, em caráter excepcional, desde que o devedor não haja concorrido para a superação do prazo.',
  lei=[(RF + '6', 'Na recuperação judicial, as suspensões e a proibição', 'superação do lapso temporal.', 'Lei 11.101/2005, art. 6º, § 4º')],
  kw=['stay period', 'cento e oitenta dias'])
I(P, 1, 'Requisito temporal para a recuperação',
  'Pode requerer recuperação judicial o devedor que, no momento do pedido, exerça regularmente suas atividades há mais de um ano.', 'E',
  'Art. 48: exige-se exercício regular há **mais de 2 (dois) anos**, além de não ser falido e não ter obtido recuperação há menos de 5 anos, entre outros requisitos.',
  lei=[(RF + '48', 'Poderá requerer recuperação judicial o devedor que', 'mais de 2 (dois) anos', 'Lei 11.101/2005, art. 48')],
  juris=[J['T1145']],
  exc=['Produtor rural: basta estar inscrito na Junta Comercial no momento do pedido; os 2 anos de atividade empresarial podem ser anteriores ao registro (Tema 1.145/STJ; art. 48, §§ 2º e 3º).'],
  kw=['dois anos', 'requerer recuperação judicial'])
I(P, 1, 'Créditos sujeitos',
  'Estão sujeitos à recuperação judicial todos os créditos existentes na data do pedido, ainda que não vencidos.', 'C',
  'Art. 49 + **Tema 1.051/STJ**: a existência do crédito se define pela data do seu **fato gerador**.',
  lei=[(RF + '49', 'Estão sujeitos à recuperação judicial todos os créditos existentes na data do pedido', 'ainda que não vencidos.', 'Lei 11.101/2005, art. 49')],
  juris=[J['T1051']],
  kw=['créditos existentes', 'fato gerador'])
I(P, 1, 'Credor fiduciário',
  'O credor titular da posição de proprietário fiduciário de bens móveis ou imóveis não se submete aos efeitos da recuperação judicial, prevalecendo os direitos de propriedade sobre a coisa.', 'C',
  'Art. 49, § 3º: a **alienação fiduciária** fica fora (a "trava bancária"), mas não se permite, no stay period, a retirada de **bens de capital essenciais**.',
  lei=[(RF + '49', 'Tratando-se de credor titular da posição de proprietário fiduciário', 'essenciais a sua atividade empresarial.', 'Lei 11.101/2005, art. 49, § 3º')],
  kw=['proprietário fiduciário', 'bens de capital essenciais'])
I(P, 1, 'Impontualidade',
  'Será decretada a falência do devedor que, sem relevante razão de direito, não paga, no vencimento, obrigação líquida materializada em título executivo protestado cuja soma ultrapasse o equivalente a cinquenta salários mínimos.', 'E',
  'Art. 94, I: o piso é de **40 (quarenta) salários mínimos** na data do pedido; credores podem reunir-se em litisconsórcio para atingi-lo.',
  lei=[(RF + '94', 'sem relevante razão de direito, não paga', 'na data do pedido de falência;', 'Lei 11.101/2005, art. 94, I')],
  kw=['impontualidade', 'quarenta salários mínimos'])
I(P, 1, 'Classificação dos créditos',
  'Na classificação dos créditos na falência, os derivados da legislação trabalhista, limitados a cento e cinquenta salários mínimos por credor, e os decorrentes de acidentes de trabalho precedem os créditos gravados com direito real de garantia.', 'C',
  'Art. 83: **I — trabalhistas (até 150 s.m.) e acidentários**; **II — garantia real** até o valor do bem; **III — tributários**; depois, quirografários, multas e subordinados.',
  lei=[(RF + '83', 'I - os créditos derivados da legislação trabalhista', 'acidentes de trabalho;', 'Lei 11.101/2005, art. 83, I')],
  juris=[J['T637']],
  exc=['Honorários advocatícios equiparam-se aos trabalhistas, no limite do inciso I; os devidos por serviços à massa após a quebra são extraconcursais (Tema 637/STJ).'],
  kw=['classificação', 'cento e cinquenta salários'])
I(P, 1, 'Prazo do plano de recuperação',
  'O plano de recuperação judicial será apresentado pelo devedor no prazo improrrogável de trinta dias da publicação da decisão que deferir o processamento, sob pena de convolação em falência.', 'E',
  'Art. 53: o prazo improrrogável é de **60 (sessenta) dias**.',
  lei=[(RF + '53', 'O plano de recuperação será apresentado pelo devedor em juízo', 'convolação em falência', 'Lei 11.101/2005, art. 53')],
  kw=['plano de recuperação', 'sessenta dias'])

# Acréscimo de 07/11/2026: classes, cram down, convolação, termo legal, extrajudicial.
I(P, 1, 'Classes de credores na assembleia',
  'Na assembleia-geral de credores, os titulares de créditos trabalhistas votam na classe própria apenas até o limite de cento e cinquenta salários mínimos, e pelo excedente na classe dos quirografários.', 'E',
  'Art. 41, § 1º: o trabalhista vota na classe I **com o total do crédito, independentemente do valor** (o teto de 150 salários mínimos é regra de **classificação na falência**, art. 83, I). Quem vota dividido é o credor com **garantia real**: na classe II até o valor do bem e na III pelo restante (§ 2º). São quatro classes: trabalhista, garantia real, quirografários e ME/EPP.',
  lei=[(RF + '41', 'A assembléia-geral será composta pelas seguintes classes de credores', 'microempresa ou empresa de pequeno porte.', 'Lei 11.101/2005, art. 41'),
       (RF + '41', 'Os titulares de créditos derivados da legislação do trabalho votam', 'independentemente do valor.', 'Lei 11.101/2005, art. 41, § 1º')],
  peg='Transplantar o teto de 150 salários mínimos do art. 83 para o voto na assembleia.',
  kw=['classes de credores', 'total de seu crédito'])
I(P, 1, 'Cram down',
  'O juiz pode conceder a recuperação judicial com base em plano não aprovado por todas as classes, desde que, na mesma assembleia, tenha obtido voto favorável de credores que representem mais da metade de todos os créditos presentes, aprovação de três classes (ou de duas, se só houver três votantes) e, na classe que o rejeitou, voto favorável de mais de um terço dos credores.', 'C',
  'Art. 58, § 1º: o ***cram down*** brasileiro exige requisitos **cumulativos** — maioria do valor total presente (independentemente de classes), aprovação da maioria das classes e **mais de 1/3** na classe dissidente. E só se o plano **não der tratamento diferenciado** aos credores da classe que o rejeitou (§ 2º).',
  lei=[(RF + '58', 'O juiz poderá conceder a recuperação judicial com base em plano que não obteve aprovação', 'computados na forma dos §§ 1º e 2º do art. 45 desta Lei.', 'Lei 11.101/2005, art. 58, § 1º'),
       (RF + '58', 'A recuperação judicial somente poderá ser concedida com base no § 1º', 'classe que o houver rejeitado.', 'Lei 11.101/2005, art. 58, § 2º')],
  kw=['cram down', 'um terço', 'tratamento diferenciado'])
I(P, 1, 'Convolação em falência',
  'O juiz decretará a falência durante o processo de recuperação judicial se o devedor não apresentar o plano de recuperação no prazo legal.', 'C',
  'Art. 73: a **convolação** ocorre por deliberação da assembleia, **não apresentação do plano** no prazo do art. 53, rejeição do plano dos credores, **descumprimento do plano** no período de fiscalização, descumprimento de parcelamento ou transação fiscal e **esvaziamento patrimonial** (incisos V e VI, Lei 14.112/2020).',
  lei=[(RF + '73', 'O juiz decretará a falência durante o processo de recuperação judicial:', 'no prazo do art. 53 desta Lei;', 'Lei 11.101/2005, art. 73, I e II')],
  kw=['convolação', 'não apresentação do plano'])
I(P, 1, 'Termo legal da falência',
  'A sentença que decreta a falência fixará o termo legal, podendo retrotraí-lo por até cento e oitenta dias contados do pedido de falência, do pedido de recuperação judicial ou do primeiro protesto por falta de pagamento.', 'E',
  'Art. 99, II: o termo legal retroage **no máximo 90 dias** desses marcos (excluídos os protestos cancelados). Ele importa para a **ineficácia objetiva** de pagamentos e garantias feitos dentro dele (art. 129, I a III).',
  lei=[(RF + '99', 'II – fixará o termo legal da falência', 'protestos que tenham sido cancelados;', 'Lei 11.101/2005, art. 99, II')],
  peg='Trocar 90 por 180 dias — 180 é o stay period.',
  kw=['termo legal', 'noventa dias'])
I(P, 1, 'Recuperação extrajudicial — créditos abrangidos',
  'Ficam fora da recuperação extrajudicial os créditos tributários e os do proprietário fiduciário, e a inclusão de créditos trabalhistas e por acidente de trabalho exige negociação coletiva com o sindicato da categoria.', 'C',
  'Art. 161, § 1º (Lei 14.112/2020): estão fora os **tributários**, os do **art. 49, § 3º** (fiduciário, arrendador, promitente vendedor com irrevogabilidade) e os de **adiantamento de contrato de câmbio**; trabalhistas entram só com **negociação coletiva**. O devedor precisa preencher os requisitos do art. 48.',
  lei=[(RF + '161', 'O devedor que preencher os requisitos do art. 48 desta Lei', 'plano de recuperação extrajudicial.', 'Lei 11.101/2005, art. 161'),
       (RF + '161', 'Estão sujeitos à recuperação extrajudicial todos os créditos existentes na data do pedido', 'sindicato da respectiva categoria profissional.', 'Lei 11.101/2005, art. 161, § 1º')],
  kw=['recuperação extrajudicial', 'negociação coletiva'])

# ---------------- PONTO 11 — RODADA 2
I(P, 2, 'Coobrigados e garantidores',
  'A recuperação judicial do devedor principal suspende as execuções movidas contra os avalistas e fiadores do crédito.', 'E',
  '**Súmula 581/STJ**: a recuperação **não impede o prosseguimento** das ações e execuções contra **devedores solidários e coobrigados** (garantia cambial, real ou fidejussória). Ver também art. 49, § 1º.',
  lei=[(RF + '49', 'Os credores do devedor em recuperação judicial conservam seus direitos e privilégios', 'obrigados de regresso.', 'Lei 11.101/2005, art. 49, § 1º')],
  juris=[J['S581'], J['T885']],
  kw=['coobrigados', 'avalistas'])
I(P, 2, 'Bens fora do plano',
  'O juízo da recuperação judicial não é competente para decidir sobre a constrição de bens não abrangidos pelo plano de recuperação da empresa.', 'C',
  '**Súmula 480/STJ**.',
  juris=[J['S480']],
  kw=['juízo da recuperação', 'constrição'])
I(P, 2, 'Débitos condominiais',
  'Os débitos condominiais, mesmo anteriores ao pedido de recuperação judicial, são créditos extraconcursais e podem ser executados no juízo cível competente.', 'C',
  '**Tema 1.391/STJ**: pela natureza **propter rem**, ficam fora do concurso — exceção ao critério temporal do Tema 1.051.',
  juris=[J['T1391'], J['T1051']],
  kw=['débitos condominiais', 'extraconcursais'])
I(P, 2, 'Período de fiscalização',
  'Concedida a recuperação judicial, o juiz poderá determinar a manutenção do devedor em recuperação até que sejam cumpridas todas as obrigações previstas no plano que vencerem até, no máximo, dois anos depois da concessão.', 'C',
  'Art. 61 (Lei 14.112/2020): **até 2 anos**, e agora como faculdade do juiz ("poderá"), independentemente de período de carência.',
  lei=[(RF + '61', 'Proferida a decisão prevista no art. 58 desta Lei, o juiz poderá determinar a manutenção do devedor em recuperação judicial', 'período de carência.', 'Lei 11.101/2005, art. 61')],
  kw=['dois anos', 'manutenção do devedor'])
I(P, 2, 'Extraconcursais',
  'Os créditos extraconcursais serão pagos com precedência sobre os créditos concursais classificados no art. 83 da Lei 11.101/2005.', 'C',
  'Art. 84: os **extraconcursais** vêm **antes** da ordem do art. 83.',
  lei=[(RF + '84', 'Serão considerados créditos extraconcursais', 'mencionados no art. 83 desta Lei', 'Lei 11.101/2005, art. 84')],
  kw=['extraconcursais', 'precedência'])
I(P, 2, 'Inabilitação do falido',
  'O falido fica inabilitado para exercer qualquer atividade empresarial a partir da decretação da falência e até a sentença que extingue suas obrigações.', 'C',
  'Art. 102: **inabilitação empresarial** do falido.',
  lei=[(RF + '102', 'O falido fica inabilitado para exercer qualquer atividade empresarial', 'extingue suas obrigações', 'Lei 11.101/2005, art. 102')],
  kw=['inabilitado', 'atividade empresarial'])
I(P, 2, 'Extinção das obrigações do falido',
  'Extingue as obrigações do falido o pagamento, após realizado todo o ativo, de mais de cinquenta por cento dos créditos quirografários.', 'E',
  'Art. 158, II (Lei 14.112/2020): basta o pagamento de **mais de 25%** dos quirografários; extingue também o decurso de **3 anos** da decretação, entre outras hipóteses.',
  lei=[(RF + '158', 'II - o pagamento, após realizado todo o ativo, de mais de 25%', 'para atingir a referida porcentagem', 'Lei 11.101/2005, art. 158, II')],
  kw=['extinção das obrigações', 'vinte e cinco por cento'])
I(P, 2, 'Plano especial de ME e EPP',
  'O plano especial de recuperação judicial para microempresas e empresas de pequeno porte prevê o parcelamento das dívidas em até sessenta parcelas mensais.', 'E',
  'Art. 71, II: em até **36 (trinta e seis) parcelas** mensais, iguais e sucessivas, acrescidas de juros pela SELIC.',
  lei=[(RF + '71', 'II - preverá parcelamento em até 36 (trinta e seis) parcelas mensais', None, 'Lei 11.101/2005, art. 71, II')],
  kw=['microempresas', 'trinta e seis parcelas'])
I(P, 2, 'Protesto para requerer falência',
  'A notificação do protesto, para requerimento de falência da empresa devedora, exige a identificação da pessoa que a recebeu.', 'C',
  '**Súmula 361/STJ**. E a duplicata não aceita, mas protestada e com prova da prestação dos serviços, instrui o pedido de falência (Súmula 248/STJ).',
  juris=[J['S361'], J['S248']],
  kw=['protesto', 'identificação'])

# Acréscimo de 07/11/2026: ineficácia, revocatória, efeitos da falência, extrajudicial, estatais.
I(P, 2, 'Ineficácia objetiva',
  'Para que o pagamento de dívida não vencida feito pelo devedor dentro do termo legal seja declarado ineficaz perante a massa, é indispensável provar que o credor conhecia a crise econômico-financeira do devedor.', 'E',
  'Art. 129: a ineficácia é **objetiva** — vale **tenha ou não o contratante conhecimento** da crise e **seja ou não** intenção do devedor fraudar. Pode ser declarada **de ofício**, alegada em defesa ou pleiteada em ação própria ou incidentalmente (parágrafo único). Atos gratuitos e renúncia a herança: até **2 anos** antes da quebra.',
  lei=[(RF + '129', 'São ineficazes em relação à massa falida, tenha ou não o contratante conhecimento', 'ainda que pelo desconto do próprio título;', 'Lei 11.101/2005, art. 129, I'),
       (RF + '129', 'A ineficácia poderá ser declarada de ofício pelo juiz', 'incidentalmente no curso do processo.', 'Lei 11.101/2005, art. 129, par. ún.')],
  kw=['ineficácia', 'termo legal', 'de ofício'])
I(P, 2, 'Ação revocatória',
  'A ação revocatória, que exige prova do conluio fraudulento entre o devedor e o terceiro e do efetivo prejuízo à massa, deve ser proposta pelo administrador judicial, por qualquer credor ou pelo Ministério Público no prazo de dois anos contado da decretação da falência.', 'E',
  'Arts. 130 e 132: o prazo é de **3 (três) anos** da decretação. Diferente do art. 129, a revocatória é **subjetiva**: exige **conluio fraudulento** e **efetivo prejuízo** à massa.',
  lei=[(RF + '130', 'São revogáveis os atos praticados com a intenção de prejudicar credores', 'sofrido pela massa falida.', 'Lei 11.101/2005, art. 130'),
       (RF + '132', 'A ação revocatória, de que trata o art. 130 desta Lei', 'contado da decretação da falência.', 'Lei 11.101/2005, art. 132')],
  kw=['revocatória', 'conluio fraudulento', 'três anos'])
I(P, 2, 'Contratos bilaterais na falência',
  'A decretação da falência resolve de pleno direito os contratos bilaterais do falido, cabendo ao contratante habilitar o crédito correspondente.', 'E',
  'Art. 117: os contratos bilaterais **não se resolvem** pela falência; o administrador judicial pode cumpri-los, com autorização do Comitê, se isso reduzir o passivo ou preservar ativos. Interpelado, tem 10 dias para declarar se cumpre; a recusa ou o silêncio gera **indenização como crédito quirografário** (§ 2º). A quebra, por outro lado, **antecipa o vencimento** das dívidas do devedor (art. 77).',
  lei=[(RF + '117', 'Os contratos bilaterais não se resolvem pela falência', 'mediante autorização do Comitê.', 'Lei 11.101/2005, art. 117'),
       (RF + '77', 'A decretação da falência determina o vencimento antecipado das dívidas', 'abatimento proporcional dos juros', 'Lei 11.101/2005, art. 77')],
  kw=['contratos bilaterais', 'não se resolvem', 'vencimento antecipado'])
I(P, 2, 'Recuperação extrajudicial — quórum',
  'O devedor pode requerer a homologação de plano de recuperação extrajudicial que obrigue todos os credores por ele abrangidos, desde que assinado por credores que representem mais de três quintos dos créditos de cada espécie abrangida.', 'E',
  'Art. 163 (Lei 14.112/2020): basta **mais da metade** dos créditos de cada espécie abrangida (antes eram 3/5). O pedido pode ser feito com **1/3** de adesão e compromisso de atingir o quórum em **90 dias improrrogáveis** (§ 7º), e o pedido já atrai a suspensão do art. 6º quanto às espécies abrangidas (§ 8º).',
  lei=[(RF + '163', 'O devedor poderá também requerer a homologação de plano de recuperação extrajudicial que obriga', 'abrangidos pelo plano de recuperação extrajudicial.', 'Lei 11.101/2005, art. 163'),
       (RF + '163', 'Aplica-se à recuperação extrajudicial, desde o respectivo pedido, a suspensão', 'exigido pelo § 7º deste artigo.', 'Lei 11.101/2005, art. 163, § 8º')],
  peg='O quórum antigo (3/5) ainda aparece em questões desatualizadas.',
  kw=['recuperação extrajudicial', 'mais da metade'])
I(P, 2, 'Estatais em concorrência com a iniciativa privada',
  'Para o STF, estatal que explora atividade econômica disputando mercado com empresas privadas continua fora da falência e da recuperação judicial, sendo válida a exclusão feita pela Lei 11.101/2005.', 'C',
  '**Tema 1.101/RG (2025)**: é **constitucional** o art. 2º, I — pesa o interesse público na criação da estatal e o **paralelismo das formas** (se a criação depende de lei, a extinção também).',
  lei=[(RF + '2', 'Esta Lei não se aplica a', 'sociedade de economia mista;', 'Lei 11.101/2005, art. 2º, I')],
  juris=[J['RG1101']],
  kw=['estatais', 'paralelismo das formas', 'concorrência'])

P = 'DBA26-CIV-12'
# ---------------- PONTO 12 · Jurisprudência aplicada — RODADA 1
I(P, 1, 'Legitimidade dos herdeiros para o dano moral',
  'Os herdeiros da vítima podem apenas prosseguir na ação indenizatória por danos morais já ajuizada pelo falecido, não tendo legitimidade para propô-la.', 'E',
  '**Súmula 642/STJ**: os herdeiros têm legitimidade para **ajuizar ou prosseguir** a ação.',
  juris=[J['S642']],
  kw=['herdeiros', 'ajuizar ou prosseguir'])
I(P, 1, 'Uso comercial de imagem',
  'Independe de prova do prejuízo a indenização pela publicação não autorizada de imagem de pessoa com fins econômicos ou comerciais.', 'C',
  '**Súmula 403/STJ**: dano **in re ipsa**. Base legal: CC, art. 20.',
  lei=[(CC + '20', 'Salvo se autorizadas, ou se necessárias à administração da justiça', 'se se destinarem a fins comerciais.', 'CC, art. 20')],
  juris=[J['S403']],
  kw=['imagem', 'fins econômicos'])
I(P, 1, 'Furto em estacionamento',
  'A empresa responde, perante o cliente, pela reparação de dano ou furto de veículo ocorridos em seu estacionamento.', 'C',
  '**Súmula 130/STJ**: dever de **guarda e vigilância** de quem oferece estacionamento.',
  juris=[J['S130']],
  kw=['estacionamento', 'furto de veículo'])
I(P, 1, 'Venda de veículo sem registro',
  'O antigo proprietário responde solidariamente pelos danos de acidente envolvendo veículo que alienou, enquanto não registrada a transferência.', 'E',
  '**Súmula 132/STJ**: a **ausência de registro** da transferência **não implica** a responsabilidade do antigo proprietário.',
  juris=[J['S132']],
  kw=['registro da transferência', 'antigo proprietário'])
I(P, 1, 'Locadora de veículos',
  'A empresa locadora de veículos responde, civil e solidariamente com o locatário, pelos danos por este causados a terceiro, no uso do carro locado.', 'C',
  '**Súmula 492/STF**.',
  juris=[J['STF492']],
  kw=['locadora', 'solidariamente'])
I(P, 1, 'Internação hospitalar',
  'É válida a cláusula de plano de saúde que limita no tempo a internação hospitalar, desde que redigida com destaque.', 'E',
  '**Súmula 302/STJ**: é **abusiva** a cláusula que **limita no tempo** a internação.',
  juris=[J['S302']],
  kw=['internação hospitalar', 'abusiva'])
I(P, 1, 'Carência em urgência',
  'A cláusula de plano de saúde que prevê carência para atendimento de emergência ou urgência é abusiva se ultrapassado o prazo máximo de vinte e quatro horas contado da data da contratação.', 'C',
  '**Súmula 597/STJ**: **24 horas**.',
  juris=[J['S597']],
  kw=['carência', 'vinte e quatro horas'])
I(P, 1, 'Doença preexistente',
  'É lícita a recusa de cobertura securitária sob a alegação de doença preexistente, ainda que a seguradora não tenha exigido exames médicos prévios à contratação.', 'E',
  '**Súmula 609/STJ**: a recusa é **ilícita** se não houve **exames prévios** nem prova de **má-fé** do segurado.',
  juris=[J['S609']],
  kw=['doença preexistente', 'exames médicos prévios'])
I(P, 1, 'Resolução de promessa de compra e venda',
  'Na resolução de promessa de compra e venda de imóvel submetida ao CDC, a restituição das parcelas pagas pelo comprador deve ocorrer apenas ao final da obra, ainda que a culpa seja do vendedor.', 'E',
  '**Súmula 543/STJ**: a restituição é **imediata** — **integral**, se a culpa for do vendedor ou construtor; **parcial**, se o comprador deu causa.',
  juris=[J['S543']],
  kw=['restituição imediata', 'promessa de compra e venda'])
I(P, 1, 'Hipoteca da construtora',
  'A hipoteca firmada entre a construtora e o agente financeiro, anterior ou posterior à celebração da promessa de compra e venda, não tem eficácia perante os adquirentes do imóvel.', 'C',
  '**Súmula 308/STJ**: protege o **adquirente** de boa-fé.',
  juris=[J['S308']],
  kw=['hipoteca', 'adquirentes'])
I(P, 1, 'Fiador e bem de família',
  'É válida a penhora de bem de família pertencente a fiador de contrato de locação, entendimento que o STF estendeu às locações comerciais.', 'C',
  '**Súmula 549/STJ** + **Tema 1.127/STF** (residencial ou comercial).',
  juris=[J['S549'], J['RG1127']],
  kw=['fiador', 'bem de família'])

# ---------------- PONTO 12 — RODADA 2
I(P, 2, 'Câmara de Vereadores',
  'A Câmara de Vereadores possui personalidade jurídica própria, podendo demandar em juízo na defesa de quaisquer interesses do Município.', 'E',
  '**Súmula 525/STJ**: só tem **personalidade judiciária**, para defender **direitos institucionais**.',
  juris=[J['S525']],
  kw=['personalidade judiciária', 'direitos institucionais'])
I(P, 2, 'Responsabilidade do corretor',
  'O corretor de imóveis responde solidariamente com a construtora por todos os danos causados ao consumidor em razão do descumprimento das obrigações do empreendimento.', 'E',
  'No **Tema 1.173**, o STJ decidiu que o corretor **normalmente não responde**, salvo envolvimento na incorporação ou construção, mesmo grupo econômico ou confusão/desvio patrimonial.',
  juris=[J['T1173']],
  kw=['corretor de imóveis', 'Tema 1.173'])
I(P, 2, 'Embargos de terceiro do promissário comprador',
  'É admissível a oposição de embargos de terceiro fundados em alegação de posse advinda do compromisso de compra e venda de imóvel, ainda que desprovido do registro.', 'C',
  '**Súmula 84/STJ**: protege a **posse** do promissário comprador **sem registro**.',
  juris=[J['S84']],
  kw=['embargos de terceiro', 'sem registro'])
I(P, 2, 'Curso não reconhecido',
  'As instituições de ensino superior respondem objetivamente pelos danos suportados pelo aluno pela realização de curso não reconhecido pelo Ministério da Educação, sobre o qual não lhe tenha sido dada prévia e adequada informação.', 'C',
  '**Súmula 595/STJ**: falha no dever de **informação**.',
  juris=[J['S595']],
  kw=['curso não reconhecido', 'objetivamente'])
I(P, 2, 'Penhor de joias',
  'É válida a cláusula que limita a responsabilidade da instituição financeira pelo roubo das joias entregues em garantia no contrato de penhor civil, desde que o valor de avaliação tenha sido aceito pelo consumidor.', 'E',
  '**Súmula 638/STJ**: essa cláusula é **abusiva**.',
  juris=[J['S638']],
  kw=['penhor', 'abusiva'])
I(P, 2, 'Baixa de gravame',
  'O atraso da instituição financeira na baixa do gravame de alienação fiduciária no registro do veículo caracteriza, por si só, dano moral presumido.', 'E',
  '**Tema 1.078/STJ**: o atraso, **por si só**, **não** gera dano moral in re ipsa.',
  juris=[J['T1078']],
  kw=['baixa de gravame', 'in re ipsa'])
I(P, 2, 'Escore de crédito',
  'A utilização de escore de crédito, por constituir banco de dados, depende de consentimento prévio do consumidor.', 'E',
  '**Súmula 550/STJ**: o escore é **método estatístico** que **não constitui banco de dados** e **dispensa o consentimento**; o consumidor pode pedir esclarecimentos sobre as informações consideradas.',
  juris=[J['S550']],
  kw=['escore de crédito', 'dispensa o consentimento'])
I(P, 2, 'Prescrição do DPVAT e do seguro em grupo',
  'A ação de cobrança do seguro obrigatório DPVAT prescreve em três anos, e a ação de indenização do segurado em grupo contra a seguradora, em um ano.', 'C',
  '**Súmulas 405 e 101/STJ**.',
  juris=[J['S405'], J['S101']],
  kw=['DPVAT', 'seguro em grupo'])
