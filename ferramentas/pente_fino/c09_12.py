from base import I, J

P = 'DBA26-CPC-9'
# ---------------- PONTO 9 · Tribunais e meios de impugnação — RODADA 1
I(P, 1, 'Rol de recursos',
  'São cabíveis no CPC os embargos infringentes contra acórdão não unânime que reformar sentença de mérito.', 'E',
  'O art. 994 **não prevê embargos infringentes**. No lugar deles entrou a **técnica de ampliação do colegiado** (art. 942), que não é recurso.',
  lei=[('L13105:994', 'São cabíveis os seguintes recursos:', 'embargos de divergência.', 'CPC, art. 994')],
  kw=['rol taxativo', 'embargos infringentes', 'art. 942'])
I(P, 1, 'Prazo recursal',
  'Excetuados os embargos de declaração, o prazo para interpor os recursos e para responder-lhes é de 15 dias.', 'C',
  'Art. 1.003, § 5º. Embargos de declaração: **5 dias** (art. 1.023).',
  lei=[('L13105:1003', 'Excetuados os embargos de declaração', 'é de 15 (quinze) dias.', 'CPC, art. 1.003, § 5º')],
  kw=['prazo recursal', '15 dias'])
I(P, 1, 'Interlocutórias não agraváveis',
  'As questões resolvidas na fase de conhecimento cuja decisão não comporte agravo de instrumento não são cobertas pela preclusão e devem ser suscitadas em preliminar de apelação ou nas contrarrazões.', 'C',
  'Art. 1.009, § 1º: **preclusão diferida**.',
  lei=[('L13105:1009', 'As questões resolvidas na fase de conhecimento', 'ou nas contrarrazões.', 'CPC, art. 1.009, § 1º')],
  kw=['preclusão', 'preliminar de apelação'])
I(P, 1, 'Efeito suspensivo da apelação',
  'A apelação contra sentença que condena a pagar alimentos é recebida, em regra, com efeito suspensivo.', 'E',
  'Regra: a apelação tem efeito suspensivo (art. 1.012). Mas a sentença que **condena a pagar alimentos** produz efeitos **imediatamente** (§ 1º, II).',
  exc=['Homologa divisão ou demarcação (I)', 'Condena a pagar alimentos (II)', 'Extingue sem mérito ou julga improcedentes os embargos do executado (III)', 'Julga procedente a instituição de arbitragem (IV)', 'Confirma, concede ou revoga tutela provisória (V)', 'Decreta a interdição (VI)'],
  lei=[('L13105:1012', 'A apelação terá efeito suspensivo.', None, 'CPC, art. 1.012'),
       ('L13105:1012', 'II - condena a pagar alimentos;', None, 'CPC, art. 1.012, § 1º, II')],
  kw=['efeito suspensivo', 'alimentos'])
I(P, 1, 'Taxatividade mitigada',
  'Para o STJ, o rol do art. 1.015 do CPC é de taxatividade mitigada, admitindo agravo de instrumento quando verificada urgência decorrente da inutilidade do julgamento da questão no recurso de apelação.', 'C',
  'Tema 988/STJ.',
  lei=[('L13105:1015', 'Cabe agravo de instrumento contra as decisões interlocutórias que versarem sobre:', None, 'CPC, art. 1.015')],
  juris=[J['T988']],
  kw=['agravo de instrumento', 'taxatividade mitigada', 'Tema 988'])
I(P, 1, 'Admissibilidade da apelação',
  'Interposta a apelação, o juiz de primeiro grau exerce o juízo de admissibilidade antes de remeter os autos ao tribunal.', 'E',
  'Art. 1.010, § 3º: os autos sobem **independentemente de juízo de admissibilidade**. Se o juiz trancar a apelação, cabe **reclamação** (Tema 1.267/STJ).',
  lei=[('L13105:1010', 'Após as formalidades previstas nos §§ 1º e 2º', 'independentemente de juízo de admissibilidade.', 'CPC, art. 1.010, § 3º')],
  juris=[J['T1267']],
  kw=['juízo de admissibilidade', 'reclamação', 'Tema 1.267'])
I(P, 1, 'Embargos de declaração — cabimento e prazo',
  'Cabem embargos de declaração contra qualquer decisão judicial, no prazo de 5 dias, para esclarecer obscuridade, eliminar contradição, suprir omissão ou corrigir erro material.', 'C',
  'Arts. 1.022 e 1.023.',
  lei=[('L13105:1022', 'Cabem embargos de declaração contra qualquer decisão judicial para:', None, 'CPC, art. 1.022'),
       ('L13105:1023', 'Os embargos serão opostos, no prazo de 5 (cinco) dias', None, 'CPC, art. 1.023')],
  kw=['embargos de declaração', '5 dias'])
I(P, 1, 'Embargos de declaração — efeitos',
  'Os embargos de declaração não possuem efeito suspensivo e suspendem o prazo para a interposição de recurso.', 'E',
  'Art. 1.026: não têm efeito suspensivo (certo), mas **interrompem** — não suspendem — o prazo: ele volta a correr do zero.',
  lei=[('L13105:1026', 'Os embargos de declaração não possuem efeito suspensivo', 'interposição de recurso.', 'CPC, art. 1.026')],
  peg='Interromper (o prazo recomeça inteiro) x suspender (retoma o que sobrou).',
  kw=['interrupção', 'efeito suspensivo'])
I(P, 1, 'Prazo da rescisória',
  'O direito à rescisão se extingue em 2 anos contados do trânsito em julgado da última decisão proferida no processo.', 'C',
  'Art. 975, caput.',
  lei=[('L13105:975', 'O direito à rescisão se extingue em 2 (dois) anos', 'última decisão proferida no processo.', 'CPC, art. 975')],
  kw=['ação rescisória', '2 anos'])
