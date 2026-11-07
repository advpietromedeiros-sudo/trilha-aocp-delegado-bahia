from base import I
from civ_juris import J

CC = 'L10406:'
LI = 'LINDB:'
P = 'DBA26-CIV-5'
# ---------------- PONTO 5 · Do direito de empresa — RODADA 1
I(P, 1, 'Conceito de empresário',
  'Considera-se empresário quem exerce profissionalmente atividade econômica organizada para a produção ou a circulação de bens ou de serviços, não se considerando empresário quem exerce profissão intelectual, de natureza científica, literária ou artística, salvo se o exercício da profissão constituir elemento de empresa.', 'C',
  'Art. 966: **profissionalidade** + **atividade econômica organizada**. O profissional intelectual só é empresário se a profissão for **elemento de empresa**.',
  lei=[(CC + '966', 'Considera-se empresário quem exerce profissionalmente', 'elemento de empresa.', 'CC, art. 966')],
  kw=['empresário', 'elemento de empresa'])
I(P, 1, 'Inscrição obrigatória',
  'É obrigatória a inscrição do empresário no Registro Público de Empresas Mercantis da respectiva sede, antes do início de sua atividade.', 'C',
  'Art. 967: inscrição **antes do início** da atividade. A inscrição é **declaratória** da condição de empresário (o irregular continua empresário).',
  lei=[(CC + '967', 'É obrigatória a inscrição do empresário', 'antes do início de sua atividade.', 'CC, art. 967')],
  kw=['inscrição', 'Registro Público de Empresas Mercantis'])
I(P, 1, 'Empresário rural',
  'O empresário cuja atividade rural constitua sua principal profissão é obrigado a inscrever-se no Registro Público de Empresas Mercantis.', 'E',
  'Art. 971: para o rural a inscrição é **facultativa** ("pode requerer"); feita, ele fica **equiparado** ao empresário sujeito a registro.',
  lei=[(CC + '971', 'O empresário, cuja atividade rural constitua sua principal profissão', 'sujeito a registro.', 'CC, art. 971')],
  kw=['empresário rural', 'facultativa'])
I(P, 1, 'Incapaz e atividade empresarial',
  'O incapaz pode iniciar atividade de empresário individual, desde que devidamente representado ou assistido.', 'E',
  'Art. 974: o incapaz só pode **continuar** a empresa antes exercida por ele enquanto capaz, por seus pais ou pelo autor de herança, mediante **autorização judicial**. Não pode **iniciar**.',
  lei=[(CC + '974', 'Poderá o incapaz, por meio de representante ou devidamente assistido, continuar a empresa', 'autor de herança.', 'CC, art. 974')],
  kw=['incapaz', 'continuar a empresa', 'autorização judicial'])
I(P, 1, 'Sociedade entre cônjuges',
  'Faculta-se aos cônjuges contratar sociedade, entre si ou com terceiros, desde que não tenham casado no regime da comunhão universal de bens, ou no da separação convencional.', 'E',
  'Art. 977: os regimes vedados são a **comunhão universal** e a **separação obrigatória** (não a convencional).',
  lei=[(CC + '977', 'Faculta-se aos cônjuges contratar sociedade', 'separação obrigatória.', 'CC, art. 977')],
  peg='Trocar "separação obrigatória" por "separação convencional".',
  kw=['cônjuges', 'separação obrigatória'])
I(P, 1, 'Contrato de sociedade',
  'Celebram contrato de sociedade as pessoas que reciprocamente se obrigam a contribuir, com bens ou serviços, para o exercício de atividade econômica e a partilha, entre si, dos resultados.', 'C',
  'Art. 981: **contribuição** + **atividade econômica** + **partilha dos resultados**.',
  lei=[(CC + '981', 'Celebram contrato de sociedade', 'dos resultados.', 'CC, art. 981')],
  kw=['contrato de sociedade', 'partilha'])
I(P, 1, 'Sociedade por ações e cooperativa',
  'Independentemente de seu objeto, considera-se empresária a sociedade por ações e também a cooperativa.', 'E',
  'Art. 982, parágrafo único: a sociedade por ações é **sempre empresária**; a **cooperativa** é **sempre simples**.',
  lei=[(CC + '982', 'Independentemente de seu objeto, considera-se empresária a sociedade por ações', 'simples, a cooperativa.', 'CC, art. 982, par. ún.')],
  kw=['sociedade por ações', 'cooperativa'])
I(P, 1, 'Sociedade em comum',
  'Na sociedade em comum, todos os sócios respondem solidária e ilimitadamente pelas obrigações sociais, excluído do benefício de ordem aquele que contratou pela sociedade.', 'C',
  'Art. 990: sociedade **sem registro** → responsabilidade **solidária e ilimitada**; quem **contratou** pela sociedade perde o **benefício de ordem**.',
  lei=[(CC + '990', 'Todos os sócios respondem solidária e ilimitadamente', 'contratou pela sociedade.', 'CC, art. 990')],
  kw=['sociedade em comum', 'benefício de ordem'])
I(P, 1, 'Responsabilidade na limitada',
  'Na sociedade limitada, a responsabilidade de cada sócio é restrita ao valor de suas quotas, mas todos respondem solidariamente pela integralização do capital social.', 'C',
  'Art. 1.052: limite = **quotas**, com **solidariedade** pela **integralização** do capital.',
  lei=[(CC + '1052', 'Na sociedade limitada, a responsabilidade de cada sócio', 'integralização do capital social.', 'CC, art. 1.052')],
  kw=['sociedade limitada', 'integralização'])
I(P, 1, 'Contribuição em serviços na limitada',
  'Na sociedade limitada admite-se a contribuição do sócio que consista em prestação de serviços.', 'E',
  'Art. 1.055, § 2º: é **vedada** a contribuição em **serviços** na limitada (diferente da sociedade simples, que a admite).',
  lei=[(CC + '1055', 'É vedada contribuição que consista em prestação de serviços.', None, 'CC, art. 1.055, § 2º')],
  kw=['prestação de serviços', 'vedada'])
I(P, 1, 'Estabelecimento',
  'Considera-se estabelecimento todo complexo de bens organizado, para exercício da empresa, por empresário, ou por sociedade empresária.', 'C',
  'Art. 1.142: **universalidade de fato** de bens organizados para a empresa; pode ser objeto unitário de negócios (art. 1.143).',
  lei=[(CC + '1142', 'Considera-se estabelecimento todo complexo de bens organizado', 'sociedade empresária.', 'CC, art. 1.142')],
  kw=['estabelecimento', 'complexo de bens'])
# Acréscimo de 07/11/2026 (Livro II por inteiro).
I(P, 1, 'Empresário casado e imóveis da empresa',
  'Salvo se casado no regime da separação absoluta, o empresário precisa da anuência do cônjuge para vender ou hipotecar imóvel que integre o patrimônio da empresa.', 'E',
  'Art. 978: o empresário casado aliena ou grava os imóveis da empresa **sem outorga conjugal**, **qualquer que seja o regime de bens** — exceção ao art. 1.647, I.',
  lei=[(CC + '978', 'O empresário casado pode, sem necessidade de outorga conjugal', 'gravá-los de ônus real.', 'CC, art. 978')],
  kw=['outorga conjugal', 'qualquer que seja o regime'])
