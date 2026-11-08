# Pente Fino de Direito Processual Penal — CPP-4 (ação penal), 4.1 (conceito, espécies, condições), 4.2 (ANPP),
# 4.2-B2 (sujeitos do processo), CPP-5 (Juizados Especiais Criminais) e CPP-6 (TCO; atos processuais: forma, lugar,
# tempo) (08/11/2026).
from base import I
from cpp_juris import J

CPP = 'CPP:'
CF = 'CF:'
CP = 'CP:'
JE = 'L9099:'

# ======================= CPP-4 · Ação penal =======================
P = 'DBA26-CPP-4'
I(P, 1, 'Regra da ação pública',
  'A ação penal é pública, salvo quando a lei expressamente a declara privativa do ofendido.', 'C',
  'CP, art. 100, caput: **a regra é a ação pública**; a privada depende de previsão expressa ("somente se procede mediante queixa").',
  lei=[(CP + '100', 'A ação penal é pública, salvo quando a lei expressamente a declara privativa do ofendido', None, 'CP, art. 100, caput')],
  kw=['ação pública', 'privativa do ofendido'])
I(P, 1, 'Crime contra ente público',
  'Seja qual for o crime, quando praticado em detrimento do patrimônio ou interesse da União, Estado e Município, a ação penal será pública.', 'C',
  'Art. 24, § 2º, do CPP.',
  lei=[(CPP + '24', 'Seja qual for o crime, quando praticado em detrimento do patrimônio ou interesse da União, Estado e Município, a ação penal será pública', None, 'CPP, art. 24, § 2º')],
  kw=['ação penal será pública', 'patrimônio público'])
I(P, 1, 'Indisponibilidade',
  'O Ministério Público pode desistir da ação penal pública se, no curso da instrução, se convencer da inocência do réu.', 'E',
  'Art. 42: o MP **não poderá desistir** da ação penal (**indisponibilidade**). Pode, nas alegações finais, pedir a absolvição — e o juiz pode condenar assim mesmo (art. 385).',
  lei=[(CPP + '42', 'O Ministério Público não poderá desistir da ação penal', None, 'CPP, art. 42')],
  peg='Confundir pedido de absolvição com desistência.',
  kw=['indisponibilidade', 'não poderá desistir'])
I(P, 1, 'Ação privada subsidiária',
  'Será admitida ação privada nos crimes de ação pública se esta não for intentada no prazo legal, cabendo ao MP, entre outras providências, aditar a queixa, repudiá-la e oferecer denúncia substitutiva.', 'C',
  'Art. 29 do CPP e CF, art. 5º, LIX: só cabe na **inércia** do MP — não quando ele pede arquivamento ou diligências.',
  lei=[(CPP + '29', 'Será admitida ação privada nos crimes de ação pública, se esta não for intentada no prazo legal', 'oferecer denúncia substitutiva', 'CPP, art. 29')],
  kw=['ação privada subsidiária', 'inércia'])
I(P, 1, 'Subsidiária e arquivamento',
  'Cabe ação penal privada subsidiária da pública quando o Ministério Público, no prazo legal, promove o arquivamento do inquérito.', 'E',
  'O arquivamento não é inércia: o MP **atuou**. A subsidiária pressupõe que a ação **não foi intentada no prazo legal** sem qualquer manifestação.',
  lei=[(CF + '5', 'será admitida ação privada nos crimes de ação pública, se esta não for intentada no prazo legal', None, 'CF, art. 5º, LIX')],
  peg='Tratar o pedido de arquivamento como inércia.',
  kw=['inércia', 'arquivamento'])
I(P, 1, 'Prazo da denúncia',
  'O prazo para oferecimento da denúncia é de 5 dias se o réu estiver preso e de 30 dias se estiver solto ou afiançado.', 'E',
  'Art. 46 do CPP: **5 dias** (preso) e **15 dias** (solto ou afiançado), contados do recebimento dos autos pelo MP.',
  lei=[(CPP + '46', 'O prazo para oferecimento da denúncia, estando o réu preso, será de 5 dias', 'se o réu estiver solto ou afiançado', 'CPP, art. 46, caput')],
  exc=['Lei de Drogas: 10 dias (art. 54, III, da Lei 11.343/2006)', 'Crimes contra a economia popular: 2 dias (Lei 1.521/1951)'],
  peg='Confundir o prazo da denúncia com o do inquérito de réu solto.',
  kw=['5 dias', '15 dias'])
# --- CPP-4 · Rodada 2
I(P, 2, 'Lesão corporal na violência doméstica',
  'A ação penal relativa ao crime de lesão corporal resultante de violência doméstica contra a mulher é pública condicionada à representação, por se tratar de lesão leve.', 'E',
  '**Súmula 542/STJ**: é pública **incondicionada**. A Lei Maria da Penha afasta a Lei 9.099/1995 (art. 41), inclusive o art. 88 (representação nas lesões leves).',
  lei=[('L11340:41', 'Aos crimes praticados com violência doméstica e familiar contra a mulher', 'não se aplica a Lei nº 9.099', 'Lei 11.340/2006, art. 41')],
  juris=[J['S542']],
  peg='Aplicar o art. 88 da Lei 9.099/1995 à violência doméstica.',
  kw=['Súmula 542', 'pública incondicionada'])
I(P, 2, 'Crime contra a honra de servidor',
  'No crime contra a honra de servidor público em razão de suas funções, a legitimidade é exclusiva do Ministério Público, mediante representação do ofendido.', 'E',
  '**Súmula 714/STF**: legitimidade **concorrente** — queixa do ofendido **ou** denúncia do MP mediante representação.',
  juris=[J['STF714']],
  peg='Trocar "concorrente" por "exclusiva".',
  kw=['Súmula 714', 'legitimidade concorrente'])
I(P, 2, 'Crimes sexuais',
  'Nos crimes contra a liberdade sexual e nos crimes sexuais contra vulnerável, procede-se mediante ação penal pública incondicionada.', 'C',
  'CP, art. 225 (Lei 13.718/2018): **pública incondicionada** em todos os crimes dos Capítulos I e II do Título VI.',
  lei=[(CP + '225', 'procede-se mediante ação penal pública incondicionada', None, 'CP, art. 225')],
  kw=['pública incondicionada', 'crimes sexuais'])
