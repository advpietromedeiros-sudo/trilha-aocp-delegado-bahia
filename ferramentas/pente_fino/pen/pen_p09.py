# Pente Fino de Direito Penal (Parte Geral) — PEN-9 (extinção da punibilidade), 9.1 (conceito, causas, momentos) e
# 9.2 (prescrição) (08/11/2026).
from base import I
from pen_juris import J

CP = 'CP:'
ROL = (CP + '107', 'Extingue-se a punibilidade:', None, 'CP, art. 107, caput')
DECAD = (CP + '103', 'Salvo disposição expressa em contrário, o ofendido decai do direito de queixa ou de representação se não o exerce dentro do prazo de 6 (seis) meses', 'do dia em que se esgota o prazo para oferecimento da denúncia', 'CP, art. 103, caput')
P109 = (CP + '109', 'A prescrição, antes de transitar em julgado a sentença final', 'regula-se pelo máximo da pena privativa de liberdade cominada ao crime', 'CP, art. 109, caput')
INTER = (CP + '117', 'O curso da prescrição interrompe-se:', 'pela reincidência', 'CP, art. 117, I a VI')

# ======================= PEN-9 · Extinção da punibilidade =======================
P = 'DBA26-PEN-9'
I(P, 1, 'Natureza das causas',
  'As causas de extinção da punibilidade fazem desaparecer o direito de punir do Estado, mas não apagam o fato típico, ilícito e culpável já praticado.', 'C',
  'Some o **direito de punir**, não o crime: por isso o art. 108 diz que a extinção não se estende a crime de que o extinto era pressuposto ou elemento.',
  lei=[ROL, (CP + '108', 'A extinção da punibilidade de crime que é pressuposto, elemento constitutivo ou circunstância agravante de outro não se estende a este.', None, 'CP, art. 108, 1ª parte')],
  kw=['direito de punir'])
I(P, 1, 'Declaração de ofício',
  'A extinção da punibilidade depende sempre de requerimento da defesa, não podendo o juiz reconhecê-la de ofício.', 'E',
  'A extinção da punibilidade é matéria de **ordem pública**: o juiz a declara **de ofício** em qualquer fase (CPP, art. 61).',
  lei=[('CPP:61', 'Em qualquer fase do processo, o juiz, se reconhecer extinta a punibilidade, deverá declará-lo de ofício.', None, 'CPP, art. 61, caput')],
  peg='Exigir requerimento.', kw=['de ofício', 'ordem pública'])
I(P, 1, 'Juiz da execução',
  'Compete ao juiz da execução declarar extinta a punibilidade após o trânsito em julgado da condenação.', 'C',
  'Após o trânsito, cabe ao **juiz da execução** declarar extinta a punibilidade (LEP, art. 66, II).',
  lei=[('L7210:66', 'declarar extinta a punibilidade', None, 'LEP, art. 66, II')],
  kw=['juiz da execução'])
I(P, 1, 'Medida de segurança',
  'Extinta a punibilidade, subsiste a medida de segurança já imposta, por ter natureza curativa.', 'E',
  'Art. 96, par. ún.: extinta a punibilidade, **não se impõe** medida de segurança **nem subsiste** a que tenha sido imposta.',
  lei=[(CP + '96', 'Extinta a punibilidade, não se impõe medida de segurança nem subsiste a que tenha sido imposta.', None, 'CP, art. 96, par. ún.')],
  peg='Manter a medida de segurança.', kw=['nem subsiste'])
I(P, 1, 'Extinção e concurso',
  'No concurso de crimes, a extinção da punibilidade incide sobre a pena de cada um, isoladamente.', 'C',
  'Art. 119.',
  lei=[(CP + '119', 'No caso de concurso de crimes, a extinção da punibilidade incidirá sobre a pena de cada um, isoladamente.', None, 'CP, art. 119')],
  kw=['isoladamente'])
# --- PEN-9 · Rodada 2
I(P, 2, 'Suspensão condicional do processo',
  'Expirado o prazo da suspensão condicional do processo sem revogação, o juiz declarará extinta a punibilidade.', 'C',
  'Causa extintiva **fora do art. 107** (Lei 9.099/1995, art. 89, § 5º) — prova de que o rol é exemplificativo.',
  lei=[('L9099:89', 'Expirado o prazo sem revogação, o Juiz declarará extinta a punibilidade.', None, 'Lei 9.099/1995, art. 89, § 5º')],
  kw=['suspensão condicional do processo'])
