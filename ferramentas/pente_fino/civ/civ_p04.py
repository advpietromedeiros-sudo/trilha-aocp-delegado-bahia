from base import I
from civ_juris import J

CC = 'L10406:'
P = 'DBA26-CIV-4'
# ---------------- PONTO 4 · Do direito das obrigações — RODADA 1
I(P, 1, 'Acessórios na obrigação de dar coisa certa',
  'A obrigação de dar coisa certa abrange os acessórios dela embora não mencionados, salvo se o contrário resultar do título ou das circunstâncias do caso.', 'C',
  'Art. 233: **o acessório segue o principal** também nas obrigações de dar.',
  lei=[(CC + '233', 'A obrigação de dar coisa certa abrange', 'circunstâncias do caso.', 'CC, art. 233')],
  kw=['dar coisa certa', 'acessórios'])
I(P, 1, 'Perda da coisa certa sem culpa',
  'Se, na obrigação de dar coisa certa, a coisa se perder sem culpa do devedor antes da tradição, o devedor responde pelo equivalente, mas não por perdas e danos.', 'E',
  'Art. 234: **sem culpa**, a obrigação **fica resolvida para ambas as partes**. Equivalente **mais perdas e danos** só se houver **culpa** do devedor.',
  lei=[(CC + '234', 'Se, no caso do artigo antecedente, a coisa se perder', 'mais perdas e danos.', 'CC, art. 234')],
  kw=['perda da coisa', 'sem culpa', 'resolvida'])
I(P, 1, 'Solidariedade não se presume',
  'Presume-se a solidariedade quando, na mesma obrigação, concorrer mais de um devedor.', 'E',
  'Art. 265: **a solidariedade não se presume**; resulta da **lei** ou da **vontade das partes**.',
  lei=[(CC + '265', 'A solidariedade não se presume', 'vontade das partes.', 'CC, art. 265')],
  exc=['Nas relações de consumo, todos os responsáveis pela ofensa respondem solidariamente (CDC, art. 7º, par. ún.)'],
  kw=['solidariedade', 'não se presume'])
I(P, 1, 'Solidariedade passiva',
  'O credor tem direito a exigir e receber de um ou de alguns dos devedores, parcial ou totalmente, a dívida comum.', 'C',
  'Art. 275: na **solidariedade passiva** o credor escolhe de quem cobrar e quanto cobrar; se o pagamento for parcial, os demais continuam obrigados pelo resto.',
  lei=[(CC + '275', 'O credor tem direito a exigir e receber', 'a dívida comum', 'CC, art. 275')],
  kw=['solidariedade passiva', 'dívida comum'])
I(P, 1, 'Pagamento por terceiro não interessado',
  'O terceiro não interessado que paga a dívida em seu próprio nome sub-roga-se nos direitos do credor.', 'E',
  'Art. 305: tem **direito a reembolsar-se** do que pagar, mas **não se sub-roga** nos direitos do credor. Quem se sub-roga de pleno direito é o **terceiro interessado** (art. 346, III).',
  lei=[(CC + '305', 'O terceiro não interessado, que paga a dívida em seu próprio nome', 'não se sub-roga nos direitos do credor.', 'CC, art. 305')],
  kw=['terceiro não interessado', 'reembolsar', 'sub-roga'])
I(P, 1, 'Lugar do pagamento',
  'Efetuar-se-á o pagamento no domicílio do devedor, salvo se as partes convencionarem diversamente, ou se o contrário resultar da lei, da natureza da obrigação ou das circunstâncias.', 'C',
  'Art. 327: a regra é a dívida **quesível** (paga no **domicílio do devedor**); a portável depende de convenção, lei ou natureza da obrigação.',
  lei=[(CC + '327', 'Efetuar-se-á o pagamento no domicílio do devedor', 'das circunstâncias.', 'CC, art. 327')],
  kw=['domicílio do devedor', 'quesível'])
I(P, 1, 'Mora ex re',
  'O inadimplemento da obrigação, positiva e líquida, no seu termo, constitui de pleno direito em mora o devedor.', 'C',
  'Art. 397: **mora automática** (*dies interpellat pro homine*). Sem termo, a mora depende de **interpelação** judicial ou extrajudicial (parágrafo único).',
  lei=[(CC + '397', 'O inadimplemento da obrigação, positiva e líquida', 'em mora o devedor.', 'CC, art. 397')],
  kw=['mora', 'de pleno direito'])