I(P, 1, 'Sociedade em conta de participação',
  'Na sociedade em conta de participação, perante terceiros obrigam-se solidariamente o sócio ostensivo e o sócio participante, pois a inscrição do contrato no registro lhe confere personalidade jurídica.', 'E',
  'Arts. 991 e 993: a atividade é exercida **só pelo sócio ostensivo**, em nome próprio; perante terceiro obriga-se **apenas o ostensivo**, e o participante só perante este. A sociedade é **despersonificada** — a eventual inscrição do contrato **não** lhe dá personalidade. O participante que intervier nas relações com terceiros responde solidariamente.',
  lei=[(CC + '991', 'Obriga-se perante terceiro tão-somente o sócio ostensivo', 'nos termos do contrato social.', 'CC, art. 991, par. ún.'),
       (CC + '993', 'O contrato social produz efeito somente entre os sócios', 'personalidade jurídica à sociedade.', 'CC, art. 993')],
  kw=['sócio ostensivo', 'sócio participante', 'despersonificada'])
I(P, 1, 'Sociedade em nome coletivo',
  'Somente pessoas físicas podem tomar parte na sociedade em nome coletivo, e todos os sócios respondem solidária e ilimitadamente pelas obrigações sociais.', 'C',
  'Art. 1.039: **só pessoas físicas** e responsabilidade **solidária e ilimitada** (subsidiária ao patrimônio social, art. 1.024). Entre si, os sócios podem limitar a responsabilidade, sem efeito perante terceiros. Na **comandita simples**, só os comanditados (pessoas físicas) respondem ilimitadamente; os comanditários, pelo valor da quota (art. 1.045).',
  lei=[(CC + '1039', 'Somente pessoas físicas podem tomar parte na sociedade em nome coletivo', 'pelas obrigações sociais.', 'CC, art. 1.039'),
       (CC + '1045', 'Na sociedade em comandita simples tomam parte sócios de duas categorias', 'valor de sua quota.', 'CC, art. 1.045')],
  kw=['nome coletivo', 'pessoas físicas', 'comandita simples'])
I(P, 1, 'Cooperativa',
  'Na sociedade cooperativa, cada sócio tem direito a votos proporcionais ao valor de sua participação no capital social.', 'E',
  'Art. 1.094, VI: **um só voto por sócio**, tenha ou não capital a sociedade e qualquer que seja a participação. O quórum da assembleia se funda no **número de sócios presentes**, não no capital (inciso V); as quotas são **intransferíveis** a estranhos, ainda que por herança (inciso IV).',
  lei=[(CC + '1094', 'VI - direito de cada sócio a um só voto', 'valor de sua participação;', 'CC, art. 1.094, VI'),
       (CC + '1094', 'IV - intransferibilidade das quotas do capital', 'ainda que por herança;', 'CC, art. 1.094, IV')],
  kw=['cooperativa', 'um só voto'])
I(P, 1, 'Sociedade dependente de autorização',
  'Quando a sociedade depender de autorização do Poder Executivo para funcionar, a competência para concedê-la será sempre do Poder Executivo federal.', 'C',
  'Art. 1.123, parágrafo único: a autorização é **sempre federal**. A sociedade **estrangeira** não pode funcionar no País sem autorização, embora possa ser acionista de S.A. brasileira (art. 1.134).',
  lei=[(CC + '1123', 'A competência para a autorização será sempre do Poder Executivo federal.', None, 'CC, art. 1.123, par. ún.'),
       (CC + '1134', 'A sociedade estrangeira, qualquer que seja o seu objeto', 'acionista de sociedade anônima brasileira.', 'CC, art. 1.134')],
  kw=['autorização', 'Poder Executivo federal'])

# ---------------- PONTO 5 — RODADA 2
I(P, 2, 'Débitos no trespasse',
  'O adquirente do estabelecimento responde pelo pagamento dos débitos anteriores à transferência, desde que regularmente contabilizados, continuando o devedor primitivo solidariamente obrigado pelo prazo de cinco anos.', 'E',
  'Art. 1.146: o alienante fica solidário pelo prazo de **um ano** — dos créditos vencidos, a partir da publicação; dos outros, da data do vencimento.',
  lei=[(CC + '1146', 'O adquirente do estabelecimento responde', 'da data do vencimento.', 'CC, art. 1.146')],
  kw=['trespasse', 'um ano'])
I(P, 2, 'Cláusula de não restabelecimento',
  'Não havendo autorização expressa, o alienante do estabelecimento não pode fazer concorrência ao adquirente, nos cinco anos subsequentes à transferência.', 'C',
  'Art. 1.147: **não concorrência** implícita por **5 anos**.',
  lei=[(CC + '1147', 'Não havendo autorização expressa', 'subseqüentes à transferência.', 'CC, art. 1.147')],
  kw=['concorrência', 'cinco anos'])
I(P, 2, 'Eficácia do trespasse perante terceiros',
  'O contrato que tenha por objeto a alienação do estabelecimento só produzirá efeitos quanto a terceiros depois de averbado à margem da inscrição do empresário no Registro Público de Empresas Mercantis e de publicado na imprensa oficial.', 'C',
  'Art. 1.144: **averbação** + **publicação** na imprensa oficial.',
  lei=[(CC + '1144', 'O contrato que tenha por objeto a alienação', 'imprensa oficial.', 'CC, art. 1.144')],
  kw=['averbado', 'imprensa oficial'])
I(P, 2, 'Anuência dos credores no trespasse',
  'Se ao alienante não restarem bens suficientes para solver o seu passivo, a eficácia da alienação do estabelecimento depende do pagamento de todos os credores, ou do consentimento destes, de modo expresso ou tácito, em sessenta dias a partir de sua notificação.', 'E',
  'Art. 1.145: o prazo para o consentimento tácito é de **trinta dias** da notificação.',
  lei=[(CC + '1145', 'Se ao alienante não restarem bens suficientes', 'a partir de sua notificação.', 'CC, art. 1.145')],
  kw=['credores', 'trinta dias'])
I(P, 2, 'Limitada unipessoal',
  'A sociedade limitada exige, para sua constituição, a pluralidade de sócios, admitindo-se a unipessoalidade apenas temporária.', 'E',
  'Art. 1.052, § 1º (Lei 13.874/2019): a limitada **pode ser constituída por 1 (uma) ou mais pessoas**.',
  lei=[(CC + '1052', 'A sociedade limitada pode ser constituída por 1 (uma) ou mais pessoas.', None, 'CC, art. 1.052, § 1º')],
  kw=['unipessoal', 'uma ou mais pessoas'])
I(P, 2, 'Benefício de ordem do sócio',
  'Os bens particulares dos sócios não podem ser executados por dívidas da sociedade, senão depois de executados os bens sociais.', 'C',
  'Art. 1.024: **subsidiariedade** — primeiro o patrimônio social.',
  lei=[(CC + '1024', 'Os bens particulares dos sócios não podem ser executados', 'executados os bens sociais.', 'CC, art. 1.024')],
  kw=['bens particulares', 'bens sociais'])
I(P, 2, 'Nome empresarial',
  'O nome empresarial pode ser objeto de alienação, desde que acompanhe a transferência do estabelecimento.', 'E',
  'Art. 1.164: o nome empresarial **não pode ser objeto de alienação**. O adquirente do estabelecimento pode usar o nome do alienante **precedido do seu próprio**, com qualificação de sucessor, se o contrato permitir (parágrafo único).',
  lei=[(CC + '1164', 'O nome empresarial não pode ser objeto de alienação.', None, 'CC, art. 1.164')],
  kw=['nome empresarial', 'alienação'])
