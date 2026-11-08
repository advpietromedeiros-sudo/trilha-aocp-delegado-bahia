# Pente Fino de Legislação Penal Extravagante — LPE-21 (identificação criminal), LPE-22 (Lei 12.830/2013), LPE-23
# (economia popular), LPE-24 (genocídio), LPE-25 (Lei 8.176/1991), LPE-26 (propriedade industrial), LPE-27
# (transplantes), LPE-28 (programa de computador), LPE-29 (lavagem de dinheiro) e LPE-30 (proteção a vítimas e
# testemunhas) (08/11/2026). LPE-26 e LPE-28 evitam repetir os temas do PEN-10.3 e 10.4 (mesmas leis).
from base import I
from lpe_juris import J

IC = 'L12037:'
DP = 'L12830:'
EP = 'L1521:'
GE = 'L2889:'
OE = 'L8176:'
PI = 'L9279:'
TR = 'L9434:'
SW = 'L9609:'
LV = 'L9613:'
PT = 'L9807:'

# ======================= LPE-21 · Identificação criminal =======================
P = 'DBA26-LPE-21'
I(P, 1, 'Regra geral',
  'O civilmente identificado não será submetido a identificação criminal, salvo nos casos previstos na Lei 12.037/2009.', 'C',
  'Art. 1º (CF, art. 5º, LVIII).',
  lei=[(IC + '1', 'O civilmente identificado não será submetido a identificação criminal, salvo nos casos previstos nesta Lei.', None, 'Lei 12.037/2009, art. 1º')],
  kw=['civilmente identificado'])
I(P, 1, 'Documento militar',
  'Para os fins da Lei 12.037/2009, equiparam-se aos documentos de identificação civil os documentos de identificação militares.', 'C',
  'Art. 2º, par. ún.',
  lei=[(IC + '2', 'equiparam-se aos documentos de identificação civis os documentos de identificação militares', None, 'Lei 12.037/2009, art. 2º, par. ún.')],
  kw=['identificação militares'])
I(P, 1, 'Essencial às investigações',
  'Quando a identificação criminal for essencial às investigações, o delegado de polícia pode determiná-la por despacho próprio, ainda que o investigado apresente documento idôneo.', 'E',
  'Art. 3º, IV: depende de **despacho da autoridade judiciária**, de ofício ou mediante representação do delegado, do MP ou da defesa.',
  lei=[(IC + '3', 'segundo despacho da autoridade judiciária competente, que decidirá de ofício ou mediante representação da autoridade policial', None, 'Lei 12.037/2009, art. 3º, IV')],
  peg='Atribuir ao delegado a decisão.', kw=['autoridade judiciária', 'essencial às investigações'])
I(P, 1, 'Atestado de antecedentes',
  'A identificação criminal do indiciado pode constar de atestados de antecedentes antes do trânsito em julgado, se houver inquérito em curso.', 'E',
  'Art. 6º: é **vedado** mencioná-la em atestados de antecedentes ou informações não destinadas ao juízo criminal **antes do trânsito em julgado**.',
  lei=[(IC + '6', 'É vedado mencionar a identificação criminal do indiciado em atestados de antecedentes', None, 'Lei 12.037/2009, art. 6º')],
  peg='Liberar a menção.', kw=['atestados de antecedentes'])
I(P, 1, 'Recebimento da denúncia (2025)',
  'Embora apresentado documento de identificação, poderá ocorrer identificação criminal quando houver recebimento da denúncia por crime praticado com grave violência contra a pessoa ou por crime contra a liberdade sexual.', 'C',
  'Art. 3º, VII (**Lei 15.295/2025**), que também inclui crimes do ECA e organização criminosa armada; nesses casos, coleta-se material biológico (art. 5º, § 1º).',
  lei=[(IC + '3', 'VII – houver recebimento da denúncia pelo juiz por:', None, 'Lei 12.037/2009, art. 3º, VII'), (IC + '3', 'a) crime praticado com grave violência contra a pessoa;', None, 'Lei 12.037/2009, art. 3º, VII, a')],
  kw=['Lei 15.295/2025', 'recebimento da denúncia'])
# --- LPE-21 · Rodada 2
I(P, 2, 'Perfil genético',
  'Nas hipóteses de identificação criminal essencial às investigações e de recebimento de denúncia pelos crimes do art. 3º, VII, a identificação incluirá a coleta de material biológico para obtenção do perfil genético.', 'C',
  'Art. 5º, § 1º (Lei 15.295/2025).',
  lei=[(IC + '5', 'Nas hipóteses dos incisos IV e VII do caput do art. 3º, a identificação criminal incluirá a coleta de material biológico', None, 'Lei 12.037/2009, art. 5º, § 1º')],
  kw=['material biológico', 'perfil genético'])
I(P, 2, 'Exclusão do perfil',
  'Em caso de condenação, o perfil genético é excluído do banco de dados, mediante requerimento, após 10 anos do cumprimento da pena.', 'E',
  'Art. 7º-A, II (Lei 13.964/2019): após **20 anos**; na absolvição, a exclusão é imediata (I).',
  lei=[(IC + '7-A', 'após decorridos 20 (vinte) anos do cumprimento da pena', None, 'Lei 12.037/2009, art. 7º-A, II')],
  peg='Trocar 20 por 10 anos.', kw=['20 (vinte) anos', 'exclusão'])
I(P, 2, 'Traços revelados',
  'As informações genéticas dos bancos de perfis genéticos podem revelar traços comportamentais das pessoas, se úteis à investigação.', 'E',
  'Art. 5º-A, § 1º: **não** podem revelar traços somáticos ou comportamentais, **exceto a determinação genética de gênero**.',
  lei=[(IC + '5-A', 'não poderão revelar traços somáticos ou comportamentais das pessoas, exceto determinação genética de gênero', None, 'Lei 12.037/2009, art. 5º-A, § 1º')],
  peg='Ampliar o uso dos dados.', kw=['traços somáticos ou comportamentais'])

# ======================= LPE-22 · Investigação criminal pelo delegado (Lei 12.830/2013) =======================
P = 'DBA26-LPE-22'
I(P, 1, 'Natureza das funções',
  'As funções de polícia judiciária e a apuração de infrações penais exercidas pelo delegado de polícia são de natureza jurídica, essenciais e exclusivas de Estado.', 'C',
  'Art. 2º, caput.',
  lei=[(DP + '2', 'são de natureza jurídica, essenciais e exclusivas de Estado', None, 'Lei 12.830/2013, art. 2º')],
  kw=['natureza jurídica', 'exclusivas de Estado'])
