/* Peças complementares do Treino de Discursiva — acrescentadas em 03/11/2026 (D-013).
   Tipos de peça que faltavam, levantados na conferência de 03/11/2026. Texto autoral, conferido na lei federal;
   nada do material de terceiro usado na conferência foi copiado (D-002). Carrega depois de conteudo.js. */
PECAS.push(
  /* ---------------------------------------------------------------- 10 */
  {
    id: 'apf', titulo: 'Despacho de conclusão do flagrante + representação pela conversão em preventiva', freq: 'FGV PC-RN e PC-SC; CEBRASPE PC-PE 2024 cobrou a conversão',
    tipo: 'inquerito',
    cabecalho: 'POLÍCIA CIVIL DO ESTADO DA BAHIA\nDelegacia Territorial de …\nAuto de Prisão em Flagrante nº …/…\nDESPACHO',
    pre_orient: 'Quem decide, com que atribuição e com que fundamento (CF, art. 5º, LXI a LXIV; CPP, arts. 301 a 306), sobre qual auto e qual preso.',
    pre_check: ['Citei a CF (art. 144, § 4º, e art. 5º, LXI a LXIV)', 'Citei os arts. 301 a 306 do CPP', 'Usei o verbo de quem decide (DECIDE / DETERMINA)'],
    enunciado: 'Em 25/10/2026, em Camaçari/BA, Diego, empunhando um revólver, tomou a motocicleta de Lucas em um semáforo. Policiais militares que estavam na esquina saíram em perseguição ininterrupta e o detiveram cerca de 20 minutos depois, ainda com a motocicleta e o revólver municiado. Na Delegacia, Lucas o reconheceu formalmente. A folha de antecedentes mostra duas condenações definitivas anteriores por roubo. Diego, informado de seus direitos, ficou em silêncio e não indicou advogado. Na condição de Delegado de Polícia Civil, elabore a peça que conclui o procedimento.',
    mnemonico: 'Fechou o auto? "LIFE-PC": Legalidade do flagrante (art. 302) · Indiciamento (Lei 12.830, art. 2º, § 6º) · Fiança (art. 322: só pena máxima ≤ 4 anos) · Expedientes (nota de culpa em 24 h; comunicação ao juiz, MP e família; cópia à Defensoria em 24 h) · Perícias (corpo de delito, arma) · Conversão (representa pela preventiva: arts. 310, II, 312 e 313).',
    preambulo: 'DESPACHO\nO DELEGADO DE POLÍCIA CIVIL que este subscreve, no exercício das atribuições do art. 144, § 4º, da Constituição Federal e do art. 2º da Lei nº 12.830/2013, com fundamento no art. 5º, LXI a LXIV, da Constituição Federal e nos arts. 301 a 306 do Código de Processo Penal, encerrada a lavratura do auto de prisão em flagrante de DIEGO (qualificação nos autos), DECIDE nos termos a seguir.',
    pre_arts: ['CF, art. 144, § 4º, e art. 5º, LXI a LXIV', 'Lei 12.830/13, art. 2º', 'CPP, arts. 301 a 306'],
    fatos: 'Em 25/10/2026, nesta cidade, o conduzido teria subtraído a motocicleta da vítima Lucas mediante grave ameaça exercida com revólver. Policiais militares o perseguiram sem interrupção e o detiveram cerca de 20 minutos depois, na posse da motocicleta e da arma municiada. A vítima o reconheceu formalmente nesta Delegacia.',
    direito: [
      { t: 'Legalidade do flagrante (art. 302)', orient: 'Diga QUAL espécie de flagrante e por quê. Perseguido logo após, sem interrupção = flagrante impróprio (art. 302, III; art. 290, § 1º). Encontrado logo depois com a coisa ou a arma também se encaixa no inciso IV. Ratifique a prisão.',
        arts: ['CPP, art. 302, III (perseguido logo após) e IV (encontrado logo depois com instrumentos)', 'CPP, art. 290, § 1º (o que é perseguição)', 'CPP, art. 304 (oitiva do condutor, testemunhas e interrogatório)'],
        check: ['Nomeei a espécie de flagrante com o inciso do art. 302', 'Usei a perseguição ininterrupta (art. 290, § 1º)', 'Disse que o auto seguiu o art. 304 e ratifiquei a prisão'],
        modelo: 'DA LEGALIDADE DA PRISÃO\nO conduzido foi perseguido logo após o fato, sem interrupção, e detido na posse da coisa subtraída e da arma usada, situação de flagrante impróprio (art. 302, III, do CPP, c/c art. 290, § 1º), também enquadrável no inciso IV. Ouvidos o condutor, as testemunhas e a vítima, e interrogado o conduzido após ciência de seus direitos (art. 304), RATIFICO a voz de prisão em flagrante.' },
      { t: 'Tipificação e indiciamento', orient: 'Tipifique com precisão e INDICIE por ato fundamentado (é privativo do delegado). Roubo com arma de fogo = art. 157, § 2º-A, I.',
        arts: ['CP, art. 157, § 2º-A, I (emprego de arma de fogo)', 'Lei 12.830/13, art. 2º, § 6º (indiciamento fundamentado)'],
        check: ['Tipifiquei com o parágrafo e o inciso certos', 'Indiciei por ato fundamentado (autoria, materialidade, circunstâncias)'],
        modelo: 'DO INDICIAMENTO\nA materialidade está demonstrada pela apreensão da motocicleta e da arma, e a autoria, pela prisão em perseguição e pelo reconhecimento formal da vítima. Com base nessa análise técnico-jurídica (art. 2º, § 6º, da Lei nº 12.830/2013), INDICIO DIEGO como incurso no art. 157, § 2º-A, I, do Código Penal.' },
      { t: 'Fiança', orient: 'O delegado só arbitra fiança em infração com pena máxima de até 4 anos (art. 322). Roubo majorado passa disso: a fiança, se cabível, é com o juiz.',
        arts: ['CPP, art. 322 (fiança pela autoridade policial: pena máxima não superior a 4 anos)', 'CPP, art. 324, IV (não cabe fiança quando presentes os motivos da preventiva)'],
        check: ['Disse por que o delegado não arbitra fiança (art. 322)', 'Mencionei o art. 324, IV'],
        modelo: 'DA FIANÇA\nDeixo de arbitrar fiança: a pena máxima do crime supera 4 anos, o que afasta a atribuição da autoridade policial (art. 322 do CPP), além de estarem presentes os motivos da preventiva (art. 324, IV).' },
      { t: 'Providências (formalidades)', orient: 'Liste, numeradas, as providências que o examinador procura: nota de culpa, comunicações, Defensoria, exames, restituição à vítima, custódia.',
        arts: ['CF, art. 5º, LXII e LXIII', 'CPP, art. 306, caput e §§ 1º e 2º', 'CPP, art. 310 (audiência de custódia em 24 h)', 'CPP, art. 6º, VII e X', 'CPP, art. 120 (restituição)'],
        check: ['Nota de culpa em 24 h (art. 306, § 2º)', 'Comunicação imediata ao juiz, ao MP e à família (art. 306)', 'Cópia à Defensoria em 24 h (sem advogado — art. 306, § 1º)', 'Corpo de delito e perícia na arma', 'Restituição da moto à vítima (art. 120)', 'Apresentação à audiência de custódia (art. 310)'],
        modelo: 'DAS PROVIDÊNCIAS\nDetermino:\n1. a entrega da nota de culpa ao preso, em até 24 horas (art. 306, § 2º);\n2. a comunicação imediata da prisão ao juiz competente, ao Ministério Público e à família do preso ou pessoa por ele indicada (art. 306, caput; CF, art. 5º, LXII);\n3. a remessa do auto ao juiz em 24 horas e, não tendo o preso advogado, cópia integral à Defensoria Pública (art. 306, § 1º);\n4. o exame de corpo de delito no preso e a perícia na arma e nas munições;\n5. a restituição da motocicleta à vítima, mediante termo, por não interessar mais ao processo (art. 120);\n6. a juntada da folha de antecedentes e a coleta de informações sobre filhos (art. 6º, X);\n7. a apresentação do preso à audiência de custódia (art. 310).' },
      { t: 'Representação pela conversão em preventiva', orient: 'No mesmo despacho, REPRESENTE ao juiz pela conversão (art. 310, II): fumus, periculum concreto, cabimento (art. 313, I e II) e insuficiência das cautelares.',
        arts: ['CPP, art. 310, II (conversão do flagrante em preventiva)', 'CPP, arts. 312 e 313, I e II', 'CPP, art. 282, § 6º'],
        check: ['Pedi a CONVERSÃO (art. 310, II)', 'Citei o cabimento (art. 313, I e II)', 'Mostrei o perigo concreto (reiteração em roubos)', 'Afastei as cautelares do art. 319 (art. 282, § 6º)'],
        modelo: 'DA REPRESENTAÇÃO PELA CONVERSÃO\nREPRESENTO ao Juízo pela conversão da prisão em flagrante em PRISÃO PREVENTIVA (art. 310, II, do CPP). Há prova da existência do crime e indício suficiente de autoria (art. 312); o crime é doloso, com pena máxima superior a 4 anos, e o conduzido é reincidente em crime doloso (art. 313, I e II); a garantia da ordem pública está concretamente ameaçada pela reiteração em roubos com arma de fogo, fato contemporâneo (art. 312, § 2º), e as cautelares do art. 319 são insuficientes (art. 282, § 6º).' },
    ],
    pedidos: '', pedidos_check: [],
    cards: [
      { p: 'As espécies de flagrante do art. 302', r: 'I e II — próprio (está cometendo / acaba de cometer); III — impróprio (perseguido logo após); IV — presumido (encontrado logo depois com instrumentos, armas ou objetos).', a: 'CPP, art. 302', ce: ['É flagrante presumido o do agente perseguido logo após a infração, em situação que faça presumir ser o autor.', 'E', 'Perseguido logo após = flagrante IMPRÓPRIO (inciso III). Presumido é o encontrado logo depois com objetos (inciso IV).'] },
      { p: 'Prazo da nota de culpa', r: 'Em até 24 horas após a prisão, assinada pela autoridade, com o motivo, o nome do condutor e das testemunhas.', a: 'CPP, art. 306, § 2º', ce: ['A nota de culpa deve ser entregue ao preso em até 24 horas.', 'C', 'Art. 306, § 2º.'] },
      { p: 'Preso sem advogado: o que a lei manda fazer com o auto?', r: 'Em até 24 horas, remeter o auto ao juiz e cópia integral à Defensoria Pública.', a: 'CPP, art. 306, § 1º', ce: ['Se o preso não indicar advogado, cópia integral do auto vai à Defensoria Pública em até 48 horas.', 'E', 'O prazo é de 24 horas (art. 306, § 1º).'] },
      { p: 'Até que pena máxima o delegado pode conceder fiança?', r: 'Infração com pena privativa de liberdade máxima não superior a 4 anos; acima disso, só o juiz, em 48 horas.', a: 'CPP, art. 322', ce: ['A autoridade policial pode conceder fiança em crime com pena máxima de até 4 anos.', 'C', 'Art. 322, caput.'] },
      { p: 'Prazo da audiência de custódia e o que o juiz pode decidir', r: 'Até 24 horas após a prisão; o juiz relaxa a prisão ilegal, converte em preventiva ou concede liberdade provisória.', a: 'CPP, art. 310', ce: ['Na audiência de custódia, o juiz pode converter o flagrante em preventiva de ofício.', 'E', 'STF e STJ exigem requerimento do MP ou representação policial: daí a representação no despacho.'] },
      { p: 'Uso de algemas', r: 'Só em caso de resistência, fundado receio de fuga ou perigo à integridade própria ou alheia, justificado por escrito.', a: 'STF, Súmula Vinculante 11', ce: ['O uso de algemas é livre, a critério do condutor, sem necessidade de justificativa.', 'E', 'Exige justificativa escrita (Súmula Vinculante 11).'] },
    ],
  },
  /* ---------------------------------------------------------------- 11 */
  {
    id: 'cautelar-diversa', dirfund: { bem: 'liberdade de locomoção e o livre exercício da função', inc: 'XIII e XV' }, titulo: 'Representação por cautelares diversas da prisão (suspensão da função pública)', freq: 'CEBRASPE PC-PB e PC-RO aceitaram a suspensão da função (art. 319, VI)',
    enunciado: 'No IP nº 140/2026 (Lauro de Freitas/BA), apura-se que Henrique, fiscal de obras do Município, solicitou R$ 5.000,00 a dois empresários para não embargar suas obras, conforme depoimentos e mensagens entregues pelas vítimas. Henrique é primário, tem residência fixa e continua fiscalizando obras na cidade; os empresários dizem temer represálias nas próximas vistorias. Elabore a peça cabível, considerando que a prisão preventiva seria desproporcional.',
    mnemonico: 'Cautelar diversa = "NA-SUB": Necessidade e Adequação (art. 282, I e II) + SUBsidiariedade da prisão (art. 282, § 6º). Servidor que usa o cargo para o crime: art. 319, VI ("justo receio de sua utilização para a prática de infrações penais"). Pode cumular (art. 282, § 1º). Descumpriu? Pode virar preventiva (art. 282, § 4º).',
    preambulo: 'O DELEGADO DE POLÍCIA CIVIL que esta subscreve, no exercício das atribuições do art. 144, § 4º, da Constituição Federal e do art. 2º da Lei nº 12.830/2013, com fundamento nos arts. 282 e 319, III e VI, do Código de Processo Penal, vem REPRESENTAR pela imposição das MEDIDAS CAUTELARES DIVERSAS DA PRISÃO de suspensão do exercício da função pública e de proibição de contato com as vítimas, em desfavor de HENRIQUE (qualificação nos autos).',
    pre_arts: ['CF, art. 144, § 4º', 'Lei 12.830/13, art. 2º', 'CPP, arts. 282 e 319, III e VI'],
    fatos: 'No IP nº 140/2026, apura-se que o representado, fiscal de obras do Município, solicitou R$ 5.000,00 a dois empresários para não embargar suas obras, conforme depoimentos e mensagens entregues pelas vítimas. Ele segue no exercício da fiscalização, e as vítimas relatam temor de represálias.',
    direito: [
      { t: 'Fumus comissi delicti e tipificação', orient: 'Prova do crime e indício de autoria, com a tipificação. Solicitar vantagem indevida em razão da função = corrupção passiva (art. 317), crime formal que se consuma com a solicitação.',
        arts: ['CP, art. 317 (corrupção passiva — "solicitar")', 'CPP, art. 282, I'],
        check: ['Tipifiquei como corrupção passiva (art. 317)', 'Disse que o crime é formal (consuma com a solicitação)', 'Usei os depoimentos e as mensagens'],
        modelo: 'DO FUMUS COMISSI DELICTI\nOs depoimentos das vítimas e as mensagens por elas entregues provam a solicitação de vantagem indevida em razão da função, o que configura, em tese, corrupção passiva (art. 317 do CP), crime formal que se consuma com a simples solicitação, ainda que o valor não seja pago.' },
      { t: 'Periculum e a medida do art. 319, VI', orient: 'O perigo está no USO DO CARGO para novos crimes e para pressionar as vítimas: é exatamente o requisito do art. 319, VI. Some a proibição de contato (art. 319, III).',
        arts: ['CPP, art. 319, VI (suspensão da função: justo receio de sua utilização para infrações penais)', 'CPP, art. 319, III (proibição de contato com pessoa determinada)', 'CPP, art. 282, § 1º (cumulação)'],
        check: ['Usei a expressão "justo receio de sua utilização para a prática de infrações penais"', 'Pedi também a proibição de contato (art. 319, III)', 'Citei a cumulação (art. 282, § 1º)'],
        modelo: 'DO PERICULUM E DAS MEDIDAS ADEQUADAS\nO representado segue fiscalizando obras, e as vítimas temem represálias nas próximas vistorias: há justo receio de que a função seja usada para a prática de novas infrações penais (art. 319, VI, do CPP). Por isso, representa-se pela suspensão do exercício da função pública, cumulada (art. 282, § 1º) com a proibição de manter contato com as vítimas (art. 319, III).' },
      { t: 'Proporcionalidade: por que não a prisão', orient: 'Mostre que você PENSOU na preventiva e a afastou: primário, residência fixa, sem violência. A cautelar diversa é necessária e adequada (art. 282, I e II), e o descumprimento autoriza a prisão (art. 282, § 4º).',
        arts: ['CPP, art. 282, I e II (necessidade e adequação)', 'CPP, art. 282, § 6º (prisão só se outra cautelar não bastar)', 'CPP, art. 282, § 4º (descumprimento)', 'CPP, art. 282, § 3º (urgência dispensa o contraditório prévio)'],
        check: ['Afastei a preventiva com motivo concreto', 'Citei o art. 282, I e II', 'Lembrei a consequência do descumprimento (art. 282, § 4º)', 'Justifiquei a decisão sem oitiva prévia (art. 282, § 3º)'],
        modelo: 'DA PROPORCIONALIDADE\nO representado é primário, tem residência fixa e o crime não envolveu violência, de modo que a prisão seria desproporcional (art. 282, § 6º). As medidas pedidas são necessárias para evitar novas infrações e adequadas à gravidade do fato e às condições pessoais do investigado (art. 282, I e II), ficando advertido de que o descumprimento poderá ensejar a preventiva (art. 282, § 4º). A urgência e o risco às vítimas justificam a decisão sem prévia intimação (art. 282, § 3º).' },
    ],
    pedidos: 'DOS PEDIDOS\na) a SUSPENSÃO do exercício da função pública de fiscal de obras por HENRIQUE (art. 319, VI, do CPP), com comunicação ao Município;\nb) a PROIBIÇÃO de contato com as vítimas, por qualquer meio (art. 319, III);\nc) a advertência de que o descumprimento poderá ensejar a prisão preventiva (art. 282, § 4º);\nd) a oitiva do Ministério Público;\ne) a tramitação em sigilo e com urgência.',
    pedidos_check: ['Suspensão da função (art. 319, VI), com ofício ao órgão', 'Proibição de contato (art. 319, III)', 'Advertência do art. 282, § 4º', 'Oitiva do MP, sigilo e urgência'],
    cards: [
      { p: 'Requisito específico da suspensão da função pública (art. 319, VI)', r: 'Justo receio de sua utilização para a prática de infrações penais.', a: 'CPP, art. 319, VI', ce: ['A suspensão do exercício de função pública exige justo receio de sua utilização para a prática de infrações penais.', 'C', 'Art. 319, VI.'] },
      { p: 'As cautelares diversas cabem em infração sem pena privativa de liberdade?', r: 'Não: não se aplicam à infração a que não for cominada, isolada, cumulativa ou alternativamente, pena privativa de liberdade.', a: 'CPP, art. 283, § 1º', ce: ['As medidas cautelares diversas podem ser impostas em infração punida apenas com multa.', 'E', 'Exige-se pena privativa de liberdade cominada (art. 283, § 1º).'] },
      { p: 'Descumprida a cautelar diversa, o que o juiz pode fazer?', r: 'Substituir a medida, impor outra em cumulação ou, em último caso, decretar a preventiva.', a: 'CPP, art. 282, § 4º', ce: ['O descumprimento de cautelar diversa impede a decretação da preventiva.', 'E', 'Pode levar à preventiva, em último caso (art. 282, § 4º).'] },
      { p: 'Corrupção passiva: quando se consuma na forma "solicitar"?', r: 'Com a simples solicitação: é crime formal; o recebimento é exaurimento.', a: 'CP, art. 317', ce: ['A corrupção passiva na modalidade "solicitar" só se consuma com o recebimento da vantagem.', 'E', 'É formal: consuma-se com a solicitação.'] },
      { p: 'Quem provoca a cautelar diversa na investigação?', r: 'Representação da autoridade policial ou requerimento do MP; o juiz não decreta de ofício.', a: 'CPP, art. 282, § 2º', ce: ['Na investigação, as cautelares são decretadas mediante representação da autoridade policial ou requerimento do MP.', 'C', 'Art. 282, § 2º.'] },
    ],
  },
  /* ---------------------------------------------------------------- 14 */
  {
    id: 'relatorio', titulo: 'Relatório final do inquérito policial', freq: 'Peça conclusiva: o edital admite "peça de inquérito policial"',
    tipo: 'inquerito',
    cabecalho: 'POLÍCIA CIVIL DO ESTADO DA BAHIA\nDelegacia Territorial de …\nInquérito Policial nº …/…\nRELATÓRIO FINAL\nExcelentíssimo(a) Senhor(a) Juiz(íza) de Direito',
    pre_orient: 'Quem relata, com que fundamento (CPP, art. 10, § 1º) e o que se encerra. Relatório é objetivo: descreve o que foi apurado; não acusa nem absolve.',
    pre_check: ['Citei o art. 10, § 1º, do CPP', 'Identifiquei o IP e como foi instaurado', 'Mantive tom descritivo (sem opinião de mérito)'],
    enunciado: 'O IP nº 512/2026, instaurado por portaria em Itabuna/BA, apurou que Eduardo, funcionário de uma loja, subtraiu R$ 8.000,00 do caixa em seis ocasiões ao longo de duas semanas, valendo-se da confiança do gerente. A perícia nas imagens internas confirmou as retiradas; o gerente e uma colega foram ouvidos; Eduardo, interrogado, confessou e devolveu R$ 2.000,00. Encerradas as diligências, com o investigado solto, elabore a peça cabível.',
    mnemonico: 'Relatório = "FDMAI": Fatos · Diligências · Materialidade · Autoria · Indiciamento (Lei 12.830, art. 2º, § 6º). Prazo: 10 dias preso / 30 solto (art. 10). Remete ao JUIZ (art. 10, § 1º); o delegado NÃO arquiva (art. 17).',
    preambulo: 'O DELEGADO DE POLÍCIA CIVIL que este subscreve, no exercício das atribuições do art. 144, § 4º, da Constituição Federal e do art. 2º da Lei nº 12.830/2013, com fundamento no art. 10, § 1º, do Código de Processo Penal, apresenta o RELATÓRIO FINAL do Inquérito Policial nº 512/2026, instaurado por portaria.',
    pre_arts: ['CF, art. 144, § 4º', 'Lei 12.830/13, art. 2º', 'CPP, art. 10, § 1º'],
    fatos: 'O inquérito foi instaurado para apurar subtrações de valores do caixa de estabelecimento comercial, atribuídas ao funcionário EDUARDO, que somariam R$ 8.000,00 em seis ocasiões, ao longo de duas semanas.',
    direito: [
      { t: 'Diligências, materialidade e autoria', orient: 'Diga o que foi feito e o que cada diligência provou. Separe materialidade (perícia, imagens) de autoria (testemunhas, confissão).',
        arts: ['CPP, art. 6º (diligências)', 'CPP, art. 158 (exame de corpo de delito / perícia)'],
        check: ['Listei as diligências realizadas', 'Separei materialidade de autoria', 'Usei só o que o enunciado traz'],
        modelo: 'DAS DILIGÊNCIAS\nForam ouvidos o gerente e uma funcionária da loja, realizou-se perícia nas imagens internas e o investigado foi interrogado.\nDA MATERIALIDADE\nA perícia nas imagens confirmou as seis retiradas de valores do caixa.\nDA AUTORIA\nAs testemunhas e as imagens apontam o investigado, que, interrogado, confessou as subtrações e restituiu R$ 2.000,00.' },
      { t: 'Indiciamento e tipificação', orient: 'Indicie por ato fundamentado. Abuso de confiança qualifica o furto (art. 155, § 4º, II); várias subtrações nas mesmas condições = crime continuado (art. 71). Reparação PARCIAL não gera arrependimento posterior (art. 16 exige reparação integral).',
        arts: ['Lei 12.830/13, art. 2º, § 6º', 'CP, art. 155, § 4º, II', 'CP, art. 71 (crime continuado)', 'CP, art. 16 (arrependimento posterior: reparação integral)'],
        check: ['Indiciei com fundamento (autoria, materialidade, circunstâncias)', 'Tipifiquei: art. 155, § 4º, II, c/c art. 71', 'Afastei o art. 16 (reparação só parcial)'],
        modelo: 'DO INDICIAMENTO\nPor ato fundamentado, com análise técnico-jurídica do fato (art. 2º, § 6º, da Lei nº 12.830/2013), INDICIO EDUARDO como incurso no art. 155, § 4º, II, c/c art. 71, do Código Penal. A restituição de R$ 2.000,00 foi parcial e não configura arrependimento posterior (art. 16 do CP).' },
      { t: 'Encerramento e remessa', orient: 'Encerre e registre a remessa ao juiz, com vista ao MP. Nunca peça arquivamento como decisão sua: o delegado não arquiva (art. 17).',
        arts: ['CPP, art. 10, §§ 1º e 2º', 'CPP, art. 17 (vedado ao delegado arquivar)', 'CPP, art. 23 (comunicação ao instituto de identificação)'],
        check: ['Determinei a remessa ao juiz (art. 10, § 1º)', 'Comuniquei o instituto de identificação (art. 23)', 'Não arquivei nem tratei o arquivamento como decisão minha'],
        modelo: 'DA CONCLUSÃO\nEncerradas as diligências, remetam-se os autos ao Juízo competente (art. 10, § 1º, do CPP), com vista ao Ministério Público, comunicando-se o instituto de identificação (art. 23).' },
    ],
    pedidos: '', pedidos_check: [],
    cards: [
      { p: 'O que o delegado faz ao concluir o IP?', r: 'Minucioso relatório do que foi apurado, enviando os autos ao juiz competente.', a: 'CPP, art. 10, § 1º', ce: ['Concluído o inquérito, o delegado faz minucioso relatório e envia os autos ao juiz competente.', 'C', 'Art. 10, § 1º.'] },
      { p: 'Testemunhas não ouvidas: o que o relatório pode trazer?', r: 'A indicação de testemunhas que não tiverem sido inquiridas, mencionando onde possam ser encontradas.', a: 'CPP, art. 10, § 2º', ce: ['No relatório, o delegado pode indicar testemunhas não inquiridas e onde encontrá-las.', 'C', 'Art. 10, § 2º.'] },
      { p: 'Prazos do IP na Lei de Drogas', r: '30 dias se preso; 90 dias se solto; podem ser duplicados pelo juiz, ouvido o MP.', a: 'Lei 11.343/06, art. 51', ce: ['Na Lei de Drogas, o IP com indiciado preso termina em 10 dias.', 'E', '30 dias preso e 90 solto, duplicáveis (art. 51).'] },
      { p: 'Relatório na Lei de Drogas: o que deve justificar?', r: 'As razões que levaram à classificação do delito (quantidade, natureza, local, circunstâncias, conduta, antecedentes).', a: 'Lei 11.343/06, art. 52, I', ce: ['Na Lei de Drogas, o relatório deve justificar as razões que levaram à classificação do delito.', 'C', 'Art. 52, I.'] },
      { p: 'Arrependimento posterior (art. 16 do CP)', r: 'Crime sem violência ou grave ameaça, reparação INTEGRAL do dano ou restituição da coisa até o recebimento da denúncia, por ato voluntário: redução de 1/3 a 2/3.', a: 'CP, art. 16', ce: ['A restituição parcial da coisa até o recebimento da denúncia basta para o arrependimento posterior.', 'E', 'Exige reparação integral (art. 16).'] },
    ],
  }
);