I(P, 2, 'Dissolução irregular',
  'Presume-se dissolvida irregularmente a empresa que deixar de funcionar no seu domicílio fiscal sem comunicação aos órgãos competentes, o que legitima o redirecionamento da execução fiscal para o sócio-gerente.', 'C',
  '**Súmula 435/STJ** — atenção: é regra da **execução fiscal**. Nas relações civis e empresariais o encerramento irregular, sozinho, não autoriza a desconsideração (Tema 1.210).',
  juris=[J['S435'], J['T1210']],
  kw=['dissolução irregular', 'sócio-gerente'])
# Acréscimo de 07/11/2026 (Livro II por inteiro).
I(P, 2, 'Sociedades coligadas',
  'Diz-se coligada ou filiada a sociedade de cujo capital outra sociedade participa com cinco por cento ou mais, sem controlá-la.', 'E',
  'Art. 1.099: o patamar da **filiada/coligada** é de **10% ou mais**, sem controle. Abaixo de 10% do capital votante, é de **simples participação** (art. 1.100); com maioria de votos e poder de eleger a maioria dos administradores, **controlada** (art. 1.098).',
  lei=[(CC + '1099', 'Diz-se coligada ou filiada a sociedade', 'sem controlá-la.', 'CC, art. 1.099'),
       (CC + '1100', 'É de simples participação a sociedade', 'capital com direito de voto.', 'CC, art. 1.100')],
  kw=['coligada', 'dez por cento', 'simples participação'])
I(P, 2, 'Transformação',
  'A transformação de uma sociedade em outro tipo societário pressupõe a sua prévia dissolução e liquidação.', 'E',
  'Art. 1.113: a transformação **independe de dissolução ou liquidação**; segue as regras de constituição do novo tipo. Depende do **consentimento de todos os sócios**, salvo previsão no ato constitutivo, caso em que o dissidente pode retirar-se (art. 1.114).',
  lei=[(CC + '1113', 'O ato de transformação independe de dissolução ou liquidação da sociedade', 'em que vai converter-se.', 'CC, art. 1.113'),
       (CC + '1114', 'A transformação depende do consentimento de todos os sócios', 'o disposto no art. 1.031.', 'CC, art. 1.114')],
  kw=['transformação', 'independe de dissolução'])
I(P, 2, 'Incorporação, fusão e cisão — credor prejudicado',
  'Até noventa dias após publicados os atos relativos à incorporação, fusão ou cisão, o credor anterior por ela prejudicado poderá promover judicialmente a anulação deles.', 'C',
  'Art. 1.122: **90 dias** da publicação. A **consignação em pagamento** prejudica a anulação; sendo ilíquida a dívida, a garantia da execução suspende o processo (§§ 1º e 2º). Na **incorporação** a incorporadora sucede as absorvidas (art. 1.116); na **fusão** todas se extinguem e nasce sociedade nova (art. 1.119).',
  lei=[(CC + '1122', 'Até noventa dias após publicados os atos relativos à incorporação', 'promover judicialmente a anulação deles.', 'CC, art. 1.122'),
       (CC + '1119', 'A fusão determina a extinção das sociedades que se unem', 'nos direitos e obrigações.', 'CC, art. 1.119')],
  kw=['incorporação', 'fusão', 'cisão', 'noventa dias'])
I(P, 2, 'Liquidação',
  'Não designado no contrato social, o liquidante será eleito pelos sócios, podendo a escolha recair em pessoa estranha à sociedade.', 'C',
  'Art. 1.038: o liquidante pode ser **estranho** à sociedade e destituído a todo tempo pelos sócios (se eleito por eles) ou, havendo **justa causa**, judicialmente. Em todos os atos usa a denominação seguida da cláusula **"em liquidação"** (art. 1.103, par. ún.).',
  lei=[(CC + '1038', 'Se não estiver designado no contrato social, o liquidante será eleito', 'pessoa estranha à sociedade.', 'CC, art. 1.038'),
       (CC + '1103', 'Em todos os atos, documentos ou publicações, o liquidante empregará', 'declaração de sua qualidade.', 'CC, art. 1.103, par. ún.')],
  kw=['liquidante', 'pessoa estranha', 'em liquidação'])
I(P, 2, 'Prepostos',
  'Os preponentes são responsáveis pelos atos de quaisquer prepostos praticados nos seus estabelecimentos e relativos à atividade da empresa, ainda que não autorizados por escrito.', 'C',
  'Art. 1.178: **dentro do estabelecimento**, o preponente responde mesmo sem autorização escrita; **fora dele**, só nos limites dos **poderes conferidos por escrito** (parágrafo único). O preposto responde ao preponente pelos atos **culposos** e, perante terceiros, solidariamente com ele pelos **dolosos** (art. 1.177, par. ún.).',
  lei=[(CC + '1178', 'Os preponentes são responsáveis pelos atos de quaisquer prepostos', 'ainda que não autorizados por escrito.', 'CC, art. 1.178'),
       (CC + '1177', 'No exercício de suas funções, os prepostos são pessoalmente responsáveis', 'pelos atos dolosos.', 'CC, art. 1.177, par. ún.')],
  kw=['preponente', 'preposto', 'estabelecimento'])
I(P, 2, 'Escrituração — sigilo dos livros',
  'O juiz pode, de ofício e a qualquer tempo, determinar a exibição integral dos livros e papéis de escrituração do empresário, para verificar se observam as formalidades legais.', 'E',
  'Arts. 1.190 e 1.191: vigora o **sigilo** — nenhuma autoridade, juiz ou tribunal pode ordenar diligência para verificar a regularidade dos livros, ressalvados os casos legais. A **exibição integral** só cabe em questões de **sucessão, comunhão ou sociedade, gestão à conta de outrem ou falência**; fora disso, cabe **exame parcial** (§ 1º).',
  lei=[(CC + '1190', 'Ressalvados os casos previstos em lei, nenhuma autoridade', 'as formalidades prescritas em lei.', 'CC, art. 1.190'),
       (CC + '1191', 'O juiz só poderá autorizar a exibição integral', 'ou em caso de falência.', 'CC, art. 1.191')],
  exc=['O sigilo não vale perante as autoridades fazendárias no exercício da fiscalização tributária (art. 1.193).'],
  kw=['exibição integral', 'sigilo', 'escrituração'])

P = 'DBA26-CIV-5-B2'
# ---------------- PONTO 5-B2 · Da posse — RODADA 1
I(P, 1, 'Conceito de possuidor',
  'Considera-se possuidor todo aquele que tem de fato o exercício, pleno ou não, de algum dos poderes inerentes à propriedade.', 'C',
  'Art. 1.196: o CC adota a **teoria objetiva** (Ihering) — posse é exteriorização da propriedade.',
  lei=[(CC + '1196', 'Considera-se possuidor todo aquele', 'inerentes à propriedade.', 'CC, art. 1.196')],
  kw=['possuidor', 'teoria objetiva'])
I(P, 1, 'Detenção',
  'O caseiro que conserva o imóvel em nome do proprietário e em cumprimento de suas ordens é possuidor direto e pode, cumpridos os prazos legais, adquiri-lo por usucapião.', 'E',
  'Art. 1.198: é **detentor** (fâmulo da posse) quem, em **relação de dependência**, conserva a posse em nome de outro e cumpre suas ordens. Detenção não gera usucapião.',
  lei=[(CC + '1198', 'Considera-se detentor aquele que', 'ordens ou instruções suas.', 'CC, art. 1.198')],
  kw=['detentor', 'relação de dependência'])
