# Pente Fino de Legislação Penal Extravagante — LPE-31 (Lei Geral do Esporte), LPE-32 (crimes falimentares), LPE-33
# (biossegurança), LPE-34 (Decreto-Lei 201/1967), LPE-35 (crimes contra a pessoa com deficiência), LPE-36
# (terrorismo), LPE-37 (Lei 14.344/2022), LPE-38 (Lei 13.431/2017 e Decreto 9.603/2018), LPE-39 (Lei 15.358/2026,
# marco legal do combate ao crime organizado) e LPE-40 (jurisprudência aplicada, como ponto de FECHAMENTO, toda
# conferida em fonte oficial — lpe_juris.py) (08/11/2026).
from base import I
from lpe_juris import J

ES = 'L14597:'
FA = 'L11101:'
BI = 'L11105:'
PR = 'DL201:'
PD = 'L13146:'
TE = 'L13260:'
HB = 'L14344:'
EE = 'L13431:'
DE = 'D9603:'
MO = 'L15358:'

# ======================= LPE-31 · Lei Geral do Esporte =======================
P = 'DBA26-LPE-31'
I(P, 1, 'Cambismo',
  'Vender ou portar para venda ingressos de evento esportivo por preço superior ao estampado no bilhete é crime punido com reclusão, de 1 a 2 anos, e multa.', 'C',
  'Lei 14.597/2023, art. 166 — o **cambismo** é crime.',
  lei=[(ES + '166', 'Vender ou portar para venda ingressos de evento esportivo, por preço superior ao estampado no bilhete:', None, 'Lei 14.597/2023, art. 166'), (ES + '166', 'Pena - reclusão, de 1 (um) a 2 (dois) anos, e multa.', None, 'Lei 14.597/2023, art. 166, pena')],
  kw=['cambismo', 'ingressos'])
I(P, 1, 'Corrupção esportiva ativa',
  'Dar ou prometer vantagem com o fim de alterar o resultado de competição esportiva é punido com detenção, de 6 meses a 2 anos.', 'E',
  'Art. 199: **reclusão, de 2 a 6 anos**, e multa — a mesma pena da forma passiva (art. 198) e da fraude ao resultado (art. 200).',
  lei=[(ES + '199', 'Pena - reclusão, de 2 (dois) a 6 (seis) anos, e multa.', None, 'Lei 14.597/2023, art. 199, pena')],
  peg='Rebaixar a pena da manipulação de resultado.', kw=['alterar ou falsear o resultado', 'reclusão'])
I(P, 1, 'Tumulto fora do estádio',
  'Responde pelo crime de promover tumulto o torcedor que pratica violência em um raio de 1.000 metros ao redor do local do evento esportivo.', 'E',
  'Art. 201, § 1º, I: o raio é de **5.000 metros**, e também alcança o trajeto de ida e volta.',
  lei=[(ES + '201', 'em um raio de 5.000 m (cinco mil metros) ao redor do local de realização do evento esportivo', None, 'Lei 14.597/2023, art. 201, § 1º, I')],
  peg='Encolher o raio.', kw=['5.000 m', 'tumulto'])
I(P, 1, 'Racismo e violência contra a mulher no esporte',
  'As penas do crime de tumulto e violência em eventos esportivos são aplicadas em dobro nos casos de racismo no esporte ou de infrações cometidas contra as mulheres.', 'C',
  'Art. 201, § 7º.',
  lei=[(ES + '201', 'serão aplicadas em dobro quando se tratar de casos de racismo no esporte brasileiro ou de infrações cometidas contra as mulheres', None, 'Lei 14.597/2023, art. 201, § 7º')],
  kw=['em dobro', 'racismo no esporte'])
I(P, 1, 'Corrupção privada no esporte',
  'O crime de exigir ou receber vantagem indevida para realizar ou omitir ato no âmbito do esporte só pode ser praticado por funcionário público.', 'E',
  'Art. 165: o sujeito ativo é o **representante de organização esportiva privada** — é uma **corrupção privada**; quem oferece ou paga responde nas mesmas penas (par. ún.).',
  lei=[(ES + '165', 'como representante de organização esportiva privada', None, 'Lei 14.597/2023, art. 165')],
  peg='Exigir funcionário público.', kw=['corrupção privada', 'organização esportiva privada'])
# --- LPE-31 · Rodada 2
I(P, 2, 'Pena impeditiva',
  'Na condenação por tumulto em evento esportivo, o juiz deverá converter a pena de reclusão em pena impeditiva de comparecimento às proximidades da arena esportiva, de 3 meses a 3 anos.', 'C',
  'Art. 201, § 2º; o descumprimento injustificado reconverte em privativa (§ 3º).',
  lei=[(ES + '201', 'o juiz deverá converter a pena de reclusão em pena impeditiva de comparecimento às proximidades da arena esportiva', None, 'Lei 14.597/2023, art. 201, § 2º')],
  kw=['pena impeditiva de comparecimento'])
I(P, 2, 'Desvio de ingressos',
  'Fornecer, desviar ou facilitar a distribuição de ingressos para venda por preço superior ao estampado no bilhete é punido com reclusão, de 2 a 4 anos, e multa.', 'C',
  'Art. 167 — pena maior que a do cambista (art. 166).',
  lei=[(ES + '167', 'Fornecer, desviar ou facilitar a distribuição de ingressos para venda por preço superior ao estampado no bilhete:', None, 'Lei 14.597/2023, art. 167'), (ES + '167', 'Pena - reclusão, de 2 (dois) a 4 (quatro) anos, e multa.', None, 'Lei 14.597/2023, art. 167, pena')],
  kw=['desviar', 'ingressos'])
I(P, 2, 'Quem organiza o tumulto',
  'A pena do crime de tumulto é aplicada em dobro para quem organiza ou prepara o tumulto ou incita a sua prática.', 'E',
  'Art. 201, § 6º: aumento de **1/3 até a metade**, sem as medidas substitutivas; o "em dobro" é o do § 7º (racismo e violência contra a mulher).',
  lei=[(ES + '201', 'será aumentada de 1/3 (um terço) até a metade para aquele que organiza ou prepara o tumulto ou incita a sua prática', None, 'Lei 14.597/2023, art. 201, § 6º')],
  peg='Trocar os §§ 6º e 7º.', kw=['organiza ou prepara o tumulto'])

# ======================= LPE-32 · Crimes falimentares =======================
P = 'DBA26-LPE-32'
I(P, 1, 'Condição objetiva de punibilidade',
  'A sentença que decreta a falência, concede a recuperação judicial ou concede a recuperação extrajudicial é condição objetiva de punibilidade dos crimes da Lei 11.101/2005.', 'C',
  'Art. 180.',
  lei=[(FA + '180', 'é condição objetiva de punibilidade das infrações penais descritas nesta Lei', None, 'Lei 11.101/2005, art. 180')],
  kw=['condição objetiva de punibilidade'])
I(P, 1, 'Ação penal',
  'Os crimes falimentares são de ação penal privada, cabendo a iniciativa ao credor prejudicado ou ao administrador judicial.', 'E',
  'Art. 184: **pública incondicionada**; credor habilitado ou administrador judicial só podem oferecer a **subsidiária**, se o MP não agir no prazo (par. ún.).',
  lei=[(FA + '184', 'Os crimes previstos nesta Lei são de ação penal pública incondicionada.', None, 'Lei 11.101/2005, art. 184')],
  peg='Privatizar a ação.', kw=['pública incondicionada', 'subsidiária'])
