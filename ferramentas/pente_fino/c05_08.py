from base import I, J

P = 'DBA26-CPC-5'
# ---------------- PONTO 5 · Tutela provisória — RODADA 1
I(P, 1, 'Espécies',
  'A tutela provisória pode fundamentar-se em urgência ou evidência, e a tutela de urgência, cautelar ou antecipada, pode ser concedida em caráter antecedente ou incidental.', 'C',
  'Art. 294: **urgência** (cautelar ou antecipada; antecedente ou incidental) x **evidência** (sempre incidental).',
  lei=[('L13105:294', 'A tutela provisória pode fundamentar-se', 'antecedente ou incidental.', 'CPC, art. 294')],
  kw=['urgência', 'evidência', 'antecedente', 'incidental'])
I(P, 1, 'Revogabilidade',
  'A tutela provisória conserva sua eficácia na pendência do processo, mas pode, a qualquer tempo, ser revogada ou modificada.', 'C',
  'Art. 296: **precariedade** — eficácia durante o processo, revogável a qualquer tempo. Na suspensão do processo, conserva eficácia (par. ún.).',
  lei=[('L13105:296', 'A tutela provisória conserva sua eficácia', 'revogada ou modificada.', 'CPC, art. 296')],
  kw=['precariedade', 'revogação'])
I(P, 1, 'Requisitos da urgência',
  'A tutela de urgência será concedida quando houver prova inequívoca que convença o juiz da verossimilhança da alegação.', 'E',
  'Art. 300: **probabilidade do direito** + **perigo de dano ou risco ao resultado útil do processo**. "Prova inequívoca/verossimilhança" é linguagem do CPC/1973.',
  lei=[('L13105:300', 'A tutela de urgência será concedida quando houver elementos', 'resultado útil do processo.', 'CPC, art. 300')],
  peg='Requisitos do CPC/1973 apresentados como atuais.',
  kw=['probabilidade do direito', 'perigo de dano'])
I(P, 1, 'Irreversibilidade',
  'A tutela de urgência de natureza antecipada não será concedida quando houver perigo de irreversibilidade dos efeitos da decisão.', 'C',
  'Art. 300, § 3º. A vedação é para a **antecipada** (a cautelar só conserva).',
  lei=[('L13105:300', 'A tutela de urgência de natureza antecipada não será concedida', 'efeitos da decisão.', 'CPC, art. 300, § 3º')],
  kw=['irreversibilidade', 'antecipada'])
I(P, 1, 'Liminar ou justificação prévia',
  'A tutela de urgência só pode ser concedida após justificação prévia, vedada a concessão liminar.', 'E',
  'Art. 300, § 2º: pode ser concedida **liminarmente ou após justificação prévia**.',
  lei=[('L13105:300', 'A tutela de urgência pode ser concedida liminarmente ou após justificação prévia.', None, 'CPC, art. 300, § 2º')],
  kw=['liminar', 'justificação prévia'])
I(P, 1, 'Antecipada antecedente — aditamento',
  'Concedida a tutela antecipada em caráter antecedente, o autor deverá aditar a petição inicial no prazo de 30 dias ou em outro maior que o juiz fixar.', 'E',
  'Art. 303, § 1º, I: aditamento em **15 dias** (ou maior fixado pelo juiz). Os **30 dias** são da **cautelar** antecedente (art. 308).',
  lei=[('L13105:303', 'o autor deverá aditar a petição inicial', 'o juiz fixar;', 'CPC, art. 303, § 1º, I')],
  peg='Mistura dos prazos: 15 dias (antecipada) x 30 dias (cautelar).',
  kw=['aditamento', '15 dias', 'antecipada antecedente'])
I(P, 1, 'Estabilização',
  'A tutela antecipada concedida em caráter antecedente torna-se estável se da decisão que a conceder não for interposto o respectivo recurso.', 'C',
  'Art. 304, caput: **estabilização** pela inércia recursal do réu; o processo é extinto (§ 1º).',
  lei=[('L13105:304', 'A tutela antecipada, concedida nos termos do art. 303', 'respectivo recurso.', 'CPC, art. 304')],
  kw=['estabilização', 'recurso'])
I(P, 1, 'Prazo para rever a tutela estabilizada',
  'O direito de rever, reformar ou invalidar a tutela antecipada estabilizada extingue-se após 5 anos, contados da ciência da decisão que extinguiu o processo.', 'E',
  'Art. 304, § 5º: **2 anos**.',
  lei=[('L13105:304', 'O direito de rever, reformar ou invalidar a tutela antecipada', 'extinguiu o processo', 'CPC, art. 304, § 5º')],
  kw=['estabilização', '2 anos'])
I(P, 1, 'Estabilização x coisa julgada',
  'A decisão que concede a tutela antecipada estabilizada faz coisa julgada material.', 'E',
  'Art. 304, § 6º: **não faz coisa julgada**; a estabilidade só cai por decisão na ação do § 2º.',
  lei=[('L13105:304', 'A decisão que concede a tutela não fará coisa julgada', None, 'CPC, art. 304, § 6º')],
  kw=['coisa julgada', 'estabilidade'])
I(P, 1, 'Cautelar antecedente — pedido principal',
  'Efetivada a tutela cautelar, o pedido principal terá de ser formulado pelo autor no prazo de 30 dias, nos mesmos autos, sem adiantamento de novas custas.', 'C',
  'Art. 308.',
  lei=[('L13105:308', 'Efetivada a tutela cautelar', 'adiantamento de novas custas processuais.', 'CPC, art. 308')],
  kw=['cautelar antecedente', '30 dias'])
I(P, 1, 'Tutela da evidência',
  'A tutela da evidência exige a demonstração de perigo de dano ou de risco ao resultado útil do processo.', 'E',
  'Art. 311: a evidência é concedida **independentemente** da demonstração de perigo de dano.',
  lei=[('L13105:311', 'A tutela da evidência será concedida, independentemente da demonstração de perigo de dano', 'resultado útil do processo', 'CPC, art. 311')],
  kw=['evidência', 'sem urgência'])