I(P, 1, 'Mora no ato ilícito',
  'Nas obrigações provenientes de ato ilícito, considera-se o devedor em mora a partir da citação válida na ação indenizatória.', 'E',
  'Art. 398: o devedor está em mora **desde que praticou o ato ilícito**. Daí a **Súmula 54/STJ**: juros moratórios desde o evento danoso, na responsabilidade extracontratual.',
  lei=[(CC + '398', 'Nas obrigações provenientes de ato ilícito', 'desde que o praticou.', 'CC, art. 398')],
  juris=[J['S54']],
  peg='A AOCP já cobrou o art. 398; a troca típica é "desde a citação".',
  kw=['ato ilícito', 'desde que o praticou'])
I(P, 1, 'Limite da cláusula penal',
  'O valor da cominação imposta na cláusula penal não pode exceder o da obrigação principal.', 'C',
  'Art. 412: a **cláusula penal** tem como teto o valor da obrigação principal.',
  lei=[(CC + '412', 'O valor da cominação imposta na cláusula penal', 'obrigação principal.', 'CC, art. 412')],
  kw=['cláusula penal', 'não pode exceder'])
I(P, 1, 'Redução da cláusula penal',
  'É vedado ao juiz reduzir a penalidade quando a obrigação principal tiver sido cumprida em parte, pois a cláusula penal é pré-fixação das perdas e danos.', 'E',
  'Art. 413: a penalidade **deve ser reduzida equitativamente** pelo juiz se a obrigação foi **cumprida em parte** ou se o montante for **manifestamente excessivo**.',
  lei=[(CC + '413', 'A penalidade deve ser reduzida eqüitativamente pelo juiz', 'finalidade do negócio.', 'CC, art. 413')],
  kw=['reduzida equitativamente', 'cumprida em parte'])
I(P, 1, 'Função social e intervenção mínima',
  'A liberdade contratual será exercida nos limites da função social do contrato, e nas relações contratuais privadas prevalecerão o princípio da intervenção mínima e a excepcionalidade da revisão contratual.', 'C',
  'Art. 421 e parágrafo único (Lei da Liberdade Econômica, 2019): **função social** como limite e **intervenção mínima** como regra.',
  lei=[(CC + '421', 'A liberdade contratual será exercida nos limites da função social do contrato.', None, 'CC, art. 421'),
       (CC + '421', 'Nas relações contratuais privadas, prevalecerão o princípio da intervenção mínima', 'revisão contratual.', 'CC, art. 421, par. ún.')],
  kw=['função social', 'intervenção mínima'])
I(P, 1, 'Contrato de adesão',
  'Quando houver no contrato de adesão cláusulas ambíguas ou contraditórias, dever-se-á adotar a interpretação mais favorável ao estipulante, que redigiu o instrumento.', 'E',
  'Art. 423: a interpretação favorece o **aderente**. E são nulas as cláusulas que estipulem a renúncia antecipada do aderente a direito resultante da natureza do negócio (art. 424).',
  lei=[(CC + '423', 'Quando houver no contrato de adesão', 'mais favorável ao aderente.', 'CC, art. 423')],
  kw=['adesão', 'aderente'])
# Títulos de crédito (CC, arts. 887 a 926 — Parte Especial, Livro I): acréscimo de 07/11/2026.
I(P, 1, 'Títulos de crédito — conceito',
  'Segundo o Código Civil, sem a apresentação da cártula não se exerce o direito nela mencionado, que é literal e autônomo; e o título só tem eficácia se atender aos requisitos fixados em lei.', 'C',
  'Art. 887: o conceito traz os três atributos clássicos — **cartularidade** (documento necessário), **literalidade** e **autonomia**. Leis especiais (cheque, duplicata, letra de câmbio) prevalecem; o CC é supletivo (art. 903).',
  lei=[(CC + '887', 'O título de crédito, documento necessário', 'requisitos da lei.', 'CC, art. 887'),
       (CC + '903', 'Salvo disposição diversa em lei especial', 'neste Código.', 'CC, art. 903')],
  kw=['cartularidade', 'literalidade', 'autonomia'])
