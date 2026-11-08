# Pente Fino de Direito Processual Penal — CPP-7 (provas) e 7.1 a 7.7: conceito, objeto, classificação e sistemas;
# princípios e procedimento probatório; valoração; ônus; provas ilícitas e cadeia de custódia; meios de prova; busca e
# apreensão (08/11/2026).
from base import I
from cpp_juris import J

CPP = 'CPP:'
CF = 'CF:'

# ======================= CPP-7 · Provas =======================
P = 'DBA26-CPP-7'
I(P, 1, 'Corpo de delito',
  'Quando a infração deixar vestígios, será indispensável o exame de corpo de delito, direto ou indireto, não podendo supri-lo a confissão do acusado.', 'C',
  'Art. 158, caput: **exame de corpo de delito indispensável** nos crimes que deixam vestígios (não transeuntes).',
  lei=[(CPP + '158', 'Quando a infração deixar vestígios, será indispensável o exame de corpo de delito', 'não podendo supri-lo a confissão do acusado', 'CPP, art. 158, caput')],
  kw=['corpo de delito', 'confissão'])
I(P, 1, 'Confissão e materialidade',
  'Desaparecidos os vestígios, a confissão do acusado pode suprir a falta do exame de corpo de delito.', 'E',
  'Desaparecidos os vestígios, quem supre é a **prova testemunhal** (art. 167). A **confissão nunca** supre o exame (art. 158).',
  lei=[(CPP + '167', 'Não sendo possível o exame de corpo de delito, por haverem desaparecido os vestígios', 'a prova testemunhal poderá suprir-lhe a falta', 'CPP, art. 167')],
  peg='Trocar prova testemunhal por confissão.',
  kw=['prova testemunhal', 'vestígios'])
I(P, 1, 'Prioridade do exame',
  'Dar-se-á prioridade à realização do exame de corpo de delito quando se tratar de crime que envolva violência doméstica e familiar contra a mulher ou violência contra criança, adolescente, idoso ou pessoa com deficiência.', 'C',
  'Art. 158, par. ún. (Lei 13.721/2018).',
  lei=[(CPP + '158', 'Dar-se-á prioridade à realização do exame de corpo de delito quando se tratar de crime que envolva', None, 'CPP, art. 158, par. ún.')],
  kw=['prioridade', 'violência doméstica'])
I(P, 1, 'Horário do exame',
  'O exame de corpo de delito só pode ser realizado em dias úteis, no horário de expediente.', 'E',
  'Art. 161: **em qualquer dia e a qualquer hora**.',
  lei=[(CPP + '161', 'O exame de corpo de delito poderá ser feito em qualquer dia e a qualquer hora', None, 'CPP, art. 161')],
  peg='Inventar limitação de horário.',
  kw=['qualquer dia e a qualquer hora', 'exame de corpo de delito'])
I(P, 1, 'Indício',
  'Considera-se indício a circunstância conhecida e provada que, tendo relação com o fato, autorize, por indução, concluir-se a existência de outra ou outras circunstâncias.', 'C',
  'Art. 239 do CPP: **prova indireta**, por raciocínio indutivo.',
  lei=[(CPP + '239', 'Considera-se indício a circunstância conhecida e provada', 'outra ou outras circunstâncias', 'CPP, art. 239')],
  kw=['indício', 'indução'])
# --- CPP-7 · Rodada 2
I(P, 2, 'Juiz e laudo',
  'O juiz fica adstrito às conclusões do laudo pericial, que só pode ser afastado por nova perícia.', 'E',
  'Art. 182: o juiz **não ficará adstrito** ao laudo, podendo aceitá-lo ou rejeitá-lo, no todo ou em parte (sistema **liberatório**).',
  lei=[(CPP + '182', 'O juiz não ficará adstrito ao laudo', 'no todo ou em parte', 'CPP, art. 182')],
  peg='Adotar o sistema vinculatório.',
  kw=['não ficará adstrito', 'laudo'])
I(P, 2, 'Perícia negada',
  'O juiz ou a autoridade policial negará a perícia requerida pelas partes quando não for necessária ao esclarecimento da verdade, salvo o caso de exame de corpo de delito.', 'C',
  'Art. 184 do CPP.',
  lei=[(CPP + '184', 'Salvo o caso de exame de corpo de delito', 'ao esclarecimento da verdade', 'CPP, art. 184')],
  kw=['perícia', 'exame de corpo de delito'])
I(P, 2, 'Documentos em qualquer fase',
  'Salvo os casos expressos em lei, as partes poderão apresentar documentos em qualquer fase do processo.', 'C',
  'Art. 231. Exceção: no **júri**, documento a ser exibido em plenário deve ser juntado com **3 dias úteis** de antecedência (art. 479).',
  lei=[(CPP + '231', 'Salvo os casos expressos em lei, as partes poderão apresentar documentos em qualquer fase do processo', None, 'CPP, art. 231')],
  exc=['Plenário do júri: juntada com antecedência mínima de 3 dias úteis, com ciência à outra parte (art. 479)'],
  kw=['documentos', 'qualquer fase'])

# ======================= CPP-7.1 · Conceito, objeto, classificação e sistemas de avaliação =======================
P = 'DBA26-CPP-7.1'
I(P, 1, 'Livre convencimento motivado',
  'O juiz formará sua convicção pela livre apreciação da prova produzida em contraditório judicial.', 'C',
  'Art. 155: sistema do **livre convencimento motivado** (persuasão racional), a regra no Brasil.',
  lei=[(CPP + '155', 'O juiz formará sua convicção pela livre apreciação da prova produzida em contraditório judicial', None, 'CPP, art. 155, caput')],
  kw=['livre convencimento motivado', 'persuasão racional'])
I(P, 1, 'Íntima convicção',
  'O sistema da íntima convicção foi integralmente abolido do ordenamento brasileiro.', 'E',
  'Ele subsiste no **Tribunal do Júri**: os jurados votam sem fundamentar, sob **sigilo das votações** (CF, art. 5º, XXXVIII, b).',
  lei=[(CF + '5', 'é reconhecida a instituição do júri', None, 'CF, art. 5º, XXXVIII')],
  peg='Esquecer o júri.',
  kw=['íntima convicção', 'Tribunal do Júri'])
I(P, 1, 'Prova tarifada residual',
  'O CPP traz resquício do sistema da prova legal ao exigir, quanto ao estado das pessoas, a observância das restrições estabelecidas na lei civil.', 'C',
  'Art. 155, par. ún.: **estado das pessoas** prova-se como manda a lei civil (ex.: certidão de nascimento para a idade). Também o art. 158 (corpo de delito) é apontado como resquício.',
  lei=[(CPP + '155', 'Somente quanto ao estado das pessoas serão observadas as restrições estabelecidas na lei civil', None, 'CPP, art. 155, par. ún.')],
  kw=['prova tarifada', 'estado das pessoas'])