I(P, 1, 'Hipóteses da rescisória',
  'Cabe ação rescisória contra decisão de mérito transitada em julgado proferida por juiz suspeito.', 'E',
  'Art. 966, II: juiz **impedido** ou juízo **absolutamente incompetente**. Suspeição e incompetência relativa não rendem rescisória.',
  lei=[('L13105:966', 'II - for proferida por juiz impedido ou por juízo absolutamente incompetente;', None, 'CPC, art. 966, II')],
  peg='"Impedido" trocado por "suspeito".',
  kw=['rescisória', 'impedimento', 'suspeição'])
I(P, 1, 'IRDR — cabimento',
  'É cabível o incidente de resolução de demandas repetitivas quando houver, simultaneamente, efetiva repetição de processos que contenham controvérsia sobre a mesma questão unicamente de direito e risco de ofensa à isonomia e à segurança jurídica.', 'C',
  'Art. 976: dois requisitos **cumulativos**. Não cabe IRDR preventivo nem sobre questão de fato.',
  lei=[('L13105:976', 'É cabível a instauração do incidente de resolução de demandas repetitivas quando houver, simultaneamente:', 'à segurança jurídica.', 'CPC, art. 976')],
  kw=['IRDR', 'questão de direito'])
I(P, 1, 'Reclamação após o trânsito',
  'É admissível a reclamação proposta após o trânsito em julgado da decisão reclamada, desde que dentro de 2 anos.', 'E',
  'Art. 988, § 5º, I e Súmula 734/STF: a reclamação proposta após o trânsito em julgado é **liminarmente indeferida** (redação da Lei 15.484/2026; antes, \"inadmissível\").',
  lei=[('L13105:988', 'Será liminarmente indeferida a reclamação:', None, 'CPC, art. 988, § 5º (Lei 15.484/2026)'), ('L13105:988', 'I – proposta após o trânsito em julgado da decisão reclamada;', None, 'CPC, art. 988, § 5º, I')],
  juris=[J['STF734']],
  kw=['reclamação', 'trânsito em julgado'])

# ---------------- PONTO 9 — RODADA 2
I(P, 2, 'Ampliação do colegiado — exclusões',
  'A técnica de ampliação do colegiado do art. 942 aplica-se ao julgamento não unânime do IRDR e da remessa necessária.', 'E',
  'Art. 942, § 4º: **não** se aplica ao IAC, ao IRDR, à remessa necessária nem ao julgamento do plenário ou da corte especial.',
  exc=['IAC e IRDR (§ 4º, I)', 'Remessa necessária (§ 4º, II)', 'Não unânime do plenário ou corte especial (§ 4º, III)'],
  lei=[('L13105:942', 'Não se aplica o disposto neste artigo ao julgamento:', 'pelo plenário ou pela corte especial.', 'CPC, art. 942, § 4º')],
  kw=['art. 942', 'ampliação do colegiado'])
I(P, 2, 'Ratificação do recurso',
  'Não é necessário ratificar o recurso especial interposto na pendência do julgamento dos embargos de declaração, quando inalterado o resultado anterior.', 'C',
  'Súmula 579/STJ e art. 1.024, § 5º.',
  lei=[('L13105:1024', 'Se os embargos de declaração forem rejeitados ou não alterarem a conclusão do julgamento anterior', 'independentemente de ratificação.', 'CPC, art. 1.024, § 5º')],
  juris=[J['S579']],
  kw=['ratificação', 'embargos de declaração'])
I(P, 2, 'Prequestionamento ficto',
  'Consideram-se incluídos no acórdão os elementos que o embargante suscitou para fins de prequestionamento, ainda que os embargos de declaração sejam inadmitidos ou rejeitados, caso o tribunal superior considere existentes erro, omissão, contradição ou obscuridade.', 'C',
  'Art. 1.025: **prequestionamento ficto**, que superou na prática a lógica da Súmula 211/STJ.',
  lei=[('L13105:1025', 'Consideram-se incluídos no acórdão', 'contradição ou obscuridade.', 'CPC, art. 1.025')],
  juris=[J['S211']],
  kw=['prequestionamento ficto'])
I(P, 2, 'Embargos protelatórios',
  'Quando manifestamente protelatórios os embargos de declaração, o embargante será condenado, já na primeira oposição, a multa de até 10% sobre o valor atualizado da causa.', 'E',
  'Art. 1.026, § 2º: na primeira vez, multa **não excedente a 2%**; na **reiteração**, até **10%** (§ 3º).',
  lei=[('L13105:1026', 'Quando manifestamente protelatórios os embargos de declaração', 'sobre o valor atualizado da causa.', 'CPC, art. 1.026, § 2º')],
  kw=['embargos protelatórios', '2%', '10%'])
I(P, 2, 'RE contra liminar',
  'Cabe recurso extraordinário contra acórdão que defere medida liminar, desde que demonstrada a repercussão geral.', 'E',
  'Súmula 735/STF: **não cabe** RE contra acórdão que defere liminar (decisão provisória, sem juízo definitivo). Na mesma linha, a Súmula 7/STJ veda o reexame de prova no REsp.',
  juris=[J['STF735'], J['S7']],
  kw=['recurso extraordinário', 'liminar'])
I(P, 2, 'Repercussão geral presumida',
  'Haverá repercussão geral sempre que o recurso impugnar acórdão que contrarie súmula ou jurisprudência dominante do Supremo Tribunal Federal.', 'C',
  'Art. 1.035, § 3º, I.',
  lei=[('L13105:1035', 'I - contrarie súmula ou jurisprudência dominante do Supremo Tribunal Federal;', None, 'CPC, art. 1.035, § 3º, I')],
  kw=['repercussão geral', 'presunção'])
I(P, 2, 'Rescisória e interpretação controvertida',
  'Não cabe ação rescisória por ofensa a literal disposição de lei quando a decisão rescindenda se tiver baseado em texto legal de interpretação controvertida nos tribunais.', 'C',
  'Súmula 343/STF.',
  juris=[J['STF343']],
  kw=['rescisória', 'Súmula 343'])
