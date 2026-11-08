# Pente Fino de Direito Processual Penal — CPP-8 (prisão) e 8.1 a 8.6: conceito, espécies, mandado e cumprimento;
# flagrante; temporária; preventiva; necessidade, prisão especial e liberdade provisória; fiança (08/11/2026).
# Atenção (conferido na lei seca oficial, 08/11/2026): Lei 15.272/2025 (art. 310, §§ 5º e 6º; art. 312, §§ 3º e 4º) e
# Lei 15.358/2026 (audiência de custódia por videoconferência, art. 310; art. 313, V) e Lei 15.487/2026 (art. 313, VI).
from base import I
from cpp_juris import J

CPP = 'CPP:'
CF = 'CF:'
TEMP = 'L7960:'

# ======================= CPP-8 · Prisão =======================
P = 'DBA26-CPP-8'
I(P, 1, 'Hipóteses de prisão',
  'Ninguém poderá ser preso senão em flagrante delito ou por ordem escrita e fundamentada da autoridade judiciária competente, em decorrência de prisão cautelar ou em virtude de condenação criminal transitada em julgado.', 'C',
  'Art. 283, caput (Lei 13.964/2019): **flagrante**, **prisão cautelar** (temporária e preventiva) e **prisão-pena** após o trânsito.',
  lei=[(CPP + '283', 'Ninguém poderá ser preso senão em flagrante delito', 'condenação criminal transitada em julgado', 'CPP, art. 283, caput')],
  kw=['prisão cautelar', 'trânsito em julgado'])
I(P, 1, 'Relaxamento',
  'A prisão ilegal será imediatamente relaxada pela autoridade judiciária.', 'C',
  'CF, art. 5º, LXV: **relaxamento** é para a prisão **ilegal**; a **revogação** é para a prisão legal que perdeu o fundamento; a **liberdade provisória**, para a prisão legal desnecessária.',
  lei=[(CF + '5', 'a prisão ilegal será imediatamente relaxada pela autoridade judiciária', None, 'CF, art. 5º, LXV')],
  kw=['relaxamento', 'prisão ilegal'])
I(P, 1, 'Comunicação da prisão',
  'A prisão de qualquer pessoa e o local onde se encontre serão comunicados imediatamente ao juiz competente, ao Ministério Público e à família do preso ou à pessoa por ele indicada.', 'C',
  'Art. 306, caput (a CF, art. 5º, LXII, não menciona o MP; o CPP o inclui).',
  lei=[(CPP + '306', 'A prisão de qualquer pessoa e o local onde se encontre serão comunicados imediatamente ao juiz competente', 'pessoa por ele indicada', 'CPP, art. 306, caput')],
  kw=['comunicados imediatamente', 'Ministério Público'])
I(P, 1, 'Medidas cautelares e pena de multa',
  'As medidas cautelares pessoais do CPP aplicam-se mesmo à infração a que não seja cominada pena privativa de liberdade.', 'E',
  'Art. 283, § 1º: **não se aplicam** à infração a que não for isolada, cumulativa ou alternativamente cominada **pena privativa de liberdade**.',
  lei=[(CPP + '283', 'As medidas cautelares previstas neste Título não se aplicam à infração', 'pena privativa de liberdade', 'CPP, art. 283, § 1º')],
  peg='Admitir cautelar onde só há multa.',
  kw=['pena privativa de liberdade', 'cautelares'])
I(P, 1, 'Execução provisória de restritiva',
  'A execução da pena restritiva de direitos pode ter início antes do trânsito em julgado da condenação, após o julgamento em segunda instância.', 'E',
  '**Súmula 643/STJ**: depende do **trânsito em julgado**.',
  juris=[J['S643']],
  peg='Admitir execução provisória da restritiva.',
  kw=['Súmula 643', 'restritiva de direitos'])
# --- CPP-8 · Rodada 2
I(P, 2, 'Prisão e liberdade provisória na CF',
  'Ninguém será levado à prisão ou nela mantido quando a lei admitir a liberdade provisória, com ou sem fiança.', 'C',
  '**CF, art. 5º, LXVI**.',
  lei=[(CF + '5', 'ninguém será levado à prisão ou nela mantido, quando a lei admitir a liberdade provisória, com ou sem fiança', None, 'CF, art. 5º, LXVI')],
  kw=['liberdade provisória', 'com ou sem fiança'])
I(P, 2, 'Separação dos presos',
  'As pessoas presas provisoriamente ficarão separadas das que já estiverem definitivamente condenadas.', 'C',
  'Art. 300 do CPP; os presos temporários também ficam separados dos demais (Lei 7.960/1989, art. 3º).',
  lei=[(CPP + '300', 'As pessoas presas provisoriamente ficarão separadas das que já estiverem definitivamente condenadas', None, 'CPP, art. 300')],
  kw=['separação', 'presos provisórios'])
I(P, 2, 'Excesso de prazo superado',
  'Pronunciado o réu, fica superada a alegação de constrangimento ilegal da prisão por excesso de prazo na instrução.', 'C',
  '**Súmula 21/STJ** (no mesmo sentido, encerrada a instrução — Súmula 52/STJ; excesso provocado pela defesa — Súmula 64/STJ).',
  juris=[J['S21'], J['S52'], J['S64']],
  kw=['excesso de prazo', 'Súmula 21'])

# ======================= CPP-8.1 · Conceito, espécies, mandado e cumprimento =======================
P = 'DBA26-CPP-8.1'
I(P, 1, 'Dia e hora',
  'A prisão só poderá ser efetuada durante o dia, das 6 às 18 horas.', 'E',
  'Art. 283, § 2º: a prisão pode ser efetuada **em qualquer dia e a qualquer hora**, respeitada a inviolabilidade do domicílio.',
  lei=[(CPP + '283', 'A prisão poderá ser efetuada em qualquer dia e a qualquer hora', 'inviolabilidade do domicílio', 'CPP, art. 283, § 2º')],
  peg='Transpor à prisão a limitação de horário da casa.',
  kw=['qualquer dia e a qualquer hora', 'inviolabilidade do domicílio'])
I(P, 1, 'Emprego de força',
  'No cumprimento da prisão é permitido o emprego de força, salvo se o preso não oferecer resistência.', 'E',
  'Art. 284: **não será permitido** o emprego de força, **salvo a indispensável** no caso de resistência ou de tentativa de fuga. A regra é a vedação.',
  lei=[(CPP + '284', 'Não será permitido o emprego de força, salvo a indispensável no caso de resistência ou de tentativa de fuga do preso', None, 'CPP, art. 284')],
  peg='Inverter regra e exceção.',
  kw=['emprego de força', 'indispensável'])
I(P, 1, 'Mandado e infração inafiançável',
  'Se a infração for inafiançável, a falta de exibição do mandado não obstará a prisão, e o preso será imediatamente apresentado ao juiz que tiver expedido o mandado, para a realização de audiência de custódia.', 'C',
  'Art. 287 (Lei 13.964/2019).',
  lei=[(CPP + '287', 'Se a infração for inafiançável, a falta de exibição do mandado não obstará a prisão', 'para a realização de audiência de custódia', 'CPP, art. 287')],
  kw=['inafiançável', 'exibição do mandado'])
