# Pente Fino de Direito Penal (Parte Geral) — PEN-4 (teoria do tipo e fato típico, 4.1 a 4.12) (08/11/2026).
from base import I
from pen_juris import J

CP = 'CP:'
DOLO = (CP + '18', 'doloso, quando o agente quis o resultado ou assumiu o risco de produzi-lo', None, 'CP, art. 18, I')
CULPA = (CP + '18', 'culposo, quando o agente deu causa ao resultado por imprudência, negligência ou imperícia', None, 'CP, art. 18, II')
EXCEP = (CP + '18', 'Salvo os casos expressos em lei, ninguém pode ser punido por fato previsto como crime, senão quando o pratica dolosamente.', None, 'CP, art. 18, par. ún.')
ERRO_TIPO = (CP + '20', 'O erro sobre elemento constitutivo do tipo legal de crime exclui o dolo, mas permite a punição por crime culposo, se previsto em lei.', None, 'CP, art. 20, caput')
TENT = (CP + '14', 'tentado, quando, iniciada a execução, não se consuma por circunstâncias alheias à vontade do agente', None, 'CP, art. 14, II')
PENA_TENT = (CP + '14', 'Salvo disposição em contrário, pune-se a tentativa com a pena correspondente ao crime consumado, diminuída de um a dois terços.', None, 'CP, art. 14, par. ún.')
DESIST = (CP + '15', 'O agente que, voluntariamente, desiste de prosseguir na execução ou impede que o resultado se produza, só responde pelos atos já praticados.', None, 'CP, art. 15')
ARREP = (CP + '16', 'Nos crimes cometidos sem violência ou grave ameaça à pessoa', 'a pena será reduzida de um a dois terços', 'CP, art. 16')
IMPOSS = (CP + '17', 'Não se pune a tentativa quando, por ineficácia absoluta do meio ou por absoluta impropriedade do objeto, é impossível consumar-se o crime.', None, 'CP, art. 17')

# ======================= PEN-4 · Teoria do tipo e fato típico =======================
P = 'DBA26-PEN-4'
I(P, 1, 'Elementos do fato típico',
  'São elementos do fato típico, no crime material consumado: conduta, resultado naturalístico, nexo causal e tipicidade.', 'C',
  'Nos crimes **formais** e de **mera conduta**, o fato típico se resume a conduta e tipicidade. O nexo causal está no art. 13.',
  lei=[(CP + '13', 'O resultado, de que depende a existência do crime, somente é imputável a quem lhe deu causa.', None, 'CP, art. 13, caput')],
  kw=['conduta, resultado naturalístico, nexo causal e tipicidade'])
I(P, 1, 'Elementos normativos',
  'Elementos normativos do tipo são aqueles percebidos pelos sentidos, sem necessidade de juízo de valor, como "matar" e "alguém".', 'E',
  'Esses são os elementos **descritivos**. Os **elementos normativos** exigem **juízo de valor** ("coisa alheia", "sem justa causa").',
  lei=[(CP + '155', 'Subtrair, para si ou para outrem, coisa alheia móvel', None, 'CP, art. 155, caput')],
  kw=['elementos normativos', 'juízo de valor'])
I(P, 1, 'Tipo e ilicitude: ratio cognoscendi',
  'Pela teoria indiciária (ratio cognoscendi), adotada pela doutrina majoritária, a tipicidade é indício da ilicitude, que se presume até prova de causa justificante.', 'C',
  'Praticado o fato típico, presume-se relativamente a ilicitude; a **excludente** (art. 23) é que precisa ser demonstrada.',
  lei=[(CP + '23', 'Não há crime quando o agente pratica o fato:', None, 'CP, art. 23, caput')],
  kw=['teoria indiciária', 'ratio cognoscendi'])
I(P, 1, 'Elemento subjetivo especial',
  'O especial fim de agir, como o "intuito de obter indevida vantagem econômica" na extorsão, é elemento objetivo do tipo.', 'E',
  'É **elemento subjetivo especial** do tipo (dolo específico, na linguagem clássica): finalidade que vai além do dolo de constranger.',
  lei=[(CP + '158', 'Constranger alguém, mediante violência ou grave ameaça, e com o intuito de obter para si ou para outrem indevida vantagem econômica', None, 'CP, art. 158, caput')],
  peg='Classificar a finalidade especial como elemento objetivo.', kw=['elemento subjetivo especial'])
I(P, 1, 'Adequação típica mediata',
  'Na tentativa e na participação, a adequação típica é mediata (ou indireta), pois exige uma norma de extensão da Parte Geral.', 'C',
  'Normas de extensão: **tentativa** (art. 14, II — extensão temporal) e **concurso de pessoas** (art. 29 — extensão pessoal).',
  lei=[TENT, (CP + '29', 'Quem, de qualquer modo, concorre para o crime incide nas penas a este cominadas', None, 'CP, art. 29, caput')],
  kw=['adequação típica mediata', 'norma de extensão'])
# --- PEN-4 · Rodada 2
I(P, 2, 'Tipo aberto',
  'Os crimes culposos são, em regra, tipos fechados, pois a lei descreve minuciosamente a conduta imprudente punível.', 'E',
  'Os culposos são **tipos abertos**: a lei não descreve a conduta descuidada, cabendo ao juiz comparar com o **dever objetivo de cuidado** (art. 18, II).',
  lei=[CULPA], peg='Trocar aberto por fechado.', kw=['tipos abertos', 'dever objetivo de cuidado'])
I(P, 2, 'Tipicidade material',
  'Além da tipicidade formal, a tipicidade penal exige tipicidade material, isto é, lesão ou perigo relevante ao bem jurídico, cuja ausência é reconhecida pela insignificância.', 'C',
  'A **tipicidade material** é afastada quando presentes os vetores da insignificância fixados pelo STF (HC 84.412).',
  juris=[J['HC84412']], kw=['tipicidade material'])
I(P, 2, 'Teoria dos elementos negativos do tipo',
  'Para a teoria dos elementos negativos do tipo, as causas de justificação integram o tipo como elementos negativos, de modo que o fato justificado é atípico.', 'C',
  'É a teoria do **tipo total de injusto**. A doutrina majoritária no Brasil prefere a teoria indiciária: o fato justificado é típico, mas lícito (art. 23: "não há crime").',
  lei=[(CP + '23', 'Não há crime quando o agente pratica o fato:', None, 'CP, art. 23, caput')],
  kw=['elementos negativos do tipo'])

# ======================= PEN-4.1 · Crime doloso e crime culposo =======================
P = 'DBA26-PEN-4.1'
I(P, 1, 'Dolo direto e eventual',
  'O Código Penal adotou a teoria da representação para o dolo eventual, bastando que o agente preveja o resultado como possível.', 'E',
  'A letra do art. 18, I, exige que o agente **assuma o risco** de produzir o resultado (teoria do **assentimento**); a mera previsão também está na culpa consciente.',
  lei=[DOLO], kw=['teoria da vontade', 'assentimento'])
I(P, 1, 'Culpa consciente x dolo eventual',
  'Na culpa consciente, o agente prevê o resultado e o aceita, sendo-lhe indiferente que ocorra.', 'E',
  'Isso é **dolo eventual**. Na **culpa consciente** o agente prevê o resultado, mas **acredita sinceramente** que ele não ocorrerá (confia na sua habilidade).',
  lei=[DOLO, CULPA], peg='Descrever o dolo eventual como culpa consciente.', kw=['culpa consciente', 'dolo eventual'])
I(P, 1, 'Excepcionalidade do crime culposo',
  'Salvo os casos expressos em lei, ninguém pode ser punido por fato previsto como crime senão quando o pratica dolosamente.', 'C',
  'É a **excepcionalidade do crime culposo** (art. 18, par. ún.): só há crime culposo com previsão expressa.',
  lei=[EXCEP], kw=['excepcionalidade do crime culposo'])
