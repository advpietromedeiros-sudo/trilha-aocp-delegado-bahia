# Pente Fino de Direito Penal (Parte Geral) — PEN-5 (ilicitude, 5.1), PEN-6 (culpabilidade, 6.1 a 6.6) e
# PEN-7 (concurso de agentes) (08/11/2026).
from base import I
from pen_juris import J

CP = 'CP:'
EXCL = (CP + '23', 'Não há crime quando o agente pratica o fato:', 'no exercício regular de direito', 'CP, art. 23, I a III')
EXCESSO = (CP + '23', 'O agente, em qualquer das hipóteses deste artigo, responderá pelo excesso doloso ou culposo.', None, 'CP, art. 23, par. ún.')
EN = (CP + '24', 'Considera-se em estado de necessidade quem pratica o fato para salvar de perigo atual', 'não era razoável exigir-se', 'CP, art. 24, caput')
LD = (CP + '25', 'Entende-se em legítima defesa quem, usando moderadamente dos meios necessários', 'a direito seu ou de outrem', 'CP, art. 25, caput')
INIMP = (CP + '26', 'É isento de pena o agente que, por doença mental ou desenvolvimento mental incompleto ou retardado', 'de determinar-se de acordo com esse entendimento', 'CP, art. 26, caput')
SEMI = (CP + '26', 'A pena pode ser reduzida de um a dois terços, se o agente, em virtude de perturbação de saúde mental', None, 'CP, art. 26, par. ún.')
EMBR = (CP + '28', 'É isento de pena o agente que, por embriaguez completa, proveniente de caso fortuito ou força maior', None, 'CP, art. 28, § 1º')
PROIB = (CP + '21', 'O desconhecimento da lei é inescusável.', 'poderá diminuí-la de um sexto a um terço', 'CP, art. 21, caput')
COAC = (CP + '22', 'Se o fato é cometido sob coação irresistível ou em estrita obediência a ordem, não manifestamente ilegal, de superior hierárquico', 'só é punível o autor da coação ou da ordem', 'CP, art. 22')
CONC = (CP + '29', 'Quem, de qualquer modo, concorre para o crime incide nas penas a este cominadas, na medida de sua culpabilidade.', None, 'CP, art. 29, caput')
MENOR = (CP + '29', 'Se a participação for de menor importância, a pena pode ser diminuída de um sexto a um terço.', None, 'CP, art. 29, § 1º')
COOP = (CP + '29', 'Se algum dos concorrentes quis participar de crime menos grave', 'na hipótese de ter sido previsível o resultado mais grave', 'CP, art. 29, § 2º')
COMUN = (CP + '30', 'Não se comunicam as circunstâncias e as condições de caráter pessoal, salvo quando elementares do crime.', None, 'CP, art. 30')

# ======================= PEN-5 · Ilicitude =======================
P = 'DBA26-PEN-5'
I(P, 1, 'Conceito',
  'Ilicitude (antijuridicidade) é o choque do fato típico com o ordenamento jurídico considerado em seu conjunto.', 'C',
  'Presente uma **causa de justificação**, o fato típico é lícito: "não há crime" (art. 23).',
  lei=[EXCL], kw=['ilicitude', 'contrariedade'])
I(P, 1, 'Rol legal',
  'O art. 23 do Código Penal prevê como causas de exclusão da ilicitude o estado de necessidade, a legítima defesa, o estrito cumprimento do dever legal, o exercício regular de direito e a obediência hierárquica.', 'E',
  'A **obediência hierárquica** (art. 22) exclui a **culpabilidade** (inexigibilidade de conduta diversa), não a ilicitude. O art. 23 traz só as quatro primeiras.',
  lei=[EXCL, COAC], peg='Incluir a obediência hierárquica entre as justificantes.', kw=['obediência hierárquica', 'culpabilidade'])
I(P, 1, 'Excesso punível',
  'Em qualquer das excludentes de ilicitude, o agente responde pelo excesso doloso ou culposo.', 'C',
  'Art. 23, par. ún.: o **excesso** vale para todas as justificantes, não só para a legítima defesa.',
  lei=[EXCESSO], kw=['excesso doloso ou culposo'])
I(P, 1, 'Elemento subjetivo das justificantes',
  'Para a doutrina majoritária, as causas de justificação exigem, além dos requisitos objetivos, o elemento subjetivo: o agente deve saber que age amparado pela excludente.', 'C',
  'Ex.: quem mata desafeto sem saber que este ia matar um terceiro não está em legítima defesa (falta o **animus defendendi**). O art. 25 fala em quem "repele" a agressão — conduta orientada.',
  lei=[LD], kw=['elemento subjetivo', 'animus defendendi'])
I(P, 1, 'Excesso exculpante',
  'O excesso na legítima defesa é sempre punível, ainda que decorrente de medo, surpresa ou perturbação de ânimo invencíveis.', 'E',
  'A doutrina admite o **excesso exculpante** (inexigibilidade de conduta diversa), que não está no art. 23 — o CP Militar o prevê expressamente. A assertiva absoluta erra.',
  lei=[EXCESSO], peg='Absolutizar a punição do excesso.', kw=['excesso exculpante'])
# --- PEN-5 · Rodada 2
I(P, 2, 'Ilicitude formal e material',
  'Ilicitude material é a lesão ou exposição a perigo do bem jurídico; ilicitude formal é a mera contrariedade à norma.', 'C',
  'Distinção doutrinária entre **ilicitude formal** e **material**; a base positiva da ilicitude é a ausência das justificantes do art. 23.',
  lei=[EXCL], kw=['ilicitude material', 'ilicitude formal'])
I(P, 2, 'Legítima defesa da honra',
  'A legítima defesa da honra pode ser alegada no plenário do júri pela defesa, por força da plenitude de defesa, ainda que o STF a considere inconstitucional.', 'E',
  'Na **ADPF 779** o STF vedou o uso da tese, direta ou indiretamente, em qualquer fase (inclusive no júri), sob pena de **nulidade** do ato e do julgamento.',
  juris=[J['ADPF779']], peg='Invocar a plenitude de defesa para ressuscitar a tese.', kw=['ADPF 779', 'legítima defesa da honra'])
I(P, 2, 'Justificante e reparação civil',
  'Reconhecida a legítima defesa real, o agente não responde penalmente, mas pode ter de indenizar terceiro inocente atingido por erro na execução.', 'C',
  'A justificante afasta o crime (art. 23); na esfera civil, o terceiro atingido por **aberratio ictus** pode ser indenizado (com direito de regresso contra o agressor).',
  lei=[EXCL, (CP + '73', 'Quando, por acidente ou erro no uso dos meios de execução', None, 'CP, art. 73')],
  kw=['legítima defesa real', 'terceiro inocente'])