I(P, 1, 'Competência',
  'Compete ao juiz criminal da jurisdição onde tenha sido decretada a falência ou concedida a recuperação judicial conhecer da ação penal pelos crimes falimentares.', 'C',
  'Art. 183 — não é o juízo universal da falência.',
  lei=[(FA + '183', 'Compete ao juiz criminal da jurisdição onde tenha sido decretada a falência', None, 'Lei 11.101/2005, art. 183')],
  kw=['juiz criminal'])
I(P, 1, 'Efeitos da condenação',
  'A inabilitação para o exercício de atividade empresarial é efeito automático da condenação por crime falimentar e perdura por 10 anos.', 'E',
  'Art. 181, § 1º: os efeitos **não são automáticos**, devem ser declarados motivadamente e perduram **até 5 anos** após a extinção da punibilidade.',
  lei=[(FA + '181', 'Os efeitos de que trata este artigo não são automáticos, devendo ser motivadamente declarados na sentença, e perdurarão até 5 (cinco) anos após a extinção da punibilidade', None, 'Lei 11.101/2005, art. 181, § 1º')],
  peg='Tornar automático e alongar o prazo.', kw=['não são automáticos', '5 (cinco) anos'])
I(P, 1, 'Fraude a credores',
  'A fraude a credores, crime mais grave da Lei 11.101/2005, é punida com detenção, de 1 a 2 anos.', 'E',
  'Art. 168: **reclusão, de 3 a 6 anos**, e multa, com aumentos de 1/6 a 1/3 (contabilidade falsa) e de 1/3 até metade (caixa dois).',
  lei=[(FA + '168', 'Pena – reclusão, de 3 (três) a 6 (seis) anos, e multa.', None, 'Lei 11.101/2005, art. 168, pena')],
  peg='Rebaixar a pena.', kw=['fraude a credores', 'reclusão'])
# --- LPE-32 · Rodada 2
I(P, 2, 'Início da prescrição',
  'A prescrição dos crimes falimentares começa a correr do dia da decretação da falência, da concessão da recuperação judicial ou da homologação do plano de recuperação extrajudicial.', 'C',
  'Art. 182; a decretação da falência interrompe a prescrição iniciada com a recuperação (par. ún.).',
  lei=[(FA + '182', 'começando a correr do dia da decretação da falência', None, 'Lei 11.101/2005, art. 182')],
  kw=['prescrição', 'decretação da falência'])
I(P, 2, 'Contador',
  'Nas penas da fraude a credores incidem os contadores, técnicos contábeis, auditores e outros profissionais que concorrerem para as condutas, na medida de sua culpabilidade.', 'C',
  'Art. 168, § 3º.',
  lei=[(FA + '168', 'Nas mesmas penas incidem os contadores, técnicos contábeis, auditores e outros profissionais', None, 'Lei 11.101/2005, art. 168, § 3º')],
  kw=['contadores', 'concurso de pessoas'])
I(P, 2, 'Omissão de documentos contábeis',
  'Deixar de elaborar ou escriturar os documentos contábeis obrigatórios é punido com reclusão, de 3 a 6 anos.', 'E',
  'Art. 178: **detenção, de 1 a 2 anos**, e multa, se o fato não constitui crime mais grave (é infração de menor potencial ofensivo).',
  lei=[(FA + '178', 'Pena – detenção, de 1 (um) a 2 (dois) anos, e multa, se o fato não constitui crime mais grave.', None, 'Lei 11.101/2005, art. 178, pena')],
  peg='Usar a pena do art. 168.', kw=['detenção, de 1 (um) a 2 (dois) anos'])

# ======================= LPE-33 · Biossegurança =======================
P = 'DBA26-LPE-33'
I(P, 1, 'Clonagem humana',
  'Realizar clonagem humana é crime punido com reclusão, de 2 a 5 anos, e multa.', 'C',
  'Lei 11.105/2005, art. 26 — **clonagem humana** é crime, sem exceção.',
  lei=[(BI + '26', 'Realizar clonagem humana:', None, 'Lei 11.105/2005, art. 26'), (BI + '26', 'Pena – reclusão, de 2 (dois) a 5 (cinco) anos, e multa.', None, 'Lei 11.105/2005, art. 26, pena')],
  kw=['clonagem humana'])
I(P, 1, 'Engenharia genética em embrião',
  'A engenharia genética em embrião humano é permitida para fins de pesquisa, desde que aprovada por comitê de ética.', 'E',
  'Art. 25: **praticar engenharia genética** em célula germinal humana, zigoto ou embrião humano é **crime** (reclusão, de 1 a 4 anos). A pesquisa com células-tronco embrionárias segue as condições do art. 5º.',
  lei=[(BI + '25', 'Praticar engenharia genética em célula germinal humana, zigoto humano ou embrião humano:', None, 'Lei 11.105/2005, art. 25')],
  peg='Liberar a engenharia genética.', kw=['engenharia genética', 'embrião humano'])
I(P, 1, 'Uso de embrião',
  'Utilizar embrião humano em desacordo com as condições legais de pesquisa é crime punido com detenção, de 1 a 3 anos, e multa.', 'C',
  'Art. 24 (remete ao art. 5º: embriões inviáveis ou congelados há 3 anos ou mais, com consentimento dos genitores).',
  lei=[(BI + '24', 'Utilizar embrião humano em desacordo com o que dispõe o art. 5º desta Lei:', None, 'Lei 11.105/2005, art. 24')],
  kw=['embrião humano', 'detenção'])
I(P, 1, 'OGM com morte',
  'Se da liberação de OGM no meio ambiente resulta a morte de outrem, a pena é agravada da metade.', 'E',
  'Art. 27, § 2º, IV: **de 2/3 até o dobro**; a de metade até 2/3 é a da lesão grave (III).',
  lei=[(BI + '27', 'IV – de 2/3 (dois terços) até o dobro, se resultar a morte de outrem.', None, 'Lei 11.105/2005, art. 27, § 2º, IV')],
  peg='Trocar a fração.', kw=['OGM', 'até o dobro'])
I(P, 1, 'Comércio de OGM',
  'Comercializar OGM sem autorização ou em desacordo com as normas da CTNBio é mera infração administrativa.', 'E',
  'Art. 29: é **crime** (reclusão, de 1 a 2 anos, e multa).',
  lei=[(BI + '29', 'Produzir, armazenar, transportar, comercializar, importar ou exportar OGM ou seus derivados, sem autorização', None, 'Lei 11.105/2005, art. 29')],
  peg='Negar a tipicidade.', kw=['OGM', 'CTNBio'])
# --- LPE-33 · Rodada 2
I(P, 2, 'Tecnologias de restrição de uso',
  'Utilizar, comercializar, registrar, patentear e licenciar tecnologias genéticas de restrição do uso é crime punido com reclusão, de 2 a 5 anos, e multa.', 'C',
  'Art. 28 (as chamadas sementes "terminator").',
  lei=[(BI + '28', 'Utilizar, comercializar, registrar, patentear e licenciar tecnologias genéticas de restrição do uso:', None, 'Lei 11.105/2005, art. 28')],
  kw=['tecnologias genéticas de restrição do uso'])
I(P, 2, 'Liberação de OGM',
  'Liberar ou descartar OGM no meio ambiente em desacordo com as normas da CTNBio é punido com detenção, de 6 meses a 1 ano.', 'E',
  'Art. 27: **reclusão, de 1 a 4 anos**, e multa.',
  lei=[(BI + '27', 'Liberar ou descartar OGM no meio ambiente, em desacordo com as normas estabelecidas pela CTNBio', None, 'Lei 11.105/2005, art. 27')],
  kw=['liberar ou descartar OGM'])
