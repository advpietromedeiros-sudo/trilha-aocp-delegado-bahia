# Pente Fino de Legislação Penal Extravagante — LPE-6 (ECA), LPE-7 (Estatuto da Pessoa Idosa), LPE-8 (organizações
# criminosas) e LPE-9 (interceptação telefônica e captação ambiental) (08/11/2026).
from base import I
from lpe_juris import J

EC = 'L8069:'
ID = 'L10741:'
OC = 'L12850:'
IT = 'L9296:'

# ======================= LPE-6 · ECA =======================
P = 'DBA26-LPE-6'
I(P, 1, 'Criança e adolescente',
  'Para o ECA, criança é a pessoa até doze anos de idade incompletos, e adolescente, aquela entre doze e dezoito anos.', 'C',
  'Art. 2º; excepcionalmente, nos casos expressos em lei, o Estatuto alcança quem tem entre 18 e 21 anos (par. ún.).',
  lei=[(EC + '2', 'Considera-se criança, para os efeitos desta Lei, a pessoa até doze anos de idade incompletos', None, 'ECA, art. 2º')],
  kw=['doze anos de idade incompletos'])
I(P, 1, 'Idade à data do fato',
  'Para os efeitos do ECA, considera-se a idade do adolescente na data da sentença que aplica a medida socioeducativa.', 'E',
  'Art. 104, par. ún.: vale a idade **à data do fato** (teoria da atividade).',
  lei=[(EC + '104', 'Para os efeitos desta Lei, deve ser considerada a idade do adolescente à data do fato.', None, 'ECA, art. 104, par. ún.')],
  peg='Deslocar o marco para a sentença.', kw=['à data do fato'])
I(P, 1, 'Internação provisória',
  'A internação do adolescente antes da sentença pode durar, no máximo, 90 dias.', 'E',
  'Art. 108: prazo máximo de **45 dias**, com decisão fundamentada em indícios suficientes de autoria e materialidade e necessidade imperiosa.',
  lei=[(EC + '108', 'A internação, antes da sentença, pode ser determinada pelo prazo máximo de quarenta e cinco dias.', None, 'ECA, art. 108')],
  peg='Dobrar o prazo.', kw=['quarenta e cinco dias', 'internação provisória'])
I(P, 1, 'Limites da internação',
  'A internação não comporta prazo determinado, mas em nenhuma hipótese excederá três anos, e a liberação será compulsória aos vinte e um anos.', 'C',
  'Art. 121, §§ 2º, 3º e 5º: reavaliação no máximo a cada seis meses.',
  lei=[(EC + '121', 'Em nenhuma hipótese o período máximo de internação excederá a três anos.', None, 'ECA, art. 121, § 3º'), (EC + '121', 'A liberação será compulsória aos vinte e um anos de idade.', None, 'ECA, art. 121, § 5º')],
  kw=['três anos', 'vinte e um anos'])
I(P, 1, 'Tráfico e internação',
  'O ato infracional análogo ao tráfico de drogas, por ser equiparado a hediondo, autoriza por si só a internação do adolescente.', 'E',
  '**Súmula 492/STJ**: não conduz **obrigatoriamente** à internação; o art. 122 a reserva à violência ou grave ameaça, à reiteração em infrações graves e ao descumprimento reiterado.',
  lei=[(EC + '122', 'I - tratar-se de ato infracional cometido mediante grave ameaça ou violência a pessoa;', None, 'ECA, art. 122, I')],
  juris=[J['S492']], peg='Internar pela gravidade abstrata.', kw=['Súmula 492/STJ', 'art. 122'])
I(P, 1, 'Internação-sanção',
  'A internação por descumprimento reiterado e injustificável de medida anteriormente imposta não pode superar três meses e deve ser decretada judicialmente após o devido processo legal.', 'C',
  'Art. 122, III e § 1º (Lei 12.594/2012) — a chamada **internação-sanção**.',
  lei=[(EC + '122', 'não poderá ser superior a 3 (três) meses, devendo ser decretada judicialmente após o devido processo legal', None, 'ECA, art. 122, § 1º')],
  kw=['internação-sanção', '3 (três) meses'])