I(P, 1, 'Objeto da prova',
  'Os fatos notórios, os axiomáticos e as presunções legais absolutas dependem de prova no processo penal.', 'E',
  'São **independentes de prova**: fatos **notórios**, **axiomáticos** (intuitivos), **inúteis** e as **presunções legais absolutas**. O direito, em regra, não se prova (salvo estadual, municipal, estrangeiro ou consuetudinário).',
  lei=[(CPP + '156', 'A prova da alegação incumbirá a quem a fizer', None, 'CPP, art. 156, caput')],
  peg='Exigir prova do que dela independe.',
  kw=['fatos notórios', 'presunções absolutas'])
I(P, 1, 'Elementos informativos',
  'O juiz pode condenar com base exclusiva em provas cautelares, não repetíveis e antecipadas colhidas na investigação.', 'C',
  'É a **ressalva** do art. 155: essas provas sujeitam-se a **contraditório diferido** e podem fundamentar a decisão.',
  lei=[(CPP + '155', 'ressalvadas as provas cautelares, não repetíveis e antecipadas', None, 'CPP, art. 155, caput')],
  kw=['provas cautelares', 'contraditório diferido'])
I(P, 1, 'Classificação — prova direta e indireta',
  'O indício é prova direta, pois demonstra imediatamente o fato principal.', 'E',
  'O **indício** é prova **indireta**: parte de circunstância provada para, por **indução**, chegar a outra (art. 239).',
  lei=[(CPP + '239', 'Considera-se indício a circunstância conhecida e provada', 'outra ou outras circunstâncias', 'CPP, art. 239')],
  peg='Classificar o indício como prova direta.',
  kw=['prova indireta', 'indício'])
# --- CPP-7.1 · Rodada 2
I(P, 2, 'Prova emprestada',
  'A prova emprestada é admitida no processo penal desde que submetida ao contraditório no processo de destino, ainda que a parte não tenha participado do processo de origem.', 'C',
  'Doutrina e jurisprudência admitem a **prova emprestada**, assegurado o **contraditório** sobre ela; a prova ilícita na origem não se convalida (CF, art. 5º, LVI).',
  lei=[(CF + '5', 'são inadmissíveis, no processo, as provas obtidas por meios ilícitos', None, 'CF, art. 5º, LVI')],
  kw=['prova emprestada', 'contraditório'])
I(P, 2, 'Prova cautelar, não repetível e antecipada',
  'Prova antecipada é a produzida perante o juiz, com contraditório, antes do momento processual próprio, em razão de urgência e relevância.', 'C',
  'Ex.: oitiva de testemunha enferma (art. 225) e produção antecipada no art. 366 (com fundamentação concreta — Súmula 455/STJ).',
  lei=[(CPP + '225', 'Se qualquer testemunha houver de ausentar-se, ou, por enfermidade ou por velhice', None, 'CPP, art. 225')],
  juris=[J['S455']],
  kw=['prova antecipada', 'urgência'])
I(P, 2, 'Produção antecipada pelo decurso do tempo',
  'A decisão que determina a produção antecipada de provas com base no art. 366 do CPP pode fundamentar-se unicamente no mero decurso do tempo.', 'E',
  '**Súmula 455/STJ**: exige **fundamentação concreta**; o mero decurso do tempo não basta.',
  juris=[J['S455']],
  peg='Admitir fundamentação genérica.',
  kw=['Súmula 455', 'fundamentação concreta'])
I(P, 2, 'Inquéritos em curso',
  'Inquéritos policiais e ações penais em curso podem ser usados para agravar a pena-base, como maus antecedentes.', 'E',
  '**Súmula 444/STJ**: é **vedado**. Reflexo da presunção de inocência na valoração.',
  juris=[J['S444']],
  peg='Valorar procedimentos em curso como antecedentes.',
  kw=['Súmula 444', 'pena-base'])

# ======================= CPP-7.2 · Princípios gerais da prova; procedimento probatório =======================
P = 'DBA26-CPP-7.2'
I(P, 1, 'Comunhão da prova',
  'Pelo princípio da comunhão da prova, a prova produzida pertence ao processo e não à parte que a requereu, de modo que, após produzida, a parte só pode desistir dela com a concordância da outra.', 'C',
  '**Comunhão (aquisição) da prova**: produzida, serve a ambas as partes e ao juiz. Base: o juiz pode determinar diligências (art. 156, II).',
  lei=[(CPP + '156', 'determinar, no curso da instrução, ou antes de proferir sentença', 'ponto relevante', 'CPP, art. 156, II')],
  kw=['comunhão da prova', 'aquisição'])
I(P, 1, 'Produção antecipada de ofício',
  'O juiz pode, de ofício, ordenar, mesmo antes de iniciada a ação penal, a produção antecipada de provas urgentes e relevantes, observando a necessidade, adequação e proporcionalidade da medida.', 'C',
  'É a **letra do art. 156, I**. A doutrina majoritária vê incompatibilidade com o **art. 3º-A** (vedada a iniciativa do juiz na investigação); a assertiva reproduz o texto legal.',
  lei=[(CPP + '156', 'ordenar, mesmo antes de iniciada a ação penal, a produção antecipada de provas consideradas urgentes e relevantes', 'proporcionalidade da medida', 'CPP, art. 156, I')],
  kw=['produção antecipada', 'art. 3º-A'])
I(P, 1, 'Ordem da audiência',
  'Na audiência de instrução e julgamento, o interrogatório do acusado é o primeiro ato, seguido das declarações do ofendido e da oitiva das testemunhas.', 'E',
  'Art. 400: ofendido → testemunhas de acusação → de defesa → peritos, acareações, reconhecimentos → **interrogatório por último** (meio de defesa).',
  lei=[(CPP + '400', 'proceder-se-á à tomada de declarações do ofendido', 'interrogando-se, em seguida, o acusado', 'CPP, art. 400, caput')],
  peg='Pôr o interrogatório no início (como era antes de 2008).',
  kw=['interrogatório por último', 'audiência de instrução'])
I(P, 1, 'Número de testemunhas',
  'No procedimento ordinário, poderão ser inquiridas até 5 testemunhas arroladas pela acusação e 5 pela defesa.', 'E',
  'Art. 401: no **ordinário**, até **8** por parte. Cinco é o número do sumário (art. 532).',
  lei=[(CPP + '401', 'Na instrução poderão ser inquiridas até 8 (oito) testemunhas arroladas pela acusação e 8 (oito) pela defesa', None, 'CPP, art. 401, caput')],
  peg='Trocar o número do ordinário pelo do sumário.',
  kw=['8 testemunhas', 'procedimento ordinário'])
I(P, 1, 'Exame cruzado',
  'As perguntas às testemunhas são formuladas pelas partes por intermédio do juiz, que as reformula, segundo o sistema presidencialista.', 'E',
  'Desde 2008, art. 212: perguntas **diretamente** à testemunha (**cross-examination**); o juiz só **complementa** os pontos não esclarecidos.',
  lei=[(CPP + '212', 'As perguntas serão formuladas pelas partes diretamente à testemunha', 'repetição de outra já respondida', 'CPP, art. 212, caput')],
  peg='Manter o sistema presidencialista, abandonado em 2008.',
  kw=['diretamente à testemunha', 'cross-examination'])