I(P, 1, 'Modalidades de culpa',
  'Imperícia é a culpa decorrente de falta de aptidão técnica para o exercício de arte, profissão ou ofício; negligência é a omissão de cautela; imprudência é a ação precipitada.', 'C',
  'São as três modalidades de culpa do art. 18, II: **imprudência** (fazer), **negligência** (deixar de fazer) e **imperícia** (falta de aptidão técnica).',
  lei=[CULPA], kw=['imperícia', 'negligência', 'imprudência'])
I(P, 1, 'Compensação de culpas',
  'No direito penal, a culpa concorrente da vítima compensa a culpa do agente e exclui o crime culposo.', 'E',
  'Não há **compensação de culpas** no direito penal. A culpa da vítima pode influir na pena (comportamento da vítima, art. 59); só a **culpa exclusiva** da vítima afasta a responsabilidade.',
  lei=[(CP + '59', 'bem como ao comportamento da vítima', None, 'CP, art. 59, caput')],
  peg='Importar a compensação de culpas do direito civil.', kw=['compensação de culpas', 'culpa exclusiva'])
I(P, 1, 'Perdão judicial no homicídio culposo',
  'No homicídio culposo, o juiz poderá deixar de aplicar a pena se as consequências da infração atingirem o próprio agente de forma tão grave que a sanção penal se torne desnecessária.', 'C',
  'Hipótese de **perdão judicial** (CP, art. 121, § 5º; art. 107, IX).',
  lei=[(CP + '121', 'Na hipótese de homicídio culposo, o juiz poderá deixar de aplicar a pena', 'se torne desnecessária', 'CP, art. 121, § 5º')],
  kw=['perdão judicial', 'homicídio culposo'])
# --- PEN-4.1 · Rodada 2
I(P, 2, 'Tentativa no crime culposo',
  'Admite-se tentativa no crime culposo, inclusive na culpa inconsciente.', 'E',
  'A tentativa exige o agente **querer** a consumação (art. 14, II: não se consuma "por circunstâncias alheias à vontade"). Não cabe no culposo; a doutrina só ressalva a **culpa imprópria** (erro vencível na descriminante putativa).',
  lei=[TENT],
  exc=['Culpa imprópria (descriminante putativa por erro evitável, art. 20, § 1º, parte final): a doutrina admite tentativa'],
  peg='Admitir tentativa em culpa propriamente dita.', kw=['tentativa', 'culpa imprópria'])
I(P, 2, 'Culpa imprópria',
  'Na culpa imprópria, o agente quer o resultado por erro evitável sobre situação de fato que, se existisse, tornaria a ação legítima, e responde por crime culposo, se previsto em lei.', 'C',
  'É a **culpa imprópria** da parte final do art. 20, § 1º: "não há isenção de pena quando o erro deriva de culpa e o fato é punível como crime culposo".',
  lei=[(CP + '20', 'Não há isenção de pena quando o erro deriva de culpa e o fato é punível como crime culposo.', None, 'CP, art. 20, § 1º, parte final')],
  kw=['culpa imprópria'])
I(P, 2, 'Dolo geral',
  'No dolo geral (erro sucessivo), o agente que, acreditando ter matado a vítima, a lança ao rio, causando a morte por afogamento, responde por homicídio doloso consumado.', 'C',
  'Doutrina majoritária: o **dolo geral** abrange todo o processo; o desvio causal é irrelevante e não se fraciona em tentativa + homicídio culposo. A base é o art. 13 (causalidade) e o art. 18, I.',
  lei=[DOLO], kw=['dolo geral', 'erro sucessivo'])
I(P, 2, 'Concorrência de culpas',
  'Se dois motoristas agem com imprudência e causam juntos a morte de terceiro, cada um responde por homicídio culposo.', 'C',
  'Na **concorrência de culpas** cada um responde pelo seu descuido; não se fala em compensação. Base: equivalência dos antecedentes (art. 13) e art. 18, II.',
  lei=[CULPA], kw=['concorrência de culpas'])

# ======================= PEN-4.2 · Crime qualificado pelo resultado e preterdoloso =======================
P = 'DBA26-PEN-4.2'
I(P, 1, 'Resultado agravador: culpa mínima',
  'Pelo resultado que agrava especialmente a pena responde o agente que lhe deu causa, ainda que o resultado fosse imprevisível.', 'E',
  'Art. 19: só responde quem causou o resultado **ao menos culposamente**; o resultado imprevisível não é imputado, pois se veda a **responsabilidade objetiva**.',
  lei=[(CP + '19', 'Pelo resultado que agrava especialmente a pena, só responde o agente que o houver causado ao menos culposamente.', None, 'CP, art. 19')],
  kw=['ao menos culposamente', 'responsabilidade objetiva'])
I(P, 1, 'Preterdolo: lesão corporal seguida de morte',
  'A lesão corporal seguida de morte é exemplo de crime preterdoloso: dolo na lesão e culpa no resultado morte.', 'C',
  'Art. 129, § 3º: "as circunstâncias evidenciam que o agente não quis o resultado, nem assumiu o risco". **Dolo no antecedente, culpa no consequente**.',
  lei=[(CP + '129', 'Se resulta morte e as circunstâncias evidenciam que o agente não', 'nem assumiu o risco de', 'CP, art. 129, § 3º')],
  kw=['preterdoloso', 'dolo no antecedente'])
I(P, 1, 'Tentativa no preterdoloso',
  'O crime preterdoloso admite tentativa, pois o agente tinha dolo quanto à conduta antecedente.', 'E',
  'No preterdoloso propriamente dito o resultado agravador é **culposo**, e não há tentativa de resultado que o agente não quis. A doutrina admite, porém, tentativa nos qualificados pelo resultado com **dolo no consequente**.',
  lei=[TENT], peg='Admitir tentativa de resultado culposo.', kw=['tentativa', 'preterdoloso'])
I(P, 1, 'Qualificado pelo resultado: espécies',
  'O crime qualificado pelo resultado é gênero que comporta dolo no antecedente e dolo no consequente, dolo e culpa (preterdolo), culpa e culpa e culpa e dolo.', 'C',
  'Classificação doutrinária; o **preterdoloso** é só uma das espécies. O limite é o art. 19: o resultado agravador exige ao menos culpa.',
  lei=[(CP + '19', 'Pelo resultado que agrava especialmente a pena', None, 'CP, art. 19')],
  kw=['qualificado pelo resultado', 'gênero'])
I(P, 1, 'Latrocínio consumado',
  'Para o STF, há latrocínio consumado quando o homicídio se consuma, ainda que o agente não realize a subtração dos bens da vítima.', 'C',
  'É a **Súmula 610/STF**: no latrocínio (qualificado pelo resultado), a consumação acompanha a morte.',
  juris=[J['STF610']], kw=['Súmula 610/STF', 'latrocínio'])
# --- PEN-4.2 · Rodada 2
I(P, 2, 'Latrocínio: subtração consumada, morte tentada',
  'Se a subtração se consuma, mas a morte da vítima fica na tentativa, o STF entende configurado o latrocínio consumado.', 'E',
  'A lógica da **Súmula 610/STF** é que a consumação do latrocínio depende da **morte**: com morte tentada, há latrocínio **tentado**.',
  juris=[J['STF610']], peg='Inverter a regra da Súmula 610.', kw=['latrocínio tentado'])
I(P, 2, 'Lesão seguida de morte e dolo eventual',
  'Se as circunstâncias indicam que o agente assumiu o risco de matar ao agredir a vítima, o crime deixa de ser lesão corporal seguida de morte e passa a ser homicídio.', 'C',
  'O § 3º do art. 129 exige que o agente **não tenha assumido o risco** do resultado; havendo dolo eventual, aplica-se o art. 18, I (homicídio).',
  lei=[DOLO], kw=['assumiu o risco', 'homicídio'])