I(P, 1, 'Liberação aos pais',
  'Comparecendo qualquer dos pais ou responsável, o adolescente apreendido será, em regra, prontamente liberado pela autoridade policial, sob termo de compromisso de apresentá-lo ao Ministério Público.', 'C',
  'Art. 174: a liberação só não ocorre se a gravidade do ato e sua repercussão social exigirem a internação para garantia da segurança pessoal do adolescente ou da ordem pública.',
  lei=[(EC + '174', 'Comparecendo qualquer dos pais ou responsável, o adolescente será prontamente liberado pela autoridade policial', None, 'ECA, art. 174')],
  kw=['prontamente liberado', 'termo de compromisso'])
I(P, 1, 'Apresentação ao MP',
  'Não liberado o adolescente e impossível a apresentação imediata, a entidade de atendimento deve apresentá-lo ao Ministério Público em até 48 horas.', 'E',
  'Art. 175, § 1º: no prazo de **vinte e quatro horas**.',
  lei=[(EC + '175', 'que fará a apresentação ao representante do Ministério Público no prazo de vinte e quatro horas', None, 'ECA, art. 175, § 1º')],
  peg='Trocar 24 por 48 horas.', kw=['vinte e quatro horas'])
I(P, 1, 'Corrupção de menores',
  'O crime de corrupção de menores do art. 244-B do ECA é formal e dispensa prova da efetiva corrupção do menor.', 'C',
  '**Súmula 500/STJ**. A pena aumenta de 1/3 se a infração for hedionda (§ 2º).',
  lei=[(EC + '244-B', 'Corromper ou facilitar a corrupção de menor de 18 (dezoito) anos, com ele praticando infração penal ou induzindo-o a praticá-la', None, 'ECA, art. 244-B')],
  juris=[J['S500']], kw=['Súmula 500/STJ', 'delito formal'])
# --- LPE-6 · Rodada 2
I(P, 2, 'Maioridade superveniente',
  'Atingidos os 18 anos, extingue-se a medida socioeducativa de liberdade assistida em curso.', 'E',
  '**Súmula 605/STJ**: a maioridade **não interfere** na apuração nem na medida em curso, inclusive a liberdade assistida, **enquanto não atingidos 21 anos**.',
  juris=[J['S605']], peg='Extinguir a medida aos 18.', kw=['Súmula 605/STJ', '21 anos'])
I(P, 2, 'Confissão do adolescente',
  'No procedimento de apuração de ato infracional, é válida a desistência das demais provas diante da confissão do adolescente.', 'E',
  '**Súmula 342/STJ**: essa desistência é **nula**.',
  juris=[J['S342']], peg='Contentar-se com a confissão.', kw=['Súmula 342/STJ', 'nula'])
I(P, 2, 'Bebida alcoólica',
  'Fornecer bebida alcoólica a adolescente configura o crime do art. 243 do ECA, e a pena é aumentada se ele consumir o produto.', 'C',
  '**Súmula 669/STJ** (após a Lei 13.106/2015) e art. 243, par. ún. (Lei 15.234/2025): aumento de 1/3 até a metade se houver consumo.',
  lei=[(EC + '243', 'A pena será aumentada de 1/3 (um terço) até a metade se a criança ou o adolescente utilizar ou consumir o produto.', None, 'ECA, art. 243, par. ún.')],
  juris=[J['S669']], kw=['Súmula 669/STJ', 'bebida alcoólica'])
I(P, 2, 'Apreensão ilegal',
  'A apreensão de adolescente sem flagrante e sem ordem judicial escrita é infração de menor potencial ofensivo e admite transação penal.', 'E',
  'Art. 230, § 2º (Lei 15.163/2025): ao crime **não se aplica a Lei 9.099/1995**; o § 1º pune também a apreensão sem as formalidades legais.',
  lei=[(EC + '230', 'Ao crime previsto neste artigo não se aplica a Lei nº 9.099, de 26 de setembro de 1995.', None, 'ECA, art. 230, § 2º')],
  peg='Aplicar a Lei 9.099.', kw=['Lei nº 9.099', 'apreensão'])