I(P, 1, 'Registro no CNJ',
  'O juiz competente providenciará o imediato registro do mandado de prisão em banco de dados mantido pelo Conselho Nacional de Justiça.', 'C',
  'Art. 289-A: qualquer agente pode cumprir mandado registrado no **BNMP**, ainda que fora da competência territorial do juiz que o expediu (§ 1º).',
  lei=[(CPP + '289-A', 'O juiz competente providenciará o imediato registro do mandado de prisão em banco de dados mantido pelo Conselho Nacional de Justiça', None, 'CPP, art. 289-A, caput')],
  kw=['banco de dados', 'CNJ'])
I(P, 1, 'Resistência à prisão',
  'Havendo resistência à prisão, ainda que por parte de terceiros, o executor e quem o auxiliar podem usar dos meios necessários para defender-se ou vencer a resistência, lavrando-se auto subscrito também por duas testemunhas.', 'C',
  'Art. 292, caput: **auto de resistência**.',
  lei=[(CPP + '292', 'Se houver, ainda que por parte de terceiros, resistência à prisão', 'subscrito também por duas testemunhas', 'CPP, art. 292, caput')],
  kw=['resistência', 'duas testemunhas'])
I(P, 1, 'Algemas e parto',
  'É permitido o uso de algemas em mulheres grávidas durante o trabalho de parto, desde que haja risco de fuga.', 'E',
  'Art. 292, par. ún.: é **vedado** o uso de algemas durante os atos médico-hospitalares preparatórios do parto, o **trabalho de parto** e o **puerpério imediato**, sem ressalva.',
  lei=[(CPP + '292', 'É vedado o uso de algemas em mulheres grávidas', 'puerpério imediato', 'CPP, art. 292, par. ún.')],
  peg='Criar exceção onde a lei veda sem ressalva.',
  kw=['algemas', 'trabalho de parto'])
I(P, 1, 'Prisão especial — estabelecimento',
  'Não havendo estabelecimento específico para o preso especial, ele deverá ser posto em liberdade até o trânsito em julgado.', 'E',
  'Art. 295, § 2º: será recolhido em **cela distinta** do mesmo estabelecimento.',
  lei=[(CPP + '295', 'Não havendo estabelecimento específico para o preso especial, este será recolhido em cela distinta do mesmo estabelecimento', None, 'CPP, art. 295, § 2º')],
  peg='Transformar a falta de cela especial em liberdade.',
  kw=['prisão especial', 'cela distinta'])
# --- CPP-8.1 · Rodada 2
I(P, 2, 'Algemas — SV 11',
  'Segundo súmula vinculante, a excepcionalidade do uso de algemas deve ser justificada por escrito, sob pena de responsabilidade disciplinar, civil e penal do agente e de nulidade da prisão ou do ato processual.', 'C',
  '**SV 11**.',
  juris=[J['SV11']],
  kw=['SV 11', 'justificada por escrito'])
I(P, 2, 'Prisão em outra comarca',
  'Quando o acusado estiver no território nacional, fora da jurisdição do juiz processante, será deprecada a sua prisão, devendo constar da precatória o inteiro teor do mandado.', 'C',
  'Art. 289, caput. Havendo urgência, a requisição pode ser feita por qualquer meio de comunicação (§ 1º).',
  lei=[(CPP + '289', 'Quando o acusado estiver no território nacional, fora da jurisdição do juiz processante, será deprecada a sua prisão', None, 'CPP, art. 289, caput')],
  kw=['carta precatória', 'prisão deprecada'])
I(P, 2, 'Perseguição',
  'Se o réu, sendo perseguido, passar ao território de outro município ou comarca, o executor só poderá efetuar a prisão após autorização do juiz do local.', 'E',
  'Art. 290: o executor **poderá efetuar-lhe a prisão no lugar onde o alcançar**, apresentando-o à autoridade local.',
  lei=[(CPP + '290', 'Se o réu, sendo perseguido, passar ao território de outro município ou comarca, o executor poderá efetuar-lhe a prisão no lugar onde o alcançar', None, 'CPP, art. 290, caput')],
  peg='Exigir autorização prévia.',
  kw=['perseguição', 'onde o alcançar'])
I(P, 2, 'Entrada em casa de dia',
  'Verificado que o réu procurado está em casa e não obedecida a intimação ao morador para entregá-lo, o executor, sendo dia, convocará duas testemunhas e entrará à força na casa, arrombando as portas, se preciso.', 'C',
  'Art. 293, caput.',
  lei=[(CPP + '293', 'sendo dia, entrará à força na casa, arrombando as portas, se preciso', None, 'CPP, art. 293, caput')],
  kw=['de dia', 'arrombando as portas'])

# ======================= CPP-8.2 · Prisão em flagrante =======================
P = 'DBA26-CPP-8.2'
I(P, 1, 'Flagrante facultativo e obrigatório',
  'Qualquer do povo poderá e as autoridades policiais e seus agentes deverão prender quem quer que seja encontrado em flagrante delito.', 'C',
  'Art. 301: flagrante **facultativo** (qualquer do povo) e **obrigatório** (autoridades policiais e agentes).',
  lei=[(CPP + '301', 'Qualquer do povo poderá e as autoridades policiais e seus agentes deverão prender', 'flagrante delito', 'CPP, art. 301')],
  kw=['flagrante obrigatório', 'flagrante facultativo'])
I(P, 1, 'Flagrante próprio',
  'Considera-se em flagrante delito quem está cometendo a infração penal ou acaba de cometê-la.', 'C',
  'Art. 302, I e II: flagrante **próprio** (real, perfeito).',
  lei=[(CPP + '302', 'está cometendo a infração penal', None, 'CPP, art. 302, I'),
       (CPP + '302', 'acaba de cometê-la', None, 'CPP, art. 302, II')],
  kw=['flagrante próprio', 'acaba de cometê-la'])
I(P, 1, 'Flagrante impróprio',
  'Está em flagrante impróprio quem é encontrado, logo depois, com instrumentos, armas, objetos ou papéis que façam presumir ser ele o autor da infração.', 'E',
  'Essa é a hipótese do art. 302, IV: flagrante **presumido** (ficto). **Impróprio** (quase flagrante) é o do inciso III: **perseguido, logo após**.',
  lei=[(CPP + '302', 'é perseguido, logo após, pela autoridade, pelo ofendido ou por qualquer pessoa', 'autor da infração', 'CPP, art. 302, III')],
  peg='Trocar o flagrante impróprio (III) pelo presumido (IV).',
  kw=['flagrante impróprio', 'perseguido, logo após'])