I(P, 1, 'Responsabilidade do requerente',
  'Independentemente da reparação por dano processual, a parte responde pelo prejuízo que a efetivação da tutela de urgência causar à parte adversa se a sentença lhe for desfavorável.', 'C',
  'Art. 302, I: responsabilidade **objetiva** do beneficiário da tutela.',
  lei=[('L13105:302', 'Independentemente da reparação por dano processual', 'sentença lhe for desfavorável;', 'CPC, art. 302, I')],
  kw=['responsabilidade objetiva'])

# ---------------- PONTO 5 — RODADA 2
I(P, 2, 'Competência',
  'A tutela provisória antecedente será requerida ao juízo competente para conhecer do pedido principal.', 'C',
  'Art. 299: incidental → juízo da causa; antecedente → juízo competente para o **pedido principal**.',
  lei=[('L13105:299', 'A tutela provisória será requerida ao juízo da causa', 'pedido principal.', 'CPC, art. 299')],
  kw=['competência', 'pedido principal'])
I(P, 2, 'Medidas cautelares',
  'A tutela de urgência cautelar pode ser efetivada mediante arresto, sequestro, arrolamento de bens, registro de protesto contra alienação de bem e qualquer outra medida idônea para asseguração do direito.', 'C',
  'Art. 301: rol **exemplificativo** — o poder geral de cautela permanece.',
  lei=[('L13105:301', 'A tutela de urgência de natureza cautelar pode ser efetivada', 'asseguração do direito.', 'CPC, art. 301')],
  kw=['poder geral de cautela', 'arresto', 'sequestro'])
I(P, 2, 'Fungibilidade',
  'Se o juiz entender que o pedido cautelar antecedente tem natureza antecipada, deve indeferi-lo, pois é vedada a fungibilidade entre as tutelas de urgência.', 'E',
  'Art. 305, par. ún.: o juiz **observará o art. 303** — há **fungibilidade**.',
  lei=[('L13105:305', 'Caso entenda que o pedido a que se refere o caput tem natureza antecipada', 'disposto no art. 303', 'CPC, art. 305, par. ún.')],
  kw=['fungibilidade'])
I(P, 2, 'Cessação da eficácia da cautelar',
  'Cessa a eficácia da tutela cautelar concedida em caráter antecedente se ela não for efetivada dentro de 30 dias.', 'C',
  'Art. 309, II. Também cessa se o pedido principal não for deduzido no prazo (I) ou se o juiz julgar improcedente o principal ou extinguir sem mérito (III).',
  lei=[('L13105:309', 'II - não for efetivada dentro de 30 (trinta) dias;', None, 'CPC, art. 309, II')],
  kw=['cessação da eficácia'])
I(P, 2, 'Indeferimento da cautelar',
  'O indeferimento da tutela cautelar não obsta a formulação do pedido principal nem influi no seu julgamento em nenhuma hipótese.', 'E',
  'Art. 310: há exceção — quando o motivo do indeferimento for o reconhecimento de **decadência ou prescrição**.',
  exc=['Indeferimento por decadência ou prescrição influi no pedido principal (art. 310)'],
  lei=[('L13105:310', 'O indeferimento da tutela cautelar não obsta', 'decadência ou de prescrição.', 'CPC, art. 310')],
  kw=['prescrição', 'decadência'])
I(P, 2, 'Evidência liminar',
  'A tutela da evidência fundada no abuso do direito de defesa ou no manifesto propósito protelatório da parte pode ser concedida liminarmente.', 'E',
  'Liminar só nos incisos **II e III** do art. 311. O abuso de defesa (inciso I) pressupõe a defesa já apresentada.',
  lei=[('L13105:311', 'Nas hipóteses dos incisos II e III, o juiz poderá decidir liminarmente.', None, 'CPC, art. 311, par. ún.')],
  kw=['evidência', 'liminar'])
I(P, 2, 'Emenda na antecipada antecedente',
  'Se entender que não há elementos para a concessão de tutela antecipada antecedente, o órgão jurisdicional determinará a emenda da petição inicial em até 5 dias, sob pena de indeferimento e extinção sem resolução de mérito.', 'C',
  'Art. 303, § 6º.',
  lei=[('L13105:303', 'Caso entenda que não há elementos para a concessão de tutela antecipada', 'sem resolução de mérito.', 'CPC, art. 303, § 6º')],
  kw=['emenda', '5 dias'])
I(P, 2, 'Ação para rever a estabilização',
  'Somente o réu tem legitimidade para demandar a revisão, reforma ou invalidação da tutela antecipada estabilizada.', 'E',
  'Art. 304, § 2º: **qualquer das partes** pode demandar a outra.',
  lei=[('L13105:304', 'Qualquer das partes poderá demandar a outra', 'estabilizada nos termos do caput', 'CPC, art. 304, § 2º')],
  kw=['estabilização', 'qualquer das partes'])
I(P, 2, 'Liquidação do prejuízo',
  'A indenização pelo prejuízo causado pela efetivação da tutela de urgência será liquidada nos autos em que a medida tiver sido concedida, sempre que possível.', 'C',
  'Art. 302, par. ún.',
  lei=[('L13105:302', 'A indenização será liquidada nos autos', 'sempre que possível.', 'CPC, art. 302, par. ún.')],
  kw=['liquidação', 'mesmos autos'])