I(P, 2, 'Visualizar conteúdo (2026)',
  'Incorre na pena do art. 241-B do ECA quem acessa ou visualiza, em aplicação de internet ou streaming, material de violência sexual contra criança ou adolescente, com o fim de satisfazer a própria lascívia ou a de outrem.', 'C',
  'Art. 241-B, § 4º (**Lei 15.487/2026**), que também passou a falar em "conteúdo de violência sexual" no lugar de "pornografia infantil".',
  lei=[(EC + '241-B', 'quem acessar ou visualizar aplicações de internet, serviços de streaming ou outra forma de registro que disponibilize material de violência sexual contra criança ou adolescente', None, 'ECA, art. 241-B, § 4º')],
  kw=['Lei 15.487/2026', 'acessar ou visualizar'])
I(P, 2, 'Aliciamento de menor de 14',
  'Aliciar, por qualquer meio, menor de 14 anos com o fim de praticar ato libidinoso é punido com detenção, de 1 a 3 anos.', 'E',
  'Art. 241-D (redação da **Lei 15.487/2026**): **reclusão, de 3 a 5 anos**, e multa, se o fato não constituir crime mais grave; a pena de 1 a 3 anos é a redação revogada.',
  lei=[(EC + '241-D', 'Pena - reclusão, de 3 (três) a 5 (cinco) anos, e multa, se o fato não constituir crime mais grave.', None, 'ECA, art. 241-D, pena')],
  peg='Citar a pena anterior a 2026.', kw=['aliciamento', 'reclusão, de 3 (três) a 5 (cinco) anos'])

# ======================= LPE-7 · Estatuto da Pessoa Idosa =======================
P = 'DBA26-LPE-7'
I(P, 1, 'Pessoa idosa',
  'O Estatuto da Pessoa Idosa protege as pessoas com idade igual ou superior a 60 anos.', 'C',
  'Art. 1º (redação da Lei 14.423/2022, que trocou "idoso" por "pessoa idosa").',
  lei=[(ID + '1', 'às pessoas com idade igual ou superior a 60 (sessenta) anos', None, 'Lei 10.741/2003, art. 1º')],
  kw=['60 (sessenta) anos'])
I(P, 1, 'Imunidades patrimoniais',
  'Nos crimes do Estatuto da Pessoa Idosa, o filho que se apropria dos proventos do pai idoso fica isento de pena pela imunidade do art. 181 do Código Penal.', 'E',
  'Art. 95: os crimes são de ação **pública incondicionada** e **não se aplicam os arts. 181 e 182** do CP.',
  lei=[(ID + '95', 'Os crimes definidos nesta Lei são de ação penal pública incondicionada, não se lhes aplicando os arts. 181 e 182 do Código Penal.', None, 'Lei 10.741/2003, art. 95')],
  peg='Aplicar a escusa absolutória.', kw=['arts. 181 e 182', 'pública incondicionada'])
I(P, 1, 'Lei 9.099 afastada',
  'Aos crimes do Estatuto da Pessoa Idosa e aos crimes praticados com violência contra a pessoa idosa, independentemente da pena prevista, não se aplica a Lei 9.099/1995.', 'C',
  'Art. 94, par. ún.: a regra nova fecha a porta aos institutos despenalizadores; o caput manda aplicar, no que couber, o CP e o CPP.',
  lei=[(ID + '94', 'independentemente da pena prevista, não se aplica a Lei nº 9.099, de 26 de setembro de 1995', None, 'Lei 10.741/2003, art. 94, par. ún.')],
  peg='Ressuscitar o rito sumaríssimo para crimes até 4 anos.', kw=['Lei nº 9.099', 'violência contra a pessoa idosa'])
I(P, 1, 'Apropriação de proventos',
  'Apropriar-se dos proventos ou da pensão da pessoa idosa, dando-lhes aplicação diversa da finalidade, é punido com detenção de 6 meses a 1 ano.', 'E',
  'Art. 102: **reclusão de 1 a 4 anos** e multa.',
  lei=[(ID + '102', 'Pena – reclusão de 1 (um) a 4 (quatro) anos e multa.', None, 'Lei 10.741/2003, art. 102, pena')],
  peg='Rebaixar a pena.', kw=['apropriação', 'reclusão de 1 (um) a 4 (quatro) anos'])