I(P, 1, 'Crime permanente',
  'Nas infrações permanentes, entende-se o agente em flagrante delito enquanto não cessar a permanência.', 'C',
  'Art. 303. O ingresso em domicílio, porém, depende de fundadas razões prévias (Tema 280/RG).',
  lei=[(CPP + '303', 'Nas infrações permanentes, entende-se o agente em flagrante delito enquanto não cessar a permanência', None, 'CPP, art. 303')],
  juris=[J['RG280']],
  kw=['infrações permanentes', 'permanência'])
I(P, 1, 'Flagrante preparado',
  'O flagrante preparado pela polícia, que torna impossível a consumação do crime, é válido, pois o agente revelou sua intenção criminosa.', 'E',
  '**Súmula 145/STF**: **não há crime** quando a preparação do flagrante pela polícia torna impossível a consumação (crime impossível). Diferente do flagrante **esperado**, que é válido.',
  juris=[J['STF145']],
  peg='Confundir flagrante preparado com esperado.',
  kw=['flagrante preparado', 'Súmula 145'])
I(P, 1, 'Ordem do auto',
  'Apresentado o preso, a autoridade ouvirá o condutor, colhendo desde logo sua assinatura e entregando-lhe cópia do termo e recibo de entrega do preso; em seguida, ouvirá as testemunhas e interrogará o acusado.', 'C',
  'Art. 304, caput: **condutor → testemunhas → conduzido**.',
  lei=[(CPP + '304', 'Apresentado o preso à autoridade competente, ouvirá esta o condutor', 'recibo de entrega do preso', 'CPP, art. 304, caput')],
  kw=['condutor', 'auto de prisão em flagrante'])
I(P, 1, 'Falta de testemunhas',
  'A falta de testemunhas da infração impede a lavratura do auto de prisão em flagrante.', 'E',
  'Art. 304, § 2º: **não impede**; assinam com o condutor pelo menos **duas pessoas** que tenham testemunhado a **apresentação** do preso.',
  lei=[(CPP + '304', 'A falta de testemunhas da infração não impedirá o auto de prisão em flagrante', 'apresentação do preso à autoridade', 'CPP, art. 304, § 2º')],
  peg='Exigir testemunhas do fato.',
  kw=['testemunhas de apresentação', 'auto de prisão'])
I(P, 1, 'Nota de culpa e prazo',
  'Em até 24 horas após a prisão, será encaminhado ao juiz o auto de prisão em flagrante e, se o autuado não informar advogado, cópia integral à Defensoria Pública, entregando-se ao preso, no mesmo prazo, a nota de culpa.', 'C',
  'Art. 306, §§ 1º e 2º.',
  lei=[(CPP + '306', 'Em até 24 (vinte e quatro) horas após a realização da prisão, será encaminhado ao juiz competente o auto de prisão em flagrante', 'cópia integral para a Defensoria Pública', 'CPP, art. 306, § 1º'),
       (CPP + '306', 'No mesmo prazo, será entregue ao preso, mediante recibo, a nota de culpa', 'os das testemunhas', 'CPP, art. 306, § 2º')],
  kw=['24 horas', 'nota de culpa'])
I(P, 1, 'Audiência de custódia por videoconferência',
  'Após a Lei 15.358/2026, a audiência de custódia deve ser realizada presencialmente, vedado o emprego de videoconferência.', 'E',
  'O art. 310, caput, passou a prever audiência **por meio de videoconferência em tempo real**; a forma presencial é exceção, por força maior e decisão justificada (§ 13).',
  lei=[(CPP + '310', 'o juiz deverá promover, por meio de videoconferência em tempo real, audiência de custódia', None, 'CPP, art. 310, caput'),
       (CPP + '310', 'Em situações excepcionais decorrentes de força maior, poderá a audiência de custódia ser realizada presencialmente', None, 'CPP, art. 310, § 13')],
  peg='Repetir a vedação à videoconferência da redação de 2019.',
  kw=['videoconferência', 'Lei 15.358/2026'])
I(P, 1, 'Decisões na custódia',
  'Na audiência de custódia, o juiz deverá, fundamentadamente, relaxar a prisão ilegal, converter o flagrante em preventiva quando presentes os requisitos do art. 312 e inadequadas as cautelares diversas, ou conceder liberdade provisória, com ou sem fiança.', 'C',
  'Art. 310, I a III.',
  lei=[(CPP + '310', 'relaxar a prisão ilegal', None, 'CPP, art. 310, I'),
       (CPP + '310', 'conceder liberdade provisória, com ou sem fiança', None, 'CPP, art. 310, III')],
  kw=['relaxar', 'converter'])
# --- CPP-8.2 · Rodada 2
I(P, 2, 'Circunstâncias que recomendam a conversão',
  'Desde a Lei 15.272/2025, são circunstâncias que, sem prejuízo de outras, recomendam a conversão do flagrante em preventiva, entre outras, a prática reiterada de infrações, a violência ou grave ameaça contra a pessoa e a fuga ou o perigo de fuga.', 'C',
  'Art. 310, § 5º; a decisão deve examinar essas circunstâncias (§ 6º).',
  lei=[(CPP + '310', 'São circunstâncias que, sem prejuízo de outras, recomendam a conversão da prisão em flagrante em preventiva', None, 'CPP, art. 310, § 5º')],
  kw=['Lei 15.272/2025', 'conversão'])
I(P, 2, 'Denegação obrigatória',
  'Se o juiz verificar que o agente é reincidente, integra organização criminosa armada ou milícia, ou porta arma de fogo de uso restrito, deverá denegar a liberdade provisória, com ou sem medidas cautelares.', 'C',
  'Art. 310, § 2º (Lei 13.964/2019) — dispositivo de constitucionalidade discutida na doutrina, mas vigente na letra.',
  lei=[(CPP + '310', 'Se o juiz verificar que o agente é reincidente ou que integra organização criminosa armada ou milícia', 'com ou sem medidas cautelares', 'CPP, art. 310, § 2º')],
  kw=['denegar a liberdade provisória', 'reincidente'])
I(P, 2, 'Excludente no flagrante',
  'Se o juiz verificar, pelo auto de prisão em flagrante, que o agente agiu em legítima defesa, deverá relaxar a prisão por ilegalidade.', 'E',
  'Art. 310, § 1º: poderá conceder **liberdade provisória**, mediante termo de comparecimento a todos os atos. A prisão em flagrante não é ilegal por isso.',
  lei=[(CPP + '310', 'poderá, fundamentadamente, conceder ao acusado liberdade provisória, mediante termo de comparecimento obrigatório', 'sob pena de revogação', 'CPP, art. 310, § 1º')],
  peg='Trocar liberdade provisória por relaxamento.',
  kw=['excludente de ilicitude', 'liberdade provisória'])
I(P, 2, 'Lugar sem autoridade',
  'Não havendo autoridade no lugar da prisão em flagrante, o preso deve aguardar no local a chegada da autoridade da circunscrição.', 'E',
  'Art. 308: o preso será **logo apresentado** à autoridade do **lugar mais próximo**.',
  lei=[(CPP + '308', 'Não havendo autoridade no lugar em que se tiver efetuado a prisão', 'lugar mais próximo', 'CPP, art. 308')],
  peg='Inventar espera no local.',
  kw=['lugar mais próximo', 'autoridade'])