I(P, 1, 'Posse direta e indireta',
  'A posse direta, de pessoa que tem a coisa em seu poder temporariamente, em virtude de direito pessoal ou real, não anula a indireta, de quem aquela foi havida, podendo o possuidor direto defender a sua posse contra o indireto.', 'C',
  'Art. 1.197: **desdobramento da posse**; o possuidor direto pode defender-se **inclusive contra o indireto**.',
  lei=[(CC + '1197', 'A posse direta, de pessoa que tem a coisa em seu poder', 'defender a sua posse contra o indireto.', 'CC, art. 1.197')],
  kw=['posse direta', 'posse indireta'])
I(P, 1, 'Posse justa',
  'É justa a posse que não for violenta, clandestina ou precária.', 'C',
  'Art. 1.200: os **vícios objetivos** da posse são **violência, clandestinidade e precariedade**.',
  lei=[(CC + '1200', 'É justa a posse que não for violenta, clandestina ou precária.', None, 'CC, art. 1.200')],
  kw=['posse justa', 'violenta, clandestina ou precária'])
I(P, 1, 'Justo título e boa-fé',
  'O possuidor com justo título tem por si a presunção absoluta de boa-fé.', 'E',
  'Art. 1.201, parágrafo único: a presunção é **relativa** — vale **salvo prova em contrário**, ou quando a lei expressamente não a admite.',
  lei=[(CC + '1201', 'O possuidor com justo título tem por si a presunção de boa-fé', 'não admite esta presunção.', 'CC, art. 1.201, par. ún.')],
  kw=['justo título', 'presunção de boa-fé'])
I(P, 1, 'Atos de mera tolerância',
  'Não induzem posse os atos de mera permissão ou tolerância, assim como não autorizam a sua aquisição os atos violentos, ou clandestinos, senão depois de cessar a violência ou a clandestinidade.', 'C',
  'Art. 1.208: **permissão e tolerância** não geram posse; violência e clandestinidade impedem a posse **enquanto durarem**.',
  lei=[(CC + '1208', 'Não induzem posse os atos de mera permissão ou tolerância', 'a violência ou a clandestinidade.', 'CC, art. 1.208')],
  kw=['mera permissão ou tolerância'])
I(P, 1, 'Autotutela da posse',
  'O possuidor turbado, ou esbulhado, poderá manter-se ou restituir-se por sua própria força, contanto que o faça logo; os atos de defesa, ou de desforço, não podem ir além do indispensável à manutenção, ou restituição da posse.', 'C',
  'Art. 1.210, § 1º: **legítima defesa da posse** e **desforço imediato** — "logo" e com **moderação**.',
  lei=[(CC + '1210', 'O possuidor turbado, ou esbulhado, poderá manter-se', 'restituição da posse.', 'CC, art. 1.210, § 1º')],
  kw=['desforço imediato', 'contanto que o faça logo'])
I(P, 1, 'Exceção de domínio',
  'Obsta à manutenção ou reintegração na posse a alegação de propriedade, ou de outro direito sobre a coisa.', 'E',
  'Art. 1.210, § 2º: **não obsta** — o juízo possessório é separado do petitório (vedada a **exceção de domínio**).',
  lei=[(CC + '1210', 'Não obsta à manutenção ou reintegração na posse', 'outro direito sobre a coisa.', 'CC, art. 1.210, § 2º')],
  kw=['exceção de domínio', 'não obsta'])
I(P, 1, 'Frutos pendentes',
  'O possuidor de boa-fé tem direito aos frutos percebidos enquanto ela durar, e também aos frutos pendentes ao tempo em que cessar a boa-fé.', 'E',
  'Art. 1.214: os frutos **pendentes** ao tempo em que cessar a boa-fé **devem ser restituídos**, deduzidas as despesas da produção e custeio; também os colhidos com antecipação.',
  lei=[(CC + '1214', 'O possuidor de boa-fé tem direito, enquanto ela durar, aos frutos percebidos.', None, 'CC, art. 1.214'),
       (CC + '1214', 'Os frutos pendentes ao tempo em que cessar a boa-fé devem ser restituídos', 'colhidos com antecipação.', 'CC, art. 1.214, par. ún.')],
  peg='A AOCP já cobrou o art. 1.214; aqui a troca está no parágrafo único.',
  kw=['frutos pendentes', 'restituídos'])
I(P, 1, 'Benfeitorias do possuidor de má-fé',
  'Ao possuidor de má-fé serão ressarcidas somente as benfeitorias necessárias, assegurado o direito de retenção pela importância destas.', 'E',
  'Art. 1.220: o de má-fé recebe só as **necessárias** e **não tem direito de retenção**. O de boa-fé recebe necessárias e úteis, com retenção, e pode levantar as voluptuárias (art. 1.219).',
  lei=[(CC + '1219', 'O possuidor de boa-fé tem direito à indenização das benfeitorias necessárias e úteis', 'benfeitorias necessárias e úteis.', 'CC, art. 1.219'),
       (CC + '1220', 'Ao possuidor de má-fé serão ressarcidas somente as benfeitorias necessárias', 'voluptuárias.', 'CC, art. 1.220')],
  kw=['má-fé', 'direito de retenção'])
I(P, 1, 'Ação contra terceiro de má-fé',
  'O possuidor pode intentar a ação de esbulho, ou a de indenização, contra o terceiro que recebeu a coisa esbulhada sabendo que o era.', 'C',
  'Art. 1.212: a ação alcança o **terceiro de má-fé** (que sabia do esbulho).',
  lei=[(CC + '1212', 'O possuidor pode intentar a ação de esbulho', 'sabendo que o era.', 'CC, art. 1.212')],
  kw=['esbulho', 'terceiro'])

# ---------------- PONTO 5-B2 — RODADA 2
I(P, 2, 'Percepção dos frutos',
  'Os frutos naturais e industriais reputam-se colhidos e percebidos dia por dia, e os civis logo que são separados.', 'E',
  'Art. 1.215 inverteu-se: **naturais e industriais** → logo que **separados**; **civis** → **dia por dia**.',
  lei=[(CC + '1215', 'Os frutos naturais e industriais reputam-se colhidos', 'dia por dia.', 'CC, art. 1.215')],
  kw=['frutos civis', 'dia por dia'])
I(P, 2, 'Perda ou deterioração da coisa',
  'O possuidor de boa-fé não responde pela perda ou deterioração da coisa a que não der causa; o de má-fé responde, ainda que acidentais, salvo se provar que de igual modo se teriam dado estando ela na posse do reivindicante.', 'C',
  'Arts. 1.217 e 1.218: o de má-fé responde até pelo **fortuito**, salvo a prova de que o dano ocorreria de qualquer modo.',
  lei=[(CC + '1217', 'O possuidor de boa-fé não responde pela perda ou deterioração', 'não der causa.', 'CC, art. 1.217'),
       (CC + '1218', 'O possuidor de má-fé responde pela perda', 'na posse do reivindicante.', 'CC, art. 1.218')],
  kw=['deterioração', 'má-fé'])
