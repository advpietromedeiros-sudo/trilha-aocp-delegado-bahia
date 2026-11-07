# Base do Pente Fino de CPC: helper de itens e jurisprudência CONFERIDA em fonte oficial (07/11/2026).
ITENS = []


def I(ponto, rodada, tema, assertiva, gab, resumo, lei=(), juris=(), exc=None, regra=None, peg=None, kw=()):
    ITENS.append(dict(ponto=ponto, rodada=rodada, tema=tema, assertiva=assertiva, gabarito=gab, resumo=resumo,
                      lei=list(lei), juris=list(juris), excecoes=exc, regra=regra, pegadinha=peg,
                      palavras_chave=list(kw)))


# Jurisprudência: cada entrada conferida em 07/11/2026.
#  STJ súmulas: processo.stj.jus.br/SCON/sumstj (data = "julgado em").
#  STJ temas: processo.stj.jus.br/repetitivos (data = julgamento).
#  STF súmulas: PDF oficial "Enunciados_Sumulas_STF_1_a_736_Completo" (data = Sessão Plenária de aprovação).
#  STF Tema 1.075: notícia oficial STF de 09/04/2021 (sessão virtual finalizada em 7/4/2021).
#  STF ADI 4.296: Informativo STF 1.021 (julgamento em 9/6/2021).
def _s(trib, fonte, data, texto, conf):
    return dict(tribunal=trib, fonte=fonte, data=data, texto=texto, _conferido=conf)