I(P, 2, 'Composição civil',
  'Na ação pública condicionada à representação de menor potencial ofensivo, o acordo de composição civil homologado acarreta a renúncia ao direito de representação.', 'C',
  'Na **composição civil** homologada, o acordo acarreta a **renúncia** ao direito de queixa ou representação (Lei 9.099/1995, art. 74, par. ún.).',
  lei=[('L9099:74', 'Tratando-se de ação penal de iniciativa privada ou de ação penal pública condicionada à representação', 'acarreta a renúncia ao direito de queixa ou representação', 'Na **composição civil** homologada, o acordo acarreta a **renúncia** ao direito de queixa ou representação (Lei 9.099/1995, art. 74, par. ún.).')],
  kw=['composição civil', 'renúncia'])
I(P, 2, 'Sursis expirado',
  'Expirado o prazo do sursis sem revogação, considera-se cumprida a pena e extinta a punibilidade apenas se o condenado requerer.', 'E',
  'Art. 82: expirado o prazo sem revogação, **considera-se extinta** a pena privativa — efeito automático, declarado pelo juiz.',
  lei=[(CP + '82', 'Expirado o prazo sem que tenha havido revogação, considera-se extinta a pena privativa de liberdade.', None, 'CP, art. 82')],
  peg='Condicionar a extinção a requerimento.', kw=['considera-se extinta'])

# ======================= PEN-9.1 · Conceito, causas gerais e específicas, momentos =======================
P = 'DBA26-PEN-9.1'
I(P, 1, 'Causas gerais e específicas',
  'Causas gerais de extinção da punibilidade aplicam-se a todos os crimes, como a morte e a prescrição; específicas, só a alguns, como a retratação na calúnia ou o ressarcimento no peculato culposo.', 'C',
  'Classificação doutrinária; as **gerais** estão sobretudo no art. 107, as **específicas** na Parte Especial (arts. 143, 312, § 3º, 342, § 2º).',
  lei=[ROL, (CP + '312', 'a reparação do dano, se precede à sentença irrecorrível, extingue a punibilidade', None, 'CP, art. 312, § 3º')],
  kw=['causas gerais', 'causas específicas'])
I(P, 1, 'Momentos',
  'As causas extintivas podem ocorrer antes do trânsito em julgado, atingindo a pretensão punitiva, ou depois dele, atingindo a pretensão executória.', 'C',
  'Ex.: a prescrição da pretensão **punitiva** (art. 109) apaga todos os efeitos; a da pretensão **executória** (art. 110) só impede a execução da pena, mantendo os efeitos secundários.',
  lei=[P109, (CP + '110', 'A prescrição depois de transitar em julgado a sentença condenatória regula-se pela pena aplicada', None, 'CP, art. 110, caput')],
  kw=['pretensão punitiva', 'pretensão executória'])
I(P, 1, 'Decadência: prazo',
  'O ofendido decai do direito de queixa ou de representação se não o exercer em 6 meses, contados do dia em que veio a saber quem é o autor do crime.', 'C',
  'Art. 103, caput: prazo **decadencial**, de natureza **penal** (conta-se o dia do começo, art. 10), que não se suspende nem se interrompe.',
  lei=[DECAD], kw=['decadência', '6 meses'])
I(P, 1, 'Decadência na violência doméstica',
  'Nos crimes praticados no âmbito de violência doméstica e familiar contra a mulher, o prazo de decadência do direito de queixa ou de representação continua sendo de 6 meses.', 'E',
  'A **Lei 15.438/2026** incluiu o par. ún. no art. 103: nesses crimes, o prazo é de **12 meses**, com o mesmo termo inicial.',
  lei=[(CP + '103', 'Nos crimes praticados no âmbito de violência doméstica e familiar contra a mulher, a ofendida decai do direito de queixa ou de representação se não o exerce no prazo de 12 (doze) meses', None, 'CP, art. 103, par. ún.')],
  peg='Cobrar o prazo antigo de 6 meses.', kw=['12 meses', 'Lei 15.438/2026'])