I(P, 2, 'Perda da posse por quem não presenciou o esbulho',
  'Só se considera perdida a posse para quem não presenciou o esbulho quando, tendo notícia dele, se abstém de retornar a coisa, ou, tentando recuperá-la, é violentamente repelido.', 'C',
  'Art. 1.224: a posse do ausente só se perde com a **inércia** após a notícia ou com a **repulsa violenta**.',
  lei=[(CC + '1224', 'Só se considera perdida a posse para quem não presenciou o esbulho', 'violentamente repelido.', 'CC, art. 1.224')],
  kw=['esbulho', 'violentamente repelido'])
I(P, 2, 'Composse',
  'Se duas ou mais pessoas possuírem coisa indivisa, poderá cada uma exercer sobre ela atos possessórios, contanto que não excluam os dos outros compossuidores.', 'C',
  'Art. 1.199: **composse** — cada um exerce atos possessórios **sem excluir** os demais.',
  lei=[(CC + '1199', 'Se duas ou mais pessoas possuírem coisa indivisa', 'dos outros compossuidores.', 'CC, art. 1.199')],
  kw=['composse'])
I(P, 2, 'Ocupação de bem público',
  'O particular que ocupa indevidamente bem público tem posse de boa-fé e direito à indenização pelas benfeitorias necessárias que realizou.', 'E',
  '**Súmula 619/STJ**: a ocupação indevida de bem público é **mera detenção**, precária, **sem retenção nem indenização** por acessões e benfeitorias.',
  juris=[J['S619']],
  kw=['bem público', 'mera detenção'])
I(P, 2, 'Posse disputada com base no domínio',
  'Será deferida a posse a quem, evidentemente, tiver o domínio, se com base neste for ela disputada.', 'C',
  '**Súmula 487/STF**: exceção à regra do art. 1.210, § 2º — se **ambos** disputam a posse **com base no domínio**, vence quem evidentemente é o dono.',
  juris=[J['STF487']],
  kw=['domínio', 'posse disputada'])
I(P, 2, 'Posse provisória',
  'Quando mais de uma pessoa se disser possuidora, manter-se-á provisoriamente a que tiver a coisa, se não estiver manifesto que a obteve de alguma das outras por modo vicioso.', 'C',
  'Art. 1.211: proteção provisória de quem **detém a coisa**, salvo vício manifesto.',
  lei=[(CC + '1211', 'Quando mais de uma pessoa se disser possuidora', 'por modo vicioso.', 'CC, art. 1.211')],
  kw=['provisoriamente', 'modo vicioso'])
I(P, 2, 'Caráter da posse',
  'Entende-se, de forma absoluta, que a posse mantém o mesmo caráter com que foi adquirida.', 'E',
  'Art. 1.203: a presunção vale **salvo prova em contrário** — é relativa (admite-se a interversão da posse).',
  lei=[(CC + '1203', 'Salvo prova em contrário, entende-se manter a posse o mesmo caráter', None, 'CC, art. 1.203')],
  kw=['mesmo caráter', 'salvo prova em contrário'])
I(P, 2, 'Sucessão na posse',
  'O sucessor universal continua de direito a posse do seu antecessor, e ao sucessor singular é obrigatório unir sua posse à do antecessor.', 'E',
  'Art. 1.207: ao sucessor **singular** é **facultado** unir sua posse à do antecessor (*accessio possessionis*); o universal continua de direito (*successio possessionis*).',
  lei=[(CC + '1207', 'O sucessor universal continua de direito a posse', 'para os efeitos legais.', 'CC, art. 1.207')],
  kw=['sucessor singular', 'facultado'])

P = 'DBA26-CIV-6'
# ---------------- PONTO 6 · Da propriedade — RODADA 1
I(P, 1, 'Faculdades do proprietário',
  'O proprietário tem a faculdade de usar, gozar e dispor da coisa, e o direito de reavê-la do poder de quem quer que injustamente a possua ou detenha.', 'C',
  'Art. 1.228: **usar, gozar, dispor** e **reaver** (ação reivindicatória).',
  lei=[(CC + '1228', 'O proprietário tem a faculdade de usar, gozar e dispor da coisa', 'injustamente a possua ou detenha.', 'CC, art. 1.228')],
  kw=['usar, gozar e dispor', 'reaver'])
I(P, 1, 'Atos emulativos',
  'São defesos os atos que não trazem ao proprietário qualquer comodidade, ou utilidade, e sejam animados pela intenção de prejudicar outrem.', 'C',
  'Art. 1.228, § 2º: vedação dos **atos emulativos**.',
  lei=[(CC + '1228', 'São defesos os atos que não trazem ao proprietário', 'intenção de prejudicar outrem.', 'CC, art. 1.228, § 2º')],
  kw=['atos emulativos'])
I(P, 1, 'Jazidas e recursos minerais',
  'A propriedade do solo abrange a do espaço aéreo e do subsolo correspondentes, em altura e profundidade úteis ao seu exercício, incluindo as jazidas, minas e demais recursos minerais.', 'E',
  'Art. 1.230: a propriedade do solo **não abrange** jazidas, minas e recursos minerais, potenciais de energia hidráulica, monumentos arqueológicos e outros bens referidos em lei especial.',
  lei=[(CC + '1229', 'A propriedade do solo abrange a do espaço aéreo', 'úteis ao seu exercício', 'CC, art. 1.229'),
       (CC + '1230', 'A propriedade do solo não abrange as jazidas', 'leis especiais.', 'CC, art. 1.230')],
  kw=['jazidas', 'não abrange'])
I(P, 1, 'Usucapião extraordinária',
  'Aquele que, por quinze anos, sem interrupção nem oposição, possuir como seu um imóvel, adquire-lhe a propriedade, independentemente de título e boa-fé; o prazo reduz-se a dez anos se o possuidor houver estabelecido no imóvel a sua moradia habitual ou nele realizado obras ou serviços de caráter produtivo.', 'C',
  'Art. 1.238: **15 anos** sem título nem boa-fé; **10 anos** com **moradia habitual** ou **obras produtivas** (posse-trabalho).',
  lei=[(CC + '1238', 'Aquele que, por quinze anos, sem interrupção', 'caráter produtivo.', 'CC, art. 1.238')],
  kw=['usucapião extraordinária', 'quinze anos'])
I(P, 1, 'Usucapião ordinária',
  'Adquire a propriedade do imóvel aquele que, contínua e incontestadamente, com justo título e boa-fé, o possuir por quinze anos.', 'E',
  'Art. 1.242: a **ordinária** exige **justo título e boa-fé** e **dez anos**; cai para **cinco** se o imóvel foi adquirido onerosamente com base em registro depois cancelado e o possuidor nele morar ou investir.',
  lei=[(CC + '1242', 'Adquire também a propriedade do imóvel aquele que', 'por dez anos.', 'CC, art. 1.242')],
  kw=['usucapião ordinária', 'justo título e boa-fé'])
I(P, 1, 'Usucapião especial urbana',
  'Aquele que possuir como sua área urbana de até duzentos e cinquenta metros quadrados, por cinco anos ininterruptamente e sem oposição, utilizando-a para sua moradia ou de sua família, adquirir-lhe-á o domínio, desde que não seja proprietário de outro imóvel urbano ou rural.', 'C',
  'Art. 1.240 (e CF, art. 183): **250 m²**, **5 anos**, **moradia**, **não ser proprietário** de outro imóvel; o direito não se reconhece mais de uma vez.',
  lei=[(CC + '1240', 'Aquele que possuir, como sua, área urbana', 'outro imóvel urbano ou rural.', 'CC, art. 1.240')],
  kw=['usucapião especial urbana', 'duzentos e cinqüenta metros'])