I(P, 1, 'Indiciamento',
  'O indiciamento, privativo do delegado de polícia, dar-se-á por ato fundamentado, mediante análise técnico-jurídica do fato, indicando autoria, materialidade e circunstâncias.', 'C',
  'Art. 2º, § 6º: por ser **privativo** do delegado, a lei não o atribui ao juiz nem ao MP.',
  lei=[(DP + '2', 'O indiciamento, privativo do delegado de polícia, dar-se-á por ato fundamentado, mediante análise técnico-jurídica do fato', None, 'Lei 12.830/2013, art. 2º, § 6º')],
  kw=['indiciamento', 'análise técnico-jurídica'])
I(P, 1, 'Avocação do inquérito',
  'O inquérito policial em curso pode ser avocado pelo membro do Ministério Público que exerce o controle externo da atividade policial.', 'E',
  'Art. 2º, § 4º: só pode ser avocado ou redistribuído por **superior hierárquico**, mediante **despacho fundamentado**, por interesse público ou inobservância de procedimentos que prejudique a investigação.',
  lei=[(DP + '2', 'somente poderá ser avocado ou redistribuído por superior hierárquico, mediante despacho fundamentado', None, 'Lei 12.830/2013, art. 2º, § 4º')],
  peg='Atribuir a avocação ao MP.', kw=['superior hierárquico', 'avocado'])
I(P, 1, 'Remoção',
  'A remoção do delegado de polícia é ato discricionário da administração, dispensada motivação.', 'E',
  'Art. 2º, § 5º: dar-se-á **somente por ato fundamentado** — garantia contra remoção como retaliação.',
  lei=[(DP + '2', 'A remoção do delegado de polícia dar-se-á somente por ato fundamentado.', None, 'Lei 12.830/2013, art. 2º, § 5º')],
  peg='Dispensar motivação.', kw=['remoção', 'ato fundamentado'])
I(P, 1, 'Bacharel em Direito',
  'O cargo de delegado de polícia é privativo de bacharel em Direito, devendo-lhe ser dispensado o mesmo tratamento protocolar dos magistrados, membros da Defensoria, do MP e advogados.', 'C',
  'Art. 3º.',
  lei=[(DP + '3', 'O cargo de delegado de polícia é privativo de bacharel em Direito', None, 'Lei 12.830/2013, art. 3º')],
  kw=['bacharel em Direito', 'tratamento protocolar'])
# --- LPE-22 · Rodada 2
I(P, 2, 'Poder de requisição',
  'Durante a investigação criminal, cabe ao delegado de polícia a requisição de perícia, informações, documentos e dados que interessem à apuração dos fatos.', 'C',
  'Art. 2º, § 2º (respeitada a reserva de jurisdição).',
  lei=[(DP + '2', 'cabe ao delegado de polícia a requisição de perícia, informações, documentos e dados que interessem à apuração dos fatos', None, 'Lei 12.830/2013, art. 2º, § 2º')],
  kw=['requisição', 'perícia'])
I(P, 2, 'Investigação pelo MP',
  'A Lei 12.830/2013 tornou a investigação criminal atribuição exclusiva da polícia judiciária, vedada a investigação pelo Ministério Público.', 'E',
  '**Tema 184/RG** (STF, 14/05/2015): o MP pode investigar por autoridade própria, por prazo razoável, sob controle jurisdicional. A lei trata da investigação **conduzida pelo delegado**.',
  juris=[J['RG184']], peg='Ler exclusividade na lei.', kw=['Tema 184', 'Ministério Público'])
I(P, 2, 'Termo circunstanciado',
  'A lavratura de termo circunstanciado é atribuição privativa do delegado de polícia, por ser ato de polícia judiciária.', 'E',
  'STF, **ADI 5.637** (11/03/2022): o TC **não tem natureza investigativa** nem é privativo da polícia judiciária; lei estadual pode permitir sua lavratura pela PM.',
  juris=[J['ADI5637']], peg='Tornar o TC privativo.', kw=['ADI 5.637', 'termo circunstanciado'])

# ======================= LPE-23 · Crimes contra a economia popular =======================
P = 'DBA26-LPE-23'
I(P, 1, 'Competência',
  'Compete à Justiça dos Estados, em ambas as instâncias, o processo e o julgamento dos crimes contra a economia popular.', 'C',
  '**Súmula 498/STF**.',
  juris=[J['STF498']], kw=['Súmula 498/STF', 'Justiça dos Estados'])
I(P, 1, 'Pirâmide financeira',
  'Obter ganhos ilícitos em detrimento de número indeterminado de pessoas mediante especulações ou processos fraudulentos, como "bola de neve" e "cadeias", é crime contra a economia popular.', 'C',
  'Art. 2º, IX — o enquadramento usual das pirâmides financeiras.',
  lei=[(EP + '2', 'mediante especulações ou processos fraudulentos ("bola de neve", "cadeias", "pichardismo" e quaisquer outros equivalentes)', None, 'Lei 1.521/1951, art. 2º, IX')],
  kw=['bola de neve', 'pirâmide'])
I(P, 1, 'Usura',
  'A cobrança de juros acima da taxa permitida por lei é mero ilícito civil, sem repercussão penal.', 'E',
  'Art. 4º, a: a **usura pecuniária** é crime contra a economia popular (detenção, de 6 meses a 2 anos, e multa).',
  lei=[(EP + '4', 'Constitui crime da mesma natureza a usura pecuniária ou real', None, 'Lei 1.521/1951, art. 4º')],
  peg='Negar a tipicidade da usura.', kw=['usura pecuniária'])
I(P, 1, 'Pena do art. 2º',
  'Os crimes do art. 2º da Lei 1.521/1951 são punidos com reclusão, de 2 a 10 anos.', 'E',
  'Art. 2º: **detenção, de 6 meses a 2 anos**, e multa. A pena de 2 a 10 anos (detenção) é a do art. 3º.',
  lei=[(EP + '2', 'Pena - detenção, de 6 (seis) meses a 2 (dois) anos, e multa', None, 'Lei 1.521/1951, art. 2º, pena')],
  peg='Trocar as penas dos arts. 2º e 3º.', kw=['detenção, de 6 (seis) meses a 2 (dois) anos'])