I(P, 1, 'Superendividamento',
  'Não constitui crime a negativa de crédito motivada por superendividamento da pessoa idosa.', 'C',
  'Art. 96, § 3º.',
  lei=[(ID + '96', 'Não constitui crime a negativa de crédito motivada por superendividamento da pessoa idosa.', None, 'Lei 10.741/2003, art. 96, § 3º')],
  kw=['superendividamento'])
I(P, 1, 'Retenção de cartão',
  'Reter o cartão magnético de benefício da pessoa idosa é atípico quando o objetivo for apenas assegurar o recebimento de dívida legítima.', 'E',
  'Art. 104: é crime justamente reter o cartão ou documento **com objetivo de assegurar recebimento ou ressarcimento de dívida**.',
  lei=[(ID + '104', 'Reter o cartão magnético de conta bancária relativa a benefícios, proventos ou pensão da pessoa idosa', None, 'Lei 10.741/2003, art. 104')],
  peg='Legitimar a "garantia" da dívida.', kw=['cartão magnético', 'ressarcimento de dívida'])
# --- LPE-7 · Rodada 2
I(P, 2, 'Exposição a perigo com morte',
  'Se da exposição a perigo da integridade da pessoa idosa resulta a morte, a pena é de reclusão de 8 a 14 anos.', 'C',
  'Art. 99, § 2º (Lei 15.163/2025, que elevou as penas do artigo: caput, 2 a 5 anos; lesão grave, 3 a 7).',
  lei=[(ID + '99', 'Pena - reclusão, de 8 (oito) a 14 (quatorze) anos.', None, 'Lei 10.741/2003, art. 99, § 2º')],
  kw=['resulta a morte', 'Lei 15.163/2025'])
I(P, 2, 'Omissão de socorro',
  'No crime de deixar de prestar assistência à pessoa idosa, a pena é dobrada se da omissão resulta a morte.', 'E',
  'Art. 97, par. ún.: aumenta de **metade** se resulta lesão grave e é **triplicada** se resulta morte.',
  lei=[(ID + '97', 'A pena é aumentada de metade, se da omissão resulta lesão corporal de natureza grave, e triplicada, se resulta a morte.', None, 'Lei 10.741/2003, art. 97, par. ún.')],
  peg='Trocar triplicada por dobrada.', kw=['triplicada'])
I(P, 2, 'Procuração induzida',
  'Induzir pessoa idosa sem discernimento de seus atos a outorgar procuração para administrar bens ou deles dispor livremente é crime punido com reclusão.', 'C',
  'Art. 106: reclusão de 2 a 4 anos.',
  lei=[(ID + '106', 'Induzir pessoa idosa sem discernimento de seus atos a outorgar procuração para fins de administração de bens ou deles dispor livremente', None, 'Lei 10.741/2003, art. 106')],
  kw=['procuração', 'sem discernimento'])
I(P, 2, 'Discriminação sob cuidados',
  'Na discriminação de pessoa idosa, a pena é aumentada de metade se a vítima estiver sob os cuidados ou a responsabilidade do agente.', 'E',
  'Art. 96, § 2º: aumento de **1/3**.',
  lei=[(ID + '96', 'A pena será aumentada de 1/3 (um terço) se a vítima se encontrar sob os cuidados ou responsabilidade do agente.', None, 'Lei 10.741/2003, art. 96, § 2º')],
  peg='Trocar a fração.', kw=['1/3 (um terço)', 'sob os cuidados'])

# ======================= LPE-8 · Organizações criminosas =======================
P = 'DBA26-LPE-8'
I(P, 1, 'Conceito legal',
  'Organização criminosa é a associação de 4 ou mais pessoas, estruturalmente ordenada e com divisão de tarefas, ainda que informal, voltada a infrações penais com penas máximas superiores a 4 anos ou de caráter transnacional.', 'C',
  'Art. 1º, § 1º: requisitos **cumulativos** — número, estrutura, divisão de tarefas, objetivo de vantagem e gravidade (ou transnacionalidade) das infrações.',
  lei=[(OC + '1', 'associação de 4 (quatro) ou mais pessoas estruturalmente ordenada e caracterizada pela divisão de tarefas', None, 'Lei 12.850/2013, art. 1º, § 1º'), (OC + '1', 'cujas penas máximas sejam superiores a 4 (quatro) anos, ou que sejam de caráter transnacional', None, 'Lei 12.850/2013, art. 1º, § 1º')],
  kw=['4 (quatro) ou mais pessoas', 'divisão de tarefas'])