I(P, 1, 'Liberdade probatória',
  'No processo penal vigora a liberdade dos meios de prova, sendo admitidas provas não previstas em lei (inominadas), desde que não ilícitas.', 'C',
  'Admitem-se provas **inominadas** (atípicas), respeitados os limites constitucionais (art. 5º, LVI) e as restrições da lei civil quanto ao estado das pessoas (art. 155, par. ún.).',
  lei=[(CF + '5', 'são inadmissíveis, no processo, as provas obtidas por meios ilícitos', None, 'CF, art. 5º, LVI')],
  kw=['provas inominadas', 'liberdade probatória'])
# --- CPP-7.2 · Rodada 2
I(P, 2, 'Juiz complementa',
  'Sobre os pontos não esclarecidos, o juiz poderá complementar a inquirição das testemunhas.', 'C',
  'Art. 212, par. ún.: atuação **complementar** do juiz.',
  lei=[(CPP + '212', 'Sobre os pontos não esclarecidos, o juiz poderá complementar a inquirição', None, 'CPP, art. 212, par. ún.')],
  kw=['complementar', 'inquirição'])
I(P, 2, 'Testemunhas não computadas',
  'No limite de testemunhas do procedimento ordinário computam-se também as que não prestam compromisso e as referidas.', 'E',
  'Art. 401, § 1º: **não** se computam as que não prestem compromisso e as **referidas**.',
  lei=[(CPP + '401', 'Nesse número não se compreendem as que não prestem compromisso e as referidas', None, 'CPP, art. 401, § 1º')],
  peg='Incluir no limite quem a lei exclui.',
  kw=['referidas', 'não prestem compromisso'])
I(P, 2, 'Testemunha por precatória',
  'A expedição da carta precatória para inquirição de testemunha suspende a instrução criminal até o seu retorno.', 'E',
  'Art. 222, § 1º: a expedição da precatória **não suspende** a instrução; findo o prazo, pode haver julgamento.',
  lei=[(CPP + '222', 'A expedição da precatória não suspenderá a instrução criminal', None, 'CPP, art. 222, § 1º')],
  peg='Atribuir efeito suspensivo à precatória.',
  kw=['precatória', 'não suspenderá'])
I(P, 2, 'Diligências na audiência',
  'Produzidas as provas, ao final da audiência, o MP, o querelante, o assistente e o acusado poderão requerer diligências cuja necessidade se origine de circunstâncias ou fatos apurados na instrução.', 'C',
  'Art. 402 do CPP.',
  lei=[(CPP + '402', 'Produzidas as provas, ao final da audiência', 'apurados na instrução', 'CPP, art. 402')],
  kw=['diligências', 'art. 402'])

# ======================= CPP-7.3 · Valoração =======================
P = 'DBA26-CPP-7.3'
I(P, 1, 'Valor da confissão',
  'A confissão tem valor absoluto, por ser a rainha das provas, e dispensa o confronto com as demais provas do processo.', 'E',
  'Art. 197: o valor da confissão se afere pelos critérios dos outros elementos; o juiz deve **confrontá-la** com as demais provas. Não há hierarquia de provas.',
  lei=[(CPP + '197', 'O valor da confissão se aferirá pelos critérios adotados para os outros elementos de prova', 'compatibilidade ou concordância', 'CPP, art. 197')],
  peg='Ressuscitar a "rainha das provas".',
  kw=['confissão', 'sem hierarquia'])
I(P, 1, 'Divisibilidade e retratabilidade',
  'A confissão será divisível e retratável, sem prejuízo do livre convencimento do juiz, fundado no exame das provas em conjunto.', 'C',
  'Art. 200 do CPP.',
  lei=[(CPP + '200', 'A confissão será divisível e retratável', 'exame das provas em conjunto', 'CPP, art. 200')],
  kw=['divisível', 'retratável'])
I(P, 1, 'Condenação e inquérito',
  'É possível condenar o réu com base exclusiva em depoimentos colhidos no inquérito policial, se coerentes entre si.', 'E',
  'Art. 155: o juiz **não pode** fundamentar a decisão **exclusivamente** nos elementos informativos da investigação (ressalvadas as provas cautelares, não repetíveis e antecipadas).',
  lei=[(CPP + '155', 'não podendo fundamentar sua decisão exclusivamente nos elementos informativos colhidos na investigação', None, 'CPP, art. 155, caput')],
  peg='Admitir condenação só com o inquérito.',
  kw=['exclusivamente', 'elementos informativos'])
I(P, 1, 'In dubio pro reo',
  'O juiz absolverá o réu quando não existir prova suficiente para a condenação.', 'C',
  'Art. 386, VII: expressão do **in dubio pro reo** na sentença.',
  lei=[(CPP + '386', 'não existir prova suficiente para a condenação', None, 'CPP, art. 386, VII')],
  kw=['in dubio pro reo', 'prova suficiente'])
I(P, 1, 'Silêncio e convencimento',
  'Segundo a letra do art. 198 do CPP, ainda vigente em sua integralidade, o silêncio do acusado pode constituir elemento para a formação do convencimento do juiz.', 'E',
  'A parte final do **art. 198** é tida por **não recepcionada** e incompatível com o art. 186, par. ún. (silêncio não pode ser interpretado em prejuízo da defesa).',
  lei=[(CPP + '186', 'O silêncio, que não importará em confissão, não poderá ser interpretado em prejuízo da defesa', None, 'CPP, art. 186, par. ún.')],
  peg='Valorar o silêncio contra o réu.',
  kw=['silêncio', 'não recepcionada'])
# --- CPP-7.3 · Rodada 2
I(P, 2, 'Reconhecimento fora do art. 226',
  'Para o STJ, o reconhecimento de pessoa feito sem observância do procedimento do art. 226 do CPP é inválido e não pode servir de lastro à condenação, mesmo que confirmado em juízo.', 'C',
  'STJ, **HC 598.886** (27/10/2020): o art. 226 **não é mera recomendação**.',
  lei=[(CPP + '226', 'Quando houver necessidade de fazer-se o reconhecimento de pessoa', 'pela seguinte forma', 'CPP, art. 226, caput')],
  juris=[J['HC598886']],
  kw=['art. 226', 'HC 598.886'])
I(P, 2, 'Colaborador e condenação',
  'A sentença condenatória pode ser proferida com fundamento apenas nas declarações do colaborador premiado, se forem detalhadas.', 'E',
  'Lei 12.850/2013, art. 4º, § 16: **nenhuma** sentença condenatória (nem medida cautelar ou recebimento de denúncia) será proferida **apenas** com base nas declarações do colaborador (regra de corroboração).',
  lei=[('L12850:4', 'Nenhuma das seguintes medidas será decretada ou proferida com fundamento apenas nas declarações do colaborador', None, 'Lei 12.850/2013, art. 4º, § 16')],
  peg='Dispensar corroboração da palavra do colaborador.',
  kw=['colaborador', 'corroboração'])