I(P, 2, 'Rescisória por prova nova',
  'Fundada a rescisória em prova nova, o termo inicial é a data de sua descoberta, observado o prazo máximo de 10 anos contado do trânsito em julgado.', 'E',
  'Art. 975, § 2º: prazo máximo de **5 anos**.',
  lei=[('L13105:975', 'Se fundada a ação no inciso VII do art. 966', 'última decisão proferida no processo.', 'CPC, art. 975, § 2º')],
  kw=['prova nova', '5 anos'])
I(P, 2, 'Depósito da rescisória',
  'O autor da rescisória deve depositar 5% sobre o valor da causa, exigência que não se aplica à Fazenda Pública, ao Ministério Público, à Defensoria Pública e aos beneficiários da gratuidade.', 'C',
  'Art. 968, II e § 1º; limite de 1.000 salários mínimos (§ 2º).',
  lei=[('L13105:968', 'II - depositar a importância de cinco por cento', 'inadmissível ou improcedente.', 'CPC, art. 968, II'),
       ('L13105:968', 'Não se aplica o disposto no inciso II', 'gratuidade da justiça.', 'CPC, art. 968, § 1º')],
  kw=['rescisória', 'depósito de 5%'])
I(P, 2, 'Feriado local',
  'Se o recorrente não comprovar o feriado local no ato de interposição, o recurso é intempestivo, sem possibilidade de correção.', 'E',
  'Art. 1.003, § 6º (Lei 14.939/2024): o tribunal **determinará a correção do vício formal**, ou o desconsiderará se a informação já constar do processo eletrônico.',
  lei=[('L13105:1003', 'O recorrente comprovará a ocorrência de feriado local no ato de interposição do recurso, e, se não o fizer', 'já conste do processo eletrônico.', 'CPC, art. 1.003, § 6º')],
  kw=['feriado local', 'vício sanável', 'Lei 14.939/2024'])

P = 'DBA26-CPC-10'
# ---------------- PONTO 10 · ACP, ação popular e MS — RODADA 1
I(P, 1, 'ACP — objeto vedado',
  'É cabível ação civil pública para veicular pretensões que envolvam tributos, desde que os contribuintes sejam indeterminados.', 'E',
  'Art. 1º, par. ún., da LACP: **não cabe** ACP sobre tributos, contribuições previdenciárias, FGTS ou fundos institucionais de beneficiários individualizáveis.',
  lei=[('L7347:1', 'Não será cabível ação civil pública para veicular pretensões que envolvam tributos', 'individualmente determinados.', 'Lei 7.347/1985, art. 1º, par. ún.')],
  kw=['ACP', 'tributos', 'FGTS'])
I(P, 1, 'ACP — legitimidade da associação',
  'A associação tem legitimidade para a ação civil pública desde que esteja constituída há pelo menos 2 anos e inclua entre suas finalidades a proteção do bem tutelado.', 'E',
  'Art. 5º, V, "a": **1 ano** de constituição — requisito que o juiz pode dispensar diante de manifesto interesse social (§ 4º). Os demais legitimados: MP, **Defensoria Pública**, entes federativos e administração indireta.',
  lei=[('L7347:5', 'a) esteja constituída há pelo menos 1 (um) ano nos termos da lei civil;', None, 'Lei 7.347/1985, art. 5º, V, "a"'),
       ('L7347:5', 'O requisito da pré-constituição poderá ser dispensado pelo juiz', 'bem jurídico a ser protegido.', 'Lei 7.347/1985, art. 5º, § 4º')],
  kw=['associação', 'pré-constituição', '1 ano'])
I(P, 1, 'ACP — competência',
  'As ações civis públicas serão propostas no foro do local onde ocorrer o dano, cujo juízo terá competência funcional para processar e julgar a causa.', 'C',
  'Art. 2º: competência **funcional** = **absoluta**.',
  lei=[('L7347:2', 'As ações previstas nesta Lei serão propostas no foro do local onde ocorrer o dano', 'processar e julgar a causa.', 'Lei 7.347/1985, art. 2º')],
  kw=['competência funcional', 'local do dano'])
I(P, 1, 'ACP — limite territorial da coisa julgada',
  'Conforme a jurisprudência atual do STF, a sentença da ação civil pública faz coisa julgada erga omnes apenas nos limites da competência territorial do órgão prolator.', 'E',
  'O STF (Tema 1.075) declarou **inconstitucional** a redação do art. 16 dada pela Lei 9.494/1997 — que ainda aparece no texto do Planalto. ACP nacional ou regional segue o art. 93, II, do CDC.',
  lei=[('L7347:16', 'A sentença civil fará coisa julgada erga omnes, nos limites da competência territorial do órgão prolator', None, 'Lei 7.347/1985, art. 16 (redação declarada inconstitucional)')],
  juris=[J['RG1075']],
  peg='O texto do art. 16 continua publicado — a banca cobra a letra da lei contra a tese do STF.',
  kw=['art. 16', 'Tema 1.075', 'erga omnes'])
I(P, 1, 'Ação popular — legitimidade',
  'Qualquer cidadão é parte legítima para propor ação popular, mas a pessoa jurídica não tem essa legitimidade.', 'C',
  'Art. 1º da Lei 4.717/1965 e Súmula 365/STF. A cidadania se prova com o **título eleitoral** (art. 1º, § 3º). E o MS não substitui a ação popular (Súmula 101/STF).',
  lei=[('L4717:1', 'Qualquer cidadão será parte legítima', None, 'Lei 4.717/1965, art. 1º'),
       ('L4717:1', 'A prova da cidadania, para ingresso em juízo, será feita com o título eleitoral', None, 'Lei 4.717/1965, art. 1º, § 3º')],
  juris=[J['STF365'], J['STF101']],
  kw=['cidadão', 'título eleitoral', 'pessoa jurídica'])
I(P, 1, 'Ação popular — prescrição',
  'A ação popular prescreve em 3 anos.', 'E',
  'Art. 21: **5 anos**.',
  lei=[('L4717:21', 'A ação prevista nesta lei prescreve em 5 (cinco) anos.', None, 'Lei 4.717/1965, art. 21')],
  kw=['ação popular', '5 anos'])