I(P, 2, 'OGM com dano ambiental',
  'Se da liberação de OGM resultar dano ao meio ambiente, a pena é agravada de 1/6 a 1/3.', 'E',
  'Art. 27, § 2º, II: **de 1/3 até a metade**; de 1/6 a 1/3 é o dano à propriedade alheia (I).',
  lei=[(BI + '27', 'II – de 1/3 (um terço) até a metade, se resultar dano ao meio ambiente;', None, 'Lei 11.105/2005, art. 27, § 2º, II')],
  peg='Trocar as frações.', kw=['dano ao meio ambiente'])

# ======================= LPE-34 · Decreto-Lei 201/1967 =======================
P = 'DBA26-LPE-34'
I(P, 1, 'Julgamento pelo Judiciário',
  'Os crimes de responsabilidade do art. 1º do Decreto-Lei 201/1967 são julgados pelo Poder Judiciário, independentemente do pronunciamento da Câmara de Vereadores.', 'C',
  'Art. 1º, caput: apesar do nome, são **crimes comuns** (as infrações político-administrativas do art. 4º é que vão à Câmara).',
  lei=[(PR + '1', 'sujeitos ao julgamento do Poder Judiciário, independentemente do pronunciamento da Câmara dos Vereadores', None, 'DL 201/1967, art. 1º')],
  kw=['Poder Judiciário', 'Câmara dos Vereadores'])
I(P, 1, 'Penas',
  'Os crimes do Decreto-Lei 201/1967 são de ação pública; apropriar-se de bens ou rendas públicas ou utilizá-los indevidamente é punido com reclusão de dois a doze anos, e os demais com detenção de três meses a três anos.', 'C',
  'Art. 1º, § 1º.',
  lei=[(PR + '1', 'punidos os dos itens I e II, com a pena de reclusão, de dois a doze anos, e os demais, com a pena de detenção, de três meses a três anos', None, 'DL 201/1967, art. 1º, § 1º')],
  kw=['dois a doze anos', 'ação pública'])
I(P, 1, 'Inabilitação',
  'A condenação definitiva por crime do Decreto-Lei 201/1967 acarreta a perda do cargo e a inabilitação, por 8 anos, para cargo ou função pública.', 'E',
  'Art. 1º, § 2º: inabilitação pelo prazo de **cinco anos**.',
  lei=[(PR + '1', 'acarreta a perda de cargo e a inabilitação, pelo prazo de cinco anos', None, 'DL 201/1967, art. 1º, § 2º')],
  peg='Trocar 5 por 8 anos.', kw=['inabilitação', 'cinco anos'])
I(P, 1, 'Fim do mandato',
  'Extinto o mandato do prefeito, não pode mais ser instaurado processo pelos crimes do art. 1º do Decreto-Lei 201/1967.', 'E',
  '**Súmula 703/STF** e **Súmula 164/STJ**: a extinção do mandato **não impede** a instauração nem o prosseguimento do processo.',
  juris=[J['STF703'], J['S164']], peg='Extinguir a persecução com o mandato.', kw=['Súmula 703/STF', 'Súmula 164/STJ'])
I(P, 1, 'Defesa prévia',
  'No processo por crime do Decreto-Lei 201/1967, antes de receber a denúncia, o juiz notifica o acusado para apresentar defesa prévia em 15 dias.', 'E',
  'Art. 2º, I: prazo de **cinco dias**.',
  lei=[(PR + '2', 'Antes de receber a denúncia, o Juiz ordenará a notificação do acusado para apresentar defesa prévia, no prazo de cinco dias.', None, 'DL 201/1967, art. 2º, I')],
  peg='Trocar o prazo.', kw=['defesa prévia', 'cinco dias'])
I(P, 1, 'Verba federal incorporada',
  'Compete sempre à Justiça Federal julgar prefeito por desvio de verba federal, ainda que transferida e incorporada ao patrimônio municipal.', 'E',
  '**Súmulas 208 e 209/STJ**: é federal se a verba está **sujeita a prestação de contas perante órgão federal**; incorporada ao patrimônio municipal, é **estadual**.',
  juris=[J['S208'], J['S209']], peg='Ignorar a incorporação.', kw=['Súmula 209/STJ', 'incorporada'])
# --- LPE-34 · Rodada 2
I(P, 2, 'Preventiva e afastamento',
  'Ao receber a denúncia, o juiz manifesta-se, obrigatória e motivadamente, sobre a prisão preventiva do prefeito, nos casos dos incisos I e II do art. 1º, e sobre seu afastamento do cargo durante a instrução.', 'C',
  'Art. 2º, II.',
  lei=[(PR + '2', 'Ao receber a denúncia, o Juiz manifestar-se-á, obrigatória e motivadamente, sobre a prisão preventiva do acusado', None, 'DL 201/1967, art. 2º, II')],
  kw=['afastamento do exercício do cargo', 'prisão preventiva'])
I(P, 2, 'Recurso',
  'Do despacho que concede ou nega a prisão preventiva ou o afastamento do prefeito cabe recurso em sentido estrito, em cinco dias, em autos apartados.', 'C',
  'Art. 2º, III.',
  lei=[(PR + '2', 'caberá recurso, em sentido estrito, para o Tribunal competente, no prazo de cinco dias, em autos apartados', None, 'DL 201/1967, art. 2º, III')],
  kw=['recurso, em sentido estrito'])
I(P, 2, 'Foro do prefeito',
  'O Tribunal de Justiça é competente para julgar o prefeito por qualquer crime, inclusive federal ou eleitoral.', 'E',
  '**Súmula 702/STF**: a competência do TJ restringe-se aos crimes da **Justiça comum estadual**; nos demais, cabe ao tribunal de segundo grau respectivo (TRF ou TRE).',
  juris=[J['STF702']], peg='Universalizar o foro no TJ.', kw=['Súmula 702/STF'])

# ======================= LPE-35 · Crimes contra a pessoa com deficiência =======================
P = 'DBA26-LPE-35'
I(P, 1, 'Discriminação',
  'Praticar, induzir ou incitar discriminação de pessoa em razão de sua deficiência é crime punido com reclusão, de 1 a 3 anos, e multa.', 'C',
  'Lei 13.146/2015, art. 88 — **discriminação** em razão da deficiência.',
  lei=[(PD + '88', 'Praticar, induzir ou incitar discriminação de pessoa em razão de sua deficiência:', None, 'Lei 13.146/2015, art. 88')],
  kw=['discriminação', 'deficiência'])
I(P, 1, 'Meios de comunicação',
  'Se a discriminação de pessoa com deficiência é cometida por meio de comunicação social ou de publicação de qualquer natureza, a pena é de reclusão, de 2 a 5 anos, e multa.', 'C',
  'Art. 88, § 2º; o juiz pode determinar o recolhimento do material ainda antes do inquérito (§ 3º).',
  lei=[(PD + '88', 'é cometido por intermédio de meios de comunicação social ou de publicação de qualquer natureza', None, 'Lei 13.146/2015, art. 88, § 2º')],
  kw=['meios de comunicação social'])