I(P, 2, 'Preterdolo e hediondez',
  'A lesão corporal seguida de morte é sempre crime hediondo, por ter resultado morte.', 'E',
  'Só é hedionda nas hipóteses do art. 1º, I-A, da Lei 8.072/1990 (contra agentes de segurança, membros do Judiciário/MP etc., ou nas dependências de instituição de ensino), na redação da Lei 15.159/2025.',
  lei=[('L8072:1', 'lesão corporal dolosa de natureza gravíssima (art. 129, § 2º) e lesão corporal seguida de morte (art. 129, § 3º), quando praticadas:', None, 'Lei 8.072/1990, art. 1º, I-A')],
  peg='Ver hediondez em todo resultado morte.', kw=['hediondo', 'I-A'])

# ======================= PEN-4.3 · Erro de tipo =======================
P = 'DBA26-PEN-4.3'
I(P, 1, 'Erro de tipo essencial',
  'O erro sobre elemento constitutivo do tipo legal exclui o dolo, mas permite a punição por crime culposo, se previsto em lei.', 'C',
  'Art. 20, caput. Se **invencível**: exclui dolo e culpa (atipicidade). Se **vencível**: exclui o dolo, restando culpa se houver tipo culposo.',
  lei=[ERRO_TIPO], kw=['erro de tipo', 'exclui o dolo'])
I(P, 1, 'Erro de tipo invencível',
  'O erro de tipo inevitável exclui apenas o dolo, subsistindo sempre a responsabilização a título de culpa.', 'E',
  'O erro **invencível** exclui **dolo e culpa**. A culpa só subsiste no erro **vencível** e se houver previsão do crime culposo.',
  lei=[ERRO_TIPO], peg='Manter a culpa no erro invencível.', kw=['invencível', 'dolo e culpa'])
I(P, 1, 'Erro sobre a pessoa',
  'No erro sobre a pessoa, consideram-se as condições ou qualidades da vítima efetivamente atingida, e não as da pessoa que o agente queria atingir.', 'E',
  'É o contrário: no **error in persona** consideram-se as qualidades da **vítima virtual** (pretendida), art. 20, § 3º.',
  lei=[(CP + '20', 'O erro quanto à pessoa contra a qual o crime é praticado não isenta de pena.', 'senão as da pessoa contra quem o agente queria praticar o crime', 'CP, art. 20, § 3º')],
  peg='Trocar vítima virtual por vítima real.', kw=['error in persona', 'vítima virtual'])
I(P, 1, 'Erro provocado por terceiro',
  'No erro determinado por terceiro, só responde pelo crime quem foi induzido em erro, por ter praticado a conduta.', 'E',
  'Art. 20, § 2º: responde pelo crime o **terceiro que determina o erro** (**autor mediato**); o provocado só responde se agiu com culpa e houver tipo culposo.',
  lei=[(CP + '20', 'Responde pelo crime o terceiro que determina o erro.', None, 'CP, art. 20, § 2º')],
  kw=['terceiro que determina o erro', 'autor mediato'])
I(P, 1, 'Descriminante putativa por erro de tipo',
  'É isento de pena quem, por erro plenamente justificado pelas circunstâncias, supõe situação de fato que, se existisse, tornaria a ação legítima.', 'C',
  'Art. 20, § 1º: **descriminante putativa** sobre os pressupostos fáticos (ex.: legítima defesa putativa). O CP adotou aqui a **teoria limitada da culpabilidade** (item 17 da Exposição de Motivos).',
  lei=[(CP + '20', 'É isento de pena quem, por erro plenamente justificado pelas circunstâncias', 'tornaria a ação legítima', 'CP, art. 20, § 1º, 1ª parte')],
  kw=['descriminante putativa', 'teoria limitada da culpabilidade'])
I(P, 1, 'Aberratio criminis',
  'Se, por erro na execução, sobrevém resultado diverso do pretendido, o agente responde por culpa, se o fato é previsto como crime culposo.', 'C',
  'É a **aberratio criminis** (resultado diverso do pretendido), art. 74; se ocorre também o resultado pretendido, concurso formal.',
  lei=[(CP + '74', 'quando, por acidente ou erro na execução do crime, sobrevém resultado diverso do pretendido', 'se o fato é previsto como crime culposo', 'CP, art. 74')],
  kw=['aberratio criminis', 'resultado diverso'])
# --- PEN-4.3 · Rodada 2
I(P, 2, 'Aberratio ictus',
  'Na aberratio ictus, o agente, por acidente ou erro no uso dos meios de execução, atinge pessoa diversa da pretendida e responde como se tivesse praticado o crime contra a pessoa visada.', 'C',
  'Art. 73, que remete ao § 3º do art. 20 (qualidades da vítima virtual).',
  lei=[(CP + '73', 'Quando, por acidente ou erro no uso dos meios de execução', 'atendendo-se ao disposto no § 3º do art. 20 deste Código', 'CP, art. 73, 1ª parte')],
  kw=['aberratio ictus', 'erro na execução'])
I(P, 2, 'Erro sobre o objeto',
  'O erro sobre o objeto (error in objecto), como subtrair um relógio de latão pensando ser de ouro, exclui o dolo do furto.', 'E',
  'É **erro acidental**: recai sobre dado irrelevante para o tipo; o agente responde pelo furto normalmente. Só o erro **essencial** (art. 20) exclui o dolo.',
  lei=[ERRO_TIPO], peg='Dar efeito de erro essencial ao erro acidental.', kw=['erro acidental', 'error in objecto'])
I(P, 2, 'Aberratio criminis e resultado mais grave',
  'Se o agente atira uma pedra para quebrar uma vitrine e, por erro, atinge pessoa, que se fere, responde por lesão corporal culposa, absorvido o dano tentado se não houver resultado pretendido.', 'C',
  'Na **aberratio criminis** (pessoa no lugar da coisa) responde-se pelo resultado diverso a título de **culpa** (art. 74). A doutrina ressalva que, se o resultado produzido for menos grave que o pretendido (coisa no lugar da pessoa), prevalece a tentativa do crime visado.',
  lei=[(CP + '74', 'o agente responde por culpa, se o fato é previsto como crime culposo', None, 'CP, art. 74')],
  kw=['aberratio criminis', 'culpa'])

# ======================= PEN-4.4 · Classificação jurídica dos crimes =======================
P = 'DBA26-PEN-4.4'
I(P, 1, 'Crime formal',
  'Crime formal é aquele cujo tipo descreve conduta e resultado naturalístico, mas a consumação ocorre com a conduta, independentemente do resultado.', 'C',
  'Ex.: **extorsão** — consuma-se independentemente da obtenção da vantagem (Súmula 96/STJ).',
  juris=[J['S96']], kw=['crime formal', 'Súmula 96/STJ'])
I(P, 1, 'Crime de mera conduta',
  'O crime de mera conduta é aquele em que o resultado naturalístico está descrito no tipo, mas é dispensável para a consumação.', 'E',
  'Essa definição é a do crime **formal**. No de **mera conduta** o tipo **não descreve** resultado naturalístico algum (ex.: violação de domicílio, ato obsceno).',
  lei=[(CP + '233', 'Praticar ato obsceno em lugar público, ou aberto ou exposto ao público', None, 'CP, art. 233')],
  peg='Trocar formal por mera conduta.', kw=['mera conduta', 'formal'])
I(P, 1, 'Crime próprio x de mão própria',
  'O crime de mão própria, como o falso testemunho, só pode ser praticado pessoalmente pelo agente, não admitindo coautoria, embora admita participação.', 'C',
  'Nos **crimes de mão própria** a execução é personalíssima; já os **crimes próprios** (ex.: peculato) admitem coautoria e participação de terceiros, comunicando-se a elementar (art. 30).',
  lei=[(CP + '342', 'O fato deixa de ser punível se, antes da sentença no processo em que ocorreu o ilícito, o agente se retrata ou declara a verdade.', None, 'CP, art. 342, § 2º')],
  kw=['crime de mão própria', 'participação'])