I(P, 2, 'Caução',
  'Para a concessão da tutela de urgência, a caução real ou fidejussória é sempre obrigatória.', 'E',
  'Art. 300, § 1º: a caução é **faculdade do juiz** ("pode") e pode ser **dispensada** se a parte economicamente hipossuficiente não puder oferecê-la.',
  lei=[('L13105:300', 'Para a concessão da tutela de urgência, o juiz pode', 'não puder oferecê-la.', 'CPC, art. 300, § 1º')],
  peg='"Pode" virou "sempre obrigatória".',
  kw=['caução', 'hipossuficiente'])

P = 'DBA26-CPC-6'
# ---------------- PONTO 6 · Formação, suspensão e extinção — RODADA 1
I(P, 1, 'Formação do processo',
  'Considera-se proposta a ação quando a petição inicial for protocolada, mas a propositura só produz quanto ao réu os efeitos do art. 240 depois que ele for validamente citado.', 'C',
  'Art. 312.',
  lei=[('L13105:312', 'Considera-se proposta a ação', 'validamente citado.', 'CPC, art. 312')],
  kw=['propositura', 'citação'])
I(P, 1, 'Suspensão por morte',
  'Suspende-se o processo pela morte ou pela perda da capacidade processual de qualquer das partes, de seu representante legal ou de seu procurador.', 'C',
  'Art. 313, I.',
  lei=[('L13105:313', 'pela morte ou pela perda da capacidade processual', 'de seu procurador;', 'CPC, art. 313, I')],
  kw=['suspensão', 'morte'])
I(P, 1, 'Suspensão convencional — prazo',
  'A suspensão do processo por convenção das partes pode durar até 1 ano.', 'E',
  'Art. 313, § 4º: convenção → **nunca mais de 6 meses**; prejudicialidade (inciso V) → **nunca mais de 1 ano**.',
  lei=[('L13105:313', 'O prazo de suspensão do processo nunca poderá exceder 1 (um) ano', 'prevista no inciso II.', 'CPC, art. 313, § 4º')],
  kw=['convenção', '6 meses'])
I(P, 1, 'Atos durante a suspensão',
  'Durante a suspensão é vedado praticar qualquer ato processual, inclusive os urgentes destinados a evitar dano irreparável.', 'E',
  'Art. 314: o juiz **pode determinar atos urgentes** para evitar dano irreparável (salvo na arguição de impedimento e suspeição).',
  lei=[('L13105:314', 'Durante a suspensão é vedado praticar qualquer ato processual', 'impedimento e de suspeição.', 'CPC, art. 314')],
  kw=['suspensão', 'atos urgentes'])
I(P, 1, 'Extinção sem mérito',
  'O juiz não resolverá o mérito quando verificar ausência de legitimidade ou de interesse processual.', 'C',
  'Art. 485, VI.',
  lei=[('L13105:485', 'VI - verificar ausência de legitimidade ou de interesse processual;', None, 'CPC, art. 485, VI')],
  kw=['extinção sem mérito', 'condições da ação'])
I(P, 1, 'Mérito x sem mérito',
  'Haverá resolução de mérito quando o juiz homologar a desistência da ação.', 'E',
  'Desistência → **sem mérito** (art. 485, VIII). Com mérito é a homologação de **reconhecimento da procedência, transação ou renúncia** (art. 487, III).',
  lei=[('L13105:485', 'VIII - homologar a desistência da ação;', None, 'CPC, art. 485, VIII'),
       ('L13105:487', 'III - homologar:', 'renúncia à pretensão formulada na ação ou na reconvenção.', 'CPC, art. 487, III')],
  peg='Trocar "desistência" (da ação) por "renúncia" (ao direito).',
  kw=['desistência', 'renúncia'])
I(P, 1, 'Desistência após a contestação',
  'Oferecida a contestação, o autor não poderá, sem o consentimento do réu, desistir da ação.', 'C',
  'Art. 485, § 4º.',
  lei=[('L13105:485', 'Oferecida a contestação, o autor não poderá', 'desistir da ação.', 'CPC, art. 485, § 4º')],
  kw=['desistência', 'consentimento do réu'])
I(P, 1, 'Limite temporal da desistência',
  'A desistência da ação pode ser apresentada até o trânsito em julgado.', 'E',
  'Art. 485, § 5º: **até a sentença**.',
  lei=[('L13105:485', 'A desistência da ação pode ser apresentada até a sentença.', None, 'CPC, art. 485, § 5º')],
  kw=['desistência', 'até a sentença'])
I(P, 1, 'Matérias de ofício',
  'O juiz conhecerá de ofício, em qualquer tempo e grau de jurisdição, enquanto não ocorrer o trânsito em julgado, da ausência de pressupostos processuais, da perempção, litispendência ou coisa julgada e da ausência de legitimidade ou interesse.', 'C',
  'Art. 485, § 3º (incisos IV, V, VI e IX).',
  lei=[('L13105:485', 'O juiz conhecerá de ofício da matéria', 'trânsito em julgado.', 'CPC, art. 485, § 3º')],
  kw=['ordem pública', 'de ofício'])
I(P, 1, 'Perempção',
  'Se o autor der causa, por 2 vezes, a sentença fundada em abandono da causa, não poderá propor nova ação contra o réu com o mesmo objeto.', 'E',
  'Art. 486, § 3º: **3 vezes**. Fica ressalvada a alegação do direito em defesa.',
  lei=[('L13105:486', 'Se o autor der causa, por 3 (três) vezes', 'alegar em defesa o seu direito.', 'CPC, art. 486, § 3º')],
  kw=['perempção', '3 vezes'])
I(P, 1, 'Abandono da causa',
  'Mesmo depois de oferecida a contestação, a extinção do processo por abandono da causa pelo autor pode ser decretada de ofício.', 'E',
  'Art. 485, § 6º e Súmula 240/STJ: após a contestação, depende de **requerimento do réu**.',
  lei=[('L13105:485', 'Oferecida a contestação, a extinção do processo por abandono', 'requerimento do réu.', 'CPC, art. 485, § 6º')],
  juris=[J['S240']],
  kw=['abandono', 'requerimento do réu'])