I(P, 1, 'Apropriação pelo curador',
  'Na apropriação de proventos de pessoa com deficiência, a pena aumenta de metade se o crime é cometido por tutor ou curador.', 'E',
  'Art. 89, par. ún., I: aumento de **1/3**.',
  lei=[(PD + '89', 'Aumenta-se a pena em 1/3 (um terço) se o crime é cometido:', None, 'Lei 13.146/2015, art. 89, par. ún.')],
  peg='Trocar a fração.', kw=['tutor, curador', '1/3 (um terço)'])
I(P, 1, 'Abandono',
  'Abandonar pessoa com deficiência em hospital ou entidade de abrigamento é punido com reclusão, de 6 meses a 3 anos.', 'E',
  'Art. 90 (redação da **Lei 15.163/2025**): **reclusão, de 2 a 5 anos**, e multa; a pena de 6 meses a 3 anos é a redação anterior.',
  lei=[(PD + '90', 'Pena - reclusão, de 2 (dois) a 5 (cinco) anos, e multa.', None, 'Lei 13.146/2015, art. 90, pena')],
  peg='Citar a pena revogada.', kw=['abandono', 'Lei 15.163/2025'])
I(P, 1, 'Cartão magnético',
  'Reter o cartão de benefício da pessoa com deficiência é atípico quando praticado por familiar que administra seus recursos.', 'E',
  'Art. 91: é crime reter ou utilizar o cartão ou documento (detenção, de 6 meses a 2 anos), e a pena **aumenta de 1/3** se o autor é tutor ou curador.',
  lei=[(PD + '91', 'Reter ou utilizar cartão magnético, qualquer meio eletrônico ou documento de pessoa com deficiência', None, 'Lei 13.146/2015, art. 91')],
  peg='Criar excludente familiar.', kw=['cartão magnético'])
# --- LPE-35 · Rodada 2
I(P, 2, 'Abandono com morte',
  'Se do abandono de pessoa com deficiência resulta morte, a pena é de reclusão, de 8 a 14 anos, e multa.', 'C',
  'Art. 90, § 2º (Lei 15.163/2025).',
  lei=[(PD + '90', 'Pena - reclusão, de 8 (oito) a 14 (quatorze) anos, e multa.', None, 'Lei 13.146/2015, art. 90, § 2º')],
  kw=['resulta morte'])
I(P, 2, 'Necessidades básicas',
  'Incorre nas penas do abandono quem não prover as necessidades básicas de pessoa com deficiência quando obrigado por lei ou mandado.', 'C',
  'Art. 90, § 3º (Lei 15.163/2025).',
  lei=[(PD + '90', 'Nas mesmas penas incorre quem não prover as necessidades básicas de pessoa com deficiência quando obrigado por lei ou mandado.', None, 'Lei 13.146/2015, art. 90, § 3º')],
  kw=['necessidades básicas'])
I(P, 2, 'Vítima sob cuidado',
  'Na discriminação de pessoa com deficiência, a pena aumenta de metade se a vítima estiver sob cuidado e responsabilidade do agente.', 'E',
  'Art. 88, § 1º: aumento de **1/3**.',
  lei=[(PD + '88', 'Aumenta-se a pena em 1/3 (um terço) se a vítima encontrar-se sob cuidado e responsabilidade do agente.', None, 'Lei 13.146/2015, art. 88, § 1º')],
  peg='Trocar a fração.', kw=['sob cuidado e responsabilidade'])

# ======================= LPE-36 · Terrorismo =======================
P = 'DBA26-LPE-36'
I(P, 1, 'Elementos do terrorismo',
  'O terrorismo exige que os atos sejam praticados por razões de xenofobia, discriminação ou preconceito de raça, cor, etnia e religião, com a finalidade de provocar terror social ou generalizado.', 'C',
  'Art. 2º, caput: motivação **e** finalidade específicas (motivação política não está na lei).',
  lei=[(TE + '2', 'por razões de xenofobia, discriminação ou preconceito de raça, cor, etnia e religião, quando cometidos com a finalidade de provocar terror social ou generalizado', None, 'Lei 13.260/2016, art. 2º')],
  kw=['terror social ou generalizado', 'xenofobia'])
I(P, 1, 'Movimentos sociais',
  'A Lei Antiterrorismo não se aplica à conduta de pessoas em manifestações políticas e movimentos sociais, sindicais ou religiosos direcionados por propósitos sociais ou reivindicatórios.', 'C',
  'Art. 2º, § 2º — sem prejuízo da tipificação penal comum.',
  lei=[(TE + '2', 'não se aplica à conduta individual ou coletiva de pessoas em manifestações políticas, movimentos sociais, sindicais, religiosos', None, 'Lei 13.260/2016, art. 2º, § 2º')],
  kw=['movimentos sociais', 'manifestações políticas'])
I(P, 1, 'Pena do terrorismo',
  'Os atos de terrorismo são punidos com reclusão, de 5 a 8 anos.', 'E',
  'Art. 2º, § 1º: **reclusão, de 12 a 30 anos**, além das sanções da ameaça ou da violência; 5 a 8 anos é a pena da organização terrorista (art. 3º).',
  lei=[(TE + '2', 'Pena - reclusão, de doze a trinta anos, além das sanções correspondentes à ameaça ou à violência.', None, 'Lei 13.260/2016, art. 2º, § 1º, pena')],
  peg='Trocar com a pena do art. 3º.', kw=['doze a trinta anos'])
I(P, 1, 'Atos preparatórios',
  'Os atos preparatórios de terrorismo são impuníveis, como na regra geral do iter criminis.', 'E',
  'Art. 5º: são **punidos** quando há propósito inequívoco de consumar o delito, com a pena do consumado diminuída de 1/4 até a metade — exceção à regra do art. 14, II, do CP.',
  lei=[(TE + '5', 'Realizar atos preparatórios de terrorismo com o propósito inequívoco de consumar tal delito:', None, 'Lei 13.260/2016, art. 5º')],
  peg='Aplicar a regra geral.', kw=['atos preparatórios', 'propósito inequívoco'])
I(P, 1, 'Competência',
  'O terrorismo é investigado pela Polícia Civil e julgado pela Justiça Estadual, salvo quando atingir bens da União.', 'E',
  'Art. 11: os crimes da lei são considerados praticados **contra o interesse da União**: investigação pela **Polícia Federal** e julgamento pela **Justiça Federal**.',
  lei=[(TE + '11', 'considera-se que os crimes previstos nesta Lei são praticados contra o interesse da União, cabendo à Polícia Federal a investigação criminal', None, 'Lei 13.260/2016, art. 11')],
  peg='Estadualizar.', kw=['Polícia Federal', 'Justiça Federal'])
I(P, 1, 'Hediondez',
  'Aplicam-se aos crimes da Lei 13.260/2016 as disposições da Lei dos Crimes Hediondos.', 'C',
  'Art. 17 (o terrorismo é equiparado a hediondo, CF, art. 5º, XLIII).',
  lei=[(TE + '17', 'Aplicam-se as disposições da Lei nº 8.072, de 25 de julho de 1990 , aos crimes previstos nesta Lei.', None, 'Lei 13.260/2016, art. 17')],
  kw=['Lei nº 8.072', 'equiparado'])
# --- LPE-36 · Rodada 2
I(P, 2, 'Organização terrorista',
  'Promover, constituir, integrar ou prestar auxílio a organização terrorista é crime punido com reclusão, de 5 a 8 anos, e multa.', 'C',
  'Art. 3º.',
  lei=[(TE + '3', 'Promover, constituir, integrar ou prestar auxílio, pessoalmente ou por interposta pessoa, a organização terrorista:', None, 'Lei 13.260/2016, art. 3º'), (TE + '3', 'Pena - reclusão, de cinco a oito anos, e multa.', None, 'Lei 13.260/2016, art. 3º, pena')],
  kw=['organização terrorista'])