I(P, 1, 'Crime plurissubjetivo',
  'A associação criminosa é crime plurissubjetivo que se configura com a associação estável de duas ou mais pessoas.', 'E',
  'O art. 288 exige **3 (três) ou mais pessoas** para o fim específico de cometer crimes — crime **plurissubjetivo** (de concurso necessário).',
  lei=[(CP + '288', 'Associarem-se 3 (três) ou mais pessoas, para o fim específico de cometer crimes', None, 'CP, art. 288, caput')],
  kw=['plurissubjetivo', 'concurso necessário'])
I(P, 1, 'Crime habitual',
  'O crime habitual admite tentativa, pois cada ato isolado já configura o delito.', 'E',
  'No **crime habitual** o ato isolado é **atípico**; só a reiteração configura o crime. Por isso a doutrina majoritária **não admite tentativa**.',
  lei=[TENT], peg='Tratar ato isolado do crime habitual como crime.', kw=['crime habitual', 'reiteração'])
I(P, 1, 'Fraude à licitação: crime formal',
  'Para o STJ, o crime de fraude à licitação é material e exige prova do prejuízo ao erário.', 'E',
  'A **Súmula 645/STJ** diz que é crime **formal**: a consumação prescinde de prejuízo ou de vantagem.',
  juris=[J['S645']], peg='Exigir prejuízo em crime formal.', kw=['Súmula 645/STJ', 'formal'])
# --- PEN-4.4 · Rodada 2
I(P, 2, 'Crime instantâneo de efeitos permanentes',
  'O homicídio é crime instantâneo de efeitos permanentes, porque a consumação se dá em um momento, mas seus efeitos perduram.', 'C',
  'Diferente do **permanente**, cuja consumação se prolonga (sequestro) — relevante para a prescrição (art. 111, III) e a Súmula 711/STF.',
  lei=[(CP + '111', 'nos crimes permanentes, do dia em que cessou a permanência', None, 'CP, art. 111, III')],
  kw=['instantâneo de efeitos permanentes', 'permanente'])
I(P, 2, 'Crime exaurido',
  'Crime exaurido é aquele em que, após a consumação, o agente prossegue lesando o bem jurídico, o que pode influir na dosimetria como consequência do crime.', 'C',
  'Ex.: na extorsão (formal), obter a vantagem é **exaurimento**. As **consequências do crime** entram na pena-base (art. 59).',
  lei=[(CP + '59', 'às circunstâncias e conseqüências do crime', None, 'CP, art. 59, caput')], juris=[J['S96']],
  kw=['exaurimento', 'consequências do crime'])
I(P, 2, 'Crime de atentado',
  'Nos chamados crimes de atentado, a forma tentada recebe a mesma pena da consumada, sem a redução do art. 14, parágrafo único.', 'C',
  'É a ressalva "**salvo disposição em contrário**" do art. 14, par. ún. Ex.: evasão mediante violência (art. 352: "evadir-se ou tentar evadir-se").',
  lei=[PENA_TENT, (CP + '352', 'Evadir-se ou tentar evadir-se o preso', None, 'CP, art. 352')],
  kw=['crime de atentado', 'salvo disposição em contrário'])

# ======================= PEN-4.5 · Crimes comissivos e omissivos =======================
P = 'DBA26-PEN-4.5'
I(P, 1, 'Omissivo próprio',
  'Crime omissivo próprio é aquele em que o tipo descreve uma omissão, consumando-se com a simples abstenção, como a omissão de socorro.', 'C',
  'Art. 135 do CP: "Deixar de prestar assistência". Não admite tentativa, segundo a doutrina.',
  lei=[(CP + '135', 'Deixar de prestar assistência, quando possível fazê-lo sem risco pessoal', None, 'CP, art. 135, caput')],
  kw=['omissivo próprio', 'abstenção'])
I(P, 1, 'Omissivo impróprio',
  'Nos crimes omissivos impróprios, o tipo legal descreve expressamente uma conduta omissiva.', 'E',
  'Nos **omissivos impróprios** (comissivos por omissão) o tipo é **comissivo** (ex.: "matar"); a omissão é punida por força da norma de extensão do art. 13, § 2º (garantidor).',
  lei=[(CP + '13', 'A omissão é penalmente relevante quando o omitente devia e podia agir para evitar o resultado.', None, 'CP, art. 13, § 2º')],
  peg='Atribuir ao omissivo impróprio tipo omissivo.', kw=['comissivos por omissão', 'garantidor'])
I(P, 1, 'Garantidor por lei',
  'A mãe que deixa, dolosamente, de alimentar o filho recém-nascido, que morre por inanição, responde por homicídio doloso por omissão.', 'C',
  'Tem **por lei** dever de cuidado e proteção (art. 13, § 2º, a): é garantidora e o resultado lhe é imputado.',
  lei=[(CP + '13', 'tenha por lei obrigação de cuidado, proteção ou vigilância', None, 'CP, art. 13, § 2º, a')],
  kw=['garantidora', 'por lei'])
I(P, 1, 'Garantidor contratual',
  'Só é garantidor quem tem o dever de agir imposto por lei, não bastando a assunção voluntária da responsabilidade de impedir o resultado.', 'E',
  'O art. 13, § 2º, b, inclui quem "**de outra forma, assumiu a responsabilidade** de impedir o resultado" (ex.: babá, salva-vidas contratado, guia).',
  lei=[(CP + '13', 'de outra forma, assumiu a responsabilidade de impedir o resultado', None, 'CP, art. 13, § 2º, b')],
  peg='Reduzir as fontes do dever de garantidor à lei.', kw=['assumiu a responsabilidade'])
I(P, 1, 'Omissão de socorro majorada',
  'Na omissão de socorro, o resultado morte não altera a pena do omitente, por ser crime omissivo próprio.', 'E',
  'O resultado não é imputado como homicídio, mas **majora** a pena: aumenta de metade se resulta lesão grave e **triplica** se resulta morte (art. 135, par. ún.).',
  lei=[(CP + '135', 'A pena é aumentada de metade, se da omissão resulta lesão corporal de natureza grave, e triplicada, se resulta a morte.', None, 'CP, art. 135, par. ún.')],
  peg='Ignorar a majorante pelo resultado.', kw=['triplicada', 'omissão de socorro'])
# --- PEN-4.5 · Rodada 2
I(P, 2, 'Tentativa no omissivo impróprio',
  'Os crimes omissivos impróprios admitem tentativa, pois o resultado naturalístico pode não ocorrer por circunstâncias alheias à vontade do omitente.', 'C',
  'Ex.: a mãe que deixa de alimentar o filho para matá-lo, mas a criança é salva por vizinhos — tentativa de homicídio (art. 14, II).',
  lei=[TENT], kw=['tentativa', 'omissivo impróprio'])
I(P, 2, 'Participação por omissão',
  'Admite-se participação por omissão de quem tinha o dever jurídico de impedir o resultado, como o policial que presencia o roubo e nada faz para impedi-lo.', 'C',
  'Quem é **garantidor** (art. 13, § 2º) e se omite contribui para o crime; a doutrina discute se é coautoria ou participação, mas há responsabilização. A CF, para hediondos, alcança "os que, podendo evitá-los, se omitirem" (art. 5º, XLIII).',
  lei=[('CF:5', 'por eles respondendo os mandantes, os executores e os que, podendo evitá-los, se omitirem', None, 'CF, art. 5º, XLIII, parte final')],
  kw=['participação por omissão', 'garantidor'])
I(P, 2, 'Omissão e risco pessoal',
  'O crime de omissão de socorro se configura mesmo que prestar assistência implicasse risco pessoal ao omitente, já que o dever de solidariedade é absoluto.', 'E',
  'O tipo exige que fosse "**possível fazê-lo sem risco pessoal**" (art. 135). Havendo risco, o omitente deve ao menos pedir socorro à autoridade pública.',
  lei=[(CP + '135', 'Deixar de prestar assistência, quando possível fazê-lo sem risco pessoal', None, 'CP, art. 135, caput')],
  peg='Apagar o "sem risco pessoal".', kw=['sem risco pessoal'])