I(P, 2, 'Estelionato',
  'No estelionato, somente se procede mediante representação, salvo se a vítima for a Administração Pública, criança ou adolescente, pessoa com deficiência mental, ou maior de 70 anos ou incapaz.', 'E',
  'A **Lei 15.397/2026 revogou o § 5º do art. 171** do CP (incluído pela Lei 13.964/2019). Sem previsão expressa de representação, volta a regra do art. 100: ação **pública incondicionada**.',
  lei=[(CP + '171', '§ 5º (Revogado). (Redação dada pela Lei nº 15.397, de 2026)', None, 'CP, art. 171, § 5º'),
       (CP + '100', 'A ação penal é pública, salvo quando a lei expressamente a declara privativa do ofendido', None, 'CP, art. 100, caput')],
  peg='Repetir a regra da representação, revogada em 2026.',
  kw=['pública incondicionada', 'Lei 15.397/2026'])

# ======================= CPP-4.1 · Conceito, características, espécies e condições =======================
P = 'DBA26-CPP-4.1'
I(P, 1, 'Condicionada — titularidade',
  'Nos crimes de ação pública, esta será promovida por denúncia do Ministério Público, mas dependerá, quando a lei o exigir, de requisição do Ministro da Justiça ou de representação do ofendido.', 'C',
  'Art. 24, caput: mesmo **condicionada**, a ação segue **pública** e o titular é o **MP**.',
  lei=[(CPP + '24', 'Nos crimes de ação pública, esta será promovida por denúncia do Ministério Público', 'qualidade para representá-lo', 'CPP, art. 24, caput')],
  kw=['condicionada', 'requisição do Ministro da Justiça'])
I(P, 1, 'Irretratabilidade da representação',
  'A representação é retratável até a sentença de primeiro grau.', 'E',
  'Art. 25: a representação é **irretratável depois de oferecida a denúncia**. Na Lei Maria da Penha, a renúncia só perante o juiz, em audiência, antes do **recebimento** da denúncia (art. 16).',
  lei=[(CPP + '25', 'A representação será irretratável, depois de oferecida a denúncia', None, 'CPP, art. 25')],
  exc=['Lei 11.340/2006, art. 16: renúncia à representação só em audiência, perante o juiz, antes do recebimento da denúncia, ouvido o MP'],
  peg='Estender a retratação até a sentença.',
  kw=['irretratável', 'oferecida a denúncia'])
I(P, 1, 'Forma da representação',
  'A representação exige forma solene, devendo ser feita por escrito e com assinatura reconhecida, sob pena de nulidade.', 'E',
  'Art. 39: a representação pode ser **escrita ou oral**, ao juiz, ao MP ou à **autoridade policial**. A jurisprudência dispensa formalismo: basta a vontade inequívoca da vítima.',
  lei=[(CPP + '39', 'O direito de representação poderá ser exercido, pessoalmente ou por procurador com poderes especiais', 'ou à autoridade policial', 'CPP, art. 39, caput')],
  peg='Exigir forma solene onde a lei admite declaração oral.',
  kw=['representação', 'escrita ou oral'])
I(P, 1, 'Decadência',
  'Salvo disposição em contrário, o ofendido decairá do direito de queixa ou de representação se não o exercer em seis meses, contados da data do fato.', 'E',
  'Art. 38, caput: o prazo de seis meses conta-se do dia em que o ofendido **vier a saber quem é o autor** do crime, e não da data do fato.',
  lei=[(CPP + '38', 'decairá no direito de queixa ou de representação, se não o exercer dentro do prazo de seis meses', 'quem é o autor do crime', 'CPP, art. 38, caput')],
  peg='Trocar o termo inicial (ciência da autoria) pela data do fato.',
  kw=['decadência', 'seis meses'])
I(P, 1, 'Decadência na violência doméstica',
  'Nos crimes praticados no âmbito de violência doméstica e familiar contra a mulher, o prazo decadencial para a queixa ou a representação é o mesmo de seis meses dos demais crimes.', 'E',
  'Desde a **Lei 15.438/2026**, o art. 38, § 2º, fixa **12 meses** para a ofendida em violência doméstica e familiar.',
  lei=[(CPP + '38', 'Nos crimes praticados no âmbito de violência doméstica e familiar contra a mulher, a ofendida decairá', 'no prazo de 12 (doze) meses', 'CPP, art. 38, § 2º')],
  peg='Ignorar a mudança de 2026.',
  kw=['12 meses', 'Lei 15.438/2026'])
I(P, 1, 'Sucessão processual',
  'No caso de morte do ofendido ou quando declarado ausente por decisão judicial, o direito de oferecer queixa ou de prosseguir na ação passará ao cônjuge, ascendente, descendente ou irmão.', 'C',
  'Art. 31: o **CADI** (cônjuge, ascendente, descendente, irmão), nessa ordem de preferência (art. 36).',
  lei=[(CPP + '31', 'No caso de morte do ofendido ou quando declarado ausente por decisão judicial', 'ascendente, descendente ou irmão', 'CPP, art. 31')],
  exc=['Ação privada personalíssima (CP, art. 236, par. ún.): não há sucessão; a morte do ofendido extingue a punibilidade'],
  kw=['CADI', 'sucessão'])
I(P, 1, 'Indivisibilidade',
  'Na ação penal privada, a queixa contra qualquer dos autores do crime obrigará ao processo de todos, e o Ministério Público velará pela sua indivisibilidade.', 'C',
  'Art. 48: **indivisibilidade**. A renúncia em relação a um se estende a todos (art. 49).',
  lei=[(CPP + '48', 'A queixa contra qualquer dos autores do crime obrigará ao processo de todos', 'velará pela sua indivisibilidade', 'CPP, art. 48')],
  kw=['indivisibilidade', 'queixa'])
I(P, 1, 'Perdão do ofendido',
  'O perdão concedido a um dos querelados aproveita a todos, inclusive ao que o recusar.', 'E',
  'Art. 51: aproveita a todos, **sem efeito em relação ao que o recusar** (o perdão é ato **bilateral**).',
  lei=[(CPP + '51', 'O perdão concedido a um dos querelados aproveitará a todos', 'em relação ao que o recusar', 'CPP, art. 51')],
  peg='Esquecer que o perdão depende de aceitação.',
  kw=['perdão', 'bilateral'])