I(P, 1, 'Número mínimo',
  'Três pessoas estruturalmente organizadas para a prática de crimes graves já configuram organização criminosa.', 'E',
  'Três pessoas formam **associação criminosa** (CP, art. 288). A **organização criminosa** exige **4 ou mais**.',
  lei=[(OC + '1', 'associação de 4 (quatro) ou mais pessoas estruturalmente ordenada', None, 'Lei 12.850/2013, art. 1º, § 1º')],
  peg='Confundir com o art. 288 do CP.', kw=['associação criminosa', '4 (quatro) ou mais'])
I(P, 1, 'Arma de fogo',
  'As penas do crime de organização criminosa aumentam-se até a metade se na atuação da organização houver emprego de arma de fogo.', 'C',
  'Art. 2º, § 2º.',
  lei=[(OC + '2', 'As penas aumentam-se até a metade se na atuação da organização criminosa houver emprego de arma de fogo.', None, 'Lei 12.850/2013, art. 2º, § 2º')],
  kw=['arma de fogo', 'até a metade'])
I(P, 1, 'Embaraço à investigação',
  'Quem embaraça investigação de infração penal que envolva organização criminosa só responde pelo crime da Lei 12.850/2013 se empregar violência ou grave ameaça.', 'E',
  'Art. 2º, § 1º (redação da Lei 15.245/2025): **impedir ou, de qualquer forma, embaraçar** já basta, se o fato não constituir crime mais grave.',
  lei=[(OC + '2', 'embaraça a investigação de infração penal que envolva organização criminosa, se o fato não constituir crime mais grave', None, 'Lei 12.850/2013, art. 2º, § 1º')],
  peg='Exigir violência.', kw=['embaraça', 'Lei 15.245/2025'])
I(P, 1, 'Benefícios da colaboração',
  'Na colaboração premiada, o juiz pode, a requerimento das partes, conceder perdão judicial, reduzir em até 2/3 a pena privativa de liberdade ou substituí-la por restritiva de direitos.', 'C',
  'Art. 4º, caput, desde que a colaboração gere ao menos um dos resultados dos incisos I a V.',
  lei=[(OC + '4', 'conceder o perdão judicial, reduzir em até 2/3 (dois terços) a pena privativa de liberdade ou substituí-la por restritiva de direitos', None, 'Lei 12.850/2013, art. 4º, caput')],
  kw=['perdão judicial', '2/3 (dois terços)'])
I(P, 1, 'Palavra do colaborador',
  'O recebimento da denúncia pode fundamentar-se apenas nas declarações do colaborador, desde que o acordo tenha sido homologado.', 'E',
  'Art. 4º, § 16 (Lei 13.964/2019): nem **cautelares**, nem **recebimento da denúncia**, nem **sentença condenatória** com base **apenas** nas declarações do colaborador.',
  lei=[(OC + '4', 'II - recebimento de denúncia ou queixa-crime;', None, 'Lei 12.850/2013, art. 4º, § 16, II')],
  peg='Bastar a delação homologada.', kw=['§ 16', 'apenas nas declarações'])
I(P, 1, 'Juiz e negociação',
  'O juiz não participa das negociações para a formalização do acordo de colaboração premiada.', 'C',
  'Art. 4º, § 6º: negociam delegado (com manifestação do MP) ou MP, o investigado e o defensor; ao juiz cabe a homologação (§ 7º).',
  lei=[(OC + '4', 'O juiz não participará das negociações realizadas entre as partes para a formalização do acordo de colaboração', None, 'Lei 12.850/2013, art. 4º, § 6º')],
  kw=['não participará das negociações'])