I(P, 2, 'Filhos do preso',
  'Do auto de prisão em flagrante deverá constar a informação sobre a existência de filhos, suas idades e se possuem deficiência, e o nome e contato de eventual responsável por seus cuidados, indicado pela pessoa presa.', 'C',
  'Art. 304, § 4º (Lei 13.257/2016, Marco Legal da Primeira Infância).',
  lei=[(CPP + '304', 'Da lavratura do auto de prisão em flagrante deverá constar a informação sobre a existência de filhos', 'indicado pela pessoa presa', 'CPP, art. 304, § 4º')],
  kw=['filhos', 'primeira infância'])
I(P, 2, 'Flagrante no JECrim',
  'Nas infrações de menor potencial ofensivo, assumido o compromisso de comparecer ao Juizado, a autoridade policial deve lavrar o auto de prisão em flagrante, mas dispensar a fiança.', 'E',
  'Lei 9.099/1995, art. 69, par. ún.: **não se imporá prisão em flagrante** nem se exigirá fiança; lavra-se **termo circunstanciado**.',
  lei=[('L9099:69', 'não se imporá prisão em flagrante, nem se exigirá fiança', None, 'Lei 9.099/1995, art. 69, par. ún.')],
  peg='Lavrar auto de prisão onde a lei manda lavrar TCO.',
  kw=['termo circunstanciado', 'não se imporá prisão em flagrante'])
I(P, 2, 'Flagrante diferido',
  'Na ação controlada da Lei de Organizações Criminosas, a intervenção policial é retardada para que se concretize no momento mais eficaz à formação de provas, mediante prévia comunicação ao juiz competente.', 'C',
  'Lei 12.850/2013, art. 8º e § 1º: **flagrante diferido** (retardado), com **comunicação prévia** ao juiz.',
  lei=[('L12850:8', 'Consiste a ação controlada em retardar a intervenção policial ou administrativa', 'obtenção de informações', 'Lei 12.850/2013, art. 8º, caput')],
  kw=['ação controlada', 'flagrante diferido'])

# ======================= CPP-8.3 · Prisão temporária =======================
P = 'DBA26-CPP-8.3'
I(P, 1, 'Iniciativa',
  'A prisão temporária será decretada pelo juiz, em face da representação da autoridade policial ou de requerimento do Ministério Público.', 'C',
  'Lei 7.960/1989, art. 2º, caput: **não cabe de ofício**; só na fase de **investigação** (inquérito).',
  lei=[(TEMP + '2', 'A prisão temporária será decretada pelo Juiz, em face da representação da autoridade policial ou de requerimento do Ministério Público', None, 'Lei 7.960/1989, art. 2º, caput')],
  kw=['representação da autoridade policial', 'não cabe de ofício'])
I(P, 1, 'Temporária de ofício',
  'O juiz pode decretar a prisão temporária de ofício durante a ação penal, se imprescindível à instrução.', 'E',
  'A temporária depende de **representação ou requerimento** e é medida da **fase investigatória** (imprescindível às investigações do **inquérito**). Na ação penal, a cautelar é a preventiva.',
  lei=[(TEMP + '1', 'quando imprescindível para as investigações do inquérito policial', None, 'Lei 7.960/1989, art. 1º, I')],
  peg='Levar a temporária à ação penal e ao "de ofício".',
  kw=['fase investigatória', 'inquérito'])
I(P, 1, 'Prazo',
  'A prisão temporária terá o prazo de 5 dias, prorrogável por igual período em caso de extrema e comprovada necessidade.', 'C',
  'Lei 7.960/1989, art. 2º. Nos **hediondos e equiparados**: 30 + 30 dias (Lei 8.072/1990, art. 2º, § 4º).',
  lei=[(TEMP + '2', 'terá o prazo de 5 (cinco) dias, prorrogável por igual período em caso de extrema e comprovada necessidade', None, 'Lei 7.960/1989, art. 2º, caput'),
       ('L8072:2', 'terá o prazo de 30 (trinta) dias, prorrogável por igual período em caso de extrema e comprovada necessidade', None, 'Lei 8.072/1990, art. 2º, § 4º')],
  kw=['5 dias', '30 dias'])
I(P, 1, 'Oitiva do MP',
  'Na hipótese de representação da autoridade policial, o juiz decidirá sobre a temporária sem ouvir o Ministério Público, dada a urgência da medida.', 'E',
  'Lei 7.960/1989, art. 2º, § 1º: o juiz, **antes de decidir, ouvirá o MP**. A decisão sai em **24 horas** (§ 2º).',
  lei=[(TEMP + '2', 'Na hipótese de representação da autoridade policial, o Juiz, antes de decidir, ouvirá o Ministério Público', None, 'Lei 7.960/1989, art. 2º, § 1º')],
  peg='Dispensar a oitiva do MP.',
  kw=['ouvirá o Ministério Público', '24 horas'])
I(P, 1, 'Soltura automática',
  'Decorrido o prazo do mandado de prisão temporária, a autoridade responsável pela custódia deverá, independentemente de nova ordem judicial, pôr imediatamente o preso em liberdade, salvo se já comunicada da prorrogação ou da decretação da preventiva.', 'C',
  'Lei 7.960/1989, art. 2º, § 7º (Lei 13.869/2019). O mandado deve trazer o período e o **dia da soltura** (§ 4º-A).',
  lei=[(TEMP + '2', 'Decorrido o prazo contido no mandado de prisão, a autoridade responsável pela custódia deverá', 'decretação da prisão preventiva', 'Lei 7.960/1989, art. 2º, § 7º')],
  kw=['independentemente de nova ordem', 'soltura'])
I(P, 1, 'Requisitos — STF',
  'Segundo o STF, a ausência de residência fixa do investigado basta, por si só, para a decretação da prisão temporária.', 'E',
  'ADIs **3.360 e 4.109** (11/02/2022): a temporária exige requisitos **cumulativos** e **não** se funda só na falta de residência fixa nem serve para **averiguação**.',
  juris=[J['ADI3360']],
  peg='Usar isoladamente o inciso II do art. 1º.',
  kw=['ADI 3.360', 'residência fixa'])
I(P, 1, 'Separação do preso temporário',
  'Os presos temporários deverão permanecer, obrigatoriamente, separados dos demais detentos.', 'C',
  '**Lei 7.960/1989, art. 3º**: separação obrigatória.',
  lei=[(TEMP + '3', 'Os presos temporários deverão permanecer, obrigatoriamente, separados dos demais detentos', None, 'Lei 7.960/1989, art. 3º')],
  kw=['separados', 'presos temporários'])