I(P, 1, 'Ação popular — papel do MP',
  'Na ação popular, o Ministério Público pode assumir a defesa do ato impugnado quando entender que ele é legal.', 'E',
  'Art. 6º, § 4º: o MP acompanha a ação, é-lhe **vedado, em qualquer hipótese**, assumir a defesa do ato impugnado ou de seus autores.',
  lei=[('L4717:6', 'O Ministério Público acompanhará a ação', 'ou dos seus autores.', 'Lei 4.717/1965, art. 6º, § 4º')],
  kw=['MP', 'ação popular', 'vedação'])
I(P, 1, 'MS — cabimento',
  'Conceder-se-á mandado de segurança para proteger direito líquido e certo, não amparado por habeas corpus ou habeas data, contra ilegalidade ou abuso de poder de autoridade.', 'C',
  'Art. 1º da Lei 12.016/2009: **residualidade** em relação ao HC e ao HD.',
  lei=[('L12016:1', 'Conceder-se-á mandado de segurança para proteger direito líquido e certo', 'sejam quais forem as funções que exerça.', 'Lei 12.016/2009, art. 1º')],
  kw=['direito líquido e certo', 'residualidade'])
I(P, 1, 'MS — prazo decadencial',
  'O direito de requerer mandado de segurança extingue-se decorridos 90 dias contados da ciência, pelo interessado, do ato impugnado.', 'E',
  'Art. 23: **120 dias** — prazo **decadencial**, constitucional segundo a Súmula 632/STF e a ADI 4.296.',
  lei=[('L12016:23', 'O direito de requerer mandado de segurança extinguir-se-á decorridos 120 (cento e vinte) dias', 'do ato impugnado.', 'Lei 12.016/2009, art. 23')],
  kw=['120 dias', 'decadência'])
I(P, 1, 'MS — hipóteses de não cabimento',
  'Não se concederá mandado de segurança contra ato do qual caiba recurso administrativo com efeito suspensivo, independentemente de caução, nem contra decisão judicial transitada em julgado.', 'C',
  'Art. 5º, I e III.',
  lei=[('L12016:5', 'I - de ato do qual caiba recurso administrativo com efeito suspensivo, independentemente de caução;', None, 'Lei 12.016/2009, art. 5º, I'),
       ('L12016:5', 'III - de decisão judicial transitada em julgado.', None, 'Lei 12.016/2009, art. 5º, III')],
  kw=['MS', 'não cabimento'])
I(P, 1, 'MS — honorários',
  'Não cabe, no mandado de segurança, condenação ao pagamento de honorários advocatícios, sem prejuízo das sanções por litigância de má-fé.', 'C',
  'Art. 25 da Lei 12.016/2009; Súmulas 105/STJ e 512/STF.',
  lei=[('L12016:25', 'Não cabem, no processo de mandado de segurança', 'litigância de má-fé.', 'Lei 12.016/2009, art. 25')],
  juris=[J['S105'], J['STF512']],
  kw=['honorários', 'mandado de segurança'])
I(P, 1, 'MS coletivo — legitimados',
  'O mandado de segurança coletivo pode ser impetrado por associação legalmente constituída e em funcionamento há pelo menos 1 ano, exigida autorização especial dos associados.', 'E',
  'Art. 21: o requisito de **1 ano** de funcionamento está certo, mas a autorização especial é **dispensada** (Súmula 629/STF).',
  lei=[('L12016:21', 'ou por organização sindical, entidade de classe ou associação legalmente constituída', 'dispensada, para tanto, autorização especial.', 'Lei 12.016/2009, art. 21')],
  juris=[J['STF629']],
  kw=['MS coletivo', '1 ano', 'autorização'])

# ---------------- PONTO 10 — RODADA 2
I(P, 2, 'ACP — MP fiscal',
  'Na ação civil pública, o Ministério Público, se não intervier no processo como parte, atuará obrigatoriamente como fiscal da lei.', 'C',
  'Art. 5º, § 1º.',
  lei=[('L7347:5', 'O Ministério Público, se não intervier no processo como parte', 'fiscal da lei.', 'Lei 7.347/1985, art. 5º, § 1º')],
  kw=['MP', 'fiscal da lei'])
I(P, 2, 'Compromisso de ajustamento de conduta',
  'O compromisso de ajustamento de conduta tomado pelos órgãos públicos legitimados tem eficácia de título executivo judicial.', 'E',
  'Art. 5º, § 6º: título executivo **extrajudicial**.',
  lei=[('L7347:5', 'Os órgãos públicos legitimados poderão tomar dos interessados compromisso', 'título executivo extrajudicial.', 'Lei 7.347/1985, art. 5º, § 6º')],
  kw=['TAC', 'título extrajudicial'])
I(P, 2, 'Inquérito civil',
  'O inquérito civil pode ser instaurado por qualquer dos legitimados à ação civil pública, inclusive pelas associações.', 'E',
  'Art. 8º, § 1º: o inquérito civil é **exclusivo do MP**, que o preside.',
  lei=[('L7347:8', 'O Ministério Público poderá instaurar, sob sua presidência, inquérito civil', 'inferior a 10 (dez) dias úteis.', 'Lei 7.347/1985, art. 8º, § 1º')],
  kw=['inquérito civil', 'exclusividade do MP'])
I(P, 2, 'Ônus da associação autora',
  'Vencida na ação civil pública, a associação autora será sempre condenada em honorários de advogado, custas e despesas processuais.', 'E',
  'Art. 18: **não há** condenação da associação autora, **salvo comprovada má-fé**.',
  lei=[('L7347:18', 'Nas ações de que trata esta lei, não haverá adiantamento de custas', 'custas e despesas processuais.', 'Lei 7.347/1985, art. 18')],
  kw=['associação', 'má-fé', 'custas'])