# ======================= PEN-5.1 · Causas de exclusão da ilicitude =======================
P = 'DBA26-PEN-5.1'
I(P, 1, 'Estado de necessidade: perigo atual',
  'Age em estado de necessidade quem pratica o fato para salvar de perigo atual, que não provocou por sua vontade, nem podia de outro modo evitar, direito próprio ou alheio.', 'C',
  'Requisitos do art. 24, caput: **perigo atual**, não provocado voluntariamente, inevitabilidade e inexigibilidade do sacrifício.',
  lei=[EN], kw=['perigo atual', 'estado de necessidade'])
I(P, 1, 'Dever legal de enfrentar o perigo',
  'O bombeiro pode alegar estado de necessidade para não enfrentar o incêndio, desde que haja risco à sua vida.', 'E',
  'Não pode alegar estado de necessidade **quem tinha o dever legal de enfrentar o perigo** (art. 24, § 1º). O dever não é ilimitado (não se exige heroísmo suicida), mas a regra legal veda a alegação.',
  lei=[(CP + '24', 'Não pode alegar estado de necessidade quem tinha o dever legal de enfrentar o perigo.', None, 'CP, art. 24, § 1º')],
  peg='Ignorar o § 1º do art. 24.', kw=['dever legal de enfrentar o perigo'])
I(P, 1, 'Teoria unitária',
  'Quanto ao estado de necessidade, o Código Penal comum adotou a teoria diferenciadora, distinguindo o estado de necessidade justificante do exculpante.', 'E',
  'O CP comum adotou a **teoria unitária** (art. 24, § 2º): se era razoável exigir o sacrifício, não há justificante, mas só **causa de diminuição** de 1/3 a 2/3.',
  lei=[(CP + '24', 'Embora seja razoável exigir-se o sacrifício do direito ameaçado, a pena poderá ser reduzida de um a dois terços.', None, 'CP, art. 24, § 2º')],
  kw=['teoria unitária', 'causa de diminuição'])
I(P, 1, 'Legítima defesa: requisitos',
  'Entende-se em legítima defesa quem, usando moderadamente dos meios necessários, repele injusta agressão, atual ou iminente, a direito seu ou de outrem.', 'C',
  'Requisitos do art. 25: **agressão injusta**, **atual ou iminente**, a direito próprio ou alheio, **meios necessários** usados **moderadamente**.',
  lei=[LD], kw=['injusta agressão', 'atual ou iminente'])
I(P, 1, 'Agressão futura',
  'Admite-se legítima defesa contra agressão futura, desde que certa, como a ameaça de morte para o dia seguinte.', 'E',
  'A agressão deve ser **atual ou iminente** (art. 25). Contra mal futuro, cabe buscar a proteção do Estado; reagir antes é vingança antecipada.',
  lei=[LD], peg='Aceitar agressão futura.', kw=['atual ou iminente', 'agressão futura'])
I(P, 1, 'Agente de segurança e refém',
  'Considera-se também em legítima defesa o agente de segurança pública que repele agressão ou risco de agressão a vítima mantida refém durante a prática de crimes.', 'C',
  'Art. 25, par. ún. (Lei 13.964/2019), **observados os requisitos do caput**. Não cria licença para matar: só explicita uma hipótese.',
  lei=[(CP + '25', 'Observados os requisitos previstos no caput deste artigo, considera-se também em legítima defesa o agente de segurança pública', 'durante a prática de crimes', 'CP, art. 25, par. ún.')],
  kw=['agente de segurança pública', 'refém'])
I(P, 1, 'Estrito cumprimento e exercício regular',
  'O estrito cumprimento do dever legal e o exercício regular de direito são causas de exclusão da ilicitude expressas no Código Penal.', 'C',
  'Art. 23, III. Ex.: prisão em flagrante pelo policial (dever) e intervenção médica consentida ou violência desportiva dentro das regras (direito).',
  lei=[(CP + '23', 'em estrito cumprimento de dever legal ou no exercício regular de direito', None, 'CP, art. 23, III')],
  kw=['estrito cumprimento', 'exercício regular de direito'])
I(P, 1, 'Consentimento do ofendido',
  'O consentimento do ofendido é causa legal e expressa de exclusão da ilicitude no Código Penal.', 'E',
  'É **causa supralegal** de exclusão da ilicitude (bem disponível, ofendido capaz, consentimento anterior ou concomitante). Quando o dissenso é elementar do tipo (ex.: violação de domicílio), o consentimento exclui a **tipicidade**.',
  lei=[EXCL], peg='Dizer que o consentimento está no art. 23.', kw=['causa supralegal', 'consentimento'])
# --- PEN-5.1 · Rodada 2
I(P, 2, 'Legítima defesa recíproca',
  'Não se admite legítima defesa real contra legítima defesa real, mas é possível legítima defesa real contra legítima defesa putativa.', 'C',
  'Quem age em legítima defesa real pratica conduta **lícita**, não "injusta". Já a putativa é ilícita (só exculpa), e contra ela cabe defesa real.',
  lei=[LD], kw=['legítima defesa recíproca', 'putativa'])
I(P, 2, 'Estado de necessidade contra estado de necessidade',
  'Não se admite estado de necessidade recíproco, porque um dos agentes estará necessariamente praticando agressão injusta contra o outro.', 'E',
  'No estado de necessidade há **perigo**, não agressão injusta: o **estado de necessidade recíproco** é possível, e ambos agem licitamente (art. 24).',
  lei=[EN], kw=['estado de necessidade recíproco'])
I(P, 2, 'Legítima defesa contra inimputável',
  'Não cabe legítima defesa contra agressão de inimputável, como um doente mental, porque falta a culpabilidade do agressor.', 'E',
  'A agressão precisa ser **injusta** (ilícita), não culpável. Cabe legítima defesa contra inimputável; a doutrina recomenda maior cautela (preferir a fuga quando possível).',
  lei=[LD], peg='Exigir culpabilidade do agressor.', kw=['injusta', 'inimputável'])
I(P, 2, 'Ofendículos',
  'Os ofendículos (cerca elétrica, cacos de vidro no muro) são, para parte da doutrina, exercício regular de direito e, para outra, legítima defesa preordenada.', 'C',
  'Os **ofendículos** dividem a doutrina; em ambas as leituras, exige-se moderação, e o excesso é punível (art. 23, par. ún.).',
  lei=[EXCESSO], kw=['ofendículos', 'legítima defesa preordenada'])
I(P, 2, 'Estado de necessidade e perigo provocado',
  'Quem provoca dolosamente o perigo pode, ainda assim, invocar estado de necessidade para salvar direito próprio.', 'E',
  'O perigo não pode ter sido provocado "**por sua vontade**" (art. 24). A doutrina majoritária lê a expressão como provocação dolosa.',
  lei=[EN], peg='Admitir estado de necessidade para quem criou o perigo de propósito.', kw=['por sua vontade'])

