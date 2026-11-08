# Pente Fino de Legislação Penal Extravagante — LPE-15 (Lei 8.137/1990), LPE-16 (Maria da Penha), LPE-17 (Drogas),
# LPE-18 (crimes do CDC), LPE-19 (contravenções penais) e LPE-20 (crimes ambientais) (08/11/2026).
from base import I
from lpe_juris import J

OT = 'L8137:'
MP = 'L11340:'
DR = 'L11343:'
CD = 'L8078:'
CV = 'DL3688:'
AM = 'L9605:'

# ======================= LPE-15 · Lei 8.137/1990 =======================
P = 'DBA26-LPE-15'
I(P, 1, 'Lançamento definitivo',
  'Não se tipifica crime material contra a ordem tributária do art. 1º, I a IV, da Lei 8.137/1990 antes do lançamento definitivo do tributo.', 'C',
  '**Súmula Vinculante 24**: o lançamento definitivo é condição para a tipicidade (e para o início da prescrição) dos crimes **materiais**.',
  lei=[(OT + '1', 'Constitui crime contra a ordem tributária suprimir ou reduzir tributo', None, 'Lei 8.137/1990, art. 1º, caput')],
  juris=[J['SV24']], kw=['Súmula Vinculante 24', 'lançamento definitivo'])
I(P, 1, 'Ação penal',
  'Os crimes contra a ordem tributária dependem de representação fiscal da Fazenda Pública para que o Ministério Público ofereça denúncia.', 'E',
  'Art. 15: são de **ação penal pública** (incondicionada, art. 100 do CP); qualquer pessoa pode provocar o MP (art. 16).',
  lei=[(OT + '15', 'Os crimes previstos nesta lei são de ação penal pública', None, 'Lei 8.137/1990, art. 15')],
  peg='Criar condição de procedibilidade.', kw=['ação penal pública'])
I(P, 1, 'Apropriação indébita tributária',
  'O crime de apropriação indébita tributária pode ocorrer tanto em operações próprias como em razão de substituição tributária.', 'C',
  '**Súmula 658/STJ** (art. 2º, II).',
  lei=[(OT + '2', 'II - deixar de recolher, no prazo legal, valor de tributo ou de contribuição social, descontado ou cobrado', None, 'Lei 8.137/1990, art. 2º, II')],
  juris=[J['S658']], kw=['Súmula 658/STJ', 'apropriação indébita tributária'])
I(P, 1, 'Pena do art. 2º',
  'Os crimes do art. 2º da Lei 8.137/1990 têm a mesma pena dos crimes materiais do art. 1º: reclusão, de 2 a 5 anos.', 'E',
  'Art. 2º: **detenção, de 6 meses a 2 anos**, e multa — são infrações de **menor potencial ofensivo**.',
  lei=[(OT + '2', 'Pena - detenção, de 6 (seis) meses a 2 (dois) anos, e multa.', None, 'Lei 8.137/1990, art. 2º, pena')],
  peg='Igualar as penas.', kw=['detenção', 'menor potencial ofensivo'])
I(P, 1, 'Mercadoria imprópria',
  'Vender ou ter em depósito mercadoria em condições impróprias ao consumo é crime contra as relações de consumo que não admite a modalidade culposa.', 'E',
  'Art. 7º, IX, e par. ún.: nos incisos II, III e IX **pune-se a modalidade culposa**, com redução da pena.',
  lei=[(OT + '7', 'Nas hipóteses dos incisos II, III e IX pune-se a modalidade culposa', None, 'Lei 8.137/1990, art. 7º, par. ún.')],
  peg='Negar a forma culposa.', kw=['modalidade culposa', 'impróprias ao consumo'])
I(P, 1, 'Servidor público',
  'É circunstância que pode agravar de 1/3 até a metade as penas dos crimes da Lei 8.137/1990 ser o crime cometido por servidor público no exercício de suas funções.', 'C',
  'Art. 12, II; também o grave dano à coletividade (I) e os bens essenciais à vida ou à saúde (III).',
  lei=[(OT + '12', 'II - ser o crime cometido por servidor público no exercício de suas funções;', None, 'Lei 8.137/1990, art. 12, II')],
  kw=['servidor público', '1/3 (um terço) até a metade'])
# --- LPE-15 · Rodada 2
I(P, 2, 'Delação',
  'Nos crimes da Lei 8.137/1990 cometidos em quadrilha ou coautoria, o coautor que, por confissão espontânea, revelar toda a trama delituosa terá a pena reduzida de um a dois terços.', 'C',
  'Art. 16, par. ún. (mesma fórmula da Lei 7.492/1986).',
  lei=[(OT + '16', 'revelar à autoridade policial ou judicial toda a trama delituosa', None, 'Lei 8.137/1990, art. 16, par. ún.')],
  kw=['trama delituosa', 'confissão espontânea'])
I(P, 2, 'Insignificância tributária federal',
  'Incide a insignificância nos crimes tributários federais e no descaminho quando o débito não ultrapassar R$ 20.000,00.', 'C',
  '**Tema 157/STJ** (revisado em 28/02/2018), com base no art. 20 da Lei 10.522/2002 e nas Portarias 75 e 130 do MF.',
  juris=[J['T157']], kw=['Tema 157/STJ', 'R$ 20.000,00'])