# ======================= PEN-4.6 · Crimes de dano e de perigo =======================
P = 'DBA26-PEN-4.6'
I(P, 1, 'Crime de dano',
  'O crime de dano consuma-se com a mera exposição do bem jurídico a perigo, dispensando a lesão efetiva.', 'E',
  'Isso define o crime de perigo. O **crime de dano** exige **efetiva lesão** ao bem jurídico (homicídio, furto).',
  lei=[(CP + '155', 'Subtrair, para si ou para outrem, coisa alheia móvel', None, 'CP, art. 155, caput')],
  kw=['crime de dano', 'efetiva lesão'])
I(P, 1, 'Perigo concreto',
  'Nos crimes de perigo concreto, o perigo é presumido pela lei, dispensando-se a prova de que alguém foi efetivamente exposto a risco.', 'E',
  'Isso é o perigo **abstrato**. No **perigo concreto** é preciso **provar** a situação de risco a pessoa determinada (ex.: art. 132 — "perigo direto e iminente").',
  lei=[(CP + '132', 'Expor a vida ou a saúde de outrem a perigo direto e iminente', None, 'CP, art. 132, caput')],
  peg='Trocar perigo concreto por abstrato.', kw=['perigo concreto', 'perigo abstrato'])
I(P, 1, 'Perigo individual e comum',
  'Crimes de perigo comum (ou coletivo) expõem a risco número indeterminado de pessoas, como o incêndio.', 'C',
  'Título VIII do CP ("Dos crimes contra a incolumidade pública"): art. 250 (incêndio) expõe a perigo a vida, a integridade ou o patrimônio **de outrem** indeterminado.',
  lei=[(CP + '250', 'Causar incêndio, expondo a perigo a vida, a integridade física ou o patrimônio de outrem', None, 'CP, art. 250, caput')],
  kw=['perigo comum', 'incêndio'])
I(P, 1, 'Perigo e subsidiariedade',
  'O crime de perigo para a vida ou saúde de outrem é expressamente subsidiário, aplicando-se só se o fato não constituir crime mais grave.', 'C',
  'Art. 132: "se o fato não constitui crime mais grave".',
  lei=[(CP + '132', 'se o fato não constitui crime mais grave', None, 'CP, art. 132, caput')],
  kw=['subsidiário'])
I(P, 1, 'Agravante de perigo comum',
  'Constitui agravante genérica ter o agente cometido o crime com emprego de meio de que podia resultar perigo comum.', 'C',
  'Art. 61, II, d, do CP — desde que não constitua ou qualifique o crime.',
  lei=[(CP + '61', 'ou de que podia resultar perigo comum', None, 'CP, art. 61, II, d')],
  kw=['perigo comum', 'agravante'])
# --- PEN-4.6 · Rodada 2
I(P, 2, 'Perigo abstrato e constitucionalidade',
  'No crime de perigo abstrato, a acusação precisa provar que, no caso concreto, pessoa determinada foi efetivamente exposta a risco.', 'E',
  'No **perigo abstrato** o perigo é **presumido** pelo legislador a partir da conduta; a prova de risco a pessoa determinada é exigência do **perigo concreto** (ex.: art. 132, "perigo direto e iminente").',
  lei=[(CP + '132', 'Expor a vida ou a saúde de outrem a perigo direto e iminente', None, 'CP, art. 132, caput')],
  peg='Exigir no abstrato a prova do concreto.', kw=['perigo abstrato', 'presumido'])
I(P, 2, 'Perigo concreto e dolo',
  'Nos crimes de perigo, o dolo se dirige à exposição do bem a risco, sem que o agente deseje a lesão efetiva.', 'C',
  'É o **dolo de perigo**. Se o agente quiser o dano, responde pelo crime de dano correspondente (tentado ou consumado). Base: art. 18, I, e a subsidiariedade do art. 132.',
  lei=[DOLO], kw=['dolo de perigo'])
I(P, 2, 'Tentativa nos crimes de perigo',
  'Os crimes de perigo concreto comissivos, por serem plurissubsistentes, admitem tentativa, segundo parte da doutrina.', 'C',
  'Quando a conduta é fracionável e o perigo não se concretiza por circunstâncias alheias, pode haver **tentativa** (art. 14, II); o tema é controvertido na doutrina.',
  lei=[TENT], kw=['tentativa', 'plurissubsistentes'])

# ======================= PEN-4.7 · Causas de extinção da punibilidade =======================
P = 'DBA26-PEN-4.7'
I(P, 1, 'Morte do agente',
  'A morte do agente extingue a punibilidade, mas a pena de multa já aplicada pode ser cobrada dos herdeiros, até as forças da herança.', 'E',
  'Art. 107, I: a **multa** é pena e não passa da pessoa do condenado (CF, art. 5º, XLV). Com a **morte do agente**, só a obrigação civil de reparar o dano se transmite.',
  lei=[(CP + '107', 'pela morte do agente', None, 'CP, art. 107, I'),
       ('CF:5', 'nenhuma pena passará da pessoa do condenado', None, 'CF, art. 5º, XLV')],
  kw=['morte do agente', 'multa'])
I(P, 1, 'Anistia, graça e indulto',
  'A anistia, a graça e o indulto são concedidos pelo Presidente da República por decreto.', 'E',
  'A **anistia** é concedida por **lei** do Congresso Nacional e apaga o fato (efeitos penais); **graça** (individual) e **indulto** (coletivo) são atos do **Presidente**. Todas extinguem a punibilidade (art. 107, II).',
  lei=[(CP + '107', 'pela anistia, graça ou indulto', None, 'CP, art. 107, II')],
  peg='Atribuir a anistia ao Presidente.', kw=['anistia', 'lei'])
I(P, 1, 'Retratação',
  'A retratação do agente extingue a punibilidade nos casos em que a lei a admite, como na calúnia e na difamação, antes da sentença.', 'C',
  'Art. 107, VI, e art. 143 do CP (não cabe na **injúria**). Também no falso testemunho (art. 342, § 2º).',
  lei=[(CP + '107', 'pela retratação do agente, nos casos em que a lei a admite', None, 'CP, art. 107, VI'),
       (CP + '143', 'O querelado que, antes da sentença, se retrata cabalmente da calúnia ou da difamação, fica isento de pena.', None, 'CP, art. 143, caput')],
  exc=['Injúria não admite retratação (CP, art. 143)'], kw=['retratação', 'calúnia ou da difamação'])
I(P, 1, 'Renúncia e perdão',
  'A renúncia ao direito de queixa e o perdão aceito extinguem a punibilidade tanto na ação privada quanto na ação pública condicionada.', 'E',
  'O art. 107, V, restringe-se aos **crimes de ação privada**. Na pública condicionada há **retratação da representação** (até a denúncia, art. 102), não perdão.',
  lei=[(CP + '107', 'pela renúncia do direito de queixa ou pelo perdão aceito, nos crimes de ação privada', None, 'CP, art. 107, V')],
  peg='Estender perdão à ação pública.', kw=['ação privada', 'perdão aceito'])
I(P, 1, 'Abolitio criminis',
  'Extingue-se a punibilidade pela retroatividade de lei que não mais considera o fato como criminoso.', 'C',
  'Art. 107, III, combinado com o art. 2º, caput.',
  lei=[(CP + '107', 'pela retroatividade de lei que não mais considera o fato como criminoso', None, 'CP, art. 107, III')],
  kw=['abolitio criminis'])
I(P, 1, 'Casamento com a vítima',
  'O casamento do agente com a vítima nos crimes contra a dignidade sexual continua sendo causa de extinção da punibilidade.', 'E',
  'Os incisos VII e VIII do art. 107 foram **revogados** pela Lei 11.106/2005.',
  lei=[(CP + '107', 'VII - (Revogado pela Lei nº 11.106, de 2005)', None, 'CP, art. 107, VII')],
  peg='Ressuscitar causa revogada.', kw=['revogados', 'Lei 11.106/2005'])
