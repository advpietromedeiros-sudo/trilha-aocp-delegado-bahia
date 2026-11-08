# Jurisprudência do Pente Fino de Direito Processual Penal — cada entrada CONFERIDA em 08/11/2026:
#  STJ súmulas: processo.stj.jus.br/SCON/sumstj (data = "julgado em"; nenhuma com indicação de cancelamento).
#  STF súmulas: PDF oficial "Enunciados das Súmulas do STF 1 a 736" (.scratch/pente_fino/stf_sumulas.txt; data = Sessão
#  Plenária; nenhuma das usadas marcada como superada ou cancelada). A 690 ficou de fora (tida por superada).
#  STF súmulas vinculantes: portal.stf.jus.br/jurisprudencia/sumariosumulas.asp (a página traz só a publicação no DJe,
#  e é essa a data usada, dita na fonte).
#  STF ADIs 6.298, 6.299, 6.300 e 6.305 (juiz das garantias): notícia oficial de 24/08/2023 (resultado proclamado na sessão
#  de 24/08/2023). HC 185.913 (ANPP): notícia oficial de 18/09/2024 (sessão de 18/09/2024). Tema 280 (RE 603.616):
#  julgamento de 05/11/2015 (portal do STF, andamento do tema). ADPFs 395 e 444: notícia oficial (sessão de 14/06/2018).
#  ADIs 3.360 e 4.109: notícia oficial de 14/02/2022 (sessão virtual concluída em 11/02/2022). Tema 184 (RE 593.727):
#  julgamento de 14/05/2015 (portal do STF, andamento do tema).
#  STJ HC 598.886/SC: Informativo 684 (julgado em 27/10/2020). STJ RHC 158.580/BA: Informativo 735 (julgado em 19/04/2022).
#  STJ HC 877.943/MS: Informativo 818 (Terceira Seção, julgado em 18/04/2024). STF ADI 5.637: notícia oficial de
#  15/03/2022 e Informativo 1.046 (sessão virtual encerrada em 11/03/2022).
from base import _s