I(P, 2, 'Valor do laudo',
  'O juiz pode rejeitar o laudo pericial, no todo ou em parte, fundamentadamente.', 'C',
  'Art. 182: sistema **liberatório**.',
  lei=[(CPP + '182', 'O juiz não ficará adstrito ao laudo', 'no todo ou em parte', 'CPP, art. 182')],
  kw=['sistema liberatório', 'laudo'])

# ======================= CPP-7.4 · Ônus da prova =======================
P = 'DBA26-CPP-7.4'
I(P, 1, 'Regra do ônus',
  'A prova da alegação incumbirá a quem a fizer, sendo facultado ao juiz, de ofício, determinar diligências para dirimir dúvida sobre ponto relevante.', 'C',
  'Art. 156: **ônus de quem alega**; atuação judicial supletiva.',
  lei=[(CPP + '156', 'A prova da alegação incumbirá a quem a fizer', None, 'CPP, art. 156, caput')],
  kw=['ônus da prova', 'quem alega'])
I(P, 1, 'Ônus da defesa',
  'Por força da presunção de inocência, a acusação deve provar a autoria e a materialidade, mas, se a defesa alegar excludente de ilicitude, a dúvida razoável sobre ela beneficia o réu.', 'C',
  'Doutrina majoritária: a acusação prova o fato típico; havendo **fundada dúvida** sobre excludente, impõe-se a absolvição (art. 386, VI).',
  lei=[(CPP + '386', 'ou mesmo se houver fundada dúvida sobre sua existência', None, 'CPP, art. 386, VI')],
  kw=['fundada dúvida', 'excludente'])
I(P, 1, 'Inversão do ônus',
  'No processo penal, admite-se a inversão do ônus da prova em desfavor do acusado quando a acusação tiver dificuldade em provar a autoria.', 'E',
  'A **presunção de inocência** (CF, art. 5º, LVII) impede inverter o ônus contra o réu: na dúvida sobre a autoria, absolve-se.',
  lei=[(CF + '5', 'ninguém será considerado culpado até o trânsito em julgado de sentença penal condenatória', None, 'CF, art. 5º, LVII')],
  peg='Importar a inversão do ônus do processo civil.',
  kw=['inversão do ônus', 'presunção de inocência'])
I(P, 1, 'Absolvição por dúvida',
  'A dúvida sobre a existência de circunstância que exclua o crime ou isente o réu de pena impõe a condenação, pois a excludente deve ser cabalmente provada pela defesa.', 'E',
  'Art. 386, VI: absolve-se se houver **fundada dúvida** sobre a existência da excludente.',
  lei=[(CPP + '386', 'ou mesmo se houver fundada dúvida sobre sua existência', None, 'CPP, art. 386, VI')],
  peg='Exigir prova cabal da excludente.',
  kw=['fundada dúvida', 'absolvição'])
I(P, 1, 'Silêncio e ônus',
  'O silêncio do acusado não importará em confissão e não poderá ser interpretado em prejuízo da defesa.', 'C',
  'Art. 186, par. ún.: o silêncio **não transfere ônus** à defesa.',
  lei=[(CPP + '186', 'O silêncio, que não importará em confissão', None, 'CPP, art. 186, par. ún.')],
  kw=['silêncio', 'ônus'])
# --- CPP-7.4 · Rodada 2
I(P, 2, 'Ônus e iniciativa do juiz',
  'Com a estrutura acusatória, o juiz não pode substituir a atuação probatória do órgão de acusação.', 'C',
  'Art. 3º-A: vedada a **substituição da atuação probatória** da acusação; o juiz atua só de modo supletivo (art. 156, II).',
  lei=[(CPP + '3-A', 'a substituição da atuação probatória do órgão de acusação', None, 'CPP, art. 3º-A')],
  kw=['substituição da atuação probatória', 'acusatório'])
I(P, 2, 'Busca pessoal e ônus estatal',
  'Na busca pessoal sem mandado, cabe à defesa provar a ausência de fundada suspeita.', 'E',
  'É do **Estado** o ônus de demonstrar, com **elementos objetivos** anteriores à diligência, a **fundada suspeita** (STJ, RHC 158.580).',
  lei=[(CPP + '244', 'A busca pessoal independerá de mandado', 'corpo de delito', 'CPP, art. 244')],
  juris=[J['RHC158580']],
  peg='Inverter o ônus da fundada suspeita.',
  kw=['fundada suspeita', 'ônus do Estado'])
I(P, 2, 'Estado das pessoas',
  'A prova da menoridade do réu, para fins penais, pode ser feita por qualquer meio, inclusive pela simples declaração do acusado.', 'E',
  'Quanto ao **estado das pessoas**, observam-se as restrições da lei civil (art. 155, par. ún.): a menoridade se prova por documento hábil.',
  lei=[(CPP + '155', 'Somente quanto ao estado das pessoas serão observadas as restrições estabelecidas na lei civil', None, 'CPP, art. 155, par. ún.')],
  peg='Ignorar a restrição do estado das pessoas.',
  kw=['estado das pessoas', 'documento hábil'])

# ======================= CPP-7.5 · Provas ilícitas e cadeia de custódia =======================
P = 'DBA26-CPP-7.5'
I(P, 1, 'Conceito de prova ilícita',
  'São inadmissíveis, devendo ser desentranhadas do processo, as provas ilícitas, assim entendidas as obtidas em violação a normas constitucionais ou legais.', 'C',
  'Art. 157, caput.',
  lei=[(CPP + '157', 'São inadmissíveis, devendo ser desentranhadas do processo, as provas ilícitas', 'normas constitucionais ou legais', 'CPP, art. 157, caput')],
  kw=['prova ilícita', 'desentranhadas'])
I(P, 1, 'Derivadas e exceções',
  'São também inadmissíveis as provas derivadas das ilícitas, salvo quando não evidenciado o nexo de causalidade entre umas e outras, ou quando as derivadas puderem ser obtidas por uma fonte independente das primeiras.', 'C',
  'Art. 157, § 1º: **frutos da árvore envenenada**, com as exceções da **ausência de nexo** e da **fonte independente**.',
  lei=[(CPP + '157', 'São também inadmissíveis as provas derivadas das ilícitas', 'fonte independente das primeiras', 'CPP, art. 157, § 1º')],
  kw=['frutos da árvore envenenada', 'fonte independente'])
I(P, 1, 'Fonte independente',
  'Considera-se fonte independente aquela que por si só, seguindo os trâmites típicos e de praxe da investigação ou instrução, seria capaz de conduzir ao fato objeto da prova.', 'C',
  'Art. 157, § 2º: a definição legal corresponde, na doutrina, à **descoberta inevitável**.',
  lei=[(CPP + '157', 'Considera-se fonte independente aquela que por si só', 'conduzir ao fato objeto da prova', 'CPP, art. 157, § 2º')],
  kw=['fonte independente', 'descoberta inevitável'])
