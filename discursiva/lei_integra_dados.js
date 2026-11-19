/* lei_integra_dados.js — dados do módulo "Lei na Íntegra" (aba do Treino de Letra de Lei, 19/11/2026).
 * O ARTIGO INTEIRO (caput + incisos + parágrafos) para estudo em 3 modos (Esconder / Teste / Revisão),
 * todos saindo deste MESMO registro. As palavras-chave vêm marcadas com {chaves}: no Esconder viram lacuna,
 * no Teste aparecem uma a uma, na Revisão ficam grifadas. "imp" marca o que mais cai (ganha "!"); "destaque"
 * é o campeão de pegadinha. "poder" num parágrafo pinta o grifo de ciano (titularidade do poder).
 * Texto OFICIAL da CF/88 (público); nada de terceiro entra aqui — só a incidência medida orientou a seleção.
 * Fase 1: Constituição, maior lacuna do guia "DECORANDO 02" (ver docs/PROCEDENCIA.md). */
window.LEI_INTEGRA = [
{d:"CF", art:"1º", titulo:"TÍTULO I — DOS PRINCÍPIOS FUNDAMENTAIS", rub:"Fundamentos da República",
 caput:"A República Federativa do Brasil, formada pela {união indissolúvel} dos Estados e Municípios e do Distrito Federal, constitui-se em {Estado Democrático de Direito} e tem como fundamentos:",
 incisos:[
  {n:"I", t:"a {soberania}", imp:true},
  {n:"II", t:"a {cidadania}", imp:true},
  {n:"III", t:"a {dignidade da pessoa humana}", imp:true, destaque:true},
  {n:"IV", t:"os {valores sociais do trabalho} e da livre iniciativa"},
  {n:"V", t:"o {pluralismo político}"}
 ],
 paragrafos:[
  {rot:"Parágrafo único.", t:"Todo o poder emana do {povo}, que o exerce por meio de representantes eleitos ou diretamente, nos termos desta Constituição.", imp:true, poder:true}
 ],
 mnem:"SO-CI-DI-VA-PLU", base:"CF, art. 1º"},

{d:"CF", art:"2º", titulo:"DOS PRINCÍPIOS FUNDAMENTAIS", rub:"Separação dos Poderes",
 caput:"São Poderes da União, independentes e {harmônicos} entre si, o {Legislativo}, o {Executivo} e o {Judiciário}.",
 incisos:[], paragrafos:[],
 mnem:"independentes e HARMÔNICOS", base:"CF, art. 2º"},

{d:"CF", art:"3º", titulo:"DOS PRINCÍPIOS FUNDAMENTAIS", rub:"Objetivos fundamentais",
 caput:"Constituem {objetivos fundamentais} da República Federativa do Brasil:",
 incisos:[
  {n:"I", t:"construir uma sociedade {livre, justa e solidária}", imp:true},
  {n:"II", t:"garantir o {desenvolvimento nacional}"},
  {n:"III", t:"erradicar a {pobreza} e a marginalização e reduzir as {desigualdades sociais e regionais}", imp:true, destaque:true},
  {n:"IV", t:"promover o {bem de todos}, sem preconceitos de origem, raça, sexo, cor, idade e quaisquer outras formas de discriminação", imp:true}
 ],
 paragrafos:[],
 mnem:"verbos: CONSTRUIR · GARANTIR · ERRADICAR · PROMOVER", base:"CF, art. 3º"},

{d:"CF", art:"4º", titulo:"DOS PRINCÍPIOS FUNDAMENTAIS", rub:"Princípios das relações internacionais",
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
 paragrafos:[
  {rot:"Parágrafo único.", t:"A República Federativa do Brasil buscará a {integração} econômica, política, social e cultural dos povos da {América Latina}, visando à formação de uma comunidade latino-americana de nações."}
 ],
 mnem:"Prevalência dos DIREITOS HUMANOS (II) e ASILO POLÍTICO (X) são os campeões", base:"CF, art. 4º"},

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
  {n:"XLVI", t:"a lei regulará a {individualização da pena}"},
  {n:"XLVII", t:"não haverá penas: de morte, salvo em caso de guerra declarada; de caráter {perpétuo}; de trabalhos forçados; de banimento; cruéis", imp:true},
  {n:"LIV", t:"ninguém será privado da liberdade ou de seus bens sem o {devido processo legal}", imp:true, destaque:true},
  {n:"LV", t:"aos litigantes, em processo judicial ou administrativo, e aos acusados em geral são assegurados o {contraditório} e a ampla defesa, com os meios e recursos a ela inerentes", imp:true, destaque:true},
  {n:"LVI", t:"são inadmissíveis, no processo, as provas obtidas por meios {ilícitos}", imp:true},
  {n:"LVII", t:"ninguém será considerado culpado até o {trânsito em julgado} de sentença penal condenatória", imp:true, destaque:true},
  {n:"LXI", t:"ninguém será preso senão em {flagrante delito} ou por ordem escrita e fundamentada de autoridade judiciária competente, salvo nos casos de transgressão militar ou crime propriamente militar, definidos em lei", imp:true, destaque:true},
  {n:"LXIII", t:"o preso será informado de seus direitos, entre os quais o de permanecer {calado}, sendo-lhe assegurada a assistência da família e de advogado", imp:true},
  {n:"LXV", t:"a prisão ilegal será imediatamente {relaxada} pela autoridade judiciária", imp:true},
  {n:"LXVIII", t:"conceder-se-á {habeas corpus} sempre que alguém sofrer ou se achar ameaçado de sofrer violência ou coação em sua liberdade de locomoção, por ilegalidade ou abuso de poder", imp:true},
  {n:"LXXVIII", t:"a todos, no âmbito judicial e administrativo, são assegurados a {razoável duração} do processo e os meios que garantam a celeridade de sua tramitação", imp:true}
 ],
 paragrafos:[
  {rot:"§ 3º", t:"Os tratados e convenções internacionais sobre direitos humanos que forem aprovados, em cada Casa do Congresso Nacional, em dois turnos, por três quintos dos votos dos respectivos membros, serão equivalentes às {emendas constitucionais}.", imp:true}
 ],
 mnem:"caput: VI-LI-I-SE-PRO (vida, liberdade, igualdade, segurança, propriedade)", base:"CF, art. 5º"},

