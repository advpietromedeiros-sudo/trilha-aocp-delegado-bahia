# Jurisprudência do Pente Fino de Direito Penal (Parte Geral) — cada entrada CONFERIDA em 08/11/2026:
#  STJ súmulas: processo.stj.jus.br/SCON/sumstj (data = "julgado em"; nenhuma das usadas com indicação de cancelamento).
#   As Súmulas 545 e 630 foram REVISADAS em 10/09/2025 (Terceira Seção, REsp 2.001.973/RS, Tema 1.194): vale a redação nova.
#  STJ temas repetitivos: processo.stj.jus.br/repetitivos (data = "Julgado em").
#  STF súmulas: PDF oficial "Enunciados das Súmulas do STF 1 a 736" (data = Sessão Plenária de aprovação).
#  STF súmulas vinculantes 26 e 56: portal.stf.jus.br/jurisprudencia/sumariosumulas.asp (a página traz só a publicação
#   do enunciado no DJe, e é essa a data usada, dita na fonte).
#  STF ADPF 779: notícia oficial de 01/08/2023 (mérito julgado na sessão plenária de 01/08/2023).
#  STF HC 176.473: notícia oficial de 28/04/2020 (sessão virtual do Plenário de 17 a 24/04/2020).
#  STF Tema 788/RG (ARE 848.107): notícia oficial de 05/07/2023 (sessão virtual encerrada em 30/06/2023).
#  STF HC 84.412/SP: Segunda Turma, julgado em 19/10/2004 (data citada nos acórdãos do próprio STF que o seguem).
from base import _s