I(P, 1, 'Primazia do mérito',
  'Antes de proferir decisão sem resolução de mérito, o juiz deverá conceder à parte oportunidade para, se possível, corrigir o vício.', 'C',
  'Art. 317: **primazia do julgamento de mérito**.',
  lei=[('L13105:317', 'Antes de proferir decisão sem resolução de mérito', 'corrigir o vício.', 'CPC, art. 317')],
  kw=['primazia do mérito', 'sanabilidade'])

# ---------------- PONTO 6 — RODADA 2
I(P, 2, 'Prejudicialidade criminal',
  'Se o conhecimento do mérito depender da verificação da existência de fato delituoso, o juiz pode suspender o processo; se a ação penal não for proposta em 6 meses, cessa o efeito da suspensão.', 'E',
  'Art. 315, § 1º: o prazo é de **3 meses** contados da intimação do ato de suspensão.',
  lei=[('L13105:315', 'Se a ação penal não for proposta no prazo de 3 (três) meses', 'questão prévia.', 'CPC, art. 315, § 1º')],
  kw=['prejudicial criminal', '3 meses'])
I(P, 2, 'Prejudicialidade criminal — duração',
  'Proposta a ação penal, o processo civil ficará suspenso pelo prazo máximo de 1 ano, ao final do qual o juiz cível examinará incidentemente a questão prévia.', 'C',
  'Art. 315, § 2º.',
  lei=[('L13105:315', 'Proposta a ação penal, o processo ficará suspenso', 'parte final do § 1º.', 'CPC, art. 315, § 2º')],
  kw=['independência das instâncias', '1 ano'])
I(P, 2, 'Paternidade do advogado',
  'Suspende-se o processo por 8 dias quando o advogado responsável pelo processo constituir o único patrono da causa e tornar-se pai.', 'C',
  'Art. 313, X e § 7º: **8 dias** para o pai; **30 dias** para a advogada, pelo parto ou adoção (IX e § 6º).',
  lei=[('L13105:313', 'No caso do inciso X, o período de suspensão será de 8 (oito) dias', None, 'CPC, art. 313, § 7º')],
  kw=['suspensão', 'advogado pai'])
I(P, 2, 'Maternidade da advogada',
  'Pelo parto ou concessão de adoção, quando a advogada for a única patrona da causa, o processo fica suspenso por 60 dias.', 'E',
  'Art. 313, § 6º: **30 dias** contados do parto ou da adoção, mediante comprovação e notificação ao cliente.',
  lei=[('L13105:313', 'No caso do inciso IX, o período de suspensão será de 30 (trinta) dias', None, 'CPC, art. 313, § 6º')],
  kw=['suspensão', 'advogada', '30 dias'])
I(P, 2, 'Retratação na apelação',
  'Interposta apelação contra sentença sem resolução de mérito, o juiz terá 5 dias para retratar-se.', 'C',
  'Art. 485, § 7º.',
  lei=[('L13105:485', 'Interposta a apelação em qualquer dos casos', 'para retratar-se.', 'CPC, art. 485, § 7º')],
  kw=['retratação', 'efeito regressivo'])
I(P, 2, 'Repropositura',
  'A sentença que extingue o processo por ilegitimidade de parte impede, em qualquer caso, a propositura de nova ação.', 'E',
  'Art. 486, § 1º: nova ação é possível, mas depende da **correção do vício** que levou à extinção.',
  lei=[('L13105:486', 'No caso de extinção em razão de litispendência', 'correção do vício que levou à sentença sem resolução do mérito.', 'CPC, art. 486, § 1º')],
  kw=['repropositura', 'correção do vício'])
I(P, 2, 'Intimação pessoal antes da extinção',
  'Nos casos de paralisação do processo por mais de 1 ano por negligência das partes e de abandono pelo autor, a parte será intimada pessoalmente para suprir a falta no prazo de 5 dias.', 'C',
  'Art. 485, § 1º.',
  lei=[('L13105:485', 'Nas hipóteses descritas nos incisos II e III', 'no prazo de 5 (cinco) dias.', 'CPC, art. 485, § 1º')],
  kw=['intimação pessoal', 'abandono'])
I(P, 2, 'Prescrição e contraditório',
  'Ressalvada a improcedência liminar, a prescrição e a decadência não serão reconhecidas sem que antes seja dada às partes oportunidade de manifestar-se.', 'C',
  'Art. 487, par. ún. — aplicação direta do art. 10.',
  lei=[('L13105:487', 'Ressalvada a hipótese do § 1º do art. 332', 'oportunidade de manifestar-se.', 'CPC, art. 487, par. ún.')],
  kw=['prescrição', 'contraditório'])
I(P, 2, 'Questão prejudicial externa',
  'A suspensão do processo por depender o julgamento do mérito de outra causa pode durar até 2 anos.', 'E',
  'Art. 313, § 4º: **nunca mais de 1 ano** nas hipóteses do inciso V; findo o prazo, o juiz manda prosseguir (§ 5º).',
  lei=[('L13105:313', 'O prazo de suspensão do processo nunca poderá exceder 1 (um) ano nas hipóteses do inciso V', None, 'CPC, art. 313, § 4º')],
  kw=['prejudicialidade', '1 ano'])

P = 'DBA26-CPC-7'
# ---------------- PONTO 7 · Conhecimento e cumprimento de sentença — RODADA 1
I(P, 1, 'Petição inicial — requisitos',
  'A petição inicial indicará a opção do autor pela realização ou não de audiência de conciliação ou de mediação.', 'C',
  'Art. 319, VII.',
  lei=[('L13105:319', 'VII - a opção do autor pela realização ou não de audiência de conciliação ou de mediação.', None, 'CPC, art. 319, VII')],
  kw=['petição inicial', 'requisitos'])