I(P, 1, 'Usucapião especial rural',
  'Adquire a propriedade aquele que, não sendo proprietário de imóvel rural ou urbano, possua como sua, por cinco anos ininterruptos, sem oposição, área de terra em zona rural não superior a cem hectares, tornando-a produtiva por seu trabalho ou de sua família e nela tendo sua moradia.', 'E',
  'Art. 1.239 (e CF, art. 191): o limite é de **cinquenta hectares**.',
  lei=[(CC + '1239', 'Aquele que, não sendo proprietário de imóvel rural ou urbano', 'adquirir-lhe-á a propriedade.', 'CC, art. 1.239')],
  kw=['usucapião especial rural', 'cinqüenta hectares'])
I(P, 1, 'Usucapião familiar',
  'A usucapião por abandono do lar exige posse direta, com exclusividade, por cinco anos ininterruptos e sem oposição, sobre imóvel urbano de até duzentos e cinquenta metros quadrados cuja propriedade o possuidor divida com ex-cônjuge ou ex-companheiro.', 'E',
  'Art. 1.240-A: o prazo é de **dois anos** ininterruptos.',
  lei=[(CC + '1240-A', 'Aquele que exercer, por 2 (dois) anos ininterruptamente', 'urbano ou rural.', 'CC, art. 1.240-A')],
  kw=['usucapião familiar', 'dois anos'])
I(P, 1, 'Registro do título',
  'Transfere-se entre vivos a propriedade imóvel mediante o registro do título translativo no Registro de Imóveis; enquanto não se registrar, o alienante continua a ser havido como dono do imóvel.', 'C',
  'Art. 1.245: no Brasil, o contrato não transfere a propriedade — o **registro** é **constitutivo**.',
  lei=[(CC + '1245', 'Transfere-se entre vivos a propriedade', 'havido como dono do imóvel.', 'CC, art. 1.245, caput e § 1º')],
  kw=['registro', 'título translativo'])
I(P, 1, 'Tradição de móveis',
  'A propriedade das coisas não se transfere pelos negócios jurídicos antes da tradição.', 'C',
  'Art. 1.267: para **móveis**, o modo de aquisição derivada é a **tradição**.',
  lei=[(CC + '1267', 'A propriedade das coisas não se transfere pelos negócios jurídicos antes da tradição.', None, 'CC, art. 1.267')],
  kw=['tradição', 'móveis'])
I(P, 1, 'Usucapião de bens móveis',
  'A usucapião ordinária de coisa móvel exige posse contínua e incontestada por cinco anos, com justo título e boa-fé; a extraordinária, por dez anos, independentemente de título ou boa-fé.', 'E',
  'Arts. 1.260 e 1.261: **3 anos** (ordinária) e **5 anos** (extraordinária).',
  lei=[(CC + '1260', 'Aquele que possuir coisa móvel como sua', 'adquirir-lhe-á a propriedade.', 'CC, art. 1.260'),
       (CC + '1261', 'Se a posse da coisa móvel se prolongar por cinco anos', 'independentemente de título ou boa-fé.', 'CC, art. 1.261')],
  kw=['coisa móvel', 'três anos'])

# ---------------- PONTO 6 — RODADA 2
I(P, 2, 'Desapropriação judicial privada',
  'O proprietário pode ser privado da coisa se o imóvel reivindicado consistir em extensa área, na posse ininterrupta e de boa-fé, por mais de cinco anos, de considerável número de pessoas, e estas nela houverem realizado obras e serviços considerados pelo juiz de interesse social e econômico relevante, caso em que o juiz fixará a justa indenização devida ao proprietário.', 'C',
  'Art. 1.228, §§ 4º e 5º: **extensa área** + **posse de boa-fé por mais de 5 anos** + **considerável número de pessoas** + **obras de interesse social** → indenização ao proprietário.',
  lei=[(CC + '1228', 'O proprietário também pode ser privado da coisa', 'interesse social e econômico relevante.', 'CC, art. 1.228, § 4º'),
       (CC + '1228', 'No caso do parágrafo antecedente, o juiz fixará a justa indenização', 'em nome dos possuidores.', 'CC, art. 1.228, § 5º')],
  kw=['extensa área', 'justa indenização'])
I(P, 2, 'Usucapião como defesa',
  'A usucapião pode ser arguida em defesa, na contestação da ação reivindicatória.', 'C',
  '**Súmula 237/STF**: a **usucapião** pode ser **arguida em defesa**.',
  juris=[J['STF237']],
  kw=['usucapião', 'arguida em defesa'])
I(P, 2, 'Linha telefônica',
  'O direito de uso de linha telefônica pode ser adquirido por usucapião.', 'C',
  '**Súmula 193/STJ**: a usucapião alcança bens **incorpóreos** passíveis de posse, como o direito de uso de linha telefônica.',
  juris=[J['S193']],
  kw=['linha telefônica', 'usucapião'])
I(P, 2, 'Soma de posses',
  'O possuidor pode, para o fim de contar o tempo exigido para a usucapião, acrescentar à sua posse a dos seus antecessores, contanto que todas sejam contínuas e pacíficas.', 'C',
  'Art. 1.243: **accessio possessionis**; na ordinária, todas as posses precisam ter justo título e boa-fé.',
  lei=[(CC + '1243', 'O possuidor pode, para o fim de contar o tempo', 'com justo título e de boa-fé.', 'CC, art. 1.243')],
  kw=['acrescentar à sua posse', 'antecessores'])
I(P, 2, 'Causas suspensivas e usucapião',
  'As causas que obstam, suspendem ou interrompem a prescrição não se aplicam à usucapião, que corre contra todos.', 'E',
  'Art. 1.244: estende-se ao possuidor o disposto quanto ao devedor sobre as causas que **obstam, suspendem ou interrompem** a prescrição. Ex.: não corre usucapião entre cônjuges na constância da sociedade conjugal (art. 197, I).',
  lei=[(CC + '1244', 'Estende-se ao possuidor o disposto quanto ao devedor', 'usucapião.', 'CC, art. 1.244')],
  kw=['usucapião', 'suspendem ou interrompem'])
I(P, 2, 'Recompensa na descoberta',
  'O descobridor que restituir a coisa alheia perdida terá direito a uma recompensa não inferior a dez por cento do seu valor, além da indenização pelas despesas com a conservação e o transporte.', 'E',
  'Art. 1.234: a recompensa **não inferior a cinco por cento** do valor (achádego).',
  lei=[(CC + '1234', 'Aquele que restituir a coisa achada', 'se o dono não preferir abandoná-la.', 'CC, art. 1.234')],
  kw=['descoberta', 'cinco por cento'])
I(P, 2, 'Uso anormal da propriedade',
  'O proprietário ou o possuidor de um prédio tem o direito de fazer cessar as interferências prejudiciais à segurança, ao sossego e à saúde dos que o habitam, provocadas pela utilização de propriedade vizinha.', 'C',
  'Art. 1.277: **direito de vizinhança** — os três "S": **segurança, sossego e saúde**.',
  lei=[(CC + '1277', 'O proprietário ou o possuidor de um prédio tem o direito', 'utilização de propriedade vizinha.', 'CC, art. 1.277')],
  kw=['vizinhança', 'segurança, ao sossego e à saúde'])