/* Representações acrescentadas em 03/11/2026 (D-014): os tipos do roteiro de peças que o edital admite
   (item 7.2.9.1: "peça cautelar (representações)"). A redação segue a estrutura do roteiro, corrigida na lei
   federal onde ele erra (inciso do art. 5º, número da lei, fundamento da LC 105, procedimento do ECA). */
PECAS.push(
  /* ---------------------------------------------------------------- 15 */
  {
    id: 'captacao', dirfund: { bem: 'intimidade, vida privada e sigilo das comunicações', inc: 'X e XII' }, titulo: 'Representação por captação ambiental (Lei 9.296, art. 8º-A)', freq: 'Meio de prova do Pacote Anticrime; serve quando a interceptação já não alcança o grupo',
    enunciado: 'No IP nº 412/2026 (Salvador/BA), apura-se o tráfico de drogas comandado por Wagner, que abastece pontos de venda em três bairros. A interceptação telefônica autorizada anteriormente perdeu a utilidade: os investigados deixaram de falar ao telefone e passaram a combinar compras e entregas dentro da caminhonete de Wagner, placa XYZ-9A87, que fica estacionada à noite na via pública em frente à casa dele. Campanas registraram as reuniões no veículo, duas vezes por semana. Elabore a peça cabível.',
    mnemonico: 'Captação ambiental = 8º-A da Lei 9.296: "SUB-4-15". SUBsidiariedade (inciso I: não há outro meio igualmente eficaz) · pena máxima acima de 4 anos (inciso II) · 15 dias, renováveis se a atividade criminal for permanente, habitual ou continuada (§ 3º). Diga ONDE e COMO instala (§ 1º): operação disfarçada ou à noite pode, EXCETO na casa (§ 2º).',
    preambulo: 'O DELEGADO DE POLÍCIA CIVIL que esta subscreve, no exercício das atribuições do art. 144, § 4º, da Constituição Federal e do art. 2º, §§ 1º e 2º, da Lei nº 12.830/2013, com fundamento no art. 5º, X e XII, da Constituição Federal e no art. 8º-A da Lei nº 9.296/1996, vem REPRESENTAR pela CAPTAÇÃO AMBIENTAL DE SINAIS ELETROMAGNÉTICOS, ÓPTICOS OU ACÚSTICOS, pelo prazo de 15 (quinze) dias, no veículo utilizado por WAGNER (qualificação nos autos), pelos fatos e fundamentos a seguir.',
    pre_arts: ['CF, art. 144, § 4º, e art. 5º, X e XII', 'Lei 12.830/13, art. 2º, §§ 1º e 2º', 'Lei 9.296/96, art. 8º-A'],
    fatos: 'No IP nº 412/2026, apura-se o tráfico de drogas comandado pelo representado, que abastece pontos de venda em três bairros desta capital. A interceptação telefônica anteriormente autorizada perdeu a utilidade, pois os investigados passaram a tratar das compras e entregas apenas pessoalmente, dentro da caminhonete placa XYZ-9A87, como registraram as campanas, duas vezes por semana.',
    direito: [
      { t: 'Fumus e pena máxima acima de 4 anos (art. 8º-A, II)', orient: 'Mostre os elementos razoáveis de autoria e tipifique: tráfico (art. 33 da Lei 11.343) tem pena de 5 a 15 anos, acima do piso de 4 anos do inciso II. Se houver associação (art. 35), diga.',
        arts: ['Lei 9.296/96, art. 8º-A, II', 'Lei 11.343/06, arts. 33 e 35'],
        check: ['Tipifiquei (tráfico, art. 33; associação, art. 35, se houver)', 'Disse que a pena máxima supera 4 anos (art. 8º-A, II)', 'Usei as campanas e a interceptação anterior como elementos de autoria'],
        modelo: 'DO FUMUS COMISSI DELICTI E DO CABIMENTO\nAs campanas e o resultado da interceptação anterior trazem elementos probatórios razoáveis de que o representado comanda o tráfico de drogas na região (art. 33 da Lei nº 11.343/2006), em associação com outros investigados (art. 35). Os crimes têm pena máxima superior a 4 anos, o que satisfaz o art. 8º-A, II, da Lei nº 9.296/1996.' },
      { t: 'Subsidiariedade: não há outro meio (art. 8º-A, I)', orient: 'É o requisito que a banca mais cobra: diga por que a prova NÃO pode ser feita por outros meios disponíveis e igualmente eficazes. Aqui: a interceptação perdeu o objeto, e a campana vê a reunião mas não ouve o conteúdo.',
        arts: ['Lei 9.296/96, art. 8º-A, I', 'CPP, art. 282, I e II'],
        check: ['Usei a expressão "outros meios disponíveis e igualmente eficazes"', 'Expliquei por que a interceptação e a campana não bastam', 'Demonstrei necessidade e adequação (art. 282, I e II)'],
        modelo: 'DA SUBSIDIARIEDADE DA MEDIDA\nA prova não pode ser feita por outros meios disponíveis e igualmente eficazes (art. 8º-A, I): a interceptação telefônica perdeu a utilidade, pois os investigados abandonaram o telefone, e as campanas registram as reuniões, mas não alcançam o seu conteúdo. A medida é, assim, necessária à investigação e adequada à gravidade dos fatos (art. 282, I e II, do CPP).' },
      { t: 'Local e forma de instalação (§§ 1º e 2º)', orient: 'O requerimento deve DESCREVER o local e a forma de instalação (§ 1º). A instalação pode ser por operação policial disfarçada ou à noite, EXCETO na casa (§ 2º; CF, art. 5º, XI). Veículo na via pública não é casa.',
        arts: ['Lei 9.296/96, art. 8º-A, §§ 1º e 2º', 'CF, art. 5º, XI'],
        check: ['Descrevi o local (o veículo, com placa) e a forma de instalação', 'Pedi a instalação à noite / disfarçada e disse que não é casa (§ 2º)'],
        modelo: 'DO LOCAL E DA FORMA DE INSTALAÇÃO\nO dispositivo será instalado pela equipe policial na caminhonete placa XYZ-9A87, no período noturno, enquanto o veículo permanece estacionado na via pública, por meio de operação policial disfarçada, o que o art. 8º-A, § 2º, admite fora da casa (art. 5º, XI, da Constituição Federal), hipótese em que não se enquadra o veículo.' },
    ],
    pedidos: 'DOS PEDIDOS\na) a autorização da CAPTAÇÃO AMBIENTAL de sinais eletromagnéticos, ópticos e acústicos na caminhonete placa XYZ-9A87, utilizada por WAGNER, pelo prazo de 15 (quinze) dias, renovável (art. 8º-A, caput e § 3º, da Lei nº 9.296/1996);\nb) a autorização para instalar o dispositivo no período noturno, por operação policial disfarçada (art. 8º-A, § 2º);\nc) a oitiva do Ministério Público;\nd) a decisão sem intimação prévia do investigado, sob pena de ineficácia da medida (art. 282, § 3º, do CPP), com autuação em apartado e sigilo (art. 8º-A, § 5º, c/c art. 8º);\ne) a tramitação com urgência.',
    pedidos_check: ['Captação pelo prazo de 15 dias, renovável (art. 8º-A, § 3º)', 'Instalação à noite / disfarçada (§ 2º)', 'Oitiva do MP', 'Sem intimação prévia (art. 282, § 3º), autos apartados, sigilo e urgência'],
    cards: [
      { p: 'Requisitos da captação ambiental (art. 8º-A da Lei 9.296)', r: 'I — a prova não puder ser feita por outros meios disponíveis e igualmente eficazes; II — elementos probatórios razoáveis de autoria e participação em infrações com pena máxima superior a 4 anos ou em infrações penais conexas.', a: 'Lei 9.296/96, art. 8º-A, I e II', ce: ['A captação ambiental cabe em qualquer crime punido com reclusão.', 'E', 'Exige pena máxima superior a 4 anos ou infração conexa (art. 8º-A, II).'] },
      { p: 'Prazo da captação ambiental', r: 'Até 15 dias, renovável por decisão judicial por iguais períodos, se comprovada a indispensabilidade e presente atividade criminal permanente, habitual ou continuada.', a: 'Lei 9.296/96, art. 8º-A, § 3º', ce: ['A captação ambiental tem prazo de 15 dias, renovável se comprovada a indispensabilidade e a atividade criminal permanente, habitual ou continuada.', 'C', 'Art. 8º-A, § 3º.'] },
      { p: 'Instalação do dispositivo: disfarçada e à noite?', r: 'Pode ser feita por operação policial disfarçada ou no período noturno, exceto na casa (CF, art. 5º, XI).', a: 'Lei 9.296/96, art. 8º-A, § 2º', ce: ['A instalação do dispositivo de captação ambiental pode ocorrer no período noturno em qualquer local, inclusive na casa, se houver ordem judicial.', 'E', 'Na casa, não (§ 2º, remetendo ao art. 5º, XI, da CF).'] },
      { p: 'Gravação feita por um dos interlocutores, sem conhecimento da polícia ou do MP', r: 'Pode ser usada em matéria de defesa, quando demonstrada a integridade da gravação.', a: 'Lei 9.296/96, art. 8º-A, § 4º', ce: ['A captação feita por um dos interlocutores sem conhecimento prévio da autoridade policial pode ser usada pela defesa, demonstrada a integridade da gravação.', 'C', 'Art. 8º-A, § 4º.'] },
      { p: 'Crime de captação ambiental sem autorização', r: 'Realizar captação ambiental de sinais eletromagnéticos, ópticos ou acústicos para investigação ou instrução criminal sem autorização judicial, quando exigida: reclusão de 2 a 4 anos e multa.', a: 'Lei 9.296/96, art. 10-A', ce: ['Realizar captação ambiental para investigação sem autorização judicial, quando exigida, é crime.', 'C', 'Art. 10-A da Lei 9.296.'] },
    ],
  },
  /* ---------------------------------------------------------------- 16 */
  {
    id: 'sigilo-bancario', dirfund: { bem: 'intimidade e vida privada (sigilo de dados)', inc: 'X e XII' }, titulo: 'Representação por quebra de sigilo bancário e fiscal', freq: 'Clássica nos crimes contra a Administração e na lavagem; LC 105/2001',
    enunciado: 'No IP nº 233/2026 (Feira de Santana/BA), apura-se que Rogério, tesoureiro da Câmara Municipal, desviou cerca de R$ 600.000,00 de contas do órgão entre janeiro e agosto de 2026. A auditoria interna identificou transferências para contas de terceiros sem contrato que as justifique, e um Relatório de Inteligência Financeira da UIF aponta depósitos fracionados em contas de Rogério e de sua companheira, Paula, no mesmo período. Ambos declaram à Receita renda incompatível com esses valores. Elabore a peça cabível.',
    mnemonico: 'Sigilo bancário = LC 105, art. 1º, § 4º (qualquer ilícito, em qualquer fase do IP ou do processo; "especialmente" a lista dos incisos). Sigilo fiscal = CTN, art. 198, § 1º, I (requisição de autoridade judiciária). Delegado NÃO quebra sozinho: reserva de jurisdição. Peça sempre PERÍODO certo e CONTAS/PESSOAS certas.',
    preambulo: 'O DELEGADO DE POLÍCIA CIVIL que esta subscreve, no exercício das atribuições do art. 144, § 4º, da Constituição Federal e do art. 2º, §§ 1º e 2º, da Lei nº 12.830/2013, com fundamento no art. 5º, X e XII, da Constituição Federal, no art. 1º, § 4º, da Lei Complementar nº 105/2001 e no art. 198, § 1º, I, do Código Tributário Nacional, vem REPRESENTAR pela QUEBRA DOS SIGILOS BANCÁRIO E FISCAL de ROGÉRIO e de PAULA (qualificações nos autos), no período de 1º/01/2026 a 31/08/2026, pelos fatos e fundamentos a seguir.',
    pre_arts: ['CF, art. 144, § 4º, e art. 5º, X e XII', 'Lei 12.830/13, art. 2º, §§ 1º e 2º', 'LC 105/2001, art. 1º, § 4º', 'CTN, art. 198, § 1º, I'],
    fatos: 'No IP nº 233/2026, apura-se que o representado, tesoureiro da Câmara Municipal, teria desviado cerca de R$ 600.000,00 de contas do órgão entre janeiro e agosto de 2026, por transferências a terceiros sem lastro contratual, segundo a auditoria interna. Relatório de Inteligência Financeira aponta depósitos fracionados nas contas dele e de sua companheira no mesmo período, e a renda declarada de ambos é incompatível com esses valores.',
    direito: [
      { t: 'Fumus e tipificação', orient: 'Tipifique: funcionário que desvia dinheiro público de que tem a posse em razão do cargo = peculato-desvio (art. 312, caput, 2ª parte). Depósitos fracionados para ocultar a origem sugerem lavagem (Lei 9.613, art. 1º).',
        arts: ['CP, art. 312, caput', 'Lei 9.613/98, art. 1º'],
        check: ['Tipifiquei como peculato-desvio (art. 312)', 'Apontei a lavagem pelos depósitos fracionados (Lei 9.613, art. 1º)', 'Usei a auditoria e o RIF'],
        modelo: 'DO FUMUS COMISSI DELICTI\nA auditoria interna e o Relatório de Inteligência Financeira indicam que o representado, valendo-se da posse do dinheiro público em razão do cargo, desviou-o em proveito próprio e alheio, o que configura, em tese, peculato (art. 312, caput, do CP), e que os valores retornaram em depósitos fracionados, conduta própria da ocultação da origem ilícita (art. 1º da Lei nº 9.613/1998).' },
      { t: 'Cabimento e necessidade (LC 105, art. 1º, § 4º)', orient: 'A quebra cabe na apuração de QUALQUER ilícito, em qualquer fase do IP, e especialmente nos crimes contra a Administração e na lavagem (incisos do § 4º). Diga para que serve: rastrear o destino do dinheiro, o tamanho do desvio e os beneficiários.',
        arts: ['LC 105/2001, art. 1º, § 4º', 'CTN, art. 198, § 1º, I', 'CPP, art. 282, I e II'],
        check: ['Citei o art. 1º, § 4º, da LC 105 ("qualquer ilícito, em qualquer fase")', 'Disse para que serve a quebra (destino, extensão, beneficiários)', 'Incluí a companheira e justifiquei (depósitos nas contas dela)', 'Delimitei o período'],
        modelo: 'DO CABIMENTO E DA NECESSIDADE\nA quebra de sigilo pode ser decretada quando necessária à apuração de qualquer ilícito, em qualquer fase do inquérito, especialmente nos crimes contra a Administração Pública e na lavagem de dinheiro (art. 1º, § 4º, da LC nº 105/2001), e o sigilo fiscal cede à requisição judicial no interesse da justiça (art. 198, § 1º, I, do CTN). A medida é necessária para rastrear o destino dos valores, medir a extensão do desvio e identificar os beneficiários, inclusive a companheira, em cujas contas houve depósitos, e é adequada por limitar-se ao período dos fatos (art. 282, I e II, do CPP).' },
    ],
    pedidos: 'DOS PEDIDOS\na) a QUEBRA DO SIGILO BANCÁRIO de ROGÉRIO e de PAULA, de 1º/01/2026 a 31/08/2026, com ofício ao Banco Central para consulta ao Cadastro de Clientes do Sistema Financeiro Nacional e envio dos extratos pelas instituições financeiras;\nb) a QUEBRA DO SIGILO FISCAL de ambos, com ofício à Receita Federal para envio das declarações de imposto de renda dos exercícios correspondentes (art. 198, § 1º, I, do CTN);\nc) a oitiva do Ministério Público;\nd) a decisão sem intimação prévia dos investigados, sob pena de ineficácia (art. 282, § 3º, do CPP);\ne) a tramitação em sigilo e com urgência.',
    pedidos_check: ['Sigilo bancário dos dois, com período delimitado', 'Sigilo fiscal com ofício à Receita (CTN, art. 198, § 1º, I)', 'Oitiva do MP', 'Sem intimação prévia, sigilo e urgência'],
    cards: [
      { p: 'Fundamento legal da quebra de sigilo bancário na investigação', r: 'Pode ser decretada quando necessária à apuração de qualquer ilícito, em qualquer fase do inquérito ou do processo, especialmente nos crimes listados nos incisos.', a: 'LC 105/2001, art. 1º, § 4º', ce: ['A quebra de sigilo bancário só cabe nos crimes expressamente listados no art. 1º, § 4º, da LC 105/2001.', 'E', 'Cabe para qualquer ilícito; os incisos são exemplos ("especialmente").'] },
      { p: 'O delegado pode requisitar extratos bancários sem ordem judicial?', r: 'Não: para a polícia, a quebra de sigilo bancário está sob reserva de jurisdição.', a: 'LC 105/2001, art. 1º, § 4º; CF, art. 5º, X e XII', ce: ['O delegado de polícia pode requisitar diretamente às instituições financeiras os extratos do investigado.', 'E', 'Depende de ordem judicial.'] },
      { p: 'Sigilo fiscal: quando a Receita fornece dados à investigação criminal?', r: 'Mediante requisição de autoridade judiciária no interesse da justiça.', a: 'CTN, art. 198, § 1º, I', ce: ['A Fazenda pode fornecer dados fiscais do investigado mediante requisição de autoridade judiciária no interesse da justiça.', 'C', 'Art. 198, § 1º, I, do CTN.'] },
      { p: 'Relatório de Inteligência Financeira (UIF) compartilhado com a polícia', r: 'O STF admite o compartilhamento do RIF da UIF e da íntegra do procedimento fiscal da Receita com os órgãos de persecução penal, sem prévia autorização judicial, resguardado o sigilo.', a: 'STF, Tema 990 (RE 1.055.941)', ce: ['O compartilhamento de RIF da UIF com a polícia, para fins penais, depende de prévia autorização judicial.', 'E', 'O STF, no Tema 990, admitiu sem autorização judicial prévia, resguardado o sigilo.'] },
    ],
  },
  /* ---------------------------------------------------------------- 17 */
  {
    id: 'localizacao-13b', dirfund: { bem: 'intimidade e vida privada (sigilo de dados)', inc: 'X e XII' }, titulo: 'Representação pelos meios técnicos de localização da vítima e dos suspeitos (CPP, art. 13-B)', freq: 'Lei 13.344/2016 (tráfico de pessoas); cobrada como peça urgente, com prazo de 12 horas',
    enunciado: 'Em 30/10/2026, às 7h, a estudante Larissa, de 19 anos, foi abordada por dois homens armados ao sair de casa, em Salvador/BA, e levada em um carro. Às 10h, a família recebeu ligações do celular (71) 9XXXX-3333 exigindo R$ 200.000,00 pela libertação. O celular de Larissa está desligado desde a abordagem. A ocorrência foi registrada às 11h na Delegacia. Elabore, com urgência, a peça cabível para localizar a vítima e os autores.',
    mnemonico: 'Art. 13-B: só nos crimes do 13-A (148, 149, 149-A, 158 § 3º, 159 do CP; 239 do ECA). "SINAL, não CONTEÚDO" (§ 2º, I). 30 dias + 1 renovação (§ 2º, II). IP em 72 h do registro (§ 3º). Juiz calado por 12 h → o delegado requisita direto e comunica (§ 4º).',
    preambulo: 'O DELEGADO DE POLÍCIA CIVIL que esta subscreve, no exercício das atribuições do art. 144, § 4º, da Constituição Federal e do art. 2º, §§ 1º e 2º, da Lei nº 12.830/2013, com fundamento no art. 5º, X e XII, da Constituição Federal e no art. 13-B do Código de Processo Penal, vem REPRESENTAR, COM URGÊNCIA, pela autorização para requisitar às empresas prestadoras de serviço de telecomunicações e telemática a DISPONIBILIZAÇÃO IMEDIATA DOS MEIOS TÉCNICOS que permitam a LOCALIZAÇÃO DA VÍTIMA LARISSA E DOS SUSPEITOS, pelos fatos e fundamentos a seguir.',
    pre_arts: ['CF, art. 144, § 4º, e art. 5º, X e XII', 'Lei 12.830/13, art. 2º, §§ 1º e 2º', 'CPP, art. 13-B'],
    fatos: 'Em 30/10/2026, por volta das 7h, nesta capital, a vítima Larissa teria sido abordada por dois homens armados ao sair de casa e levada em um veículo. Às 10h, seus familiares receberam ligações do número (71) 9XXXX-3333 exigindo R$ 200.000,00 pela libertação. O celular da vítima está desligado desde a abordagem. A ocorrência foi registrada às 11h do mesmo dia.',
    direito: [
      { t: 'Crime do rol e cabimento (arts. 13-A e 13-B)', orient: 'O 13-B só vale para os crimes "relacionados ao tráfico de pessoas", que correspondem ao rol do art. 13-A. Extorsão mediante sequestro (art. 159) está no rol. Tipifique e diga que o crime está EM CURSO.',
        arts: ['CPP, arts. 13-A e 13-B', 'CP, art. 159, § 1º (se durar mais de 24 h ou for cometido por bando ou quadrilha — avalie)'],
        check: ['Tipifiquei como extorsão mediante sequestro (art. 159)', 'Disse que o crime está no rol do art. 13-A', 'Disse que o delito está em curso'],
        modelo: 'DO CABIMENTO\nOs fatos configuram, em tese, extorsão mediante sequestro (art. 159 do CP), delito em curso e incluído no rol do art. 13-A do CPP, ao qual se refere o art. 13-B como crime relacionado ao tráfico de pessoas. A localização imediata da vítima e dos suspeitos é necessária à repressão do crime e à preservação da vida e da integridade física de Larissa.' },
      { t: 'O que se pede: sinal, não conteúdo (§§ 1º e 2º)', orient: 'Diga O QUE É o sinal (§ 1º: posicionamento da estação de cobertura, setorização e intensidade de radiofrequência) e que NÃO dá acesso ao conteúdo das comunicações (§ 2º, I). Prazo: até 30 dias, renovável uma vez (§ 2º, II).',
        arts: ['CPP, art. 13-B, § 1º', 'CPP, art. 13-B, § 2º, I a III'],
        check: ['Defini o sinal (§ 1º)', 'Disse que não há acesso ao conteúdo (§ 2º, I)', 'Pedi o prazo de 30 dias, renovável uma vez (§ 2º, II)'],
        modelo: 'DO ALCANCE DA MEDIDA\nPede-se o sinal que permita localizar os aparelhos da vítima e dos suspeitos, isto é, o posicionamento da estação de cobertura, a setorização e a intensidade de radiofrequência (art. 13-B, § 1º), sem acesso ao conteúdo das comunicações, que depende de autorização própria (§ 2º, I), pelo prazo de 30 dias, renovável uma vez por igual período (§ 2º, II).' },
      { t: 'Urgência: 12 horas e IP em 72 horas (§§ 3º e 4º)', orient: 'Peça decisão em 12 horas e avise: sem manifestação judicial nesse prazo, o delegado requisita diretamente e comunica o juiz (§ 4º). Informe que o IP será instaurado em até 72 horas do registro (§ 3º).',
        arts: ['CPP, art. 13-B, § 3º', 'CPP, art. 13-B, § 4º'],
        check: ['Pedi decisão em 12 horas (§ 4º)', 'Disse que, sem decisão, requisitará direto e comunicará o juiz (§ 4º)', 'Informei a instauração do IP em até 72 horas do registro (§ 3º)'],
        modelo: 'DA URGÊNCIA\nHá risco atual à vida da vítima. Requer-se a manifestação judicial em até 12 horas; não havendo, esta autoridade requisitará diretamente às empresas a disponibilização imediata dos meios técnicos, com imediata comunicação a este Juízo (art. 13-B, § 4º). O inquérito policial será instaurado no prazo máximo de 72 horas, contado do registro da ocorrência (§ 3º).' },
    ],
    pedidos: 'DOS PEDIDOS\na) a autorização para requisitar às prestadoras de telecomunicações e telemática a disponibilização imediata dos meios técnicos adequados (posicionamento da estação de cobertura, setorização e intensidade de radiofrequência) que permitam localizar o aparelho da vítima e o de número (71) 9XXXX-3333, pelo prazo de 30 dias, renovável uma vez (art. 13-B, caput, §§ 1º e 2º, II, do CPP);\nb) a decisão no prazo de 12 horas (art. 13-B, § 4º);\nc) a ciência do Ministério Público;\nd) a tramitação em sigilo e com urgência.',
    pedidos_check: ['Meios técnicos para os dois aparelhos, por 30 dias renováveis uma vez', 'Decisão em 12 horas (§ 4º)', 'Ciência do MP, sigilo e urgência'],
    cards: [
      { p: 'Crimes que autorizam a medida do art. 13-B (e a requisição do 13-A)', r: 'Sequestro e cárcere privado (148), redução à condição análoga à de escravo (149), tráfico de pessoas (149-A), extorsão com restrição da liberdade (158, § 3º), extorsão mediante sequestro (159) e envio ilegal de criança ao exterior (ECA, art. 239).', a: 'CPP, arts. 13-A e 13-B', ce: ['A extorsão mediante sequestro está entre os crimes que autorizam a medida do art. 13-B do CPP.', 'C', 'Rol do art. 13-A, ao qual remete o 13-B.'] },
      { p: 'O sinal do art. 13-B dá acesso ao conteúdo das conversas?', r: 'Não: o conteúdo depende de autorização judicial conforme lei específica.', a: 'CPP, art. 13-B, § 2º, I', ce: ['O sinal fornecido com base no art. 13-B permite ouvir as ligações dos suspeitos.', 'E', 'Não permite acesso ao conteúdo (§ 2º, I).'] },
      { p: 'Juiz sem manifestação em 12 horas: o que faz o delegado?', r: 'Requisita diretamente às empresas a disponibilização imediata dos meios técnicos, com imediata comunicação ao juiz.', a: 'CPP, art. 13-B, § 4º', ce: ['Sem manifestação judicial em 12 horas, o delegado pode requisitar diretamente os meios técnicos, comunicando de imediato o juiz.', 'C', 'Art. 13-B, § 4º.'] },
      { p: 'Prazo do sinal e da instauração do IP no art. 13-B', r: 'Sinal por até 30 dias, renovável uma vez por igual período (acima disso, ordem judicial); IP instaurado em até 72 horas do registro da ocorrência.', a: 'CPP, art. 13-B, §§ 2º, II e III, e 3º', ce: ['Na medida do art. 13-B, o inquérito deve ser instaurado em até 24 horas do registro da ocorrência.', 'E', 'O prazo é de 72 horas (§ 3º).'] },
    ],
  },
  /* ---------------------------------------------------------------- 18 */
  {
    id: 'alienacao', dirfund: { bem: 'propriedade', inc: 'XXII' }, titulo: 'Representação pela alienação antecipada de bens (CPP, art. 144-A)', freq: 'Medida assecuratória que costuma vir junto do sequestro; Lei 12.694/2012',
    enunciado: 'No IP nº 77/2026 (Salvador/BA), que apura lavagem de dinheiro por Sérgio, foram sequestrados por ordem judicial e recolhidos ao pátio da Delegacia uma caminhonete Hilux 2025 e uma lancha de 32 pés. O pátio é descoberto, a lancha não tem onde ser guardada nem conservada, e a perícia registrou ferrugem inicial na caminhonete e perda de valor de mercado estimada em 15% em seis meses. Elabore a peça cabível para preservar o valor dos bens.',
    mnemonico: 'Alienação antecipada = 144-A: "DDD" — Deterioração, Depreciação ou Dificuldade de manutenção. Avaliação judicial → leilão (de preferência eletrônico) → valor da avaliação ou maior; 2º leilão em até 10 dias, por no mínimo 80% → dinheiro em conta judicial (§ 3º). Veículo: CRLV ao arrematante sem multas antigas (§ 5º).',
    preambulo: 'O DELEGADO DE POLÍCIA CIVIL que esta subscreve, no exercício das atribuições do art. 144, § 4º, da Constituição Federal e do art. 2º, §§ 1º e 2º, da Lei nº 12.830/2013, com fundamento no art. 5º, XXII, da Constituição Federal, no art. 144-A do Código de Processo Penal e no art. 4º, § 1º, da Lei nº 9.613/1998, vem REPRESENTAR pela ALIENAÇÃO ANTECIPADA da caminhonete e da lancha sequestradas de SÉRGIO (qualificação nos autos), pelos fatos e fundamentos a seguir.',
    pre_arts: ['CF, art. 144, § 4º, e art. 5º, XXII', 'Lei 12.830/13, art. 2º, §§ 1º e 2º', 'CPP, art. 144-A', 'Lei 9.613/98, art. 4º, § 1º'],
    fatos: 'No IP nº 77/2026, que apura lavagem de dinheiro atribuída ao representado, foram sequestrados por ordem judicial uma caminhonete Hilux 2025 e uma lancha de 32 pés, recolhidas ao pátio descoberto desta Delegacia. A perícia registrou ferrugem inicial na caminhonete e perda de valor de mercado estimada em 15% em seis meses; a lancha não dispõe de local adequado para guarda e conservação.',
    direito: [
      { t: 'Fumus: o crime e a origem dos bens', orient: 'A alienação é medida assecuratória: lembre o fumus que justificou o sequestro (indícios da proveniência ilícita) e o crime (lavagem, Lei 9.613, art. 1º). Os bens interessam aos efeitos da condenação (CP, art. 91, II).',
        arts: ['Lei 9.613/98, art. 1º', 'CPP, art. 126 (sequestro: indícios veementes da proveniência ilícita)', 'CP, art. 91, II, "b"'],
        check: ['Tipifiquei (lavagem, Lei 9.613, art. 1º)', 'Lembrei que os bens já estão sequestrados e por quê', 'Liguei os bens aos efeitos da condenação (art. 91, II)'],
        modelo: 'DO FUMUS COMISSI DELICTI\nOs bens foram sequestrados por haver indícios veementes de sua proveniência ilícita (art. 126 do CPP), ligados à lavagem de dinheiro apurada (art. 1º da Lei nº 9.613/1998), e interessam ao confisco como efeito da condenação (art. 91, II, "b", do CP).' },
      { t: 'Periculum: deterioração, depreciação, dificuldade (art. 144-A)', orient: 'É o núcleo da peça: os bens estão sujeitos a deterioração ou depreciação, ou há dificuldade para mantê-los. Use os DADOS do enunciado (ferrugem, 15% em seis meses, lancha sem guarda).',
        arts: ['CPP, art. 144-A, caput', 'Lei 9.613/98, art. 4º, § 1º'],
        check: ['Usei as três hipóteses do art. 144-A (deterioração, depreciação, dificuldade de manutenção)', 'Usei os dados concretos da perícia', 'Disse que a medida PRESERVA o valor (interesse também do investigado)'],
        modelo: 'DO PERICULUM IN MORA\nOs bens estão sujeitos a deterioração e depreciação: a perícia constatou ferrugem inicial na caminhonete e perda de valor estimada em 15% em seis meses, e não há local adequado para guarda e conservação da lancha. Presentes, assim, as hipóteses do art. 144-A do CPP e do art. 4º, § 1º, da Lei nº 9.613/1998. A alienação antecipada preserva o valor dos bens, no interesse do Estado e do próprio investigado, em caso de absolvição.' },
      { t: 'Procedimento: avaliação, leilão e depósito (§§ 1º a 3º e 5º)', orient: 'Mostre que sabe o rito: avaliação judicial, leilão preferencialmente eletrônico, segundo leilão por no mínimo 80% da avaliação, depósito em conta judicial e destino conforme o resultado; veículo: certificado ao arrematante livre de débitos anteriores.',
        arts: ['CPP, art. 144-A, §§ 1º, 2º, 3º e 5º'],
        check: ['Pedi a avaliação judicial', 'Mencionei o leilão e o piso de 80% no segundo leilão (§ 2º)', 'Pedi o depósito em conta vinculada ao juízo (§ 3º)', 'Pedi o ofício ao Detran para o arrematante (§ 5º)'],
        modelo: 'DO PROCEDIMENTO\nOs bens devem ser avaliados judicialmente e alienados em leilão, preferencialmente eletrônico, pelo valor da avaliação ou maior; não alcançado esse valor, em novo leilão, em até 10 dias, por valor não inferior a 80% da avaliação (art. 144-A, §§ 1º e 2º). O produto ficará depositado em conta vinculada ao Juízo até a decisão final (§ 3º).' },
    ],
    pedidos: 'DOS PEDIDOS\na) a avaliação judicial da caminhonete e da lancha (art. 144-A, § 2º, do CPP);\nb) a ALIENAÇÃO ANTECIPADA dos bens em leilão, preferencialmente eletrônico (art. 144-A, caput e § 1º);\nc) o depósito do produto em conta vinculada ao Juízo até a decisão final, com conversão em renda para o Estado em caso de condenação ou devolução em caso de absolvição (§ 3º);\nd) a expedição de ofício ao Detran e à Capitania dos Portos para o registro em nome do arrematante, livre de multas, encargos e tributos anteriores (§ 5º);\ne) a intimação do proprietário e a oitiva do Ministério Público.',
    pedidos_check: ['Avaliação judicial', 'Alienação em leilão (art. 144-A)', 'Depósito em conta judicial (§ 3º)', 'Ofício ao órgão de registro para o arrematante (§ 5º)', 'Intimação do proprietário e oitiva do MP'],
    cards: [
      { p: 'Hipóteses de alienação antecipada (art. 144-A do CPP)', r: 'Bens sujeitos a qualquer grau de deterioração ou depreciação, ou quando houver dificuldade para sua manutenção.', a: 'CPP, art. 144-A, caput', ce: ['A alienação antecipada exige que o bem esteja em risco de perecimento total.', 'E', 'Basta qualquer grau de deterioração ou depreciação, ou dificuldade de manutenção.'] },
      { p: 'Segundo leilão na alienação antecipada: qual o piso?', r: 'Novo leilão em até 10 dias do primeiro, por valor não inferior a 80% da avaliação judicial.', a: 'CPP, art. 144-A, § 2º', ce: ['Não alcançado o valor da avaliação, os bens podem ser alienados em novo leilão por valor não inferior a 80% do avaliado.', 'C', 'Art. 144-A, § 2º.'] },
      { p: 'Destino do dinheiro da alienação antecipada', r: 'Fica em conta vinculada ao juízo até a decisão final: convertido em renda para a União, o Estado ou o DF, se houver condenação; devolvido ao acusado, se absolvido.', a: 'CPP, art. 144-A, § 3º', ce: ['O produto da alienação antecipada é imediatamente incorporado ao patrimônio do Estado.', 'E', 'Fica depositado em conta judicial até a decisão final (§ 3º).'] },
      { p: 'Veículo alienado antecipadamente: e as multas antigas?', r: 'O juiz ordena à autoridade de trânsito o registro e licenciamento em favor do arrematante, livre de multas, encargos e tributos anteriores.', a: 'CPP, art. 144-A, § 5º', ce: ['O arrematante do veículo alienado antecipadamente responde pelas multas anteriores à arrematação.', 'E', 'Fica livre delas (§ 5º).'] },
    ],
  },
  /* ---------------------------------------------------------------- 19 */
  {
    id: 'perfil-genetico', dirfund: { bem: 'intimidade e a identificação civil (só se identifica criminalmente nas hipóteses da lei)', inc: 'X e LVIII' }, titulo: 'Representação por identificação criminal com coleta de perfil genético e acesso aos bancos de dados', freq: 'Lei 12.037/2009 (com a Lei 12.654/2012 e o Pacote Anticrime); tema em alta no STJ',
    enunciado: 'No IP nº 518/2026 (Itabuna/BA), apura-se o estupro de Camila, ocorrido em 12/10/2026 em terreno baldio. O exame de corpo de delito colheu material biológico do agressor, cujo perfil genético foi obtido pela perícia. Uma testemunha viu Fábio sair do terreno logo depois do fato; Camila não conseguiu reconhecê-lo com segurança, pois foi atacada por trás. Fábio é civilmente identificado e se recusa a fornecer material. Elabore a peça cabível para confirmar ou afastar a autoria.',
    mnemonico: 'Identificação criminal de quem é civilmente identificado = exceção (CF, art. 5º, LVIII). Lei 12.037: art. 3º, IV (essencial às investigações, por DESPACHO JUDICIAL) + art. 5º, parágrafo único (pode incluir PERFIL GENÉTICO). Acesso aos bancos: art. 7º-C, § 11 (Multibiométrico) e LEP, art. 9º-A, § 2º (perfis genéticos) — sempre com IP instaurado e juiz.',
    preambulo: 'O DELEGADO DE POLÍCIA CIVIL que esta subscreve, no exercício das atribuições do art. 144, § 4º, da Constituição Federal e do art. 2º, §§ 1º e 2º, da Lei nº 12.830/2013, com fundamento no art. 5º, X e LVIII, da Constituição Federal, nos arts. 3º, IV, 5º, parágrafo único, e 7º-C, § 11, da Lei nº 12.037/2009 e no art. 9º-A, § 2º, da Lei nº 7.210/1984, vem REPRESENTAR pela IDENTIFICAÇÃO CRIMINAL de FÁBIO (qualificação nos autos), com COLETA DE MATERIAL BIOLÓGICO para obtenção do PERFIL GENÉTICO, e pelo ACESSO AOS BANCOS DE DADOS de perfis genéticos e multibiométrico, pelos fatos e fundamentos a seguir.',
    pre_arts: ['CF, art. 144, § 4º, e art. 5º, X e LVIII', 'Lei 12.830/13, art. 2º, §§ 1º e 2º', 'Lei 12.037/09, arts. 3º, IV, 5º, parágrafo único, e 7º-C, § 11', 'LEP, art. 9º-A, § 2º'],
    fatos: 'No IP nº 518/2026, apura-se o estupro da vítima Camila, ocorrido em 12/10/2026, em terreno baldio desta cidade. O exame de corpo de delito colheu material biológico do agressor, cujo perfil genético foi obtido pela perícia. Testemunha viu o representado sair do terreno logo após o fato; a vítima, atacada por trás, não o reconheceu com segurança. O representado é civilmente identificado e recusou-se a fornecer material.',
    direito: [
      { t: 'Fumus e tipificação', orient: 'Tipifique (estupro, art. 213) e mostre os indícios: a testemunha que viu Fábio sair do local. Diga por que eles NÃO bastam sozinhos: a vítima não reconheceu.',
        arts: ['CP, art. 213', 'CPP, art. 158 (corpo de delito nos crimes que deixam vestígios)'],
        check: ['Tipifiquei como estupro (art. 213)', 'Apontei o indício (testemunha) e sua insuficiência', 'Mencionei o vestígio já periciado'],
        modelo: 'DO FUMUS COMISSI DELICTI\nO laudo de corpo de delito comprova a materialidade do estupro (art. 213 do CP) e preservou vestígio biológico do agressor, cujo perfil genético já foi obtido. Há indício de autoria, pois testemunha viu o representado deixar o local logo após o fato, mas a vítima, atacada por trás, não o reconheceu com segurança.' },
      { t: 'Identificação essencial às investigações (Lei 12.037, art. 3º, IV)', orient: 'Quem é civilmente identificado só é identificado criminalmente nas hipóteses da lei (CF, art. 5º, LVIII). A do caso é o art. 3º, IV: essencial às investigações, por despacho judicial, que pode ser provocado pela autoridade policial. O art. 5º, parágrafo único, permite incluir a coleta de material biológico.',
        arts: ['CF, art. 5º, LVIII', 'Lei 12.037/09, art. 3º, IV', 'Lei 12.037/09, art. 5º, parágrafo único', 'Lei 12.037/09, art. 5º-A, § 1º (sem traços somáticos ou comportamentais)'],
        check: ['Citei o art. 5º, LVIII, da CF (exceção à regra)', 'Fundamentei no art. 3º, IV (essencial às investigações, despacho judicial)', 'Pedi a coleta pelo art. 5º, parágrafo único', 'Disse que o perfil não revela traços somáticos ou comportamentais (art. 5º-A, § 1º)'],
        modelo: 'DA IDENTIFICAÇÃO CRIMINAL ESSENCIAL ÀS INVESTIGAÇÕES\nEmbora civilmente identificado, o representado pode ser identificado criminalmente nas hipóteses legais (art. 5º, LVIII, da CF), entre elas quando a identificação for essencial às investigações, por despacho judicial provocado pela autoridade policial (art. 3º, IV, da Lei nº 12.037/2009), podendo incluir a coleta de material biológico para obtenção do perfil genético (art. 5º, parágrafo único). O confronto com o perfil extraído do vestígio é o único meio seguro de confirmar ou afastar a autoria, e os dados não revelarão traços somáticos ou comportamentais (art. 5º-A, § 1º).' },
      { t: 'Acesso aos bancos de dados (7º-C, § 11; LEP, 9º-A, § 2º)', orient: 'Com o IP instaurado, a autoridade policial pode requerer ao juiz o acesso ao Banco Nacional Multibiométrico e de Impressões Digitais (Lei 12.037, art. 7º-C, § 11) e ao banco de perfis genéticos (LEP, art. 9º-A, § 2º). Serve para comparar o vestígio com perfis já cadastrados (outros crimes).',
        arts: ['Lei 12.037/09, art. 7º-C, § 11', 'LEP, art. 9º-A, § 2º'],
        check: ['Disse que há IP instaurado (requisito do acesso)', 'Pedi o acesso ao banco multibiométrico (7º-C, § 11)', 'Pedi o acesso ao banco de perfis genéticos (LEP, 9º-A, § 2º)'],
        modelo: 'DO ACESSO AOS BANCOS DE DADOS\nInstaurado o inquérito, requer-se também o acesso ao Banco Nacional Multibiométrico e de Impressões Digitais (art. 7º-C, § 11, da Lei nº 12.037/2009) e ao banco de dados de perfis genéticos (art. 9º-A, § 2º, da Lei nº 7.210/1984), para o confronto do vestígio com os perfis já cadastrados, inclusive para apurar eventual autoria de outros crimes.' },
    ],
    pedidos: 'DOS PEDIDOS\na) a IDENTIFICAÇÃO CRIMINAL de FÁBIO, pelos processos datiloscópico e fotográfico, com COLETA DE MATERIAL BIOLÓGICO para obtenção do perfil genético, por técnica adequada e indolor (arts. 3º, IV, e 5º, parágrafo único, da Lei nº 12.037/2009);\nb) o confronto do perfil obtido com o vestígio colhido no exame de corpo de delito, consignado em laudo pericial;\nc) o ACESSO ao Banco Nacional Multibiométrico e de Impressões Digitais e ao banco de dados de perfis genéticos (art. 7º-C, § 11, da Lei nº 12.037/2009; art. 9º-A, § 2º, da LEP);\nd) a oitiva do Ministério Público;\ne) a tramitação em sigilo.',
    pedidos_check: ['Identificação criminal com coleta de perfil genético (arts. 3º, IV, e 5º, parágrafo único)', 'Confronto com o vestígio, em laudo', 'Acesso aos dois bancos de dados', 'Oitiva do MP e sigilo'],
    cards: [
      { p: 'Identificação criminal "essencial às investigações": quem decide?', r: 'O juiz, por despacho, de ofício ou mediante representação da autoridade policial, do MP ou da defesa.', a: 'Lei 12.037/09, art. 3º, IV', ce: ['O delegado pode determinar sozinho a identificação criminal do civilmente identificado quando a julgar essencial às investigações.', 'E', 'Depende de despacho judicial (art. 3º, IV).'] },
      { p: 'A identificação criminal pode incluir coleta de DNA?', r: 'Sim, na hipótese do art. 3º, IV (essencial às investigações): coleta de material biológico para obter o perfil genético.', a: 'Lei 12.037/09, art. 5º, parágrafo único', ce: ['Na identificação criminal essencial às investigações, pode haver coleta de material biológico para obtenção do perfil genético.', 'C', 'Art. 5º, parágrafo único, da Lei 12.037.'] },
      { p: 'O que o perfil genético do banco pode revelar?', r: 'Não pode revelar traços somáticos ou comportamentais, salvo a determinação genética de gênero.', a: 'Lei 12.037/09, art. 5º-A, § 1º', ce: ['As informações dos bancos de perfis genéticos podem revelar traços comportamentais do investigado.', 'E', 'Vedado, salvo a determinação de gênero (art. 5º-A, § 1º).'] },
      { p: 'Condenado que se recusa a fornecer DNA (LEP, art. 9º-A)', r: 'A recusa é falta grave; o STJ entendeu que a coleta do art. 9º-A não viola a vedação à autoincriminação.', a: 'LEP, arts. 9º-A, § 8º, e 50, VIII; STJ, HC 879.757 (2024)', ce: ['A recusa do condenado em fornecer material para o perfil genético do art. 9º-A da LEP constitui falta grave.', 'C', 'Arts. 9º-A, § 8º, e 50, VIII, da LEP.'] },
      { p: 'Acesso da polícia ao banco de perfis genéticos', r: 'A autoridade policial pode requerer ao juiz competente, no caso de inquérito instaurado, o acesso ao banco de dados de identificação de perfil genético.', a: 'LEP, art. 9º-A, § 2º', ce: ['O delegado pode consultar o banco de perfis genéticos independentemente de inquérito instaurado e de autorização judicial.', 'E', 'Exige inquérito instaurado e requerimento ao juiz (art. 9º-A, § 2º).'] },
    ],
  },
  /* ---------------------------------------------------------------- 20 */
  {
    id: 'internacao', dirfund: { bem: 'liberdade de locomoção do adolescente', inc: 'LXI' }, titulo: 'Representação pela internação provisória de adolescente (ECA, art. 108)', freq: 'ECA no edital; costuma cair com ato infracional análogo a roubo',
    enderecamento: 'EXCELENTÍSSIMO(A) SENHOR(A) JUIZ(ÍZA) DE DIREITO DA VARA DA INFÂNCIA E JUVENTUDE DA COMARCA DE …/BA',
    enunciado: 'Em 01/11/2026, em Salvador/BA, Kauã, de 16 anos, encostou uma faca no pescoço de Renata em um ponto de ônibus e levou o celular dela. Foi apreendido 10 minutos depois, com o celular e a faca. Na Delegacia, foi lavrado o auto de apreensão em flagrante de ato infracional. Há registro de outros dois atos infracionais análogos a roubo nos últimos seis meses, e Renata conta que Kauã gritou que "voltaria para pegá-la". Os pais compareceram à Delegacia. Elabore a peça cabível.',
    mnemonico: 'Internação provisória = ECA 108: máximo 45 DIAS + decisão fundamentada + indícios de autoria e materialidade + NECESSIDADE IMPERIOSA. Cabimento da internação (122): violência ou grave ameaça, reiteração em infrações graves ou descumprimento reiterado de medida. Nunca em presídio (123 e 185). Não é inquérito: é auto de apreensão (173).',
    preambulo: 'O DELEGADO DE POLÍCIA CIVIL que esta subscreve, no exercício das atribuições do art. 144, § 4º, da Constituição Federal e do art. 2º, §§ 1º e 2º, da Lei nº 12.830/2013, com fundamento no art. 227, § 3º, V, da Constituição Federal e nos arts. 106, 108, 122, 174 e 175 da Lei nº 8.069/1990, vem REPRESENTAR pela INTERNAÇÃO PROVISÓRIA, pelo prazo máximo de 45 (quarenta e cinco) dias, do adolescente KAUÃ (qualificação nos autos), pelos fatos e fundamentos a seguir.',
    pre_arts: ['CF, art. 144, § 4º, e art. 227, § 3º, V', 'Lei 12.830/13, art. 2º, §§ 1º e 2º', 'ECA, arts. 106, 108, 122, 174 e 175'],
    fatos: 'Em 01/11/2026, nesta capital, o adolescente teria subtraído o celular da vítima Renata mediante grave ameaça, encostando uma faca em seu pescoço. Foi apreendido cerca de 10 minutos depois, com o celular e a faca, e lavrado o auto de apreensão em flagrante de ato infracional (art. 173 do ECA). Há registro de outros dois atos infracionais análogos a roubo nos últimos seis meses, e a vítima relata ter sido ameaçada de nova investida.',
    direito: [
      { t: 'Ato infracional e indícios (art. 108, parágrafo único)', orient: 'Adolescente não comete crime: comete ATO INFRACIONAL ANÁLOGO (art. 103). Tipifique o análogo (roubo com arma branca: art. 157, § 2º, VII) e mostre os indícios suficientes de autoria e materialidade.',
        arts: ['ECA, art. 103 (ato infracional)', 'CP, art. 157, § 2º, VII (arma branca)', 'ECA, art. 108, parágrafo único'],
        check: ['Falei em ato infracional análogo (não em crime)', 'Tipifiquei o análogo com o inciso da arma branca (art. 157, § 2º, VII)', 'Mostrei indícios de autoria e materialidade'],
        modelo: 'DO ATO INFRACIONAL E DOS INDÍCIOS\nO adolescente foi apreendido logo após o fato, na posse do celular da vítima e da faca, o que traz indícios suficientes de autoria e materialidade (art. 108, parágrafo único, do ECA) do ato infracional análogo ao roubo majorado pelo emprego de arma branca (art. 103 do ECA c/c art. 157, § 2º, VII, do CP).' },
      { t: 'Cabimento e necessidade imperiosa (arts. 122 e 174)', orient: 'A internação só cabe nas hipóteses do art. 122 (aqui, incisos I e II). A provisória exige NECESSIDADE IMPERIOSA (108). Use o art. 174: gravidade do ato e repercussão social, para a segurança pessoal do adolescente ou a manutenção da ordem pública. Afaste outra medida adequada (122, § 2º).',
        arts: ['ECA, art. 122, I e II, e § 2º', 'ECA, art. 174', 'CF, art. 227, § 3º, V (brevidade, excepcionalidade, condição peculiar)'],
        check: ['Enquadrei no art. 122, I (grave ameaça) e II (reiteração)', 'Demonstrei a necessidade imperiosa com fatos (ameaça à vítima, reiteração)', 'Usei o art. 174 (ordem pública)', 'Afastei outra medida adequada (art. 122, § 2º)', 'Citei brevidade, excepcionalidade e condição peculiar'],
        modelo: 'DO CABIMENTO E DA NECESSIDADE IMPERIOSA\nO ato foi cometido mediante grave ameaça a pessoa e há reiteração em infrações graves, hipóteses do art. 122, I e II, do ECA. A necessidade da medida é imperiosa (art. 108, parágrafo único): o adolescente ameaçou voltar a atacar a vítima e reitera atos análogos a roubo em curto intervalo, de modo que a liberação aos pais não garante a ordem pública (art. 174). Nenhuma outra medida é adequada no momento (art. 122, § 2º), observados a brevidade, a excepcionalidade e a condição peculiar de pessoa em desenvolvimento (art. 227, § 3º, V, da CF).' },
      { t: 'Local de cumprimento (arts. 123 e 185)', orient: 'A internação se cumpre em entidade exclusiva para adolescentes, nunca em estabelecimento prisional (arts. 123 e 185). Sem vaga imediata, pode aguardar na repartição policial, separado dos adultos, por no máximo 5 dias (art. 185, § 2º).',
        arts: ['ECA, art. 123', 'ECA, art. 185 e § 2º', 'ECA, art. 175 (encaminhamento ao MP)'],
        check: ['Pedi entidade exclusiva para adolescentes (art. 123)', 'Disse que não pode ser em estabelecimento prisional (art. 185)', 'Informei o encaminhamento ao MP (art. 175)'],
        modelo: 'DO LOCAL DE CUMPRIMENTO\nA medida deverá ser cumprida em entidade exclusiva para adolescentes, em local distinto do destinado ao abrigo, observada a separação por idade, compleição física e gravidade da infração (art. 123 do ECA), vedado o estabelecimento prisional (art. 185). Não liberado o adolescente, ele é encaminhado ao representante do Ministério Público (art. 175).' },
    ],
    pedidos: 'DOS PEDIDOS\na) a INTERNAÇÃO PROVISÓRIA do adolescente KAUÃ pelo prazo máximo de 45 (quarenta e cinco) dias (art. 108 do ECA);\nb) o cumprimento em entidade exclusiva para adolescentes, vedado o estabelecimento prisional (arts. 123 e 185);\nc) a oitiva do Ministério Público, a quem o adolescente é encaminhado (art. 175);\nd) a ciência aos pais ou responsável;\ne) a tramitação com urgência e em segredo de justiça (art. 143).',
    pedidos_check: ['Internação provisória por no máximo 45 dias (art. 108)', 'Entidade exclusiva, não presídio (arts. 123 e 185)', 'Oitiva/encaminhamento ao MP (art. 175)', 'Ciência aos pais', 'Urgência e sigilo (art. 143)'],
    cards: [
      { p: 'Prazo e requisitos da internação provisória', r: 'No máximo 45 dias; decisão fundamentada, com indícios suficientes de autoria e materialidade e demonstrada a necessidade imperiosa da medida.', a: 'ECA, art. 108 e parágrafo único', ce: ['A internação provisória do adolescente pode durar até 90 dias.', 'E', 'O máximo é de 45 dias (art. 108).'] },
      { p: 'Hipóteses em que cabe a internação (art. 122)', r: 'I — ato infracional com grave ameaça ou violência a pessoa; II — reiteração no cometimento de outras infrações graves; III — descumprimento reiterado e injustificável de medida anteriormente imposta.', a: 'ECA, art. 122', ce: ['A internação só pode ser aplicada nas hipóteses do art. 122 do ECA, e nunca quando houver outra medida adequada.', 'C', 'Art. 122, caput e § 2º.'] },
      { p: 'Ato infracional análogo ao tráfico e internação', r: 'O ato infracional análogo ao tráfico de drogas, por si só, não conduz obrigatoriamente à internação.', a: 'STJ, Súmula 492', ce: ['O ato infracional análogo ao tráfico de drogas, por si só, impõe a internação do adolescente.', 'E', 'Súmula 492 do STJ: não conduz obrigatoriamente à internação.'] },
      { p: 'Adolescente pode aguardar vaga na delegacia?', r: 'Sim, excepcionalmente: em seção isolada dos adultos e com instalações apropriadas, por no máximo 5 dias, se impossível a transferência imediata.', a: 'ECA, art. 185, § 2º', ce: ['Sem vaga em entidade, o adolescente pode aguardar em repartição policial, isolado dos adultos, por até 5 dias.', 'C', 'Art. 185, § 2º.'] },
      { p: 'Apreendido em flagrante de ato com violência ou grave ameaça: que peça a autoridade policial lavra?', r: 'O auto de apreensão (ouvidas as testemunhas e o adolescente), apreende o produto e os instrumentos e requisita os exames.', a: 'ECA, art. 173', ce: ['No ato infracional com grave ameaça, a autoridade policial pode substituir o auto de apreensão por boletim de ocorrência circunstanciado.', 'E', 'Com violência ou grave ameaça, lavra-se o auto de apreensão (art. 173); o boletim circunstanciado só nos demais casos (parágrafo único).'] },
    ],
  }
);