I(P, 1, 'Títulos de crédito — aval parcial',
  'No regime do Código Civil, o pagamento de título que contenha obrigação de pagar soma determinada pode ser garantido por aval, admitindo-se o aval parcial.', 'E',
  'Art. 897, parágrafo único: o CC **veda o aval parcial**. Atenção: a Lei Uniforme de Genebra (letra de câmbio e nota promissória) e a Lei do Cheque o admitem — e a lei especial prevalece (art. 903).',
  lei=[(CC + '897', 'O pagamento de título de crédito, que contenha obrigação de pagar soma determinada', 'É vedado o aval parcial.', 'CC, art. 897 e par. ún.')],
  peg='Trocar "vedado" por "admitido", ou cobrar a regra do CC num título regido por lei especial.',
  kw=['aval parcial', 'vedado'])
I(P, 1, 'Títulos de crédito — vencimento e lugar',
  'O título de crédito que não indique o vencimento é considerado à vista e, se omitir o lugar de emissão e de pagamento, considera-se como tal o domicílio do emitente.', 'C',
  'Art. 889, §§ 1º e 2º: requisitos mínimos são **data de emissão**, **direitos conferidos** e **assinatura do emitente**; a falta de vencimento faz o título **à vista**; a falta de lugar remete ao **domicílio do emitente**.',
  lei=[(CC + '889', 'Deve o título de crédito conter a data da emissão', 'assinatura do emitente.', 'CC, art. 889'),
       (CC + '889', 'É à vista o título de crédito que não contenha indicação de vencimento.', 'o domicílio do emitente.', 'CC, art. 889, §§ 1º e 2º')],
  kw=['à vista', 'domicílio do emitente'])
I(P, 1, 'Títulos de crédito — cláusulas não escritas',
  'É válida e eficaz a cláusula de juros inserida no título de crédito, desde que pactuada no momento da emissão.', 'E',
  'Art. 890: consideram-se **não escritas** a cláusula de **juros**, a **proibitiva de endosso**, a **excludente de responsabilidade** pelo pagamento ou despesas e a que dispense termos e formalidades. O título continua válido; só a cláusula é desconsiderada.',
  lei=[(CC + '890', 'Consideram-se não escritas no título a cláusula de juros', 'restrinja direitos e obrigações.', 'CC, art. 890')],
  kw=['cláusula de juros', 'não escritas'])
I(P, 1, 'Títulos de crédito — responsabilidade do endossante',
  'Pelo Código Civil, o endossante responde, em regra, pelo cumprimento da prestação constante do título, salvo cláusula expressa que o exonere.', 'E',
  'Art. 914: a regra do CC é a **inversa** — o endossante **não responde**, salvo cláusula expressa em contrário; se assumir a responsabilidade, torna-se **devedor solidário** (§ 1º). Na letra de câmbio (lei especial), o endossante garante o pagamento.',
  lei=[(CC + '914', 'Ressalvada cláusula expressa em contrário', 'prestação constante do título.', 'CC, art. 914'),
       (CC + '914', 'Assumindo responsabilidade pelo pagamento', 'devedor solidário.', 'CC, art. 914, § 1º')],
  peg='A troca típica é inverter a regra geral do endosso no CC.',
  kw=['endossante', 'não responde', 'devedor solidário'])

# ---------------- PONTO 4 — RODADA 2
I(P, 2, 'Arras confirmatórias',
  'Se a inexecução do contrato for de quem recebeu as arras, poderá quem as deu haver o contrato por desfeito e exigir apenas a sua devolução simples.', 'E',
  'Art. 418: quem deu as arras pode exigir sua **devolução mais o equivalente**, com atualização monetária, juros e honorários. Se quem deu as arras é que não cumpriu, a outra parte as **retém**.',
  lei=[(CC + '418', 'Na hipótese de inexecução do contrato', 'honorários de advogado.', 'CC, art. 418')],
  kw=['arras', 'mais o equivalente'])
I(P, 2, 'Evicção em hasta pública',
  'Nos contratos onerosos, o alienante responde pela evicção, garantia que subsiste ainda que a aquisição se tenha realizado em hasta pública.', 'C',
  'Art. 447: a **evicção** subsiste **ainda que a aquisição se tenha realizado em hasta pública**. As partes podem reforçar, diminuir ou excluir a garantia por cláusula expressa (art. 448).',
  lei=[(CC + '447', 'Nos contratos onerosos, o alienante responde pela evicção', 'hasta pública.', 'CC, art. 447')],
  kw=['evicção', 'hasta pública'])