I(P, 1, 'Inutilização',
  'Preclusa a decisão de desentranhamento da prova inadmissível, ela será inutilizada por decisão judicial, vedado às partes acompanhar o incidente.', 'E',
  'Art. 157, § 3º: é **facultado** às partes acompanhar o incidente.',
  lei=[(CPP + '157', 'Preclusa a decisão de desentranhamento da prova declarada inadmissível', 'facultado às partes acompanhar o incidente', 'CPP, art. 157, § 3º')],
  peg='Trocar "facultado" por "vedado".',
  kw=['inutilizada', 'incidente'])
I(P, 1, 'Cadeia de custódia — conceito',
  'Considera-se cadeia de custódia o conjunto de todos os procedimentos utilizados para manter e documentar a história cronológica do vestígio coletado em locais ou em vítimas de crimes, para rastrear sua posse e manuseio a partir de seu reconhecimento até o descarte.', 'C',
  'Art. 158-A, caput (Lei 13.964/2019).',
  lei=[(CPP + '158-A', 'Considera-se cadeia de custódia o conjunto de todos os procedimentos', 'até o descarte', 'CPP, art. 158-A, caput')],
  kw=['cadeia de custódia', 'história cronológica'])
I(P, 1, 'Início da cadeia',
  'O início da cadeia de custódia dá-se apenas com a chegada do perito ao local do crime.', 'E',
  'Art. 158-A, § 1º: inicia com a **preservação do local** de crime ou com procedimentos policiais ou periciais em que se detecte vestígio.',
  lei=[(CPP + '158-A', 'O início da cadeia de custódia dá-se com a preservação do local de crime', 'existência de vestígio', 'CPP, art. 158-A, § 1º')],
  peg='Adiar o início para a chegada do perito.',
  kw=['preservação do local', 'início'])
I(P, 1, 'Etapas da cadeia',
  'A cadeia de custódia compreende as etapas de reconhecimento, isolamento, fixação, coleta, acondicionamento, transporte, recebimento, processamento, armazenamento e descarte.', 'C',
  'Art. 158-B: **dez etapas**, na ordem.',
  lei=[(CPP + '158-B', 'A cadeia de custódia compreende o rastreamento do vestígio nas seguintes etapas', None, 'CPP, art. 158-B, caput')],
  kw=['etapas', 'rastreamento do vestígio'])
I(P, 1, 'Coleta por perito',
  'A coleta dos vestígios deverá ser realizada preferencialmente por perito oficial, e é proibida a entrada em locais isolados ou a remoção de vestígios antes da liberação pelo perito responsável, sob pena de fraude processual.', 'C',
  'Art. 158-C, caput e § 2º.',
  lei=[(CPP + '158-C', 'A coleta dos vestígios deverá ser realizada preferencialmente por perito oficial', None, 'CPP, art. 158-C, caput'),
       (CPP + '158-C', 'É proibida a entrada em locais isolados bem como a remoção de quaisquer vestígios', 'fraude processual a sua realização', 'CPP, art. 158-C, § 2º')],
  kw=['perito oficial', 'fraude processual'])
I(P, 1, 'Cartas interceptadas',
  'As cartas particulares interceptadas ou obtidas por meios criminosos podem ser admitidas em juízo se favoráveis à acusação.', 'E',
  'Art. 233: **não serão admitidas** em juízo. A doutrina admite a prova ilícita **pro reo** (em favor da defesa), não da acusação.',
  lei=[(CPP + '233', 'As cartas particulares, interceptadas ou obtidas por meios criminosos, não serão admitidas em juízo', None, 'CPP, art. 233, caput')],
  peg='Inverter a admissibilidade pro reo.',
  kw=['cartas particulares', 'prova ilícita pro reo'])
# --- CPP-7.5 · Rodada 2
I(P, 2, 'Prova inadmissível e juiz',
  'O STF declarou inconstitucional a regra que impedia o juiz que conheceu do conteúdo da prova inadmissível de proferir a sentença.', 'C',
  'ADIs 6.298 e outras: **art. 157, § 5º, inconstitucional**.',
  juris=[J['ADI6298']],
  kw=['art. 157, § 5º', 'inconstitucional'])
I(P, 2, 'Ingresso em domicílio',
  'Para o STF, a entrada forçada em domicílio sem mandado é lícita, mesmo à noite, quando amparada em fundadas razões, justificadas a posteriori, que indiquem flagrante delito dentro da casa.', 'C',
  '**Tema 280/RG** (RE 603.616): as razões devem existir **antes** do ingresso e ser justificadas depois; o achado posterior não as supre.',
  lei=[(CF + '5', 'a casa é asilo inviolável do indivíduo', 'por determinação judicial', 'CF, art. 5º, XI')],
  juris=[J['RG280']],
  kw=['Tema 280', 'fundadas razões'])
I(P, 2, 'Denúncia anônima e domicílio',
  'A simples denúncia anônima de tráfico, sem outros elementos, autoriza o ingresso forçado em domicílio, por se tratar de crime permanente.', 'E',
  'O crime permanente permite flagrante, mas o ingresso exige **fundadas razões** prévias (Tema 280); a notícia anônima isolada não basta.',
  juris=[J['RG280']],
  peg='Usar a permanência do crime para dispensar fundadas razões.',
  kw=['denúncia anônima', 'crime permanente'])
I(P, 2, 'Interceptação — requisitos',
  'Não será admitida a interceptação telefônica quando a prova puder ser feita por outros meios disponíveis ou quando o fato investigado for punido, no máximo, com detenção.', 'C',
  'Lei 9.296/1996, art. 2º, II e III: **subsidiariedade** e **reclusão**.',
  lei=[('L9296:2', 'a prova puder ser feita por outros meios disponíveis', None, 'Lei 9.296/1996, art. 2º, II'),
       ('L9296:2', 'o fato investigado constituir infração penal punida, no máximo, com pena de detenção', None, 'Lei 9.296/1996, art. 2º, III')],
  kw=['interceptação', 'subsidiariedade'])
I(P, 2, 'Interceptação — prazo',
  'A interceptação telefônica não poderá exceder 15 dias, renovável por igual tempo uma única vez.', 'E',
  'Art. 5º da Lei 9.296/1996: renovável por igual tempo, comprovada a **indispensabilidade**; a jurisprudência admite **renovações sucessivas** fundamentadas.',
  lei=[('L9296:5', 'não poderá exceder o prazo de quinze dias, renovável por igual tempo', 'indispensabilidade do meio de prova', 'Lei 9.296/1996, art. 5º')],
  peg='Limitar a uma única renovação.',
  kw=['quinze dias', 'renovações sucessivas'])
I(P, 2, 'Quebra da cadeia',
  'A quebra da cadeia de custódia gera, automaticamente, a nulidade absoluta da prova pericial, independentemente de qualquer outra análise.', 'E',
  'A lei **não comina nulidade automática** para a quebra da cadeia de custódia; prevalece que o juiz avalia a **confiabilidade** da prova à luz dos demais elementos. A lei define o que se deve preservar (art. 158-A).',
  lei=[(CPP + '158-A', 'Considera-se cadeia de custódia o conjunto de todos os procedimentos', None, 'CPP, art. 158-A, caput')],
  peg='Tratar toda irregularidade como nulidade absoluta automática.',
  kw=['quebra da cadeia', 'confiabilidade'])