# --- CPP-8.3 · Rodada 2
I(P, 2, 'Fatos contemporâneos',
  'Para o STF, a temporária deve ser justificada em fatos novos ou contemporâneos e só cabe se insuficientes as medidas cautelares diversas da prisão.', 'C',
  'ADIs 3.360 e 4.109: **contemporaneidade** e **subsidiariedade** (arts. 319 e 320 do CPP).',
  juris=[J['ADI3360']],
  kw=['contemporâneos', 'subsidiariedade'])
I(P, 2, 'Rol de crimes',
  'Segundo o STF, o rol de crimes que admitem prisão temporária pode ser ampliado por analogia, dada a natureza processual da norma.', 'E',
  'O STF exigiu fundadas razões de autoria nos crimes **previstos na lei**, vedadas **analogia** e **interpretação extensiva** do rol.',
  juris=[J['ADI3360']],
  peg='Ampliar o rol por analogia.',
  kw=['rol taxativo', 'analogia'])
I(P, 2, 'Apresentação do preso',
  'O juiz poderá, de ofício ou a requerimento do MP e do advogado, determinar que o preso temporário lhe seja apresentado, solicitar informações da autoridade policial e submetê-lo a exame de corpo de delito.', 'C',
  '**Lei 7.960/1989, art. 2º, § 3º**: controle judicial da custódia.',
  lei=[(TEMP + '2', 'O Juiz poderá, de ofício, ou a requerimento do Ministério Público e do Advogado', 'exame de corpo de delito', 'Lei 7.960/1989, art. 2º, § 3º')],
  kw=['apresentado', 'exame de corpo de delito'])
I(P, 2, 'Nota de culpa da temporária',
  'Decretada a temporária, expede-se mandado em via única, que fica com a autoridade policial, dispensada a nota de culpa.', 'E',
  '**Lei 7.960/1989, art. 2º, § 4º**: mandado em **duas vias**, uma entregue ao indiciado, que **serve como nota de culpa**.',
  lei=[(TEMP + '2', 'expedir-se-á mandado de prisão, em duas vias, uma das quais será entregue ao indiciado e servirá como nota de culpa', None, 'Lei 7.960/1989, art. 2º, § 4º')],
  peg='Dispensar a nota de culpa.',
  kw=['nota de culpa', 'duas vias'])
I(P, 2, 'Temporária e preventiva',
  'Vencido o prazo da temporária, o investigado só pode continuar preso se houver decretação de preventiva ou prorrogação da temporária comunicada à autoridade custodiante.', 'C',
  'Art. 2º, § 7º, da Lei 7.960/1989: sem prorrogação ou preventiva comunicadas, **soltura imediata**.',
  lei=[(TEMP + '2', 'salvo se já tiver sido comunicada da prorrogação da prisão temporária ou da decretação da prisão preventiva', None, 'Lei 7.960/1989, art. 2º, § 7º')],
  kw=['prorrogação', 'preventiva'])

# ======================= CPP-8.4 · Prisão preventiva =======================
P = 'DBA26-CPP-8.4'
I(P, 1, 'Cabimento e iniciativa',
  'Em qualquer fase da investigação policial ou do processo penal caberá a prisão preventiva decretada pelo juiz, a requerimento do MP, do querelante ou do assistente, ou por representação da autoridade policial.', 'C',
  'Art. 311 (Lei 13.964/2019): sem decretação **de ofício** (Súmula 676/STJ).',
  lei=[(CPP + '311', 'Em qualquer fase da investigação policial ou do processo penal, caberá a prisão preventiva', 'representação da autoridade policial', 'CPP, art. 311')],
  juris=[J['S676']],
  kw=['prisão preventiva', 'representação'])
I(P, 1, 'Fundamentos',
  'A preventiva poderá ser decretada como garantia da ordem pública, da ordem econômica, por conveniência da instrução criminal ou para assegurar a aplicação da lei penal, quando houver prova da existência do crime e indício suficiente de autoria e de perigo gerado pelo estado de liberdade do imputado.', 'C',
  'Art. 312, caput: **fumus comissi delicti** e **periculum libertatis**.',
  lei=[(CPP + '312', 'A prisão preventiva poderá ser decretada como garantia da ordem pública', 'perigo gerado pelo estado de liberdade do imputado', 'CPP, art. 312, caput')],
  kw=['periculum libertatis', 'fumus comissi delicti'])
I(P, 1, 'Contemporaneidade',
  'A decisão que decretar a prisão preventiva deve ser motivada e fundamentada em receio de perigo e existência concreta de fatos novos ou contemporâneos que justifiquem a medida.', 'C',
  'Art. 312, § 2º: **contemporaneidade**.',
  lei=[(CPP + '312', 'A decisão que decretar a prisão preventiva deve ser motivada e fundamentada em receio de perigo', 'justifiquem a aplicação da medida adotada', 'CPP, art. 312, § 2º')],
  kw=['contemporaneidade', 'fatos novos'])
I(P, 1, 'Gravidade abstrata',
  'A gravidade abstrata do delito é fundamento suficiente para a prisão preventiva por garantia da ordem pública.', 'E',
  'Art. 312, § 4º (Lei 15.272/2025): é **incabível** preventiva com base em **gravidade abstrata**; exige-se demonstração concreta.',
  lei=[(CPP + '312', 'É incabível a decretação da prisão preventiva com base em alegações de gravidade abstrata do delito', None, 'CPP, art. 312, § 4º')],
  peg='Fundar a prisão na gravidade em abstrato.',
  kw=['gravidade abstrata', 'Lei 15.272/2025'])
I(P, 1, 'Crime doloso com pena superior a 4 anos',
  'Admite-se a preventiva nos crimes dolosos punidos com pena privativa de liberdade máxima igual ou superior a 4 anos.', 'E',
  'Art. 313, I: pena máxima **superior** a 4 anos.',
  lei=[(CPP + '313', 'nos crimes dolosos punidos com pena privativa de liberdade máxima superior a 4 (quatro) anos', None, 'CPP, art. 313, I')],
  peg='Trocar "superior" por "igual ou superior".',
  kw=['superior a 4 anos', 'crimes dolosos'])
I(P, 1, 'Violência doméstica',
  'Admite-se a preventiva se o crime envolver violência doméstica e familiar contra a mulher, criança, adolescente, idoso, enfermo ou pessoa com deficiência, para garantir a execução das medidas protetivas de urgência.', 'C',
  'Art. 313, III.',
  lei=[(CPP + '313', 'se o crime envolver violência doméstica e familiar contra a mulher', 'medidas protetivas de urgência', 'CPP, art. 313, III')],
  kw=['medidas protetivas', 'violência doméstica'])
I(P, 1, 'Vedações',
  'Não será admitida a preventiva com a finalidade de antecipação de cumprimento de pena ou como decorrência imediata de investigação criminal ou da apresentação ou recebimento de denúncia.', 'C',
  'Art. 313, § 2º.',
  lei=[(CPP + '313', 'Não será admitida a decretação da prisão preventiva com a finalidade de antecipação de cumprimento de pena', 'recebimento de denúncia', 'CPP, art. 313, § 2º')],
  kw=['antecipação de pena', 'vedação'])