SCON = 'processo.stj.jus.br/SCON/sumstj'
REP = 'processo.stj.jus.br/repetitivos'
STFPDF = 'stf.jus.br — Enunciados das Súmulas do STF 1 a 736 (PDF oficial)'
J = {
    'S1': _s('STJ', 'Súmula 1/STJ', '25/04/1990', 'Na investigação de paternidade cumulada com alimentos, o foro competente é o do domicílio ou da residência do alimentando.', SCON),
    'S7': _s('STJ', 'Súmula 7/STJ', '28/06/1990', 'A pretensão de simples reexame de prova não enseja recurso especial.', SCON),
    'S33': _s('STJ', 'Súmula 33/STJ', '24/10/1991', 'A incompetência relativa não pode ser declarada de ofício.', SCON),
    'S99': _s('STJ', 'Súmula 99/STJ', '14/04/1994', 'O MP tem legitimidade para recorrer no processo em que oficiou como fiscal da lei, ainda que não haja recurso da parte.', SCON),
    'S105': _s('STJ', 'Súmula 105/STJ', '26/05/1994', 'Na ação de mandado de segurança não se admite condenação em honorários advocatícios.', SCON),
    'S106': _s('STJ', 'Súmula 106/STJ', '26/05/1994', 'Proposta a ação no prazo, a demora na citação por motivos inerentes ao mecanismo da Justiça não justifica o acolhimento da prescrição ou da decadência.', SCON),
    'S150': _s('STJ', 'Súmula 150/STJ', '07/02/1996', 'Compete à Justiça Federal decidir sobre a existência de interesse jurídico que justifique a presença da União, suas autarquias ou empresas públicas.', SCON),
    'S196': _s('STJ', 'Súmula 196/STJ', '01/10/1997', 'Ao executado citado por edital ou por hora certa que permanecer revel será nomeado curador especial, com legitimidade para apresentar embargos.', SCON),
    'S203': _s('STJ', 'Súmula 203/STJ (redação alterada em 23/05/2002)', '23/05/2002', 'Não cabe recurso especial contra decisão proferida por órgão de segundo grau dos Juizados Especiais.', SCON),
    'S206': _s('STJ', 'Súmula 206/STJ', '01/04/1998', 'A existência de vara privativa, instituída por lei estadual, não altera a competência territorial resultante das leis de processo.', SCON),
    'S211': _s('STJ', 'Súmula 211/STJ', '01/07/1998', 'Inadmissível REsp quanto à questão que, a despeito dos embargos declaratórios, não foi apreciada pelo tribunal a quo.', SCON),
    'S213': _s('STJ', 'Súmula 213/STJ', '23/09/1998', 'O mandado de segurança constitui ação adequada para a declaração do direito à compensação tributária.', SCON),
    'S235': _s('STJ', 'Súmula 235/STJ', '01/02/2000', 'A conexão não determina a reunião dos processos, se um deles já foi julgado.', SCON),
    'S240': _s('STJ', 'Súmula 240/STJ', '02/08/2000', 'A extinção do processo, por abandono da causa pelo autor, depende de requerimento do réu.', SCON),
    'S329': _s('STJ', 'Súmula 329/STJ', '02/08/2006', 'O Ministério Público tem legitimidade para propor ação civil pública em defesa do patrimônio público.', SCON),
    'S333': _s('STJ', 'Súmula 333/STJ', '13/12/2006', 'Cabe mandado de segurança contra ato praticado em licitação promovida por sociedade de economia mista ou empresa pública.', SCON),
    'S375': _s('STJ', 'Súmula 375/STJ', '18/03/2009', 'O reconhecimento da fraude à execução depende do registro da penhora do bem alienado ou da prova de má-fé do terceiro adquirente.', SCON),
    'S376': _s('STJ', 'Súmula 376/STJ', '18/03/2009', 'Compete à turma recursal processar e julgar o mandado de segurança contra ato de juizado especial.', SCON),
    'S393': _s('STJ', 'Súmula 393/STJ', '23/09/2009', 'A exceção de pré-executividade é admissível na execução fiscal relativamente às matérias conhecíveis de ofício que não demandem dilação probatória.', SCON),
    'S410': _s('STJ', 'Súmula 410/STJ', '25/11/2009', 'A prévia intimação pessoal do devedor é condição necessária para a cobrança de multa pelo descumprimento de obrigação de fazer ou não fazer.', SCON),
    'S460': _s('STJ', 'Súmula 460/STJ', '25/08/2010', 'É incabível o mandado de segurança para convalidar a compensação tributária realizada pelo contribuinte.', SCON),
    'S489': _s('STJ', 'Súmula 489/STJ', '28/06/2012', 'Reconhecida a continência, devem ser reunidas na Justiça Federal as ações civis públicas propostas nesta e na Justiça estadual.', SCON),
    'S579': _s('STJ', 'Súmula 579/STJ', '01/07/2016', 'Não é necessário ratificar o REsp interposto na pendência dos embargos de declaração quando inalterado o resultado anterior.', SCON),
    'S601': _s('STJ', 'Súmula 601/STJ', '07/02/2018', 'O MP tem legitimidade ativa para a defesa de direitos difusos, coletivos e individuais homogêneos dos consumidores, ainda que decorrentes da prestação de serviço público.', SCON),
    'S628': _s('STJ', 'Súmula 628/STJ', '12/12/2018', 'A teoria da encampação aplica-se ao MS quando presentes, cumulativamente: vínculo hierárquico, manifestação sobre o mérito nas informações e ausência de modificação de competência constitucional.', SCON),
    'T988': _s('STJ', 'Tema 988/STJ — REsp 1.704.520/MT e REsp 1.696.396/MT', '05/12/2018', 'O rol do art. 1.015 do CPC é de taxatividade mitigada: admite agravo de instrumento quando verificada urgência decorrente da inutilidade do julgamento da questão na apelação.', REP),
    'T1076': _s('STJ', 'Tema 1.076/STJ — REsp 1.850.512/SP e outros', '16/03/2022', 'A fixação de honorários por equidade não é permitida quando forem elevados a condenação, o proveito econômico ou o valor da causa; só cabe se o proveito for inestimável ou irrisório, ou o valor da causa muito baixo.', REP),
    'T1137': _s('STJ', 'Tema 1.137/STJ — REsp 1.955.539/SP e REsp 1.955.574/SP', '04/12/2025', 'Meios executivos atípicos cabem desde que, cumulativamente: ponderadas efetividade e menor onerosidade; uso prioritariamente subsidiário; fundamentação adequada; contraditório, proporcionalidade e razoabilidade, inclusive quanto à duração.', REP),
    'T1267': _s('STJ', 'Tema 1.267/STJ — REsp 2.072.867/MA e outros', '19/03/2025', 'O juiz de 1º grau que obsta o processamento da apelação viola o art. 1.010, § 3º, e usurpa a competência do tribunal: cabe reclamação (art. 988, I); em execução ou cumprimento de sentença, cabe também agravo de instrumento.', REP),
    'T1296': _s('STJ', 'Tema 1.296/STJ — REsp 2.096.505/SP e outros', '04/03/2026', 'A prévia intimação pessoal do devedor para cumprir obrigação de fazer ou não fazer é pressuposto da multa coercitiva; a Súmula 410 permanece hígida após o CPC/2015.', REP),
    'T1338': _s('STJ', 'Tema 1.338/STJ — REsp 2.166.983/AP e REsp 2.162.483/AP', '18/03/2026', 'Ofícios a cadastros públicos ou concessionárias não são requisito obrigatório da citação por edital; basta, em regra, a frustração das tentativas nos endereços dos autos e nos sistemas informatizados do juízo.', REP),
    'STF101': _s('STF', 'Súmula 101/STF', '13/12/1963', 'O mandado de segurança não substitui a ação popular.', STFPDF),
    'STF266': _s('STF', 'Súmula 266/STF', '13/12/1963', 'Não cabe mandado de segurança contra lei em tese.', STFPDF),
    'STF267': _s('STF', 'Súmula 267/STF', '13/12/1963', 'Não cabe mandado de segurança contra ato judicial passível de recurso ou correição.', STFPDF),
    'STF268': _s('STF', 'Súmula 268/STF', '13/12/1963', 'Não cabe mandado de segurança contra decisão judicial com trânsito em julgado.', STFPDF),
    'STF269': _s('STF', 'Súmula 269/STF', '13/12/1963', 'O mandado de segurança não é substitutivo de ação de cobrança.', STFPDF),
    'STF271': _s('STF', 'Súmula 271/STF', '13/12/1963', 'A concessão de MS não produz efeitos patrimoniais quanto a período pretérito, que devem ser reclamados administrativamente ou pela via judicial própria.', STFPDF),
    'STF343': _s('STF', 'Súmula 343/STF', '13/12/1963', 'Não cabe ação rescisória por ofensa a literal disposição de lei quando a decisão rescindenda se baseou em texto de interpretação controvertida nos tribunais.', STFPDF),
    'STF365': _s('STF', 'Súmula 365/STF', '13/12/1963', 'Pessoa jurídica não tem legitimidade para propor ação popular.', STFPDF),
    'STF512': _s('STF', 'Súmula 512/STF', '03/12/1969', 'Não cabe condenação em honorários de advogado na ação de mandado de segurança.', STFPDF),
    'STF625': _s('STF', 'Súmula 625/STF', '24/09/2003', 'Controvérsia sobre matéria de direito não impede concessão de mandado de segurança.', STFPDF),
    'STF629': _s('STF', 'Súmula 629/STF', '24/09/2003', 'A impetração de MS coletivo por entidade de classe em favor dos associados independe da autorização destes.', STFPDF),
    'STF630': _s('STF', 'Súmula 630/STF', '24/09/2003', 'A entidade de classe tem legitimação para o MS ainda quando a pretensão interesse apenas a uma parte da categoria.', STFPDF),
    'STF632': _s('STF', 'Súmula 632/STF', '24/09/2003', 'É constitucional lei que fixa o prazo de decadência para a impetração de mandado de segurança.', STFPDF),
    'STF640': _s('STF', 'Súmula 640/STF', '24/09/2003', 'É cabível RE contra decisão de juiz de 1º grau nas causas de alçada, ou de turma recursal de juizado especial cível e criminal.', STFPDF),
    'STF734': _s('STF', 'Súmula 734/STF', '26/11/2003', 'Não cabe reclamação quando já houver transitado em julgado o ato judicial que se alega ter desrespeitado decisão do STF.', STFPDF),
    'STF735': _s('STF', 'Súmula 735/STF', '26/11/2003', 'Não cabe recurso extraordinário contra acórdão que defere medida liminar.', STFPDF),
    'RG1075': _s('STF', 'Tema 1.075/RG — RE 1.101.937 (sessão virtual finalizada em 7/4/2021)', '07/04/2021', 'É inconstitucional a redação do art. 16 da Lei 7.347/1985 dada pela Lei 9.494/1997 (limite territorial da coisa julgada); ACP de efeito nacional ou regional segue o art. 93, II, do CDC, com prevenção do juízo que primeiro conheceu.', 'portal.stf.jus.br — notícia de 09/04/2021 e andamento do Tema 1.075'),
    'ADI4296': _s('STF', 'ADI 4.296/DF (Informativo STF 1.021)', '09/06/2021', 'São inconstitucionais o art. 7º, § 2º (vedações de liminar em MS) e o art. 22, § 2º (oitiva prévia do ente público para liminar em MS coletivo) da Lei 12.016/2009; mantidos a caução do art. 7º, III, e o prazo de 120 dias do art. 23.', 'stf.jus.br — Informativo 1.021 e notícia oficial'),
}