I(P, 2, 'Cartel',
  'Formar acordo entre ofertantes visando à fixação artificial de preços é crime contra a ordem econômica punido com detenção, de 6 meses a 2 anos.', 'E',
  'Art. 4º, II, a (Lei 12.529/2011): **reclusão, de 2 a 5 anos**, e multa.',
  lei=[(OT + '4', 'a) à fixação artificial de preços ou quantidades vendidas ou produzidas;', None, 'Lei 8.137/1990, art. 4º, II, a'), (OT + '4', 'Pena - reclusão, de 2 (dois) a 5 (cinco) anos e multa.', None, 'Lei 8.137/1990, art. 4º, pena')],
  peg='Rebaixar a pena do cartel.', kw=['cartel', 'fixação artificial de preços'])
I(P, 2, 'Bens imunes',
  'A Lei Complementar 224/2025 criou causa de diminuição de pena para os crimes tributários relacionados a bens alcançados por imunidade tributária.', 'E',
  'Art. 12, IV (LC 224/2025): é circunstância que pode **agravar** a pena de 1/3 até a metade.',
  lei=[(OT + '12', 'IV - ser o crime relacionado a bens alcançados pelas imunidades tributárias', None, 'Lei 8.137/1990, art. 12, IV')],
  peg='Trocar agravamento por diminuição.', kw=['imunidades tributárias', 'agravar'])

# ======================= LPE-16 · Maria da Penha =======================
P = 'DBA26-LPE-16'
I(P, 1, 'Coabitação',
  'A violência doméstica e familiar da Lei Maria da Penha pressupõe coabitação entre agressor e vítima.', 'E',
  '**Súmula 600/STJ** e art. 5º, III: basta relação íntima de afeto em que o agressor conviva ou **tenha convivido**, **independentemente de coabitação**.',
  lei=[(MP + '5', 'na qual o agressor conviva ou tenha convivido com a ofendida, independentemente de coabitação', None, 'Lei 11.340/2006, art. 5º, III')],
  juris=[J['S600']], peg='Exigir coabitação.', kw=['Súmula 600/STJ', 'independentemente de coabitação'])
I(P, 1, 'Orientação sexual',
  'As relações pessoais protegidas pela Lei Maria da Penha independem de orientação sexual.', 'C',
  'Art. 5º, par. ún.: alcança, por exemplo, a violência entre duas mulheres em relação afetiva.',
  lei=[(MP + '5', 'As relações pessoais enunciadas neste artigo independem de orientação sexual.', None, 'Lei 11.340/2006, art. 5º, par. ún.')],
  kw=['orientação sexual'])
I(P, 1, 'Violência vicária (2026)',
  'A violência vicária, praticada contra descendente, ascendente, dependente ou pessoa da rede de apoio da mulher com vistas a atingi-la, é forma de violência doméstica e familiar.', 'C',
  'Art. 7º, VI (**Lei 15.384/2026**, a mesma que criou o vicaricídio, art. 121-B do CP).',
  lei=[(MP + '7', 'a violência vicária, entendida como qualquer forma de violência praticada contra descendente, ascendente, dependente', None, 'Lei 11.340/2006, art. 7º, VI')],
  kw=['violência vicária', 'Lei 15.384/2026'])
I(P, 1, 'Afastamento pelo delegado',
  'O delegado de polícia pode afastar imediatamente o agressor do lar em qualquer município, independentemente de ser sede de comarca.', 'E',
  'Art. 12-C, II: o **delegado** só age quando o **Município não for sede de comarca**; o **policial**, se além disso não houver delegado disponível (III). O juiz é comunicado em 24 horas (§ 1º).',
  lei=[(MP + '12-C', 'II - pelo delegado de polícia, quando o Município não for sede de comarca; ou', None, 'Lei 11.340/2006, art. 12-C, II')],
  peg='Generalizar a atribuição do delegado.', kw=['sede de comarca', 'afastado'])
I(P, 1, 'Renúncia à representação',
  'Nos crimes de ação pública condicionada da Lei Maria da Penha, só se admite a renúncia à representação perante o juiz, em audiência especialmente designada, antes do recebimento da denúncia.', 'C',
  'Art. 16 (a "renúncia" é, tecnicamente, retratação — como esclarece o par. ún., redação da Lei 15.380/2026).',
  lei=[(MP + '16', 'só será admitida a renúncia à representação perante o juiz, em audiência especialmente designada com tal finalidade', None, 'Lei 11.340/2006, art. 16')],
  kw=['audiência especialmente designada', 'renúncia'])
I(P, 1, 'Decadência (2026)',
  'Nos crimes de violência doméstica contra a mulher, a ofendida decai do direito de queixa ou de representação em 6 meses, contados do dia em que soube quem é o autor.', 'E',
  'Art. 16-A (2026): o prazo é de **12 meses** (no CP, art. 103, par. ún., a mesma regra).',
  lei=[(MP + '16-A', 'a ofendida decai do direito de queixa ou de representação se não o exerce no prazo de 12 (doze) meses', None, 'Lei 11.340/2006, art. 16-A')],
  peg='Aplicar o prazo geral de 6 meses.', kw=['12 (doze) meses', 'decadência'])