I(P, 1, 'Notícias falsas',
  'Provocar a alta ou a baixa de preços de mercadorias, títulos públicos ou valores por meio de notícias falsas ou operações fictícias é crime contra a economia popular.', 'C',
  'Art. 3º, VI.',
  lei=[(EP + '3', 'VI - provocar a alta ou baixa de preços de mercadorias, títulos públicos, valores ou salários por meio de notícias falsas', None, 'Lei 1.521/1951, art. 3º, VI')],
  kw=['notícias falsas', 'alta ou baixa de preços'])
# --- LPE-23 · Rodada 2
I(P, 2, 'Usura real',
  'Constitui usura obter, abusando da premente necessidade, inexperiência ou leviandade da outra parte, lucro patrimonial que exceda o quinto do valor justo da prestação.', 'C',
  'Art. 4º, b.',
  lei=[(EP + '4', 'lucro patrimonial que exceda o quinto do valor corrente ou justo da prestação feita ou prometida', None, 'Lei 1.521/1951, art. 4º, b')],
  kw=['usura real', 'quinto do valor'])
I(P, 2, 'Agravante da usura',
  'É agravante do crime de usura o cometimento em detrimento de maior de 60 anos.', 'E',
  'Art. 4º, § 2º, IV, b: em detrimento de operário ou agricultor, **menor de 18 anos** ou deficiente mental.',
  lei=[(EP + '4', 'de menor de 18 (dezoito) anos ou de deficiente mental, interditado ou não', None, 'Lei 1.521/1951, art. 4º, § 2º, IV, b')],
  peg='Trocar a vítima qualificada.', kw=['menor de 18', 'agravantes'])
I(P, 2, 'Pena do art. 3º',
  'Os crimes contra a economia popular do art. 3º da Lei 1.521/1951, como reter matérias-primas para dominar o mercado, são punidos com reclusão de 1 a 4 anos.', 'E',
  'Art. 3º, pena: **detenção, de 2 a 10 anos**, e multa.',
  lei=[(EP + '3', 'Pena - detenção, de 2 (dois) anos a 10 (dez) anos', None, 'Lei 1.521/1951, art. 3º, pena')],
  kw=['detenção, de 2 (dois) anos a 10 (dez) anos'])

# ======================= LPE-24 · Genocídio =======================
P = 'DBA26-LPE-24'
I(P, 1, 'Dolo específico',
  'Comete genocídio quem, com a intenção de destruir, no todo ou em parte, grupo nacional, étnico, racial ou religioso, como tal, mata membros do grupo.', 'C',
  'Art. 1º, a, com as penas do homicídio qualificado.',
  lei=[(GE + '1', 'com a intenção de destruir, no todo ou em parte, grupo nacional, étnico, racial ou religioso, como tal', None, 'Lei 2.889/1956, art. 1º')],
  kw=['intenção de destruir', 'grupo nacional, étnico, racial ou religioso'])
I(P, 1, 'Grupo político',
  'A Lei 2.889/1956 protege também os grupos políticos contra atos de genocídio.', 'E',
  'Art. 1º: só grupos **nacional, étnico, racial ou religioso** — o grupo político ficou de fora, como na Convenção de 1948.',
  lei=[(GE + '1', 'grupo nacional, étnico, racial ou religioso', None, 'Lei 2.889/1956, art. 1º')],
  peg='Incluir grupo político.', kw=['grupo político'])
I(P, 1, 'Associação para genocídio',
  'Associarem-se duas ou mais pessoas para a prática de genocídio é crime punido com metade da pena dos crimes visados.', 'E',
  'Art. 2º: exige que se associem **mais de 3** pessoas (quatro ou mais).',
  lei=[(GE + '2', 'Associarem-se mais de 3 (três) pessoas para prática dos crimes mencionados no artigo anterior', None, 'Lei 2.889/1956, art. 2º')],
  peg='Reduzir o número mínimo.', kw=['mais de 3 (três) pessoas'])
I(P, 1, 'Extradição',
  'Os crimes de genocídio não são considerados crimes políticos para efeitos de extradição.', 'C',
  'Art. 6º.',
  lei=[(GE + '6', 'Os crimes de que trata esta lei não serão considerados crimes políticos para efeitos de extradição.', None, 'Lei 2.889/1956, art. 6º')],
  kw=['extradição', 'crimes políticos'])
I(P, 1, 'Transferência de crianças',
  'Efetuar a transferência forçada de crianças do grupo para outro grupo, com a intenção de destruí-lo, é forma de genocídio.', 'C',
  'Art. 1º, e (pena do art. 148 do CP).',
  lei=[(GE + '1', 'e) efetuar a transferência forçada de crianças do grupo para outro grupo;', None, 'Lei 2.889/1956, art. 1º, e')],
  kw=['transferência forçada de crianças'])
# --- LPE-24 · Rodada 2
I(P, 2, 'Incitação consumada',
  'A pena pela incitação ao genocídio será a mesma do crime incitado, se este se consumar.', 'C',
  'Art. 3º, § 1º; sem consumação, metade das penas (caput).',
  lei=[(GE + '3', 'A pena pelo crime de incitação será a mesma de crime incitado, se este se consumar.', None, 'Lei 2.889/1956, art. 3º, § 1º')],
  kw=['incitação', 'se este se consumar'])
I(P, 2, 'Governante',
  'As penas do genocídio, da associação e da incitação são aumentadas de metade quando o crime for cometido por governante ou funcionário público.', 'E',
  'Art. 4º: agravadas de **1/3**.',
  lei=[(GE + '4', 'A pena será agravada de 1/3 (um terço), no caso dos arts. 1º, 2º e 3º, quando cometido o crime por governante ou funcionário público.', None, 'Lei 2.889/1956, art. 4º')],
  peg='Trocar a fração.', kw=['governante', '1/3 (um terço)'])
I(P, 2, 'Incitação pela imprensa',
  'A pena da incitação ao genocídio é aumentada de 1/3 quando cometida pela imprensa.', 'C',
  'Art. 3º, § 2º.',
  lei=[(GE + '3', 'A pena será aumentada de 1/3 (um terço), quando a incitação for cometida pela imprensa.', None, 'Lei 2.889/1956, art. 3º, § 2º')],
  kw=['imprensa'])

# ======================= LPE-25 · Lei 8.176/1991 (ordem econômica e combustíveis) =======================
P = 'DBA26-LPE-25'
I(P, 1, 'Combustíveis em desacordo',
  'Adquirir, distribuir e revender derivados de petróleo e demais combustíveis em desacordo com as normas legais é crime contra a ordem econômica, punido com detenção de um a cinco anos.', 'C',
  'Art. 1º, I.',
  lei=[(OE + '1', 'I - adquirir, distribuir e revender derivados de petróleo', None, 'Lei 8.176/1991, art. 1º, I'), (OE + '1', 'Pena: detenção de um a cinco anos.', None, 'Lei 8.176/1991, art. 1º, pena')],
  kw=['combustíveis', 'detenção de um a cinco anos'])