# ======================= PEN-6 · Teoria geral da culpabilidade =======================
P = 'DBA26-PEN-6'
I(P, 1, 'Teoria normativa pura',
  'Pela teoria normativa pura, adotada pelo finalismo, a culpabilidade compõe-se de imputabilidade, potencial consciência da ilicitude e exigibilidade de conduta diversa.', 'C',
  'Na **teoria normativa pura** o CP espelha os três elementos: imputabilidade (arts. 26–28), potencial consciência da ilicitude (art. 21) e exigibilidade de conduta diversa (art. 22).',
  lei=[INIMP, PROIB, COAC], kw=['teoria normativa pura', 'exigibilidade de conduta diversa'])
I(P, 1, 'Dolo na culpabilidade',
  'Na teoria normativa pura, o dolo e a culpa continuam integrando a culpabilidade, ao lado da imputabilidade.', 'E',
  'No finalismo, dolo e culpa **migram para o tipo**; a culpabilidade fica só com elementos **normativos**. Quem mantinha o dolo (normativo) na culpabilidade era a teoria **psicológico-normativa**.',
  lei=[(CP + '20', 'O erro sobre elemento constitutivo do tipo legal de crime exclui o dolo', None, 'CP, art. 20, caput')],
  peg='Manter o dolo na culpabilidade finalista.', kw=['dolo no tipo', 'psicológico-normativa'])
I(P, 1, 'Culpabilidade e dosimetria',
  'A culpabilidade, além de elemento do crime, é a primeira circunstância judicial do art. 59, funcionando como medida da pena.', 'C',
  'No art. 59, a "**culpabilidade**" é o grau de reprovabilidade da conduta (culpabilidade-medida), distinta da culpabilidade-fundamento.',
  lei=[(CP + '59', 'O juiz, atendendo à culpabilidade', None, 'CP, art. 59, caput')],
  kw=['culpabilidade-medida', 'art. 59'])
I(P, 1, 'Coautoria e culpabilidade',
  'Quem concorre para o crime incide nas penas a este cominadas, na medida de sua culpabilidade.', 'C',
  'Art. 29, caput: a cláusula final individualiza a pena de cada concorrente.',
  lei=[CONC], kw=['na medida de sua culpabilidade'])
I(P, 1, 'Teoria psicológica',
  'Para a teoria psicológica da culpabilidade, a culpabilidade é juízo de reprovação baseado na exigibilidade de conduta diversa.', 'E',
  'Na **teoria psicológica** (causalismo), culpabilidade é o **vínculo psíquico** (dolo ou culpa) entre autor e fato. O juízo de **reprovação** surge com as teorias **normativas**.',
  lei=[(CP + '18', 'doloso, quando o agente quis o resultado ou assumiu o risco de produzi-lo', None, 'CP, art. 18, I')],
  peg='Atribuir à teoria psicológica o juízo normativo.', kw=['teoria psicológica', 'vínculo psíquico'])
# --- PEN-6 · Rodada 2
I(P, 2, 'Coculpabilidade',
  'A coculpabilidade sustenta que o Estado divide a reprovação quando falha em oferecer oportunidades ao agente, e pode ser considerada como atenuante inominada.', 'C',
  'Construção doutrinária (Zaffaroni) cuja via positiva sugerida é o **art. 66** do CP (atenuante por circunstância relevante não prevista em lei).',
  lei=[(CP + '66', 'A pena poderá ser ainda atenuada em razão de circunstância relevante, anterior ou posterior ao crime, embora não prevista expressamente em lei.', None, 'CP, art. 66')],
  kw=['coculpabilidade', 'atenuante inominada'])
I(P, 2, 'Culpabilidade de autor',
  'O direito penal brasileiro adota a culpabilidade de autor, que reprova o agente pelo seu caráter ou modo de vida.', 'E',
  'Adota-se a **culpabilidade do fato**: reprova-se o que foi feito. Personalidade e antecedentes só graduam a pena (art. 59).',
  lei=[(CP + '59', 'aos antecedentes, à conduta social, à personalidade do agente', None, 'CP, art. 59, caput')],
  peg='Trocar culpabilidade do fato por culpabilidade de autor.', kw=['culpabilidade do fato'])
I(P, 2, 'Teoria limitada e erro de tipo permissivo',
  'O Código Penal adotou a teoria limitada da culpabilidade: o engano sobre a situação fática que embasaria uma justificante recebe o tratamento de erro de tipo, e o engano sobre seus limites ou sua existência, o de erro de proibição.', 'C',
  'Art. 20, § 1º (descriminante putativa fática, com punição culposa se evitável) e art. 21 (erro de proibição indireto). Assim consta do item 17 da Exposição de Motivos.',
  lei=[(CP + '20', 'Não há isenção de pena quando o erro deriva de culpa e o fato é punível como crime culposo.', None, 'CP, art. 20, § 1º, parte final')],
  kw=['teoria limitada da culpabilidade', 'erro de tipo permissivo'])

# ======================= PEN-6.1 · Fundamentos, conceito, elementos e conteúdo =======================
P = 'DBA26-PEN-6.1'
I(P, 1, 'Conceito normativo',
  'Culpabilidade é o juízo de reprovação que recai sobre o autor de um fato típico e ilícito que podia agir de acordo com o direito.', 'C',
  'Conceito **normativo**: reprovabilidade. Os elementos estão nos arts. 21, 22 e 26 a 28 do CP.',
  lei=[INIMP], kw=['juízo de reprovação', 'normativo'])
I(P, 1, 'Potencial consciência da ilicitude',
  'Para a culpabilidade exige-se a consciência atual da ilicitude, de modo que quem não sabia que o fato era proibido nunca pode ser punido.', 'E',
  'Basta a **potencial** consciência: se o agente podia, nas circunstâncias, atingir a consciência da ilicitude, o erro é **evitável** e só reduz a pena (art. 21, par. ún.).',
  lei=[(CP + '21', 'Considera-se evitável o erro se o agente atua ou se omite sem a consciência da ilicitude do fato', 'ter ou atingir essa consciência', 'CP, art. 21, par. ún.')],
  peg='Trocar potencial por atual.', kw=['potencial consciência', 'evitável'])
I(P, 1, 'Exigibilidade de conduta diversa',
  'A coação moral irresistível exclui a culpabilidade por inexigibilidade de conduta diversa, punindo-se apenas o autor da coação.', 'C',
  'Art. 22, 1ª parte: o coagido não é culpável; o coator responde como **autor mediato** (e com a agravante do art. 62, II).',
  lei=[COAC], kw=['inexigibilidade de conduta diversa', 'autor mediato'])
