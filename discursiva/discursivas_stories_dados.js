/* discursivas_stories_dados.js — dados do módulo "Discursivas em Stories" (20/11/2026, pedido do titular).
 * Questões discursivas para Delegado estudadas na metodologia dos Stories: o ENUNCIADO fica fixo no topo e você
 * toca para revelar UM PONTO-CHAVE da resposta por vez (recordação ativa da estrutura da resposta).
 * Organizado em BLOCOS por disciplina. Conteúdo autoral, fundado na lei seca oficial e na doutrina majoritária;
 * nada de material de terceiro entra aqui. */
window.DISC_STORIES = [

{id:"pen", bloco:"Direito Penal", curto:"Penal", itens:[
  {tema:"Erro de tipo × erro de proibição",
   enun:"Distinga erro de tipo e erro de proibição, indicando os efeitos de cada um na responsabilidade penal.",
   pontos:[
    "Erro de TIPO (CP, art. 20): recai sobre elemento constitutivo do tipo — o agente não sabe o que faz. Exclui o DOLO.",
    "Se o erro de tipo for inevitável (escusável), exclui dolo e culpa (atipicidade); se evitável, pune-se por crime culposo, se previsto em lei.",
    "Erro de PROIBIÇÃO (CP, art. 21): recai sobre a ilicitude — o agente sabe o que faz, mas supõe lícito. Atinge a CULPABILIDADE (potencial consciência da ilicitude).",
    "Erro de proibição inevitável ISENTA de pena; evitável, apenas DIMINUI a pena de 1/6 a 1/3. O desconhecimento da lei é inescusável.",
    "Resumo: erro de tipo → exclui dolo (tipicidade); erro de proibição → exclui/reduz culpabilidade."
   ], base:"CP, arts. 20 e 21"},
  {tema:"Concurso de pessoas",
   enun:"Discorra sobre a teoria adotada pelo Código Penal no concurso de pessoas e sobre a cooperação dolosamente distinta.",
   pontos:[
    "O CP adota a teoria MONISTA (unitária): todos que concorrem para o crime respondem pelo mesmo delito, na medida de sua culpabilidade (art. 29).",
    "Admite exceções pluralistas (ex.: aborto consentido — gestante e terceiro em tipos distintos).",
    "Requisitos do concurso: pluralidade de agentes e condutas, relevância causal, liame subjetivo (vínculo) e identidade de infração.",
    "Cooperação dolosamente distinta (art. 29, §2º): se o agente quis participar de crime MENOS grave, aplica-se a pena deste, aumentada até 1/2 se era previsível o resultado mais grave.",
    "Participação de menor importância (art. 29, §1º): pena diminuída de 1/6 a 1/3."
   ], base:"CP, art. 29"},
  {tema:"Excludentes de ilicitude",
   enun:"Diferencie legítima defesa e estado de necessidade e aponte os requisitos da legítima defesa.",
   pontos:[
    "Ambas são excludentes de ilicitude (art. 23): afastam o crime por ausência de contrariedade ao direito.",
    "Legítima defesa (art. 25): reação a uma AGRESSÃO humana, injusta, atual ou iminente, a direito próprio ou alheio.",
    "Requisitos da LD: agressão injusta + atual/iminente + uso MODERADO dos meios NECESSÁRIOS + animus defendendi.",
    "Estado de necessidade (art. 24): conflito de interesses lícitos (perigo atual não provocado voluntariamente), sacrificando-se bem de valor igual ou menor que não era razoável exigir se preservasse.",
    "Em qualquer delas, o agente responde pelo EXCESSO doloso ou culposo (art. 23, §único)."
   ], base:"CP, arts. 23 a 25"},
  {tema:"Iter criminis e tentativa",
   enun:"Explique o iter criminis, a tentativa e a distinção entre desistência voluntária e arrependimento eficaz.",
   pontos:[
    "Iter criminis: cogitação → preparação → execução → consumação. Em regra só se pune a partir da execução.",
    "Tentativa (art. 14, II): iniciada a execução, o crime não se consuma por circunstâncias ALHEIAS à vontade do agente. Pena do consumado reduzida de 1/3 a 2/3.",
    "Desistência voluntária (art. 15): o agente, podendo prosseguir, interrompe voluntariamente a execução.",
    "Arrependimento eficaz (art. 15): esgotada a execução, o agente impede voluntariamente o resultado. Em ambos responde só pelos atos já praticados (tentativa abandonada).",
    "Arrependimento posterior (art. 16): crime sem violência/grave ameaça, reparado o dano até o recebimento da denúncia → redução de 1/3 a 2/3."
   ], base:"CP, arts. 14 a 16"},
  {tema:"Crimes hediondos e progressão",
   enun:"Disserte sobre os efeitos da hediondez na execução penal, com atenção aos patamares de progressão de regime.",
   pontos:[
    "Hediondos e equiparados (Lei 8.072/90) têm regime mais severo: insuscetíveis de anistia, graça, indulto e fiança.",
    "Progressão de regime é possível, mas com percentuais maiores (LEP, art. 112): 40% (comum primário), 60% (comum reincidente).",
    "Hediondo primário: 50% (sem morte) e 70% com resultado morte, vedado o livramento neste último.",
    "Hediondo reincidente: 60% e 70%/80% conforme o resultado; reincidente específico em hediondo com morte: 70%, vedado livramento.",
    "Lei Antifacção (15.358/26) incluiu novos patamares (ex.: 75% para comando de facção, vedado o livramento)."
   ], base:"Lei 8.072/90; LEP, art. 112"}
]},

{id:"pp", bloco:"Direito Processual Penal", curto:"Proc. Penal", itens:[
  {tema:"Inquérito policial",
   enun:"Conceitue o inquérito policial e aponte suas características e seu valor probatório.",
   pontos:[
    "IP é procedimento administrativo, investigativo e preparatório, presidido pelo delegado de polícia, destinado a apurar a autoria e a materialidade da infração.",
    "Características: escrito, sigiloso, inquisitivo (não há contraditório pleno), oficioso/oficialidade, indisponível e dispensável (a denúncia pode fundar-se em outros elementos).",
    "Valor probatório relativo: os elementos informativos do IP não podem, sozinhos, fundamentar a condenação (CPP, art. 155).",
    "Exceção: provas cautelares, não repetíveis e antecipadas podem embasar a decisão.",
    "O indiciamento é ato privativo do delegado, por despacho fundamentado."
   ], base:"CPP, art. 155; Lei 12.830/13"},
  {tema:"Prisão preventiva",
   enun:"Disserte sobre os pressupostos, os fundamentos e as hipóteses de cabimento da prisão preventiva.",
   pontos:[
    "Pressupostos (fumus commissi delicti): prova da materialidade e indício suficiente de autoria (CPP, art. 312).",
    "Fundamentos (periculum libertatis): garantia da ordem pública, da ordem econômica, conveniência da instrução criminal ou para assegurar a aplicação da lei penal.",
    "Exige perigo gerado pelo estado de liberdade e fatos novos/contemporâneos; decisão sempre motivada.",
    "Cabimento (art. 313): crime doloso com pena máxima > 4 anos; reincidente em doloso; violência doméstica; dúvida sobre identidade.",
    "Não pode ser decretada de ofício; revisão da necessidade a cada 90 dias, sob pena de ilegalidade (art. 316, §único)."
   ], base:"CPP, arts. 312, 313 e 316"},
  {tema:"Cadeia de custódia",
   enun:"Explique a cadeia de custódia da prova e as consequências de sua quebra.",
   pontos:[
    "Cadeia de custódia é o conjunto de procedimentos para rastrear e documentar a prova desde a coleta até o descarte, garantindo sua integridade e autenticidade (CPP, arts. 158-A a 158-F).",
    "Etapas: reconhecimento, isolamento, fixação, coleta, acondicionamento, transporte, recebimento, processamento, armazenamento e descarte.",
    "Começa com a preservação do local de crime ou com a apreensão do vestígio.",
    "A quebra pode gerar a ilicitude/invalidade da prova, aferida no caso concreto (não é nulidade automática para parte da doutrina/jurisprudência).",
    "Objetivo: assegurar a mesmidade (a prova analisada é a mesma coletada) e evitar manipulação."
   ], base:"CPP, arts. 158-A a 158-F"},
  {tema:"Acordo de não persecução penal",
   enun:"Discorra sobre o acordo de não persecução penal (ANPP): requisitos e natureza.",
   pontos:[
    "ANPP (CPP, art. 28-A) é negócio jurídico pré-processual proposto pelo MP, não sendo caso de arquivamento.",
    "Requisitos: confissão formal e circunstanciada; infração sem violência ou grave ameaça; pena mínima inferior a 4 anos.",
    "Condições (cumulativas/alternativas): reparar o dano, renunciar a bens, prestar serviço à comunidade, pagar prestação pecuniária, etc.",
    "Vedações: cabível transação penal; reincidente/habitualidade; ANPP nos últimos 5 anos; violência doméstica contra a mulher.",
    "Cumprido o acordo, extingue-se a punibilidade; descumprido, o MP oferece denúncia."
   ], base:"CPP, art. 28-A"},
  {tema:"Prisão em flagrante",
   enun:"Aponte as espécies de flagrante e o papel da autoridade policial e do juiz após a prisão.",
   pontos:[
    "Espécies (CPP, art. 302): flagrante próprio (cometendo/acabando de cometer), impróprio (perseguição logo após) e presumido/ficto (encontrado logo depois com instrumentos).",
    "Classificações doutrinárias: preparado (prova ilícita — Súmula 145 STF), esperado (válido), forjado (atípico) e retardado/ação controlada.",
    "Lavrado o auto, a prisão é comunicada em 24h ao juiz, ao MP e à família/defensor.",
    "Em até 24h realiza-se a audiência de custódia (CPP, art. 310), agora por videoconferência (Lei 15.358/26).",
    "Na custódia, o juiz: relaxa a prisão ilegal, converte em preventiva (se presentes os requisitos) ou concede liberdade provisória."
   ], base:"CPP, arts. 302, 304 e 310"}
]},

{id:"cf", bloco:"Direito Constitucional", curto:"Constitucional", itens:[
  {tema:"Segurança pública (art. 144)",
   enun:"Disserte sobre a segurança pública na CF/88 e as funções da polícia civil.",
   pontos:[
    "Segurança pública é dever do Estado e direito/responsabilidade de todos, exercida para preservação da ordem pública e da incolumidade das pessoas e do patrimônio (art. 144, caput).",
    "Órgãos (rol taxativo): PF, PRF, PFF, polícias civis, polícias militares e corpos de bombeiros, polícias penais.",
    "À polícia civil, dirigida por delegado de carreira, incumbem as funções de polícia JUDICIÁRIA e a apuração de infrações penais, exceto as militares (art. 144, §4º).",
    "Polícia judiciária (repressiva, pós-delito) ≠ polícia administrativa/ostensiva (preventiva, da PM).",
    "As polícias civis subordinam-se aos Governadores (art. 144, §6º)."
   ], base:"CF, art. 144"},
  {tema:"Direitos do preso",
   enun:"Aponte os direitos fundamentais do preso e as garantias constitucionais aplicáveis à prisão.",
   pontos:[
    "Prisão só em flagrante ou por ordem escrita e fundamentada da autoridade judiciária competente (art. 5º, LXI).",
    "Direito ao silêncio e à não autoincriminação; informação dos direitos; assistência da família e de advogado (LXIII).",
    "Comunicação imediata da prisão ao juiz e à família (LXII); identificação dos responsáveis (LXIV).",
    "Relaxamento da prisão ilegal pela autoridade judiciária (LXV); liberdade provisória com ou sem fiança (LXVI).",
    "Respeito à integridade física e moral do preso (XLIX); vedação de penas cruéis e perpétuas (XLVII)."
   ], base:"CF, art. 5º"},
  {tema:"Presunção de inocência",
   enun:"Discorra sobre o princípio da presunção de inocência e seus desdobramentos.",
   pontos:[
    "Ninguém será considerado culpado até o trânsito em julgado de sentença penal condenatória (art. 5º, LVII).",
    "Desdobramentos: regra de tratamento (não tratar o acusado como culpado), regra probatória (ônus da acusação) e regra de juízo (in dubio pro reo).",
    "A prisão antes do trânsito em julgado só se admite a título cautelar (flagrante, temporária, preventiva).",
    "Não impede medidas cautelares nem a execução provisória em hipóteses específicas definidas pela jurisprudência.",
    "Relaciona-se ao devido processo legal, contraditório e ampla defesa (LIV e LV)."
   ], base:"CF, art. 5º, LVII"}
]},

{id:"lpe", bloco:"Legislação Penal Especial", curto:"Leg. Especial", itens:[
  {tema:"Lei de Drogas — porte para consumo",
   enun:"Disserte sobre a natureza jurídica do art. 28 da Lei 11.343/06 e sobre o tráfico privilegiado.",
   pontos:[
    "Art. 28 (porte para consumo pessoal): não há pena privativa de liberdade — só advertência, prestação de serviços e medida educativa.",
    "Natureza: houve despenalização (não descriminalização) — permanece crime, mas sem prisão (posição majoritária/STF).",
    "Distinção entre usuário e traficante: analisa-se quantidade, local, circunstâncias, conduta e antecedentes (art. 28, §2º).",
    "Tráfico privilegiado (art. 33, §4º): réu primário, bons antecedentes, não dedicado a atividades criminosas nem integrante de organização → redução de 1/6 a 2/3.",
    "O tráfico privilegiado NÃO tem natureza hedionda (entendimento consolidado)."
   ], base:"Lei 11.343/06, arts. 28 e 33"},
  {tema:"Organização criminosa × Lei Antifacção",
   enun:"Diferencie a organização criminosa da Lei 12.850/13 e a facção criminosa da Lei 15.358/26.",
   pontos:[
    "ORCRIM (Lei 12.850/13, art. 1º, §1º): 4 ou mais pessoas, estruturalmente ordenada, divisão de tarefas, para obter vantagem com infrações de pena máxima > 4 anos ou transnacionais.",
    "Facção criminosa / organização ultraviolenta (Lei 15.358/26, art. 2º, §2º): 3 ou mais pessoas que empregam violência, grave ameaça ou coação para impor controle territorial/social.",
    "Domínio social estruturado (art. 2º): pena de reclusão de 20 a 40 anos; crime hediondo; insuscetível de anistia, graça, indulto, fiança e livramento.",
    "A Lei 15.358/26 aplica subsidiariamente os meios de obtenção de prova da Lei 12.850/13 (colaboração premiada, infiltração, ação controlada).",
    "Facção é forma especial e mais grave de organização criminosa."
   ], base:"Lei 12.850/13; Lei 15.358/26"},
  {tema:"Lei de Abuso de Autoridade",
   enun:"Aponte o elemento subjetivo exigido pela Lei 13.869/19 e um exemplo de conduta típica aplicável ao delegado.",
   pontos:[
    "Os crimes de abuso de autoridade exigem DOLO ESPECÍFICO: finalidade de prejudicar outrem, beneficiar a si ou por mero capricho/satisfação pessoal (art. 1º, §1º).",
    "A divergência na interpretação da lei ou na avaliação de fatos/provas não configura abuso (art. 1º, §2º).",
    "Sujeito ativo: qualquer agente público, inclusive o delegado (crime próprio).",
    "Exemplos: constranger preso a produzir prova contra si; decretar/prolongar indevidamente a prisão; proceder a interrogatório de madrugada sem urgência.",
    "As penas somam-se às de eventuais crimes conexos; cabível ação penal pública incondicionada."
   ], base:"Lei 13.869/19, art. 1º"},
  {tema:"Maria da Penha — medidas protetivas",
   enun:"Discorra sobre as medidas protetivas de urgência e o papel do delegado na Lei 11.340/06.",
   pontos:[
    "A Lei 11.340/06 coíbe a violência doméstica e familiar contra a mulher (física, psicológica, sexual, patrimonial e moral).",
    "Medidas protetivas podem obrigar o agressor (afastamento do lar, proibição de contato/aproximação) ou proteger a ofendida.",
    "O delegado pode aplicar/ representar por medidas protetivas; em determinadas hipóteses a autoridade policial pode conceder o afastamento do agressor (art. 12-C).",
    "A ação penal na lesão corporal (mesmo leve) é pública INCONDICIONADA (Súmula 542 STJ).",
    "Vedada a aplicação de penas de cesta básica ou pecuniária isolada (art. 17)."
   ], base:"Lei 11.340/06"},
  {tema:"Lei de Tortura",
   enun:"Aponte as características do crime de tortura e seus efeitos quanto à hediondez e à prescrição.",
   pontos:[
    "A Lei 9.455/97 tipifica a tortura, que pode ser cometida por particular (crime comum), salvo a tortura-omissão, própria de quem tinha o dever de evitá-la.",
    "Modalidades: tortura-prova/confissão, tortura para ação/omissão criminosa, tortura discriminatória e tortura-castigo.",
    "A tortura é crime equiparado a hediondo (CF, art. 5º, XLIII): inafiançável e insuscetível de graça/anistia.",
    "Efeito automático da condenação: perda do cargo e interdição para seu exercício pelo dobro do prazo da pena (art. 1º, §5º).",
    "Se o agente é servidor público, a pena é aumentada; regime inicial fechado."
   ], base:"Lei 9.455/97; CF, art. 5º, XLIII"}
]},

{id:"adm", bloco:"Direito Administrativo", curto:"Administrativo", itens:[
  {tema:"Poder de polícia",
   enun:"Disserte sobre os poderes da Administração, com destaque para o poder de polícia e seus atributos.",
   pontos:[
    "Poderes administrativos são instrumentais e irrenunciáveis: vinculado, discricionário, hierárquico, disciplinar, regulamentar e de polícia.",
    "Poder de polícia é a faculdade de condicionar/limitar o uso de bens, direitos e atividades em prol do interesse público.",
    "Atributos: discricionariedade, autoexecutoriedade (dispensa o Judiciário) e coercibilidade (imposição coativa).",
    "Ciclo de polícia (4 fases): ordem, consentimento, fiscalização e sanção. A fiscalização e a sanção são indelegáveis a privados.",
    "Limites: proporcionalidade, legalidade e menor restrição possível (não pode ser arbitrário)."
   ], base:"Doutrina; CF; CTN, art. 78"},
  {tema:"Requisitos do ato administrativo",
   enun:"Aponte os requisitos de validade e os atributos do ato administrativo.",
   pontos:[
    "Requisitos/elementos (COM-FI-FO-MO-OB): Competência, Finalidade, Forma, Motivo e Objeto.",
    "Competência, finalidade e forma são, em regra, vinculados; motivo e objeto podem ser discricionários (mérito).",
    "Atributos: presunção de legitimidade e veracidade, imperatividade, autoexecutoriedade e tipicidade.",
    "Teoria dos motivos determinantes: o ato vincula-se aos motivos declarados; se falsos/inexistentes, é inválido.",
    "Convalidação: vícios sanáveis de competência e forma; vícios de finalidade, motivo e objeto não se convalidam."
   ], base:"Lei 9.784/99; doutrina"},
  {tema:"Improbidade administrativa",
   enun:"Discorra sobre as espécies de ato de improbidade e o elemento subjetivo após a Lei 14.230/21.",
   pontos:[
    "Três espécies: enriquecimento ilícito (art. 9º), prejuízo ao erário (art. 10) e atentado aos princípios da Administração (art. 11).",
    "Após a Lei 14.230/21, exige-se DOLO (vontade livre e consciente de alcançar o resultado ilícito) em todas as espécies.",
    "A modalidade culposa foi extinta: a mera ilegalidade ou culpa não configura mais improbidade.",
    "Sanções (art. 12): perda da função, suspensão dos direitos políticos, ressarcimento, multa e proibição de contratar com o Poder Público.",
    "A ação de ressarcimento ao erário por ato doloso é imprescritível (CF, art. 37, §5º)."
   ], base:"Lei 8.429/92; CF, art. 37"},
  {tema:"Responsabilidade civil do Estado",
   enun:"Disserte sobre a responsabilidade civil do Estado, a teoria adotada e as excludentes.",
   pontos:[
    "A CF (art. 37, §6º) adota a responsabilidade OBJETIVA, na modalidade teoria do risco administrativo.",
    "Requisitos: conduta do agente (nessa qualidade), dano e nexo causal — dispensa-se a prova de culpa.",
    "Excludentes/atenuantes do nexo: culpa exclusiva da vítima, caso fortuito/força maior e fato exclusivo de terceiro.",
    "Há direito de regresso contra o agente nos casos de dolo ou culpa (responsabilidade subjetiva do agente).",
    "Na omissão, parte da doutrina/jurisprudência exige responsabilidade subjetiva (faute du service — falta do serviço)."
   ], base:"CF, art. 37, §6º"},
  {tema:"Licitações (Lei 14.133/21)",
   enun:"Aponte as modalidades e as fases do procedimento licitatório na Lei 14.133/21.",
   pontos:[
    "Modalidades: pregão, concorrência, concurso, leilão e diálogo competitivo (extinguiram-se tomada de preços e convite).",
    "Critérios de julgamento: menor preço, maior desconto, melhor técnica ou conteúdo artístico, técnica e preço, maior lance e maior retorno econômico.",
    "Fases (art. 17): preparatória, divulgação do edital, apresentação de propostas/lances, julgamento, habilitação, recursal e homologação.",
    "Em regra, a habilitação ocorre após o julgamento (inversão de fases, como no pregão).",
    "Princípios: legalidade, impessoalidade, moralidade, publicidade, eficiência, isonomia, competitividade e julgamento objetivo."
   ], base:"Lei 14.133/21"}
]},

{id:"dh", bloco:"Direitos Humanos", curto:"Dir. Humanos", itens:[
  {tema:"Características dos Direitos Humanos",
   enun:"Discorra sobre as características dos direitos humanos e a diferença entre direitos humanos e direitos fundamentais.",
   pontos:[
    "Características: universalidade, indivisibilidade, interdependência, imprescritibilidade, inalienabilidade, irrenunciabilidade e historicidade.",
    "Vedação ao retrocesso (efeito cliquet): os direitos já reconhecidos não podem ser suprimidos.",
    "Direitos humanos: plano internacional (tratados); direitos fundamentais: positivados na Constituição de um Estado.",
    "Fundamento comum: a dignidade da pessoa humana.",
    "Dimensões: 1ª (liberdade/civis e políticos), 2ª (igualdade/sociais), 3ª (fraternidade/difusos)."
   ], base:"Doutrina; CF, art. 5º"},
  {tema:"Status dos tratados de direitos humanos",
   enun:"Explique a hierarquia dos tratados internacionais de direitos humanos no ordenamento brasileiro.",
   pontos:[
    "Tratados comuns ingressam com status de lei ordinária.",
    "Tratados de direitos humanos aprovados pelo rito do art. 5º, §3º (3/5, em 2 turnos, nas 2 Casas) têm status de EMENDA constitucional.",
    "Tratados de direitos humanos não aprovados por esse rito têm status SUPRALEGAL (acima da lei, abaixo da CF) — STF.",
    "Consequência: o Pacto de San José tornou inaplicável a prisão civil do depositário infiel (Súmula Vinculante 25).",
    "Incidente de deslocamento de competência (IDC) para a Justiça Federal em grave violação de direitos humanos (art. 109, §5º)."
   ], base:"CF, art. 5º, §§2º e 3º"},
  {tema:"Sistemas de proteção",
   enun:"Aponte os sistemas internacionais de proteção dos direitos humanos.",
   pontos:[
    "Sistema global (ONU): Declaração Universal de 1948, Pactos de 1966 (civis/políticos e sociais).",
    "Sistema regional interamericano (OEA): Convenção Americana (Pacto de San José da Costa Rica, 1969).",
    "Órgãos: Comissão Interamericana e Corte Interamericana de Direitos Humanos.",
    "O Brasil reconheceu a jurisdição contenciosa da Corte Interamericana em 1998.",
    "Controle de convencionalidade: compatibilização das leis internas com os tratados de direitos humanos."
   ], base:"Convenção Americana; Pactos de 1966"},
  {tema:"Controle de convencionalidade",
   enun:"Conceitue o controle de convencionalidade e suas espécies.",
   pontos:[
    "É a verificação de compatibilidade das normas internas com os tratados internacionais de direitos humanos.",
    "Parâmetro: tratados de direitos humanos (bloco de convencionalidade).",
    "Controle difuso (nacional): qualquer juiz pode afastar a norma incompatível com o tratado.",
    "Controle concentrado (internacional): exercido pela Corte Interamericana.",
    "Fundamenta-se no dever de os Estados darem efetividade aos tratados ratificados (boa-fé e pacta sunt servanda)."
   ], base:"Doutrina; Convenção Americana"}
]},

{id:"civ", bloco:"Direito Civil", curto:"Civil", itens:[
  {tema:"Personalidade e capacidade",
   enun:"Disserte sobre o início da personalidade civil e o regime das incapacidades após o Estatuto da Pessoa com Deficiência.",
   pontos:[
    "A personalidade civil começa do nascimento com vida; a lei põe a salvo, desde a concepção, os direitos do nascituro (art. 2º).",
    "Teorias sobre o nascituro: natalista, concepcionista e da personalidade condicional.",
    "Absolutamente incapazes: apenas os menores de 16 anos (art. 3º, após a Lei 13.146/15).",
    "Relativamente incapazes: 16 a 18 anos, ébrios/viciados, os que não puderem exprimir vontade e os pródigos (art. 4º).",
    "A pessoa com deficiência, em regra, é capaz; sujeita-se à tomada de decisão apoiada e, excepcionalmente, à curatela (que atinge atos patrimoniais)."
   ], base:"CC, arts. 2º a 4º; Lei 13.146/15"},
  {tema:"Prescrição e decadência",
   enun:"Diferencie prescrição e decadência, apontando efeitos e prazos gerais.",
   pontos:[
    "Prescrição atinge a pretensão (exigibilidade do direito) pela inércia; decadência atinge o próprio direito potestativo.",
    "Prazo geral de prescrição: 10 anos (art. 205), quando a lei não fixar prazo menor (art. 206).",
    "A prescrição admite impedimento, suspensão e interrupção; a decadência legal, em regra, não.",
    "A prescrição pode ser alegada em qualquer grau de jurisdição e reconhecida de ofício.",
    "A decadência legal é irrenunciável; a convencional pode ser renunciada."
   ], base:"CC, arts. 189, 205 e 206"},
  {tema:"Responsabilidade civil",
   enun:"Aponte os pressupostos da responsabilidade civil e distinga a subjetiva da objetiva.",
   pontos:[
    "Pressupostos: conduta (ação/omissão), culpa ou dolo (na subjetiva), nexo causal e dano.",
    "Responsabilidade subjetiva (regra, art. 186): depende da prova de culpa ou dolo.",
    "Responsabilidade objetiva: independe de culpa, nos casos previstos em lei ou pela teoria do risco (art. 927, §único).",
    "O dano pode ser material, moral ou estético, sendo cumuláveis (Súmula 387 STJ).",
    "Abuso de direito (art. 187) é ato ilícito e gera responsabilidade objetiva."
   ], base:"CC, arts. 186, 187 e 927"},
  {tema:"Posse",
   enun:"Discorra sobre a teoria da posse adotada pelo Código Civil e suas classificações.",
   pontos:[
    "O CC adotou a teoria OBJETIVA de Ihering: basta o exercício de fato dos poderes da propriedade (corpus), dispensando o animus domini.",
    "Posse direta e indireta (desdobramento, ex.: locador e locatário).",
    "Posse justa (sem violência, clandestinidade ou precariedade) × injusta.",
    "Posse de boa-fé × má-fé (ciência do vício), relevante para frutos, benfeitorias e usucapião.",
    "Efeitos: proteção possessória (interditos), usucapião, percepção de frutos e indenização por benfeitorias."
   ], base:"CC, arts. 1.196 e seguintes"}
]},

{id:"cri", bloco:"Criminologia", curto:"Criminologia", itens:[
  {tema:"Escola Clássica × Positiva",
   enun:"Diferencie a Escola Clássica e a Escola Positiva da criminologia.",
   pontos:[
    "Escola Clássica (Beccaria, Carrara): parte do livre-arbítrio; o crime é opção racional; foco no fato/delito; pena com função retributiva.",
    "Escola Positiva (Lombroso, Ferri, Garofalo): método empírico; determinismo; foco no criminoso.",
    "Lombroso: criminoso nato (antropologia criminal); Ferri: fatores sociais (sociologia criminal); Garofalo: delito natural.",
    "A pena, para o positivismo, tem função de defesa social e tratamento/ressocialização.",
    "A Clássica inaugura o direito penal liberal; a Positiva, a criminologia científica."
   ], base:"História da criminologia"},
  {tema:"Labeling approach",
   enun:"Explique a teoria do etiquetamento (labeling approach) e seus conceitos de criminalização.",
   pontos:[
    "O labeling approach (rotulação) sustenta que o desvio não é qualidade do ato, mas resultado da reação social que o rotula.",
    "Criminalização primária: criação da lei penal (seleção abstrata de condutas).",
    "Criminalização secundária: aplicação da lei pelas agências (polícia, MP, Judiciário), de forma seletiva.",
    "Desvio primário (conduta inicial) × desvio secundário (assunção do papel de desviante após a rotulação).",
    "Fundamenta a criminologia crítica e o garantismo; critica a cifra oculta e a seletividade penal."
   ], base:"Criminologia crítica"},
  {tema:"Prevenção criminal",
   enun:"Aponte os níveis de prevenção à criminalidade.",
   pontos:[
    "Prevenção primária: atua sobre as causas sociais do crime (educação, emprego, moradia) — longo prazo.",
    "Prevenção secundária: dirige-se a grupos e locais de risco (policiamento ostensivo, urbanismo).",
    "Prevenção terciária: destina-se ao condenado, buscando evitar a reincidência (ressocialização).",
    "A prevenção situacional reduz oportunidades do crime (teoria das atividades rotineiras).",
    "O delegado atua sobretudo na prevenção secundária e na repressão qualificada."
   ], base:"Criminologia aplicada"},
  {tema:"Vitimologia",
   enun:"Conceitue a vitimologia e os processos de vitimização.",
   pontos:[
    "Vitimologia estuda a vítima, seu papel no fato criminoso e as formas de proteção e reparação.",
    "Vitimização primária: dano sofrido diretamente com o crime.",
    "Vitimização secundária (sobrevitimização): sofrimento causado pelas instâncias formais (polícia, Justiça) ao reviver o fato.",
    "Vitimização terciária: estigmatização pela sociedade e pelo meio após o crime.",
    "A atuação policial deve reduzir a vitimização secundária (acolhimento, não revitimização)."
   ], base:"Vitimologia"}
]},

{id:"mle", bloco:"Medicina Legal", curto:"Medicina Legal", itens:[
  {tema:"Energias e lesões",
   enun:"Classifique as energias que produzem lesões corporais, de interesse médico-legal.",
   pontos:[
    "Energias de ordem MECÂNICA: ferimentos por instrumentos perfurantes, cortantes, contundentes e mistos.",
    "Energias de ordem FÍSICA: temperatura, eletricidade, pressão, radiação e luz.",
    "Energias de ordem QUÍMICA: cáusticos (ácidos e bases) e venenos.",
    "Energias FÍSICO-QUÍMICAS: asfixias (enforcamento, estrangulamento, esganadura, afogamento).",
    "Energias BIOQUÍMICAS (perturbações nutritivas), BIODINÂMICAS (funcionais) e de ordem MISTA."
   ], base:"Medicina legal — lesões"},
  {tema:"Tanatologia",
   enun:"Disserte sobre os fenômenos cadavéricos e a cronotanatognose.",
   pontos:[
    "Tanatologia estuda a morte e o cadáver; cronotanatognose é a estimativa do tempo de morte.",
    "Fenômenos abióticos imediatos: perda da consciência, abolição de sensibilidade, cessação da respiração e circulação.",
    "Fenômenos abióticos consecutivos: resfriamento (algor), livores (hipóstases), rigidez (rigor mortis) e desidratação.",
    "Fenômenos transformativos destrutivos: autólise e putrefação (inicia pela mancha verde abdominal).",
    "Fenômenos transformativos conservadores: mumificação, saponificação (adipocera) e calcificação."
   ], base:"Medicina legal — tanatologia"},
  {tema:"Sexologia forense",
   enun:"Aponte os principais temas da sexologia forense de interesse policial.",
   pontos:[
    "Conjunção carnal: introdução do pênis na cavidade vaginal; antes exigia ruptura himenal para prova.",
    "Atos libidinosos diversos: qualquer ato de natureza sexual que não a conjunção carnal.",
    "Vestígios: exame do hímen (complacente, roto), pesquisa de sêmen, lesões e DST.",
    "Importante para o estupro (art. 213 CP) e o estupro de vulnerável (art. 217-A CP).",
    "A palavra da vítima tem especial relevância nos crimes sexuais, praticados às ocultas."
   ], base:"Medicina legal — sexologia"},
  {tema:"Documentos médico-legais",
   enun:"Aponte os principais documentos médico-legais e suas finalidades.",
   pontos:[
    "Notificação: comunicação compulsória de fato (ex.: doenças, violência) às autoridades.",
    "Atestado: afirmação simples de um fato médico.",
    "Parecer: resposta a quesitos por especialista (consultor), sobre tese ou fato.",
    "Relatório: descrição minuciosa de perícia — pode ser auto (ditado na hora) ou laudo (redigido depois).",
    "O laudo pericial tem valor probatório relevante no inquérito e no processo penal."
   ], base:"Medicina legal — documentos"}
]}

];