I(P, 1, 'Usurpação de bens da União',
  'Produzir bens ou explorar matéria-prima pertencentes à União sem autorização legal é crime contra o patrimônio, na modalidade de usurpação.', 'C',
  'Art. 2º (ex.: extração clandestina de minério); incorre na mesma pena quem adquire ou comercializa o produto (§ 1º).',
  lei=[(OE + '2', 'Constitui crime contra o patrimônio, na modalidade de usurpacão, produzir bens ou explorar matéria-prima pertencentes à União', None, 'Lei 8.176/1991, art. 2º')],
  kw=['usurpação', 'matéria-prima pertencentes à União'])
I(P, 1, 'Comércio de combustível ilícito (2026)',
  'O crime do art. 1º-A da Lei 8.176/1991, que pune o comércio e a guarda de combustível de origem ilícita, tem pena de detenção de um a cinco anos.', 'E',
  'Art. 1º-A (**Lei 15.517/2026**): **reclusão, de 3 a 8 anos**, e multa.',
  lei=[(OE + '1-A', 'Pena: reclusão, de 3 (três) a 8 (oito) anos, e multa.', None, 'Lei 8.176/1991, art. 1º-A, pena')],
  peg='Usar a pena do art. 1º.', kw=['Lei 15.517/2026', 'reclusão, de 3 (três) a 8 (oito) anos'])
I(P, 1, 'Autor do crime antecedente',
  'O crime do art. 1º-A da Lei 8.176/1991 é punível ainda que desconhecido ou isento de pena o autor do crime de que proveio a coisa.', 'C',
  'Art. 1º-A, § 2º (Lei 15.517/2026) — lógica da receptação.',
  lei=[(OE + '1-A', 'é punível ainda que desconhecido ou isento de pena o autor do crime de que proveio a coisa', None, 'Lei 8.176/1991, art. 1º-A, § 2º')],
  kw=['desconhecido ou isento de pena'])
I(P, 1, 'Perda do cargo',
  'A condenação pelos crimes dos arts. 1º-A e 1º-B da Lei 8.176/1991 não gera perda do cargo público, que depende de processo administrativo.', 'E',
  'Art. 1º-C (Lei 15.517/2026): a condenação **terá como efeito a perda** do cargo, função ou emprego público, com inabilitação pelo dobro do prazo da pena.',
  lei=[(OE + '1-C', 'a condenação terá como efeito a perda do cargo, da função ou do emprego público', None, 'Lei 8.176/1991, art. 1º-C')],
  peg='Negar o efeito.', kw=['perda do cargo', 'Lei 15.517/2026'])
# --- LPE-25 · Rodada 2
I(P, 2, 'GLP automotivo (2026)',
  'Usar gás liquefeito de petróleo para fins automotivos, em desacordo com as normas estabelecidas na forma da lei, é crime contra a ordem econômica.', 'C',
  'Art. 1º, II (redação da **Lei 15.348/2026**).',
  lei=[(OE + '1', 'II - usar gás liquefeito de petróleo para fins automotivos, em desacordo com as normas estabelecidas na forma da lei.', None, 'Lei 8.176/1991, art. 1º, II')],
  kw=['gás liquefeito de petróleo'])
I(P, 2, 'Primário no art. 1º-B',
  'No crime do art. 1º-B da Lei 8.176/1991, sendo o agente primário, o juiz pode diminuir a pena de 1/3 a 2/3 ou deixar de aplicar a multa.', 'C',
  'Art. 1º-B, § 1º (Lei 15.517/2026) — paralelo à receptação culposa/privilegiada.',
  lei=[(OE + '1-B', 'Se o agente é primário, poderá o juiz, consideradas as circunstâncias e as consequências do crime, diminuir a pena de 1/3 (um terço) a 2/3 (dois terços) ou deixar de aplicar a multa.', None, 'Lei 8.176/1991, art. 1º-B, § 1º')],
  kw=['primário', '1/3 (um terço) a 2/3'])
I(P, 2, 'Interdição do estabelecimento',
  'Constitui efeito da condenação pelo art. 1º-A da Lei 8.176/1991 a interdição do estabelecimento pelo mesmo prazo da pena aplicada.', 'E',
  'Art. 1º-A, § 3º: pelo **dobro** do prazo da pena.',
  lei=[(OE + '1-A', 'Constitui efeito da condenação a interdição do estabelecimento pelo dobro do prazo da pena aplicada.', None, 'Lei 8.176/1991, art. 1º-A, § 3º')],
  peg='Trocar o dobro pelo mesmo prazo.', kw=['interdição do estabelecimento', 'dobro'])

# ======================= LPE-26 · Propriedade industrial (Lei 9.279/1996) =======================
P = 'DBA26-LPE-26'
I(P, 1, 'Patente de invenção',
  'Comete crime contra patente quem fabrica, sem autorização do titular, produto que seja objeto de patente de invenção ou de modelo de utilidade.', 'C',
  'Art. 183, I (detenção, de 3 meses a 1 ano, ou multa).',
  lei=[(PI + '183', 'I - fabrica produto que seja objeto de patente de invenção ou de modelo de utilidade, sem autorização do titular', None, 'Lei 9.279/1996, art. 183, I')],
  kw=['patente de invenção', 'modelo de utilidade'])
I(P, 1, 'Produto com marca imitada',
  'Comete crime contra registro de marca quem vende ou tem em estoque produto assinalado com marca ilicitamente reproduzida ou imitada.', 'C',
  'Art. 190, I.',
  lei=[(PI + '190', 'I - produto assinalado com marca ilicitamente reproduzida ou imitada, de outrem, no todo ou em parte', None, 'Lei 9.279/1996, art. 190, I')],
  kw=['marca ilicitamente reproduzida'])
I(P, 1, 'Corrupção de empregado do concorrente',
  'Dar ou prometer dinheiro a empregado de concorrente para que, faltando ao dever do emprego, proporcione vantagem é crime de concorrência desleal.', 'C',
  'Art. 195, IX; o empregado que aceita responde pelo inciso X.',
  lei=[(PI + '195', 'IX - dá ou promete dinheiro ou outra utilidade a empregado de concorrente', None, 'Lei 9.279/1996, art. 195, IX')],
  kw=['concorrência desleal', 'empregado de concorrente'])