I(P, 1, 'Imputabilidade: critério',
  'Quanto aos inimputáveis por doença mental, o Código Penal adotou o critério exclusivamente biológico, bastando a doença para isentar de pena.', 'E',
  'Adotou o critério **biopsicológico**: além da doença ou desenvolvimento incompleto/retardado (biológico), exige-se a **incapacidade** de entender ou de se determinar ao tempo da conduta (psicológico) — art. 26.',
  lei=[INIMP], exc=['Menores de 18 anos: critério puramente biológico (CP, art. 27)'],
  peg='Trocar biopsicológico por biológico.', kw=['biopsicológico'])
I(P, 1, 'Momento da aferição',
  'A imputabilidade penal é aferida no momento da sentença, quando o juiz examina o laudo pericial.', 'E',
  'Art. 26: a capacidade é verificada **ao tempo da ação ou da omissão** (coerente com a teoria da atividade, art. 4º).',
  lei=[INIMP], kw=['ao tempo da ação ou da omissão'])
# --- PEN-6.1 · Rodada 2
I(P, 2, 'Funcionalismo e culpabilidade',
  'Para o funcionalismo teleológico, a culpabilidade integra a categoria mais ampla da responsabilidade, que exige também a necessidade preventiva da pena.', 'C',
  'Formulação doutrinária (Roxin): **responsabilidade** = culpabilidade + necessidade de pena. Ecoa no art. 59 ("necessário e suficiente").',
  lei=[(CP + '59', 'conforme seja necessário e suficiente para reprovação e prevenção do crime', None, 'CP, art. 59, caput')],
  kw=['responsabilidade', 'necessidade preventiva'])
I(P, 2, 'Inexigibilidade supralegal',
  'A inexigibilidade de conduta diversa só exclui a culpabilidade nas hipóteses expressas do art. 22, não admitindo a doutrina causas supralegais.', 'E',
  'Boa parte da doutrina admite a **inexigibilidade de conduta diversa** como **causa supralegal** de exculpação (ex.: aborto de feto anencéfalo antes da ADPF 54, excesso exculpante).',
  lei=[COAC], peg='Fechar o rol de exculpantes.', kw=['causa supralegal', 'inexigibilidade'])
I(P, 2, 'Emoção e paixão',
  'A emoção e a paixão não excluem a imputabilidade penal, podendo, conforme o caso, atenuar ou diminuir a pena.', 'C',
  'Art. 28, I. A violenta emoção provocada por ato injusto da vítima atenua (art. 65, III, c) ou privilegia o homicídio (art. 121, § 1º).',
  lei=[(CP + '28', 'Não excluem a imputabilidade penal:', 'a emoção ou a paixão', 'CP, art. 28, I')],
  kw=['emoção ou a paixão'])

# ======================= PEN-6.2 · Princípio de culpabilidade =======================
P = 'DBA26-PEN-6.2'
I(P, 1, 'Responsabilidade subjetiva',
  'O princípio da culpabilidade veda a responsabilidade penal objetiva: ninguém responde por resultado que não causou ao menos culposamente.', 'C',
  'Art. 19 do CP (resultado agravador) e art. 18, par. ún. (excepcionalidade da culpa).',
  lei=[(CP + '19', 'Pelo resultado que agrava especialmente a pena, só responde o agente que o houver causado ao menos culposamente.', None, 'CP, art. 19')],
  kw=['responsabilidade penal objetiva'])
I(P, 1, 'Pessoalidade',
  'Do princípio da culpabilidade decorre que a pena pode ser estendida aos familiares do condenado quando estes se beneficiarem do crime.', 'E',
  'A **pena** não passa da pessoa do condenado; aos sucessores estendem-se só a reparação do dano e o perdimento de bens, até o limite do patrimônio transferido (CF, art. 5º, XLV).',
  lei=[('CF:5', 'nenhuma pena passará da pessoa do condenado', 'até o limite do valor do patrimônio transferido', 'CF, art. 5º, XLV')],
  peg='Estender a pena a quem se beneficiou.', kw=['pessoalidade', 'reparação do dano'])
I(P, 1, 'Culpabilidade como limite da pena',
  'A culpabilidade funciona como limite da pena, impedindo que razões preventivas justifiquem punição acima do grau de reprovação do fato.', 'C',
  'É a função **limitadora**: a pena-base parte da culpabilidade (art. 59) e o concurso de pessoas respeita a "medida de sua culpabilidade" (art. 29).',
  lei=[CONC], kw=['limite da pena'])
I(P, 1, 'Versari in re illicita',
  'O Código Penal adota a regra do versari in re illicita, pela qual quem pratica ato ilícito responde por todas as suas consequências, ainda que imprevisíveis.', 'E',
  'O **versari** foi abolido pelo art. 19: o resultado agravador exige ao menos **culpa** (previsibilidade).',
  lei=[(CP + '19', 'só responde o agente que o houver causado ao menos culposamente', None, 'CP, art. 19')],
  peg='Ressuscitar o versari.', kw=['versari in re illicita'])
I(P, 1, 'Embriaguez preordenada',
  'A embriaguez preordenada, em que o agente se embriaga para cometer o crime, é agravante genérica.', 'C',
  'Art. 61, II, l. Pela teoria da **actio libera in causa**, a imputabilidade é aferida no momento em que o agente se embriagou livremente.',
  lei=[(CP + '61', 'em estado de embriaguez preordenada', None, 'CP, art. 61, II, l')],
  kw=['embriaguez preordenada', 'actio libera in causa'])
# --- PEN-6.2 · Rodada 2
I(P, 2, 'Actio libera in causa e responsabilidade objetiva',
  'A punição da embriaguez voluntária ou culposa não excludente, sem que o agente tenha previsto o crime ao se embriagar, é apontada por parte da doutrina como resquício de responsabilidade objetiva.', 'C',
  'Crítica doutrinária ao art. 28, II: a **actio libera in causa** só explica bem os casos em que o crime era ao menos previsível quando o agente bebeu.',
  lei=[(CP + '28', 'a embriaguez, voluntária ou culposa, pelo álcool ou substância de efeitos análogos', None, 'CP, art. 28, II')],
  kw=['actio libera in causa', 'resquício de responsabilidade objetiva'])
I(P, 2, 'Culpabilidade e reincidência',
  'O STJ admite que a reincidência seja valorada como circunstância judicial e, simultaneamente, como agravante, por expressarem aspectos diferentes da culpabilidade.', 'E',
  'A **Súmula 241/STJ** veda esse **bis in idem**.',
  juris=[J['S241']], peg='Dupla valoração da reincidência.', kw=['Súmula 241/STJ', 'bis in idem'])
I(P, 2, 'Medida da culpabilidade no concurso',
  'Na cooperação dolosamente distinta, aplica-se ao concorrente que quis participar de crime menos grave a pena deste, aumentada até a metade se o resultado mais grave era previsível.', 'C',
  'Art. 29, § 2º: expressão direta do princípio da culpabilidade no concurso de pessoas.',
  lei=[COOP], kw=['cooperação dolosamente distinta'])