I(P, 1, 'Cesta básica',
  'É vedada, nos casos de violência doméstica e familiar contra a mulher, a aplicação de pena de cesta básica ou outra prestação pecuniária, bem como a substituição que implique pagamento isolado de multa.', 'C',
  'Art. 17.',
  lei=[(MP + '17', 'de penas de cesta básica ou outras de prestação pecuniária', None, 'Lei 11.340/2006, art. 17')],
  kw=['cesta básica', 'pagamento isolado de multa'])
I(P, 1, 'Descumprimento de medida protetiva',
  'Descumprir decisão judicial que defere medida protetiva de urgência é crime punido com detenção, de 3 meses a 2 anos.', 'E',
  'Art. 24-A (redação da Lei 14.994/2024): **reclusão, de 2 a 5 anos**, e multa; com violação de área de exclusão monitorada, +1/3 até a metade (§ 4º, Lei 15.383/2026).',
  lei=[(MP + '24-A', 'Pena – reclusão, de 2 (dois) a 5 (cinco) anos, e multa.', None, 'Lei 11.340/2006, art. 24-A, pena')],
  peg='Citar a pena revogada.', kw=['reclusão, de 2 (dois) a 5 (cinco) anos', 'medidas protetivas'])
I(P, 1, 'Lei 9.099 afastada',
  'Aos crimes praticados com violência doméstica e familiar contra a mulher, independentemente da pena prevista, não se aplica a Lei 9.099/1995.', 'C',
  'Art. 41 e **Súmula 536/STJ** (nem transação nem suspensão condicional do processo).',
  lei=[(MP + '41', 'independentemente da pena prevista, não se aplica a Lei nº 9.099', None, 'Lei 11.340/2006, art. 41')],
  kw=['art. 41', 'Lei nº 9.099'])
# --- LPE-16 · Rodada 2
I(P, 2, 'Fiança no art. 24-A',
  'Preso em flagrante pelo descumprimento de medida protetiva, o autor pode ter a fiança arbitrada pelo delegado de polícia, conforme a pena.', 'E',
  'Art. 24-A, § 2º: **apenas a autoridade judicial** pode conceder fiança.',
  lei=[(MP + '24-A', 'Na hipótese de prisão em flagrante, apenas a autoridade judicial poderá conceder fiança.', None, 'Lei 11.340/2006, art. 24-A, § 2º')],
  peg='Aplicar o art. 322 do CPP.', kw=['apenas a autoridade judicial', 'fiança'])
I(P, 2, 'Monitoração eletrônica (2026)',
  'Verificado risco atual ou iminente à mulher, o agressor será submetido à monitoração eletrônica, que pode ser determinada pelo delegado de polícia quando o Município não for sede de comarca, com comunicação ao juiz em até 24 horas.', 'C',
  'Art. 12-D (**Lei 15.383/2026**); o juiz decide em igual prazo sobre a manutenção.',
  lei=[(MP + '12-D', 'II – pelo delegado de polícia, quando o Município não for sede de comarca.', None, 'Lei 11.340/2006, art. 12-D, II')],
  kw=['monitoração eletrônica', 'Lei 15.383/2026'])
I(P, 2, 'Juiz que deferiu a medida',
  'A configuração do crime de descumprimento de medida protetiva independe da competência civil ou criminal do juiz que a deferiu.', 'C',
  'Art. 24-A, § 1º.',
  lei=[(MP + '24-A', 'A configuração do crime independe da competência civil ou criminal do juiz que deferiu as medidas.', None, 'Lei 11.340/2006, art. 24-A, § 1º')],
  kw=['competência civil ou criminal'])
I(P, 2, 'Insignificância',
  'O princípio da insignificância pode ser aplicado às vias de fato praticadas contra a mulher no âmbito doméstico, se a lesão for ínfima.', 'E',
  '**Súmula 589/STJ**: é **inaplicável** a insignificância nos crimes **ou contravenções** contra a mulher no âmbito doméstico.',
  juris=[J['S589']], peg='Aplicar a bagatela.', kw=['Súmula 589/STJ'])
I(P, 2, 'Não revitimização',
  'A inquirição da mulher em situação de violência doméstica deve evitar sucessivas inquirições sobre o mesmo fato nos âmbitos criminal, cível e administrativo, bem como questionamentos sobre a vida privada.', 'C',
  'Art. 10-A, § 1º, III (Lei 13.505/2017).',
  lei=[(MP + '10-A', 'não revitimização da depoente, evitando sucessivas inquirições sobre o mesmo fato', None, 'Lei 11.340/2006, art. 10-A, § 1º, III')],
  kw=['não revitimização'])
I(P, 2, 'Audiência do art. 16 (2026)',
  'O juiz deve designar sempre, de ofício, a audiência do art. 16 da Lei Maria da Penha, para que a vítima confirme a representação.', 'E',
  'Art. 16, par. ún. (**Lei 15.380/2026**): a audiência confirma a **retratação**, não a representação, e **só** é designada mediante **manifestação expressa** da vítima de se retratar.',
  lei=[(MP + '16', 'tem por objetivo confirmar a retratação da vítima, não a representação', None, 'Lei 11.340/2006, art. 16, par. ún.')],
  peg='Tornar a audiência obrigatória.', kw=['retratação', 'Lei 15.380/2026'])