SCON = 'processo.stj.jus.br/SCON/sumstj'
STFPDF = 'stf.jus.br — Enunciados das Súmulas do STF 1 a 736 (PDF oficial)'
SV = 'portal.stf.jus.br — Súmulas Vinculantes (data de publicação do enunciado no DJe)'
STFNOT = 'portal.stf.jus.br — notícia oficial do julgamento'
INF = 'processo.stj.jus.br — Informativo de Jurisprudência'
J = {
    # ---------------- STJ
    'S6': _s('STJ', 'Súmula 6/STJ', '07/06/1990', 'Compete à Justiça Comum Estadual o delito decorrente de acidente de trânsito com viatura da polícia militar, salvo se autor e vítima forem policiais militares em atividade.', SCON),
    'S21': _s('STJ', 'Súmula 21/STJ', '06/12/1990', 'Pronunciado o réu, fica superada a alegação do constrangimento ilegal da prisão por excesso de prazo na instrução.', SCON),
    'S38': _s('STJ', 'Súmula 38/STJ', '19/03/1992', 'Compete à Justiça Estadual Comum o processo por contravenção penal, ainda que praticada em detrimento de bens, serviços ou interesse da União ou de suas entidades.', SCON),
    'S42': _s('STJ', 'Súmula 42/STJ', '14/05/1992', 'Compete à Justiça Comum Estadual processar e julgar as causas cíveis em que é parte sociedade de economia mista e os crimes praticados em seu detrimento.', SCON),
    'S52': _s('STJ', 'Súmula 52/STJ', '17/09/1992', 'Encerrada a instrução criminal, fica superada a alegação de constrangimento por excesso de prazo.', SCON),
    'S53': _s('STJ', 'Súmula 53/STJ', '17/09/1992', 'Compete à Justiça Comum Estadual processar e julgar civil acusado de prática de crime contra instituições militares estaduais.', SCON),
    'S62': _s('STJ', 'Súmula 62/STJ', '19/11/1992', 'Compete à Justiça Estadual o crime de falsa anotação na CTPS atribuído a empresa privada.', SCON),
    'S64': _s('STJ', 'Súmula 64/STJ', '03/12/1992', 'Não constitui constrangimento ilegal o excesso de prazo na instrução, provocado pela defesa.', SCON),
    'S104': _s('STJ', 'Súmula 104/STJ', '19/05/1994', 'Compete à Justiça Estadual o processo dos crimes de falsificação e uso de documento falso relativo a estabelecimento particular de ensino.', SCON),
    'S122': _s('STJ', 'Súmula 122/STJ', '01/12/1994', 'Compete à Justiça Federal o processo e julgamento unificado dos crimes conexos de competência federal e estadual, não se aplicando a regra do art. 78, II, "a", do CPP.', SCON),
    'S140': _s('STJ', 'Súmula 140/STJ', '18/05/1995', 'Compete à Justiça Comum Estadual processar e julgar crime em que o indígena figure como autor ou vítima.', SCON),
    'S147': _s('STJ', 'Súmula 147/STJ', '07/12/1995', 'Compete à Justiça Federal processar e julgar os crimes praticados contra funcionário público federal, quando relacionados com o exercício da função.', SCON),
    'S151': _s('STJ', 'Súmula 151/STJ', '14/02/1996', 'A competência para o crime de contrabando ou descaminho define-se pela prevenção do juízo federal do lugar da apreensão dos bens.', SCON),
    'S165': _s('STJ', 'Súmula 165/STJ', '14/08/1996', 'Compete à Justiça Federal processar e julgar crime de falso testemunho cometido no processo trabalhista.', SCON),
    'S200': _s('STJ', 'Súmula 200/STJ', '22/10/1997', 'O juízo federal competente para o crime de uso de passaporte falso é o do lugar onde o delito se consumou.', SCON),
    'S208': _s('STJ', 'Súmula 208/STJ', '27/05/1998', 'Compete à Justiça Federal processar e julgar prefeito municipal por desvio de verba sujeita a prestação de contas perante órgão federal.', SCON),
    'S209': _s('STJ', 'Súmula 209/STJ', '27/05/1998', 'Compete à Justiça Estadual processar e julgar prefeito por desvio de verba transferida e incorporada ao patrimônio municipal.', SCON),
    'S234': _s('STJ', 'Súmula 234/STJ', '13/12/1999', 'A participação de membro do Ministério Público na fase investigatória criminal não acarreta o seu impedimento ou suspeição para o oferecimento da denúncia.', SCON),
    'S273': _s('STJ', 'Súmula 273/STJ', '11/09/2002', 'Intimada a defesa da expedição da carta precatória, torna-se desnecessária intimação da data da audiência no juízo deprecado.', SCON),
    'S330': _s('STJ', 'Súmula 330/STJ', '13/09/2006', 'É desnecessária a resposta preliminar do art. 514 do CPP na ação penal instruída por inquérito policial.', SCON),
    'S337': _s('STJ', 'Súmula 337/STJ', '09/05/2007', 'É cabível a suspensão condicional do processo na desclassificação do crime e na procedência parcial da pretensão punitiva.', SCON),
    'S415': _s('STJ', 'Súmula 415/STJ', '09/12/2009', 'O período de suspensão do prazo prescricional é regulado pelo máximo da pena cominada.', SCON),
    'S444': _s('STJ', 'Súmula 444/STJ', '28/04/2010', 'É vedada a utilização de inquéritos policiais e ações penais em curso para agravar a pena-base.', SCON),
    'S455': _s('STJ', 'Súmula 455/STJ', '25/08/2010', 'A decisão que determina a produção antecipada de provas com base no art. 366 do CPP deve ser concretamente fundamentada, não a justificando unicamente o mero decurso do tempo.', SCON),
    'S536': _s('STJ', 'Súmula 536/STJ', '10/06/2015', 'A suspensão condicional do processo e a transação penal não se aplicam na hipótese de delitos sujeitos ao rito da Lei Maria da Penha.', SCON),
    'S542': _s('STJ', 'Súmula 542/STJ', '26/08/2015', 'A ação penal relativa ao crime de lesão corporal resultante de violência doméstica contra a mulher é pública incondicionada.', SCON),
    'S546': _s('STJ', 'Súmula 546/STJ', '14/10/2015', 'A competência para o crime de uso de documento falso é firmada pela entidade ou órgão a que foi apresentado o documento público, não importando a qualificação do órgão expedidor.', SCON),
    'S604': _s('STJ', 'Súmula 604/STJ', '28/02/2018', 'O mandado de segurança não se presta para atribuir efeito suspensivo a recurso criminal interposto pelo Ministério Público.', SCON),
    'S643': _s('STJ', 'Súmula 643/STJ', '10/02/2021', 'A execução da pena restritiva de direitos depende do trânsito em julgado da condenação.', SCON),
    'S648': _s('STJ', 'Súmula 648/STJ', '14/04/2021', 'A superveniência da sentença condenatória prejudica o pedido de trancamento da ação penal por falta de justa causa feito em habeas corpus.', SCON),
    'S676': _s('STJ', 'Súmula 676/STJ', '11/12/2024', 'Em razão da Lei n. 13.964/2019, não é mais possível ao juiz, de ofício, decretar ou converter prisão em flagrante em prisão preventiva.', SCON),
    'HC598886': _s('STJ', 'HC 598.886/SC, Sexta Turma (Informativo 684)', '27/10/2020', 'O procedimento do art. 226 do CPP não é mera recomendação: sua inobservância torna inválido o reconhecimento, que não pode lastrear condenação, mesmo se confirmado em juízo; o reconhecimento por foto na fase policial não serve como prova isolada.', INF),
    'RHC158580': _s('STJ', 'RHC 158.580/BA, Sexta Turma (Informativo 735)', '19/04/2022', 'A busca pessoal sem mandado exige fundada suspeita descrita com elementos objetivos; "atitude suspeita" vaga não basta, e o encontro posterior de objeto ilícito não convalida a revista ilegal.', INF),
    'HC877943': _s('STJ', 'HC 877.943/MS, Terceira Seção (Informativo 818)', '18/04/2024', 'A fuga repentina do réu ao avistar a guarnição policial pode configurar fundada suspeita para a busca pessoal em via pública, cabendo ao Estado o ônus de provar as circunstâncias, sob especial escrutínio.', INF),
    # ---------------- STF — súmulas
    'STF145': _s('STF', 'Súmula 145/STF', '13/12/1963', 'Não há crime, quando a preparação do flagrante pela polícia torna impossível a sua consumação.', STFPDF),
    'STF155': _s('STF', 'Súmula 155/STF', '13/12/1963', 'É relativa a nulidade do processo criminal por falta de intimação da expedição de precatória para inquirição de testemunha.', STFPDF),
    'STF156': _s('STF', 'Súmula 156/STF', '13/12/1963', 'É absoluta a nulidade do julgamento, pelo júri, por falta de quesito obrigatório.', STFPDF),
    'STF160': _s('STF', 'Súmula 160/STF', '13/12/1963', 'É nula a decisão do Tribunal que acolhe, contra o réu, nulidade não arguida no recurso da acusação, ressalvados os casos de recurso de ofício.', STFPDF),
    'STF208': _s('STF', 'Súmula 208/STF', '13/12/1963', 'O assistente do Ministério Público não pode recorrer, extraordinariamente, de decisão concessiva de habeas corpus.', STFPDF),
    'STF210': _s('STF', 'Súmula 210/STF', '13/12/1963', 'O assistente do Ministério Público pode recorrer, inclusive extraordinariamente, na ação penal, nos casos dos arts. 584, § 1º, e 598 do CPP.', STFPDF),
    'STF351': _s('STF', 'Súmula 351/STF', '13/12/1963', 'É nula a citação por edital de réu preso na mesma unidade da Federação em que o juiz exerce a sua jurisdição.', STFPDF),
    'STF366': _s('STF', 'Súmula 366/STF', '13/12/1963', 'Não é nula a citação por edital que indica o dispositivo da lei penal, embora não transcreva a denúncia ou queixa, ou não resuma os fatos em que se baseia.', STFPDF),
    'STF396': _s('STF', 'Súmula 396/STF', '03/04/1964', 'Para a ação penal por ofensa à honra, sendo admissível a exceção da verdade quanto ao desempenho de função pública, prevalece a competência especial por prerrogativa de função, ainda que já cessado o exercício funcional do ofendido.', STFPDF),
    'STF397': _s('STF', 'Súmula 397/STF', '03/04/1964', 'O poder de polícia da Câmara dos Deputados e do Senado, em caso de crime cometido nas suas dependências, compreende, consoante o regimento, a prisão em flagrante do acusado e a realização do inquérito.', STFPDF),
    'STF448': _s('STF', 'Súmula 448/STF', '01/10/1964', 'O prazo para o assistente recorrer, supletivamente, começa a correr imediatamente após o transcurso do prazo do Ministério Público.', STFPDF),
    'STF453': _s('STF', 'Súmula 453/STF', '01/10/1964', 'Não se aplicam à segunda instância o art. 384 e parágrafo único do CPP (nova definição jurídica por circunstância elementar não contida na denúncia ou queixa).', STFPDF),
    'STF523': _s('STF', 'Súmula 523/STF', '03/12/1969', 'No processo penal, a falta da defesa constitui nulidade absoluta, mas a sua deficiência só o anulará se houver prova de prejuízo para o réu.', STFPDF),
    'STF524': _s('STF', 'Súmula 524/STF', '03/12/1969', 'Arquivado o inquérito policial, por despacho do juiz, a requerimento do promotor de justiça, não pode a ação penal ser iniciada, sem novas provas.', STFPDF),
    'STF568': _s('STF', 'Súmula 568/STF', '15/12/1976', 'A identificação criminal não constitui constrangimento ilegal, ainda que o indiciado já tenha sido identificado civilmente.', STFPDF),
    'STF594': _s('STF', 'Súmula 594/STF', '15/12/1976', 'Os direitos de queixa e de representação podem ser exercidos, independentemente, pelo ofendido ou por seu representante legal.', STFPDF),
    'STF691': _s('STF', 'Súmula 691/STF', '24/09/2003', 'Não compete ao STF conhecer de habeas corpus contra decisão do relator que, em HC requerido a tribunal superior, indefere a liminar.', STFPDF),
    'STF693': _s('STF', 'Súmula 693/STF', '24/09/2003', 'Não cabe habeas corpus contra decisão condenatória a pena de multa, ou relativo a processo em curso por infração penal a que a pena pecuniária seja a única cominada.', STFPDF),
    'STF695': _s('STF', 'Súmula 695/STF', '24/09/2003', 'Não cabe habeas corpus quando já extinta a pena privativa de liberdade.', STFPDF),
    'STF701': _s('STF', 'Súmula 701/STF', '24/09/2003', 'No mandado de segurança impetrado pelo MP contra decisão proferida em processo penal, é obrigatória a citação do réu como litisconsorte passivo.', STFPDF),
    'STF702': _s('STF', 'Súmula 702/STF', '24/09/2003', 'A competência do Tribunal de Justiça para julgar prefeitos restringe-se aos crimes de competência da Justiça comum estadual; nos demais casos, cabe ao respectivo tribunal de segundo grau.', STFPDF),
    'STF704': _s('STF', 'Súmula 704/STF', '24/09/2003', 'Não viola as garantias do juiz natural, da ampla defesa e do devido processo legal a atração por continência ou conexão do processo do corréu ao foro por prerrogativa de função de um dos denunciados.', STFPDF),
    'STF705': _s('STF', 'Súmula 705/STF', '24/09/2003', 'A renúncia do réu ao direito de apelação, manifestada sem a assistência do defensor, não impede o conhecimento da apelação por este interposta.', STFPDF),
    'STF707': _s('STF', 'Súmula 707/STF', '24/09/2003', 'Constitui nulidade a falta de intimação do denunciado para oferecer contrarrazões ao recurso interposto da rejeição da denúncia, não a suprindo a nomeação de defensor dativo.', STFPDF),
    'STF708': _s('STF', 'Súmula 708/STF', '24/09/2003', 'É nulo o julgamento da apelação se, após a renúncia do único defensor, o réu não foi previamente intimado para constituir outro.', STFPDF),
    'STF709': _s('STF', 'Súmula 709/STF', '24/09/2003', 'Salvo quando nula a decisão de primeiro grau, o acórdão que provê o recurso contra a rejeição da denúncia vale, desde logo, pelo recebimento dela.', STFPDF),
    'STF710': _s('STF', 'Súmula 710/STF', '24/09/2003', 'No processo penal, contam-se os prazos da data da intimação, e não da juntada aos autos do mandado ou da carta precatória ou de ordem.', STFPDF),
    'STF712': _s('STF', 'Súmula 712/STF', '24/09/2003', 'É nula a decisão que determina o desaforamento de processo da competência do júri sem audiência da defesa.', STFPDF),
    'STF714': _s('STF', 'Súmula 714/STF', '24/09/2003', 'É concorrente a legitimidade do ofendido, mediante queixa, e do MP, condicionada à representação do ofendido, para a ação penal por crime contra a honra de servidor público em razão do exercício de suas funções.', STFPDF),
    # ---------------- STF — vinculantes
    'SV11': _s('STF', 'Súmula Vinculante 11 (publicada no DJe de 22/08/2008)', '22/08/2008', 'Só é lícito o uso de algemas em casos de resistência, fundado receio de fuga ou perigo à integridade física própria ou alheia, justificada a excepcionalidade por escrito, sob pena de responsabilidade e de nulidade da prisão ou do ato.', SV),
    'SV14': _s('STF', 'Súmula Vinculante 14 (publicada no DJe de 09/02/2009)', '09/02/2009', 'É direito do defensor, no interesse do representado, ter acesso amplo aos elementos de prova que, já documentados em procedimento investigatório de órgão com competência de polícia judiciária, digam respeito ao exercício do direito de defesa.', SV),
    'SV35': _s('STF', 'Súmula Vinculante 35 (publicada no DJe de 24/04/2014)', '24/04/2014', 'A homologação da transação penal do art. 76 da Lei 9.099/1995 não faz coisa julgada material; descumpridas as cláusulas, retoma-se a situação anterior, e o MP pode oferecer denúncia ou requisitar inquérito.', SV),
    'SV45': _s('STF', 'Súmula Vinculante 45 (publicada no DJe de 17/04/2015)', '17/04/2015', 'A competência constitucional do Tribunal do Júri prevalece sobre o foro por prerrogativa de função estabelecido exclusivamente pela Constituição Estadual.', SV),
    # ---------------- STF — controle concentrado, repercussão geral e HC
    'ADI6298': _s('STF', 'ADIs 6.298, 6.299, 6.300 e 6.305 (juiz das garantias)', '24/08/2023', 'Juiz das garantias de implantação obrigatória (12 meses, prorrogáveis por mais 12, da publicação da ata); sua competência cessa com o OFERECIMENTO da denúncia; não se aplica a processos originários do STF/STJ, ao júri, à violência doméstica e às infrações de menor potencial ofensivo; afastado o relaxamento automático da prisão por excesso de prazo; inconstitucional o impedimento do art. 157, § 5º.', STFNOT),
    'ADI6298ARQ': _s('STF', 'ADIs 6.298, 6.299, 6.300 e 6.305 — art. 28 do CPP', '24/08/2023', 'Ao requerer o arquivamento, o MP submete sua manifestação ao juiz competente e comunica a vítima, o investigado e a autoridade policial, podendo encaminhar os autos à instância de revisão ministerial para homologação; audiência de custódia por videoconferência admitida em caso de urgência.', STFNOT),
    'HC185913': _s('STF', 'HC 185.913/DF, Plenário', '18/09/2024', 'Cabe ANPP em processo em andamento quando a Lei 13.964/2019 entrou em vigor, mesmo sem confissão até então, desde que o pedido seja feito antes do trânsito em julgado; nas investigações e ações iniciadas após o julgamento, a proposta (ou a motivação da recusa) deve vir antes do recebimento da denúncia.', STFNOT),
    'RG280': _s('STF', 'Tema 280/RG — RE 603.616/RO', '05/11/2015', 'A entrada forçada em domicílio sem mandado só é lícita, mesmo à noite, quando amparada em fundadas razões, justificadas a posteriori, que indiquem flagrante delito dentro da casa, sob pena de responsabilidade do agente e nulidade dos atos.', 'portal.stf.jus.br — andamento do Tema 280'),
    'RG184': _s('STF', 'Tema 184/RG — RE 593.727/MG', '14/05/2015', 'O Ministério Público pode promover, por autoridade própria e por prazo razoável, investigações de natureza penal, respeitados os direitos do investigado, a reserva de jurisdição e as prerrogativas dos advogados, sob controle jurisdicional.', 'portal.stf.jus.br — andamento do Tema 184'),
    'ADPF444': _s('STF', 'ADPFs 395 e 444, Plenário', '14/06/2018', 'A condução coercitiva de investigado ou réu para interrogatório (art. 260 do CPP) não foi recepcionada pela Constituição; sem desconstituir interrogatórios já realizados.', STFNOT),
    'ADI5637': _s('STF', 'ADI 5.637/MG (Informativo 1.046)', '11/03/2022', 'O termo circunstanciado não tem natureza investigativa nem é atribuição privativa da polícia judiciária; é constitucional lei estadual que permite à polícia militar lavrá-lo.', STFNOT),
    'ADI3360': _s('STF', 'ADIs 3.360 e 4.109 (prisão temporária)', '11/02/2022', 'A temporária exige, cumulativamente: imprescindibilidade para o inquérito com base em elementos concretos (não para averiguação nem só pela falta de residência fixa); fundadas razões de autoria nos crimes do rol; fatos novos ou contemporâneos; adequação à gravidade concreta; insuficiência das cautelares dos arts. 319 e 320.', STFNOT),
}