# ======================= PEN-6.3 · Culpabilidade e pena =======================
P = 'DBA26-PEN-6.3'
I(P, 1, 'Circunstância judicial',
  'A culpabilidade é a primeira das circunstâncias judiciais que o juiz considera ao fixar a pena-base.', 'C',
  'Art. 59, caput; a pena-base é a primeira fase do sistema trifásico (art. 68).',
  lei=[(CP + '59', 'O juiz, atendendo à culpabilidade, aos antecedentes', None, 'CP, art. 59, caput')],
  kw=['pena-base', 'culpabilidade'])
I(P, 1, 'Semi-imputabilidade',
  'O semi-imputável é isento de pena, como o inimputável, ficando sujeito apenas a medida de segurança.', 'E',
  'O **semi-imputável** é culpável e tem a pena **reduzida de 1/3 a 2/3** (art. 26, par. ún.); se necessitar de especial tratamento, a pena pode ser substituída por medida de segurança (art. 98) — sistema **vicariante**.',
  lei=[SEMI, (CP + '98', 'Na hipótese do parágrafo único do art. 26 deste Código e necessitando o condenado de especial tratamento curativo', None, 'CP, art. 98')],
  peg='Igualar o semi-imputável ao inimputável.', kw=['semi-imputável', 'vicariante'])
I(P, 1, 'Erro de proibição evitável',
  'Se evitável, o erro sobre a ilicitude do fato pode diminuir a pena de um sexto a um terço.', 'C',
  'Art. 21, caput, parte final.',
  lei=[PROIB], kw=['de um sexto a um terço', 'evitável'])
I(P, 1, 'Embriaguez fortuita incompleta',
  'A embriaguez incompleta proveniente de caso fortuito ou força maior isenta de pena o agente.', 'E',
  'A embriaguez fortuita **completa** isenta de pena (art. 28, § 1º); a **incompleta** só **reduz** de 1/3 a 2/3 (§ 2º).',
  lei=[EMBR, (CP + '28', 'A pena pode ser reduzida de um a dois terços, se o agente, por embriaguez, proveniente de caso fortuito ou força maior', None, 'CP, art. 28, § 2º')],
  peg='Trocar completa por incompleta.', kw=['embriaguez fortuita', 'incompleta'])
I(P, 1, 'Coação resistível',
  'Cometer o crime sob coação a que podia resistir é circunstância atenuante.', 'C',
  'Art. 65, III, c. A coação **irresistível** exclui a culpabilidade (art. 22); a **resistível** só atenua.',
  lei=[(CP + '65', 'cometido o crime sob coação a que podia resistir', None, 'CP, art. 65, III, c')],
  kw=['coação a que podia resistir', 'atenuante'])
# --- PEN-6.3 · Rodada 2
I(P, 2, 'Sistema vicariante',
  'Após a reforma de 1984, o semi-imputável pode receber, cumulativamente, pena reduzida e medida de segurança.', 'E',
  'O sistema do **duplo binário** foi substituído pelo **vicariante**: ou pena reduzida, **ou** medida de segurança substitutiva (art. 98), nunca as duas.',
  lei=[(CP + '98', 'a pena privativa de liberdade pode ser substituída pela internação, ou tratamento ambulatorial', None, 'CP, art. 98')],
  peg='Ressuscitar o duplo binário.', kw=['vicariante', 'duplo binário'])
I(P, 2, 'Culpabilidade e fundamentação',
  'Na dosimetria, a culpabilidade exige fundamentação em dados concretos que indiquem reprovabilidade maior que a inerente ao tipo; elementares do crime não servem para elevá-la.', 'C',
  'Decorre do dever de **fundamentação** (CF, art. 93, IX) e do art. 59 (culpabilidade como grau de reprovação).',
  lei=[('CF:93', 'todos os julgamentos dos órgãos do Poder Judiciário serão públicos, e fundamentadas todas as decisões', None, 'CF, art. 93, IX')],
  kw=['fundamentação', 'dados concretos'])
I(P, 2, 'Erro de proibição e atenuante',
  'O desconhecimento da lei é inescusável, mas constitui circunstância atenuante.', 'C',
  'Art. 21, caput, 1ª parte, e art. 65, II: não isenta, mas **atenua**. Diferente do erro sobre a **ilicitude** do fato, que pode isentar (art. 21).',
  lei=[(CP + '65', 'o desconhecimento da lei', None, 'CP, art. 65, II')],
  kw=['desconhecimento da lei', 'atenuante'])

# ======================= PEN-6.4 · Causas de exclusão da culpabilidade =======================
P = 'DBA26-PEN-6.4'
I(P, 1, 'Obediência hierárquica',
  'Se o fato é cometido em estrita obediência a ordem, não manifestamente ilegal, de superior hierárquico, só é punível o autor da ordem.', 'C',
  'Art. 22, 2ª parte. Requer relação de **direito público** e ordem **não manifestamente ilegal**.',
  lei=[COAC], kw=['obediência hierárquica', 'não manifestamente ilegal'])
I(P, 1, 'Ordem manifestamente ilegal',
  'O subordinado que cumpre ordem manifestamente ilegal fica isento de pena, respondendo apenas o superior.', 'E',
  'Ordem **manifestamente ilegal** não deve ser cumprida: ambos respondem (o subordinado com a atenuante do art. 65, III, c, "em cumprimento de ordem de autoridade superior").',
  lei=[COAC, (CP + '65', 'ou em cumprimento de ordem de autoridade superior', None, 'CP, art. 65, III, c')],
  peg='Isentar quem cumpre ordem manifestamente ilegal.', kw=['manifestamente ilegal', 'atenuante'])
I(P, 1, 'Obediência e relação privada',
  'A obediência hierárquica exclui a culpabilidade também nas relações privadas, como a do empregado com o patrão.', 'E',
  'Para a doutrina, a **hierarquia** do art. 22 é a de **direito público**; nas relações privadas pode haver, conforme o caso, coação moral.',
  lei=[COAC], peg='Estender a hierarquia ao setor privado.', kw=['direito público'])
I(P, 1, 'Rol das dirimentes',
  'Excluem a culpabilidade a inimputabilidade, o erro de proibição inevitável, a coação moral irresistível e a obediência hierárquica.', 'C',
  'São as **dirimentes** legais (arts. 21, 22 e 26 a 28). A doutrina acrescenta a inexigibilidade de conduta diversa supralegal.',
  lei=[INIMP, PROIB, COAC], kw=['dirimentes'])