# --- PEN-4.7 · Rodada 2
I(P, 2, 'Indulto e efeitos secundários',
  'O indulto extingue os efeitos primários da condenação, mas não atinge os efeitos secundários, penais ou extrapenais, como a reincidência.', 'C',
  '**Súmula 631/STJ**. A anistia, ao contrário, apaga os efeitos penais.',
  juris=[J['S631']], kw=['Súmula 631/STJ', 'efeitos secundários'])
I(P, 2, 'Perempção',
  'A perempção extingue a punibilidade também na ação penal privada subsidiária da pública, quando o querelante abandona o processo.', 'E',
  'Na **subsidiária**, a negligência do querelante faz o MP **retomar a ação como parte principal** (CPP, art. 29): não há **perempção**, causa própria da ação privada propriamente dita (art. 107, IV).',
  lei=[(CP + '107', 'pela prescrição, decadência ou perempção', None, 'CP, art. 107, IV'),
       ('CPP:29', 'retomar a ação como parte principal', None, 'CPP, art. 29')],
  kw=['perempção', 'subsidiária'])
I(P, 2, 'Perdão judicial: rol aberto',
  'O juiz pode conceder perdão judicial em qualquer crime, sempre que entender a pena desnecessária.', 'E',
  'O perdão judicial só cabe "**nos casos previstos em lei**" (art. 107, IX), como no homicídio culposo (art. 121, § 5º).',
  lei=[(CP + '107', 'pelo perdão judicial, nos casos previstos em lei', None, 'CP, art. 107, IX')],
  peg='Generalizar o perdão judicial.', kw=['casos previstos em lei'])
I(P, 2, 'Pagamento do cheque',
  'Pela Súmula 554 do STF, o pagamento de cheque emitido sem fundos após o recebimento da denúncia não obsta ao prosseguimento da ação penal.', 'C',
  'Lida a contrario sensu, a súmula indica que o pagamento **antes** do recebimento da denúncia obsta a ação penal.',
  juris=[J['STF554']], kw=['Súmula 554/STF', 'recebimento da denúncia'])

# ======================= PEN-4.8 · Iter criminis =======================
P = 'DBA26-PEN-4.8'
I(P, 1, 'Fases do iter criminis',
  'O iter criminis compreende cogitação, preparação, execução e consumação; a cogitação nunca é punível.', 'C',
  'Pela **exteriorização do fato**, o pensamento não é punido. A preparação, em regra, também não (art. 31), e a punição começa com a execução (art. 14, II).',
  lei=[TENT], kw=['iter criminis', 'cogitação'])
I(P, 1, 'Atos preparatórios',
  'Os atos preparatórios são sempre impuníveis no direito brasileiro.', 'E',
  'Em regra são impuníveis, mas a lei pode tipificá-los como **crimes autônomos** (ex.: associação criminosa, art. 288; petrechos para falsificação de moeda, art. 291).',
  lei=[(CP + '288', 'Associarem-se 3 (três) ou mais pessoas, para o fim específico de cometer crimes', None, 'CP, art. 288, caput')],
  peg='"Sempre" impuníveis.', kw=['atos preparatórios', 'crimes autônomos'])
I(P, 1, 'Ajuste e instigação',
  'O ajuste, a determinação ou instigação e o auxílio, salvo disposição expressa em contrário, não são puníveis se o crime não chega, pelo menos, a ser tentado.', 'C',
  'Art. 31 do CP: a participação depende do início da execução pelo autor (**acessoriedade**).',
  lei=[(CP + '31', 'O ajuste, a determinação ou instigação e o auxílio, salvo disposição expressa em contrário', 'pelo menos, a ser tentado', 'CP, art. 31')],
  kw=['acessoriedade', 'ajuste'])
I(P, 1, 'Início da execução',
  'Pela teoria objetivo-formal, o início da execução ocorre quando o agente começa a praticar o núcleo do tipo.', 'C',
  'A **teoria objetivo-formal** é a tradicionalmente apontada como adotada (CP, art. 14, II, "iniciada a execução"). A objetivo-individual (plano do autor) ganha espaço na doutrina.',
  lei=[TENT], kw=['teoria objetivo-formal', 'núcleo do tipo'])
I(P, 1, 'Exaurimento',
  'O exaurimento integra o iter criminis como fase posterior à consumação e é, em regra, indispensável para a configuração do crime.', 'E',
  'O **exaurimento** é posterior à consumação e **irrelevante** para a existência do crime; pode influir na pena (consequências, art. 59) — ex.: obter a vantagem na extorsão (Súmula 96/STJ).',
  juris=[J['S96']], peg='Fazer depender o crime do exaurimento.', kw=['exaurimento'])
# --- PEN-4.8 · Rodada 2
I(P, 2, 'Crime impossível e iter',
  'Nos casos de crime impossível, a tentativa não é punida porque, embora haja início de execução, o meio ou o objeto tornam absolutamente impossível a consumação.', 'C',
  'Art. 17: **tentativa inidônea**, impunível.',
  lei=[IMPOSS], kw=['tentativa inidônea'])
I(P, 2, 'Participação e crime não tentado',
  'O partícipe que instiga alguém a matar responde por tentativa de homicídio se o instigado desiste antes de iniciar a execução.', 'E',
  'Sem início de execução, o **ajuste ou instigação** não é punível (art. 31). Não há tentativa de participação.',
  lei=[(CP + '31', 'não são puníveis, se o crime não chega, pelo menos, a ser tentado', None, 'CP, art. 31')],
  peg='Punir a instigação sem execução.', kw=['não são puníveis'])
I(P, 2, 'Petrechos como crime autônomo',
  'A punição de atos preparatórios como crimes autônomos é exceção legítima à regra da impunidade da preparação, desde que prevista em lei.', 'C',
  'A lei pode punir a **preparação** como **crime autônomo**: art. 291 do CP (petrechos para falsificação de moeda) e o próprio "salvo disposição expressa em contrário" do art. 31.',
  lei=[(CP + '291', 'Fabricar, adquirir, fornecer, a título oneroso ou gratuito, possuir ou guardar maquinismo', None, 'CP, art. 291')],
  kw=['crime autônomo', 'preparação'])

# ======================= PEN-4.9 · Consumação e tentativa =======================
P = 'DBA26-PEN-4.9'
I(P, 1, 'Crime consumado',
  'Diz-se o crime consumado quando o agente obtém o proveito pretendido, ainda que nem todos os elementos do tipo estejam presentes.', 'E',
  'Art. 14, I: **consumado** quando se reúnem **todos os elementos de sua definição legal**; obter o proveito é exaurimento.',
  lei=[(CP + '14', 'consumado, quando nele se reúnem todos os elementos de sua definição legal', None, 'CP, art. 14, I')],
  kw=['consumado', 'definição legal'])
I(P, 1, 'Pena da tentativa',
  'Salvo disposição em contrário, pune-se a tentativa com a pena do crime consumado, diminuída de um sexto a dois terços.', 'E',
  'A redução da tentativa é de **um a dois terços** (art. 14, par. ún.). "Um sexto a um terço" é a do erro de proibição evitável e da participação de menor importância.',
  lei=[PENA_TENT], peg='Trocar as frações.', kw=['um a dois terços'])
I(P, 1, 'Critério da redução',
  'O quantum de redução pela tentativa é graduado pela proximidade da consumação: quanto mais perto, menor a diminuição.', 'C',
  'Critério consolidado: **iter criminis percorrido**. Tentativa branca (sem lesão) tende a redução maior; cruenta próxima da consumação, menor.',
  lei=[PENA_TENT], kw=['iter criminis percorrido'])
I(P, 1, 'Tentativa de contravenção',
  'A tentativa de contravenção é punida com a pena da contravenção consumada diminuída de um a dois terços.', 'E',
  'Pela LCP, **não é punível** a tentativa de contravenção (art. 4º).',
  lei=[('DL3688:4', 'Não é punível a tentativa de contravenção.', None, 'LCP, art. 4º')],
  peg='Aplicar o art. 14 à contravenção.', kw=['tentativa de contravenção'])