# ======================= CPP-7.6 · Meios de prova =======================
P = 'DBA26-CPP-7.6'
I(P, 1, 'Perito oficial',
  'O exame de corpo de delito e as demais perícias serão realizados por dois peritos oficiais, portadores de diploma de curso superior.', 'E',
  'Art. 159, caput: basta **um perito oficial**. Dois são exigidos só na falta de oficial (§ 1º).',
  lei=[(CPP + '159', 'O exame de corpo de delito e outras perícias serão realizados por perito oficial', 'diploma de curso superior', 'CPP, art. 159, caput')],
  peg='Exigir dois peritos oficiais (regra anterior a 2008).',
  kw=['perito oficial', 'um perito'])
I(P, 1, 'Peritos não oficiais',
  'Na falta de perito oficial, o exame será realizado por uma pessoa idônea, portadora de diploma de curso superior.', 'E',
  'Art. 159, § 1º: **duas** pessoas idôneas, com diploma superior, preferencialmente na área específica.',
  lei=[(CPP + '159', 'Na falta de perito oficial, o exame será realizado por 2 (duas) pessoas idôneas', None, 'CPP, art. 159, § 1º')],
  peg='Trocar "duas" por "uma".',
  kw=['peritos não oficiais', 'duas pessoas'])
I(P, 1, 'Assistente técnico',
  'São facultadas ao MP, ao assistente de acusação, ao ofendido, ao querelante e ao acusado a formulação de quesitos e a indicação de assistente técnico.', 'C',
  'Art. 159, § 3º. O assistente técnico atua **após** a conclusão dos exames e a elaboração do laudo (§ 4º).',
  lei=[(CPP + '159', 'Serão facultadas ao Ministério Público, ao assistente de acusação, ao ofendido, ao querelante e ao acusado', 'indicação de assistente técnico', 'CPP, art. 159, § 3º')],
  kw=['assistente técnico', 'quesitos'])
I(P, 1, 'Interrogatório com defensor',
  'O acusado que comparecer perante a autoridade judiciária será qualificado e interrogado na presença de seu defensor, constituído ou nomeado.', 'C',
  'Art. 185, caput: presença **obrigatória** do defensor, com direito a entrevista prévia e reservada (§ 5º).',
  lei=[(CPP + '185', 'será qualificado e interrogado na presença de seu defensor, constituído ou nomeado', None, 'CPP, art. 185, caput')],
  kw=['interrogatório', 'presença de seu defensor'])
I(P, 1, 'Videoconferência no interrogatório',
  'O interrogatório do réu preso por videoconferência é a regra, dispensada qualquer fundamentação.', 'E',
  'Art. 185, § 2º: **excepcionalmente**, por **decisão fundamentada**, para as finalidades listadas (risco à segurança, dificuldade de comparecimento, influência na vítima, gravíssima questão de ordem pública).',
  lei=[(CPP + '185', 'Excepcionalmente, o juiz, por decisão fundamentada', 'sistema de videoconferência', 'CPP, art. 185, § 2º')],
  peg='Fazer da exceção a regra.',
  kw=['videoconferência', 'excepcionalmente'])
I(P, 1, 'Novo interrogatório',
  'A todo tempo o juiz poderá proceder a novo interrogatório de ofício ou a pedido fundamentado de qualquer das partes.', 'C',
  'Art. 196 do CPP.',
  lei=[(CPP + '196', 'A todo tempo o juiz poderá proceder a novo interrogatório', 'qualquer das partes', 'CPP, art. 196')],
  kw=['novo interrogatório', 'a todo tempo'])
I(P, 1, 'Dever de depor e parentes',
  'O cônjuge, o ascendente, o descendente e o irmão do acusado estão proibidos de depor.', 'E',
  'Art. 206: eles **podem recusar-se** a depor (faculdade), salvo se não houver outro meio de obter a prova. **Proibidos** são os que devem guardar **segredo profissional** (art. 207).',
  lei=[(CPP + '206', 'A testemunha não poderá eximir-se da obrigação de depor', 'circunstâncias', 'CPP, art. 206')],
  peg='Trocar "podem recusar-se" por "proibidos".',
  kw=['podem recusar-se', 'parentes'])
I(P, 1, 'Sigilo profissional',
  'São proibidas de depor as pessoas que, em razão de função, ministério, ofício ou profissão, devam guardar segredo, salvo se, desobrigadas pela parte interessada, quiserem dar o seu testemunho.', 'C',
  'Art. 207: mesmo desobrigada, a pessoa **pode** depor, não é obrigada.',
  lei=[(CPP + '207', 'São proibidas de depor as pessoas que, em razão de função, ministério, ofício ou profissão, devam guardar segredo', 'quiserem dar o seu testemunho', 'CPP, art. 207')],
  kw=['segredo profissional', 'proibidas de depor'])
I(P, 1, 'Compromisso',
  'Os menores de 18 anos não prestam o compromisso de dizer a verdade.', 'E',
  'Art. 208: não prestam compromisso os doentes e deficientes mentais, os **menores de 14 anos** e os parentes do art. 206 (informantes).',
  lei=[(CPP + '208', 'Não se deferirá o compromisso a que alude o art. 203 aos doentes e deficientes mentais e aos menores de 14 (quatorze) anos', None, 'CPP, art. 208')],
  peg='Trocar 14 por 18 anos.',
  kw=['menores de 14 anos', 'compromisso'])
I(P, 1, 'Depoimento oral',
  'O depoimento será prestado oralmente, não sendo permitido à testemunha trazê-lo por escrito.', 'C',
  'Art. 204: **oralidade**; admitem-se breves consultas a apontamentos (par. ún.).',
  lei=[(CPP + '204', 'O depoimento será prestado oralmente, não sendo permitido à testemunha trazê-lo por escrito', None, 'CPP, art. 204, caput')],
  kw=['oralidade', 'depoimento'])
I(P, 1, 'Retirada do réu',
  'Se a presença do réu puder causar humilhação, temor ou sério constrangimento à testemunha, o juiz determinará imediatamente sua retirada da sala, sem outras providências.', 'E',
  'Art. 217: primeiro, **videoconferência**; só na impossibilidade dela, a **retirada** do réu, com a presença do defensor.',
  lei=[(CPP + '217', 'fará a inquirição por videoconferência e, somente na impossibilidade dessa forma, determinará a retirada do réu', None, 'CPP, art. 217, caput')],
  peg='Pular a videoconferência.',
  kw=['videoconferência', 'retirada do réu'])
I(P, 1, 'Acareação',
  'A acareação será admitida entre acusados, entre acusado e testemunha, entre testemunhas, entre acusado ou testemunha e a pessoa ofendida, e entre as pessoas ofendidas, sempre que divergirem sobre fatos ou circunstâncias relevantes.', 'C',
  'Art. 229 do CPP.',
  lei=[(CPP + '229', 'A acareação será admitida entre acusados', 'fatos ou circunstâncias relevantes', 'CPP, art. 229, caput')],
  kw=['acareação', 'divergirem'])