I(P, 1, 'Renúncia',
  'A renúncia ao direito de queixa é ato bilateral e só produz efeitos se aceita pelo querelado.', 'E',
  'A **renúncia** é **unilateral** e anterior à ação; pode ser expressa ou tácita (CP, art. 104). Bilateral é o **perdão** (depois de iniciada a ação).',
  lei=[(CP + '104', 'O direito de queixa não pode ser exercido quando renunciado expressa ou tacitamente', None, 'CP, art. 104, caput')],
  peg='Trocar as características da renúncia e do perdão.',
  kw=['renúncia', 'unilateral'])
I(P, 1, 'Perempção',
  'Considera-se perempta a ação penal privada quando, iniciada esta, o querelante deixar de promover o andamento do processo durante 60 dias seguidos.', 'E',
  'Art. 60, I: **30 dias seguidos**. (60 dias é o prazo da habilitação dos sucessores — art. 60, II.)',
  lei=[(CPP + '60', 'quando, iniciada esta, o querelante deixar de promover o andamento do processo durante 30 dias seguidos', None, 'CPP, art. 60, I')],
  peg='Trocar 30 por 60 dias.',
  kw=['perempção', '30 dias'])
I(P, 1, 'Requisitos da denúncia',
  'A denúncia ou queixa conterá a exposição do fato criminoso, com todas as suas circunstâncias, a qualificação do acusado ou esclarecimentos pelos quais se possa identificá-lo, a classificação do crime e, sempre, o rol de testemunhas, sob pena de inépcia.', 'E',
  'Art. 41: o rol de testemunhas entra **"quando necessário"**; não é requisito obrigatório.',
  lei=[(CPP + '41', 'A denúncia ou queixa conterá a exposição do fato criminoso', 'quando necessário, o rol das testemunhas', 'CPP, art. 41')],
  peg='Trocar "quando necessário" por "sempre".',
  kw=['rol de testemunhas', 'quando necessário'])
# --- CPP-4.1 · Rodada 2
I(P, 2, 'Queixa por procurador',
  'A queixa poderá ser dada por procurador com poderes gerais para o foro, dispensada a menção do fato criminoso no mandato.', 'E',
  'Art. 44: exigem-se **poderes especiais** e a **menção do fato criminoso** no instrumento.',
  lei=[(CPP + '44', 'A queixa poderá ser dada por procurador com poderes especiais', 'a menção do fato criminoso', 'CPP, art. 44')],
  peg='Bastar procuração ad judicia genérica.',
  kw=['poderes especiais', 'menção do fato criminoso'])
I(P, 2, 'Representante e ofendido',
  'Os direitos de queixa e de representação podem ser exercidos, independentemente, pelo ofendido ou por seu representante legal.', 'C',
  '**Súmula 594/STF**: prazos **independentes** para o ofendido (ao completar 18 anos) e para o representante.',
  juris=[J['STF594']],
  kw=['Súmula 594', 'prazos independentes'])
I(P, 2, 'Personalíssima',
  'Na ação penal privada personalíssima, morrendo o ofendido, o direito de queixa passa ao cônjuge, ascendente, descendente ou irmão.', 'E',
  'Na **personalíssima** (hoje só o CP, art. 236 — induzimento a erro essencial no casamento), **não há sucessão**: só o contraente enganado pode agir.',
  lei=[(CP + '236', 'A ação penal depende de queixa do contraente enganado', 'anule o casamento', 'CP, art. 236, par. ún.')],
  peg='Aplicar à personalíssima a sucessão do art. 31.',
  kw=['personalíssima', 'contraente enganado'])
I(P, 2, 'Perdão e trânsito em julgado',
  'O perdão do ofendido é admissível mesmo depois que passa em julgado a sentença condenatória.', 'E',
  'CP, art. 106, § 2º: **não** é admissível o perdão **depois do trânsito em julgado** da condenação.',
  lei=[(CP + '106', 'Não é admissível o perdão depois que passa em julgado a sentença condenatória', None, 'CP, art. 106, § 2º')],
  peg='Admitir perdão após o trânsito.',
  kw=['perdão', 'trânsito em julgado'])
I(P, 2, 'Justa causa',
  'A justa causa para a ação penal corresponde ao lastro probatório mínimo — prova da materialidade e indícios de autoria —, e sua falta leva à rejeição da denúncia.', 'C',
  'Art. 395, III. A **justa causa** é suporte probatório mínimo; sua falta também autoriza **trancamento** por HC (art. 648, I).',
  lei=[(CPP + '395', 'faltar justa causa para o exercício da ação penal', None, 'CPP, art. 395, III')],
  kw=['justa causa', 'lastro probatório mínimo'])
I(P, 2, 'Trancamento e sentença superveniente',
  'A superveniência de sentença condenatória não prejudica o habeas corpus que pede o trancamento da ação penal por falta de justa causa.', 'E',
  '**Súmula 648/STJ**: a sentença condenatória **prejudica** o pedido de trancamento por falta de justa causa.',
  juris=[J['S648']],
  peg='Inverter a Súmula 648.',
  kw=['Súmula 648', 'trancamento'])
I(P, 2, 'Prazo decadencial e subsidiária',
  'Na ação privada subsidiária, o prazo de seis meses conta-se do dia em que se esgotar o prazo para o oferecimento da denúncia.', 'C',
  'Art. 38, caput, parte final. A decadência da subsidiária **não extingue a punibilidade**: o MP pode denunciar enquanto não prescrito o crime.',
  lei=[(CPP + '38', 'do dia em que se esgotar o prazo para o oferecimento da denúncia', None, 'CPP, art. 38, caput')],
  kw=['subsidiária', 'decadência imprópria'])

# ======================= CPP-4.2 · Acordo de não persecução penal =======================
P = 'DBA26-CPP-4.2'
I(P, 1, 'Requisitos do ANPP',
  'Não sendo caso de arquivamento e tendo o investigado confessado formal e circunstancialmente a prática de infração penal sem violência ou grave ameaça e com pena mínima inferior a 4 anos, o MP poderá propor acordo de não persecução penal, desde que necessário e suficiente para reprovação e prevenção do crime.', 'C',
  'Art. 28-A, caput: **confissão formal e circunstanciada**, **sem violência ou grave ameaça**, **pena mínima inferior a 4 anos**.',
  lei=[(CPP + '28-A', 'Não sendo caso de arquivamento e tendo o investigado confessado formal e circunstancialmente', 'necessário e suficiente para reprovação e prevenção do crime', 'CPP, art. 28-A, caput')],
  kw=['ANPP', 'pena mínima inferior a 4 anos'])