SCON = 'processo.stj.jus.br/SCON/sumstj'
REP = 'processo.stj.jus.br/repetitivos'
STFPDF = 'stf.jus.br — Enunciados das Súmulas do STF 1 a 736 (PDF oficial)'
SV = 'portal.stf.jus.br — Súmulas Vinculantes (data de publicação do enunciado no DJe)'
STFNOT = 'portal.stf.jus.br — notícia oficial do julgamento'
J = {
    # ---------------- STJ — súmulas
    'S17': _s('STJ', 'Súmula 17/STJ', '20/11/1990', 'Quando o falso se exaure no estelionato, sem mais potencialidade lesiva, é por este absorvido.', SCON),
    'S18': _s('STJ', 'Súmula 18/STJ', '20/11/1990', 'A sentença concessiva do perdão judicial é declaratória da extinção da punibilidade, não subsistindo qualquer efeito condenatório.', SCON),
    'S74': _s('STJ', 'Súmula 74/STJ', '15/04/1993', 'Para efeitos penais, o reconhecimento da menoridade do réu requer prova por documento hábil.', SCON),
    'S96': _s('STJ', 'Súmula 96/STJ', '03/03/1994', 'O crime de extorsão consuma-se independentemente da obtenção da vantagem indevida.', SCON),
    'S171': _s('STJ', 'Súmula 171/STJ', '23/10/1996', 'Cominadas cumulativamente, em lei especial, penas privativa de liberdade e pecuniária, é defeso a substituição da prisão por multa.', SCON),
    'S191': _s('STJ', 'Súmula 191/STJ', '25/06/1997', 'A pronúncia é causa interruptiva da prescrição, ainda que o Tribunal do Júri venha a desclassificar o crime.', SCON),
    'S220': _s('STJ', 'Súmula 220/STJ', '12/05/1999', 'A reincidência não influi no prazo da prescrição da pretensão punitiva.', SCON),
    'S231': _s('STJ', 'Súmula 231/STJ', '22/09/1999', 'A incidência da circunstância atenuante não pode conduzir à redução da pena abaixo do mínimo legal.', SCON),
    'S241': _s('STJ', 'Súmula 241/STJ', '23/08/2000', 'A reincidência penal não pode ser considerada como circunstância agravante e, simultaneamente, como circunstância judicial.', SCON),
    'S243': _s('STJ', 'Súmula 243/STJ', '11/12/2000', 'A suspensão do processo não se aplica às infrações em concurso material, formal ou continuidade delitiva quando a pena mínima, pelo somatório ou pela incidência da majorante, ultrapassar 1 ano.', SCON),
    'S269': _s('STJ', 'Súmula 269/STJ', '22/05/2002', 'É admissível a adoção do regime prisional semiaberto aos reincidentes condenados a pena igual ou inferior a quatro anos se favoráveis as circunstâncias judiciais.', SCON),
    'S338': _s('STJ', 'Súmula 338/STJ', '09/05/2007', 'A prescrição penal é aplicável nas medidas socioeducativas.', SCON),
    'S415': _s('STJ', 'Súmula 415/STJ', '09/12/2009', 'O período de suspensão do prazo prescricional é regulado pelo máximo da pena cominada.', SCON),
    'S438': _s('STJ', 'Súmula 438/STJ', '28/04/2010', 'É inadmissível a extinção da punibilidade pela prescrição da pretensão punitiva com fundamento em pena hipotética, independentemente da existência ou sorte do processo penal.', SCON),
    'S440': _s('STJ', 'Súmula 440/STJ', '28/04/2010', 'Fixada a pena-base no mínimo legal, é vedado o estabelecimento de regime prisional mais gravoso do que o cabível em razão da sanção imposta, com base apenas na gravidade abstrata do delito.', SCON),
    'S441': _s('STJ', 'Súmula 441/STJ', '28/04/2010', 'A falta grave não interrompe o prazo para obtenção de livramento condicional.', SCON),
    'S442': _s('STJ', 'Súmula 442/STJ', '28/04/2010', 'É inadmissível aplicar, no furto qualificado, pelo concurso de agentes, a majorante do roubo.', SCON),
    'S443': _s('STJ', 'Súmula 443/STJ', '28/04/2010', 'O aumento na terceira fase no roubo circunstanciado exige fundamentação concreta, não bastando a mera indicação do número de majorantes.', SCON),
    'S444': _s('STJ', 'Súmula 444/STJ', '28/04/2010', 'É vedada a utilização de inquéritos policiais e ações penais em curso para agravar a pena-base.', SCON),
    'S471': _s('STJ', 'Súmula 471/STJ', '23/02/2011', 'Os condenados por crimes hediondos ou assemelhados cometidos antes da vigência da Lei 11.464/2007 sujeitam-se ao art. 112 da LEP para a progressão de regime.', SCON),
    'S491': _s('STJ', 'Súmula 491/STJ', '08/08/2012', 'É inadmissível a chamada progressão per saltum de regime prisional.', SCON),
    'S493': _s('STJ', 'Súmula 493/STJ', '08/08/2012', 'É inadmissível a fixação de pena substitutiva (art. 44 do CP) como condição especial ao regime aberto.', SCON),
    'S500': _s('STJ', 'Súmula 500/STJ', '23/10/2013', 'A configuração do crime do art. 244-B do ECA independe da prova da efetiva corrupção do menor, por se tratar de delito formal.', SCON),
    'S501': _s('STJ', 'Súmula 501/STJ', '23/10/2013', 'É cabível a aplicação retroativa da Lei 11.343/2006 desde que, na íntegra, seja mais favorável ao réu do que a Lei 6.368/1976, sendo vedada a combinação de leis.', SCON),
    'S511': _s('STJ', 'Súmula 511/STJ', '11/06/2014', 'É possível o privilégio do § 2º do art. 155 do CP no furto qualificado, se presentes a primariedade, o pequeno valor da coisa e a qualificadora for de ordem objetiva.', SCON),
    'S513': _s('STJ', 'Súmula 513/STJ', '11/06/2014', 'A abolitio criminis temporária da Lei 10.826/2003 aplica-se à posse de arma de uso permitido com numeração raspada, suprimida ou adulterada, praticada somente até 23/10/2005.', SCON),
    'S526': _s('STJ', 'Súmula 526/STJ', '13/05/2015', 'O reconhecimento de falta grave decorrente de fato definido como crime doloso no cumprimento da pena prescinde do trânsito em julgado de sentença penal condenatória.', SCON),
    'S527': _s('STJ', 'Súmula 527/STJ', '13/05/2015', 'O tempo de duração da medida de segurança não deve ultrapassar o limite máximo da pena abstratamente cominada ao delito praticado.', SCON),
    'S534': _s('STJ', 'Súmula 534/STJ', '10/06/2015', 'A prática de falta grave interrompe a contagem do prazo para a progressão de regime, o qual se reinicia a partir do cometimento dessa infração.', SCON),
    'S535': _s('STJ', 'Súmula 535/STJ', '10/06/2015', 'A prática de falta grave não interrompe o prazo para fim de comutação de pena ou indulto.', SCON),
    'S545': _s('STJ', 'Súmula 545/STJ (redação revisada — Tema 1.194, REsp 2.001.973/RS)', '10/09/2025', 'A confissão do autor possibilita a atenuação da pena prevista no art. 65, III, d, do Código Penal, independentemente de ser utilizada na formação do convencimento do julgador.', SCON),
    'S562': _s('STJ', 'Súmula 562/STJ', '24/02/2016', 'É possível a remição de parte do tempo de execução da pena quando o condenado, em regime fechado ou semiaberto, desempenha atividade laborativa, ainda que extramuros.', SCON),
    'S567': _s('STJ', 'Súmula 567/STJ', '24/02/2016', 'Sistema de vigilância por monitoramento eletrônico ou segurança no interior de estabelecimento comercial, por si só, não torna impossível a configuração do crime de furto.', SCON),
    'S582': _s('STJ', 'Súmula 582/STJ', '14/09/2016', 'Consuma-se o roubo com a inversão da posse do bem mediante violência ou grave ameaça, ainda que por breve tempo e com perseguição imediata e recuperação da coisa, sendo prescindível a posse mansa e pacífica ou desvigiada.', SCON),
    'S588': _s('STJ', 'Súmula 588/STJ', '13/09/2017', 'Crime ou contravenção contra a mulher com violência ou grave ameaça no ambiente doméstico impossibilita a substituição da pena privativa de liberdade por restritiva de direitos.', SCON),
    'S589': _s('STJ', 'Súmula 589/STJ', '13/09/2017', 'É inaplicável o princípio da insignificância nos crimes ou contravenções penais praticados contra a mulher no âmbito das relações domésticas.', SCON),
    'S599': _s('STJ', 'Súmula 599/STJ', '20/11/2017', 'O princípio da insignificância é inaplicável aos crimes contra a administração pública.', SCON),
    'S606': _s('STJ', 'Súmula 606/STJ', '11/04/2018', 'Não se aplica o princípio da insignificância à transmissão clandestina de sinal de internet via radiofrequência (art. 183 da Lei 9.472/1997).', SCON),
    'S617': _s('STJ', 'Súmula 617/STJ', '26/09/2018', 'A ausência de suspensão ou revogação do livramento condicional antes do término do período de prova enseja a extinção da punibilidade pelo integral cumprimento da pena.', SCON),
    'S630': _s('STJ', 'Súmula 630/STJ (redação revisada — Tema 1.194, REsp 2.001.973/RS)', '10/09/2025', 'A atenuante da confissão no tráfico, quando o acusado admite a posse para uso próprio e nega o tráfico, deve incidir em proporção inferior à da confissão plena.', SCON),
    'S631': _s('STJ', 'Súmula 631/STJ', '24/04/2019', 'O indulto extingue os efeitos primários da condenação (pretensão executória), mas não atinge os efeitos secundários, penais ou extrapenais.', SCON),
    'S636': _s('STJ', 'Súmula 636/STJ', '26/06/2019', 'A folha de antecedentes criminais é documento suficiente a comprovar os maus antecedentes e a reincidência.', SCON),
    'S643': _s('STJ', 'Súmula 643/STJ', '10/02/2021', 'A execução da pena restritiva de direitos depende do trânsito em julgado da condenação.', SCON),
    'S645': _s('STJ', 'Súmula 645/STJ', '10/02/2021', 'O crime de fraude à licitação é formal, e sua consumação prescinde da comprovação do prejuízo ou da obtenção de vantagem.', SCON),
    'S659': _s('STJ', 'Súmula 659/STJ', '13/09/2023', 'No crime continuado, a fração de aumento segue o número de delitos: 1/6 para dois, 1/5 para três, 1/4 para quatro, 1/3 para cinco, 1/2 para seis e 2/3 para sete ou mais.', SCON),
    # ---------------- STJ — temas repetitivos
    'T585': _s('STJ', 'Tema 585/STJ — REsp 1.931.145/SP', '22/06/2022', 'É possível compensar integralmente a confissão espontânea com a reincidência, específica ou não; na multirreincidência prepondera a agravante, admitida compensação proporcional.', REP),
    'T931': _s('STJ', 'Tema 931/STJ (revisado) — REsp 2.090.454/SP e REsp 2.024.901/SP', '28/02/2024', 'O inadimplemento da multa, cumprida a pena privativa ou restritiva, não obsta a extinção da punibilidade ante a alegada hipossuficiência do condenado, salvo decisão motivada que indique concretamente a possibilidade de pagamento.', REP),
    'T1077': _s('STJ', 'Tema 1.077/STJ — REsp 1.794.854/DF', '23/06/2021', 'Condenações transitadas em julgado não usadas para a reincidência só podem ser valoradas na 1ª fase como antecedentes, não para desabonar personalidade ou conduta social.', REP),
    'T1100': _s('STJ', 'Tema 1.100/STJ — REsp 1.920.091/RJ e REsp 1.930.130/MG', '10/08/2022', 'O acórdão condenatório do art. 117, IV, do CP interrompe a prescrição, inclusive quando confirmatório da sentença condenatória, mantendo, reduzindo ou aumentando a pena.', REP),
    'T1172': _s('STJ', 'Tema 1.172/STJ — REsp 2.003.716/RS', '24/10/2023', 'A reincidência específica como único fundamento só justifica agravar a pena em fração maior que 1/6 em casos excepcionais, com fundamentação concreta e detalhada.', REP),
    'T1194': _s('STJ', 'Tema 1.194/STJ — REsp 2.001.973/RS', '10/09/2025', 'A confissão espontânea atenua a pena mesmo que não usada na formação do convencimento e ainda que haja outras provas, desde que não retratada (salvo se serviu à apuração); incide em menor proporção e não prepondera quando o fato confessado tem pena menor ou configura excludente.', REP),
    'T1205': _s('STJ', 'Tema 1.205/STJ — REsp 2.062.375/AL e REsp 2.062.095/AL', '24/10/2023', 'A restituição imediata e integral do bem furtado não constitui, por si só, motivo suficiente para a incidência do princípio da insignificância.', REP),
    # ---------------- STF — súmulas
    'STF145': _s('STF', 'Súmula 145/STF', '13/12/1963', 'Não há crime, quando a preparação do flagrante pela polícia torna impossível a sua consumação.', STFPDF),
    'STF146': _s('STF', 'Súmula 146/STF', '13/12/1963', 'A prescrição da ação penal regula-se pela pena concretizada na sentença, quando não há recurso da acusação.', STFPDF),
    'STF497': _s('STF', 'Súmula 497/STF', '03/12/1969', 'Quando se tratar de crime continuado, a prescrição regula-se pela pena imposta na sentença, não se computando o acréscimo decorrente da continuação.', STFPDF),
    'STF525': _s('STF', 'Súmula 525/STF', '03/12/1969', 'A medida de segurança não será aplicada em segunda instância, quando só o réu tenha recorrido.', STFPDF),
    'STF554': _s('STF', 'Súmula 554/STF', '15/12/1976', 'O pagamento de cheque emitido sem provisão de fundos, após o recebimento da denúncia, não obsta ao prosseguimento da ação penal.', STFPDF),
    'STF610': _s('STF', 'Súmula 610/STF', '17/10/1984', 'Há crime de latrocínio, quando o homicídio se consuma, ainda que não realize o agente a subtração de bens da vítima.', STFPDF),
    'STF611': _s('STF', 'Súmula 611/STF', '17/10/1984', 'Transitada em julgado a sentença condenatória, compete ao Juízo das execuções a aplicação de lei mais benigna.', STFPDF),
    'STF711': _s('STF', 'Súmula 711/STF', '24/09/2003', 'A lei penal mais grave aplica-se ao crime continuado ou ao crime permanente, se a sua vigência é anterior à cessação da continuidade ou da permanência.', STFPDF),
    'STF715': _s('STF', 'Súmula 715/STF', '24/09/2003', 'A pena unificada para atender ao limite do art. 75 do CP (então 30 anos) não é considerada para a concessão de outros benefícios, como o livramento condicional ou regime mais favorável.', STFPDF),
    'STF718': _s('STF', 'Súmula 718/STF', '24/09/2003', 'A opinião do julgador sobre a gravidade em abstrato do crime não constitui motivação idônea para a imposição de regime mais severo do que o permitido segundo a pena aplicada.', STFPDF),
    'STF719': _s('STF', 'Súmula 719/STF', '24/09/2003', 'A imposição do regime de cumprimento mais severo do que a pena aplicada permitir exige motivação idônea.', STFPDF),
    'STF723': _s('STF', 'Súmula 723/STF', '26/11/2003', 'Não se admite a suspensão condicional do processo por crime continuado, se a soma da pena mínima da infração mais grave com o aumento mínimo de um sexto for superior a um ano.', STFPDF),
    # ---------------- STF — vinculantes
    'SV26': _s('STF', 'Súmula Vinculante 26 (publicada no DJe de 23/12/2009)', '23/12/2009', 'Para a progressão em crime hediondo ou equiparado, o juízo da execução observará a inconstitucionalidade do art. 2º da Lei 8.072/1990, podendo determinar, de modo fundamentado, exame criminológico.', SV),
    'SV56': _s('STF', 'Súmula Vinculante 56 (publicada no DJe de 08/08/2016)', '08/08/2016', 'A falta de estabelecimento penal adequado não autoriza a manutenção do condenado em regime prisional mais gravoso, observados os parâmetros do RE 641.320/RS.', SV),
    # ---------------- STF — controle concentrado, repercussão geral e HC
    'ADPF779': _s('STF', 'ADPF 779, Plenário (mérito)', '01/08/2023', 'A tese da "legítima defesa da honra" é inconstitucional (dignidade humana, proteção à vida, igualdade de gênero); não pode ser invocada direta ou indiretamente, sob pena de nulidade do ato e do julgamento.', STFNOT),
    'HC176473': _s('STF', 'HC 176.473, Plenário (sessão virtual de 17 a 24/04/2020)', '24/04/2020', 'Nos termos do art. 117, IV, do CP, o acórdão condenatório sempre interrompe a prescrição, inclusive quando confirmatório da sentença, seja mantendo, reduzindo ou aumentando a pena.', STFNOT),
    'RG788': _s('STF', 'Tema 788/RG — ARE 848.107/DF (sessão virtual encerrada em 30/06/2023)', '30/06/2023', 'A prescrição da pretensão executória só começa a correr do trânsito em julgado da condenação para AMBAS as partes; modulação: vale para os casos com trânsito para a acusação após 11/11/2020.', STFNOT),
    'HC84412': _s('STF', 'HC 84.412/SP, Segunda Turma', '19/10/2004', 'Insignificância exige, cumulativamente: mínima ofensividade da conduta, nenhuma periculosidade social da ação, reduzidíssimo grau de reprovabilidade do comportamento e inexpressividade da lesão jurídica.', 'stf.jus.br — acórdãos do STF que reproduzem os vetores do HC 84.412'),
    # ================ PARTE ESPECIAL — acrescentadas em 08/11/2026, cada uma CONFERIDA nessa data:
    #  STJ súmulas no SCON (data = "julgado em"; nenhuma com indicação de cancelamento); temas no repetitivos do STJ;
    #  STF súmulas 603 e 714 na página oficial de cada súmula (portal.stf.jus.br/jurisprudencia/sumariosumulas.asp),
    #   que traz só a publicação no DJ — é essa a data usada, dita na fonte; ADPF 54, ADPF 496 e Tema 1.003/RG nas
    #   notícias oficiais e no andamento do tema no portal do STF.
    'S24': _s('STJ', 'Súmula 24/STJ', '04/04/1991', 'Aplica-se ao crime de estelionato, em que figure como vítima entidade autárquica da Previdência Social, a qualificadora do § 3º do art. 171 do Código Penal.', SCON),
    'S73': _s('STJ', 'Súmula 73/STJ', '15/04/1993', 'A utilização de papel moeda grosseiramente falsificado configura, em tese, o crime de estelionato, da competência da Justiça Estadual.', SCON),
    'S502': _s('STJ', 'Súmula 502/STJ', '23/10/2013', 'Presentes a materialidade e a autoria, afigura-se típica, em relação ao crime do art. 184, § 2º, do CP, a conduta de expor à venda CDs e DVDs piratas.', SCON),
    'S522': _s('STJ', 'Súmula 522/STJ', '25/03/2015', 'A conduta de atribuir-se falsa identidade perante autoridade policial é típica, ainda que em situação de alegada autodefesa.', SCON),
    'S542': _s('STJ', 'Súmula 542/STJ', '26/08/2015', 'A ação penal relativa ao crime de lesão corporal resultante de violência doméstica contra a mulher é pública incondicionada.', SCON),
    'S574': _s('STJ', 'Súmula 574/STJ', '22/06/2016', 'Para a materialidade da violação de direito autoral, basta a perícia por amostragem do produto apreendido, nos aspectos externos, sendo desnecessário identificar os titulares dos direitos violados ou quem os represente.', SCON),
    'S593': _s('STJ', 'Súmula 593/STJ', '25/10/2017', 'O estupro de vulnerável se configura com a conjunção carnal ou prática de ato libidinoso com menor de 14 anos, sendo irrelevante eventual consentimento da vítima, sua experiência sexual anterior ou existência de relacionamento amoroso com o agente.', SCON),
    'T157': _s('STJ', 'Tema 157/STJ (revisado) — REsp 1.688.878/SP e REsp 1.709.029/MG', '28/02/2018', 'Incide o princípio da insignificância aos crimes tributários federais e de descaminho quando o débito tributário não ultrapassar R$ 20.000,00 (art. 20 da Lei 10.522/2002, atualizado pelas Portarias 75 e 130 do Ministério da Fazenda).', REP),
    'T934': _s('STJ', 'Tema 934/STJ — REsp 1.524.450/RJ', '14/10/2015', 'Consuma-se o crime de furto com a posse de fato da res furtiva, ainda que por breve espaço de tempo e seguida de perseguição ao agente, sendo prescindível a posse mansa e pacífica ou desvigiada.', REP),
    'T1121': _s('STJ', 'Tema 1.121/STJ — REsp 1.959.697/SC e outros', '08/06/2022', 'Presente o dolo específico de satisfazer à lascívia, a prática de ato libidinoso com menor de 14 anos configura estupro de vulnerável (art. 217-A), independentemente da ligeireza ou superficialidade da conduta, sem desclassificação para importunação sexual (art. 215-A).', REP),
    'STF603': _s('STF', 'Súmula 603/STF (publicada no DJ de 31/10/1984)', '31/10/1984', 'A competência para o processo e julgamento de latrocínio é do juiz singular e não do tribunal do júri.', 'portal.stf.jus.br — página oficial da Súmula 603 (data de publicação do enunciado)'),
    'STF714': _s('STF', 'Súmula 714/STF (publicada no DJ de 13/10/2003)', '13/10/2003', 'É concorrente a legitimidade do ofendido, mediante queixa, e do Ministério Público, condicionada à representação do ofendido, para a ação penal por crime contra a honra de servidor público em razão do exercício de suas funções.', 'portal.stf.jus.br — página oficial da Súmula 714 (data de publicação do enunciado)'),
    'ADPF54': _s('STF', 'ADPF 54, Plenário (mérito)', '12/04/2012', 'É inconstitucional interpretar a interrupção da gravidez de feto anencéfalo como conduta tipificada nos arts. 124, 126 e 128, I e II, do CP.', STFNOT),
    'ADPF496': _s('STF', 'ADPF 496, Plenário (sessão virtual finalizada em 19/06/2020)', '19/06/2020', 'O crime de desacato (art. 331 do CP) foi recepcionado pela Constituição de 1988; a tipificação não viola a liberdade de expressão, e o tipo deve ser interpretado restritivamente.', STFNOT),
    'RG1003': _s('STF', 'Tema 1.003/RG — RE 979.962/RS (mérito em 24/03/2021; tese readequada nos embargos, sessão virtual de 02 a 12/06/2023)', '24/03/2021', 'É inconstitucional aplicar a pena de 10 a 15 anos do art. 273 (Lei 9.677/1998) à hipótese do § 1º-B, I (produto sem registro no órgão de vigilância sanitária); para ela fica repristinada a pena originária: reclusão, de 1 a 3 anos, e multa.', 'portal.stf.jus.br — andamento do Tema 1.003 e Informativo 1.011'),
}