I(P, 1, 'Revisão periódica',
  'Decretada a preventiva, o órgão emissor deverá revisar a necessidade de sua manutenção a cada 30 dias, sob pena de tornar a prisão ilegal.', 'E',
  'Art. 316, par. ún.: a cada **90 dias**, de ofício, por decisão fundamentada.',
  lei=[(CPP + '316', 'revisar a necessidade de sua manutenção a cada 90 (noventa) dias', 'sob pena de tornar a prisão ilegal', 'CPP, art. 316, par. ún.')],
  peg='Trocar 90 por 30 dias.',
  kw=['90 dias', 'revisar'])
I(P, 1, 'Excludentes',
  'A preventiva pode ser decretada ainda que as provas indiquem que o agente praticou o fato em legítima defesa, se houver risco à instrução.', 'E',
  'Art. 314: **em nenhum caso** será decretada se as provas indicarem excludente de ilicitude (CP, art. 23).',
  lei=[(CPP + '314', 'A prisão preventiva em nenhum caso será decretada', 'art. 23', 'CPP, art. 314')],
  peg='Sobrepor o risco processual à excludente.',
  kw=['excludente de ilicitude', 'em nenhum caso'])
I(P, 1, 'Crime organizado ultraviolento',
  'Desde a Lei 15.358/2026, admite-se a preventiva se o crime for cometido por integrante de organização criminosa ultraviolenta, grupo paramilitar ou milícia privada, no contexto de sua atuação.', 'C',
  'Art. 313, V. A Lei 15.487/2026 incluiu ainda os crimes contra a dignidade sexual de criança ou adolescente (VI).',
  lei=[(CPP + '313', 'se o crime for cometido por integrante de organização criminosa ultraviolenta, grupo paramilitar ou milícia privada', None, 'CPP, art. 313, V')],
  kw=['Lei 15.358/2026', 'organização criminosa ultraviolenta'])
# --- CPP-8.4 · Rodada 2
I(P, 2, 'Periculosidade — critérios',
  'Na aferição da periculosidade geradora de risco à ordem pública devem ser considerados, entre outros, o modus operandi, a participação em organização criminosa, a natureza, a quantidade e a variedade de drogas ou armas apreendidas e o fundado receio de reiteração delitiva.', 'C',
  'Art. 312, § 3º (Lei 15.272/2025).',
  lei=[(CPP + '312', 'Devem ser considerados na aferição da periculosidade do agente', None, 'CPP, art. 312, § 3º')],
  kw=['periculosidade', 'modus operandi'])
I(P, 2, 'Dúvida sobre identidade',
  'Também se admite a preventiva quando houver dúvida sobre a identidade civil da pessoa ou quando ela não fornecer elementos suficientes para esclarecê-la, devendo o preso ser posto em liberdade após a identificação.', 'C',
  'Art. 313, § 1º.',
  lei=[(CPP + '313', 'Também será admitida a prisão preventiva quando houver dúvida sobre a identidade civil da pessoa', None, 'CPP, art. 313, § 1º')],
  kw=['identidade civil', 'preventiva'])
I(P, 2, 'Subsidiariedade',
  'A preventiva somente será determinada quando não for cabível sua substituição por outra medida cautelar, devendo o não cabimento ser justificado de forma fundamentada e individualizada.', 'C',
  'Art. 282, § 6º: preventiva como **ultima ratio**.',
  lei=[(CPP + '282', 'A prisão preventiva somente será determinada quando não for cabível a sua substituição por outra medida cautelar', 'de forma individualizada', 'CPP, art. 282, § 6º')],
  kw=['ultima ratio', 'subsidiariedade'])
I(P, 2, 'Revisão nos tribunais',
  'A exigência de revisar a preventiva a cada 90 dias significa que, vencido o prazo sem revisão, a soltura é automática.', 'E',
  'A lei fala em prisão **ilegal** se não revista, mas prevalece na jurisprudência que a inobservância do prazo **não implica revogação automática**: o juízo competente deve ser instado a reavaliar os fundamentos.',
  lei=[(CPP + '316', 'revisar a necessidade de sua manutenção a cada 90 (noventa) dias', None, 'CPP, art. 316, par. ún.')],
  peg='Tratar a falta de revisão como soltura automática.',
  kw=['revogação automática', '90 dias'])
I(P, 2, 'Revogação e nova decretação',
  'O juiz pode, de ofício, revogar a preventiva se faltar motivo para que subsista, bem como novamente decretá-la de ofício se sobrevierem razões.', 'E',
  'Art. 316: revogar **de ofício** pode; **novamente decretá-la** exige provocação (art. 311; Súmula 676/STJ). A letra do art. 316 fala "de ofício ou a pedido das partes", mas a decretação sem pedido é vedada pela estrutura acusatória.',
  lei=[(CPP + '316', 'O juiz poderá, de ofício ou a pedido das partes, revogar a prisão preventiva', None, 'CPP, art. 316, caput')],
  juris=[J['S676']],
  peg='Admitir decretação de ofício pela via do art. 316.',
  kw=['revogação de ofício', 'decretação'])
I(P, 2, 'Motivação',
  'A decisão que decretar, substituir ou denegar a prisão preventiva será sempre motivada e fundamentada.', 'C',
  'Art. 315, caput; o § 2º lista o que **não** se considera fundamentação (ex.: conceitos jurídicos indeterminados sem explicar a incidência).',
  lei=[(CPP + '315', 'A decisão que decretar, substituir ou denegar a prisão preventiva será sempre motivada e fundamentada', None, 'CPP, art. 315, caput')],
  kw=['motivada e fundamentada', 'art. 315'])
I(P, 2, 'Preventiva e citação por edital',
  'Citado por edital, o acusado que não comparecer nem constituir advogado terá a prisão preventiva decretada automaticamente.', 'E',
  'Art. 366: o juiz **pode**, **se for o caso**, decretar a preventiva, **nos termos do art. 312** — não há decretação automática.',
  lei=[(CPP + '366', 'se for o caso, decretar prisão preventiva, nos termos do disposto no art. 312', None, 'CPP, art. 366')],
  peg='Transformar a revelia citatória em prisão automática.',
  kw=['art. 366', 'não automática'])

# ======================= CPP-8.5 · Necessidade, prisão especial, liberdade provisória =======================
P = 'DBA26-CPP-8.5'
I(P, 1, 'Necessidade e adequação',
  'As medidas cautelares devem observar a necessidade para aplicação da lei penal, para a investigação ou a instrução criminal e, nos casos previstos, para evitar infrações penais, e a adequação à gravidade do crime, às circunstâncias do fato e às condições pessoais do agente.', 'C',
  'Art. 282, I e II: binômio **necessidade–adequação** (proporcionalidade).',
  lei=[(CPP + '282', 'necessidade para aplicação da lei penal, para a investigação ou a instrução criminal', None, 'CPP, art. 282, I'),
       (CPP + '282', 'adequação da medida à gravidade do crime, circunstâncias do fato e condições pessoais do indiciado ou acusado', None, 'CPP, art. 282, II')],
  kw=['necessidade', 'adequação'])