I(P, 2, 'Imóvel rural abandonado',
  'O imóvel rural abandonado pelo proprietário, arrecadado como bem vago, passará, três anos depois, à propriedade do Município onde se localize.', 'E',
  'Art. 1.276, § 1º: o **rural** passa à **União**, onde quer que se localize; o **urbano**, ao Município ou ao DF (caput).',
  lei=[(CC + '1276', 'O imóvel situado na zona rural, abandonado', 'onde quer que ele se localize.', 'CC, art. 1.276, § 1º')],
  kw=['abandono', 'União'])
I(P, 2, 'Presunção de propriedade plena',
  'A propriedade presume-se plena e exclusiva, de forma absoluta, não se admitindo prova em contrário.', 'E',
  'Art. 1.231: a presunção vale **até prova em contrário** (relativa).',
  lei=[(CC + '1231', 'A propriedade presume-se plena e exclusiva, até prova em contrário.', None, 'CC, art. 1.231')],
  kw=['plena e exclusiva', 'até prova em contrário'])
I(P, 2, 'Cotas condominiais e hipoteca',
  'Na execução de crédito relativo a cotas condominiais, este tem preferência sobre o crédito hipotecário.', 'C',
  '**Súmula 478/STJ**: a obrigação **propter rem** do condômino prefere à hipoteca. E a convenção de condomínio vale entre condôminos mesmo sem registro (Súmula 260/STJ).',
  juris=[J['S478'], J['S260']],
  kw=['cotas condominiais', 'propter rem'])

P = 'DBA26-CIV-7'
# ---------------- PONTO 7 · LINDB — RODADA 1
I(P, 1, 'Vacatio legis',
  'Salvo disposição contrária, a lei começa a vigorar em todo o país quarenta e cinco dias depois de oficialmente publicada.', 'C',
  'Art. 1º: **45 dias** de *vacatio legis*, salvo disposição contrária (vigência sincrônica em todo o país).',
  lei=[(LI + '1', 'Salvo disposição contrária, a lei começa a vigorar', 'oficialmente publicada.', 'LINDB, art. 1º')],
  peg='A AOCP já cobrou o art. 1º da LINDB.',
  kw=['vacatio legis', 'quarenta e cinco dias'])
I(P, 1, 'Vigência no exterior',
  'Nos Estados estrangeiros, a obrigatoriedade da lei brasileira, quando admitida, inicia-se quarenta e cinco dias depois de oficialmente publicada.', 'E',
  'Art. 1º, § 1º: no exterior, **três meses**.',
  lei=[(LI + '1', 'Nos Estados estrangeiros, a obrigatoriedade da lei brasileira', 'três meses depois de oficialmente publicada.', 'LINDB, art. 1º, § 1º')],
  kw=['Estados estrangeiros', 'três meses'])
I(P, 1, 'Correção do texto da lei',
  'Se, antes de entrar a lei em vigor, ocorrer nova publicação de seu texto, destinada a correção, o prazo de vacatio começará a correr da nova publicação; as correções a texto de lei já em vigor consideram-se lei nova.', 'C',
  'Art. 1º, §§ 3º e 4º: correção **antes** da vigência reabre o prazo; correção **depois** é **lei nova**.',
  lei=[(LI + '1', 'Se, antes de entrar a lei em vigor, ocorrer nova publicação', 'correr da nova publicação.', 'LINDB, art. 1º, § 3º'),
       (LI + '1', 'As correções a texto de lei já em vigor consideram-se lei nova.', None, 'LINDB, art. 1º, § 4º')],
  kw=['nova publicação', 'lei nova'])
I(P, 1, 'Princípio da continuidade',
  'Não se destinando à vigência temporária, a lei terá vigor até que outra a modifique ou revogue; a lei posterior revoga a anterior quando expressamente o declare, quando seja com ela incompatível ou quando regule inteiramente a matéria de que tratava a lei anterior.', 'C',
  'Art. 2º, caput e § 1º: **continuidade** e as três formas de revogação (**expressa**, **tácita por incompatibilidade** e **global**).',
  lei=[(LI + '2', 'Não se destinando à vigência temporária', 'modifique ou revogue.', 'LINDB, art. 2º'),
       (LI + '2', 'A lei posterior revoga a anterior quando expressamente o declare', 'de que tratava a lei anterior.', 'LINDB, art. 2º, § 1º')],
  kw=['continuidade', 'revogação'])
I(P, 1, 'Repristinação',
  'A lei revogada restaura-se automaticamente quando a lei revogadora perde a vigência.', 'E',
  'Art. 2º, § 3º: **salvo disposição em contrário**, a lei revogada **não se restaura** — a repristinação só existe se **expressa**.',
  lei=[(LI + '2', 'Salvo disposição em contrário, a lei revogada não se restaura', 'perdido a vigência.', 'LINDB, art. 2º, § 3º')],
  exc=['No controle concentrado, a declaração de inconstitucionalidade da lei revogadora gera efeito repristinatório da norma anterior (fenômeno distinto da repristinação legal)'],
  kw=['repristinação', 'não se restaura'])
I(P, 1, 'Obrigatoriedade da lei',
  'Ninguém se escusa de cumprir a lei, alegando que não a conhece.', 'C',
  'Art. 3º: **inescusabilidade** do desconhecimento da lei.',
  lei=[(LI + '3', 'Ninguém se escusa de cumprir a lei', 'não a conhece.', 'LINDB, art. 3º')],
  kw=['ninguém se escusa'])
I(P, 1, 'Integração das lacunas',
  'Quando a lei for omissa, o juiz decidirá o caso de acordo com a equidade, a analogia, os costumes e os princípios gerais de direito.', 'E',
  'Art. 4º: **analogia, costumes e princípios gerais de direito**. A **equidade** só se aplica nos casos previstos em lei (CPC, art. 140, par. ún.).',
  lei=[(LI + '4', 'Quando a lei for omissa', 'princípios gerais de direito.', 'LINDB, art. 4º')],
  kw=['analogia', 'costumes', 'princípios gerais de direito'])
I(P, 1, 'Efeito imediato da lei',
  'A lei em vigor terá efeito imediato e geral, respeitados o ato jurídico perfeito, o direito adquirido e a coisa julgada.', 'C',
  'Art. 6º: **irretroatividade** com respeito ao **ato jurídico perfeito**, **direito adquirido** e **coisa julgada**.',
  lei=[(LI + '6', 'A Lei em vigor terá efeito imediato e geral', 'a coisa julgada.', 'LINDB, art. 6º')],
  kw=['efeito imediato', 'direito adquirido'])
I(P, 1, 'Estatuto pessoal',
  'A lei do país de que a pessoa for nacional determina as regras sobre o começo e o fim da personalidade, o nome, a capacidade e os direitos de família.', 'E',
  'Art. 7º: o critério é o **domicílio** (*lex domicilii*), não a nacionalidade.',
  lei=[(LI + '7', 'A lei do país em que domiciliada a pessoa', 'os direitos de família.', 'LINDB, art. 7º')],
  kw=['domicílio', 'estatuto pessoal'])
I(P, 1, 'Lei aplicável às obrigações',
  'Para qualificar e reger as obrigações, aplicar-se-á a lei do país em que se constituírem.', 'C',
  'Art. 9º: *locus regit actum* para as **obrigações**.',
  lei=[(LI + '9', 'Para qualificar e reger as obrigações', 'em que se constituirem.', 'LINDB, art. 9º')],
  peg='A AOCP já cobrou o art. 9º da LINDB.',
  kw=['obrigações', 'país em que se constituírem'])