I(P, 1, 'Pena mínima igual a quatro anos',
  'Cabe ANPP em crime sem violência ou grave ameaça cuja pena mínima seja de 4 anos.', 'E',
  'A pena mínima deve ser **inferior** a 4 anos. Com mínimo de 4, não cabe.',
  lei=[(CPP + '28-A', 'com pena mínima inferior a 4 (quatro) anos', None, 'CPP, art. 28-A, caput')],
  peg='Trocar "inferior" por "igual ou inferior".',
  kw=['inferior a 4 anos', 'ANPP'])
I(P, 1, 'Causas de aumento e diminuição',
  'Para aferir a pena mínima no ANPP, desconsideram-se as causas de aumento e de diminuição de pena.', 'E',
  'Art. 28-A, § 1º: **consideram-se** as causas de aumento e diminuição aplicáveis ao caso concreto.',
  lei=[(CPP + '28-A', 'serão consideradas as causas de aumento e diminuição aplicáveis ao caso concreto', None, 'CPP, art. 28-A, § 1º')],
  peg='Inverter o § 1º.',
  kw=['causas de aumento e diminuição', 'pena mínima'])
I(P, 1, 'Vedação — transação penal',
  'Não cabe ANPP se for cabível transação penal de competência dos Juizados Especiais Criminais.', 'C',
  'Art. 28-A, § 2º, I: a **transação** prefere ao ANPP (subsidiariedade).',
  lei=[(CPP + '28-A', 'se for cabível transação penal de competência dos Juizados Especiais Criminais', None, 'CPP, art. 28-A, § 2º, I')],
  kw=['transação penal', 'subsidiariedade'])
I(P, 1, 'Vedação — violência doméstica',
  'O ANPP pode ser oferecido nos crimes praticados no âmbito de violência doméstica ou familiar, desde que sem violência física, como na ameaça.', 'E',
  'Art. 28-A, § 2º, IV: vedado em **violência doméstica ou familiar** e nos crimes contra a mulher por razões da condição de sexo feminino, **em favor do agressor**.',
  lei=[(CPP + '28-A', 'nos crimes praticados no âmbito de violência doméstica ou familiar', 'em favor do agressor', 'CPP, art. 28-A, § 2º, IV')],
  peg='Criar exceção para crimes de VD sem violência física.',
  kw=['violência doméstica', 'vedação'])
I(P, 1, 'Formalização e homologação',
  'O ANPP será formalizado por escrito e firmado pelo MP e pelo investigado, dispensada a assinatura do defensor, e o juiz pode homologá-lo sem audiência.', 'E',
  'Art. 28-A, §§ 3º e 4º: firmado também **pelo defensor**, e a homologação exige **audiência** para verificar voluntariedade e legalidade.',
  lei=[(CPP + '28-A', 'O acordo de não persecução penal será formalizado por escrito', 'pelo investigado e por seu defensor', 'CPP, art. 28-A, § 3º'),
       (CPP + '28-A', 'Para a homologação do acordo de não persecução penal, será realizada audiência', 'e sua legalidade', 'CPP, art. 28-A, § 4º')],
  peg='Dispensar defensor e audiência.',
  kw=['homologação', 'voluntariedade'])
I(P, 1, 'Execução do ANPP',
  'Homologado o ANPP, o juiz que o homologou executará as condições pactuadas.', 'E',
  'Art. 28-A, § 6º: os autos voltam ao **MP**, que inicia a execução perante o **juízo de execução penal**.',
  lei=[(CPP + '28-A', 'Homologado judicialmente o acordo de não persecução penal, o juiz devolverá os autos ao Ministério Público', 'juízo de execução penal', 'CPP, art. 28-A, § 6º')],
  peg='Atribuir a execução ao juiz da homologação.',
  kw=['juízo de execução penal', 'execução'])
I(P, 1, 'Antecedentes',
  'A celebração e o cumprimento do ANPP constarão da certidão de antecedentes criminais do investigado.', 'E',
  'Art. 28-A, § 12: **não constarão**, salvo para impedir novo benefício em 5 anos (§ 2º, III).',
  lei=[(CPP + '28-A', 'A celebração e o cumprimento do acordo de não persecução penal não constarão de certidão de antecedentes criminais', None, 'CPP, art. 28-A, § 12')],
  peg='Afirmar registro em antecedentes.',
  kw=['antecedentes', '5 anos'])
# --- CPP-4.2 · Rodada 2
I(P, 2, 'Recusa do MP',
  'No caso de recusa do Ministério Público em propor o ANPP, o investigado poderá requerer a remessa dos autos a órgão superior, na forma do art. 28 do CPP.', 'C',
  'Art. 28-A, § 14: **revisão ministerial** da recusa. O juiz não pode impor o acordo nem ofertá-lo de ofício.',
  lei=[(CPP + '28-A', 'No caso de recusa, por parte do Ministério Público, em propor o acordo de não persecução penal', 'na forma do art. 28 deste Código', 'CPP, art. 28-A, § 14')],
  kw=['recusa', 'órgão superior'])
I(P, 2, 'ANPP em processo em curso',
  'Segundo o STF, nas investigações e ações penais iniciadas a partir do julgamento do HC 185.913, a proposta de ANPP ou a motivação para o seu não oferecimento devem ser apresentadas antes do recebimento da denúncia, ressalvada a propositura no curso da ação, se for o caso.', 'C',
  'Tese do **HC 185.913** (Plenário, 18/09/2024).',
  juris=[J['HC185913']],
  kw=['HC 185.913', 'antes do recebimento da denúncia'])
I(P, 2, 'Confissão e retroatividade',
  'Segundo o STF, nos processos em andamento quando entrou em vigor a Lei 13.964/2019, o ANPP só é cabível se o réu já houver confessado até aquele momento.', 'E',
  'O STF admitiu o ANPP **mesmo se ausente confissão** até aquele momento, desde que pedido **antes do trânsito em julgado** (HC 185.913).',
  juris=[J['HC185913']],
  peg='Exigir confissão anterior, dispensada pelo STF.',
  kw=['confissão', 'antes do trânsito em julgado'])