# ======================= LPE-17 · Lei de Drogas =======================
P = 'DBA26-LPE-17'
I(P, 1, 'Porte para consumo',
  'O porte de droga para consumo pessoal não é punido com pena privativa de liberdade, mas com advertência, prestação de serviços à comunidade ou medida educativa.', 'C',
  'Art. 28, I a III: **despenalização**; as penas dos incisos II e III duram até 5 meses (10 na reincidência).',
  lei=[(DR + '28', 'I - advertência sobre os efeitos das drogas;', None, 'Lei 11.343/2006, art. 28, I')],
  kw=['consumo pessoal', 'advertência'])
I(P, 1, 'Maconha para consumo',
  'Para o STF, o porte de até 40 gramas de maconha para consumo pessoal continua sendo crime, sujeito às penas do art. 28.', 'E',
  '**Tema 506/RG** (26/06/2024): **não é infração penal** — é ilícito extrapenal; presume-se usuário quem porta até **40 g ou seis plantas-fêmeas** (presunção relativa).',
  juris=[J['RG506']], peg='Ignorar o Tema 506.', kw=['Tema 506', '40 gramas'])
I(P, 1, 'Tráfico privilegiado',
  'No tráfico, as penas podem ser reduzidas de um sexto a dois terços se o agente for primário, de bons antecedentes, não se dedicar às atividades criminosas nem integrar organização criminosa.', 'C',
  'Art. 33, § 4º: requisitos **cumulativos**. A vedação de conversão em restritiva foi suspensa pela Resolução 5/2012 do Senado.',
  lei=[(DR + '33', 'as penas poderão ser reduzidas de um sexto a dois terços, desde que o agente seja primário, de bons antecedentes', None, 'Lei 11.343/2006, art. 33, § 4º')],
  kw=['tráfico privilegiado', 'um sexto a dois terços'])
I(P, 1, 'Oferta para consumo conjunto',
  'Oferecer droga, eventualmente e sem objetivo de lucro, a pessoa de seu relacionamento, para juntos a consumirem, é crime de menor potencial ofensivo, distinto do tráfico.', 'C',
  'Art. 33, § 3º: detenção, de 6 meses a 1 ano, e multa, sem prejuízo das penas do art. 28.',
  lei=[(DR + '33', 'Oferecer droga, eventualmente e sem objetivo de lucro, a pessoa de seu relacionamento, para juntos a consumirem:', None, 'Lei 11.343/2006, art. 33, § 3º')],
  kw=['sem objetivo de lucro', 'consumo conjunto'])
I(P, 1, 'Associação para o tráfico',
  'A associação para o tráfico exige três ou mais pessoas, como a associação criminosa do Código Penal.', 'E',
  'Art. 35: bastam **duas ou mais pessoas**, para praticar, **reiteradamente ou não**, os crimes dos arts. 33, caput e § 1º, e 34 (diferentemente do art. 288 do CP, que exige três ou mais).',
  lei=[(DR + '35', 'Associarem-se duas ou mais pessoas para o fim de praticar, reiteradamente ou não', None, 'Lei 11.343/2006, art. 35')],
  peg='Transpor o número do art. 288 do CP.', kw=['duas ou mais pessoas', 'associação para o tráfico'])
I(P, 1, 'Tráfico interestadual',
  'Para a majorante do tráfico interestadual, é desnecessária a efetiva transposição da fronteira entre estados, bastando a demonstração inequívoca da intenção.', 'C',
  'Art. 40, V, e **Súmula 587/STJ**.',
  lei=[(DR + '40', 'V - caracterizado o tráfico entre Estados da Federação ou entre estes e o Distrito Federal;', None, 'Lei 11.343/2006, art. 40, V')],
  juris=[J['S587']], kw=['Súmula 587/STJ', 'interestadual'])
I(P, 1, 'Prazos do inquérito',
  'Na Lei de Drogas, o inquérito deve ser concluído em 10 dias com o indiciado preso e em 30 dias se solto.', 'E',
  'Art. 51: **30 dias** (preso) e **90 dias** (solto), prazos que o juiz pode **duplicar**, ouvido o MP, a pedido justificado do delegado.',
  lei=[(DR + '51', 'O inquérito policial será concluído no prazo de 30 (trinta) dias, se o indiciado estiver preso, e de 90 (noventa) dias, quando solto.', None, 'Lei 11.343/2006, art. 51')],
  peg='Usar os prazos do CPP.', kw=['30 (trinta) dias', '90 (noventa) dias'])
I(P, 1, 'Laudo de constatação',
  'Para a lavratura do auto de prisão em flagrante e o estabelecimento da materialidade, basta o laudo de constatação da natureza e da quantidade da droga.', 'C',
  'Art. 50, § 1º; o perito que o subscreve pode participar do laudo definitivo (§ 2º).',
  lei=[(DR + '50', 'é suficiente o laudo de constatação da natureza e quantidade da droga', None, 'Lei 11.343/2006, art. 50, § 1º')],
  kw=['laudo de constatação', 'materialidade'])
I(P, 1, 'Flagrante do usuário',
  'Surpreendido o usuário com droga para consumo, a autoridade policial lavra o auto de prisão em flagrante e arbitra fiança.', 'E',
  'Art. 48, § 2º: **não se imporá prisão em flagrante**; lavra-se **termo circunstanciado** e o autor é encaminhado ao juízo ou assume o compromisso de comparecer.',
  lei=[(DR + '48', 'Tratando-se da conduta prevista no art. 28 desta Lei, não se imporá prisão em flagrante', None, 'Lei 11.343/2006, art. 48, § 2º')],
  peg='Prender o usuário.', kw=['não se imporá prisão em flagrante', 'termo circunstanciado'])