I(P, 1, 'Prazo da infiltração',
  'A infiltração de agentes de polícia em tarefas de investigação é autorizada por até 90 dias, vedada a renovação.', 'E',
  'Art. 10, § 3º: **até 6 meses**, **renováveis** se comprovada a necessidade. O prazo de 90 dias é o da infiltração virtual do ECA (art. 190-A).',
  lei=[(OC + '10', 'A infiltração será autorizada pelo prazo de até 6 (seis) meses, sem prejuízo de eventuais renovações, desde que comprovada sua necessidade.', None, 'Lei 12.850/2013, art. 10, § 3º')],
  peg='Misturar com o prazo do ECA.', kw=['6 (seis) meses', 'infiltração'])
I(P, 1, 'Ação controlada',
  'O retardamento da intervenção policial na ação controlada será previamente comunicado ao juiz competente, que, se for o caso, estabelecerá os seus limites.', 'C',
  'Art. 8º, § 1º: na Lei 12.850/2013 basta **comunicação prévia** (não autorização); na Lei de Drogas, a ação controlada exige autorização judicial (art. 53).',
  lei=[(OC + '8', 'O retardamento da intervenção policial ou administrativa será previamente comunicado ao juiz competente', None, 'Lei 12.850/2013, art. 8º, § 1º')],
  kw=['ação controlada', 'previamente comunicado'])
I(P, 1, 'Silêncio do colaborador',
  'Nos depoimentos que prestar, o colaborador mantém o direito ao silêncio e não assume o compromisso de dizer a verdade.', 'E',
  'Art. 4º, § 14: o colaborador **renuncia**, na presença do defensor, ao **direito ao silêncio** e fica sujeito ao **compromisso legal de dizer a verdade**.',
  lei=[(OC + '4', 'o colaborador renunciará, na presença de seu defensor, ao direito ao silêncio e estará sujeito ao compromisso legal de dizer a verdade', None, 'Lei 12.850/2013, art. 4º, § 14')],
  peg='Tratar o colaborador como acusado comum.', kw=['direito ao silêncio', 'renunciará'])
# --- LPE-8 · Rodada 2
I(P, 2, 'Natureza do acordo',
  'O acordo de colaboração premiada é negócio jurídico processual e meio de obtenção de prova, que pressupõe utilidade e interesse públicos.', 'C',
  'Art. 3º-A (Lei 13.964/2019).',
  lei=[(OC + '3-A', 'O acordo de colaboração premiada é negócio jurídico processual e meio de obtenção de prova, que pressupõe utilidade e interesse públicos.', None, 'Lei 12.850/2013, art. 3º-A')],
  kw=['negócio jurídico processual', 'meio de obtenção de prova'])
I(P, 2, 'Colaboração após a sentença',
  'Se a colaboração for posterior à sentença, a pena poderá ser reduzida em até 2/3.', 'E',
  'Art. 4º, § 5º: **até a metade**, ou progressão de regime ainda que ausentes os requisitos objetivos.',
  lei=[(OC + '4', 'Se a colaboração for posterior à sentença, a pena poderá ser reduzida até a metade', None, 'Lei 12.850/2013, art. 4º, § 5º')],
  peg='Repetir a fração do caput.', kw=['posterior à sentença', 'até a metade'])
I(P, 2, 'Dados cadastrais',
  'O delegado de polícia e o Ministério Público têm acesso, independentemente de autorização judicial, aos dados cadastrais do investigado que informem exclusivamente a qualificação pessoal, a filiação e o endereço.', 'C',
  'Art. 15: o acesso direto é **restrito** a esses dados; o conteúdo de comunicações segue sob reserva de jurisdição.',
  lei=[(OC + '15', 'O delegado de polícia e o Ministério Público terão acesso, independentemente de autorização judicial, apenas aos dados cadastrais do investigado', None, 'Lei 12.850/2013, art. 15')],
  kw=['dados cadastrais', 'independentemente de autorização judicial'])
I(P, 2, 'Crime do infiltrado',
  'Não é punível, no âmbito da infiltração, a prática de crime pelo agente infiltrado no curso da investigação, quando inexigível conduta diversa.', 'C',
  'Art. 13, par. ún.: excludente de **culpabilidade**; os excessos desproporcionais são punidos (caput).',
  lei=[(OC + '13', 'Não é punível, no âmbito da infiltração, a prática de crime pelo agente infiltrado no curso da investigação, quando inexigível conduta diversa.', None, 'Lei 12.850/2013, art. 13, par. ún.')],
  kw=['inexigível conduta diversa', 'agente infiltrado'])