I(P, 2, 'Prazos dos vícios redibitórios',
  'O adquirente decai do direito de obter a redibição ou abatimento no preço no prazo de trinta dias se a coisa for móvel, e de um ano se for imóvel, contado da entrega efetiva.', 'C',
  'Art. 445: **30 dias (móvel)** e **1 ano (imóvel)** da **entrega efetiva**; se já estava na posse, o prazo conta da alienação, reduzido à metade.',
  lei=[(CC + '445', 'O adquirente decai do direito de obter a redibição', 'reduzido à metade.', 'CC, art. 445')],
  exc=['Vício que, por sua natureza, só puder ser conhecido mais tarde: o prazo conta do momento em que dele tiver ciência, até 180 dias (móveis) ou 1 ano (imóveis) — art. 445, § 1º'],
  kw=['vícios redibitórios', 'entrega efetiva'])
I(P, 2, 'Onerosidade excessiva',
  'Nos contratos de execução continuada ou diferida, se a prestação de uma das partes se tornar excessivamente onerosa, com extrema vantagem para a outra, em virtude de acontecimentos extraordinários e imprevisíveis, o devedor poderá pedir a resolução do contrato, cujos efeitos retroagirão à data da celebração.', 'E',
  'Art. 478: os efeitos da sentença que decretar a resolução **retroagirão à data da citação**. O réu pode evitar a resolução oferecendo-se a modificar equitativamente as condições (art. 479).',
  lei=[(CC + '478', 'Nos contratos de execução continuada ou diferida', 'retroagirão à data da citação.', 'CC, art. 478')],
  kw=['onerosidade excessiva', 'data da citação'])
I(P, 2, 'Juros de mora antes da Lei 14.905/2024',
  'Segundo o STJ, antes da Lei 14.905/2024, a taxa legal de juros de mora das dívidas civis referida no art. 406 do Código Civil era de 1% ao mês, nos termos do Código Tributário Nacional.', 'E',
  'No **Tema 1.368**, a Corte Especial do STJ fixou que a taxa era a **SELIC**. Hoje o art. 406 diz expressamente: SELIC **deduzido o índice de atualização monetária** do art. 389 (IPCA).',
  lei=[(CC + '406', 'Quando não forem convencionados', 'taxa legal.', 'CC, art. 406'),
       (CC + '406', 'A taxa legal corresponderá à taxa referencial do Sistema Especial de Liquidação e de Custódia (Selic)', 'parágrafo único do art. 389 deste Código.', 'CC, art. 406, § 1º')],
  juris=[J['T1368']],
  kw=['SELIC', 'juros de mora'])
I(P, 2, 'Ânimo de novar',
  'Não havendo ânimo de novar, expresso ou tácito mas inequívoco, a segunda obrigação confirma simplesmente a primeira.', 'C',
  'Art. 361: sem **animus novandi**, não há novação — a nova obrigação apenas **confirma** a anterior.',
  lei=[(CC + '361', 'Não havendo ânimo de novar', 'confirma simplesmente a primeira.', 'CC, art. 361')],
  kw=['novação', 'ânimo de novar'])
I(P, 2, 'Requisitos da compensação',
  'A compensação efetua-se entre dívidas líquidas, vencidas e de coisas fungíveis.', 'C',
  'Art. 369: **liquidez**, **vencimento** e **fungibilidade**.',
  lei=[(CC + '369', 'A compensação efetua-se entre dívidas líquidas', 'coisas fungíveis.', 'CC, art. 369')],
  kw=['compensação', 'líquidas, vencidas'])
I(P, 2, 'Fiança sem outorga conjugal',
  'A fiança prestada sem autorização de um dos cônjuges implica a ineficácia total da garantia.', 'C',
  '**Súmula 332/STJ**: **ineficácia total** — não se salva sequer a meação do cônjuge que assinou.',
  juris=[J['S332']],
  kw=['fiança', 'ineficácia total'])
I(P, 2, 'Doação verbal',
  'A doação verbal é sempre nula, pois a doação far-se-á obrigatoriamente por escritura pública ou instrumento particular.', 'E',
  'Art. 541, parágrafo único: a doação verbal é **válida** se versar sobre **bens móveis e de pequeno valor** e se lhe seguir **incontinenti a tradição**.',
  lei=[(CC + '541', 'A doação far-se-á por escritura pública ou instrumento particular.', None, 'CC, art. 541'),
       (CC + '541', 'A doação verbal será válida', 'incontinenti a tradição.', 'CC, art. 541, par. ún.')],
  kw=['doação verbal', 'pequeno valor'])