I(P, 1, 'Organização ultraviolenta (2026)',
  'As penas dos arts. 33 a 37 da Lei de Drogas são aplicadas em dobro se o crime for praticado por integrante de organização criminosa ultraviolenta, grupo paramilitar ou milícia privada, no contexto de sua atuação.', 'C',
  'Art. 40-A (**Lei 15.358/2026**); com emprego de arma de fogo, aplica-se o concurso material (par. ún.).',
  lei=[(DR + '40-A', 'serão aplicadas em dobro se o crime tiver sido praticado por integrante de organização criminosa ultraviolenta, grupo paramilitar ou milícia privada', None, 'Lei 11.343/2006, art. 40-A')],
  kw=['Lei 15.358/2026', 'em dobro'])
I(P, 1, 'Ação controlada na Lei de Drogas',
  'Na Lei de Drogas, a não atuação policial sobre os portadores de drogas depende apenas de comunicação prévia ao juiz, como na Lei de Organizações Criminosas.', 'E',
  'Art. 53, II: exige **autorização judicial**, ouvido o MP, e o conhecimento do itinerário provável e da identificação dos agentes (par. ún.).',
  lei=[(DR + '53', 'mediante autorização judicial e ouvido o Ministério Público', None, 'Lei 11.343/2006, art. 53, caput')],
  peg='Transpor o regime da Lei 12.850/2013.', kw=['autorização judicial', 'ação controlada'])
# --- LPE-17 · Rodada 2
I(P, 2, 'Financiamento do tráfico',
  'Financiar ou custear o tráfico de drogas é crime autônomo, punido com reclusão de 8 a 20 anos.', 'C',
  'Art. 36; quem financia **e** trafica responde pelo art. 33 com a majorante do art. 40, VII.',
  lei=[(DR + '36', 'Pena - reclusão, de 8 (oito) a 20 (vinte) anos', None, 'Lei 11.343/2006, art. 36, pena')],
  kw=['financiar ou custear', '8 (oito) a 20 (vinte) anos'])
I(P, 2, 'Informante',
  'Quem colabora como informante com grupo destinado ao tráfico responde como partícipe do crime do art. 33.', 'E',
  'Art. 37: o **informante** responde por crime **autônomo** (reclusão, de 2 a 6 anos) — exceção pluralista à teoria monista.',
  lei=[(DR + '37', 'Colaborar, como informante, com grupo, organização ou associação destinados à prática de qualquer dos crimes', None, 'Lei 11.343/2006, art. 37')],
  peg='Aplicar a regra geral do concurso.', kw=['informante', 'crime autônomo'])
I(P, 2, 'Transnacionalidade',
  'A majorante do tráfico transnacional configura-se com a prova da destinação internacional da droga, ainda que não consumada a transposição da fronteira.', 'C',
  '**Súmula 607/STJ** (art. 40, I).',
  juris=[J['S607']], kw=['Súmula 607/STJ', 'transnacional'])
I(P, 2, 'Agente disfarçado',
  'Incorre nas penas do tráfico quem vende droga a agente policial disfarçado, quando presentes elementos probatórios razoáveis de conduta criminal preexistente.', 'C',
  'Art. 33, § 1º, IV (Lei 13.964/2019).',
  lei=[(DR + '33', 'a agente policial disfarçado, quando presentes elementos probatórios razoáveis de conduta criminal preexistente', None, 'Lei 11.343/2006, art. 33, § 1º, IV')],
  kw=['agente policial disfarçado'])
I(P, 2, 'Livramento condicional',
  'Nos crimes de tráfico, o livramento condicional é concedido após o cumprimento de metade da pena, vedado ao reincidente específico.', 'E',
  'Art. 44, par. ún.: após **dois terços** da pena, vedado ao reincidente específico.',
  lei=[(DR + '44', 'dar-se-á o livramento condicional após o cumprimento de dois terços da pena, vedada sua concessão ao reincidente específico', None, 'Lei 11.343/2006, art. 44, par. ún.')],
  peg='Trocar 2/3 por metade.', kw=['dois terços', 'livramento condicional'])
I(P, 2, 'Preponderância na dosimetria',
  'Na fixação da pena dos crimes da Lei de Drogas, o juiz considerará, com preponderância sobre o art. 59 do CP, a natureza e a quantidade da substância, a personalidade e a conduta social do agente.', 'C',
  'Art. 42.',
  lei=[(DR + '42', 'com preponderância sobre o previsto no art. 59 do Código Penal, a natureza e a quantidade da substância ou do produto', None, 'Lei 11.343/2006, art. 42')],
  kw=['preponderância', 'natureza e a quantidade'])
I(P, 2, 'Condução após consumo',
  'O art. 39 da Lei de Drogas pune quem conduz veículo automotor em via pública após o consumo de drogas.', 'E',
  'Art. 39: o tipo é **embarcação ou aeronave**; veículo automotor sob efeito de substância psicoativa é o art. 306 do CTB.',
  lei=[(DR + '39', 'Conduzir embarcação ou aeronave após o consumo de drogas, expondo a dano potencial a incolumidade de outrem', None, 'Lei 11.343/2006, art. 39')],
  peg='Confundir com o CTB.', kw=['embarcação ou aeronave'])