I(P, 1, 'Emenda da inicial',
  'Verificando defeitos na petição inicial, o juiz determinará que o autor a emende ou complete no prazo de 10 dias.', 'E',
  'Art. 321: **15 dias**, indicando com precisão o que deve ser corrigido.',
  lei=[('L13105:321', 'determinará que o autor, no prazo de 15 (quinze) dias', 'corrigido ou completado.', 'CPC, art. 321')],
  peg='10 dias era o prazo do CPC/1973.',
  kw=['emenda', '15 dias'])
I(P, 1, 'Improcedência liminar',
  'Nas causas que dispensem a fase instrutória, o juiz, independentemente da citação do réu, julgará liminarmente improcedente o pedido que contrariar enunciado de súmula do STF ou do STJ.', 'C',
  'Art. 332, I. Também: repetitivos, IRDR/IAC, súmula de TJ sobre direito local e prescrição/decadência (§ 1º).',
  lei=[('L13105:332', 'Nas causas que dispensem a fase instrutória', 'Superior Tribunal de Justiça;', 'CPC, art. 332, I')],
  kw=['improcedência liminar'])
I(P, 1, 'Audiência de conciliação — antecedência',
  'A audiência de conciliação ou mediação será designada com antecedência mínima de 30 dias, devendo o réu ser citado com pelo menos 20 dias de antecedência.', 'C',
  'Art. 334, caput: **30 dias** (designação) e **20 dias** (citação).',
  lei=[('L13105:334', 'designará audiência de conciliação ou de mediação com antecedência mínima de 30 (trinta) dias', 'pelo menos 20 (vinte) dias de antecedência.', 'CPC, art. 334')],
  kw=['audiência de conciliação', '30 dias', '20 dias'])
I(P, 1, 'Dispensa da audiência',
  'A audiência de conciliação não será realizada se qualquer das partes manifestar desinteresse na composição consensual.', 'E',
  'Art. 334, § 4º, I: só se **ambas as partes** manifestarem desinteresse (ou quando não se admitir autocomposição).',
  lei=[('L13105:334', 'I - se ambas as partes manifestarem, expressamente, desinteresse na composição consensual;', None, 'CPC, art. 334, § 4º, I')],
  kw=['ambas as partes', 'desinteresse'])
I(P, 1, 'Ausência injustificada',
  'O não comparecimento injustificado do autor ou do réu à audiência de conciliação é ato atentatório à dignidade da justiça, sancionado com multa de até 2% da vantagem econômica pretendida ou do valor da causa.', 'C',
  'Art. 334, § 8º: multa revertida em favor da União ou do Estado.',
  lei=[('L13105:334', 'O não comparecimento injustificado do autor ou do réu', 'em favor da União ou do Estado.', 'CPC, art. 334, § 8º')],
  kw=['ato atentatório', '2%'])
I(P, 1, 'Preliminares de ofício',
  'O juiz pode conhecer de ofício da convenção de arbitragem, como das demais preliminares de contestação.', 'E',
  'Art. 337, § 5º: exceto **convenção de arbitragem** e **incompetência relativa**, o juiz conhece de ofício.',
  exc=['Convenção de arbitragem — não se conhece de ofício (art. 337, § 5º)', 'Incompetência relativa — não se conhece de ofício (art. 337, § 5º)'],
  lei=[('L13105:337', 'Excetuadas a convenção de arbitragem e a incompetência relativa', 'matérias enumeradas neste artigo.', 'CPC, art. 337, § 5º')],
  kw=['arbitragem', 'incompetência relativa'])
I(P, 1, 'Efeitos da revelia',
  'Na revelia, presumem-se verdadeiras as alegações de fato formuladas pelo autor, ainda que o litígio verse sobre direitos indisponíveis.', 'E',
  'Art. 345, II: a presunção **não se aplica** a direitos indisponíveis.',
  exc=['Pluralidade de réus e algum contestar (art. 345, I)', 'Direitos indisponíveis (II)', 'Falta de instrumento indispensável à prova do ato (III)', 'Alegações inverossímeis ou contrárias à prova dos autos (IV)'],
  lei=[('L13105:345', 'A revelia não produz o efeito mencionado no art. 344 se:', None, 'CPC, art. 345'),
       ('L13105:345', 'II - o litígio versar sobre direitos indisponíveis;', None, 'CPC, art. 345, II')],
  kw=['revelia', 'direitos indisponíveis'])
I(P, 1, 'Ônus da prova',
  'O ônus da prova incumbe ao autor, quanto ao fato constitutivo de seu direito, e ao réu, quanto à existência de fato impeditivo, modificativo ou extintivo do direito do autor.', 'C',
  'Art. 373, caput: distribuição **estática**; o § 1º permite a **dinâmica**.',
  lei=[('L13105:373', 'O ônus da prova incumbe:', 'extintivo do direito do autor.', 'CPC, art. 373')],
  kw=['ônus da prova', 'fato constitutivo'])
I(P, 1, 'Limites objetivos da coisa julgada',
  'Fazem coisa julgada os motivos, ainda que importantes para determinar o alcance da parte dispositiva da sentença.', 'E',
  'Art. 504, I: **não** fazem coisa julgada os motivos, nem a verdade dos fatos (II).',
  lei=[('L13105:504', 'Não fazem coisa julgada:', 'parte dispositiva da sentença;', 'CPC, art. 504, I')],
  kw=['coisa julgada', 'motivos'])
I(P, 1, 'Cumprimento — multa e honorários',
  'No cumprimento definitivo de sentença por quantia certa, não ocorrendo o pagamento voluntário em 15 dias, o débito será acrescido de multa de 10% e de honorários de advogado de 10%.', 'C',
  'Art. 523, caput e § 1º.',
  lei=[('L13105:523', 'Não ocorrendo pagamento voluntário no prazo do caput', 'honorários de advogado de dez por cento.', 'CPC, art. 523, § 1º')],
  kw=['cumprimento de sentença', 'multa de 10%'])