I(P, 2, 'Financiamento',
  'O financiamento do terrorismo é punido com reclusão, de 8 a 20 anos.', 'E',
  'Art. 6º: **reclusão, de 15 a 30 anos** (8 a 20 é a pena do financiamento do tráfico, Lei 11.343/2006, art. 36).',
  lei=[(TE + '6', 'Pena - reclusão, de quinze a trinta anos.', None, 'Lei 13.260/2016, art. 6º, pena')],
  peg='Confundir com a Lei de Drogas.', kw=['financiamento', 'quinze a trinta anos'])
I(P, 2, 'Desistência antes da execução',
  'Mesmo antes de iniciada a execução do terrorismo, na hipótese de atos preparatórios, aplicam-se as regras da desistência voluntária e do arrependimento eficaz do art. 15 do CP.', 'C',
  'Art. 10.',
  lei=[(TE + '10', 'Mesmo antes de iniciada a execução do crime de terrorismo, na hipótese do art. 5º desta Lei, aplicam-se as disposições do art. 15', None, 'Lei 13.260/2016, art. 10')],
  kw=['art. 15', 'desistência voluntária'])
I(P, 2, 'Meios de investigação',
  'Na investigação do terrorismo não se aplicam os meios de obtenção de prova da Lei 12.850/2013, como a colaboração premiada, por falta de previsão expressa.', 'E',
  'Art. 16: **aplicam-se** as disposições da Lei 12.850/2013 à investigação, processo e julgamento (e o art. 1º, § 2º, II, daquela lei alcança as organizações terroristas).',
  lei=[(TE + '16', 'Aplicam-se as disposições da Lei nº 12.850, de 2 agosto de 2013 , para a investigação, processo e julgamento dos crimes previstos nesta Lei.', None, 'Lei 13.260/2016, art. 16')],
  peg='Negar a remissão expressa.', kw=['Lei nº 12.850'])

# ======================= LPE-37 · Lei 14.344/2022 (Lei Henry Borel) =======================
P = 'DBA26-LPE-37'
I(P, 1, 'Coabitação',
  'A violência doméstica e familiar contra a criança e o adolescente pode configurar-se em relação na qual o agressor tenha convivido com a vítima, independentemente de coabitação.', 'C',
  'Art. 2º, III (mesma lógica da Súmula 600/STJ para a Lei Maria da Penha).',
  lei=[(HB + '2', 'na qual o agressor conviva ou tenha convivido com a vítima, independentemente de coabitação', None, 'Lei 14.344/2022, art. 2º, III')],
  kw=['independentemente de coabitação'])
I(P, 1, 'Afastamento pelo policial',
  'Na Lei 14.344/2022, o policial pode afastar o agressor do lar mesmo havendo delegado disponível, se o Município não for sede de comarca.', 'E',
  'Art. 14, III: o **policial** só age quando, além de o Município não ser sede de comarca, **não houver delegado disponível**; o juiz é comunicado em 24 horas (§ 2º).',
  lei=[(HB + '14', 'III - pelo policial, quando o Município não for sede de comarca e não houver delegado disponível no momento da denúncia.', None, 'Lei 14.344/2022, art. 14, III')],
  peg='Apagar a subsidiariedade.', kw=['policial', 'delegado disponível'])
I(P, 1, 'Descumprimento de medida protetiva',
  'Descumprir medida protetiva de urgência da Lei 14.344/2022 é punido com reclusão, de 2 a 5 anos, como na Lei Maria da Penha.', 'E',
  'Art. 25: **detenção, de 3 meses a 2 anos** — a Lei 14.994/2024 elevou só a pena do art. 24-A da Lei 11.340/2006.',
  lei=[(HB + '25', 'Pena - detenção, de 3 (três) meses a 2 (dois) anos.', None, 'Lei 14.344/2022, art. 25, pena')],
  peg='Transpor a pena da Maria da Penha.', kw=['detenção, de 3 (três) meses a 2 (dois) anos'])
I(P, 1, 'Omissão de comunicação',
  'Deixar de comunicar à autoridade a prática de violência contra criança ou adolescente é crime, com pena em dobro se praticado por ascendente, responsável legal, padrasto ou madrasta.', 'C',
  'Art. 26 e § 2º (detenção, de 6 meses a 3 anos).',
  lei=[(HB + '26', 'Aplica-se a pena em dobro se o crime é praticado por ascendente, parente consanguíneo até terceiro grau, responsável legal, tutor, guardião, padrasto ou madrasta da vítima.', None, 'Lei 14.344/2022, art. 26, § 2º')],
  kw=['deixar de comunicar', 'em dobro'])
I(P, 1, 'Prazo do juiz',
  'Recebido o pedido de medida protetiva em favor de criança, o juiz tem 48 horas para decidir.', 'E',
  'Art. 15: **24 horas**, devendo ainda comunicar o MP e determinar a apreensão imediata de arma de fogo do agressor.',
  lei=[(HB + '15', 'caberá ao juiz, no prazo de 24 (vinte e quatro) horas', None, 'Lei 14.344/2022, art. 15')],
  peg='Dobrar o prazo.', kw=['24 (vinte e quatro) horas'])
I(P, 1, 'Concessão imediata',
  'As medidas protetivas de urgência da Lei 14.344/2022 podem ser concedidas de imediato, independentemente de audiência das partes e de manifestação do Ministério Público, que deve ser prontamente comunicado.', 'C',
  'Art. 16, § 1º.',
  lei=[(HB + '16', 'poderão ser concedidas de imediato, independentemente de audiência das partes e de manifestação do Ministério Público', None, 'Lei 14.344/2022, art. 16, § 1º')],
  kw=['de imediato', 'medidas protetivas'])
# --- LPE-37 · Rodada 2
I(P, 2, 'Omissão com morte',
  'No crime de omissão de comunicação da Lei 14.344/2022, a pena é triplicada se da omissão resulta morte.', 'C',
  'Art. 26, § 1º (lesão grave: aumento de metade).',
  lei=[(HB + '26', 'A pena é aumentada de metade, se da omissão resulta lesão corporal de natureza grave, e triplicada, se resulta morte.', None, 'Lei 14.344/2022, art. 26, § 1º')],
  kw=['triplicada'])
I(P, 2, 'Fiança',
  'Preso em flagrante pelo descumprimento de medida protetiva da Lei 14.344/2022, o autor só pode obter fiança da autoridade judicial.', 'C',
  'Art. 25, § 2º.',
  lei=[(HB + '25', 'Na hipótese de prisão em flagrante, apenas a autoridade judicial poderá conceder fiança.', None, 'Lei 14.344/2022, art. 25, § 2º')],
  kw=['apenas a autoridade judicial'])
I(P, 2, 'Encaminhamento ao IML',
  'No atendimento à criança vítima de violência doméstica, a autoridade policial só encaminha a vítima ao IML após requisição do Ministério Público.', 'E',
  'Art. 13, I: a autoridade policial deve encaminhar a vítima ao SUS e ao IML **imediatamente**.',
  lei=[(HB + '13', 'I - encaminhar a vítima ao Sistema Único de Saúde e ao Instituto Médico-Legal imediatamente;', None, 'Lei 14.344/2022, art. 13, I')],
  peg='Condicionar à requisição do MP.', kw=['Instituto Médico-Legal', 'imediatamente'])