I(P, 1, 'Ação penal nos crimes contra marca',
  'Os crimes contra registro de marca da Lei 9.279/1996 são de ação penal pública incondicionada, por lesarem o consumidor.', 'E',
  'Art. 199: nos crimes da LPI **somente se procede mediante queixa**; a exceção é o art. 191 (brasões e distintivos oficiais), de ação pública.',
  lei=[(PI + '199', 'Nos crimes previstos neste Título somente se procede mediante queixa', None, 'Lei 9.279/1996, art. 199')],
  peg='Tornar pública a ação.', kw=['mediante queixa'])
I(P, 1, 'Multa na LPI',
  'A multa nos crimes contra a propriedade industrial pode ser aumentada ou reduzida até o triplo, conforme as condições do agente.', 'E',
  'Art. 197: de 10 a 360 dias-multa, que podem ser aumentados ou reduzidos **em até 10 vezes**, conforme as condições pessoais e a vantagem auferida.',
  lei=[(PI + '197', 'A multa poderá ser aumentada ou reduzida, em até 10 (dez) vezes', None, 'Lei 9.279/1996, art. 197, par. ún.')],
  peg='Usar a regra do CP.', kw=['10 (dez) vezes', 'multa'])
# --- LPE-26 · Rodada 2
I(P, 2, 'Apreensão alfandegária',
  'Produtos assinalados com marcas falsificadas podem ser apreendidos de ofício pelas autoridades alfandegárias, no ato de conferência.', 'C',
  'Art. 198.',
  lei=[(PI + '198', 'Poderão ser apreendidos, de ofício ou a requerimento do interessado, pelas autoridades alfandegárias, no ato de conferência', None, 'Lei 9.279/1996, art. 198')],
  kw=['autoridades alfandegárias', 'de ofício'])
I(P, 2, 'Segredo industrial',
  'Nos crimes de divulgação ou uso não autorizado de informações confidenciais da empresa, incluem-se como autores possíveis o empregador, o sócio ou o administrador.', 'C',
  'Art. 195, § 1º (incisos XI e XII).',
  lei=[(PI + '195', 'Inclui-se nas hipóteses a que se referem os incisos XI e XII o empregador, sócio ou administrador da empresa', None, 'Lei 9.279/1996, art. 195, § 1º')],
  kw=['informações confidenciais', 'empregador, sócio ou administrador'])
I(P, 2, 'Comércio de produto pirata patenteado',
  'Vender produto fabricado com violação de patente de invenção é punido com reclusão, de 2 a 4 anos.', 'E',
  'Art. 184: **detenção, de 1 a 3 meses, ou multa** — os crimes da LPI são de menor potencial ofensivo.',
  lei=[(PI + '184', 'Pena - detenção, de 1 (um) a 3 (três) meses, ou multa.', None, 'Lei 9.279/1996, art. 184, pena')],
  peg='Inflar a pena.', kw=['detenção, de 1 (um) a 3 (três) meses'])

# ======================= LPE-27 · Lei de Transplantes =======================
P = 'DBA26-LPE-27'
I(P, 1, 'Comércio de órgãos',
  'Comprar ou vender tecidos, órgãos ou partes do corpo humano é crime punido com reclusão, de 3 a 8 anos, e multa.', 'C',
  'Art. 15 (CF, art. 199, § 4º, veda a comercialização).',
  lei=[(TR + '15', 'Comprar ou vender tecidos, órgãos ou partes do corpo humano:', None, 'Lei 9.434/1997, art. 15'), (TR + '15', 'Pena - reclusão, de três a oito anos', None, 'Lei 9.434/1997, art. 15, pena')],
  kw=['comprar ou vender', 'órgãos'])
I(P, 1, 'Intermediação',
  'Incorre na pena do comércio de órgãos quem promove, intermedeia, facilita ou aufere qualquer vantagem com a transação.', 'C',
  'Art. 15, par. ún.',
  lei=[(TR + '15', 'Incorre na mesma pena quem promove, intermedeia, facilita ou aufere qualquer vantagem com a transação.', None, 'Lei 9.434/1997, art. 15, par. ún.')],
  kw=['intermedeia'])
I(P, 1, 'Remoção em pessoa viva com morte',
  'Se a remoção ilegal de órgão é praticada em pessoa viva e resulta morte, a pena é de reclusão de 4 a 12 anos.', 'E',
  'Art. 14, § 4º: **reclusão, de 8 a 20 anos**; de 4 a 12 é a pena da lesão gravíssima (§ 3º).',
  lei=[(TR + '14', 'Pena - reclusão, de oito a vinte anos', None, 'Lei 9.434/1997, art. 14, § 4º')],
  peg='Usar a pena do § 3º.', kw=['resulta morte', 'oito a vinte anos'])
I(P, 1, 'Morte encefálica',
  'A retirada post mortem de órgãos destinados a transplante deve ser precedida de diagnóstico de morte encefálica, constatada e registrada.', 'C',
  'Art. 3º.',
  lei=[(TR + '3', 'deverá ser precedida de diagnóstico de morte encefálica', None, 'Lei 9.434/1997, art. 3º')],
  kw=['morte encefálica'])
I(P, 1, 'Cadáver não recomposto',
  'Deixar de recompor o cadáver, devolvendo-lhe aspecto condigno para sepultamento, é mera infração administrativa.', 'E',
  'Art. 19: é **crime** (detenção, de 6 meses a 2 anos), assim como retardar a entrega aos familiares.',
  lei=[(TR + '19', 'Deixar de recompor cadáver, devolvendo-lhe aspecto condigno, para sepultamento', None, 'Lei 9.434/1997, art. 19')],
  peg='Negar a tipicidade.', kw=['recompor cadáver'])
# --- LPE-27 · Rodada 2
I(P, 2, 'Motivo torpe',
  'Se a remoção ilegal de órgãos é cometida mediante paga ou promessa de recompensa ou por outro motivo torpe, a pena é de reclusão, de 3 a 8 anos.', 'C',
  'Art. 14, § 1º.',
  lei=[(TR + '14', 'Se o crime é cometido mediante paga ou promessa de recompensa ou por outro motivo torpe:', None, 'Lei 9.434/1997, art. 14, § 1º')],
  kw=['paga ou promessa', 'motivo torpe'])
