/* lei_integra_dados.js — dados do módulo "Lei na Íntegra" (aba do Treino de Letra de Lei, 19/11/2026).
 * O ARTIGO INTEIRO (caput + incisos + parágrafos) para estudo em 3 modos (Esconder / Teste / Revisão),
 * todos saindo deste MESMO registro. As palavras-chave vêm marcadas com {chaves}: no Esconder viram lacuna,
 * no Teste aparecem uma a uma, na Revisão ficam grifadas. "imp" marca o que mais cai (ganha "!"); "destaque"
 * é o campeão de pegadinha. "poder" num parágrafo pinta o grifo de ciano.
 * Texto OFICIAL (CF/88, Código Penal e CPP — público); nada de terceiro entra — só a incidência medida
 * orientou a seleção (ver docs/PROCEDENCIA.md). Núcleo do Delegado: Constitucional, Penal e Processo Penal. */
window.LEI_INTEGRA = [

/* ==================== CONSTITUIÇÃO FEDERAL ==================== */
{d:"CF", art:"1º", titulo:"TÍTULO I — DOS PRINCÍPIOS FUNDAMENTAIS", rub:"Fundamentos da República",
 caput:"A República Federativa do Brasil, formada pela {união indissolúvel} dos Estados e Municípios e do Distrito Federal, constitui-se em {Estado Democrático de Direito} e tem como fundamentos:",
 incisos:[
  {n:"I", t:"a {soberania}", imp:true},
  {n:"II", t:"a {cidadania}", imp:true},
  {n:"III", t:"a {dignidade da pessoa humana}", imp:true, destaque:true},
  {n:"IV", t:"os {valores sociais do trabalho} e da livre iniciativa"},
  {n:"V", t:"o {pluralismo político}"}
 ],
 paragrafos:[{rot:"Parágrafo único.", t:"Todo o poder emana do {povo}, que o exerce por meio de representantes eleitos ou diretamente, nos termos desta Constituição.", imp:true, poder:true}],
 mnem:"SO-CI-DI-VA-PLU", base:"CF, art. 1º"},

{d:"CF", art:"2º", titulo:"DOS PRINCÍPIOS FUNDAMENTAIS", rub:"Separação dos Poderes",
 caput:"São Poderes da União, independentes e {harmônicos} entre si, o {Legislativo}, o {Executivo} e o {Judiciário}.",
 incisos:[], paragrafos:[], mnem:"independentes e HARMÔNICOS", base:"CF, art. 2º"},

{d:"CF", art:"3º", titulo:"DOS PRINCÍPIOS FUNDAMENTAIS", rub:"Objetivos fundamentais",
 caput:"Constituem {objetivos fundamentais} da República Federativa do Brasil:",
 incisos:[
  {n:"I", t:"construir uma sociedade {livre, justa e solidária}", imp:true},
  {n:"II", t:"garantir o {desenvolvimento nacional}"},
  {n:"III", t:"erradicar a {pobreza} e a marginalização e reduzir as {desigualdades sociais e regionais}", imp:true, destaque:true},
  {n:"IV", t:"promover o {bem de todos}, sem preconceitos de origem, raça, sexo, cor, idade e quaisquer outras formas de discriminação", imp:true}
 ],
 paragrafos:[], mnem:"verbos: CONSTRUIR · GARANTIR · ERRADICAR · PROMOVER", base:"CF, art. 3º"},

{d:"CF", art:"4º", titulo:"DOS PRINCÍPIOS FUNDAMENTAIS", rub:"Relações internacionais",
 caput:"A República Federativa do Brasil rege-se nas suas {relações internacionais} pelos seguintes princípios:",
 incisos:[
  {n:"I", t:"{independência nacional}"},
  {n:"II", t:"prevalência dos {direitos humanos}", imp:true, destaque:true},
  {n:"III", t:"{autodeterminação dos povos}"},
  {n:"IV", t:"{não intervenção}"},
  {n:"V", t:"igualdade entre os Estados"},
  {n:"VI", t:"defesa da paz"},
  {n:"VII", t:"solução pacífica dos conflitos"},
  {n:"VIII", t:"repúdio ao {terrorismo e ao racismo}", imp:true},
  {n:"IX", t:"cooperação entre os povos para o progresso da humanidade"},
  {n:"X", t:"concessão de {asilo político}", imp:true}
 ],
 paragrafos:[{rot:"Parágrafo único.", t:"A República Federativa do Brasil buscará a {integração} econômica, política, social e cultural dos povos da {América Latina}, visando à formação de uma comunidade latino-americana de nações."}],
 mnem:"DIREITOS HUMANOS (II) e ASILO POLÍTICO (X) são os campeões", base:"CF, art. 4º"},

{d:"CF", art:"5º", titulo:"DOS DIREITOS E DEVERES INDIVIDUAIS E COLETIVOS", rub:"Direitos e garantias fundamentais",
 caput:"Todos são {iguais} perante a lei, sem distinção de qualquer natureza, garantindo-se aos brasileiros e aos estrangeiros residentes no País a inviolabilidade do direito à {vida}, à {liberdade}, à {igualdade}, à {segurança} e à {propriedade}, nos termos seguintes:",
 incisos:[
  {n:"II", t:"ninguém será obrigado a fazer ou deixar de fazer alguma coisa senão em virtude de {lei}", imp:true, destaque:true},
  {n:"III", t:"ninguém será submetido a {tortura} nem a tratamento desumano ou degradante", imp:true},
  {n:"X", t:"são invioláveis a intimidade, a vida privada, a honra e a {imagem} das pessoas, assegurado o direito a indenização pelo dano material ou moral decorrente de sua violação", imp:true},
  {n:"XI", t:"a casa é {asilo inviolável} do indivíduo, ninguém nela podendo penetrar sem consentimento do morador, salvo em caso de flagrante delito ou desastre, ou para prestar socorro, ou, durante o dia, por determinação judicial", imp:true, destaque:true},
  {n:"XII", t:"é inviolável o sigilo da correspondência e das comunicações telegráficas, de dados e das comunicações telefônicas, salvo, no último caso, por {ordem judicial}, nas hipóteses e na forma que a lei estabelecer para fins de investigação criminal ou instrução processual penal", imp:true},
  {n:"XXXV", t:"a lei não excluirá da apreciação do Poder Judiciário {lesão ou ameaça a direito}", imp:true, destaque:true},
  {n:"XXXVI", t:"a lei não prejudicará o {direito adquirido}, o ato jurídico perfeito e a coisa julgada", imp:true},
  {n:"XXXIX", t:"não há crime sem lei {anterior} que o defina, nem pena sem prévia cominação legal", imp:true, destaque:true},
  {n:"XL", t:"a lei penal não retroagirá, salvo para {beneficiar} o réu", imp:true},
  {n:"XLII", t:"a prática do racismo constitui crime inafiançável e {imprescritível}, sujeito à pena de reclusão, nos termos da lei", imp:true},
  {n:"XLVII", t:"não haverá penas: de morte, salvo em caso de guerra declarada; de caráter {perpétuo}; de trabalhos forçados; de banimento; cruéis", imp:true},
  {n:"LIV", t:"ninguém será privado da liberdade ou de seus bens sem o {devido processo legal}", imp:true, destaque:true},
  {n:"LV", t:"aos litigantes, em processo judicial ou administrativo, e aos acusados em geral são assegurados o {contraditório} e a ampla defesa, com os meios e recursos a ela inerentes", imp:true, destaque:true},
  {n:"LVI", t:"são inadmissíveis, no processo, as provas obtidas por meios {ilícitos}", imp:true},
  {n:"LVII", t:"ninguém será considerado culpado até o {trânsito em julgado} de sentença penal condenatória", imp:true, destaque:true},
  {n:"LXI", t:"ninguém será preso senão em {flagrante delito} ou por ordem escrita e fundamentada de autoridade judiciária competente, salvo nos casos de transgressão militar ou crime propriamente militar, definidos em lei", imp:true, destaque:true},
  {n:"LXIII", t:"o preso será informado de seus direitos, entre os quais o de permanecer {calado}, sendo-lhe assegurada a assistência da família e de advogado", imp:true},
  {n:"LXV", t:"a prisão ilegal será imediatamente {relaxada} pela autoridade judiciária", imp:true},
  {n:"LXVI", t:"ninguém será levado à prisão ou nela mantido, quando a lei admitir a {liberdade provisória}, com ou sem fiança", imp:true},
  {n:"LXVIII", t:"conceder-se-á {habeas corpus} sempre que alguém sofrer ou se achar ameaçado de sofrer violência ou coação em sua liberdade de locomoção, por ilegalidade ou abuso de poder", imp:true},
  {n:"LXXVIII", t:"a todos, no âmbito judicial e administrativo, são assegurados a {razoável duração} do processo e os meios que garantam a celeridade de sua tramitação", imp:true}
 ],
 paragrafos:[{rot:"§ 3º", t:"Os tratados e convenções internacionais sobre direitos humanos que forem aprovados, em cada Casa do Congresso Nacional, em dois turnos, por três quintos dos votos dos respectivos membros, serão equivalentes às {emendas constitucionais}.", imp:true}],
 mnem:"caput: VI-LI-I-SE-PRO (vida, liberdade, igualdade, segurança, propriedade)", base:"CF, art. 5º"},

{d:"CF", art:"12", titulo:"DA NACIONALIDADE", rub:"Brasileiros natos e naturalizados",
 caput:"São brasileiros:",
 incisos:[
  {n:"I - natos", t:"os nascidos na República Federativa do Brasil, ainda que de pais estrangeiros, desde que estes não estejam a {serviço de seu país}", imp:true},
  {n:"II - naturalizados", t:"os que, na forma da lei, adquiram a nacionalidade brasileira, exigidas aos originários de países de língua portuguesa apenas residência por {um ano} ininterrupto e idoneidade moral", imp:true}
 ],
 paragrafos:[{rot:"§ 3º", t:"São privativos de brasileiro nato os cargos de Presidente e Vice-Presidente da República, de Presidente da Câmara, do Senado, Ministro do STF, da carreira {diplomática}, de oficial das Forças Armadas e de Ministro de Estado da Defesa.", imp:true, destaque:true}],
 mnem:"cargos de nato: MP3.COD (Ministro STF, Pres. República/Câmara/Senado, 3 — carreira diplomática, Oficial FFAA, Defesa)", base:"CF, art. 12"},

{d:"CF", art:"14", titulo:"DOS DIREITOS POLÍTICOS", rub:"Soberania popular",
 caput:"A soberania popular será exercida pelo sufrágio universal e pelo voto {direto e secreto}, com valor igual para todos, e, nos termos da lei, mediante:",
 incisos:[
  {n:"I", t:"{plebiscito}", imp:true},
  {n:"II", t:"{referendo}", imp:true},
  {n:"III", t:"{iniciativa popular}", imp:true}
 ],
 paragrafos:[{rot:"§ 1º", t:"O alistamento eleitoral e o voto são: obrigatórios para os maiores de dezoito anos; facultativos para os {analfabetos}, os maiores de setenta anos e os maiores de dezesseis e menores de dezoito anos.", imp:true}],
 mnem:"PLE-RE-INI (plebiscito, referendo, iniciativa popular)", base:"CF, art. 14"},

{d:"CF", art:"93, IX", titulo:"DO PODER JUDICIÁRIO", rub:"Publicidade e fundamentação",
 caput:"Todos os julgamentos dos órgãos do Poder Judiciário serão {públicos}, e {fundamentadas} todas as decisões, sob pena de nulidade, podendo a lei limitar a presença, em determinados atos, às próprias partes e a seus advogados, ou somente a estes, em casos nos quais a preservação do direito à intimidade do interessado no sigilo não prejudique o interesse público à informação.",
 incisos:[], paragrafos:[], mnem:"públicos + fundamentados = sob pena de NULIDADE", base:"CF, art. 93, IX"},

{d:"CF", art:"102", titulo:"DO PODER JUDICIÁRIO", rub:"Competência do STF",
 caput:"Compete ao Supremo Tribunal Federal, precipuamente, a guarda da {Constituição}, cabendo-lhe:",
 incisos:[
  {n:"I, a", t:"processar e julgar, originariamente, a ação direta de inconstitucionalidade de lei ou ato normativo federal ou estadual e a ação {declaratória de constitucionalidade}", imp:true},
  {n:"I, b", t:"nas infrações penais comuns, o {Presidente da República}, o Vice, os membros do Congresso Nacional, seus próprios Ministros e o Procurador-Geral da República", imp:true, destaque:true}
 ],
 paragrafos:[], mnem:"STF = guarda da CONSTITUIÇÃO (controle concentrado)", base:"CF, art. 102"},

{d:"CF", art:"127", titulo:"DAS FUNÇÕES ESSENCIAIS À JUSTIÇA — Ministério Público", rub:"Definição e princípios do MP",
 caput:"O Ministério Público é instituição {permanente}, essencial à função jurisdicional do Estado, incumbindo-lhe a defesa da ordem jurídica, do regime democrático e dos interesses sociais e individuais {indisponíveis}.",
 incisos:[],
 paragrafos:[{rot:"§ 1º", t:"São princípios institucionais do Ministério Público a {unidade}, a {indivisibilidade} e a {independência funcional}.", imp:true, destaque:true}],
 mnem:"princípios do MP: UNI-INDI-INDE", base:"CF, art. 127"},

{d:"CF", art:"129", titulo:"DO MINISTÉRIO PÚBLICO", rub:"Funções institucionais do MP",
 caput:"São funções institucionais do Ministério Público:",
 incisos:[
  {n:"I", t:"promover, {privativamente}, a ação penal pública, na forma da lei", imp:true, destaque:true},
  {n:"II", t:"zelar pelo efetivo respeito dos Poderes Públicos e dos serviços de relevância pública aos direitos assegurados nesta Constituição, promovendo as medidas necessárias a sua garantia"},
  {n:"III", t:"promover o {inquérito civil} e a ação civil pública, para a proteção do patrimônio público e social, do meio ambiente e de outros interesses difusos e coletivos", imp:true},
  {n:"VIII", t:"requisitar {diligências investigatórias} e a instauração de inquérito policial, indicados os fundamentos jurídicos de suas manifestações processuais", imp:true}
 ],
 paragrafos:[], mnem:"ação penal pública PRIVATIVA + inquérito CIVIL (não o policial)", base:"CF, art. 129"},

{d:"CF", art:"136", titulo:"DA DEFESA DO ESTADO E DAS INSTITUIÇÕES DEMOCRÁTICAS", rub:"Estado de defesa",
 caput:"O Presidente da República pode, ouvidos o Conselho da República e o Conselho de Defesa Nacional, decretar {estado de defesa} para preservar ou prontamente restabelecer, em locais restritos e determinados, a ordem pública ou a paz social ameaçadas por grave e iminente instabilidade institucional ou atingidas por calamidades de grandes proporções na natureza.",
 incisos:[],
 paragrafos:[{rot:"§ 1º", t:"O tempo de duração do estado de defesa não será superior a {trinta dias}, podendo ser prorrogado uma vez, por igual período, se persistirem as razões que justificaram a sua decretação.", imp:true, destaque:true}],
 mnem:"estado de DEFESA: decreta primeiro, Congresso aprova depois (24h); 30 dias + 1 prorrogação", base:"CF, art. 136"},

{d:"CF", art:"137", titulo:"DA DEFESA DO ESTADO", rub:"Estado de sítio",
 caput:"O Presidente da República pode, ouvidos o Conselho da República e o Conselho de Defesa Nacional, {solicitar ao Congresso Nacional} autorização para decretar o estado de sítio nos casos de:",
 incisos:[
  {n:"I", t:"comoção grave de repercussão nacional ou ocorrência de fatos que comprovem a ineficácia de medida tomada durante o {estado de defesa}", imp:true},
  {n:"II", t:"declaração de estado de {guerra} ou resposta a agressão armada estrangeira", imp:true}
 ],
 paragrafos:[], mnem:"estado de SÍTIO: pede autorização ANTES ao Congresso (ao contrário do de defesa)", base:"CF, art. 137"},

{d:"CF", art:"144", titulo:"DA SEGURANÇA PÚBLICA", rub:"Órgãos da segurança pública",
 caput:"A segurança pública, dever do Estado, direito e responsabilidade de todos, é exercida para a preservação da {ordem pública} e da incolumidade das pessoas e do patrimônio, através dos seguintes órgãos:",
 incisos:[
  {n:"I", t:"polícia {federal}", imp:true},
  {n:"II", t:"polícia rodoviária federal"},
  {n:"III", t:"polícia ferroviária federal"},
  {n:"IV", t:"polícias {civis}", imp:true},
  {n:"V", t:"polícias militares e corpos de bombeiros militares"},
  {n:"VI", t:"polícias penais federal, estaduais e distrital"}
 ],
 paragrafos:[
  {rot:"§ 1º, IV", t:"A polícia federal destina-se a exercer, com exclusividade, as funções de polícia {judiciária da União}.", imp:true},
  {rot:"§ 4º", t:"Às polícias civis, dirigidas por {delegados de polícia} de carreira, incumbem, ressalvada a competência da União, as funções de polícia judiciária e a apuração de infrações penais, exceto as militares.", imp:true, destaque:true}
 ],
 mnem:"polícia CIVIL (delegado) = polícia judiciária + apura infração penal, salvo militar", base:"CF, art. 144"},

/* ==================== CÓDIGO PENAL — PARTE GERAL ==================== */
{d:"CP", art:"1º", titulo:"CÓDIGO PENAL — Aplicação da lei penal", rub:"Anterioridade da lei penal",
 caput:"Não há crime sem {lei anterior} que o defina. Não há pena sem prévia {cominação legal}.",
 incisos:[], paragrafos:[], mnem:"legalidade/anterioridade (nullum crimen, nulla poena sine lege)", base:"CP, art. 1º"},

{d:"CP", art:"2º", titulo:"CÓDIGO PENAL", rub:"Lei penal no tempo (abolitio e retroatividade)",
 caput:"Ninguém pode ser punido por fato que lei posterior deixa de considerar crime, cessando em virtude dela a {execução} e os efeitos penais da sentença condenatória.",
 incisos:[],
 paragrafos:[{rot:"Parágrafo único.", t:"A lei posterior, que de qualquer modo favorecer o agente, aplica-se aos fatos {anteriores}, ainda que decididos por sentença condenatória transitada em julgado.", imp:true, destaque:true}],
 mnem:"lei penal benéfica RETROAGE (até depois do trânsito em julgado)", base:"CP, art. 2º"},

{d:"CP", art:"4º", titulo:"CÓDIGO PENAL", rub:"Tempo do crime",
 caput:"Considera-se praticado o crime no momento da {ação ou omissão}, ainda que outro seja o momento do resultado.",
 incisos:[], paragrafos:[], mnem:"TEMPO do crime = teoria da ATIVIDADE (LUTA: Lugar-Ubiquidade / Tempo-Atividade)", base:"CP, art. 4º"},

{d:"CP", art:"13", titulo:"CÓDIGO PENAL", rub:"Relação de causalidade",
 caput:"O resultado, de que depende a existência do crime, somente é imputável a quem lhe deu {causa}. Considera-se causa a ação ou omissão sem a qual o resultado não teria ocorrido.",
 incisos:[],
 paragrafos:[{rot:"§ 2º", t:"A omissão é penalmente relevante quando o omitente {devia e podia} agir para evitar o resultado (dever de agir: imposto por lei, assumido, ou por conduta anterior criadora do risco).", imp:true}],
 mnem:"teoria da equivalência (conditio sine qua non); omissão: devia E podia agir", base:"CP, art. 13"},

{d:"CP", art:"14", titulo:"CÓDIGO PENAL", rub:"Crime consumado e tentado",
 caput:"Diz-se o crime:",
 incisos:[
  {n:"I - consumado", t:"quando nele se reúnem {todos os elementos} de sua definição legal", imp:true},
  {n:"II - tentado", t:"quando, iniciada a execução, não se consuma por circunstâncias {alheias à vontade} do agente", imp:true, destaque:true}
 ],
 paragrafos:[{rot:"Parágrafo único.", t:"Salvo disposição em contrário, pune-se a tentativa com a pena correspondente ao crime consumado, diminuída de {um a dois terços}.", imp:true}],
 mnem:"tentativa: circunstâncias ALHEIAS à vontade; pena reduz de 1/3 a 2/3", base:"CP, art. 14"},

{d:"CP", art:"18", titulo:"CÓDIGO PENAL", rub:"Crime doloso e culposo",
 caput:"Diz-se o crime:",
 incisos:[
  {n:"I - doloso", t:"quando o agente {quis o resultado} ou assumiu o risco de produzi-lo", imp:true, destaque:true},
  {n:"II - culposo", t:"quando o agente deu causa ao resultado por {imprudência, negligência ou imperícia}", imp:true, destaque:true}
 ],
 paragrafos:[{rot:"Parágrafo único.", t:"Salvo os casos expressos em lei, ninguém pode ser punido por fato previsto como crime, senão quando o pratica {dolosamente}.", imp:true}],
 mnem:"dolo: quis OU assumiu o risco · culpa: imprudência, negligência, imperícia", base:"CP, art. 18"},

{d:"CP", art:"20", titulo:"CÓDIGO PENAL", rub:"Erro de tipo",
 caput:"O erro sobre {elemento constitutivo} do tipo legal de crime exclui o dolo, mas permite a punição por crime {culposo}, se previsto em lei.",
 incisos:[], paragrafos:[], mnem:"erro de TIPO exclui o DOLO (pune culpa, se houver)", base:"CP, art. 20"},

{d:"CP", art:"21", titulo:"CÓDIGO PENAL", rub:"Erro sobre a ilicitude (erro de proibição)",
 caput:"O {desconhecimento da lei} é inescusável. O erro sobre a ilicitude do fato, se inevitável, {isenta de pena}; se evitável, poderá diminuí-la de um sexto a um terço.",
 incisos:[], paragrafos:[], mnem:"erro de PROIBIÇÃO: inevitável ISENTA; evitável DIMINUI (1/6 a 1/3)", base:"CP, art. 21"},

{d:"CP", art:"23", titulo:"CÓDIGO PENAL", rub:"Exclusão de ilicitude",
 caput:"Não há crime quando o agente pratica o fato:",
 incisos:[
  {n:"I", t:"em {estado de necessidade}", imp:true},
  {n:"II", t:"em {legítima defesa}", imp:true, destaque:true},
  {n:"III", t:"em {estrito cumprimento de dever legal} ou no exercício regular de direito", imp:true}
 ],
 paragrafos:[{rot:"Parágrafo único.", t:"O agente, em qualquer das hipóteses deste artigo, responderá pelo {excesso} doloso ou culposo.", imp:true}],
 mnem:"excludentes de ilicitude: LE-EN-ES (legítima defesa, estado de necessidade, estrito cumprimento/exercício regular)", base:"CP, art. 23"},

{d:"CP", art:"25", titulo:"CÓDIGO PENAL", rub:"Legítima defesa",
 caput:"Entende-se em legítima defesa quem, usando {moderadamente} dos meios necessários, repele {injusta agressão}, atual ou iminente, a direito seu ou de outrem.",
 incisos:[], paragrafos:[], mnem:"LD: agressão INJUSTA, atual/iminente + meios necessários MODERADOS", base:"CP, art. 25"},

{d:"CP", art:"26", titulo:"CÓDIGO PENAL", rub:"Inimputáveis",
 caput:"É {isento de pena} o agente que, por doença mental ou desenvolvimento mental incompleto ou retardado, era, ao tempo da ação ou da omissão, inteiramente {incapaz} de entender o caráter ilícito do fato ou de determinar-se de acordo com esse entendimento.",
 incisos:[],
 paragrafos:[{rot:"Parágrafo único.", t:"A pena pode ser reduzida de um a dois terços, se o agente, em virtude de perturbação de saúde mental, não era {inteiramente capaz} de entender o caráter ilícito do fato (semi-imputável).", imp:true}],
 mnem:"inimputável (isenta) × semi-imputável (reduz 1/3 a 2/3)", base:"CP, art. 26"},

{d:"CP", art:"29", titulo:"CÓDIGO PENAL", rub:"Concurso de pessoas",
 caput:"Quem, de qualquer modo, concorre para o crime incide nas penas a este cominadas, na medida de sua {culpabilidade}.",
 incisos:[],
 paragrafos:[{rot:"§ 2º", t:"Se algum dos concorrentes quis participar de crime {menos grave}, ser-lhe-á aplicada a pena deste (cooperação dolosamente distinta).", imp:true}],
 mnem:"teoria MONISTA: todos no mesmo crime, na medida da culpabilidade", base:"CP, art. 29"},

{d:"CP", art:"33", titulo:"CÓDIGO PENAL — Das penas", rub:"Reclusão e detenção",
 caput:"A pena de {reclusão} deve ser cumprida em regime fechado, semiaberto ou aberto. A de {detenção}, em regime semiaberto ou aberto, salvo necessidade de transferência a regime fechado.",
 incisos:[], paragrafos:[], mnem:"RECLUSÃO: fechado/semi/aberto · DETENÇÃO: não inicia em fechado", base:"CP, art. 33"},

{d:"CP", art:"59", titulo:"CÓDIGO PENAL — Aplicação da pena", rub:"Circunstâncias judiciais",
 caput:"O juiz, atendendo à {culpabilidade}, aos antecedentes, à conduta social, à personalidade do agente, aos motivos, às circunstâncias e consequências do crime, bem como ao comportamento da vítima, estabelecerá, conforme seja necessário e suficiente para {reprovação e prevenção} do crime:",
 incisos:[
  {n:"I", t:"as penas {aplicáveis} dentre as cominadas"},
  {n:"II", t:"a {quantidade} de pena aplicável, dentro dos limites previstos"},
  {n:"III", t:"o regime inicial de cumprimento da pena privativa de liberdade"},
  {n:"IV", t:"a substituição da pena privativa de liberdade, se cabível"}
 ],
 paragrafos:[], mnem:"8 circunstâncias judiciais (1ª fase da dosimetria)", base:"CP, art. 59"},

{d:"CP", art:"65", titulo:"CÓDIGO PENAL", rub:"Circunstâncias atenuantes",
 caput:"São circunstâncias que sempre {atenuam} a pena:",
 incisos:[
  {n:"I", t:"ser o agente menor de {21} anos, na data do fato, ou maior de 70 anos, na data da sentença", imp:true, destaque:true},
  {n:"III, b", t:"ter o agente procurado, por sua espontânea vontade e com eficiência, logo após o crime, evitar-lhe ou minorar-lhe as consequências, ou ter, antes do julgamento, reparado o {dano}"},
  {n:"III, d", t:"ter o agente {confessado} espontaneamente, perante a autoridade, a autoria do crime", imp:true}
 ],
 paragrafos:[], mnem:"menor de 21 na data do FATO; maior de 70 na data da SENTENÇA", base:"CP, art. 65"},

{d:"CP", art:"107", titulo:"CÓDIGO PENAL", rub:"Extinção da punibilidade",
 caput:"Extingue-se a punibilidade:",
 incisos:[
  {n:"I", t:"pela {morte} do agente", imp:true, destaque:true},
  {n:"II", t:"pela {anistia}, graça ou indulto"},
  {n:"III", t:"pela retroatividade de lei que não mais considera o fato como criminoso (abolitio criminis)", imp:true},
  {n:"IV", t:"pela {prescrição}, decadência ou perempção", imp:true}
 ],
 paragrafos:[], mnem:"morte do agente extingue TUDO (mors omnia solvit)", base:"CP, art. 107"},

/* ==================== CÓDIGO DE PROCESSO PENAL ==================== */
{d:"CPP", art:"5º", titulo:"CÓDIGO DE PROCESSO PENAL — Inquérito policial", rub:"Início do inquérito",
 caput:"Nos crimes de ação pública o inquérito policial será iniciado:",
 incisos:[
  {n:"I", t:"de {ofício}", imp:true, destaque:true},
  {n:"II", t:"mediante {requisição} da autoridade judiciária ou do Ministério Público, ou a requerimento do ofendido ou de quem tenha qualidade para representá-lo", imp:true}
 ],
 paragrafos:[{rot:"§ 4º", t:"O inquérito, nos crimes em que a ação pública depender de {representação}, não poderá sem ela ser iniciado.", imp:true}],
 mnem:"IP de ofício (ação pública incondicionada) ou por requisição/requerimento", base:"CPP, art. 5º"},

{d:"CPP", art:"28-A", titulo:"CÓDIGO DE PROCESSO PENAL", rub:"Acordo de não persecução penal (ANPP)",
 caput:"Não sendo caso de arquivamento e tendo o investigado {confessado} formal e circunstancialmente a prática de infração penal sem violência ou grave ameaça e com pena mínima inferior a {4 anos}, o Ministério Público poderá propor acordo de não persecução penal, desde que necessário e suficiente para reprovação e prevenção do crime, mediante as condições ajustadas cumulativa e alternativamente.",
 incisos:[], paragrafos:[], mnem:"ANPP: confissão + sem violência/grave ameaça + pena mínima < 4 anos", base:"CPP, art. 28-A"},

{d:"CPP", art:"155", titulo:"CÓDIGO DE PROCESSO PENAL — Da prova", rub:"Livre convencimento motivado",
 caput:"O juiz formará sua convicção pela {livre apreciação} da prova produzida em contraditório judicial, não podendo fundamentar sua decisão {exclusivamente} nos elementos informativos colhidos na investigação, ressalvadas as provas cautelares, não repetíveis e antecipadas.",
 incisos:[], paragrafos:[], mnem:"não condena SÓ com o IP (salvo cautelar, não repetível, antecipada)", base:"CPP, art. 155"},

{d:"CPP", art:"157", titulo:"CÓDIGO DE PROCESSO PENAL", rub:"Provas ilícitas",
 caput:"São {inadmissíveis}, devendo ser desentranhadas do processo, as provas ilícitas, assim entendidas as obtidas em violação a normas constitucionais ou legais.",
 incisos:[],
 paragrafos:[{rot:"§ 1º", t:"São também inadmissíveis as provas {derivadas} das ilícitas, salvo quando não evidenciado o nexo de causalidade entre umas e outras, ou quando as derivadas puderem ser obtidas por uma fonte independente das primeiras (teoria dos frutos da árvore envenenada).", imp:true, destaque:true}],
 mnem:"prova ilícita: desentranha + contamina a DERIVADA (frutos da árvore envenenada)", base:"CPP, art. 157"},

{d:"CPP", art:"282", titulo:"CÓDIGO DE PROCESSO PENAL — Medidas cautelares", rub:"Requisitos das cautelares",
 caput:"As medidas cautelares previstas neste Título deverão ser aplicadas observando-se a:",
 incisos:[
  {n:"I", t:"{necessidade} para aplicação da lei penal, para a investigação ou a instrução criminal e, nos casos expressamente previstos, para evitar a prática de infrações penais", imp:true},
  {n:"II", t:"{adequação} da medida à gravidade do crime, circunstâncias do fato e condições pessoais do indiciado ou acusado", imp:true}
 ],
 paragrafos:[{rot:"§ 2º", t:"As medidas cautelares serão decretadas pelo juiz a {requerimento} das partes ou, quando no curso da investigação criminal, por representação da autoridade policial ou mediante requerimento do Ministério Público.", imp:true, destaque:true}],
 mnem:"cautelar: NECESSIDADE + ADEQUAÇÃO; juiz não decreta de ofício na investigação", base:"CPP, art. 282"},

{d:"CPP", art:"283", titulo:"CÓDIGO DE PROCESSO PENAL — Da prisão", rub:"Espécies de prisão",
 caput:"Ninguém poderá ser preso senão em {flagrante delito} ou por ordem escrita e fundamentada da autoridade judiciária competente, em decorrência de prisão cautelar ou em virtude de condenação criminal {transitada em julgado}.",
 incisos:[], paragrafos:[], mnem:"prisão: flagrante OU ordem judicial escrita e fundamentada", base:"CPP, art. 283"},

{d:"CPP", art:"310", titulo:"CÓDIGO DE PROCESSO PENAL", rub:"Audiência de custódia",
 caput:"Após receber o auto de prisão em flagrante, no prazo máximo de até {24 horas} após a realização da prisão, o juiz deverá promover audiência de custódia com a presença do acusado, seu advogado constituído ou membro da Defensoria Pública e o membro do Ministério Público, e, nessa audiência, deverá, fundamentadamente:",
 incisos:[
  {n:"I", t:"relaxar a prisão {ilegal}", imp:true},
  {n:"II", t:"converter a prisão em flagrante em {preventiva}, quando presentes os requisitos legais, e se revelarem inadequadas ou insuficientes as medidas cautelares diversas", imp:true, destaque:true},
  {n:"III", t:"conceder {liberdade provisória}, com ou sem fiança"}
 ],
 paragrafos:[], mnem:"custódia em 24h: relaxar · converter em preventiva · conceder liberdade", base:"CPP, art. 310"},

{d:"CPP", art:"312", titulo:"CÓDIGO DE PROCESSO PENAL — Prisão preventiva", rub:"Pressupostos e fundamentos",
 caput:"A prisão preventiva poderá ser decretada como garantia da {ordem pública}, da ordem econômica, por conveniência da {instrução criminal} ou para assegurar a {aplicação da lei penal}, quando houver prova da existência do crime e indício suficiente de autoria e de perigo gerado pelo estado de liberdade do imputado.",
 incisos:[],
 paragrafos:[{rot:"§ 2º", t:"A decisão que decretar a prisão preventiva deverá ser {motivada} e fundamentada em receio de perigo e existência concreta de fatos novos ou contemporâneos que justifiquem a aplicação da medida.", imp:true}],
 mnem:"preventiva: ORDEM pública/econômica · INSTRUÇÃO · APLICAÇÃO da lei penal (+ fumus e periculum)", base:"CPP, art. 312"},

{d:"CPP", art:"316", titulo:"CÓDIGO DE PROCESSO PENAL", rub:"Revisão da preventiva",
 caput:"O juiz poderá, de ofício ou a pedido das partes, revogar a prisão preventiva se, no correr da investigação ou do processo, verificar a {falta de motivo} para que subsista, bem como novamente decretá-la, se sobrevierem razões que a justifiquem.",
 incisos:[],
 paragrafos:[{rot:"Parágrafo único.", t:"Decretada a prisão preventiva, o órgão emissor da decisão deverá revisar a necessidade de sua manutenção a cada {90 dias}, mediante decisão fundamentada, de ofício, sob pena de tornar a prisão ilegal.", imp:true, destaque:true}],
 mnem:"revisar a preventiva a cada 90 DIAS, de ofício, sob pena de ilegalidade", base:"CPP, art. 316"},

{d:"CPP", art:"397", titulo:"CÓDIGO DE PROCESSO PENAL — Procedimento", rub:"Absolvição sumária",
 caput:"Após o cumprimento do disposto no art. 396-A, e parágrafos, deste Código, o juiz deverá {absolver sumariamente} o acusado quando verificar:",
 incisos:[
  {n:"I", t:"a existência manifesta de causa {excludente da ilicitude} do fato", imp:true},
  {n:"II", t:"a existência manifesta de causa excludente da {culpabilidade} do agente, salvo inimputabilidade", imp:true},
  {n:"III", t:"que o fato narrado evidentemente {não constitui crime}", imp:true, destaque:true},
  {n:"IV", t:"extinta a {punibilidade} do agente"}
 ],
 paragrafos:[], mnem:"absolvição sumária: ilicitude · culpabilidade · atipicidade · extinção da punibilidade", base:"CPP, art. 397"}

];