I(P, 2, 'Organização voltada a crimes do ECA (2026)',
  'Se a organização criminosa é destinada ao cometimento de crimes do ECA, a pena é aumentada até a metade.', 'E',
  'Art. 2º, § 4º, I (redação da **Lei 15.487/2026**): o aumento é de **1/6 a 2/3**, o mesmo da participação de criança ou adolescente.',
  lei=[(OC + '2', 'A pena é aumentada de 1/6 (um sexto) a 2/3 (dois terços):', None, 'Lei 12.850/2013, art. 2º, § 4º'), (OC + '2', 'ou se a organização criminosa é destinada ao cometimento dos crimes previstos na Lei nº 8.069', None, 'Lei 12.850/2013, art. 2º, § 4º, I')],
  peg='Trocar a fração.', kw=['Lei 15.487/2026', '1/6 (um sexto) a 2/3'])
I(P, 2, 'Infiltração virtual',
  'A infiltração virtual de agentes na Lei 12.850/2013 pode ser renovada sem limite total, enquanto comprovada a necessidade.', 'E',
  'Art. 10-A, § 4º: períodos de até 6 meses, desde que o **total não exceda 720 dias**.',
  lei=[(OC + '10-A', 'desde que o total não exceda a 720 (setecentos e vinte) dias', None, 'Lei 12.850/2013, art. 10-A, § 4º')],
  peg='Eternizar a infiltração.', kw=['720 (setecentos e vinte) dias', 'infiltração virtual'])

# ======================= LPE-9 · Interceptação e captação ambiental =======================
P = 'DBA26-LPE-9'
I(P, 1, 'Crime punido com detenção',
  'Não se admite interceptação telefônica quando o fato investigado constituir infração penal punida, no máximo, com pena de detenção.', 'C',
  'Art. 2º, III: a interceptação só cabe para crimes punidos com **reclusão**.',
  lei=[(IT + '2', 'III - o fato investigado constituir infração penal punida, no máximo, com pena de detenção.', None, 'Lei 9.296/1996, art. 2º, III')],
  kw=['detenção', 'reclusão'])
I(P, 1, 'Prazo da interceptação',
  'A interceptação telefônica não pode exceder 30 dias, renovável por igual período.', 'E',
  'Art. 5º: **quinze dias**, renovável por igual tempo uma vez comprovada a indispensabilidade (a renovação pode ser sucessiva, com fundamentação).',
  lei=[(IT + '5', 'que não poderá exceder o prazo de quinze dias, renovável por igual tempo uma vez comprovada a indispensabilidade do meio de prova', None, 'Lei 9.296/1996, art. 5º')],
  peg='Dobrar o prazo.', kw=['quinze dias', 'indispensabilidade'])
I(P, 1, 'Telemática',
  'A Lei 9.296/1996 aplica-se também à interceptação do fluxo de comunicações em sistemas de informática e telemática.', 'C',
  'Art. 1º, par. ún.',
  lei=[(IT + '1', 'aplica-se à interceptação do fluxo de comunicações em sistemas de informática e telemática', None, 'Lei 9.296/1996, art. 1º, par. ún.')],
  kw=['telemática'])
I(P, 1, 'Pedido verbal',
  'Excepcionalmente, o juiz pode admitir que o pedido de interceptação seja formulado verbalmente, condicionada a concessão à sua redução a termo.', 'C',
  'Art. 4º, § 1º; o juiz decide em até 24 horas (§ 2º).',
  lei=[(IT + '4', 'Excepcionalmente, o juiz poderá admitir que o pedido seja formulado verbalmente', None, 'Lei 9.296/1996, art. 4º, § 1º')],
  kw=['verbalmente', 'redução a termo'])
I(P, 1, 'Subsidiariedade',
  'A interceptação telefônica pode ser deferida mesmo que a prova possa ser feita por outros meios disponíveis, se for o meio mais rápido.', 'E',
  'Art. 2º, II: **não** se admite quando a prova puder ser feita por **outros meios disponíveis** — é medida **subsidiária** (ultima ratio).',
  lei=[(IT + '2', 'II - a prova puder ser feita por outros meios disponíveis;', None, 'Lei 9.296/1996, art. 2º, II')],
  peg='Trocar subsidiariedade por conveniência.', kw=['subsidiária', 'outros meios disponíveis'])