I(P, 1, 'Renúncia tácita',
  'Importa renúncia tácita ao direito de queixa receber o ofendido a indenização do dano causado pelo crime.', 'E',
  'Art. 104, par. ún.: a renúncia tácita é ato incompatível com a vontade de exercer a queixa, mas **não a implica** receber a indenização (salvo a regra especial do art. 74 da Lei 9.099/1995 no menor potencial ofensivo).',
  lei=[(CP + '104', 'Importa renúncia tácita ao direito de queixa a prática de ato incompatível com a vontade de exercê-lo', 'o fato de receber o ofendido a indenização do dano causado pelo crime', 'CP, art. 104, par. ún.')],
  exc=['Juizado Especial: composição civil homologada = renúncia (Lei 9.099/1995, art. 74, par. ún.)'],
  peg='Ver renúncia no recebimento da indenização.', kw=['renúncia tácita', 'indenização'])
I(P, 1, 'Perdão: extensão',
  'O perdão, no processo ou fora dele, concedido a qualquer dos querelados, a todos aproveita, mas não produz efeito em relação ao que o recusa.', 'C',
  'Art. 106, I e III: o perdão é **bilateral** (exige aceitação).',
  lei=[(CP + '106', 'se concedido a qualquer dos querelados, a todos aproveita', None, 'CP, art. 106, I'),
       (CP + '106', 'se o querelado o recusa, não produz efeito', None, 'CP, art. 106, III')],
  kw=['perdão', 'bilateral'])
I(P, 1, 'Perdão após o trânsito',
  'O perdão do ofendido é admissível até o início da execução da pena.', 'E',
  'Não é admissível o perdão **depois que passa em julgado** a sentença condenatória (art. 106, § 2º).',
  lei=[(CP + '106', 'Não é admissível o perdão depois que passa em julgado a sentença condenatória.', None, 'CP, art. 106, § 2º')],
  peg='Esticar o perdão até a execução.', kw=['passa em julgado'])
I(P, 1, 'Representação irretratável',
  'A representação será irretratável depois de oferecida a denúncia.', 'C',
  'Art. 102 do CP (o CPP, art. 25, tem a mesma regra).',
  lei=[(CP + '102', 'A representação será irretratável depois de oferecida a denúncia.', None, 'CP, art. 102')],
  kw=['irretratável', 'oferecida a denúncia'])
I(P, 1, 'Morte do ofendido',
  'Morto o ofendido, o direito de oferecer queixa ou de prosseguir na ação passa ao cônjuge, ascendente, descendente ou irmão.', 'C',
  'Art. 100, § 4º (CADI). Exceção: na ação privada **personalíssima** não há sucessão.',
  lei=[(CP + '100', 'No caso de morte do ofendido ou de ter sido declarado ausente por decisão judicial', 'cônjuge, ascendente, descendente ou irmão', 'CP, art. 100, § 4º')],
  kw=['CADI', 'sucessão processual'])
# --- PEN-9.1 · Rodada 2
I(P, 2, 'Perdão por um dos ofendidos',
  'O perdão concedido por um dos ofendidos estende-se aos demais, que perdem o direito de prosseguir na ação.', 'E',
  'Art. 106, II: o perdão concedido por um dos ofendidos **não prejudica o direito dos outros**.',
  lei=[(CP + '106', 'se concedido por um dos ofendidos, não prejudica o direito dos outros', None, 'CP, art. 106, II')],
  peg='Confundir extensão aos querelados com extensão aos ofendidos.', kw=['não prejudica o direito dos outros'])
I(P, 2, 'Perdão tácito',
  'O perdão do ofendido só produz efeito se concedido de forma expressa e nos autos do processo.', 'E',
  'Art. 106, caput e § 1º: o perdão pode ser dado **no processo ou fora dele**, expresso ou **tácito** — este resulta de ato incompatível com a vontade de prosseguir na ação.',
  lei=[(CP + '106', 'Perdão tácito é o que resulta da prática de ato incompatível com a vontade de prosseguir na ação.', None, 'CP, art. 106, § 1º')],
  kw=['perdão tácito'])