I(P, 1, 'Impugnação ao cumprimento',
  'A impugnação ao cumprimento de sentença depende de prévia garantia do juízo por penhora.', 'E',
  'Art. 525: o executado apresenta impugnação em 15 dias **independentemente de penhora ou nova intimação**.',
  lei=[('L13105:525', 'Transcorrido o prazo previsto no art. 523', 'nos próprios autos, sua impugnação.', 'CPC, art. 525')],
  kw=['impugnação', 'sem penhora'])

# ---------------- PONTO 7 — RODADA 2
I(P, 2, 'Autonomia da reconvenção',
  'A desistência da ação ou a ocorrência de causa extintiva que impeça o exame de seu mérito não obsta o prosseguimento do processo quanto à reconvenção.', 'C',
  'Art. 343, § 2º: **autonomia** da reconvenção.',
  lei=[('L13105:343', 'A desistência da ação ou a ocorrência de causa extintiva', 'quanto à reconvenção.', 'CPC, art. 343, § 2º')],
  kw=['reconvenção', 'autonomia'])
I(P, 2, 'Julgamento antecipado parcial',
  'A decisão que julga antecipadamente parte do mérito é impugnável por apelação.', 'E',
  'Art. 356, § 5º: cabe **agravo de instrumento** (decisão interlocutória de mérito).',
  lei=[('L13105:356', 'A decisão proferida com base neste artigo é impugnável por agravo de instrumento.', None, 'CPC, art. 356, § 5º')],
  kw=['julgamento parcial', 'agravo de instrumento'])
I(P, 2, 'Saneamento consensual',
  'As partes podem apresentar ao juiz, para homologação, delimitação consensual das questões de fato e de direito, que, se homologada, vincula as partes e o juiz.', 'C',
  'Art. 357, § 2º: **saneamento consensual**.',
  lei=[('L13105:357', 'As partes podem apresentar ao juiz, para homologação, delimitação consensual', 'vincula as partes e o juiz.', 'CPC, art. 357, § 2º')],
  kw=['saneamento', 'negócio processual'])
I(P, 2, 'Coisa julgada sobre questão prejudicial',
  'A coisa julgada alcança a questão prejudicial decidida expressa e incidentemente, ainda que o réu tenha sido revel.', 'E',
  'Art. 503, § 1º, II: exige **contraditório prévio e efetivo**, **não se aplicando no caso de revelia**.',
  lei=[('L13105:503', 'II - a seu respeito tiver havido contraditório prévio e efetivo', 'no caso de revelia;', 'CPC, art. 503, § 1º, II')],
  kw=['questão prejudicial', 'revelia'])
I(P, 2, 'Remessa necessária — Estados',
  'Não se aplica a remessa necessária quando a condenação ou o proveito econômico for inferior a 500 salários mínimos para os Estados, o DF, suas autarquias e fundações e os Municípios que sejam capitais.', 'C',
  'Art. 496, § 3º, II. União: 1.000 SM; demais Municípios: 100 SM.',
  lei=[('L13105:496', 'II - 500 (quinhentos) salários-mínimos', 'capitais dos Estados;', 'CPC, art. 496, § 3º, II')],
  kw=['remessa necessária', '500 salários mínimos'])
I(P, 2, 'Remessa necessária — Municípios',
  'O limite de 500 salários mínimos para dispensa da remessa necessária aplica-se a todos os Municípios.', 'E',
  'Só aos **Municípios capitais**. Os demais Municípios têm limite de **100 SM** (art. 496, § 3º, III).',
  lei=[('L13105:496', 'III - 100 (cem) salários-mínimos', 'direito público.', 'CPC, art. 496, § 3º, III')],
  kw=['remessa necessária', '100 salários mínimos'])
I(P, 2, 'Cumprimento provisório',
  'O cumprimento provisório corre por iniciativa e responsabilidade do exequente, que se obriga, se a sentença for reformada, a reparar os danos que o executado haja sofrido.', 'C',
  'Art. 520, I: responsabilidade **objetiva** do exequente.',
  lei=[('L13105:520', 'corre por iniciativa e responsabilidade do exequente', 'que o executado haja sofrido;', 'CPC, art. 520, I')],
  kw=['cumprimento provisório', 'responsabilidade'])
I(P, 2, 'Astreintes — intimação pessoal',
  'Para o STJ, a prévia intimação pessoal do devedor é pressuposto para a incidência da multa coercitiva pelo descumprimento de obrigação de fazer ou não fazer, entendimento mantido após o CPC/2015.', 'C',
  'Súmula 410/STJ, reafirmada pela Corte Especial no **Tema 1.296** (2026).',
  juris=[J['S410'], J['T1296']],
  lei=[('L13105:537', 'A multa independe de requerimento da parte', 'determine prazo razoável para cumprimento do preceito.', 'CPC, art. 537')],
  kw=['astreintes', 'intimação pessoal', 'Tema 1.296'])
I(P, 2, 'Astreintes — de ofício',
  'A multa coercitiva para cumprimento de obrigação de fazer depende de requerimento da parte.', 'E',
  'Art. 537: a multa **independe de requerimento** e pode ser fixada em qualquer fase; o juiz pode alterar a **multa vincenda** de ofício (§ 1º).',
  lei=[('L13105:537', 'A multa independe de requerimento da parte', None, 'CPC, art. 537')],
  kw=['astreintes', 'de ofício'])
I(P, 2, 'Pagamento parcial',
  'Efetuado o pagamento parcial no prazo do cumprimento de sentença, ficam afastados integralmente a multa e os honorários de 10%.', 'E',
  'Art. 523, § 2º: multa e honorários incidem **sobre o restante**.',
  lei=[('L13105:523', 'Efetuado o pagamento parcial no prazo previsto no caput', 'incidirão sobre o restante.', 'CPC, art. 523, § 2º')],
  kw=['pagamento parcial', 'restante'])