# Títulos de crédito — Rodada 2 (acréscimo de 07/11/2026).
I(P, 2, 'Títulos de crédito — aval após o vencimento',
  'O aval lançado depois do vencimento do título não tem natureza cambial e produz apenas os efeitos de uma fiança.', 'E',
  'Art. 900: o aval **posterior ao vencimento** produz **os mesmos efeitos** do anterior. Lembre ainda: o avalista se equipara ao avalizado e, pagando, tem regresso contra ele e os coobrigados anteriores (art. 899).',
  lei=[(CC + '900', 'O aval posterior ao vencimento produz os mesmos efeitos do anteriormente dado.', None, 'CC, art. 900'),
       (CC + '899', 'O avalista equipara-se àquele cujo nome indicar', 'ao emitente ou devedor final.', 'CC, art. 899')],
  exc=['Casado, salvo no regime da separação absoluta, precisa da autorização do cônjuge para prestar aval (CC, art. 1.647, III).'],
  kw=['aval posterior', 'mesmos efeitos'])
I(P, 2, 'Títulos de crédito — vício do título e negócio de origem',
  'A omissão de requisito legal que retire do escrito a validade como título de crédito não implica a invalidade do negócio jurídico subjacente.', 'C',
  'Art. 888: cai a **eficácia cambial**, mas o **negócio de origem** permanece e pode ser provado e cobrado pelas vias comuns.',
  lei=[(CC + '888', 'A omissão de qualquer requisito legal', 'negócio jurídico que lhe deu origem.', 'CC, art. 888')],
  kw=['requisito legal', 'negócio jurídico subjacente'])
I(P, 2, 'Títulos de crédito — inoponibilidade das exceções',
  'As exceções fundadas na relação do devedor com portadores anteriores só podem ser opostas ao atual portador se este, ao adquirir o título, tiver agido de má-fé.', 'C',
  'Art. 916: o portador de boa-fé fica imune às defesas que o devedor teria contra quem o antecedeu (**inoponibilidade**), reflexo da **autonomia**. Ao portador o devedor sempre pode opor as exceções de forma, conteúdo literal, falsidade da própria assinatura, defeito de capacidade ou representação e falta de requisito da ação (art. 915).',
  lei=[(CC + '916', 'As exceções, fundadas em relação do devedor com os portadores precedentes', 'tiver agido de má-fé.', 'CC, art. 916'),
       (CC + '915', 'O devedor, além das exceções fundadas nas relações pessoais', 'necessário ao exercício da ação.', 'CC, art. 915')],
  kw=['exceções pessoais', 'má-fé', 'autonomia'])
I(P, 2, 'Títulos de crédito — endosso-mandato',
  'Com a morte ou a incapacidade superveniente do endossante, o endosso-mandato perde a eficácia, como ocorre com o mandato comum.', 'E',
  'Art. 917, § 2º: o endosso-mandato **não perde eficácia** com a morte ou incapacidade superveniente do endossante — diferente do mandato civil (art. 682, II). O devedor só pode opor ao endossatário-mandatário as exceções que tiver contra o **endossante** (§ 3º).',
  lei=[(CC + '917', 'Com a morte ou a superveniente incapacidade do endossante, não perde eficácia o endosso-mandato.', None, 'CC, art. 917, § 2º'),
       (CC + '917', 'Pode o devedor opor ao endossatário de endosso-mandato somente as exceções que tiver contra o endossante.', None, 'CC, art. 917, § 3º')],
  kw=['endosso-mandato', 'não perde eficácia'])
I(P, 2, 'Títulos de crédito — nota promissória vinculada a contrato',
  'A nota promissória vinculada a contrato de abertura de crédito conserva sua autonomia e, por isso, é título executivo hábil, ainda que o contrato seja ilíquido.', 'E',
  '**Súmula 258/STJ**: a nota promissória vinculada a contrato de abertura de crédito **não goza de autonomia**, pela **iliquidez** do título que a originou. Já o avalista de título vinculado a contrato de mútuo responde pelo contrato se nele figurar como **devedor solidário** (Súmula 26/STJ).',
  juris=[J['S258'], J['S26']],
  kw=['nota promissória', 'abertura de crédito', 'iliquidez'])