# ======================= LPE-18 · Crimes do CDC =======================
P = 'DBA26-LPE-18'
I(P, 1, 'Nocividade do produto',
  'Omitir dizeres ou sinais ostensivos sobre a nocividade ou periculosidade de produtos nas embalagens é crime do CDC, punido também na forma culposa.', 'C',
  'Art. 63 e § 2º (culposo: detenção de 1 a 6 meses ou multa).',
  lei=[(CD + '63', 'Omitir dizeres ou sinais ostensivos sobre a nocividade ou periculosidade de produtos', None, 'CDC, art. 63'), (CD + '63', '§ 2° Se o crime é culposo:', None, 'CDC, art. 63, § 2º')],
  kw=['nocividade', 'culposo'])
I(P, 1, 'Patrocínio da oferta',
  'Incorre nas penas da afirmação falsa ou enganosa sobre produtos ou serviços quem patrocinar a oferta.', 'C',
  'Art. 66, § 1º.',
  lei=[(CD + '66', '§ 1º Incorrerá nas mesmas penas quem patrocinar a oferta.', None, 'CDC, art. 66, § 1º')],
  kw=['patrocinar a oferta'])
I(P, 1, 'Cobrança vexatória',
  'Utilizar ameaça ou constrangimento na cobrança de dívidas, expondo o consumidor ao ridículo, é apenas infração administrativa, sem repercussão penal.', 'E',
  'Art. 71: é **crime** (detenção de 3 meses a 1 ano e multa).',
  lei=[(CD + '71', 'Utilizar, na cobrança de dívidas, de ameaça, coação, constrangimento físico ou moral', None, 'CDC, art. 71')],
  peg='Negar a tipicidade.', kw=['cobrança de dívidas', 'constrangimento'])
I(P, 1, 'Agravante etária',
  'É agravante dos crimes do CDC o cometimento em detrimento de maior de setenta anos.', 'E',
  'Art. 76, IV, b: **maior de sessenta anos**, menor de 18, operário, rurícola ou pessoa com deficiência mental.',
  lei=[(CD + '76', 'de menor de dezoito ou maior de sessenta anos', None, 'CDC, art. 76, IV, b')],
  peg='Trocar 60 por 70.', kw=['maior de sessenta anos', 'agravantes'])
I(P, 1, 'Assistência no processo penal',
  'No processo penal por crime contra as relações de consumo, podem intervir como assistentes do Ministério Público os legitimados para a defesa coletiva do consumidor.', 'C',
  'Art. 80 (remete ao art. 82, III e IV, do CDC), que também lhes permite a ação penal subsidiária.',
  lei=[(CD + '80', 'poderão intervir, como assistentes do Ministério Público, os legitimados indicados no art. 82, inciso III e IV', None, 'CDC, art. 80')],
  kw=['assistentes do Ministério Público'])
# --- LPE-18 · Rodada 2
I(P, 2, 'Recall',
  'Incorre nas penas do art. 64 do CDC quem deixa de retirar do mercado, imediatamente quando determinado pela autoridade, os produtos nocivos ou perigosos.', 'C',
  'Art. 64, par. ún.',
  lei=[(CD + '64', 'quem deixar de retirar do mercado, imediatamente quando determinado pela autoridade competente', None, 'CDC, art. 64, par. ún.')],
  kw=['retirar do mercado'])
I(P, 2, 'Acesso a cadastros',
  'Impedir o acesso do consumidor às informações que sobre ele constem em cadastros é crime punido com reclusão, de 1 a 4 anos.', 'E',
  'Art. 72: **detenção de seis meses a um ano ou multa** — os crimes do CDC são, em regra, de menor potencial ofensivo.',
  lei=[(CD + '72', 'Pena Detenção de seis meses a um ano ou multa.', None, 'CDC, art. 72, pena')],
  peg='Inflar a pena.', kw=['cadastros', 'detenção'])
I(P, 2, 'Publicidade enganosa',
  'O crime de publicidade enganosa ou abusiva do CDC exige dolo direto, não alcançando quem apenas deveria saber do caráter enganoso.', 'E',
  'Art. 67: pune quem faz ou promove publicidade que **sabe ou deveria saber** ser enganosa ou abusiva.',
  lei=[(CD + '67', 'Fazer ou promover publicidade que sabe ou deveria saber ser enganosa ou abusiva:', None, 'CDC, art. 67')],
  peg='Restringir ao dolo direto.', kw=['sabe ou deveria saber'])

# ======================= LPE-19 · Contravenções penais =======================
P = 'DBA26-LPE-19'
I(P, 1, 'Tentativa',
  'Não é punível a tentativa de contravenção.', 'C',
  'Art. 4º da LCP.',
  lei=[(CV + '4', 'Não é punível a tentativa de contravenção.', None, 'LCP, art. 4º')],
  kw=['tentativa de contravenção'])
I(P, 1, 'Territorialidade',
  'A lei brasileira aplica-se à contravenção praticada no estrangeiro contra brasileiro, nas hipóteses de extraterritorialidade do Código Penal.', 'E',
  'Art. 2º: a lei brasileira **só** se aplica à contravenção praticada **no território nacional**.',
  lei=[(CV + '2', 'A lei brasileira só é aplicável à contravenção praticada no território nacional.', None, 'LCP, art. 2º')],
  peg='Estender a extraterritorialidade.', kw=['território nacional'])