I(P, 2, 'Multa e extinção',
  'Pela tese revisada do Tema 931 do STJ, a alegada hipossuficiência do condenado permite extinguir a punibilidade mesmo sem o pagamento da multa, salvo decisão concretamente motivada em sentido contrário.', 'C',
  '**Tema 931/STJ** (28/02/2024).',
  juris=[J['T931']], kw=['Tema 931/STJ'])
I(P, 2, 'Perdão judicial e efeitos',
  'A sentença que concede o perdão judicial é condenatória e mantém os efeitos secundários, inclusive a reincidência.', 'E',
  'É **declaratória** (Súmula 18/STJ) e não gera reincidência (art. 120).',
  lei=[(CP + '120', 'A sentença que conceder perdão judicial não será considerada para efeitos de reincidência.', None, 'CP, art. 120')],
  juris=[J['S18']], peg='Natureza condenatória do perdão judicial.', kw=['Súmula 18/STJ', 'declaratória'])
I(P, 2, 'Anistia e efeitos',
  'A anistia, por recair sobre fatos, apaga os efeitos penais da condenação, mas não afasta os efeitos civis, como a obrigação de indenizar.', 'C',
  'Diferente do indulto, que só atinge efeitos primários (Súmula 631/STJ). A obrigação civil permanece (art. 91, I).',
  lei=[(CP + '107', 'pela anistia, graça ou indulto', None, 'CP, art. 107, II')], juris=[J['S631']],
  kw=['anistia', 'efeitos civis'])
I(P, 2, 'Abolitio e efeitos civis',
  'A abolitio criminis faz cessar a execução e os efeitos penais da sentença condenatória, inclusive a obrigação de reparar o dano.', 'E',
  'Cessam os **efeitos penais** (art. 2º); os **civis** permanecem.',
  lei=[(CP + '2', 'cessando em virtude dela a execução e os efeitos penais da sentença condenatória', None, 'CP, art. 2º, caput')],
  peg='Apagar o efeito civil.', kw=['efeitos penais', 'efeitos civis'])

# ======================= PEN-9.2 · Prescrição =======================
P = 'DBA26-PEN-9.2'
I(P, 1, 'Prescrição em abstrato',
  'Antes do trânsito em julgado, a prescrição regula-se pelo máximo da pena privativa de liberdade cominada ao crime.', 'C',
  'Art. 109, caput: prescrição da pretensão punitiva **em abstrato**.',
  lei=[P109], kw=['máximo da pena cominada'])
I(P, 1, 'Tabela: pena máxima de 4 anos',
  'Se o máximo da pena é superior a dois anos e não excede a quatro, a prescrição ocorre em oito anos.', 'C',
  'Art. 109, IV.',
  lei=[(CP + '109', 'em oito anos, se o máximo da pena é superior a dois anos e não excede a quatro', None, 'CP, art. 109, IV')],
  kw=['oito anos'])
I(P, 1, 'Pena inferior a um ano',
  'Se o máximo da pena é inferior a um ano, a prescrição ocorre em dois anos.', 'E',
  'Desde a Lei 12.234/2010, o prazo é de **3 anos** (art. 109, VI). Dois anos é a prescrição da **multa** isolada (art. 114, I).',
  lei=[(CP + '109', 'em 3 (três) anos, se o máximo da pena é inferior a 1 (um) ano', None, 'CP, art. 109, VI')],
  peg='Cobrar o prazo antigo de 2 anos.', kw=['3 anos', 'Lei 12.234/2010'])
I(P, 1, 'Retroativa: termo',
  'A prescrição retroativa, regulada pela pena aplicada com trânsito em julgado para a acusação, não pode ter por termo inicial data anterior à da denúncia ou queixa.', 'C',
  'Art. 110, § 1º (Lei 12.234/2010): acabou a retroativa entre o fato e o recebimento da denúncia.',
  lei=[(CP + '110', 'A prescrição, depois da sentença condenatória com trânsito em julgado para a acusação', 'data anterior à da denúncia ou queixa', 'CP, art. 110, § 1º')],
  kw=['retroativa', 'denúncia ou queixa'])