I(P, 1, 'Coação física',
  'A coação física irresistível exclui a culpabilidade, por inexigibilidade de conduta diversa.', 'E',
  'A coação **física** irresistível elimina a **voluntariedade**, logo a **conduta** (fato atípico). A coação **moral** é que exclui a culpabilidade (art. 22).',
  lei=[COAC], peg='Trocar física por moral.', kw=['coação física', 'conduta'])
# --- PEN-6.4 · Rodada 2
I(P, 2, 'Descriminante putativa por erro de proibição',
  'Quem supõe existir uma causa de justificação que o ordenamento não prevê, ou excede os seus limites por erro, incide em erro de proibição indireto.', 'C',
  'Na **teoria limitada**, o erro sobre a **existência** ou os **limites** da justificante é erro de proibição (art. 21); só o erro sobre os **fatos** é erro de tipo permissivo (art. 20, § 1º).',
  lei=[PROIB], kw=['erro de proibição indireto'])
I(P, 2, 'Coação: coator e agravante',
  'O autor da coação, além de responder pelo crime, tem a pena agravada.', 'C',
  'Art. 62, II: agrava-se a pena de quem "coage ou induz outrem à execução material do crime". A doutrina vê ainda concurso com o crime de tortura ou constrangimento contra o coagido.',
  lei=[(CP + '62', 'coage ou induz outrem à execução material do crime', None, 'CP, art. 62, II')],
  kw=['coage ou induz', 'agravante'])
I(P, 2, 'Emoção e exclusão da culpabilidade',
  'A violenta emoção, quando intensa, exclui a culpabilidade do agente.', 'E',
  'A emoção e a paixão **não excluem a imputabilidade** (art. 28, I); só podem atenuar (art. 65, III, c) ou privilegiar.',
  lei=[(CP + '28', 'Não excluem a imputabilidade penal:', 'a emoção ou a paixão', 'CP, art. 28, I')],
  peg='Dar à emoção efeito dirimente.', kw=['não excluem a imputabilidade'])

# ======================= PEN-6.5 · Imputabilidade =======================
P = 'DBA26-PEN-6.5'
I(P, 1, 'Menoridade',
  'Os menores de 18 anos são penalmente inimputáveis, sujeitos às normas da legislação especial.', 'C',
  'CF, art. 228, e CP, art. 27: critério **biológico**, presunção absoluta.',
  lei=[(CP + '27', 'Os menores de 18 (dezoito) anos são penalmente inimputáveis, ficando sujeitos às normas estabelecidas na legislação especial.', None, 'CP, art. 27')],
  kw=['menores de 18', 'critério biológico'])
I(P, 1, 'Prova da menoridade',
  'Para efeitos penais, a menoridade do réu pode ser comprovada por qualquer meio, inclusive pela simples declaração do acusado no interrogatório.', 'E',
  'A **Súmula 74/STJ** exige **prova por documento hábil**.',
  juris=[J['S74']], peg='Aceitar a palavra do réu como prova da idade.', kw=['Súmula 74/STJ', 'documento hábil'])
I(P, 1, 'Embriaguez voluntária',
  'A embriaguez voluntária completa, que retira inteiramente a capacidade de entendimento, exclui a imputabilidade penal.', 'E',
  'Art. 28, II: a **embriaguez voluntária** ou culposa **não exclui** a imputabilidade, ainda que completa (**actio libera in causa**). Só a completa **fortuita** isenta (§ 1º).',
  lei=[(CP + '28', 'a embriaguez, voluntária ou culposa, pelo álcool ou substância de efeitos análogos', None, 'CP, art. 28, II')],
  kw=['embriaguez voluntária', 'actio libera in causa'])
I(P, 1, 'Embriaguez completa fortuita',
  'É isento de pena o agente que, por embriaguez completa proveniente de caso fortuito ou força maior, era, ao tempo da ação, inteiramente incapaz de entender o caráter ilícito do fato.', 'C',
  'Art. 28, § 1º: a **única embriaguez que isenta** é a **completa e acidental**.',
  lei=[EMBR], kw=['embriaguez completa', 'caso fortuito'])
I(P, 1, 'Embriaguez patológica',
  'A embriaguez patológica (doentia) recebe o mesmo tratamento da embriaguez voluntária, não afetando a imputabilidade.', 'E',
  'A embriaguez **patológica** é equiparada à **doença mental**: aplica-se o art. 26 (inimputabilidade ou semi-imputabilidade, conforme a perícia).',
  lei=[INIMP], peg='Tratar a embriaguez doentia como voluntária.', kw=['embriaguez patológica', 'doença mental'])
I(P, 1, 'Inimputável e medida de segurança',
  'Ao inimputável que pratica fato típico e ilícito o juiz aplica sentença absolutória imprópria, com medida de segurança.', 'C',
  'Absolvição **imprópria**: isenta de pena (art. 26) e impõe internação ou tratamento ambulatorial (art. 97).',
  lei=[(CP + '97', 'Se o agente for inimputável, o juiz determinará sua internação (art. 26).', None, 'CP, art. 97, caput, 1ª parte')],
  kw=['absolvição imprópria', 'medida de segurança'])
# --- PEN-6.5 · Rodada 2
I(P, 2, 'Menoridade e crime permanente',
  'Se o sequestro iniciado quando o agente tinha 17 anos prossegue depois que ele completa 18, ele responde pelo Código Penal.', 'C',
  'No **crime permanente** a conduta se protrai: atingida a maioridade durante a permanência, o agente é imputável a partir daí (art. 4º combinado com a lógica da Súmula 711/STF).',
  lei=[(CP + '4', 'Considera-se praticado o crime no momento da ação ou omissão', None, 'CP, art. 4º')], juris=[J['STF711']],
  kw=['crime permanente', 'maioridade'])
I(P, 2, 'Atenuante da menoridade relativa',
  'Ser o agente menor de 21 anos na data do fato é atenuante genérica, inclusive quando o crime envolver violência sexual contra a mulher.', 'E',
  'Pela Lei 15.160/2025, o art. 65, I, passou a excluir a atenuante "**salvo se o crime envolver violência sexual contra a mulher**".',
  lei=[(CP + '65', 'ser o agente menor de 21 (vinte e um) anos, na data do fato, ou maior de 70 (setenta) anos, na data da sentença, salvo se o crime envolver violência sexual contra a mulher', None, 'CP, art. 65, I')],
  peg='Ignorar a ressalva incluída pela Lei 15.160/2025.', kw=['menor de 21', 'violência sexual contra a mulher'])