I(P, 2, 'Ação popular — ente público réu',
  'A pessoa jurídica de direito público cujo ato seja impugnado na ação popular poderá abster-se de contestar o pedido ou atuar ao lado do autor, se isso se afigurar útil ao interesse público.', 'C',
  'Art. 6º, § 3º: **intervenção móvel** (migração de polo).',
  lei=[('L4717:6', 'cujo ato seja objeto de impugnação, poderá abster-se de contestar o pedido', 'representante legal ou dirigente.', 'Lei 4.717/1965, art. 6º, § 3º')],
  kw=['intervenção móvel', 'ação popular'])
I(P, 2, 'Vedações de liminar em MS',
  'Permanece válida a vedação legal de liminar em mandado de segurança que tenha por objeto a compensação de créditos tributários ou a entrega de mercadorias provenientes do exterior.', 'E',
  'O STF, na **ADI 4.296**, declarou **inconstitucional** o art. 7º, § 2º, da Lei 12.016/2009 (e o art. 22, § 2º). Ficou válida a faculdade de exigir **caução** (art. 7º, III).',
  lei=[('L12016:7', 'Não será concedida medida liminar que tenha por objeto a compensação de créditos tributários', None, 'Lei 12.016/2009, art. 7º, § 2º (declarado inconstitucional)')],
  juris=[J['ADI4296']],
  kw=['liminar', 'ADI 4.296'])
I(P, 2, 'Teoria da encampação',
  'A teoria da encampação aplica-se ao mandado de segurança quando presentes, cumulativamente, vínculo hierárquico entre a autoridade que prestou informações e a que ordenou o ato, manifestação a respeito do mérito nas informações e ausência de modificação de competência constitucional.', 'C',
  'Súmula 628/STJ: requisitos **cumulativos**.',
  juris=[J['S628']],
  kw=['encampação', 'autoridade coatora'])
I(P, 2, 'MS coletivo e ação individual',
  'O mandado de segurança coletivo induz litispendência para as ações individuais.', 'E',
  'Art. 22, § 1º: **não induz litispendência**; mas o impetrante individual só se beneficia se desistir do seu MS em **30 dias** da ciência do coletivo.',
  lei=[('L12016:22', 'O mandado de segurança coletivo não induz litispendência', 'impetração da segurança coletiva.', 'Lei 12.016/2009, art. 22, § 1º')],
  kw=['MS coletivo', 'litispendência', '30 dias'])
I(P, 2, 'Reexame necessário no MS',
  'Concedida a segurança, a sentença estará sujeita obrigatoriamente ao duplo grau de jurisdição.', 'C',
  'Art. 14, § 1º. A autoridade coatora também pode recorrer (§ 2º).',
  lei=[('L12016:14', 'Concedida a segurança, a sentença estará sujeita obrigatoriamente ao duplo grau de jurisdição.', None, 'Lei 12.016/2009, art. 14, § 1º')],
  kw=['duplo grau', 'remessa necessária'])
I(P, 2, 'Entidade de classe e parte da categoria',
  'A entidade de classe tem legitimação para o mandado de segurança ainda quando a pretensão veiculada interesse apenas a uma parte da respectiva categoria.', 'C',
  'Súmula 630/STF, refletida no art. 21 ("da totalidade, ou de parte, dos seus membros").',
  juris=[J['STF630']],
  lei=[('L12016:21', 'em defesa de direitos líquidos e certos da totalidade, ou de parte, dos seus membros ou associados', None, 'Lei 12.016/2009, art. 21')],
  kw=['MS coletivo', 'parte da categoria'])

P = 'DBA26-CPC-11'
# ---------------- PONTO 11 · Juizados Especiais — RODADA 1
I(P, 1, 'Critérios do JEC',
  'O processo nos Juizados Especiais orienta-se pelos critérios da oralidade, simplicidade, informalidade, economia processual e celeridade, buscando, sempre que possível, a conciliação ou a transação.', 'C',
  'Art. 2º da Lei 9.099/1995.',
  lei=[('L9099:2', 'O processo orientar-se-á pelos critérios da oralidade', 'a conciliação ou a transação.', 'Lei 9.099/1995, art. 2º')],
  kw=['oralidade', 'informalidade', 'celeridade'])
I(P, 1, 'Competência pelo valor',
  'O Juizado Especial Cível tem competência para as causas cujo valor não exceda 60 salários mínimos.', 'E',
  'JEC estadual: **40 SM** (art. 3º, I, Lei 9.099). **60 SM** é o teto do **Juizado da Fazenda Pública** (art. 2º, Lei 12.153).',
  lei=[('L9099:3', 'I - as causas cujo valor não exceda a quarenta vezes o salário mínimo;', None, 'Lei 9.099/1995, art. 3º, I')],
  peg='Mistura dos tetos de 40 SM (JEC) e 60 SM (JEFP/JEF).',
  kw=['40 salários mínimos', 'competência'])
I(P, 1, 'Causas excluídas',
  'Ficam excluídas da competência do Juizado Especial Cível as causas de natureza alimentar, falimentar, fiscal e de interesse da Fazenda Pública, e as relativas a acidentes de trabalho, a resíduos e ao estado e capacidade das pessoas.', 'C',
  'Art. 3º, § 2º — **ainda que de cunho patrimonial**.',
  lei=[('L9099:3', 'Ficam excluídas da competência do Juizado Especial', 'ainda que de cunho patrimonial.', 'Lei 9.099/1995, art. 3º, § 2º')],
  kw=['exclusões', 'Fazenda Pública'])
I(P, 1, 'Assistência por advogado',
  'Nas causas de valor até 40 salários mínimos, as partes comparecerão pessoalmente, sendo facultativa a assistência por advogado.', 'E',
  'Art. 9º: assistência facultativa até **20 SM**; acima disso, **obrigatória**. No recurso, advogado sempre (art. 41, § 2º).',
  lei=[('L9099:9', 'Nas causas de valor até vinte salários mínimos', 'a assistência é obrigatória.', 'Lei 9.099/1995, art. 9º')],
  kw=['advogado', '20 salários mínimos'])