I(P, 1, 'Consumação do roubo',
  'O roubo se consuma com a inversão da posse do bem mediante violência ou grave ameaça, ainda que por breve tempo, sendo prescindível a posse mansa e pacífica.', 'C',
  'Teoria da **amotio** (apprehensio): **Súmula 582/STJ**.',
  juris=[J['S582']], kw=['Súmula 582/STJ', 'inversão da posse'])
I(P, 1, 'Tentativa branca',
  'Tentativa branca (ou incruenta) é aquela em que o objeto material não é atingido.', 'C',
  'Classificação doutrinária; se atingido, a tentativa é **cruenta** (vermelha). A pena segue o art. 14, par. ún.',
  lei=[PENA_TENT], kw=['tentativa branca', 'cruenta'])
# --- PEN-4.9 · Rodada 2
I(P, 2, 'Teoria objetiva da tentativa',
  'Quanto à punibilidade da tentativa, o Código Penal adotou como regra a teoria subjetiva, punindo-a com a mesma pena do crime consumado.', 'E',
  'A regra é a **teoria objetiva** (realística): pena reduzida pelo menor desvalor do resultado. A subjetiva aparece só por exceção nos **crimes de atentado** ("salvo disposição em contrário").',
  lei=[PENA_TENT], peg='Inverter regra e exceção.', kw=['teoria objetiva', 'crimes de atentado'])
I(P, 2, 'Infrações que não admitem tentativa',
  'Não admitem tentativa, em regra, os crimes culposos, os preterdolosos, os omissivos próprios, os unissubsistentes e as contravenções.', 'C',
  'Mnemônico doutrinário (CCHOUP: culposos, contravenções, habituais, omissivos próprios, unissubsistentes, preterdolosos); nas contravenções a vedação é legal (LCP, art. 4º).',
  lei=[('DL3688:4', 'Não é punível a tentativa de contravenção.', None, 'LCP, art. 4º')],
  kw=['não admitem tentativa', 'unissubsistentes'])
I(P, 2, 'Tentativa e dolo eventual',
  'A tentativa é compatível com o dolo eventual, segundo a posição majoritária da doutrina.', 'C',
  'Quem assume o risco do resultado também "quer" na forma do art. 18, I; se o resultado não ocorre por circunstâncias alheias, há tentativa (art. 14, II). O tema é discutido, mas a doutrina majoritária admite.',
  lei=[DOLO, TENT], kw=['dolo eventual', 'tentativa'])
I(P, 2, 'Vigilância e consumação do furto',
  'O furto praticado sob monitoramento eletrônico de câmeras do supermercado é sempre crime impossível, por ineficácia absoluta do meio.', 'E',
  'A **Súmula 567/STJ** diz que a vigilância, **por si só**, não torna impossível o furto: a ineficácia é relativa, e há tentativa (ou consumação).',
  juris=[J['S567']], peg='Ver crime impossível em toda vigilância.', kw=['Súmula 567/STJ', 'por si só'])

# ======================= PEN-4.10 · Desistência voluntária e arrependimento eficaz =======================
P = 'DBA26-PEN-4.10'
I(P, 1, 'Desistência voluntária',
  'Na desistência voluntária, o agente, podendo prosseguir na execução, interrompe-a por vontade própria e responde apenas pelos atos já praticados.', 'C',
  'Art. 15, 1ª parte. Fórmula de Frank: "**posso, mas não quero**" (desistência); "quero, mas não posso" (tentativa).',
  lei=[DESIST], kw=['desistência voluntária', 'fórmula de Frank'])
I(P, 1, 'Voluntariedade x espontaneidade',
  'A desistência voluntária exige espontaneidade, de modo que não se aplica se o agente desistiu por conselho de terceiro.', 'E',
  'Basta a **voluntariedade** (ausência de coação); **não se exige espontaneidade** — a desistência sugerida por outrem vale, desde que o agente a decida livremente.',
  lei=[DESIST], peg='Exigir espontaneidade.', kw=['voluntariedade', 'espontaneidade'])
I(P, 1, 'Arrependimento eficaz',
  'No arrependimento eficaz, o agente, já esgotados os atos executórios, age para impedir que o resultado se produza; se consegue, responde só pelos atos praticados.', 'C',
  'Art. 15, 2ª parte. Se o resultado ocorrer mesmo assim, o arrependimento é **ineficaz** e responde pelo crime consumado (pode ter atenuante do art. 65, III, b).',
  lei=[DESIST], kw=['arrependimento eficaz', 'atos executórios'])
I(P, 1, 'Natureza jurídica',
  'Para a corrente majoritária, desistência voluntária e arrependimento eficaz são causas de exclusão da tipicidade do crime tentado, chamadas de "ponte de ouro".', 'C',
  'A **ponte de ouro** afasta a tentativa (tipicidade da forma tentada); há quem as veja como causas pessoais de extinção da punibilidade — divergência doutrinária.',
  lei=[DESIST], kw=['ponte de ouro', 'tentativa abandonada'])
I(P, 1, 'Desistência e circunstâncias alheias',
  'Há desistência voluntária quando o agente interrompe o furto ao perceber que o alarme disparou e a polícia se aproxima.', 'E',
  'Aí a interrupção decorre de **circunstância alheia** (medo de ser preso pela polícia que chega): é **tentativa** (art. 14, II), não desistência.',
  lei=[TENT], peg='Confundir fuga diante da polícia com desistência.', kw=['circunstância alheia', 'tentativa'])
I(P, 1, 'Resposta pelos atos praticados',
  'Quem desiste voluntariamente de matar depois de ferir a vítima responde por tentativa de homicídio, com a pena reduzida.', 'E',
  'Responde só pelos **atos já praticados** (art. 15): **lesão corporal**. A desistência voluntária afasta a tentativa (ponte de ouro).',
  lei=[DESIST], kw=['atos já praticados', 'lesão corporal'])
# --- PEN-4.10 · Rodada 2
I(P, 2, 'Comunicabilidade ao partícipe',
  'A desistência voluntária do autor aproveita ao partícipe, já que, sem tentativa punível, não há fato principal a que acessar.', 'C',
  'Pela **acessoriedade** (art. 31), sem crime ao menos tentado a participação não é punível; a doutrina majoritária estende o efeito ao partícipe.',
  lei=[(CP + '31', 'não são puníveis, se o crime não chega, pelo menos, a ser tentado', None, 'CP, art. 31')],
  kw=['acessoriedade', 'partícipe'])
I(P, 2, 'Arrependimento eficaz em crime formal',
  'O arrependimento eficaz é plenamente compatível com crimes formais e de mera conduta, já consumados com a ação.', 'E',
  'O arrependimento eficaz pressupõe **evitar o resultado** antes da consumação; nos formais e de mera conduta a consumação já ocorreu com a ação. Só cabe, em regra, nos **materiais**.',
  lei=[DESIST], peg='Aplicar a ponte de ouro a crime já consumado.', kw=['crimes materiais', 'consumação'])
I(P, 2, 'Arrependimento eficaz x posterior',
  'O arrependimento eficaz ocorre antes da consumação; o arrependimento posterior ocorre depois dela e apenas reduz a pena.', 'C',
  'Arts. 15 e 16: o primeiro afasta a tentativa; o segundo é **causa de diminuição** de 1/3 a 2/3.',
  lei=[DESIST, ARREP], kw=['arrependimento eficaz', 'arrependimento posterior'])
I(P, 2, 'Desistência e adiamento',
  'O agente que suspende a execução apenas para retomá-la em momento mais oportuno, com o mesmo plano, configura desistência voluntária.', 'E',
  'Para a doutrina, o **mero adiamento** não é desistência: não há abandono definitivo do propósito; persiste a tentativa se a execução já tinha começado (art. 14, II).',
  lei=[TENT], peg='Chamar de desistência o adiamento.', kw=['mero adiamento'])