# --- CPP-7.6 · Rodada 2
I(P, 2, 'Reconhecimento — descrição prévia',
  'No reconhecimento de pessoa, quem fará o reconhecimento será primeiro convidado a descrever a pessoa que deva ser reconhecida.', 'C',
  'Art. 226, I. Do ato lavra-se **auto pormenorizado**, subscrito pela autoridade, pelo reconhecedor e por duas testemunhas presenciais (IV).',
  lei=[(CPP + '226', 'a pessoa que tiver de fazer o reconhecimento será convidada a descrever a pessoa que deva ser reconhecida', None, 'CPP, art. 226, I')],
  kw=['reconhecimento', 'descrever'])
I(P, 2, 'Reconhecimento em juízo e intimidação',
  'A providência para que o reconhecido não veja o reconhecedor, em caso de receio de intimidação, aplica-se também na fase de instrução criminal e no plenário do júri.', 'E',
  'Art. 226, par. ún.: o inciso III **não se aplica** na instrução criminal nem em plenário (a doutrina critica; o art. 217 permite videoconferência).',
  lei=[(CPP + '226', 'não terá aplicação na fase da instrução criminal ou em plenário de julgamento', None, 'CPP, art. 226, par. ún.')],
  peg='Estender o inciso III à fase judicial.',
  kw=['reconhecimento', 'fase judicial'])
I(P, 2, 'Reconhecimento fotográfico',
  'Para o STJ, o reconhecimento fotográfico feito na fase policial pode servir como prova única e isolada da autoria, se a vítima tiver certeza.', 'E',
  'STJ, **HC 598.886**: o reconhecimento por foto é etapa antecedente e **não serve como prova isolada**; precisa de corroboração por outras provas idôneas.',
  juris=[J['HC598886']],
  peg='Validar condenação só por reconhecimento fotográfico.',
  kw=['reconhecimento fotográfico', 'prova isolada'])
I(P, 2, 'Testemunha faltosa',
  'Se a testemunha, regularmente intimada, deixar de comparecer sem motivo justificado, o juiz poderá requisitar à autoridade policial a sua apresentação ou determinar que seja conduzida por oficial de justiça.', 'C',
  'Art. 218: **condução coercitiva da testemunha** (permanece válida; o STF afastou a do investigado para interrogatório).',
  lei=[(CPP + '218', 'Se, regularmente intimada, a testemunha deixar de comparecer sem motivo justificado', 'auxílio da força pública', 'CPP, art. 218')],
  kw=['condução coercitiva da testemunha', 'oficial de justiça'])
I(P, 2, 'Documento',
  'Consideram-se documentos quaisquer escritos, instrumentos ou papéis, públicos ou particulares.', 'C',
  'Art. 232. A doutrina amplia o conceito a qualquer suporte (fotos, vídeos, arquivos digitais).',
  lei=[(CPP + '232', 'Consideram-se documentos quaisquer escritos, instrumentos ou papéis, públicos ou particulares', None, 'CPP, art. 232, caput')],
  kw=['documentos', 'conceito'])
I(P, 2, 'Confissão e silêncio',
  'A ausência de advertência sobre o direito ao silêncio no interrogatório policial gera sempre nulidade absoluta, independentemente de prejuízo.', 'E',
  'Prevalece na jurisprudência que a falta do aviso é nulidade **relativa**, que exige demonstração de **prejuízo** (art. 563).',
  lei=[(CPP + '563', 'Nenhum ato será declarado nulo, se da nulidade não resultar prejuízo', None, 'CPP, art. 563')],
  peg='Tratar como absoluta nulidade que se reputa relativa.',
  kw=['aviso de Miranda', 'nulidade relativa'])
I(P, 2, 'Colaboração premiada — natureza',
  'O acordo de colaboração premiada é negócio jurídico processual e meio de obtenção de prova, que pressupõe utilidade e interesse públicos.', 'C',
  'Lei 12.850/2013, **art. 3º-A** (Lei 13.964/2019).',
  lei=[('L12850:3-A', 'O acordo de colaboração premiada é negócio jurídico processual e meio de obtenção de prova', 'utilidade e interesse públicos', 'Lei 12.850/2013, art. 3º-A')],
  kw=['negócio jurídico processual', 'meio de obtenção de prova'])
I(P, 2, 'Juiz e colaboração',
  'O juiz participa das negociações do acordo de colaboração premiada para garantir sua legalidade.', 'E',
  'Lei 12.850/2013, art. 4º, § 6º: o juiz **não participará** das negociações (entre delegado, investigado e defensor, com manifestação do MP, ou entre MP e investigado e defensor).',
  lei=[('L12850:4', 'O juiz não participará das negociações realizadas entre as partes', None, 'Lei 12.850/2013, art. 4º, § 6º')],
  peg='Pôr o juiz na mesa de negociação.',
  kw=['juiz não participará', 'negociações'])

# ======================= CPP-7.7 · Busca e apreensão =======================
P = 'DBA26-CPP-7.7'
I(P, 1, 'Espécies de busca',
  'A busca será domiciliar ou pessoal, e a domiciliar se faz quando fundadas razões a autorizarem.', 'C',
  'Art. 240, caput e § 1º: domiciliar exige **fundadas razões**; pessoal exige **fundada suspeita** (§ 2º).',
  lei=[(CPP + '240', 'A busca será domiciliar ou pessoal', None, 'CPP, art. 240, caput')],
  kw=['busca domiciliar', 'fundadas razões'])
I(P, 1, 'Busca pessoal sem mandado',
  'A busca pessoal independerá de mandado no caso de prisão, quando houver fundada suspeita de que a pessoa esteja na posse de arma proibida ou de objetos ou papéis que constituam corpo de delito, ou quando determinada no curso de busca domiciliar.', 'C',
  'Art. 244 do CPP.',
  lei=[(CPP + '244', 'A busca pessoal independerá de mandado', 'no curso de busca domiciliar', 'CPP, art. 244')],
  kw=['busca pessoal', 'fundada suspeita'])
I(P, 1, 'Atitude suspeita',
  'Para o STJ, a percepção policial de "atitude suspeita" do abordado, sem descrição de elementos objetivos, basta para a busca pessoal sem mandado.', 'E',
  'STJ, **RHC 158.580**: exige-se **fundada suspeita** com **elementos objetivos**; o encontro posterior de droga não convalida a revista.',
  juris=[J['RHC158580']],
  peg='Validar revista por "atitude suspeita" genérica.',
  kw=['atitude suspeita', 'elementos objetivos'])
I(P, 1, 'Horário da busca domiciliar',
  'As buscas domiciliares serão executadas de dia, salvo se o morador consentir que se realizem à noite.', 'C',
  'Art. 245, caput, e CF, art. 5º, XI ("durante o dia, por determinação judicial").',
  lei=[(CPP + '245', 'As buscas domiciliares serão executadas de dia, salvo se o morador consentir que se realizem à noite', None, 'CPP, art. 245, caput')],
  kw=['de dia', 'consentimento do morador'])