I(P, 2, 'Descumprimento',
  'Descumpridas as condições do ANPP, o MP deverá comunicar ao juízo, para fins de rescisão e posterior oferecimento de denúncia, e o descumprimento pode justificar o não oferecimento de suspensão condicional do processo.', 'C',
  'Art. 28-A, §§ 10 e 11.',
  lei=[(CPP + '28-A', 'Descumpridas quaisquer das condições estipuladas no acordo de não persecução penal', 'posterior oferecimento de denúncia', 'CPP, art. 28-A, § 10')],
  kw=['rescisão', 'descumprimento'])
I(P, 2, 'Cumprimento integral',
  'Cumprido integralmente o ANPP, o próprio Ministério Público declarará a extinção da punibilidade.', 'E',
  'Art. 28-A, § 13: quem decreta a **extinção da punibilidade** é o **juízo competente**.',
  lei=[(CPP + '28-A', 'Cumprido integralmente o acordo de não persecução penal, o juízo competente decretará a extinção de punibilidade', None, 'CPP, art. 28-A, § 13')],
  peg='Dar ao MP ato jurisdicional.',
  kw=['extinção de punibilidade', 'cumprimento integral'])
I(P, 2, 'Condições abusivas',
  'Se o juiz considerar inadequadas, insuficientes ou abusivas as condições do ANPP, poderá ele mesmo reformulá-las e homologar o acordo com as novas condições.', 'E',
  'Art. 28-A, § 5º: o juiz **devolve os autos ao MP** para reformular a proposta, com concordância do investigado e do defensor. Não reescreve o acordo.',
  lei=[(CPP + '28-A', 'Se o juiz considerar inadequadas, insuficientes ou abusivas as condições', 'reformulada a proposta de acordo', 'CPP, art. 28-A, § 5º')],
  peg='Dar ao juiz o papel de parte no acordo.',
  kw=['devolverá os autos', 'reformulada a proposta'])

# ======================= CPP-4.2-B2 · Sujeitos do processo =======================
P = 'DBA26-CPP-4.2-B2'
I(P, 1, 'Impedimento do juiz',
  'O juiz não poderá exercer jurisdição no processo em que tiver funcionado seu cônjuge ou parente, consanguíneo ou afim, em linha reta ou colateral até o terceiro grau, inclusive, como defensor, órgão do MP, autoridade policial, auxiliar da justiça ou perito.', 'C',
  'Art. 252, I: **impedimento** (rol tido por taxativo; vício objetivo).',
  lei=[(CPP + '252', 'O juiz não poderá exercer jurisdição no processo em que:', None, 'CPP, art. 252, caput')],
  kw=['impedimento', 'terceiro grau'])
I(P, 1, 'Suspeição — amizade e inimizade',
  'O juiz dar-se-á por suspeito, e, se não o fizer, poderá ser recusado por qualquer das partes, se for amigo íntimo ou inimigo capital de qualquer delas.', 'C',
  'Art. 254, I: **suspeição** (vínculo subjetivo com as partes).',
  lei=[(CPP + '254', 'se for amigo íntimo ou inimigo capital de qualquer deles', None, 'CPP, art. 254, I')],
  kw=['suspeição', 'amigo íntimo'])
I(P, 1, 'Suspeição provocada',
  'A suspeição deve ser reconhecida mesmo quando a parte injuriar o juiz de propósito para criá-la.', 'E',
  'Art. 256: a suspeição **não poderá ser declarada** quando a parte injuriar o juiz ou de propósito der motivo para criá-la.',
  lei=[(CPP + '256', 'A suspeição não poderá ser declarada nem reconhecida', 'de propósito der motivo para criá-la', 'CPP, art. 256')],
  peg='Premiar a suspeição provocada.',
  kw=['suspeição provocada', 'não poderá ser declarada'])
I(P, 1, 'Funções do MP',
  'Ao Ministério Público cabe promover, privativamente, a ação penal pública e fiscalizar a execução da lei.', 'C',
  'Art. 257, I e II, do CPP.',
  lei=[(CPP + '257', 'Ao Ministério Público cabe:', 'fiscalizar a execução da lei', 'CPP, art. 257')],
  kw=['Ministério Público', 'fiscalizar a execução da lei'])
I(P, 1, 'Defesa técnica obrigatória',
  'O acusado ausente ou foragido pode ser processado sem defensor, por ter renunciado tacitamente à defesa.', 'E',
  'Art. 261: **nenhum acusado**, ainda que ausente ou foragido, será processado ou julgado **sem defensor**.',
  lei=[(CPP + '261', 'Nenhum acusado, ainda que ausente ou foragido, será processado ou julgado sem defensor', None, 'CPP, art. 261, caput')],
  peg='Admitir renúncia à defesa técnica.',
  kw=['defesa técnica', 'sem defensor'])
I(P, 1, 'Abandono do processo pelo defensor',
  'O defensor que abandonar o processo sem justo motivo, previamente comunicado ao juiz, fica sujeito à multa de 10 a 100 salários mínimos aplicada pelo próprio juiz.', 'E',
  'Desde a **Lei 14.752/2023**, o art. 265 prevê **infração disciplinar** perante o órgão correicional competente; a multa foi retirada.',
  lei=[(CPP + '265', 'O defensor não poderá abandonar o processo sem justo motivo', 'perante o órgão correicional competente', 'CPP, art. 265, caput')],
  peg='Repetir a multa da redação antiga.',
  kw=['abandono', 'infração disciplinar'])
I(P, 1, 'Assistente de acusação',
  'Em todos os termos da ação pública, poderá intervir como assistente do MP o ofendido ou seu representante legal, ou, na falta, o cônjuge, ascendente, descendente ou irmão.', 'C',
  'Art. 268 c/c art. 31. O assistente é admitido enquanto não transitar a sentença e recebe a causa no estado em que estiver (art. 269).',
  lei=[(CPP + '268', 'Em todos os termos da ação pública, poderá intervir, como assistente do Ministério Público', 'o ofendido ou seu representante legal', 'CPP, art. 268')],
  kw=['assistente de acusação', 'ofendido'])