I(P, 1, 'Contraditório prévio',
  'Ressalvados os casos de urgência ou de perigo de ineficácia da medida, o juiz, ao receber o pedido de cautelar, determinará a intimação da parte contrária para se manifestar em 5 dias.', 'C',
  'Art. 282, § 3º: **contraditório prévio** como regra.',
  lei=[(CPP + '282', 'Ressalvados os casos de urgência ou de perigo de ineficácia da medida', 'no prazo de 5 (cinco) dias', 'CPP, art. 282, § 3º')],
  kw=['contraditório prévio', '5 dias'])
I(P, 1, 'Liberdade provisória sem requisitos da preventiva',
  'Ausentes os requisitos da preventiva, o juiz poderá, a seu critério, manter a prisão em flagrante até o fim da instrução.', 'E',
  'Art. 321: ausentes os requisitos, o juiz **deverá conceder liberdade provisória**, impondo, se for o caso, cautelares do art. 319. O flagrante não se mantém por si.',
  lei=[(CPP + '321', 'Ausentes os requisitos que autorizam a decretação da prisão preventiva, o juiz deverá conceder liberdade provisória', None, 'CPP, art. 321')],
  peg='Manter o flagrante como título prisional autônomo.',
  kw=['deverá conceder liberdade provisória', 'art. 321'])
I(P, 1, 'Prisão especial — rol',
  'Os magistrados, os ministros de Estado e os ministros de confissão religiosa estão entre os que têm direito a prisão especial antes da condenação definitiva.', 'C',
  'Art. 295, I, VI e VIII. A prisão especial vale **até o trânsito em julgado**.',
  lei=[(CPP + '295', 'Serão recolhidos a quartéis ou a prisão especial', 'antes de condenação definitiva', 'CPP, art. 295, caput')],
  kw=['prisão especial', 'antes de condenação definitiva'])
I(P, 1, 'Prisão especial após o trânsito',
  'A prisão especial se estende ao cumprimento da pena após o trânsito em julgado da condenação.', 'E',
  'Art. 295, caput: vale **antes de condenação definitiva**. Depois do trânsito, aplica-se a LEP.',
  lei=[(CPP + '295', 'quando sujeitos a prisão antes de condenação definitiva', None, 'CPP, art. 295, caput')],
  peg='Prolongar a prisão especial à execução da pena.',
  kw=['prisão especial', 'condenação definitiva'])
I(P, 1, 'Liberdade provisória sem fiança',
  'Nos casos em que couber fiança, o juiz, verificando a situação econômica do preso, poderá conceder-lhe liberdade provisória sem fiança, sujeitando-o às obrigações dos arts. 327 e 328 e a outras cautelares, se for o caso.', 'C',
  'Art. 350: dispensa da fiança por **pobreza**.',
  lei=[(CPP + '350', 'Nos casos em que couber fiança, o juiz, verificando a situação econômica do preso', 'se for o caso', 'CPP, art. 350, caput')],
  kw=['situação econômica', 'dispensa de fiança'])
I(P, 1, 'Crimes inafiançáveis e liberdade',
  'Nos crimes inafiançáveis, como o tráfico de drogas, é vedada a liberdade provisória.', 'E',
  'A **inafiançabilidade** impede só a **fiança**; cabe liberdade provisória **sem fiança**, com cautelares, se ausentes os requisitos da preventiva (art. 321).',
  lei=[(CPP + '321', 'o juiz deverá conceder liberdade provisória, impondo, se for o caso, as medidas cautelares previstas no art. 319', None, 'CPP, art. 321')],
  peg='Confundir inafiançabilidade com proibição de liberdade.',
  kw=['inafiançável', 'liberdade provisória sem fiança'])
# --- CPP-8.5 · Rodada 2
I(P, 2, 'Diplomados',
  'O CPP ainda prevê prisão especial para os diplomados por faculdades superiores, mas o dispositivo é objeto de controle no STF (ADPF 334).', 'C',
  'Art. 295, VII, traz a anotação **"Vide ADPF nº 334"** na lei oficial. Não use o inciso como certo em prova sem conferir o resultado.',
  lei=[(CPP + '295', 'os diplomados por qualquer das faculdades superiores da República; (Vide ADPF nº 334)', None, 'CPP, art. 295, VII')],
  kw=['diplomados', 'ADPF 334'])
I(P, 2, 'Substituição e revogação',
  'O juiz poderá, de ofício ou a pedido das partes, revogar a medida cautelar ou substituí-la quando verificar a falta de motivo para que subsista, bem como voltar a decretá-la, se sobrevierem razões que a justifiquem.', 'C',
  'Art. 282, § 5º (cláusula **rebus sic stantibus**).',
  lei=[(CPP + '282', 'O juiz poderá, de ofício ou a pedido das partes, revogar a medida cautelar ou substituí-la', 'razões que a justifiquem', 'CPP, art. 282, § 5º')],
  kw=['rebus sic stantibus', 'revogar'])
I(P, 2, 'Iniciativa das cautelares',
  'As medidas cautelares serão decretadas pelo juiz de ofício ou a requerimento das partes, em qualquer fase.', 'E',
  'Art. 282, § 2º: a **requerimento das partes** ou, na investigação, por **representação da autoridade policial** ou requerimento do MP. Não há decretação **de ofício**.',
  lei=[(CPP + '282', 'As medidas cautelares serão decretadas pelo juiz a requerimento das partes', 'mediante requerimento do Ministério Público', 'CPP, art. 282, § 2º')],
  peg='Manter o "de ofício" anterior a 2019.',
  kw=['requerimento das partes', 'de ofício'])
I(P, 2, 'Descumprimento de cautelar',
  'No caso de descumprimento de obrigação imposta por cautelar, o juiz, mediante requerimento, poderá substituir a medida, impor outra em cumulação ou, em último caso, decretar a preventiva.', 'C',
  'Art. 282, § 4º: preventiva como **último caso**.',
  lei=[(CPP + '282', 'No caso de descumprimento de qualquer das obrigações impostas', 'em último caso, decretar a prisão preventiva', 'CPP, art. 282, § 4º')],
  kw=['descumprimento', 'último caso'])

# ======================= CPP-8.6 · Fiança =======================
P = 'DBA26-CPP-8.6'
I(P, 1, 'Fiança pelo delegado',
  'A autoridade policial somente poderá conceder fiança nos casos de infração cuja pena privativa de liberdade máxima não seja superior a 4 anos.', 'C',
  'Art. 322, caput. Nos demais casos, o juiz decide em **48 horas** (par. ún.).',
  lei=[(CPP + '322', 'A autoridade policial somente poderá conceder fiança', 'não seja superior a 4 (quatro) anos', 'CPP, art. 322, caput')],
  kw=['fiança pelo delegado', '4 anos'])