/* Atos do delegado que o edital não cobra como peça (D-014): ficam como cartões. */
LEIS.push({ id: 'atos-delegado', titulo: 'Atos do Delegado sem o juiz (12-C e 13-A)', sub: 'Afastamento do lar e requisição de dados — cartões, não peça', cards: [
 {
  "p": "Ordem de quem pode afastar o agressor do lar (art. 12-C)",
  "r": "I — juiz; II — delegado, se o município não for sede de comarca; III — policial, se também não houver delegado disponível.",
  "a": "Lei 11.340/06, art. 12-C, I a III",
  "ce": [
   "O policial pode afastar o agressor do lar quando o município não for sede de comarca e não houver delegado disponível no momento.",
   "C",
   "Art. 12-C, III."
  ]
 },
 {
  "p": "Afastado o agressor pelo delegado, em quanto tempo o juiz é comunicado?",
  "r": "24 horas; o juiz decide em igual prazo sobre manter ou rever a medida, com ciência ao MP.",
  "a": "Lei 11.340/06, art. 12-C, § 1º",
  "ce": [
   "O juiz deve ser comunicado em até 48 horas do afastamento determinado pelo delegado.",
   "E",
   "Em 24 horas (art. 12-C, § 1º)."
  ]
 },
 {
  "p": "Havendo risco à mulher, cabe liberdade provisória ao preso?",
  "r": "Não: havendo risco à integridade da ofendida ou à efetividade da medida, não se concede liberdade provisória.",
  "a": "Lei 11.340/06, art. 12-C, § 2º",
  "ce": [
   "Mesmo com risco à integridade da ofendida, o preso tem direito à liberdade provisória com fiança.",
   "E",
   "O art. 12-C, § 2º, veda a liberdade provisória nesse caso."
  ]
 },
 {
  "p": "Ameaça contra a mulher por razões da condição do sexo feminino",
  "r": "Pena aplicada em dobro (§ 1º) e ação penal pública incondicionada (§ 2º) — Lei 14.994/2024.",
  "a": "CP, art. 147, §§ 1º e 2º",
  "ce": [
   "A ameaça contra a mulher por razões da condição do sexo feminino depende de representação.",
   "E",
   "É de ação pública incondicionada (art. 147, § 2º, ressalva do § 1º)."
  ]
 },
 {
  "p": "Feminicídio hoje: onde está tipificado?",
  "r": "Crime autônomo: art. 121-A do CP, reclusão de 20 a 40 anos (Lei 14.994/2024).",
  "a": "CP, art. 121-A",
  "ce": [
   "Desde a Lei 14.994/2024, o feminicídio é crime autônomo, previsto no art. 121-A do CP.",
   "C",
   "Deixou de ser qualificadora do art. 121."
  ]
 },
 {
  "p": "Crimes do rol do art. 13-A do CPP",
  "r": "CP: 148 (sequestro e cárcere privado), 149 (condição análoga à de escravo), 149-A (tráfico de pessoas), 158, § 3º (extorsão com restrição da liberdade), 159 (extorsão mediante sequestro); ECA: 239.",
  "a": "CPP, art. 13-A",
  "ce": [
   "O roubo majorado pela restrição da liberdade da vítima está no rol do art. 13-A do CPP.",
   "E",
   "Está a EXTORSÃO com restrição da liberdade (art. 158, § 3º), não o roubo."
  ]
 },
 {
  "p": "Prazo de resposta à requisição do art. 13-A",
  "r": "24 horas.",
  "a": "CPP, art. 13-A, parágrafo único",
  "ce": [
   "A requisição de dados cadastrais do art. 13-A deve ser atendida em 24 horas.",
   "C",
   "Art. 13-A, parágrafo único."
  ]
 },
 {
  "p": "Sinal de localização (art. 13-B): por quanto tempo?",
  "r": "Por período não superior a 30 dias, renovável uma única vez por igual período; além disso, só com ordem judicial.",
  "a": "CPP, art. 13-B, § 2º, II e III",
  "ce": [
   "O sinal do art. 13-B é fornecido por até 60 dias, renováveis livremente.",
   "E",
   "Até 30 dias, renovável uma vez (art. 13-B, § 2º, II)."
  ]
 },
 {
  "p": "Art. 13-B: e se o juiz não se manifestar?",
  "r": "Em 12 horas sem manifestação, a autoridade requisita diretamente às empresas, com imediata comunicação ao juiz.",
  "a": "CPP, art. 13-B, § 4º",
  "ce": [
   "Sem manifestação judicial em 12 horas, o delegado pode requisitar diretamente os sinais, comunicando o juiz.",
   "C",
   "Art. 13-B, § 4º."
  ]
 },
 {
  "p": "Art. 13-B: prazo para instaurar o IP",
  "r": "No máximo 72 horas, contadas do registro da ocorrência.",
  "a": "CPP, art. 13-B, § 3º",
  "ce": [
   "No caso do art. 13-B, o IP deve ser instaurado em até 24 horas do registro da ocorrência.",
   "E",
   "Em até 72 horas (art. 13-B, § 3º)."
  ]
 },
 {
  "p": "Requisição de dados cadastrais na orcrim e na lavagem",
  "r": "Orcrim: Lei 12.850, art. 15 (independe de autorização judicial). Lavagem: Lei 9.613, art. 17-B.",
  "a": "Lei 12.850/13, art. 15; Lei 9.613/98, art. 17-B",
  "ce": [
   "Na investigação de organização criminosa, o delegado precisa de ordem judicial para obter dados cadastrais do investigado.",
   "E",
   "Tem acesso independentemente de autorização judicial (art. 15)."
  ]
 }
] });