I(P, 1, 'Reincidência e prazo',
  'A reincidência aumenta de um terço o prazo da prescrição da pretensão punitiva.', 'E',
  'O aumento de 1/3 vale só para a prescrição **executória** (art. 110, caput). Na **punitiva**, a reincidência **não influi** (Súmula 220/STJ).',
  lei=[(CP + '110', 'os quais se aumentam de um terço, se o condenado é reincidente', None, 'CP, art. 110, caput')],
  juris=[J['S220']], peg='Aplicar o aumento à pretensão punitiva.', kw=['Súmula 220/STJ', 'executória'])
I(P, 1, 'Redução pela idade',
  'São reduzidos de metade os prazos de prescrição quando o agente era, ao tempo do crime, menor de 21 anos ou, na data da sentença, maior de 70 anos, salvo se o crime envolver violência sexual contra a mulher.', 'C',
  'Art. 115, na redação da **Lei 15.160/2025**, que criou a ressalva da violência sexual contra a mulher.',
  lei=[(CP + '115', 'São reduzidos de metade os prazos de prescrição', 'salvo se o crime envolver violência sexual contra a mulher', 'CP, art. 115')],
  kw=['reduzidos de metade', 'Lei 15.160/2025'])
I(P, 1, 'Termo inicial na tentativa',
  'No caso de tentativa, a prescrição começa a correr do dia em que cessou a atividade criminosa.', 'C',
  'Art. 111, II; consumado, do dia da consumação (I); permanente, da cessação da permanência (III).',
  lei=[(CP + '111', 'no caso de tentativa, do dia em que cessou a atividade criminosa', None, 'CP, art. 111, II')],
  kw=['tentativa', 'cessou a atividade'])
I(P, 1, 'Bigamia',
  'Nos crimes de bigamia e de falsificação de assentamento do registro civil, a prescrição corre da data do fato.', 'E',
  'Art. 111, IV: corre da data em que o fato **se tornou conhecido**.',
  lei=[(CP + '111', 'nos de bigamia e nos de falsificação ou alteração de assentamento do registro civil, da data em que o fato se tornou conhecido', None, 'CP, art. 111, IV')],
  peg='Trocar conhecimento do fato pela data do fato.', kw=['se tornou conhecido'])
I(P, 1, 'Causas interruptivas',
  'Interrompem a prescrição o recebimento da denúncia ou queixa, a pronúncia, a decisão confirmatória da pronúncia, a publicação da sentença ou acórdão condenatórios recorríveis, o início ou continuação do cumprimento da pena e a reincidência.', 'C',
  'Art. 117, I a VI. Interrompida, o prazo **recomeça do zero** (§ 2º), salvo no caso do inciso V.',
  lei=[INTER], kw=['causas interruptivas', 'recomeça'])
I(P, 1, 'Oferecimento da denúncia',
  'O oferecimento da denúncia interrompe a prescrição.', 'E',
  'Interrompe o **recebimento** (art. 117, I), não o oferecimento.',
  lei=[(CP + '117', 'pelo recebimento da denúncia ou da queixa', None, 'CP, art. 117, I')],
  peg='Trocar recebimento por oferecimento.', kw=['recebimento'])
# --- PEN-9.2 · Rodada 2
I(P, 2, 'Acórdão confirmatório',
  'O acórdão que apenas confirma a sentença condenatória não interrompe a prescrição, pois não é "acórdão condenatório".', 'E',
  'STF (**HC 176.473**, Plenário) e STJ (**Tema 1.100**): o acórdão condenatório **sempre interrompe**, inclusive quando confirmatório, mantendo, reduzindo ou aumentando a pena.',
  juris=[J['HC176473'], J['T1100']], peg='Exigir acórdão que reforma absolvição.', kw=['HC 176.473', 'Tema 1.100/STJ'])
I(P, 2, 'Termo inicial da executória',
  'A prescrição da pretensão executória começa a correr do trânsito em julgado da condenação para ambas as partes, para os casos em que o trânsito para a acusação ocorreu após 11/11/2020.', 'C',
  '**Tema 788/RG** do STF: o art. 112, I, do CP ("trânsito em julgado para a acusação") foi reinterpretado à luz da presunção de inocência, com modulação.',
  lei=[(CP + '112', 'do dia em que transita em julgado a sentença condenatória, para a acusação', None, 'CP, art. 112, I')],
  juris=[J['RG788']], kw=['Tema 788/RG', 'ambas as partes'])