P = 'DBA26-CIV-4-B2'
# ---------------- PONTO 4-B2 · Responsabilidade civil — RODADA 1
I(P, 1, 'Ato ilícito',
  'Aquele que, por ação ou omissão voluntária, negligência ou imprudência, violar direito e causar dano a outrem, ainda que exclusivamente moral, comete ato ilícito.', 'C',
  'Art. 186: **conduta culposa** + **violação de direito** + **dano** (ainda que só moral).',
  lei=[(CC + '186', 'Aquele que, por ação ou omissão voluntária', 'comete ato ilícito.', 'CC, art. 186')],
  kw=['ato ilícito', 'exclusivamente moral'])
I(P, 1, 'Abuso de direito',
  'Só comete ato ilícito por abuso de direito o titular que, ao exercê-lo, age com a intenção de prejudicar terceiro.', 'E',
  'Art. 187: basta **exceder manifestamente** os limites do **fim econômico ou social**, da **boa-fé** ou dos **bons costumes**. A lei não exige intenção de prejudicar: o critério é objetivo.',
  lei=[(CC + '187', 'Também comete ato ilícito o titular de um direito', 'boa-fé ou pelos bons costumes.', 'CC, art. 187')],
  kw=['abuso de direito', 'fim econômico ou social'])
I(P, 1, 'Excludentes de ilicitude',
  'Não constituem atos ilícitos os praticados em legítima defesa ou no exercício regular de um direito reconhecido, nem a deterioração ou destruição da coisa alheia, ou a lesão a pessoa, a fim de remover perigo iminente.', 'C',
  'Art. 188: **legítima defesa**, **exercício regular de direito** e **estado de necessidade**. No estado de necessidade, porém, o terceiro inocente pode ser indenizado (arts. 929 e 930).',
  lei=[(CC + '188', 'Não constituem atos ilícitos', 'remover perigo iminente.', 'CC, art. 188')],
  kw=['legítima defesa', 'estado de necessidade'])
I(P, 1, 'Responsabilidade objetiva pelo risco',
  'Haverá obrigação de reparar o dano, independentemente de culpa, nos casos especificados em lei, ou quando a atividade normalmente desenvolvida pelo autor do dano implicar, por sua natureza, risco para os direitos de outrem.', 'C',
  'Art. 927, parágrafo único: **cláusula geral de responsabilidade objetiva** (teoria do **risco da atividade**).',
  lei=[(CC + '927', 'Haverá obrigação de reparar o dano, independentemente de culpa', 'risco para os direitos de outrem.', 'CC, art. 927, par. ún.')],
  kw=['independentemente de culpa', 'risco'])
I(P, 1, 'Responsabilidade por fato de terceiro',
  'Os pais, pelos filhos menores sob sua autoridade e em sua companhia, e o empregador, por seus empregados no exercício do trabalho, respondem com base em culpa presumida, que pode ser afastada por prova em contrário.', 'E',
  'Art. 933: as pessoas do art. 932 respondem **ainda que não haja culpa de sua parte** — responsabilidade **objetiva**. A Súmula 341/STF (culpa presumida do patrão) é anterior ao CC/2002.',
  lei=[(CC + '932', 'São também responsáveis pela reparação civil', 'em razão dele;', 'CC, art. 932, I a III'),
       (CC + '933', 'As pessoas indicadas nos incisos I a V do artigo antecedente', 'pelos terceiros ali referidos.', 'CC, art. 933')],
  juris=[J['STF341']],
  kw=['fato de terceiro', 'objetiva'])
I(P, 1, 'Responsabilidade do incapaz',
  'O incapaz não responde pelos prejuízos que causar, cabendo a reparação exclusivamente aos seus responsáveis.', 'E',
  'Art. 928: o incapaz responde se os responsáveis **não tiverem obrigação** de fazê-lo ou **não dispuserem de meios** — responsabilidade **subsidiária**, **mitigada** e **equitativa**, que não pode privá-lo do necessário.',
  lei=[(CC + '928', 'O incapaz responde pelos prejuízos que causar', 'meios suficientes.', 'CC, art. 928')],
  kw=['incapaz', 'subsidiária', 'equitativa'])