I(P, 2, 'Liberdade provisória',
  'Na Lei 14.344/2022, mesmo havendo risco à integridade física da vítima, o preso tem direito à liberdade provisória mediante fiança.', 'E',
  'Art. 14, § 3º: nos casos de risco à integridade física da vítima ou à efetividade da medida protetiva, **não será concedida liberdade provisória**.',
  lei=[(HB + '14', 'não será concedida liberdade provisória ao preso', None, 'Lei 14.344/2022, art. 14, § 3º')],
  peg='Garantir a liberdade provisória.', kw=['liberdade provisória'])

# ======================= LPE-38 · Escuta especializada e depoimento especial =======================
P = 'DBA26-LPE-38'
I(P, 1, 'Escuta especializada',
  'Escuta especializada é o procedimento de entrevista sobre situação de violência com criança ou adolescente perante órgão da rede de proteção, limitado o relato ao estritamente necessário.', 'C',
  'Lei 13.431/2017, art. 7º — a **escuta especializada** é feita pela rede de proteção, não para produzir prova.',
  lei=[(EE + '7', 'Escuta especializada é o procedimento de entrevista sobre situação de violência com criança ou adolescente perante órgão da rede de proteção', None, 'Lei 13.431/2017, art. 7º')],
  kw=['escuta especializada', 'rede de proteção'])
I(P, 1, 'Depoimento especial',
  'Depoimento especial é o procedimento de oitiva de criança ou adolescente vítima ou testemunha de violência perante autoridade policial ou judiciária.', 'C',
  'Art. 8º; o Decreto 9.603/2018 acrescenta a finalidade de produção de provas (art. 22).',
  lei=[(EE + '8', 'Depoimento especial é o procedimento de oitiva de criança ou adolescente vítima ou testemunha de violência perante autoridade policial ou judiciária.', None, 'Lei 13.431/2017, art. 8º')],
  kw=['depoimento especial', 'autoridade policial ou judiciária'])
I(P, 1, 'Rito cautelar',
  'O depoimento especial segue o rito cautelar de antecipação de prova quando a criança tiver menos de 12 anos ou em caso de violência física.', 'E',
  'Art. 11, § 1º: quando a criança tiver **menos de 7 anos** ou em caso de **violência sexual**.',
  lei=[(EE + '11', 'I - quando a criança ou o adolescente tiver menos de 7 (sete) anos;', None, 'Lei 13.431/2017, art. 11, § 1º, I'), (EE + '11', 'II - em caso de violência sexual.', None, 'Lei 13.431/2017, art. 11, § 1º, II')],
  peg='Trocar a idade e a espécie de violência.', kw=['menos de 7 (sete) anos', 'violência sexual'])
I(P, 1, 'Contato com o acusado',
  'A criança vítima pode ter contato visual com o acusado durante o depoimento especial, desde que não haja contato físico.', 'E',
  'Art. 9º: será resguardada de **qualquer contato, ainda que visual**, com o suposto autor ou com quem represente ameaça.',
  lei=[(EE + '9', 'será resguardado de qualquer contato, ainda que visual, com o suposto autor ou acusado', None, 'Lei 13.431/2017, art. 9º')],
  peg='Admitir o contato visual.', kw=['ainda que visual'])
I(P, 1, 'Finalidade da escuta',
  'A escuta especializada tem o escopo de produzir prova para a investigação e a responsabilização do agressor.', 'E',
  'Decreto 9.603/2018, art. 19, § 4º: **não tem o escopo de produzir prova**; limita-se à proteção social e ao provimento de cuidados. A prova é colhida no **depoimento especial**.',
  lei=[(DE + '19', 'A escuta especializada não tem o escopo de produzir prova para o processo de investigação e de responsabilização', None, 'Decreto 9.603/2018, art. 19, § 4º')],
  peg='Confundir escuta e depoimento.', kw=['não tem o escopo de produzir prova', 'Decreto 9.603/2018'])
I(P, 1, 'Violação de sigilo',
  'Violar sigilo processual, permitindo que depoimento de criança seja assistido por pessoa estranha ao processo, sem autorização judicial e sem consentimento do depoente ou de seu representante, é crime punido com reclusão, de 1 a 4 anos.', 'C',
  'Lei 13.431/2017, art. 24 — **violação de sigilo** do depoimento especial.',
  lei=[(EE + '24', 'permitindo que depoimento de criança ou adolescente seja assistido por pessoa estranha ao processo', None, 'Lei 13.431/2017, art. 24'), (EE + '24', 'Pena - reclusão, de 1 (um) a 4 (quatro) anos, e multa.', None, 'Lei 13.431/2017, art. 24, pena')],
  kw=['sigilo processual', 'pessoa estranha ao processo'])
# --- LPE-38 · Rodada 2
I(P, 2, 'Novo depoimento',
  'Não se admite novo depoimento especial, salvo quando justificada sua imprescindibilidade pela autoridade competente e houver concordância da vítima ou testemunha, ou de seu representante.', 'C',
  'Art. 11, § 2º: o depoimento é, sempre que possível, **único** (caput).',
  lei=[(EE + '11', 'Não será admitida a tomada de novo depoimento especial, salvo quando justificada a sua imprescindibilidade', None, 'Lei 13.431/2017, art. 11, § 2º')],
  kw=['novo depoimento', 'imprescindibilidade'])
I(P, 2, 'Entre 18 e 21 anos',
  'A aplicação da Lei 13.431/2017 é obrigatória para vítimas e testemunhas de violência entre 18 e 21 anos.', 'E',
  'Art. 3º, par. ún.: é **facultativa** nessa faixa etária.',
  lei=[(EE + '3', 'A aplicação desta Lei é facultativa para as vítimas e testemunhas de violência entre 18 (dezoito) e 21 (vinte e um) anos', None, 'Lei 13.431/2017, art. 3º, par. ún.')],
  peg='Tornar obrigatória.', kw=['facultativa', '18 (dezoito) e 21'])
I(P, 2, 'Depor ao juiz',
  'À vítima ou testemunha de violência é garantido o direito de prestar depoimento diretamente ao juiz, se assim o entender.', 'C',
  'Art. 12, § 1º.',
  lei=[(EE + '12', 'é garantido o direito de prestar depoimento diretamente ao juiz, se assim o entender', None, 'Lei 13.431/2017, art. 12, § 1º')],
  kw=['diretamente ao juiz'])
I(P, 2, 'Prova além do depoimento',
  'Colhido o depoimento especial, os órgãos policiais ficam dispensados de buscar outras provas, pois ele basta para a condenação.', 'E',
  'Art. 22: os órgãos policiais **envidarão esforços** para que o depoimento especial **não seja o único meio de prova**.',
  lei=[(EE + '22', 'envidarão esforços investigativos para que o depoimento especial não seja o único meio de prova', None, 'Lei 13.431/2017, art. 22')],
  peg='Dispensar a investigação.', kw=['único meio de prova'])