P = 'DBA26-CPC-8'
# ---------------- PONTO 8 · Execução — RODADA 1
I(P, 1, 'Requisitos do título',
  'A execução para cobrança de crédito fundar-se-á sempre em título de obrigação certa, líquida e exigível.', 'C',
  'Art. 783: **certeza, liquidez e exigibilidade**.',
  lei=[('L13105:783', 'A execução para cobrança de crédito', 'certa, líquida e exigível.', 'CPC, art. 783')],
  kw=['título executivo', 'certa, líquida e exigível'])
I(P, 1, 'Documento particular',
  'É título executivo extrajudicial o documento particular assinado pelo devedor e por 3 testemunhas.', 'E',
  'Art. 784, III: bastam **2 testemunhas**.',
  lei=[('L13105:784', 'III - o documento particular assinado pelo devedor e por 2 (duas) testemunhas;', None, 'CPC, art. 784, III')],
  kw=['título extrajudicial', '2 testemunhas'])
I(P, 1, 'Citação na execução por quantia',
  'Na execução por quantia certa, o executado será citado para pagar a dívida no prazo de 15 dias.', 'E',
  'Art. 829: **3 dias** contados da citação. 15 dias é o prazo do cumprimento de sentença (art. 523) e dos embargos (art. 915).',
  lei=[('L13105:829', 'O executado será citado para pagar a dívida no prazo de 3 (três) dias', 'da citação.', 'CPC, art. 829')],
  peg='Troca entre 3 dias (execução) e 15 dias (cumprimento de sentença).',
  kw=['execução por quantia', '3 dias'])
I(P, 1, 'Penhora em dinheiro',
  'É prioritária a penhora em dinheiro, podendo o juiz, nas demais hipóteses, alterar a ordem preferencial de acordo com as circunstâncias do caso concreto.', 'C',
  'Art. 835, § 1º.',
  lei=[('L13105:835', 'É prioritária a penhora em dinheiro', 'circunstâncias do caso concreto.', 'CPC, art. 835, § 1º')],
  kw=['penhora', 'dinheiro'])
I(P, 1, 'Poupança',
  'É impenhorável a quantia depositada em caderneta de poupança até o limite de 60 salários mínimos.', 'E',
  'Art. 833, X: até **40 salários mínimos**.',
  lei=[('L13105:833', 'X - a quantia depositada em caderneta de poupança, até o limite de 40 (quarenta) salários-mínimos;', None, 'CPC, art. 833, X')],
  kw=['impenhorabilidade', '40 salários mínimos'])
I(P, 1, 'Embargos sem garantia',
  'O executado, independentemente de penhora, depósito ou caução, poderá se opor à execução por meio de embargos.', 'C',
  'Art. 914.',
  lei=[('L13105:914', 'O executado, independentemente de penhora, depósito ou caução', 'por meio de embargos.', 'CPC, art. 914')],
  kw=['embargos à execução', 'sem garantia'])
I(P, 1, 'Prazo dos embargos',
  'Os embargos à execução serão oferecidos no prazo de 15 dias, contados da juntada aos autos do auto de penhora.', 'E',
  'Art. 915: 15 dias contados **na forma do art. 231** — isto é, a partir da **citação**, não da penhora.',
  lei=[('L13105:915', 'Os embargos serão oferecidos no prazo de 15 (quinze) dias', 'na forma do art. 231', 'CPC, art. 915')],
  kw=['embargos', 'termo inicial'])
I(P, 1, 'Efeito suspensivo dos embargos',
  'Os embargos à execução não terão efeito suspensivo, mas o juiz poderá atribuí-lo quando verificados os requisitos da tutela provisória e desde que a execução já esteja garantida por penhora, depósito ou caução suficientes.', 'C',
  'Art. 919, caput e § 1º.',
  lei=[('L13105:919', 'O juiz poderá, a requerimento do embargante', 'caução suficientes.', 'CPC, art. 919, § 1º')],
  kw=['efeito suspensivo', 'garantia do juízo'])
I(P, 1, 'Parcelamento',
  'No prazo para embargos, reconhecendo o crédito e depositando 30% do valor em execução, acrescido de custas e honorários, o executado poderá requerer o pagamento do restante em até 6 parcelas mensais, com correção e juros de 1% ao mês.', 'C',
  'Art. 916, caput (moratória legal).',
  lei=[('L13105:916', 'No prazo para embargos, reconhecendo o crédito do exequente', 'juros de um por cento ao mês.', 'CPC, art. 916')],
  kw=['parcelamento', '30%', '6 parcelas'])
I(P, 1, 'Fraude à execução',
  'O reconhecimento da fraude à execução depende do registro da penhora do bem alienado ou da prova de má-fé do terceiro adquirente.', 'C',
  'Súmula 375/STJ, em linha com o art. 792 (averbação da pendência do processo, da penhora ou hipoteca judiciária).',
  lei=[('L13105:792', 'A alienação ou a oneração de bem é considerada fraude à execução:', None, 'CPC, art. 792')],
  juris=[J['S375']],
  kw=['fraude à execução', 'má-fé', 'registro da penhora'])
I(P, 1, 'Suspensão por falta de bens',
  'Não localizados bens penhoráveis, a execução será suspensa pelo prazo de 2 anos, durante o qual se suspende a prescrição.', 'E',
  'Art. 921, § 1º: suspensão por **1 ano**; depois, arquivamento e curso da **prescrição intercorrente**.',
  lei=[('L13105:921', 'Na hipótese do inciso III, o juiz suspenderá a execução pelo prazo de 1 (um) ano', 'suspenderá a prescrição.', 'CPC, art. 921, § 1º')],
  kw=['prescrição intercorrente', '1 ano'])