I(P, 1, 'Independência das esferas civil e criminal',
  'A responsabilidade civil é independente da criminal, não se podendo questionar mais sobre a existência do fato, ou sobre quem seja o seu autor, quando estas questões se acharem decididas no juízo criminal.', 'C',
  'Art. 935: **independência relativa** — o que o juízo criminal decidiu sobre **fato** e **autoria** vincula o cível.',
  lei=[(CC + '935', 'A responsabilidade civil é independente da criminal', 'decididas no juízo criminal.', 'CC, art. 935')],
  kw=['independente da criminal', 'autoria'])
I(P, 1, 'Dano causado por animal',
  'O dono, ou detentor, do animal ressarcirá o dano por este causado, se não provar que o guardava e vigiava com cuidado preciso.', 'E',
  'Art. 936: as excludentes são **culpa da vítima** ou **força maior**. A prova de guarda cuidadosa era a regra do Código de 1916 — hoje a responsabilidade é **objetiva**.',
  lei=[(CC + '936', 'O dono, ou detentor, do animal', 'culpa da vítima ou força maior.', 'CC, art. 936')],
  peg='A AOCP já cobrou o art. 936; a troca é pela fórmula do CC/1916.',
  kw=['animal', 'culpa da vítima ou força maior'])
I(P, 1, 'Extensão do dano',
  'A indenização mede-se pela extensão do dano; se houver excessiva desproporção entre a gravidade da culpa e o dano, poderá o juiz reduzir, equitativamente, a indenização.', 'C',
  'Art. 944: **princípio da reparação integral**, com a válvula do parágrafo único (**redução equitativa**).',
  lei=[(CC + '944', 'A indenização mede-se pela extensão do dano.', None, 'CC, art. 944'),
       (CC + '944', 'Se houver excessiva desproporção', 'eqüitativamente, a indenização.', 'CC, art. 944, par. ún.')],
  kw=['extensão do dano', 'reduzir, equitativamente'])
I(P, 1, 'Culpa concorrente da vítima',
  'Se a vítima tiver concorrido culposamente para o evento danoso, a sua indenização será fixada tendo-se em conta a gravidade de sua culpa em confronto com a do autor do dano.', 'C',
  'Art. 945: a **culpa concorrente** não exclui, mas **reduz** a indenização; a culpa **exclusiva** da vítima rompe o nexo.',
  lei=[(CC + '945', 'Se a vítima tiver concorrido culposamente', 'a do autor do dano.', 'CC, art. 945')],
  kw=['culpa concorrente'])
I(P, 1, 'Cumulação de danos',
  'Não é possível cumular, em razão do mesmo fato, indenização por dano estético e por dano moral, porque o primeiro é espécie do segundo.', 'E',
  '**Súmula 387/STJ**: é **lícita a cumulação** do dano estético com o moral. E a **Súmula 37/STJ** admite cumular dano material e moral oriundos do mesmo fato.',
  juris=[J['S387'], J['S37']],
  kw=['dano estético', 'cumulação'])

# ---------------- PONTO 4-B2 — RODADA 2
I(P, 2, 'Correção e juros no dano moral',
  'Na indenização por dano moral decorrente de ato ilícito extracontratual, tanto a correção monetária quanto os juros de mora incidem desde a data do evento danoso.', 'E',
  'Os **juros** correm do **evento danoso** (Súmula 54/STJ), mas a **correção monetária** do dano moral incide **desde o arbitramento** (Súmula 362/STJ). No dano material, a correção corre do efetivo prejuízo (Súmula 43/STJ).',
  juris=[J['S362'], J['S54'], J['S43']],
  kw=['correção monetária', 'arbitramento'])
I(P, 2, 'Transporte de cortesia',
  'No transporte desinteressado, de simples cortesia, o transportador só responde pelos danos causados ao transportado quando incorrer em dolo ou culpa grave.', 'C',
  '**Súmula 145/STJ** + art. 736: o transporte **gratuito por amizade ou cortesia** não segue as regras do contrato de transporte.',
  lei=[(CC + '736', 'Não se subordina às normas do contrato de transporte', 'amizade ou cortesia.', 'CC, art. 736')],
  juris=[J['S145']],
  kw=['cortesia', 'dolo ou culpa grave'])