I(P, 2, 'Superveniência de doença mental',
  'O condenado a quem sobrevém doença mental continua a cumprir a pena no estabelecimento comum, recebendo apenas tratamento ambulatorial.', 'E',
  'Art. 41: a quem **sobrevém doença mental** cabe recolhimento a hospital de custódia e tratamento psiquiátrico ou outro estabelecimento adequado; e a multa tem a execução suspensa (art. 52).',
  lei=[(CP + '41', 'O condenado a quem sobrevém doença mental deve ser recolhido a hospital de custódia e tratamento psiquiátrico', None, 'CP, art. 41'),
       (CP + '52', 'É suspensa a execução da pena de multa, se sobrevém ao condenado doença mental.', None, 'CP, art. 52')],
  kw=['sobrevém doença mental'])

# ======================= PEN-6.6 · Erro de proibição =======================
P = 'DBA26-PEN-6.6'
I(P, 1, 'Erro de proibição inevitável',
  'O erro sobre a ilicitude do fato, se inevitável, isenta de pena; se evitável, poderá diminuí-la de um sexto a um terço.', 'C',
  'Art. 21, caput. O inevitável exclui a **potencial consciência da ilicitude** (culpabilidade).',
  lei=[PROIB], kw=['erro sobre a ilicitude', 'inevitável'])
I(P, 1, 'Desconhecimento da lei',
  'O desconhecimento da lei, se inevitável, isenta o agente de pena.', 'E',
  'O **desconhecimento da lei é inescusável** (art. 21, 1ª parte) — apenas atenua (art. 65, II). O que isenta é o erro sobre a **ilicitude do fato**, isto é, sobre o caráter proibido da conduta.',
  lei=[PROIB], peg='Confundir desconhecimento da lei com erro de proibição.', kw=['inescusável', 'ilicitude do fato'])
I(P, 1, 'Erro evitável',
  'Considera-se evitável o erro se o agente atua sem a consciência da ilicitude do fato, quando lhe era possível, nas circunstâncias, ter ou atingir essa consciência.', 'C',
  'Art. 21, par. ún.',
  lei=[(CP + '21', 'Considera-se evitável o erro se o agente atua ou se omite sem a consciência da ilicitude do fato', 'ter ou atingir essa consciência', 'CP, art. 21, par. ún.')],
  kw=['evitável'])
I(P, 1, 'Erro de proibição x erro de tipo',
  'No erro de proibição o agente conhece a realidade do fato, mas supõe lícita a conduta; no erro de tipo, engana-se sobre a própria realidade do fato.', 'C',
  'Erro de **tipo** recai sobre a realidade fática (exclui dolo, art. 20); erro de **proibição** recai sobre a valoração jurídica (exclui ou reduz a culpabilidade, art. 21).',
  lei=[(CP + '20', 'O erro sobre elemento constitutivo do tipo legal de crime exclui o dolo', None, 'CP, art. 20, caput'), PROIB],
  kw=['erro de proibição', 'erro de tipo'])
I(P, 1, 'Efeito do erro evitável',
  'O erro de proibição evitável exclui o dolo, permitindo a punição a título de culpa.', 'E',
  'Quem exclui o dolo é o **erro de tipo**. O erro de proibição evitável mantém o crime doloso e só **reduz a pena** de 1/6 a 1/3 (art. 21).',
  lei=[PROIB], peg='Dar ao erro de proibição o efeito do erro de tipo.', kw=['reduz a pena'])
I(P, 1, 'Erro de proibição direto',
  'Há erro de proibição direto quando o agente desconhece a existência ou o alcance da norma proibitiva, como o turista que porta substância lá permitida e aqui proibida.', 'C',
  'O erro **direto** recai sobre a norma proibitiva; o **indireto**, sobre a existência ou limites de uma justificante; o **mandamental**, sobre o dever de agir nos omissivos.',
  lei=[PROIB], kw=['erro de proibição direto'])
I(P, 1, 'Contravenção e erro de direito',
  'Na Lei das Contravenções Penais, a ignorância ou a errada compreensão da lei, quando escusáveis, permitem ao juiz deixar de aplicar a pena.', 'C',
  'Art. 8º da LCP — regra própria das contravenções.',
  lei=[('DL3688:8', 'No caso de ignorância ou de errada compreensão da lei, quando escusaveis, a pena pode deixar de ser aplicada.', None, 'LCP, art. 8º')],
  kw=['errada compreensão da lei', 'contravenções'])
# --- PEN-6.6 · Rodada 2
I(P, 2, 'Erro mandamental',
  'O erro mandamental, que recai sobre o dever de agir nos crimes omissivos impróprios, é sempre tratado como erro de tipo.', 'E',
  'O **erro mandamental** é espécie de **erro de proibição** quando recai sobre a existência ou os limites do dever de agir; será erro de tipo apenas se incidir sobre a situação de fato que gera o dever (ex.: o pai não percebe que é seu filho que se afoga).',
  lei=[PROIB], peg='Absolutizar a natureza do erro mandamental.', kw=['erro mandamental'])
I(P, 2, 'Teoria extremada x limitada',
  'Para a teoria extremada da culpabilidade, toda descriminante putativa, inclusive a fática, é erro de proibição; o Código Penal, porém, adotou a teoria limitada.', 'C',
  'Na **teoria limitada** (art. 20, § 1º) o erro sobre os pressupostos fáticos é erro de tipo permissivo; na **extremada**, seria erro de proibição.',
  lei=[(CP + '20', 'É isento de pena quem, por erro plenamente justificado pelas circunstâncias, supõe situação de fato que, se existisse, tornaria a ação legítima.', None, 'CP, art. 20, § 1º, 1ª parte')],
  kw=['teoria extremada', 'teoria limitada'])
I(P, 2, 'Crime putativo',
  'O agente que mantém relação sexual consentida com pessoa de 20 anos, crendo que isso é crime, comete crime putativo por erro de proibição, que é impunível.', 'C',
  'É o **erro de proibição às avessas**: o fato é atípico, e a crença do agente não cria crime (reserva legal, CF, art. 5º, XXXIX).',
  lei=[('CF:5', 'não há crime sem lei anterior que o defina', None, 'CF, art. 5º, XXXIX')],
  kw=['crime putativo', 'às avessas'])
I(P, 2, 'Aferição da evitabilidade',
  'A potencial consciência da ilicitude é aferida segundo o homem médio abstrato, sem considerar as condições pessoais do agente.', 'E',
  'O art. 21, par. ún., manda verificar se era possível ao agente, "**nas circunstâncias**", atingir a consciência — juízo que considera as condições concretas do autor (instrução, meio social).',
  lei=[(CP + '21', 'quando lhe era possível, nas circunstâncias, ter ou atingir essa consciência', None, 'CP, art. 21, par. ún.')],
  peg='Usar só o homem médio abstrato.', kw=['nas circunstâncias'])