I(P, 1, 'Intervenção de terceiros',
  'No processo do Juizado Especial Cível não se admite qualquer forma de intervenção de terceiro nem de assistência, mas admite-se o litisconsórcio.', 'C',
  'Art. 10 da Lei 9.099. O CPC abriu uma exceção: o **incidente de desconsideração da personalidade jurídica** (art. 1.062).',
  exc=['IDPJ é aplicável aos Juizados (CPC, art. 1.062)'],
  lei=[('L9099:10', 'Não se admitirá, no processo, qualquer forma de intervenção de terceiro nem de assistência. Admitir-se-á o litisconsórcio.', None, 'Lei 9.099/1995, art. 10'),
       ('L13105:1062', 'O incidente de desconsideração da personalidade jurídica aplica-se ao processo de competência dos juizados especiais.', None, 'CPC, art. 1.062')],
  kw=['intervenção de terceiros', 'litisconsórcio', 'IDPJ'])
I(P, 1, 'Recurso inominado',
  'O recurso contra a sentença do Juizado Especial Cível será interposto no prazo de 15 dias, contados da ciência da sentença.', 'E',
  'Art. 42: **10 dias**; preparo em **48 horas** (§ 1º).',
  lei=[('L9099:42', 'O recurso será interposto no prazo de dez dias', 'pedido do recorrente.', 'Lei 9.099/1995, art. 42')],
  kw=['recurso inominado', '10 dias'])
I(P, 1, 'Ausência do autor',
  'Extingue-se o processo no Juizado Especial Cível quando o autor deixar de comparecer a qualquer das audiências do processo.', 'C',
  'Art. 51, I — independentemente de intimação pessoal prévia (§ 1º).',
  lei=[('L9099:51', 'I - quando o autor deixar de comparecer a qualquer das audiências do processo;', None, 'Lei 9.099/1995, art. 51, I')],
  kw=['extinção', 'ausência do autor'])
I(P, 1, 'Sucumbência em primeiro grau',
  'A sentença de primeiro grau do Juizado Especial Cível não condenará o vencido em custas e honorários de advogado, ressalvados os casos de litigância de má-fé.', 'C',
  'Art. 55. Em segundo grau, o **recorrente vencido** paga custas e honorários de 10% a 20%.',
  lei=[('L9099:55', 'A sentença de primeiro grau não condenará o vencido', 'litigância de má-fé.', 'Lei 9.099/1995, art. 55')],
  kw=['custas', 'honorários', 'má-fé'])
I(P, 1, 'Recurso especial nos Juizados',
  'Cabe recurso especial contra decisão proferida por turma recursal dos Juizados Especiais.', 'E',
  'Súmula 203/STJ: **não cabe REsp** — turma recursal não é "tribunal" (CF, art. 105, III).',
  juris=[J['S203']],
  kw=['recurso especial', 'turma recursal'])
I(P, 1, 'JEFP — competência',
  'É de competência dos Juizados Especiais da Fazenda Pública processar, conciliar e julgar causas cíveis de interesse dos Estados, do DF, dos Territórios e dos Municípios até o valor de 60 salários mínimos, competência que é absoluta no foro onde estiver instalado.', 'C',
  'Art. 2º, caput e § 4º, da Lei 12.153/2009.',
  lei=[('L12153:2', 'É de competência dos Juizados Especiais da Fazenda Pública', '60 (sessenta) salários mínimos.', 'Lei 12.153/2009, art. 2º'),
       ('L12153:2', 'No foro onde estiver instalado Juizado Especial da Fazenda Pública, a sua competência é absoluta.', None, 'Lei 12.153/2009, art. 2º, § 4º')],
  kw=['JEFP', '60 salários mínimos', 'competência absoluta'])
I(P, 1, 'JEFP — partes',
  'Podem ser réus no Juizado Especial da Fazenda Pública os Estados, o DF, os Territórios e os Municípios, bem como autarquias, fundações, empresas públicas e sociedades de economia mista a eles vinculadas.', 'E',
  'Art. 5º, II: **autarquias, fundações e empresas públicas** — a lei **não** inclui as sociedades de economia mista.',
  lei=[('L12153:5', 'II – como réus, os Estados', 'empresas públicas a eles vinculadas.', 'Lei 12.153/2009, art. 5º, II')],
  kw=['JEFP', 'réus', 'sociedade de economia mista'])
I(P, 1, 'JEFP — prazos',
  'No Juizado Especial da Fazenda Pública, as pessoas jurídicas de direito público têm prazo em dobro para recorrer.', 'E',
  'Art. 7º: **não há prazo diferenciado** para qualquer ato, **inclusive recursos**; citação para a audiência com antecedência mínima de 30 dias.',
  lei=[('L12153:7', 'Não haverá prazo diferenciado para a prática de qualquer ato processual', 'antecedência mínima de 30 (trinta) dias.', 'Lei 12.153/2009, art. 7º')],
  kw=['prazo simples', 'Fazenda Pública'])

# ---------------- PONTO 11 — RODADA 2
I(P, 2, 'Renúncia ao excedente',
  'A opção pelo procedimento do Juizado Especial Cível importa renúncia ao crédito excedente ao limite legal, excetuada a hipótese de conciliação.', 'C',
  'Art. 3º, § 3º.',
  lei=[('L9099:3', 'A opção pelo procedimento previsto nesta Lei importará em renúncia', 'excetuada a hipótese de conciliação.', 'Lei 9.099/1995, art. 3º, § 3º')],
  kw=['renúncia', 'excedente'])
I(P, 2, 'Foro nas ações de reparação',
  'Nas ações para reparação de dano de qualquer natureza, é competente o Juizado do foro do domicílio do autor ou do local do ato ou fato.', 'C',
  'Art. 4º, III; em qualquer hipótese, pode-se propor no domicílio do réu (par. ún.).',
  lei=[('L9099:4', 'III - do domicílio do autor ou do local do ato ou fato', 'de qualquer natureza.', 'Lei 9.099/1995, art. 4º, III')],
  kw=['competência territorial', 'reparação de dano'])