I(P, 1, 'Crime de interceptação ilegal',
  'Realizar interceptação de comunicações telefônicas sem autorização judicial é crime punido com detenção, de 6 meses a 2 anos.', 'E',
  'Art. 10 (redação da Lei 13.869/2019): **reclusão, de 2 a 4 anos**, e multa — incorre na mesma pena o juiz que determina a medida com objetivo não autorizado em lei.',
  lei=[(IT + '10', 'Pena - reclusão, de 2 (dois) a 4 (quatro) anos, e multa.', None, 'Lei 9.296/1996, art. 10, pena')],
  peg='Rebaixar a pena.', kw=['reclusão, de 2 (dois) a 4 (quatro) anos'])
I(P, 1, 'Autos apartados',
  'A interceptação ocorre em autos apartados, apensados aos do inquérito ou do processo, preservando-se o sigilo das diligências, gravações e transcrições.', 'C',
  'Art. 8º.',
  lei=[(IT + '8', 'ocorrerá em autos apartados, apensados aos autos do inquérito policial ou do processo criminal', None, 'Lei 9.296/1996, art. 8º')],
  kw=['autos apartados', 'sigilo'])
# --- LPE-9 · Rodada 2
I(P, 2, 'Captação por interlocutor',
  'Não há crime se a captação ambiental é realizada por um dos interlocutores.', 'C',
  'Art. 10-A, § 1º (Lei 13.964/2019).',
  lei=[(IT + '10-A', 'Não há crime se a captação é realizada por um dos interlocutores.', None, 'Lei 9.296/1996, art. 10-A, § 1º')],
  kw=['um dos interlocutores', 'captação ambiental'])
I(P, 2, 'Requisitos da captação ambiental',
  'A captação ambiental pode ser autorizada para investigar infrações cuja pena mínima seja superior a 4 anos.', 'E',
  'Art. 8º-A, II: exige infrações cujas **penas máximas** sejam **superiores a 4 anos** (ou conexas), além da impossibilidade de prova por outros meios igualmente eficazes.',
  lei=[(IT + '8-A', 'cujas penas máximas sejam superiores a 4 (quatro) anos ou em infrações penais conexas', None, 'Lei 9.296/1996, art. 8º-A, II')],
  peg='Trocar pena máxima por mínima.', kw=['penas máximas', 'captação ambiental'])
I(P, 2, 'Gravação clandestina',
  'A captação ambiental feita por um dos interlocutores sem o prévio conhecimento da autoridade policial ou do Ministério Público pode ser usada pela acusação, se demonstrada a integridade da gravação.', 'E',
  'Art. 8º-A, § 4º (veto derrubado): o uso previsto é **em matéria de defesa**.',
  lei=[(IT + '8-A', 'poderá ser utilizada, em matéria de defesa, quando demonstrada a integridade da gravação', None, 'Lei 9.296/1996, art. 8º-A, § 4º')],
  peg='Trocar defesa por acusação.', kw=['em matéria de defesa'])
I(P, 2, 'Inutilização',
  'A gravação que não interessar à prova será inutilizada por decisão judicial, a requerimento do MP ou da parte interessada, facultada a presença do acusado ou de seu representante.', 'C',
  'Art. 9º e parágrafo único.',
  lei=[(IT + '9', 'A gravação que não interessar à prova será inutilizada por decisão judicial', None, 'Lei 9.296/1996, art. 9º')],
  kw=['inutilizada', 'decisão judicial'])
I(P, 2, 'Prazo para decidir',
  'O juiz decidirá sobre o pedido de interceptação telefônica no prazo máximo de quarenta e oito horas.', 'E',
  'Art. 4º, § 2º: **vinte e quatro horas**.',
  lei=[(IT + '4', 'O juiz, no prazo máximo de vinte e quatro horas, decidirá sobre o pedido.', None, 'Lei 9.296/1996, art. 4º, § 2º')],
  kw=['vinte e quatro horas'])