I(P, 2, 'Médico da família',
  'É vedada a presença de médico de confiança da família do falecido no ato de comprovação da morte encefálica, para preservar a isenção da equipe.', 'E',
  'Art. 3º, § 3º: **será admitida** a presença do médico de confiança da família.',
  lei=[(TR + '3', 'Será admitida a presença de médico de confiança da família do falecido no ato da comprovação e atestação da morte encefálica.', None, 'Lei 9.434/1997, art. 3º, § 3º')],
  peg='Inverter a regra.', kw=['médico de confiança da família'])
I(P, 2, 'Anúncio irregular',
  'Publicar anúncio ou apelo público em desacordo com a Lei de Transplantes é crime punido apenas com multa.', 'C',
  'Art. 20 (remete ao art. 11).',
  lei=[(TR + '20', 'Publicar anúncio ou apelo público em desacordo com o disposto no art. 11:', None, 'Lei 9.434/1997, art. 20')],
  kw=['anúncio', 'multa'])

# ======================= LPE-28 · Programa de computador (Lei 9.609/1998) =======================
P = 'DBA26-LPE-28'
I(P, 1, 'Registro',
  'A proteção aos direitos sobre programa de computador independe de registro.', 'C',
  'Art. 2º, § 3º.',
  lei=[(SW + '2', 'A proteção aos direitos de que trata esta Lei independe de registro.', None, 'Lei 9.609/1998, art. 2º, § 3º')],
  kw=['independe de registro'])
I(P, 1, 'Reprodução para comércio',
  'Reproduzir programa de computador, no todo ou em parte, para fins de comércio, sem autorização do autor, é punido com reclusão, de 1 a 4 anos, e multa.', 'C',
  'Art. 12, § 1º — forma qualificada; o caput (violação simples) tem detenção de 6 meses a 2 anos ou multa.',
  lei=[(SW + '12', 'Se a violação consistir na reprodução, por qualquer meio, de programa de computador, no todo ou em parte, para fins de comércio', None, 'Lei 9.609/1998, art. 12, § 1º'), (SW + '12', 'Pena - Reclusão de um a quatro anos e multa.', None, 'Lei 9.609/1998, art. 12, § 1º, pena')],
  kw=['para fins de comércio', 'reclusão'])
I(P, 1, 'Prazo de proteção',
  'A tutela dos direitos sobre programa de computador dura 70 anos, contados da morte do autor.', 'E',
  'Art. 2º, § 2º: **50 anos**, contados de 1º de janeiro do ano seguinte ao da publicação (ou da criação).',
  lei=[(SW + '2', 'pelo prazo de cinqüenta anos, contados a partir de 1º de janeiro do ano subseqüente ao da sua publicação', None, 'Lei 9.609/1998, art. 2º, § 2º')],
  peg='Usar o prazo da Lei 9.610/1998.', kw=['cinqüenta anos'])
I(P, 1, 'Direitos morais',
  'Aplicam-se integralmente ao programa de computador os direitos morais do autor previstos na lei de direitos autorais.', 'E',
  'Art. 2º, § 1º: **não se aplicam** os direitos morais, **ressalvados** o direito de reivindicar a paternidade e o de se opor a alterações que deformem o programa.',
  lei=[(SW + '2', 'Não se aplicam ao programa de computador as disposições relativas aos direitos morais', None, 'Lei 9.609/1998, art. 2º, § 1º')],
  peg='Estender os direitos morais.', kw=['direitos morais', 'paternidade'])
I(P, 1, 'Vistoria prévia',
  'A ação penal e as diligências preliminares de busca e apreensão por violação de direito de autor de programa de computador serão precedidas de vistoria.', 'C',
  'Art. 13.',
  lei=[(SW + '13', 'serão precedidas de vistoria', None, 'Lei 9.609/1998, art. 13')],
  kw=['vistoria'])
# --- LPE-28 · Rodada 2
I(P, 2, 'Violação simples',
  'Violar direitos de autor de programa de computador, sem finalidade comercial, é crime punido com detenção de seis meses a dois anos ou multa.', 'C',
  'Art. 12, caput — infração de menor potencial ofensivo.',
  lei=[(SW + '12', 'Pena - Detenção de seis meses a dois anos ou multa.', None, 'Lei 9.609/1998, art. 12, pena')],
  kw=['violação', 'detenção de seis meses a dois anos'])
I(P, 2, 'Vítima ente público',
  'Nos crimes contra programa de computador, a ação penal é sempre privada, ainda que a vítima seja autarquia ou empresa pública.', 'E',
  'Art. 12, § 3º, I: é **pública** quando praticado em prejuízo de entidade de direito público, autarquia, empresa pública, sociedade de economia mista ou fundação pública.',
  lei=[(SW + '12', 'I - quando praticados em prejuízo de entidade de direito público, autarquia, empresa pública, sociedade de economia mista ou fundação instituída pelo poder público;', None, 'Lei 9.609/1998, art. 12, § 3º, I')],
  peg='Esquecer a exceção.', kw=['entidade de direito público', 'ação penal'])
I(P, 2, 'Liminar de abstenção',
  'A liminar que proíbe ao infrator a prática do ato incriminado contra programa de computador depende do prévio ajuizamento de ação cautelar preparatória.', 'E',
  'Art. 14, § 2º: o juiz pode concedê-la **independentemente de ação cautelar preparatória** (tutela cível autônoma, independente da ação penal).',
  lei=[(SW + '14', 'Independentemente de ação cautelar preparatória, o juiz poderá conceder medida liminar proibindo ao infrator a prática do ato incriminado', None, 'Lei 9.609/1998, art. 14, § 2º')],
  kw=['medida liminar', 'abstenção'])

# ======================= LPE-29 · Lavagem de dinheiro =======================
P = 'DBA26-LPE-29'
I(P, 1, 'Infração antecedente',
  'Desde a Lei 12.683/2012, qualquer infração penal, inclusive contravenção, pode ser antecedente da lavagem de dinheiro.', 'C',
  'Art. 1º: bens provenientes, direta ou indiretamente, de **infração penal** — o rol taxativo de crimes antecedentes foi revogado (legislação de 3ª geração).',
  lei=[(LV + '1', 'provenientes, direta ou indiretamente, de infração penal', None, 'Lei 9.613/1998, art. 1º')],
  kw=['infração penal', 'Lei 12.683/2012'])