# ======================= LPE-39 · Lei 15.358/2026 (marco legal do combate ao crime organizado) =======================
P = 'DBA26-LPE-39'
I(P, 1, 'Facção criminosa',
  'Para a Lei 15.358/2026, organização criminosa ultraviolenta, denominada facção criminosa, é o agrupamento de 3 ou mais pessoas que emprega violência, grave ameaça ou coação para impor controle territorial ou social, intimidar populações ou autoridades ou atacar serviços essenciais.', 'C',
  'Art. 2º, § 2º — conceito próprio, distinto da organização criminosa da Lei 12.850/2013 (4 ou mais pessoas).',
  lei=[(MO + '2', 'considera-se organização criminosa ultraviolenta, denominada facção criminosa, o agrupamento de 3 (três) ou mais pessoas', None, 'Lei 15.358/2026, art. 2º, § 2º')],
  kw=['facção criminosa', '3 (três) ou mais pessoas'])
I(P, 1, 'Número de integrantes',
  'A organização criminosa ultraviolenta da Lei 15.358/2026 exige, como a da Lei 12.850/2013, quatro ou mais integrantes.', 'E',
  'Art. 2º, § 2º: bastam **3 ou mais** pessoas.',
  lei=[(MO + '2', 'o agrupamento de 3 (três) ou mais pessoas que emprega violência, grave ameaça ou coação', None, 'Lei 15.358/2026, art. 2º, § 2º')],
  peg='Transpor o número da Lei 12.850/2013.', kw=['3 (três) ou mais'])
I(P, 1, 'Domínio social estruturado: pena',
  'As condutas do art. 2º da Lei 15.358/2026, como impor controle territorial mediante violência, são punidas com reclusão, de 20 a 40 anos.', 'C',
  'Art. 2º, pena, sem prejuízo das sanções da violência ou de outros crimes; são hediondas (art. 4º).',
  lei=[(MO + '2', 'Pena - reclusão, de 20 (vinte) a 40 (quarenta) anos', None, 'Lei 15.358/2026, art. 2º, pena')],
  kw=['20 (vinte) a 40 (quarenta) anos'])
I(P, 1, 'Livramento condicional',
  'Os crimes do art. 2º da Lei 15.358/2026 admitem livramento condicional após o cumprimento de dois terços da pena.', 'E',
  'Art. 2º, § 4º: são insuscetíveis de anistia, graça e indulto, de fiança e de **livramento condicional**.',
  lei=[(MO + '2', 'III - livramento condicional.', None, 'Lei 15.358/2026, art. 2º, § 4º, III')],
  peg='Admitir o livramento.', kw=['livramento condicional', 'insuscetíveis'])
I(P, 1, 'Comando da facção',
  'A pena do art. 2º da Lei 15.358/2026 aumenta de 1/6 a 2/3 se o agente exercer o comando da organização, ainda que não pratique pessoalmente os atos de execução.', 'E',
  'Art. 2º, § 1º, I: aumento de **2/3 ao dobro**.',
  lei=[(MO + '2', 'Aumenta-se a pena de 2/3 (dois terços) ao dobro se:', None, 'Lei 15.358/2026, art. 2º, § 1º')],
  peg='Usar a fração da Lei 12.850/2013.', kw=['2/3 (dois terços) ao dobro', 'comando'])
I(P, 1, 'Prazos do inquérito',
  'Nos crimes da Lei 15.358/2026, o inquérito policial deve ser concluído em 90 dias se o indiciado estiver preso, e em 270 dias se solto, prorrogável por igual período.', 'C',
  'Art. 5º, caput.',
  lei=[(MO + '5', 'o inquérito policial será concluído no prazo de 90 (noventa) dias, se o indiciado estiver preso, e de 270 (duzentos e setenta) dias, quando estiver solto', None, 'Lei 15.358/2026, art. 5º')],
  kw=['90 (noventa) dias', '270 (duzentos e setenta) dias'])
I(P, 1, 'Excesso de prazo',
  'Descumprido qualquer prazo do art. 5º da Lei 15.358/2026, a prisão deve ser automaticamente relaxada.', 'E',
  'Art. 5º, § 4º: o descumprimento **não gera automaticamente** o relaxamento; o juiz avalia o caso concreto.',
  lei=[(MO + '5', 'não gera automaticamente o relaxamento da prisão ou a concessão de liberdade ao preso', None, 'Lei 15.358/2026, art. 5º, § 4º')],
  peg='Criar relaxamento automático.', kw=['relaxamento', 'automaticamente'])
I(P, 1, 'Atos preparatórios',
  'Quem pratica atos preparatórios, com propósito inequívoco de consumar condutas do art. 2º da Lei 15.358/2026, sujeita-se à pena do crime consumado, reduzida de 1/3 até a metade.', 'C',
  'Art. 2º, § 5º — antecipação da tutela penal, como na Lei Antiterrorismo.',
  lei=[(MO + '2', 'estará sujeito à pena do crime consumado, reduzida de 1/3 (um terço) até a 1/2 (metade)', None, 'Lei 15.358/2026, art. 2º, § 5º')],
  kw=['atos preparatórios'])
I(P, 1, 'Prisão preventiva',
  'Pela letra da Lei 15.358/2026, a prática dos crimes do seu art. 2º é causa suficiente para a decretação de prisão preventiva.', 'C',
  'Art. 2º, § 9º.',
  lei=[(MO + '2', 'A prática dos crimes previstos neste artigo é causa suficiente para decretação de prisão preventiva.', None, 'Lei 15.358/2026, art. 2º, § 9º')],
  kw=['prisão preventiva', 'causa suficiente'])
# --- LPE-39 · Rodada 2
I(P, 2, 'Falso integrante',
  'Alegar falsamente pertencer a organização criminosa ultraviolenta para obter vantagem ou intimidar terceiros é crime punido com reclusão, de 12 a 20 anos, e multa.', 'C',
  'Art. 3º, VI.',
  lei=[(MO + '3', 'VI - alegar falsamente pertencer a organização criminosa ultraviolenta', None, 'Lei 15.358/2026, art. 3º, VI'), (MO + '3', 'Pena - reclusão, de 12 (doze) a 20 (vinte) anos, e multa.', None, 'Lei 15.358/2026, art. 3º, pena')],
  kw=['alegar falsamente pertencer'])
I(P, 2, 'Formas especiais',
  'As condutas da Lei 15.358/2026 e a constituição de milícia privada do art. 288-A do CP constituem formas especiais de organização criminosa, aplicando-se no que couber as disposições materiais da Lei 12.850/2013.', 'C',
  'Art. 4º, par. ún.',
  lei=[(MO + '4', 'constituem formas especiais de organização criminosa', None, 'Lei 15.358/2026, art. 4º, par. ún.')],
  kw=['formas especiais de organização criminosa', 'art. 288-A'])
I(P, 2, 'Representação indeferida',
  'Indeferida representação do delegado nos crimes da Lei 15.358/2026, não há mecanismo legal de revisão se o Ministério Público não recorrer.', 'E',
  'Art. 5º, § 6º: o delegado pode, em **48 horas**, submeter a matéria à **revisão da instância superior do órgão ministerial**.',
  lei=[(MO + '5', 'poderá o delegado de polícia, no prazo de 48 (quarenta e oito) horas, submeter a matéria à revisão da instância superior competente do órgão ministerial', None, 'Lei 15.358/2026, art. 5º, § 6º')],
  peg='Ignorar a revisão ministerial.', kw=['48 (quarenta e oito) horas', 'revisão'])
I(P, 2, 'Perda civil de bens',
  'A declaração de perda civil de bens da Lei 15.358/2026 depende de prévia condenação criminal transitada em julgado.', 'E',
  'Art. 17: **independe** da aferição de responsabilidade civil ou criminal e do desfecho das ações, ressalvada a absolvição que reconheça a inexistência do fato.',
  lei=[(MO + '17', 'A declaração de perda civil independe da aferição de responsabilidade civil ou criminal', None, 'Lei 15.358/2026, art. 17')],
  peg='Exigir condenação.', kw=['perda civil', 'independe'])