I(P, 1, 'Corréu como assistente',
  'O corréu no mesmo processo pode intervir como assistente do MP se também for vítima do fato.', 'E',
  'Art. 270: o **corréu** no mesmo processo **não poderá** intervir como assistente.',
  lei=[(CPP + '270', 'no mesmo processo não poderá intervir como assistente do Ministério Público', None, 'CPP, art. 270')],
  peg='Admitir o corréu como assistente.',
  kw=['corréu', 'assistente'])
I(P, 1, 'Recurso contra admissão do assistente',
  'Do despacho que admitir ou não o assistente cabe recurso em sentido estrito.', 'E',
  'Art. 273: **não caberá recurso**; o pedido e a decisão devem constar dos autos (admite-se mandado de segurança).',
  lei=[(CPP + '273', 'Do despacho que admitir, ou não, o assistente, não caberá recurso', None, 'CPP, art. 273')],
  peg='Inventar RESE para a admissão do assistente.',
  kw=['assistente', 'não caberá recurso'])
# --- CPP-4.2-B2 · Rodada 2
I(P, 2, 'Assistente e recurso extraordinário',
  'O assistente do MP pode recorrer, inclusive extraordinariamente, nos casos dos arts. 584, § 1º, e 598 do CPP, mas não pode recorrer extraordinariamente de decisão concessiva de habeas corpus.', 'C',
  '**Súmulas 210 e 208/STF**. O prazo do assistente para recorrer supletivamente corre logo após o do MP (**Súmula 448/STF**).',
  juris=[J['STF210'], J['STF208'], J['STF448']],
  kw=['assistente', 'recurso supletivo'])
I(P, 2, 'Condução coercitiva para interrogatório',
  'O juiz pode determinar a condução coercitiva do réu para o interrogatório, nos termos do art. 260 do CPP, quando ele não atender à intimação.', 'E',
  'STF, **ADPFs 395 e 444** (14/06/2018): a condução coercitiva **para interrogatório não foi recepcionada**. Para atos que dependam da presença física (ex.: reconhecimento), a discussão é outra.',
  lei=[(CPP + '260', 'Se o acusado não atender à intimação para o interrogatório', 'a autoridade poderá mandar conduzi-lo à sua presença', 'CPP, art. 260, caput')],
  juris=[J['ADPF444']],
  peg='Aplicar a letra do art. 260 sem o julgamento do STF.',
  kw=['condução coercitiva', 'ADPF 444'])
I(P, 2, 'MP e impedimentos',
  'Os órgãos do MP não funcionarão nos processos em que o juiz ou qualquer das partes for seu cônjuge ou parente até o terceiro grau, estendendo-se a eles, no que for aplicável, as regras de suspeição e impedimento dos juízes.', 'C',
  'Art. 258 do CPP.',
  lei=[(CPP + '258', 'Os órgãos do Ministério Público não funcionarão nos processos em que o juiz ou qualquer das partes for seu cônjuge', 'até o terceiro grau, inclusive', 'CPP, art. 258')],
  kw=['MP', 'impedimento'])
I(P, 2, 'Identidade física incerta',
  'A impossibilidade de identificar o acusado com seu verdadeiro nome impede o prosseguimento da ação penal, ainda que certa a sua identidade física.', 'E',
  'Art. 259: **não retardará** a ação penal quando **certa a identidade física**.',
  lei=[(CPP + '259', 'A impossibilidade de identificação do acusado com o seu verdadeiro nome', 'quando certa a identidade física', 'CPP, art. 259')],
  peg='Paralisar a ação por falta de qualificação completa.',
  kw=['identidade física', 'qualificação'])
I(P, 2, 'Intérpretes e peritos',
  'Os intérpretes são, para todos os efeitos, equiparados aos peritos, e o perito, ainda que não oficial, está sujeito à disciplina judiciária.', 'C',
  'Arts. 281 e 275 do CPP.',
  lei=[(CPP + '281', 'Os intérpretes são, para todos os efeitos, equiparados aos peritos', None, 'CPP, art. 281'),
       (CPP + '275', 'O perito, ainda quando não oficial, estará sujeito à disciplina judiciária', None, 'CPP, art. 275')],
  kw=['intérpretes', 'peritos'])

# ======================= CPP-5 · Juizados Especiais Criminais =======================
P = 'DBA26-CPP-5'
I(P, 1, 'Menor potencial ofensivo',
  'Consideram-se infrações penais de menor potencial ofensivo as contravenções penais e os crimes a que a lei comine pena mínima não superior a 2 anos.', 'E',
  'Art. 61 da Lei 9.099/1995: o critério é a pena **máxima** não superior a **2 anos**, cumulada ou não com multa.',
  lei=[(JE + '61', 'Consideram-se infrações penais de menor potencial ofensivo', 'cumulada ou não com multa', 'Lei 9.099/1995, art. 61')],
  peg='Trocar pena máxima por mínima.',
  kw=['menor potencial ofensivo', '2 anos'])
I(P, 1, 'Critérios do JECrim',
  'O processo perante o Juizado Especial Criminal orienta-se pelos critérios da oralidade, informalidade, economia processual e celeridade, objetivando, sempre que possível, a reparação dos danos e a aplicação de pena não privativa de liberdade.', 'C',
  'Art. 62 da Lei 9.099/1995 (o rol inclui também a **simplicidade**, por remissão ao art. 2º).',
  lei=[(JE + '62', 'O processo perante o Juizado Especial orientar-se-á pelos critérios da oralidade', 'pena não privativa de liberdade', 'Lei 9.099/1995, art. 62')],
  kw=['oralidade', 'informalidade'])
I(P, 1, 'Flagrante no JECrim',
  'Ao autor de infração de menor potencial ofensivo que, após a lavratura do termo circunstanciado, for imediatamente encaminhado ao juizado ou assumir o compromisso de a ele comparecer, não se imporá prisão em flagrante nem se exigirá fiança.', 'C',
  'Art. 69, par. ún.: há **captura**, mas não se **lavra auto de prisão** nem se exige fiança se houver o compromisso.',
  lei=[(JE + '69', 'Ao autor do fato que, após a lavratura do termo', 'nem se exigirá fiança', 'Lei 9.099/1995, art. 69, par. ún.')],
  kw=['não se imporá prisão em flagrante', 'compromisso'])