I(P, 1, 'Abuso de autoridade e horário',
  'Comete crime de abuso de autoridade quem cumpre mandado de busca e apreensão domiciliar após as 21 horas ou antes das 5 horas.', 'C',
  'Lei 13.869/2019, art. 22, § 1º, III: **referência objetiva de horário** para o "dia".',
  lei=[('L13869:22', 'cumpre mandado de busca e apreensão domiciliar após as 21h (vinte e uma horas) ou antes das 5h (cinco horas)', None, 'Lei 13.869/2019, art. 22, § 1º, III')],
  kw=['21 horas', '5 horas'])
I(P, 1, 'Mandado — requisitos',
  'O mandado de busca deverá indicar, o mais precisamente possível, a casa em que será realizada a diligência e o nome do proprietário ou morador, além de mencionar o motivo e os fins da diligência.', 'C',
  'Art. 243, I e II: vedado o **mandado genérico** (fishing expedition).',
  lei=[(CPP + '243', 'indicar, o mais precisamente possível, a casa em que será realizada a diligência', None, 'CPP, art. 243, I')],
  kw=['mandado de busca', 'mandado genérico'])
I(P, 1, 'Documento em poder do defensor',
  'É permitida a apreensão de qualquer documento em poder do defensor do acusado, desde que haja mandado judicial.', 'E',
  'Art. 243, § 2º: **não** será permitida, **salvo** quando constituir elemento do **corpo de delito**.',
  lei=[(CPP + '243', 'Não será permitida a apreensão de documento em poder do defensor do acusado', 'elemento do corpo de delito', 'CPP, art. 243, § 2º')],
  peg='Ignorar a proteção ao defensor.',
  kw=['defensor', 'corpo de delito'])
I(P, 1, 'Busca em mulher',
  'A busca em mulher será feita por outra mulher, em qualquer circunstância, ainda que isso importe retardamento ou prejuízo da diligência.', 'E',
  'Art. 249: por outra mulher, **se não importar retardamento ou prejuízo** da diligência.',
  lei=[(CPP + '249', 'A busca em mulher será feita por outra mulher, se não importar retardamento ou prejuízo da diligência', None, 'CPP, art. 249')],
  peg='Retirar a ressalva do retardamento.',
  kw=['busca em mulher', 'retardamento'])
I(P, 1, 'Desobediência do morador',
  'Em caso de desobediência do morador, durante o cumprimento de mandado de busca domiciliar, será arrombada a porta e forçada a entrada.', 'C',
  'Art. 245, § 2º.',
  lei=[(CPP + '245', 'Em caso de desobediência, será arrombada a porta e forçada a entrada', None, 'CPP, art. 245, § 2º')],
  kw=['desobediência', 'arrombada a porta'])
# --- CPP-7.7 · Rodada 2
I(P, 2, 'Moradores ausentes',
  'Quando ausentes os moradores, a busca domiciliar não pode ser realizada.', 'E',
  'Art. 245, § 4º: pode-se arrombar e forçar a entrada, intimando-se **qualquer vizinho**, se houver e estiver presente, a assistir à diligência.',
  lei=[(CPP + '245', 'quando ausentes os moradores, devendo, neste caso, ser intimado a assistir à diligência qualquer vizinho', None, 'CPP, art. 245, § 4º')],
  peg='Impedir a busca na ausência dos moradores.',
  kw=['moradores ausentes', 'vizinho'])
I(P, 2, 'Auto circunstanciado',
  'Finda a diligência de busca domiciliar, o auto circunstanciado é dispensado se nada for apreendido.', 'E',
  'Art. 245, § 7º: findada a diligência, lavra-se **auto circunstanciado**, assinado com **duas testemunhas presenciais**, sem ressalva.',
  lei=[(CPP + '245', 'Finda a diligência, os executores lavrarão auto circunstanciado, assinando-o com duas testemunhas presenciais', None, 'CPP, art. 245, § 7º')],
  peg='Dispensar o auto quando a busca é negativa.',
  kw=['auto circunstanciado', 'duas testemunhas'])
I(P, 2, 'Prisão em casa à noite',
  'Para cumprir mandado de prisão durante a noite, verificado que o réu está em casa e recusada a entrega pelo morador, o executor pode arrombar as portas imediatamente.', 'E',
  'Art. 293: à noite, o executor **guarda todas as saídas**, tornando a casa incomunicável, e **só ao amanhecer** arromba as portas e efetua a prisão.',
  lei=[(CPP + '293', 'sendo noite, o executor, depois da intimação ao morador, se não for atendido, fará guardar todas as saídas', 'efetuará a prisão', 'CPP, art. 293, caput')],
  peg='Autorizar arrombamento noturno com mandado.',
  kw=['noite', 'guardar todas as saídas'])
I(P, 2, 'Busca pessoal e fuga',
  'Para o STJ, a fuga repentina do indivíduo ao avistar a guarnição policial pode configurar fundada suspeita apta a justificar a busca pessoal, cabendo ao Estado demonstrar as circunstâncias.', 'C',
  'Na linha da **fundada suspeita objetiva** (art. 244; RHC 158.580), a Terceira Seção do STJ admitiu a fuga repentina como elemento concreto, com escrutínio do ônus estatal.',
  lei=[(CPP + '244', 'quando houver fundada suspeita de que a pessoa esteja na posse de arma proibida', None, 'CPP, art. 244')],
  juris=[J['HC877943']],
  kw=['fuga repentina', 'fundada suspeita'])
I(P, 2, 'Mandado e autoridade policial',
  'A autoridade policial pode realizar pessoalmente busca domiciliar sem mandado judicial, fora das hipóteses de flagrante, como sugere a letra do art. 241 do CPP.', 'E',
  'Após a CF (art. 5º, XI), a busca domiciliar sem consentimento e sem flagrante exige **determinação judicial**; o art. 241 não foi recepcionado nesse ponto.',
  lei=[(CF + '5', 'a casa é asilo inviolável do indivíduo', 'por determinação judicial', 'CF, art. 5º, XI')],
  peg='Aplicar a letra do art. 241 contra a CF.',
  kw=['reserva de jurisdição', 'art. 241'])
I(P, 2, 'Algemas',
  'O uso de algemas é lícito em casos de resistência, de fundado receio de fuga ou de perigo à integridade física própria ou alheia, justificada a excepcionalidade por escrito.', 'C',
  '**SV 11**. E o art. 292, par. ún., do CPP veda algemas em mulheres durante o trabalho de parto e o puerpério imediato.',
  lei=[(CPP + '292', 'É vedado o uso de algemas em mulheres grávidas durante os atos médico-hospitalares preparatórios para a realização do parto', None, 'CPP, art. 292, par. ún.')],
  juris=[J['SV11']],
  kw=['SV 11', 'algemas'])