I(P, 2, 'Prescrição virtual',
  'O STJ admite a prescrição em perspectiva (virtual), calculada pela pena que provavelmente será aplicada, para evitar processo inútil.', 'E',
  'A **Súmula 438/STJ** declara **inadmissível** a prescrição com base em pena hipotética.',
  juris=[J['S438']], peg='Aceitar a prescrição virtual.', kw=['Súmula 438/STJ', 'pena hipotética'])
I(P, 1, 'Crime continuado',
  'No crime continuado, a prescrição regula-se pela pena total imposta na sentença, incluído o acréscimo decorrente da continuação.', 'E',
  '**Súmula 497/STF**: não se computa o **acréscimo** da continuação — coerente com o art. 119 (extinção crime a crime).',
  juris=[J['STF497']], kw=['Súmula 497/STF'])
I(P, 2, 'Pronúncia e desclassificação',
  'Se o Tribunal do Júri desclassificar o crime, a pronúncia perde o efeito interruptivo da prescrição.', 'E',
  '**Súmula 191/STJ**: a pronúncia interrompe a prescrição **ainda que** o júri desclassifique.',
  juris=[J['S191']], peg='Retirar o efeito da pronúncia.', kw=['Súmula 191/STJ'])
I(P, 2, 'Suspensão: ANPP e recursos inadmissíveis',
  'Antes do trânsito em julgado, a prescrição não corre enquanto não cumprido ou não rescindido o acordo de não persecução penal e na pendência de embargos de declaração ou recursos aos tribunais superiores, quando inadmissíveis.', 'C',
  'Art. 116, III e IV (Lei 13.964/2019).',
  lei=[(CP + '116', 'na pendência de embargos de declaração ou de recursos aos Tribunais Superiores, quando inadmissíveis', 'enquanto não cumprido ou não rescindido o acordo de não persecução penal', 'CP, art. 116, III e IV')],
  kw=['acordo de não persecução penal', 'causas suspensivas'])
I(P, 2, 'Suspensão no art. 366',
  'O período de suspensão do prazo prescricional do art. 366 do CPP é regulado pelo máximo da pena cominada.', 'C',
  '**Súmula 415/STJ**: depois disso, a prescrição volta a correr.',
  juris=[J['S415']], kw=['Súmula 415/STJ'])
I(P, 2, 'Interrupção e coautores',
  'A interrupção da prescrição pela reincidência de um dos autores estende-se aos demais coautores.', 'E',
  'Art. 117, § 1º: a interrupção alcança todos os autores, **exceto** nos casos dos incisos **V** (início ou continuação do cumprimento) e **VI** (reincidência), que são pessoais.',
  lei=[(CP + '117', 'Excetuados os casos dos incisos V e VI deste artigo, a interrupção da prescrição produz efeitos relativamente a todos os autores do crime.', None, 'CP, art. 117, § 1º, 1ª parte')],
  peg='Comunicar causa pessoal de interrupção.', kw=['incisos V e VI', 'pessoais'])
I(P, 1, 'Medidas socioeducativas',
  'Por não serem penas, as medidas socioeducativas não se sujeitam à prescrição penal.', 'E',
  '**Súmula 338/STJ**: a prescrição penal é **aplicável** às medidas socioeducativas.',
  juris=[J['S338']], kw=['Súmula 338/STJ'])
I(P, 2, 'Evasão e livramento revogado',
  'No caso de evasão do condenado ou de revogação do livramento condicional, a prescrição é regulada pelo total da pena aplicada.', 'E',
  'Art. 113: regula-se pelo **tempo que resta** da pena.',
  lei=[(CP + '113', 'No caso de evadir-se o condenado ou de revogar-se o livramento condicional, a prescrição é regulada pelo tempo que resta da pena.', None, 'CP, art. 113')],
  peg='Usar a pena total.', kw=['tempo que resta'])