I(P, 2, 'Parecer do MP',
  'Na representação do delegado nos crimes da Lei 15.358/2026, o Ministério Público emite parecer em 10 dias.', 'E',
  'Art. 5º, § 2º: em **5 dias**; o juiz decide em 15 dias (§ 1º) e, na urgência, ambos em 24 horas (§ 3º).',
  lei=[(MO + '5', 'o Ministério Público emitirá parecer no prazo de 5 (cinco) dias', None, 'Lei 15.358/2026, art. 5º, § 2º')],
  peg='Trocar o prazo.', kw=['5 (cinco) dias', 'parecer'])
I(P, 2, 'Recrutamento de criança',
  'A pena dos crimes de domínio social estruturado aumenta de 2/3 ao dobro se o agente recrutar ou permitir que criança ou adolescente integre a organização ou execute seus atos.', 'C',
  'Art. 2º, § 1º, VIII.',
  lei=[(MO + '2', 'VIII - o agente recrutar, atrair, convidar, induzir, coagir, permitir ou consentir que criança ou adolescente integre', None, 'Lei 15.358/2026, art. 2º, § 1º, VIII')],
  kw=['criança ou adolescente', 'recrutar'])

# ======================= LPE-40 · Jurisprudência aplicada (fechamento) =======================
P = 'DBA26-LPE-40'
I(P, 1, 'Combinação de leis de drogas',
  'É possível aplicar o tráfico privilegiado da Lei 11.343/2006 sobre a pena-base mais branda da Lei 6.368/1976, combinando o que cada lei tem de favorável.', 'E',
  '**Súmula 501/STJ**: a retroatividade só cabe se a lei nova, **na íntegra**, for mais favorável, **vedada a combinação de leis**.',
  juris=[J['S501']], peg='Admitir a lex tertia.', kw=['Súmula 501/STJ', 'combinação de leis'])
I(P, 1, 'Confissão no tráfico',
  'A atenuante da confissão no tráfico, quando o acusado admite a posse para uso próprio e nega o tráfico, deve incidir em proporção inferior à da confissão plena.', 'C',
  '**Súmula 630/STJ** na **redação revisada** (Tema 1.194, 10/09/2025) — a antiga negava a atenuante.',
  juris=[J['S630']], kw=['Súmula 630/STJ', 'redação revisada'])
I(P, 1, 'Ingresso em domicílio',
  'A entrada forçada em domicílio sem mandado, para flagrante de tráfico, só é lícita quando amparada em fundadas razões, justificadas a posteriori, que indiquem situação de flagrante dentro da casa.', 'C',
  '**Tema 280/RG** (STF, RE 603.616, 05/11/2015).',
  juris=[J['RG280']], kw=['Tema 280', 'fundadas razões'])
I(P, 1, 'Busca pessoal',
  'A "atitude suspeita" genérica, descrita pelo policial sem elementos objetivos, basta para justificar a busca pessoal sem mandado, e o encontro de droga convalida a diligência.', 'E',
  'STJ, **RHC 158.580/BA** (19/04/2022): exige **fundada suspeita** descrita com elementos objetivos; o achado posterior **não convalida** a revista ilegal.',
  juris=[J['RHC158580']], peg='Convalidar pela droga achada.', kw=['RHC 158.580', 'fundada suspeita'])
I(P, 1, 'Flagrante preparado',
  'Não há crime quando a preparação do flagrante pela polícia torna impossível a sua consumação — situação distinta da venda a agente policial disfarçado com conduta criminal preexistente.', 'C',
  '**Súmula 145/STF**; as figuras do agente disfarçado (Lei 10.826/2003, art. 17, § 2º; Lei 11.343/2006, art. 33, § 1º, IV) exigem elementos de conduta preexistente.',
  juris=[J['STF145']], kw=['Súmula 145/STF', 'agente disfarçado'])
I(P, 1, 'Transferência para presídio federal',
  'A decisão que determina a transferência de preso para estabelecimento penitenciário federal é nula se não houver oitiva prévia da defesa.', 'E',
  '**Súmula 639/STJ**: **não fere** o contraditório a decisão que, sem oitiva prévia da defesa, determina a transferência ou a permanência no sistema federal.',
  juris=[J['S639']], peg='Exigir contraditório prévio.', kw=['Súmula 639/STJ'])
I(P, 1, 'Medida socioeducativa',
  'O Ministério Público pode aplicar medida socioeducativa ao adolescente ao conceder a remissão na fase pré-processual.', 'E',
  '**Súmula 108/STJ**: a aplicação de medida socioeducativa é da **competência exclusiva do juiz**.',
  juris=[J['S108']], peg='Dar ao MP poder de aplicar medida.', kw=['Súmula 108/STJ', 'competência exclusiva do juiz'])
I(P, 1, 'Prisão temporária',
  'A prisão temporária pode ser decretada só porque o investigado não tem residência fixa, para averiguação.', 'E',
  'STF, **ADIs 3.360 e 4.109** (11/02/2022): exige imprescindibilidade concreta para o inquérito, fundadas razões nos crimes do rol, fatos contemporâneos e insuficiência de cautelares — **não** cabe para averiguação nem só pela falta de residência fixa.',
  juris=[J['ADI3360']], peg='Prender para averiguar.', kw=['ADIs 3.360 e 4.109', 'averiguação'])
# --- LPE-40 · Rodada 2
I(P, 2, 'Permanência no sistema federal',
  'Para a prorrogação da permanência do preso no sistema penitenciário federal, é prescindível fato novo, bastando decisão fundamentada sobre a persistência dos motivos da transferência.', 'C',
  '**Súmula 662/STJ**.',
  juris=[J['S662']], kw=['Súmula 662/STJ', 'fato novo'])
I(P, 2, 'Regressão da medida',
  'A regressão de medida socioeducativa dispensa a oitiva do adolescente, bastando o relatório da equipe técnica.', 'E',
  '**Súmula 265/STJ**: é **necessária a oitiva** do menor infrator antes da regressão.',
  juris=[J['S265']], peg='Dispensar a oitiva.', kw=['Súmula 265/STJ', 'regressão'])
I(P, 2, 'Sursis processual e trancamento',
  'A aceitação da proposta de suspensão condicional do processo não prejudica a análise do pedido de trancamento da ação penal.', 'C',
  '**Súmula 667/STJ**.',
  juris=[J['S667']], kw=['Súmula 667/STJ', 'trancamento'])
I(P, 2, 'Fuga ao avistar a polícia',
  'A fuga repentina do suspeito ao avistar a guarnição pode configurar fundada suspeita para a busca pessoal em via pública, cabendo ao Estado provar as circunstâncias.', 'C',
  'STJ, **HC 877.943/MS** (Terceira Seção, 18/04/2024), sob especial escrutínio do relato policial.',
  juris=[J['HC877943']], kw=['HC 877.943', 'fuga'])
I(P, 2, 'Sinal clandestino de internet',
  'Aplica-se o princípio da insignificância à transmissão clandestina de sinal de internet via radiofrequência, se o provedor for pequeno.', 'E',
  '**Súmula 606/STJ**: **não se aplica** (art. 183 da Lei 9.472/1997).',
  juris=[J['S606']], peg='Aplicar a bagatela.', kw=['Súmula 606/STJ'])