I(P, 2, 'Citação por edital',
  'No Juizado Especial Cível admite-se a citação por edital quando o réu estiver em local incerto.', 'E',
  'Art. 18, § 2º: **não se fará citação por edital**. Réu não encontrado → extinção/remessa à Justiça comum.',
  lei=[('L9099:18', 'Não se fará citação por edital.', None, 'Lei 9.099/1995, art. 18, § 2º')],
  kw=['citação por edital', 'vedação'])
I(P, 2, 'Embargos de declaração no JEC',
  'Nos Juizados Especiais, os embargos de declaração interrompem o prazo para a interposição de recurso.', 'C',
  'Art. 50 da Lei 9.099, com a redação do CPC/2015 (antes, suspendiam contra sentença).',
  lei=[('L9099:50', 'Os embargos de declaração interrompem o prazo para a interposição de recurso.', None, 'Lei 9.099/1995, art. 50')],
  kw=['embargos de declaração', 'interrupção'])
I(P, 2, 'MS contra ato de juizado',
  'Compete à turma recursal processar e julgar o mandado de segurança contra ato de juizado especial.', 'C',
  'Súmula 376/STJ.',
  juris=[J['S376']],
  kw=['mandado de segurança', 'turma recursal'])
I(P, 2, 'RE nos Juizados',
  'Não cabe recurso extraordinário contra decisão proferida por turma recursal de juizado especial cível.', 'E',
  'Súmula 640/STF: **cabe RE** (o art. 102, III, da CF fala em "causas decididas em única ou última instância", sem exigir tribunal). Contraste com a Súmula 203/STJ (não cabe REsp).',
  juris=[J['STF640']],
  peg='Inverter as regras de RE (cabe) e REsp (não cabe).',
  kw=['recurso extraordinário', 'turma recursal'])
I(P, 2, 'JEFP — tutela provisória',
  'No Juizado Especial da Fazenda Pública, o juiz poderá, de ofício ou a requerimento das partes, deferir quaisquer providências cautelares e antecipatórias no curso do processo para evitar dano de difícil ou de incerta reparação.', 'C',
  'Art. 3º da Lei 12.153/2009.',
  lei=[('L12153:3', 'O juiz poderá, de ofício ou a requerimento das partes', 'difícil ou de incerta reparação.', 'Lei 12.153/2009, art. 3º')],
  kw=['JEFP', 'de ofício', 'cautelar'])
I(P, 2, 'JEFP — reexame necessário',
  'As sentenças condenatórias proferidas no Juizado Especial da Fazenda Pública estão sujeitas a reexame necessário.', 'E',
  'Art. 11: **não haverá reexame necessário**.',
  lei=[('L12153:11', 'Nas causas de que trata esta Lei, não haverá reexame necessário.', None, 'Lei 12.153/2009, art. 11')],
  kw=['reexame necessário'])
I(P, 2, 'JEFP — causas excluídas',
  'Incluem-se na competência do Juizado Especial da Fazenda Pública os mandados de segurança de valor até 60 salários mínimos.', 'E',
  'Art. 2º, § 1º, I: excluídos **MS, desapropriação, divisão e demarcação, ações populares, improbidade, execução fiscal** e demandas sobre direitos difusos e coletivos.',
  exc=['MS, desapropriação, divisão/demarcação, populares, improbidade, execuções fiscais, difusos e coletivos (§ 1º, I)', 'Bens imóveis dos entes (§ 1º, II)', 'Impugnação de demissão de servidor ou sanção disciplinar a militar (§ 1º, III)'],
  lei=[('L12153:2', 'I – as ações de mandado de segurança', 'interesses difusos e coletivos;', 'Lei 12.153/2009, art. 2º, § 1º, I')],
  kw=['exclusões', 'mandado de segurança'])
I(P, 2, 'JEFP — conciliação pelo ente',
  'Os representantes judiciais dos réus presentes à audiência poderão conciliar, transigir ou desistir nos processos dos Juizados Especiais da Fazenda Pública, nos termos e hipóteses previstos na lei do respectivo ente.', 'C',
  'Art. 8º.',
  lei=[('L12153:8', 'Os representantes judiciais dos réus presentes à audiência', 'respectivo ente da Federação.', 'Lei 12.153/2009, art. 8º')],
  kw=['conciliação', 'Fazenda Pública'])

P = 'DBA26-CPC-12'
# ---------------- PONTO 12 · Jurisprudência aplicada — RODADA 1
I(P, 1, 'Incompetência relativa',
  'Segundo o STJ, a incompetência relativa pode ser declarada de ofício pelo juiz.', 'E',
  'Súmula 33/STJ: **não pode** ser declarada de ofício (CPC, art. 337, § 5º). Exceção: cláusula de eleição abusiva, **antes da citação** (art. 63, § 3º).',
  exc=['Cláusula de eleição de foro abusiva, antes da citação (CPC, art. 63, § 3º)'],
  juris=[J['S33']],
  kw=['incompetência relativa', 'Súmula 33'])
I(P, 1, 'Interesse da União',
  'Compete à Justiça Federal decidir sobre a existência de interesse jurídico que justifique a presença, no processo, da União, de suas autarquias ou empresas públicas.', 'C',
  'Súmula 150/STJ.',
  juris=[J['S150']],
  kw=['Justiça Federal', 'Súmula 150'])
I(P, 1, 'Investigação de paternidade com alimentos',
  'Na ação de investigação de paternidade cumulada com alimentos, é competente o foro do domicílio ou da residência do alimentando.', 'C',
  'Súmula 1/STJ, em linha com o art. 53, II, do CPC.',
  juris=[J['S1']],
  kw=['alimentando', 'Súmula 1'])
I(P, 1, 'MP e patrimônio público',
  'O Ministério Público não tem legitimidade para propor ação civil pública em defesa do patrimônio público, que cabe exclusivamente ao ente lesado.', 'E',
  'Súmula 329/STJ: o MP **tem legitimidade** (também CF, art. 129, III).',
  juris=[J['S329']],
  kw=['MP', 'patrimônio público', 'Súmula 329'])