{d:"CF", art:"37", titulo:"DA ADMINISTRAÇÃO PÚBLICA", rub:"Princípios e regras da administração",
 caput:"A administração pública direta e indireta de qualquer dos Poderes da União, dos Estados, do Distrito Federal e dos Municípios obedecerá aos princípios de {legalidade}, {impessoalidade}, {moralidade}, {publicidade} e {eficiência} e, também, ao seguinte:",
 incisos:[
  {n:"I", t:"os cargos, empregos e funções públicas são acessíveis aos {brasileiros} que preencham os requisitos estabelecidos em lei, assim como aos estrangeiros, na forma da lei"},
  {n:"II", t:"a investidura em cargo ou emprego público depende de aprovação prévia em {concurso público} de provas ou de provas e títulos, ressalvadas as nomeações para cargo em comissão declarado em lei de livre nomeação e exoneração", imp:true, destaque:true},
  {n:"V", t:"as funções de confiança, exercidas exclusivamente por servidores ocupantes de cargo efetivo, e os cargos em comissão destinam-se apenas às atribuições de {direção, chefia e assessoramento}", imp:true},
  {n:"VII", t:"o direito de greve será exercido nos termos e nos limites definidos em {lei específica}", imp:true},
  {n:"XVI", t:"é vedada a {acumulação remunerada} de cargos públicos, exceto, quando houver compatibilidade de horários, nas hipóteses previstas na Constituição", imp:true}
 ],
 paragrafos:[
  {rot:"§ 6º", t:"As pessoas jurídicas de direito público e as de direito privado prestadoras de serviços públicos responderão pelos danos que seus agentes, nessa qualidade, causarem a terceiros, assegurado o direito de {regresso} contra o responsável nos casos de dolo ou culpa.", imp:true, destaque:true}
 ],
 mnem:"LIMPE (Legalidade, Impessoalidade, Moralidade, Publicidade, Eficiência)", base:"CF, art. 37"}
];