I(P, 1, 'Vias de fato contra a mulher',
  'Se a contravenção de vias de fato é praticada contra a mulher por razões da condição do sexo feminino, aplica-se a pena em triplo.', 'C',
  'Art. 21, § 2º (Lei 14.994/2024); contra maior de 60 anos, +1/3 até a metade (§ 1º).',
  lei=[(CV + '21', 'aplica-se a pena em triplo', None, 'LCP, art. 21, § 2º')],
  kw=['vias de fato', 'em triplo'])
I(P, 1, 'Direção sem habilitação',
  'Dirigir veículo sem habilitação em via terrestre, sem gerar perigo, continua configurando a contravenção do art. 32 da LCP.', 'E',
  '**Súmula 720/STF**: o art. 309 do CTB **derrogou** o art. 32 da LCP quanto às vias terrestres; sem perigo de dano, há só infração administrativa (a contravenção subsiste para embarcação a motor em águas públicas).',
  lei=[(CV + '32', 'Dirigir, sem a devida habilitação, veículo na via pública, ou embarcação a motor em aguas públicas:', None, 'LCP, art. 32')],
  juris=[J['STF720']], peg='Ignorar a derrogação.', kw=['Súmula 720/STF', 'derrogou'])
I(P, 1, 'Jogo de azar',
  'Para a LCP, consideram-se jogos de azar também as apostas sobre qualquer competição esportiva.', 'C',
  'Art. 50, § 3º, c (salvo as modalidades autorizadas por lei específica).',
  lei=[(CV + '50', 'c) as apostas sobre qualquer outra competição esportiva.', None, 'LCP, art. 50, § 3º, c')],
  kw=['jogo de azar', 'competição esportiva'])
# --- LPE-19 · Rodada 2
I(P, 2, 'Voluntariedade',
  'Para a existência da contravenção, basta a ação ou omissão voluntária, devendo-se considerar o dolo ou a culpa quando a lei fizer depender deles algum efeito jurídico.', 'C',
  'Art. 3º.',
  lei=[(CV + '3', 'Para a existência da contravenção, basta a ação ou omissão voluntária.', None, 'LCP, art. 3º')],
  kw=['ação ou omissão voluntária'])
I(P, 2, 'Recusa de identificação',
  'Recusar à autoridade, quando justificadamente solicitados, dados sobre a própria identidade é conduta atípica, abrangida pelo direito ao silêncio.', 'E',
  'Art. 68 da LCP: é **contravenção** (e prestar declarações falsas sobre identidade, a forma do par. ún.); o silêncio protege o mérito, não a qualificação.',
  lei=[(CV + '68', 'Recusar à autoridade, quando por esta, justificadamente solicitados ou exigidos, dados ou indicações concernentes à própria identidade', None, 'LCP, art. 68')],
  peg='Estender o silêncio à qualificação.', kw=['própria identidade', 'contravenção'])
I(P, 2, 'Competência',
  'Compete à Justiça Estadual o processo por contravenção penal, ainda que praticada em detrimento de bens, serviços ou interesse da União.', 'C',
  '**Súmula 38/STJ** (CF, art. 109, IV, exclui as contravenções).',
  juris=[J['S38']], kw=['Súmula 38/STJ', 'Justiça Estadual'])

# ======================= LPE-20 · Crimes ambientais =======================
P = 'DBA26-LPE-20'
I(P, 1, 'Pessoa jurídica',
  'As pessoas jurídicas serão responsabilizadas penalmente pelos crimes ambientais cometidos por decisão de seu representante legal ou contratual, ou de seu órgão colegiado, no interesse ou benefício da entidade.', 'C',
  'Art. 3º (CF, art. 225, § 3º).',
  lei=[(AM + '3', 'As pessoas jurídicas serão responsabilizadas administrativa, civil e penalmente', None, 'Lei 9.605/1998, art. 3º')],
  kw=['pessoas jurídicas', 'penalmente'])
I(P, 1, 'Dupla imputação',
  'A ação penal contra a pessoa jurídica por crime ambiental só pode prosseguir se houver imputação simultânea a uma pessoa física.', 'E',
  'STF, **RE 548.181** (Primeira Turma, 06/08/2013): afastada a exigência da **dupla imputação**. O art. 3º, par. ún., só diz que a responsabilidade da PJ não exclui a das pessoas físicas.',
  lei=[(AM + '3', 'A responsabilidade das pessoas jurídicas não exclui a das pessoas físicas', None, 'Lei 9.605/1998, art. 3º, par. ún.')],
  juris=[J['RE548181']], peg='Exigir dupla imputação.', kw=['RE 548.181', 'dupla imputação'])
I(P, 1, 'Substituição da pena',
  'Na Lei 9.605/1998, as penas restritivas de direitos substituem as privativas quando se tratar de crime culposo ou de pena privativa inferior a quatro anos, presentes os requisitos subjetivos.', 'C',
  'Art. 7º, I e II; a restritiva terá a mesma duração da privativa substituída (par. ún.).',
  lei=[(AM + '7', 'I - tratar-se de crime culposo ou for aplicada a pena privativa de liberdade inferior a quatro anos;', None, 'Lei 9.605/1998, art. 7º, I')],
  kw=['inferior a quatro anos', 'crime culposo'])