# ======================= PEN-7 · Concurso de agentes =======================
P = 'DBA26-PEN-7'
I(P, 1, 'Teoria monista',
  'Quanto ao concurso de pessoas, o Código Penal adotou, como regra, a teoria monista: todos os que concorrem respondem pelo mesmo crime, na medida de sua culpabilidade.', 'C',
  'Art. 29, caput. As **exceções pluralistas** estão na Parte Especial (ex.: aborto consentido × provocado com consentimento; corrupção ativa × passiva).',
  lei=[CONC], exc=['Exceções pluralistas: gestante (art. 124) × terceiro (art. 126); corruptor (art. 333) × funcionário (art. 317)'],
  kw=['teoria monista', 'exceções pluralistas'])
I(P, 1, 'Requisitos',
  'São requisitos do concurso de pessoas: pluralidade de agentes e de condutas, relevância causal de cada uma, liame subjetivo e identidade de infração.', 'C',
  'O **liame subjetivo** dispensa ajuste prévio (basta a adesão consciente à conduta alheia).',
  lei=[CONC], kw=['liame subjetivo', 'identidade de infração'])
I(P, 1, 'Ajuste prévio',
  'O concurso de pessoas exige ajuste prévio entre os agentes; sem combinação anterior, cada um responde isoladamente.', 'E',
  'Basta o **liame subjetivo** (vontade de aderir), que pode ser unilateral e surgir durante a execução. Sem liame algum, há **autoria colateral**.',
  lei=[CONC], peg='Exigir combinação prévia.', kw=['liame subjetivo', 'autoria colateral'])
I(P, 1, 'Participação de menor importância',
  'Se a participação for de menor importância, a pena pode ser diminuída de um a dois terços.', 'E',
  'Art. 29, § 1º: a **participação de menor importância** reduz de **um sexto a um terço**.',
  lei=[MENOR], kw=['menor importância'])
I(P, 1, 'Comunicabilidade',
  'As circunstâncias e condições de caráter pessoal comunicam-se aos coautores quando conhecidas por eles.', 'E',
  'A regra é a **incomunicabilidade** das pessoais; só se comunicam quando **elementares** do crime (art. 30) — e desde que conhecidas pelo concorrente.',
  lei=[COMUN], peg='Comunicar circunstância pessoal não elementar.', kw=['incomunicabilidade', 'elementares'])
I(P, 1, 'Peculato e particular',
  'O particular que, ciente da condição de funcionário público do comparsa, concorre para a apropriação do bem público responde também por peculato.', 'C',
  'A condição de **funcionário público** é **elementar** do peculato e se comunica ao particular que a conhece (art. 30).',
  lei=[COMUN], kw=['elementar', 'funcionário público'])
I(P, 1, 'Teoria do domínio do fato',
  'Pela teoria do domínio do fato, é autor quem tem o controle final sobre a realização do crime, ainda que não pratique o núcleo do tipo, como o mandante e o autor mediato.', 'C',
  'O **domínio do fato** é formulação doutrinária que complementa a teoria restritiva (objetivo-formal). O CP fala genericamente em concorrer "de qualquer modo" (art. 29).',
  lei=[CONC], kw=['domínio do fato', 'autor mediato'])
I(P, 1, 'Autor mediato',
  'Na autoria mediata, o autor se vale de pessoa que atua sem culpabilidade ou em erro, e ambos respondem como coautores.', 'E',
  'Na **autoria mediata** só o **autor mediato** responde; o executor é mero instrumento (inimputável, coagido, induzido a erro). Ex.: art. 20, § 2º, e art. 22.',
  lei=[(CP + '20', 'Responde pelo crime o terceiro que determina o erro.', None, 'CP, art. 20, § 2º'), COAC],
  peg='Fazer o instrumento responder como coautor.', kw=['autoria mediata', 'instrumento'])
# --- PEN-7 · Rodada 2
I(P, 2, 'Cooperação dolosamente distinta',
  'Se um dos concorrentes quis participar de crime menos grave, ser-lhe-á aplicada a pena deste, aumentada até metade se previsível o resultado mais grave.', 'C',
  'Art. 29, § 2º: se o resultado mais grave era **previsível**, aumento até a metade; se ele o **assumiu**, responde pelo mais grave.',
  lei=[COOP], kw=['cooperação dolosamente distinta', 'até metade'])
I(P, 2, 'Participação e acessoriedade limitada',
  'Pela teoria da acessoriedade limitada, preferida pela doutrina majoritária, pune-se o partícipe se o autor praticou fato típico e ilícito, ainda que não culpável.', 'C',
  'Na **acessoriedade limitada** não se exige a culpabilidade do autor; se o executor for inculpável e usado como instrumento, há autoria mediata. A participação ainda depende de o crime ao menos ser tentado (art. 31).',
  lei=[(CP + '31', 'não são puníveis, se o crime não chega, pelo menos, a ser tentado', None, 'CP, art. 31')],
  kw=['acessoriedade limitada'])
I(P, 2, 'Autoria colateral incerta',
  'Na autoria colateral incerta, dois atiradores sem vínculo disparam contra a vítima e não se apura quem a matou: ambos respondem por homicídio consumado.', 'E',
  'Sem liame subjetivo não há concurso (art. 29). Na dúvida sobre quem causou a morte, **ambos respondem por tentativa** (in dubio pro reo).',
  lei=[CONC, (CP + '14', 'tentado, quando, iniciada a execução, não se consuma por circunstâncias alheias à vontade do agente', None, 'CP, art. 14, II')],
  peg='Imputar a consumação a ambos sem liame.', kw=['autoria colateral incerta', 'tentativa'])
I(P, 2, 'Agravante do mandante',
  'A pena é agravada em relação ao agente que promove ou organiza a cooperação no crime ou dirige a atividade dos demais.', 'C',
  'Art. 62, I. Agrava-se também quem executa mediante paga ou promessa de recompensa (IV).',
  lei=[(CP + '62', 'promove, ou organiza a cooperação no crime ou dirige a atividade dos demais agentes', None, 'CP, art. 62, I')],
  kw=['promove, ou organiza', 'agravante'])
I(P, 2, 'Participação em crime culposo',
  'Admite-se participação em crime culposo, por exemplo, do passageiro que instiga o motorista a correr.', 'E',
  'A doutrina majoritária admite **coautoria** em crime culposo (vínculo na conduta descuidada), mas **não participação**: no tipo culposo, toda violação do dever de cuidado que contribui para o resultado é autoria.',
  lei=[(CP + '18', 'culposo, quando o agente deu causa ao resultado por imprudência, negligência ou imperícia', None, 'CP, art. 18, II')],
  peg='Trocar coautoria por participação no culposo.', kw=['coautoria em crime culposo'])
I(P, 2, 'Furto e majorante do roubo',
  'No furto qualificado pelo concurso de agentes, não se aplica a majorante do roubo por concurso de pessoas, conforme súmula do STJ.', 'C',
  '**Súmula 442/STJ**.',
  juris=[J['S442']], kw=['Súmula 442/STJ'])