I(P, 1, 'Rol de antecedentes',
  'A lavagem de dinheiro só se configura se o bem provier de um dos crimes antecedentes do rol taxativo do art. 1º da Lei 9.613/1998, como tráfico, terrorismo e crimes contra a administração.', 'E',
  'Os incisos I a VIII do art. 1º estão **revogados** (Lei 12.683/2012); basta **qualquer infração penal**.',
  lei=[(LV + '1', 'I - (revogado);', None, 'Lei 9.613/1998, art. 1º, I')],
  peg='Ressuscitar o rol.', kw=['rol taxativo', 'revogado'])
I(P, 1, 'Autonomia do processo',
  'O processo e o julgamento da lavagem independem do processo e julgamento da infração antecedente, ainda que praticada em outro país.', 'C',
  'Art. 2º, II — a lavagem é crime autônomo.',
  lei=[(LV + '2', 'independem do processo e julgamento das infrações penais antecedentes, ainda que praticados em outro país', None, 'Lei 9.613/1998, art. 2º, II')],
  kw=['independem', 'autonomia'])
I(P, 1, 'Punibilidade extinta',
  'Extinta a punibilidade da infração antecedente pela prescrição, deixa de ser punível a lavagem dos bens dela provenientes.', 'E',
  'Art. 2º, § 1º: a lavagem é punível ainda que desconhecido ou isento de pena o autor, **ou extinta a punibilidade** da infração antecedente.',
  lei=[(LV + '2', 'ou extinta a punibilidade da infração penal antecedente', None, 'Lei 9.613/1998, art. 2º, § 1º')],
  peg='Contaminar a lavagem com a prescrição do antecedente.', kw=['extinta a punibilidade'])
I(P, 1, 'Art. 366 do CPP',
  'No processo por lavagem de dinheiro, o réu citado por edital que não comparece nem constitui advogado tem o processo e a prescrição suspensos, como na regra do art. 366 do CPP.', 'E',
  'Art. 2º, § 2º: **não se aplica o art. 366** do CPP; o processo segue com defensor dativo.',
  lei=[(LV + '2', 'não se aplica o disposto no art. 366 do Decreto-Lei nº 3.689', None, 'Lei 9.613/1998, art. 2º, § 2º')],
  peg='Aplicar a suspensão do art. 366.', kw=['art. 366'])
I(P, 1, 'Majorante',
  'A pena da lavagem aumenta de 1/3 a 2/3 se o crime for cometido de forma reiterada, por intermédio de organização criminosa ou por meio da utilização de ativo virtual.', 'C',
  'Art. 1º, § 4º (ativo virtual incluído pela Lei 14.478/2022).',
  lei=[(LV + '1', 'se os crimes definidos nesta Lei forem cometidos de forma reiterada, por intermédio de organização criminosa ou por meio da utilização de ativo virtual', None, 'Lei 9.613/1998, art. 1º, § 4º')],
  kw=['ativo virtual', 'forma reiterada'])
I(P, 1, 'Colaboração na lavagem',
  'Na lavagem, a pena pode ser reduzida de um a dois terços e cumprida em regime aberto ou semiaberto, ou o juiz pode deixar de aplicá-la, se o autor colaborar espontaneamente com as autoridades.', 'C',
  'Art. 1º, § 5º — admite até o **perdão judicial**.',
  lei=[(LV + '1', 'A pena poderá ser reduzida de um a dois terços e ser cumprida em regime aberto ou semiaberto, facultando-se ao juiz deixar de aplicá-la', None, 'Lei 9.613/1998, art. 1º, § 5º')],
  kw=['colaboração', 'deixar de aplicá-la'])
I(P, 1, 'Competência',
  'O processo por lavagem de dinheiro é sempre da competência da Justiça Federal, por envolver o sistema financeiro.', 'E',
  'Art. 2º, III: é federal quando praticada contra o sistema financeiro ou a ordem econômico-financeira, em detrimento de bens ou interesses da União, ou quando a **antecedente for federal**; fora disso, é **estadual**.',
  lei=[(LV + '2', 'b) quando a infração penal antecedente for de competência da Justiça Federal.', None, 'Lei 9.613/1998, art. 2º, III, b')],
  peg='Federalizar toda lavagem.', kw=['Justiça Federal', 'antecedente'])
# --- LPE-29 · Rodada 2
I(P, 2, 'Tentativa',
  'A tentativa de lavagem de dinheiro é punida nos termos do parágrafo único do art. 14 do Código Penal.', 'C',
  'Art. 1º, § 3º.',
  lei=[(LV + '1', 'A tentativa é punida nos termos do parágrafo único do art. 14 do Código Penal.', None, 'Lei 9.613/1998, art. 1º, § 3º')],
  kw=['tentativa'])
I(P, 2, 'Dados cadastrais',
  'Na apuração da lavagem, a autoridade policial e o MP têm acesso, independentemente de autorização judicial, exclusivamente aos dados cadastrais de qualificação pessoal, filiação e endereço do investigado.', 'C',
  'Art. 17-B (Lei 12.683/2012), na mesma linha do art. 15 da Lei 12.850/2013.',
  lei=[(LV + '17-B', 'A autoridade policial e o Ministério Público terão acesso, exclusivamente, aos dados cadastrais do investigado', None, 'Lei 9.613/1998, art. 17-B')],
  kw=['dados cadastrais'])
I(P, 2, 'Comunicação ao Coaf',
  'As pessoas obrigadas pela Lei de Lavagem devem comunicar ao Coaf, em 24 horas, as operações suspeitas, dando ciência ao cliente da comunicação feita.', 'E',
  'Art. 11, II: comunicam ao Coaf **abstendo-se de dar ciência** a qualquer pessoa, inclusive àquela a que se refira a informação.',
  lei=[(LV + '11', 'abstendo-se de dar ciência de tal ato a qualquer pessoa, inclusive àquela à qual se refira a informação', None, 'Lei 9.613/1998, art. 11, II')],
  peg='Avisar o cliente.', kw=['Coaf', 'abstendo-se de dar ciência'])
I(P, 2, 'Ativos virtuais',
  'As prestadoras de serviços de ativos virtuais estão sujeitas às obrigações de identificação de clientes e de comunicação de operações da Lei de Lavagem.', 'C',
  'Art. 9º, par. ún., XIX (Lei 14.478/2022).',
  lei=[(LV + '9', 'XIX - as prestadoras de serviços de ativos virtuais.', None, 'Lei 9.613/1998, art. 9º, par. ún., XIX')],
  kw=['prestadoras de serviços de ativos virtuais'])