I(P, 1, 'Composição civil',
  'Nos crimes de ação pública incondicionada, o acordo de composição civil homologado acarreta a renúncia ao direito de representação.', 'E',
  'Art. 74, par. ún.: a composição gera renúncia apenas na ação **privada** ou **pública condicionada à representação**.',
  lei=[(JE + '74', 'Tratando-se de ação penal de iniciativa privada ou de ação penal pública condicionada à representação', 'renúncia ao direito de queixa ou representação', 'Lei 9.099/1995, art. 74, par. ún.')],
  peg='Estender o efeito à ação incondicionada.',
  kw=['composição civil', 'renúncia'])
I(P, 1, 'Transação penal — impedimento',
  'Não se admite a transação penal se o agente tiver sido beneficiado anteriormente, no prazo de cinco anos, pela aplicação de pena restritiva ou multa por transação.', 'C',
  'Art. 76, § 2º, II, da Lei 9.099/1995.',
  lei=[(JE + '76', 'ter sido o agente beneficiado anteriormente, no prazo de cinco anos', None, 'Lei 9.099/1995, art. 76, § 2º, II')],
  kw=['transação penal', 'cinco anos'])
I(P, 1, 'Transação e coisa julgada',
  'A homologação da transação penal faz coisa julgada material, de modo que, descumpridas as condições, resta apenas executar a pena acordada.', 'E',
  '**SV 35**: **não** faz coisa julgada material; descumpridas as cláusulas, retoma-se a situação anterior e o MP pode **denunciar** ou requisitar inquérito.',
  juris=[J['SV35']],
  peg='Inverter a Súmula Vinculante 35.',
  kw=['SV 35', 'coisa julgada material'])
I(P, 1, 'Suspensão condicional do processo',
  'Nos crimes em que a pena mínima cominada for igual ou inferior a um ano, abrangidos ou não pela Lei 9.099/1995, o MP, ao oferecer a denúncia, poderá propor a suspensão do processo por dois a quatro anos.', 'C',
  'Art. 89: cabe também fora do JECrim; durante a suspensão **não corre a prescrição** (§ 6º).',
  lei=[(JE + '89', 'Nos crimes em que a pena mínima cominada for igual ou inferior a um ano', 'por dois a quatro anos', 'Lei 9.099/1995, art. 89, caput')],
  kw=['suspensão condicional do processo', 'pena mínima'])
I(P, 1, 'Maria da Penha e despenalizadores',
  'A suspensão condicional do processo e a transação penal aplicam-se aos delitos sujeitos ao rito da Lei Maria da Penha, desde que a pena máxima não supere dois anos.', 'E',
  '**Súmula 536/STJ** e art. 41 da Lei 11.340/2006: **não se aplicam**, independentemente da pena.',
  lei=[('L11340:41', 'independentemente da pena prevista, não se aplica a Lei nº 9.099', None, 'Lei 11.340/2006, art. 41')],
  juris=[J['S536']],
  peg='Admitir benefícios da Lei 9.099/1995 na violência doméstica.',
  kw=['Súmula 536', 'Maria da Penha'])
# --- CPP-5 · Rodada 2
I(P, 2, 'Citação por edital no JECrim',
  'No Juizado Especial Criminal, não encontrado o acusado para citação pessoal, procede-se à citação por edital.', 'E',
  'Art. 66, par. ún.: as peças vão ao **juízo comum**. Não há citação por edital no JECrim. A complexidade do caso também desloca o feito (art. 77, § 2º).',
  lei=[(JE + '66', 'Não encontrado o acusado para ser citado, o Juiz encaminhará as peças existentes ao Juízo comum', None, 'Lei 9.099/1995, art. 66, par. ún.')],
  peg='Admitir edital no rito sumaríssimo.',
  kw=['juízo comum', 'citação por edital'])
I(P, 2, 'Apelação no JECrim',
  'Da sentença no JECrim cabe apelação no prazo de 5 dias, julgada pelo Tribunal de Justiça.', 'E',
  'Lei 9.099/1995, art. 82: apelação em **10 dias**, julgada por **turma recursal** de três juízes de primeiro grau.',
  lei=[(JE + '82', 'Da decisão de rejeição da denúncia ou queixa e da sentença caberá apelação', 'reunidos na sede do Juizado', 'Lei 9.099/1995, art. 82, caput')],
  peg='Importar o prazo e o órgão do CPP.',
  kw=['apelação', 'turma recursal'])
I(P, 2, 'Desclassificação e sursis processual',
  'É cabível a suspensão condicional do processo na desclassificação do crime e na procedência parcial da pretensão punitiva.', 'C',
  '**Súmula 337/STJ**.',
  juris=[J['S337']],
  kw=['Súmula 337', 'desclassificação'])
I(P, 2, 'Justiça Militar',
  'As disposições da Lei 9.099/1995 aplicam-se no âmbito da Justiça Militar quando a infração for de menor potencial ofensivo.', 'E',
  'Art. 90-A: **não se aplicam** no âmbito da Justiça Militar.',
  lei=[(JE + '90-A', 'As disposições desta Lei não se aplicam no âmbito da Justiça Militar', None, 'Lei 9.099/1995, art. 90-A')],
  peg='Levar a Lei 9.099/1995 à Justiça Militar.',
  kw=['Justiça Militar', 'art. 90-A'])
I(P, 2, 'Representação na audiência preliminar',
  'O não oferecimento da representação na audiência preliminar implica decadência imediata do direito.', 'E',
  'Art. 75, par. ún.: **não implica decadência**; a representação pode ser oferecida no prazo legal.',
  lei=[(JE + '75', 'O não oferecimento da representação na audiência preliminar não implica decadência do direito', None, 'Lei 9.099/1995, art. 75, par. ún.')],
  peg='Antecipar a decadência para a audiência.',
  kw=['representação', 'decadência'])
I(P, 2, 'Competência territorial do JECrim',
  'A competência do Juizado Especial Criminal é determinada pelo lugar em que foi praticada a infração penal.', 'C',
  'Art. 63 da Lei 9.099/1995 (expressão interpretada pela doutrina como teoria da **ubiquidade** ou da atividade, conforme a corrente).',
  lei=[(JE + '63', 'A competência do Juizado será determinada pelo lugar em que foi praticada a infração penal', None, 'Lei 9.099/1995, art. 63')],
  kw=['lugar em que foi praticada', 'competência'])