# ======================= PEN-4.11 · Arrependimento posterior =======================
P = 'DBA26-PEN-4.11'
I(P, 1, 'Requisitos',
  'Nos crimes cometidos sem violência ou grave ameaça à pessoa, reparado o dano ou restituída a coisa até o recebimento da denúncia ou queixa, por ato voluntário, a pena será reduzida de um a dois terços.', 'C',
  'Art. 16: **causa obrigatória de diminuição** (a pena "será" reduzida).',
  lei=[ARREP], kw=['arrependimento posterior', 'recebimento da denúncia'])
I(P, 1, 'Marco temporal',
  'O arrependimento posterior pode ocorrer até a sentença de primeiro grau.', 'E',
  'O marco é o **recebimento da denúncia ou da queixa** (art. 16). Reparação depois disso e antes do julgamento gera só a **atenuante** do art. 65, III, b.',
  lei=[ARREP, (CP + '65', 'ou ter, antes do julgamento, reparado o dano', None, 'CP, art. 65, III, b')],
  peg='Esticar o prazo até a sentença.', kw=['recebimento da denúncia', 'atenuante'])
I(P, 1, 'Violência contra a coisa',
  'O arrependimento posterior é inaplicável ao furto qualificado pelo rompimento de obstáculo, por haver violência.', 'E',
  'O art. 16 exclui a violência **à pessoa**; a violência contra a **coisa** (rompimento de obstáculo) não impede o benefício.',
  lei=[ARREP], peg='Ler "violência" sem o complemento "à pessoa".', kw=['violência à pessoa', 'rompimento de obstáculo'])
I(P, 1, 'Voluntariedade',
  'A reparação do dano só gera arrependimento posterior se for espontânea, isto é, de iniciativa exclusiva do agente, sem sugestão de terceiros.', 'E',
  'O art. 16 exige **ato voluntário**, não espontâneo: a reparação sugerida pelo advogado ou por familiar vale.',
  lei=[ARREP], kw=['ato voluntário'])
I(P, 1, 'Crime culposo',
  'Admite-se arrependimento posterior em crime culposo, ainda que com resultado violento, como a lesão corporal culposa, segundo a doutrina majoritária.', 'C',
  'A violência vedada é a **dolosamente empregada**; nos culposos a doutrina majoritária admite o benefício.',
  lei=[ARREP], kw=['crime culposo', 'violência dolosa'])
# --- PEN-4.11 · Rodada 2
I(P, 2, 'Peculato culposo',
  'No peculato culposo, a reparação do dano até a sentença irrecorrível extingue a punibilidade; se posterior, reduz de metade a pena imposta.', 'C',
  'Regra **especial** (art. 312, § 3º), mais benéfica que o art. 16.',
  lei=[(CP + '312', 'No caso do parágrafo anterior, a reparação do dano, se precede à sentença irrecorrível, extingue a punibilidade; se lhe é posterior, reduz de metade a pena imposta.', None, 'CP, art. 312, § 3º')],
  kw=['peculato culposo', 'extingue a punibilidade'])
I(P, 2, 'Cheque sem fundos',
  'Pelo STF, o pagamento de cheque sem fundos após o recebimento da denúncia impede o prosseguimento da ação penal.', 'E',
  'A **Súmula 554/STF** diz que o pagamento **após** o recebimento **não obsta** a ação (pode incidir atenuante). Lida a contrario sensu, a súmula indica que o pagamento antes do recebimento obsta a ação.',
  juris=[J['STF554']], peg='Inverter a Súmula 554.', kw=['Súmula 554/STF'])
I(P, 2, 'Natureza jurídica',
  'O arrependimento posterior é causa de extinção da punibilidade quando a reparação do dano é integral e anterior à denúncia.', 'E',
  'É **causa obrigatória de diminuição de pena** (1/3 a 2/3), não de extinção da punibilidade (art. 16). Extinção pela reparação só existe em regras especiais, como o peculato culposo (art. 312, § 3º).',
  lei=[ARREP], peg='Confundir diminuição com extinção da punibilidade.', kw=['causa obrigatória de diminuição'])
I(P, 2, 'Comunicabilidade',
  'Reparado o dano por um dos coautores, a redução do arrependimento posterior estende-se aos demais, por ser circunstância objetiva.', 'C',
  'A doutrina majoritária trata a reparação como **circunstância objetiva**, comunicável aos coautores (art. 30, a contrario).',
  lei=[(CP + '30', 'Não se comunicam as circunstâncias e as condições de caráter pessoal, salvo quando elementares do crime.', None, 'CP, art. 30')],
  kw=['circunstância objetiva', 'comunicável'])

# ======================= PEN-4.12 · Crime impossível =======================
P = 'DBA26-PEN-4.12'
I(P, 1, 'Conceito',
  'Não se pune a tentativa quando, por ineficácia absoluta do meio ou por absoluta impropriedade do objeto, é impossível consumar-se o crime.', 'C',
  'Art. 17: **crime impossível** (tentativa inidônea, crime oco).',
  lei=[IMPOSS], kw=['crime impossível', 'tentativa inidônea'])
I(P, 1, 'Teoria adotada',
  'Quanto ao crime impossível, o Código Penal adotou a teoria objetiva pura, de modo que mesmo a ineficácia relativa do meio torna o fato impunível.', 'E',
  'Adotou a **teoria objetiva temperada**: só a ineficácia **absoluta** do meio ou a impropriedade **absoluta** do objeto afastam a punição. Ineficácia relativa = tentativa punível.',
  lei=[IMPOSS], peg='Trocar temperada por pura.', kw=['objetiva temperada', 'absoluta'])
I(P, 1, 'Impropriedade do objeto',
  'Atirar em pessoa já morta, supondo-a viva, configura crime impossível por absoluta impropriedade do objeto.', 'C',
  'Não há vida a ser tirada: o objeto é **absolutamente impróprio** (art. 17).',
  lei=[IMPOSS], kw=['impropriedade do objeto'])
I(P, 1, 'Flagrante preparado',
  'Não há crime quando a preparação do flagrante pela polícia torna impossível a sua consumação.', 'C',
  'É a **Súmula 145/STF** (flagrante preparado ou provocado = crime impossível).',
  juris=[J['STF145']], kw=['Súmula 145/STF', 'flagrante preparado'])
I(P, 1, 'Flagrante esperado',
  'O flagrante esperado, em que a polícia apenas aguarda a prática do crime sem induzir o agente, também configura crime impossível.', 'E',
  'No **flagrante esperado** não há provocação: o crime é possível, e o flagrante é **válido**. A Súmula 145/STF se aplica ao **preparado**.',
  juris=[J['STF145']], peg='Equiparar flagrante esperado ao preparado.', kw=['flagrante esperado'])
# --- PEN-4.12 · Rodada 2
I(P, 2, 'Vigilância eletrônica',
  'O sistema de vigilância por monitoramento eletrônico ou a presença de seguranças no estabelecimento comercial, por si só, não torna impossível o crime de furto.', 'C',
  '**Súmula 567/STJ**: ineficácia apenas relativa.',
  juris=[J['S567']], kw=['Súmula 567/STJ', 'vigilância'])
I(P, 2, 'Arma desmuniciada no roubo',
  'O uso de arma de fogo desmuniciada para intimidar a vítima de roubo caracteriza crime impossível, por ineficácia absoluta do meio.', 'E',
  'O meio de execução do roubo é a **grave ameaça**, que a arma desmuniciada é plenamente apta a causar: o roubo existe. O debate é só sobre a majorante de arma de fogo.',
  lei=[IMPOSS], peg='Confundir aptidão para ferir com aptidão para intimidar.', kw=['grave ameaça', 'ineficácia absoluta'])
I(P, 2, 'Crime impossível e putativo',
  'No crime putativo por erro de proibição, o agente acredita praticar crime, mas o fato é atípico — diferente do crime impossível, em que o fato seria típico, mas a consumação é inviável.', 'C',
  'Doutrina: o **delito putativo** (imaginário) é impunível por falta de tipo; o **crime impossível** tem tipo, mas falha absoluta do meio ou do objeto (art. 17).',
  lei=[IMPOSS], kw=['crime putativo', 'crime impossível'])