I(P, 1, 'Fiança e pena mínima',
  'O delegado pode conceder fiança em crime cuja pena mínima não supere 4 anos, ainda que a máxima seja superior.', 'E',
  'O critério do art. 322 é a pena **máxima** não superior a 4 anos.',
  lei=[(CPP + '322', 'cuja pena privativa de liberdade máxima não seja superior a 4 (quatro) anos', None, 'CPP, art. 322, caput')],
  peg='Trocar pena máxima por mínima.',
  kw=['pena máxima', 'fiança'])
I(P, 1, 'Inafiançáveis',
  'Não será concedida fiança nos crimes de racismo, tortura, tráfico ilícito de entorpecentes, terrorismo e hediondos, nem nos cometidos por grupos armados contra a ordem constitucional e o Estado Democrático.', 'C',
  'Art. 323, I a III (espelho da CF, art. 5º, XLII a XLIV).',
  lei=[(CPP + '323', 'nos crimes de racismo', None, 'CPP, art. 323, I'),
       (CPP + '323', 'nos crimes de tortura, tráfico ilícito de entorpecentes e drogas afins, terrorismo e nos definidos como crimes hediondos', None, 'CPP, art. 323, II')],
  kw=['inafiançáveis', 'hediondos'])
I(P, 1, 'Valores',
  'O valor da fiança será de 1 a 100 salários mínimos quando a pena máxima não for superior a 4 anos e de 10 a 200 salários mínimos quando superior a 4 anos.', 'C',
  'Art. 325, I e II.',
  lei=[(CPP + '325', 'de 1 (um) a 100 (cem) salários mínimos', None, 'CPP, art. 325, I'),
       (CPP + '325', 'de 10 (dez) a 200 (duzentos) salários mínimos', None, 'CPP, art. 325, II')],
  kw=['valor da fiança', 'salários mínimos'])
I(P, 1, 'Ajuste do valor',
  'Conforme a situação econômica do preso, a fiança poderá ser dispensada, reduzida até o máximo de 2/3 ou aumentada em até 1.000 vezes.', 'C',
  'Art. 325, § 1º.',
  lei=[(CPP + '325', 'reduzida até o máximo de 2/3 (dois terços); ou', None, 'CPP, art. 325, § 1º, II'),
       (CPP + '325', 'aumentada em até 1.000 (mil) vezes', None, 'CPP, art. 325, § 1º, III')],
  kw=['reduzida', 'aumentada'])
I(P, 1, 'Mudança de residência',
  'O réu afiançado pode mudar de residência livremente, bastando comunicar o novo endereço em até 30 dias.', 'E',
  'Art. 328: não pode mudar de residência **sem prévia permissão** da autoridade processante, nem ausentar-se por mais de **8 dias** sem comunicar onde será encontrado, sob pena de **quebramento**.',
  lei=[(CPP + '328', 'O réu afiançado não poderá, sob pena de quebramento da fiança, mudar de residência, sem prévia permissão da autoridade processante', 'lugar onde será encontrado', 'CPP, art. 328')],
  peg='Trocar "prévia permissão" por "comunicação posterior".',
  kw=['quebramento', 'prévia permissão'])
I(P, 1, 'Momento da fiança',
  'A fiança só pode ser prestada até a sentença de primeiro grau.', 'E',
  'Art. 334: enquanto **não transitar em julgado** a sentença condenatória.',
  lei=[(CPP + '334', 'A fiança poderá ser prestada enquanto não transitar em julgado a sentença condenatória', None, 'CPP, art. 334')],
  peg='Antecipar o limite para a sentença.',
  kw=['trânsito em julgado', 'fiança'])
I(P, 1, 'Recusa do delegado',
  'Recusando ou retardando a autoridade policial a concessão da fiança, o preso só poderá pleiteá-la ao juiz por meio de habeas corpus.', 'E',
  'Art. 335: basta **simples petição** ao juiz, que decide em **48 horas**.',
  lei=[(CPP + '335', 'Recusando ou retardando a autoridade policial a concessão da fiança', 'que decidirá em 48 (quarenta e oito) horas', 'CPP, art. 335')],
  peg='Exigir habeas corpus onde basta simples petição.',
  kw=['recusa', '48 horas'])
# --- CPP-8.6 · Rodada 2
I(P, 2, 'Destino da fiança',
  'O dinheiro ou objetos dados como fiança servirão ao pagamento das custas, da indenização do dano, da prestação pecuniária e da multa, se o réu for condenado, inclusive no caso de prescrição depois da sentença condenatória.', 'C',
  'Art. 336, caput e par. ún.',
  lei=[(CPP + '336', 'O dinheiro ou objetos dados como fiança servirão ao pagamento das custas', 'se o réu for condenado', 'CPP, art. 336, caput')],
  kw=['destino da fiança', 'indenização'])
I(P, 2, 'Quebramento',
  'O quebramento injustificado da fiança importará na perda da totalidade do seu valor.', 'E',
  'Art. 343: perda de **metade** do valor, cabendo ao juiz decidir sobre outras cautelares ou a preventiva. Perda **total** ocorre se o condenado não se apresentar para cumprir a pena (art. 344).',
  lei=[(CPP + '343', 'O quebramento injustificado da fiança importará na perda de metade do seu valor', None, 'CPP, art. 343'),
       (CPP + '344', 'Entender-se-á perdido, na totalidade, o valor da fiança', None, 'CPP, art. 344')],
  peg='Trocar quebramento (metade) por perda (totalidade).',
  kw=['quebramento', 'metade'])
I(P, 2, 'Fiança e preventiva',
  'Não será concedida fiança quando presentes os motivos que autorizam a decretação da prisão preventiva.', 'C',
  'Art. 324, IV.',
  lei=[(CPP + '324', 'quando presentes os motivos que autorizam a decretação da prisão preventiva', None, 'CPP, art. 324, IV')],
  kw=['preventiva', 'fiança'])
I(P, 2, 'Fiança quebrada anteriormente',
  'Não se concede fiança, no mesmo processo, a quem tiver quebrado fiança anteriormente concedida.', 'C',
  'Art. 324, I.',
  lei=[(CPP + '324', 'aos que, no mesmo processo, tiverem quebrado fiança anteriormente concedida', None, 'CPP, art. 324, I')],
  kw=['quebrado fiança', 'mesmo processo'])
I(P, 2, 'Fiança como cautelar autônoma',
  'A fiança não pode ser imposta como medida cautelar autônoma diversa da prisão, sendo sempre vinculada à liberdade provisória do preso em flagrante.', 'E',
  'Art. 319, VIII: a **fiança é cautelar diversa da prisão**, para assegurar o comparecimento, evitar obstrução ou em caso de resistência injustificada a ordem judicial.',
  lei=[(CPP + '319', 'fiança, nas infrações que a admitem, para assegurar o comparecimento a atos do processo', None, 'CPP, art. 319, VIII')],
  peg='Negar a fiança como cautelar autônoma.',
  kw=['fiança', 'cautelar diversa'])