# ======================= CPP-6 · TCO; atos processuais: forma, lugar e tempo =======================
P = 'DBA26-CPP-6'
I(P, 1, 'Termo circunstanciado',
  'A autoridade policial que tomar conhecimento de infração de menor potencial ofensivo lavrará termo circunstanciado e o encaminhará imediatamente ao Juizado, com o autor do fato e a vítima, providenciando as requisições dos exames periciais necessários.', 'C',
  'Art. 69, caput, da Lei 9.099/1995: o **TCO** substitui o inquérito nas infrações de menor potencial.',
  lei=[(JE + '69', 'A autoridade policial que tomar conhecimento da ocorrência lavrará termo circunstanciado', 'exames periciais necessários', 'Lei 9.099/1995, art. 69, caput')],
  kw=['termo circunstanciado', 'menor potencial ofensivo'])
I(P, 1, 'TCO e exame de corpo de delito',
  'No termo circunstanciado, o exame de corpo de delito é dispensado em qualquer caso, bastando o relato da vítima.', 'E',
  'A autoridade requisita os **exames periciais necessários** (art. 69). Para a denúncia oral, o exame pode ser **suprido por boletim médico ou prova equivalente** (art. 77, § 1º) — o que não equivale a dispensa total.',
  lei=[(JE + '77', 'prescindir-se-á do exame do corpo de delito quando a materialidade do crime estiver aferida por boletim médico ou prova equivalente', None, 'Lei 9.099/1995, art. 77, § 1º')],
  peg='Trocar "suprido por boletim médico" por "dispensado em qualquer caso".',
  kw=['boletim médico', 'materialidade'])
I(P, 1, 'Publicidade dos atos',
  'As audiências, sessões e atos processuais serão, em regra, públicos e se realizarão nas sedes dos juízos e tribunais, em dia e hora certos ou previamente designados.', 'C',
  'Art. 792 do CPP: **lugar** e **publicidade** dos atos. O § 1º admite restringir a publicidade em caso de escândalo, inconveniente grave ou perigo de perturbação da ordem.',
  lei=[(CPP + '792', 'As audiências, sessões e os atos processuais serão, em regra, públicos', 'nas sedes dos juízos e tribunais', 'CPP, art. 792, caput')],
  kw=['publicidade', 'sedes dos juízos'])
I(P, 1, 'Contagem de prazos',
  'Na contagem dos prazos processuais penais, computa-se o dia do começo e exclui-se o do vencimento.', 'E',
  'Art. 798, § 1º: **não se computa o dia do começo**, incluindo-se o do **vencimento**. (Prazo penal, como a decadência, conta o dia do começo — CP, art. 10.)',
  lei=[(CPP + '798', 'Não se computará no prazo o dia do começo, incluindo-se, porém, o do vencimento', None, 'CPP, art. 798, § 1º')],
  peg='Inverter a regra processual (ou trocá-la pela penal).',
  kw=['dia do começo', 'vencimento'])
I(P, 1, 'Continuidade dos prazos',
  'Os prazos processuais penais são contínuos e peremptórios, não se interrompendo por férias, domingo ou feriado, e o prazo que terminar em domingo ou feriado considera-se prorrogado até o dia útil imediato.', 'C',
  'Art. 798, caput e § 3º.',
  lei=[(CPP + '798', 'Todos os prazos correrão em cartório e serão contínuos e peremptórios', 'domingo ou dia feriado', 'CPP, art. 798, caput')],
  kw=['contínuos e peremptórios', 'dia útil imediato'])
I(P, 1, 'Termo inicial dos prazos',
  'No processo penal, contam-se os prazos da data da juntada aos autos do mandado ou da carta precatória, e não da intimação.', 'E',
  '**Súmula 710/STF**: contam-se da **data da intimação**, e não da juntada.',
  juris=[J['STF710']],
  peg='Importar a regra do processo civil (juntada).',
  kw=['Súmula 710', 'data da intimação'])
# --- CPP-6 · Rodada 2
I(P, 2, 'Suspensão de prazos no fim do ano',
  'Suspende-se o curso do prazo processual penal entre 20 de dezembro e 20 de janeiro, salvo, entre outros casos, nos processos que envolvam réus presos, vinculados a essas prisões.', 'C',
  'Art. 798-A, I, do CPP (Lei 14.365/2022).',
  lei=[(CPP + '798-A', 'Suspende-se o curso do prazo processual nos dias compreendidos entre 20 de dezembro e 20 de janeiro', 'nos processos vinculados a essas prisões', 'CPP, art. 798-A, caput e I')],
  kw=['20 de dezembro', 'réus presos'])
I(P, 2, 'Atos em domingos e feriados',
  'As sessões de julgamento podem ser marcadas para domingo ou feriado, como os demais atos do processo.', 'E',
  'Art. 797: as **sessões de julgamento** não serão marcadas para **domingo ou feriado**; os demais atos podem ser praticados nesses dias.',
  lei=[(CPP + '797', 'Excetuadas as sessões de julgamento, que não serão marcadas para domingo ou dia feriado', None, 'CPP, art. 797')],
  peg='Igualar sessões de julgamento aos demais atos.',
  kw=['sessões de julgamento', 'domingo ou feriado'])
I(P, 2, 'Intimação pessoal',
  'A intimação do Ministério Público e do defensor constituído será pessoal.', 'E',
  'Art. 370, § 4º: pessoal é a intimação do MP e do **defensor nomeado**. O **constituído** é intimado pela imprensa oficial (§ 1º).',
  lei=[(CPP + '370', 'A intimação do Ministério Público e do defensor nomeado será pessoal', None, 'CPP, art. 370, § 4º')],
  peg='Trocar defensor nomeado por constituído.',
  kw=['intimação pessoal', 'defensor nomeado'])
I(P, 2, 'Precatória e audiência',
  'Intimada a defesa da expedição da carta precatória, é indispensável nova intimação da data da audiência no juízo deprecado, sob pena de nulidade absoluta.', 'E',
  '**Súmula 273/STJ**: torna-se **desnecessária** a intimação da data. E a falta de intimação da expedição é nulidade **relativa** (**Súmula 155/STF**).',
  juris=[J['S273'], J['STF155']],
  peg='Exigir dupla intimação e chamar de absoluta uma nulidade relativa.',
  kw=['Súmula 273', 'carta precatória'])