I(P, 1, 'Prisão civil do devedor de alimentos',
  'O cumprimento da pena de prisão civil exime o devedor de alimentos do pagamento das prestações vencidas e vincendas.', 'E',
  'Art. 528, § 5º: **não exime**. A prisão é de **1 a 3 meses**, em regime fechado, separado dos presos comuns (§§ 3º e 4º).',
  lei=[('L13105:528', 'O cumprimento da pena não exime o executado do pagamento das prestações vencidas e vincendas.', None, 'CPC, art. 528, § 5º')],
  kw=['prisão civil', 'alimentos'])

# ---------------- PONTO 8 — RODADA 2
I(P, 2, 'Averbação premonitória',
  'Presume-se em fraude à execução a alienação ou a oneração de bens efetuada após a averbação da certidão de admissão da execução.', 'C',
  'Art. 828, § 4º.',
  lei=[('L13105:828', 'Presume-se em fraude à execução a alienação ou a oneração de bens efetuada após a averbação.', None, 'CPC, art. 828, § 4º')],
  kw=['averbação premonitória', 'fraude'])
I(P, 2, 'Intimação do terceiro adquirente',
  'Antes de declarar a fraude à execução, o juiz deverá intimar o terceiro adquirente, que poderá opor embargos de terceiro no prazo de 5 dias.', 'E',
  'Art. 792, § 4º: prazo de **15 dias**.',
  lei=[('L13105:792', 'Antes de declarar a fraude à execução, o juiz deverá intimar o terceiro adquirente', 'no prazo de 15 (quinze) dias.', 'CPC, art. 792, § 4º')],
  kw=['embargos de terceiro', '15 dias'])
I(P, 2, 'Salário e prestação alimentícia',
  'A impenhorabilidade de salários e vencimentos não se aplica à penhora para pagamento de prestação alimentícia, independentemente de sua origem.', 'C',
  'Art. 833, § 2º. A mesma ressalva vale para importâncias que excedam 50 salários mínimos mensais.',
  lei=[('L13105:833', 'O disposto nos incisos IV e X do caput não se aplica à hipótese de penhora para pagamento de prestação alimentícia, independentemente de sua origem', None, 'CPC, art. 833, § 2º')],
  kw=['impenhorabilidade', 'alimentos'])
I(P, 2, 'Medidas executivas atípicas',
  'Segundo o STJ, nas execuções cíveis o juiz pode adotar meios executivos atípicos de forma prioritária, dispensada a ponderação com a menor onerosidade do executado.', 'E',
  'Tema 1.137/STJ: cabem, mas **cumulativamente** com ponderação efetividade x **menor onerosidade**, uso **prioritariamente subsidiário**, fundamentação e contraditório/proporcionalidade.',
  lei=[('L13105:139', 'IV - determinar todas as medidas indutivas, coercitivas, mandamentais ou sub-rogatórias', 'prestação pecuniária;', 'CPC, art. 139, IV')],
  juris=[J['T1137']],
  kw=['medidas atípicas', 'Tema 1.137', 'subsidiariedade'])
I(P, 2, 'Parcelamento x embargos',
  'A opção pelo parcelamento do art. 916 importa renúncia ao direito de opor embargos.', 'C',
  'Art. 916, § 6º.',
  lei=[('L13105:916', 'A opção pelo parcelamento de que trata este artigo importa renúncia ao direito de opor embargos', None, 'CPC, art. 916, § 6º')],
  kw=['parcelamento', 'renúncia'])
I(P, 2, 'Parcelamento no cumprimento de sentença',
  'O parcelamento do art. 916 aplica-se também ao cumprimento da sentença.', 'E',
  'Art. 916, § 7º: **não se aplica** ao cumprimento de sentença.',
  lei=[('L13105:916', 'O disposto neste artigo não se aplica ao cumprimento da sentença.', None, 'CPC, art. 916, § 7º')],
  kw=['parcelamento', 'cumprimento de sentença'])
I(P, 2, 'Curador especial nos embargos',
  'O curador especial nomeado ao executado revel citado por edital não tem legitimidade para opor embargos à execução.', 'E',
  'Súmula 196/STJ: o curador especial **tem legitimidade** para apresentar embargos.',
  juris=[J['S196']],
  lei=[('L13105:72', 'revel citado por edital ou com hora certa', None, 'CPC, art. 72, II')],
  kw=['curador especial', 'embargos'])
I(P, 2, 'Exceção de pré-executividade',
  'A exceção de pré-executividade é admissível na execução fiscal relativamente às matérias conhecíveis de ofício que não demandem dilação probatória.', 'C',
  'Súmula 393/STJ: dois requisitos — matéria de **ordem pública** + **prova pré-constituída**.',
  juris=[J['S393']],
  kw=['exceção de pré-executividade', 'dilação probatória'])
I(P, 2, 'Execução contra a Fazenda',
  'Na execução fundada em título extrajudicial, a Fazenda Pública será citada para opor embargos em 15 dias.', 'E',
  'Art. 910: **30 dias**.',
  lei=[('L13105:910', 'a Fazenda Pública será citada para opor embargos em 30 (trinta) dias.', None, 'CPC, art. 910')],
  kw=['Fazenda Pública', '30 dias'])
I(P, 2, 'Menor onerosidade',
  'Quando por vários meios o exequente puder promover a execução, o juiz mandará que se faça pelo modo menos gravoso para o executado.', 'C',
  'Art. 805. Mas o executado que alegar maior gravosidade deve **indicar outros meios mais eficazes e menos onerosos**, sob pena de manutenção dos atos (par. ún.).',
  lei=[('L13105:805', 'Quando por vários meios o exequente puder promover a execução', 'menos gravoso para o executado.', 'CPC, art. 805')],
  kw=['menor onerosidade'])