I(P, 1, 'Sucessão no direito internacional privado',
  'A sucessão por morte ou por ausência obedece à lei do país em que estiverem situados os bens do falecido.', 'E',
  'Art. 10: obedece à lei do país em que **domiciliado** o defunto ou desaparecido, **qualquer que seja a natureza e a situação dos bens**.',
  lei=[(LI + '10', 'A sucessão por morte ou por ausência', 'a natureza e a situação dos bens.', 'LINDB, art. 10')],
  exc=['Bens de estrangeiros situados no Brasil: aplica-se a lei brasileira em benefício do cônjuge ou dos filhos brasileiros, sempre que não lhes seja mais favorável a lei pessoal do de cujus (art. 10, § 1º)'],
  kw=['sucessão', 'domiciliado o defunto'])

# ---------------- PONTO 7 — RODADA 2
I(P, 2, 'Consequências práticas da decisão',
  'Nas esferas administrativa, controladora e judicial, não se decidirá com base em valores jurídicos abstratos sem que sejam consideradas as consequências práticas da decisão.', 'C',
  'Art. 20 (Lei 13.655/2018): **consequencialismo** — a motivação deve demonstrar a necessidade e adequação da medida.',
  lei=[(LI + '20', 'Nas esferas administrativa, controladora e judicial', 'consequências práticas da decisão.', 'LINDB, art. 20')],
  kw=['valores jurídicos abstratos', 'consequências práticas'])
I(P, 2, 'Regime de transição',
  'A decisão que estabelecer interpretação ou orientação nova sobre norma de conteúdo indeterminado, impondo novo dever ou novo condicionamento de direito, deverá prever regime de transição quando indispensável para que o novo dever seja cumprido de modo proporcional, equânime e eficiente.', 'C',
  'Art. 23: **regime de transição** para mudanças de orientação.',
  lei=[(LI + '23', 'A decisão administrativa, controladora ou judicial que estabelecer interpretação', 'sem prejuízo aos interesses gerais.', 'LINDB, art. 23')],
  kw=['regime de transição'])
I(P, 2, 'Revisão e orientações da época',
  'A revisão, nas esferas administrativa, controladora ou judicial, quanto à validade de ato cuja produção já se houver completado, pode declarar inválidas situações plenamente constituídas com base em mudança posterior de orientação geral.', 'E',
  'Art. 24: a revisão leva em conta as **orientações gerais da época**, sendo **vedado** que, com base em mudança posterior de orientação geral, se declarem inválidas situações plenamente constituídas.',
  lei=[(LI + '24', 'A revisão, nas esferas administrativa, controladora ou judicial', 'situações plenamente constituídas.', 'LINDB, art. 24')],
  peg='A AOCP já cobrou o art. 24 da LINDB.',
  kw=['orientações gerais da época', 'situações plenamente constituídas'])
I(P, 2, 'Responsabilidade pessoal do agente público',
  'O agente público responderá pessoalmente por suas decisões ou opiniões técnicas em caso de dolo ou culpa, ainda que leve.', 'E',
  'Art. 28: responde em caso de **dolo ou erro grosseiro**.',
  lei=[(LI + '28', 'O agente público responderá pessoalmente', 'dolo ou erro grosseiro.', 'LINDB, art. 28')],
  peg='A AOCP já cobrou o art. 28 da LINDB; a troca é "erro grosseiro" por "culpa".',
  kw=['erro grosseiro', 'agente público'])
I(P, 2, 'Compromisso com interessados',
  'Para eliminar irregularidade, incerteza jurídica ou situação contenciosa na aplicação do direito público, a autoridade administrativa poderá, após oitiva do órgão jurídico e, quando for o caso, após realização de consulta pública, e presentes razões de relevante interesse geral, celebrar compromisso com os interessados.', 'C',
  'Art. 26: **compromisso** (acordo substitutivo), com publicidade e eficácia a partir da publicação oficial.',
  lei=[(LI + '26', 'Para eliminar irregularidade, incerteza jurídica', 'celebrar compromisso com os interessados', 'LINDB, art. 26')],
  kw=['compromisso', 'relevante interesse geral'])
I(P, 2, 'Regime de bens no DIPr',
  'O regime de bens, legal ou convencional, obedece à lei do país em que tiverem os nubentes domicílio e, se este for diverso, à do último domicílio conjugal.', 'E',
  'Art. 7º, § 4º: se os domicílios forem diversos, vale a lei do **primeiro domicílio conjugal**.',
  lei=[(LI + '7', 'O regime de bens, legal ou convencional', 'primeiro domicílio conjugal.', 'LINDB, art. 7º, § 4º')],
  kw=['regime de bens', 'primeiro domicílio conjugal'])
I(P, 2, 'Lei aplicável aos bens',
  'Para qualificar os bens e regular as relações a eles concernentes, aplicar-se-á a lei do país em que estiverem situados.', 'C',
  'Art. 8º: *lex rei sitae*.',
  lei=[(LI + '8', 'Para qualificar os bens e regular as relações a eles concernentes', 'em que estiverem situados.', 'LINDB, art. 8º')],
  kw=['lex rei sitae', 'situados'])
I(P, 2, 'Competência da autoridade brasileira',
  'É competente a autoridade judiciária brasileira quando for o réu domiciliado no Brasil ou aqui tiver de ser cumprida a obrigação, e só a ela compete conhecer das ações relativas a imóveis situados no Brasil.', 'C',
  'Art. 12, caput e § 1º: competência **concorrente** (réu domiciliado aqui ou obrigação a cumprir aqui) e **exclusiva** (imóveis no Brasil).',
  lei=[(LI + '12', 'É competente a autoridade judiciária brasileira', 'imóveis situados no Brasil.', 'LINDB, art. 12')],
  kw=['autoridade judiciária brasileira', 'imóveis situados no Brasil'])
I(P, 2, 'Segurança jurídica e instrumentos vinculantes',
  'As autoridades públicas devem atuar para aumentar a segurança jurídica na aplicação das normas, inclusive por meio de regulamentos, súmulas administrativas e respostas a consultas, instrumentos que terão caráter vinculante em relação ao órgão ou entidade a que se destinam, até ulterior revisão.', 'C',
  'Art. 30 e parágrafo único: **regulamentos, súmulas administrativas e respostas a consultas** vinculam o próprio órgão até revisão.',
  lei=[(LI + '30', 'As autoridades públicas devem atuar para aumentar a segurança jurídica', 'respostas a consultas.', 'LINDB, art. 30'),
       (LI + '30', 'Os instrumentos previstos no caput deste artigo terão caráter vinculante', 'até ulterior revisão.', 'LINDB, art. 30, par. ún.')],
  peg='A AOCP já cobrou o parágrafo único do art. 30.',
  kw=['segurança jurídica', 'caráter vinculante'])
I(P, 2, 'Interpretação teleológica',
  'Na aplicação da lei, o juiz atenderá à vontade do legislador histórico e às exigências da segurança jurídica.', 'E',
  'Art. 5º: o juiz atenderá aos **fins sociais** a que a lei se dirige e às **exigências do bem comum**.',
  lei=[(LI + '5', 'Na aplicação da lei, o juiz atenderá aos fins sociais', 'exigências do bem comum.', 'LINDB, art. 5º')],
  peg='A AOCP já cobrou o art. 5º da LINDB.',
  kw=['fins sociais', 'bem comum'])