I(P, 2, 'Culpa de terceiro no transporte',
  'A responsabilidade contratual do transportador por acidente com o passageiro é elidida por culpa de terceiro, que responderá diretamente perante a vítima.', 'E',
  'Art. 735: a responsabilidade **não é elidida por culpa de terceiro**; o transportador paga e tem **ação regressiva** contra ele.',
  lei=[(CC + '735', 'A responsabilidade contratual do transportador', 'ação regressiva.', 'CC, art. 735')],
  kw=['transportador', 'culpa de terceiro', 'ação regressiva'])
I(P, 2, 'Regresso contra descendente incapaz',
  'Aquele que ressarcir o dano causado por outrem pode reaver o que houver pago daquele por quem pagou, salvo se o causador do dano for descendente seu, absoluta ou relativamente incapaz.', 'C',
  'Art. 934: **direito de regresso**, com a exceção do **descendente incapaz**.',
  lei=[(CC + '934', 'Aquele que ressarcir o dano causado por outrem', 'absoluta ou relativamente incapaz.', 'CC, art. 934')],
  kw=['direito de regresso', 'descendente'])
I(P, 2, 'Solidariedade dos coautores',
  'São solidariamente responsáveis com os autores os coautores e as pessoas designadas no art. 932, como os pais e o empregador.', 'C',
  'Art. 942, parágrafo único: **solidariedade legal** entre autores, coautores e responsáveis por fato de terceiro.',
  lei=[(CC + '942', 'São solidariamente responsáveis com os autores', 'designadas no art. 932.', 'CC, art. 942, par. ún.')],
  kw=['solidariamente responsáveis', 'coautores'])
I(P, 2, 'Transmissão aos herdeiros',
  'O direito de exigir reparação e a obrigação de prestá-la transmitem-se com a herança, e os herdeiros da vítima podem ajuizar ação de indenização por danos morais sofridos pelo falecido.', 'C',
  'Art. 943 + **Súmula 642/STJ**: herdeiros têm legitimidade para **ajuizar ou prosseguir** a ação.',
  lei=[(CC + '943', 'O direito de exigir reparação', 'transmitem-se com a herança.', 'CC, art. 943')],
  juris=[J['S642']],
  kw=['herança', 'herdeiros'])
I(P, 2, 'Coisas caídas de prédio',
  'Aquele que habitar prédio responde pelo dano proveniente das coisas que dele caírem ou forem lançadas em lugar indevido, desde que a vítima prove a sua culpa.', 'E',
  'Art. 938 (*effusis et dejectis*): a responsabilidade do habitante é **objetiva** — não depende de prova de culpa.',
  lei=[(CC + '938', 'Aquele que habitar prédio', 'lançadas em lugar indevido.', 'CC, art. 938')],
  kw=['habitar prédio', 'objetiva'])
I(P, 2, 'Danos pela imprensa',
  'São civilmente responsáveis pelo ressarcimento de dano decorrente de publicação pela imprensa tanto o autor do escrito quanto o proprietário do veículo de divulgação.', 'C',
  '**Súmula 221/STJ**: legitimidade passiva do **autor** e do **proprietário do veículo**.',
  juris=[J['S221']],
  kw=['imprensa', 'autor do escrito'])
I(P, 2, 'Recusa de cobertura e dano moral',
  'A recusa indevida de cobertura médico-assistencial por operadora de plano de saúde gera, por si só, dano moral presumido.', 'E',
  'No **Tema 1.365**, o STJ fixou que a simples recusa **não gera dano moral in re ipsa**; é preciso demonstrar abalo que ultrapasse o mero aborrecimento.',
  juris=[J['T1365']],
  kw=['in re ipsa', 'plano de saúde'])
I(P, 2, 'Indenização por homicídio',
  'No caso de homicídio, a indenização consiste, sem excluir outras reparações, no pagamento das despesas com o tratamento da vítima, seu funeral e o luto da família, e na prestação de alimentos às pessoas a quem o morto os devia, levando-se em conta a duração provável da vida da vítima.', 'C',
  'Art. 948: **danos emergentes** (tratamento, funeral, luto) + **pensão** (alimentos). A morte de filho menor é indenizável ainda que ele não trabalhe (Súmula 491/STF).',
  lei=[(CC + '948', 'No caso de homicídio', 'duração provável da vida da vítima.', 'CC, art. 948')],
  juris=[J['STF491']],
  kw=['homicídio', 'alimentos'])