I(P, 1, 'MP e consumidor de serviço público',
  'O Ministério Público tem legitimidade ativa para atuar na defesa de direitos difusos, coletivos e individuais homogêneos dos consumidores, ainda que decorrentes da prestação de serviço público.', 'C',
  'Súmula 601/STJ.',
  juris=[J['S601']],
  kw=['MP', 'individuais homogêneos', 'Súmula 601'])
I(P, 1, 'Continência entre ACPs',
  'Reconhecida a continência entre ação civil pública proposta na Justiça Federal e outra na Justiça estadual, ambas devem ser reunidas na Justiça estadual, por ser a de competência residual.', 'E',
  'Súmula 489/STJ: reúnem-se na **Justiça Federal**.',
  juris=[J['S489']],
  kw=['continência', 'Súmula 489'])
I(P, 1, 'MS contra lei em tese',
  'Cabe mandado de segurança contra lei em tese, desde que demonstrado o justo receio de sua aplicação.', 'E',
  'Súmula 266/STF: **não cabe** MS contra lei em tese (cabe contra o ato concreto que a aplica, ou contra lei de efeitos concretos).',
  juris=[J['STF266']],
  kw=['lei em tese', 'Súmula 266'])
I(P, 1, 'MS contra ato judicial',
  'Não cabe mandado de segurança contra ato judicial passível de recurso ou correição.', 'C',
  'Súmula 267/STF, hoje refletida no art. 5º, II, da Lei 12.016 (recurso com efeito suspensivo).',
  juris=[J['STF267']],
  kw=['ato judicial', 'Súmula 267'])
I(P, 1, 'MS e cobrança',
  'O mandado de segurança pode substituir a ação de cobrança quando o direito a valores pretéritos for líquido e certo.', 'E',
  'Súmula 269/STF: o MS **não é substitutivo de ação de cobrança**.',
  juris=[J['STF269']],
  kw=['ação de cobrança', 'Súmula 269'])
I(P, 1, 'Prazo decadencial do MS',
  'É constitucional lei que fixa o prazo de decadência para a impetração de mandado de segurança.', 'C',
  'Súmula 632/STF; o prazo de 120 dias do art. 23 foi mantido na ADI 4.296.',
  juris=[J['STF632']],
  kw=['decadência', 'Súmula 632'])

# ---------------- PONTO 12 — RODADA 2
I(P, 2, 'Efeitos patrimoniais do MS',
  'A concessão de mandado de segurança não produz efeitos patrimoniais em relação a período pretérito, que devem ser reclamados administrativamente ou pela via judicial própria.', 'C',
  'Súmula 271/STF; no mesmo sentido, o art. 14, § 4º, da Lei 12.016 (servidor: só parcelas vencidas a partir do ajuizamento).',
  juris=[J['STF271']],
  lei=[('L12016:14', 'somente será efetuado relativamente às prestações que se vencerem a contar da data do ajuizamento da inicial.', None, 'Lei 12.016/2009, art. 14, § 4º')],
  kw=['efeitos patrimoniais', 'Súmula 271'])
I(P, 2, 'Controvérsia jurídica no MS',
  'A existência de controvérsia sobre matéria de direito impede a concessão de mandado de segurança, por afastar a liquidez e certeza do direito.', 'E',
  'Súmula 625/STF: **não impede**. "Líquido e certo" refere-se aos **fatos** provados de plano, não à tese jurídica.',
  juris=[J['STF625']],
  kw=['direito líquido e certo', 'Súmula 625'])
I(P, 2, 'MS em licitação de estatal',
  'Não cabe mandado de segurança contra ato praticado em licitação promovida por sociedade de economia mista, por se tratar de pessoa jurídica de direito privado.', 'E',
  'Súmula 333/STJ: **cabe** MS (o ato de licitação é de autoridade). Não cabe, sim, contra **atos de gestão comercial** (Lei 12.016, art. 1º, § 2º).',
  juris=[J['S333']],
  lei=[('L12016:1', 'Não cabe mandado de segurança contra os atos de gestão comercial', 'concessionárias de serviço público.', 'Lei 12.016/2009, art. 1º, § 2º')],
  kw=['licitação', 'estatais', 'Súmula 333'])
I(P, 2, 'MS e compensação tributária',
  'O mandado de segurança constitui ação adequada para a declaração do direito à compensação tributária.', 'C',
  'Súmula 213/STJ. Atenção ao contraponto: **não cabe** MS para convalidar compensação **já realizada** pelo contribuinte (Súmula 460/STJ).',
  juris=[J['S213']],
  kw=['compensação tributária', 'Súmula 213'])
I(P, 2, 'Convalidação de compensação',
  'É cabível mandado de segurança para convalidar a compensação tributária já realizada pelo contribuinte.', 'E',
  'Súmula 460/STJ: **incabível**. O MS serve para **declarar o direito** à compensação (Súmula 213), não para chancelar a que já foi feita.',
  juris=[J['S460']],
  kw=['compensação', 'Súmula 460'])
I(P, 2, 'MS contra decisão transitada',
  'Admite-se mandado de segurança contra decisão judicial transitada em julgado quando houver ilegalidade manifesta.', 'E',
  'Súmula 268/STF e art. 5º, III, da Lei 12.016: **não cabe**. O caminho é a **ação rescisória**.',
  juris=[J['STF268']],
  kw=['coisa julgada', 'Súmula 268'])
I(P, 2, 'Vara privativa',
  'A existência de vara privativa, instituída por lei estadual, não altera a competência territorial resultante das leis de processo.', 'C',
  'Súmula 206/STJ.',
  juris=[J['S206']],
  kw=['vara privativa', 'competência territorial'])
I(P, 2, 'MS coletivo sem autorização',
  'Segundo o STF, a impetração de mandado de segurança coletivo por entidade de classe em favor dos associados depende de autorização expressa destes.', 'E',
  'Súmula 629/STF: **independe** de autorização (substituição processual — CF, art. 5º, LXX). Diferente da ação coletiva ordinária de associação (CF, art. 5º, XXI).',
  juris=[J['STF629']],
  kw=['MS coletivo', 'substituição processual'])