I(P, 2, 'Técnicas especiais',
  'Na apuração da lavagem de dinheiro, são vedadas a ação controlada e a infiltração de agentes, restritas às organizações criminosas.', 'E',
  'Art. 1º, § 6º (Lei 13.964/2019): **admite-se** a ação controlada e a infiltração de agentes.',
  lei=[(LV + '1', 'Para a apuração do crime de que trata este artigo, admite-se a utilização da ação controlada e da infiltração de agentes.', None, 'Lei 9.613/1998, art. 1º, § 6º')],
  peg='Vedar as técnicas.', kw=['ação controlada', 'infiltração de agentes'])

# ======================= LPE-30 · Proteção a vítimas e testemunhas (Lei 9.807/1999) =======================
P = 'DBA26-LPE-30'
I(P, 1, 'Duração da proteção',
  'A proteção oferecida pelo programa terá duração máxima de dois anos, podendo ser prorrogada em circunstâncias excepcionais, se persistirem os motivos da admissão.', 'C',
  'Art. 11 e parágrafo único.',
  lei=[(PT + '11', 'A proteção oferecida pelo programa terá a duração máxima de dois anos.', None, 'Lei 9.807/1999, art. 11')],
  kw=['duração máxima de dois anos'])
I(P, 1, 'Excluídos do programa',
  'Estão excluídos da proteção os condenados que estejam cumprindo pena e os indiciados ou acusados sob prisão cautelar.', 'C',
  'Art. 2º, § 2º (e também quem tem conduta incompatível com as restrições do programa) — o preso colaborador recebe as medidas do art. 15.',
  lei=[(PT + '2', 'os condenados que estejam cumprindo pena e os indiciados ou acusados sob prisão cautelar', None, 'Lei 9.807/1999, art. 2º, § 2º')],
  kw=['excluídos da proteção', 'prisão cautelar'])
I(P, 1, 'Anuência',
  'O ingresso no programa de proteção pode ser determinado compulsoriamente pelo juiz quando a testemunha for essencial ao processo.', 'E',
  'Art. 2º, § 3º: o ingresso e as restrições terão **sempre a anuência** da pessoa protegida ou de seu representante legal.',
  lei=[(PT + '2', 'terão sempre a anuência da pessoa protegida, ou de seu representante legal', None, 'Lei 9.807/1999, art. 2º, § 3º')],
  peg='Tornar compulsório o ingresso.', kw=['anuência'])
I(P, 1, 'Perdão judicial',
  'O juiz pode conceder perdão judicial ao acusado primário que tenha colaborado efetiva e voluntariamente, desde que dela resulte, por exemplo, a localização da vítima com a integridade física preservada.', 'C',
  'Art. 13, II; levam-se em conta a personalidade do beneficiado e a gravidade do fato (par. ún.).',
  lei=[(PT + '13', 'conceder o perdão judicial e a conseqüente extinção da punibilidade ao acusado que, sendo primário', None, 'Lei 9.807/1999, art. 13'), (PT + '13', 'II - a localização da vítima com a sua integridade física preservada;', None, 'Lei 9.807/1999, art. 13, II')],
  kw=['perdão judicial', 'primário'])
I(P, 1, 'Quem pede o ingresso',
  'A solicitação de ingresso no programa de proteção só pode ser encaminhada ao órgão executor pelo Ministério Público ou pelo juiz.', 'E',
  'Art. 5º: também **pelo interessado**, pela **autoridade policial** que conduz a investigação e por órgãos de defesa dos direitos humanos.',
  lei=[(PT + '5', 'III - pela autoridade policial que conduz a investigação criminal;', None, 'Lei 9.807/1999, art. 5º, III')],
  peg='Excluir o delegado.', kw=['autoridade policial', 'órgão executor'])
I(P, 1, 'Alteração de nome',
  'Em casos excepcionais, o próprio conselho deliberativo pode alterar, por ato administrativo, o nome completo da pessoa protegida.', 'E',
  'Art. 9º: o conselho **encaminha requerimento ao juiz** de registros públicos, que ouve o MP; o procedimento corre em segredo de justiça.',
  lei=[(PT + '9', 'poderá o conselho deliberativo encaminhar requerimento da pessoa protegida ao juiz competente para registros públicos', None, 'Lei 9.807/1999, art. 9º')],
  peg='Dispensar o juiz.', kw=['alteração de nome', 'juiz competente para registros públicos'])
# --- LPE-30 · Rodada 2
I(P, 2, 'Colaborador preso',
  'Estando sob prisão temporária, preventiva ou em flagrante, o colaborador será custodiado em dependência separada dos demais presos.', 'C',
  'Art. 15, § 1º.',
  lei=[(PT + '15', 'o colaborador será custodiado em dependência separada dos demais presos', None, 'Lei 9.807/1999, art. 15, § 1º')],
  kw=['dependência separada'])
I(P, 2, 'Depoimento antecipado',
  'Qualquer que seja o rito, o juiz, após a citação, tomará antecipadamente o depoimento das pessoas incluídas nos programas de proteção.', 'C',
  'Art. 19-A, par. ún. (Lei 12.483/2011); o feito tem prioridade de tramitação (caput).',
  lei=[(PT + '19-A', 'o juiz, após a citação, tomará antecipadamente o depoimento das pessoas incluídas nos programas de proteção', None, 'Lei 9.807/1999, art. 19-A, par. ún.')],
  kw=['antecipadamente', 'prioridade'])
I(P, 2, 'Redução de pena',
  'O indiciado ou acusado que colabora voluntariamente na identificação dos coautores, na localização da vítima com vida e na recuperação do produto do crime terá, em caso de condenação, a pena reduzida de metade.', 'E',
  'Art. 14: redução de **um a dois terços** (benefício que independe da primariedade, ao contrário do perdão do art. 13).',
  lei=[(PT + '14', 'no caso de condenação, terá pena reduzida de um a dois terços', None, 'Lei 9.807/1999, art. 14')],
  peg='Trocar a fração.', kw=['um a dois terços'])
I(P, 2, 'Conselho deliberativo',
  'Cada programa de proteção é dirigido exclusivamente pela polícia judiciária, que executa as medidas.', 'E',
  'Art. 4º: é dirigido por **conselho deliberativo** com representantes do **MP, do Judiciário** e de órgãos de segurança pública e direitos humanos; a polícia **colabora** (§ 2º).',
  lei=[(PT + '4', 'Cada programa será dirigido por um conselho deliberativo em cuja composição haverá representantes do Ministério Público, do Poder Judiciário', None, 'Lei 9.807/1999, art. 4º')],
  peg='Entregar o programa à polícia.', kw=['conselho deliberativo'])