I(P, 1, 'Maus-tratos a cão ou gato',
  'Quando os maus-tratos atingem cão ou gato, a pena é de reclusão, de 2 a 5 anos, multa e proibição da guarda.', 'C',
  'Art. 32, § 1º-A (Lei 14.064/2020) — por isso não é infração de menor potencial ofensivo.',
  lei=[(AM + '32', 'Quando se tratar de cão ou gato, a pena para as condutas descritas no caput deste artigo será de reclusão, de 2 (dois) a 5 (cinco) anos, multa e proibição da guarda.', None, 'Lei 9.605/1998, art. 32, § 1º-A')],
  kw=['cão ou gato', 'proibição da guarda'])
I(P, 1, 'Pesca e fauna',
  'O crime de matar ou caçar espécimes da fauna silvestre do art. 29 da Lei 9.605/1998 aplica-se também aos atos de pesca.', 'E',
  'Art. 29, § 6º: as disposições do artigo **não se aplicam aos atos de pesca**, que têm tipos próprios (arts. 33 a 35).',
  lei=[(AM + '29', 'As disposições deste artigo não se aplicam aos atos de pesca.', None, 'Lei 9.605/1998, art. 29, § 6º')],
  peg='Misturar caça e pesca.', kw=['atos de pesca'])
I(P, 1, 'Transação ambiental',
  'Nos crimes ambientais de menor potencial ofensivo, a transação penal pode ser proposta independentemente de prévia composição do dano ambiental.', 'E',
  'Art. 27: a proposta **somente** poderá ser formulada se houver **prévia composição do dano ambiental**, salvo comprovada impossibilidade.',
  lei=[(AM + '27', 'Nos crimes ambientais de menor potencial ofensivo, a proposta de aplicação imediata de pena restritiva de direitos ou multa', None, 'Lei 9.605/1998, art. 27')],
  peg='Dispensar a composição prévia.', kw=['prévia composição do dano', 'transação'])
I(P, 1, 'Penas da pessoa jurídica',
  'Às pessoas jurídicas podem ser aplicadas, pela Lei 9.605/1998, as penas de multa, restritivas de direitos, prestação de serviços à comunidade e, nos casos graves, pena privativa de liberdade convertida em suspensão de atividades.', 'E',
  'Art. 21: multa, restritivas de direitos e prestação de serviços à comunidade — não há pena privativa de liberdade para a PJ.',
  lei=[(AM + '21', 'As penas aplicáveis isolada, cumulativa ou alternativamente às pessoas jurídicas', None, 'Lei 9.605/1998, art. 21')],
  peg='Atribuir privação de liberdade à PJ.', kw=['art. 21', 'multa'])
# --- LPE-20 · Rodada 2
I(P, 2, 'Desastre e animais (2026)',
  'Incorre nas penas dos maus-tratos a animais quem provoca desastre ambiental que prejudique a vida, a integridade física ou o bem-estar de animais silvestres ou domésticos.', 'C',
  'Art. 32, § 1º-C (**Lei 15.355/2026**).',
  lei=[(AM + '32', 'quem provoca desastre ambiental que prejudique a vida, a integridade física ou o bem-estar de animais silvestres ou domésticos', None, 'Lei 9.605/1998, art. 32, § 1º-C')],
  kw=['desastre ambiental', 'Lei 15.355/2026'])
I(P, 2, 'Suspensão do processo ambiental',
  'Na suspensão condicional do processo por crime ambiental, a extinção da punibilidade depende de laudo de constatação de reparação do dano ambiental.', 'C',
  'Art. 28, I; reparação incompleta prorroga o período de prova (II).',
  lei=[(AM + '28', 'dependerá de laudo de constatação de reparação do dano ambiental', None, 'Lei 9.605/1998, art. 28, I')],
  kw=['laudo de constatação', 'reparação do dano ambiental'])
I(P, 2, 'Guarda doméstica',
  'Na guarda doméstica de espécie silvestre não ameaçada de extinção, o juiz deve aplicar a pena, sem possibilidade de perdão judicial.', 'E',
  'Art. 29, § 2º: o juiz **pode deixar de aplicar a pena**, consideradas as circunstâncias (perdão judicial).',
  lei=[(AM + '29', 'pode o juiz, considerando as circunstâncias, deixar de aplicar a pena', None, 'Lei 9.605/1998, art. 29, § 2º')],
  peg='Negar o perdão judicial.', kw=['perdão judicial', 'guarda doméstica'])
I(P, 2, 'Laudo ambiental falso',
  'Elaborar ou apresentar, no licenciamento, laudo ambiental total ou parcialmente falso é crime punido com detenção, de 1 a 3 anos, mesmo na forma dolosa.', 'E',
  'Art. 69-A: dolo, **reclusão de 3 a 6 anos** e multa; a detenção de 1 a 3 anos é a da forma **culposa** (§ 1º).',
  lei=[(AM + '69-A', 'Pena - reclusão, de 3 (três) a 6 (seis) anos, e multa.', None, 'Lei 9.605/1998, art. 69-A, pena')],
  peg='Usar a pena culposa para o dolo.', kw=['laudo', 'reclusão, de 3 (três) a 6 (seis) anos'])
