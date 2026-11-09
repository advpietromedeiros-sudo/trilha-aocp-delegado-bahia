// Pente Fino — Direito Processual Civil (DBA26-CPC-1 a 12). Gerado por ferramentas/pente_fino/construir.py em 07/11/2026.
// Esquema: docs/PENTE_FINO_ESQUEMA.md. Lei recortada de assets/lei_seca_oficial.json; jurisprudência conferida em fonte oficial.
window.PENTE_FINO = window.PENTE_FINO || {};
window.PENTE_FINO.CPC = {
 "disciplina": "Direito Processual Civil",
 "conferido_em": "07/11/2026",
 "fontes": [
  "Lei 13.105/2015 (CPC) — Planalto",
  "Lei 7.347/1985 (Ação Civil Pública) — Planalto",
  "Lei 4.717/1965 (Ação Popular) — Planalto",
  "Lei 12.016/2009 (Mandado de Segurança) — Planalto",
  "Lei 9.099/1995 (Juizados Especiais) — Planalto",
  "Lei 12.153/2009 (Juizados da Fazenda Pública) — Planalto",
  "Súmulas do STJ — processo.stj.jus.br/SCON/sumstj",
  "Temas repetitivos do STJ — processo.stj.jus.br/repetitivos",
  "Súmulas do STF — PDF oficial \"Enunciados das Súmulas do STF 1 a 736\" (stf.jus.br)",
  "STF — Tema 1.075/RG (portal.stf.jus.br) e ADI 4.296 (Informativo STF 1.021)"
 ],
 "pontos": [
  {
   "id": "DBA26-CPC-1",
   "titulo": "Das normas fundamentais e da aplicação das normas processuais."
  },
  {
   "id": "DBA26-CPC-2",
   "titulo": "Da função jurisdicional."
  },
  {
   "id": "DBA26-CPC-3",
   "titulo": "Dos sujeitos do processo."
  },
  {
   "id": "DBA26-CPC-4",
   "titulo": "Dos atos processuais."
  },
  {
   "id": "DBA26-CPC-5",
   "titulo": "Da tutela provisória."
  },
  {
   "id": "DBA26-CPC-6",
   "titulo": "Da formação, da suspensão e da extinção do processo."
  },
  {
   "id": "DBA26-CPC-7",
   "titulo": "Do processo de conhecimento e do cumprimento de sentença."
  },
  {
   "id": "DBA26-CPC-8",
   "titulo": "Do processo de execução."
  },
  {
   "id": "DBA26-CPC-9",
   "titulo": "Dos processos nos Tribunais e dos meios de impugnação das decisões judiciais."
  },
  {
   "id": "DBA26-CPC-10",
   "titulo": "Ação civil pública, ação popular e mandado de segurança."
  },
  {
   "id": "DBA26-CPC-11",
   "titulo": "Juizados Especiais Cíveis e da Fazenda Pública."
  },
  {
   "id": "DBA26-CPC-12",
   "titulo": "Jurisprudência aplicada dos tribunais superiores e legislação aplicável a cada um dos tópicos do edital."
  }
 ],
 "rodadas": [
  {
   "n": 1,
   "titulo": "Rodada 1 · O essencial",
   "itens": [
    {
     "id": "CPC-1-R1-01",
     "ponto": "DBA26-CPC-1",
     "tema": "Princípio dispositivo e impulso oficial",
     "assertiva": "O processo civil começa por iniciativa da parte e se desenvolve por impulso oficial, salvo as exceções previstas em lei.",
     "gabarito": "C",
     "comentario": {
      "resumo": "É a literalidade do art. 2º: **inércia** para começar (iniciativa da parte) e **impulso oficial** para andar.",
      "lei": [
       {
        "lei": "L13105",
        "art": "2",
        "par": "",
        "inc": "",
        "rotulo": "CPC, art. 2º",
        "texto": "O processo começa por iniciativa da parte e se desenvolve por impulso oficial, salvo as exceções previstas em lei."
       }
      ],
      "palavras_chave": [
       "inércia",
       "impulso oficial"
      ],
      "aprofundamento": "O art. 2º combina dois princípios que convivem sem conflito. O **princípio dispositivo** (ou da inércia) protege a imparcialidade: o juiz que escolhe quais conflitos vai julgar deixa de ser terceiro desinteressado. Por isso quem provoca a jurisdição é a parte, que também delimita o objeto do processo com o pedido.\n\nUma vez provocado, porém, o processo não fica à mercê da vontade das partes. O **impulso oficial** faz o juiz conduzir o feito de fase em fase, porque há interesse público na solução do litígio e na duração razoável.\n\nA ressalva final (\"salvo as exceções previstas em lei\") é a que a banca costuma apagar. Há situações excepcionais em que a lei admite atuação judicial sem provocação, e por isso uma assertiva que diga que o juiz \"jamais\" age de ofício para iniciar algo tende a estar errada.",
      "exemplo": "Maria tem um crédito vencido, mas não ajuíza ação: o juiz não pode, por conta própria, abrir processo de cobrança. Ajuizada a ação, o juiz manda citar e marca audiência sem esperar novo pedido dela.",
      "memorize": "Começa pela parte (inércia), anda pelo juiz (impulso oficial), salvo exceção legal."
     }
    },
    {
     "id": "CPC-1-R1-02",
     "ponto": "DBA26-CPC-1",
     "tema": "Métodos consensuais",
     "assertiva": "A conciliação, a mediação e outros métodos de solução consensual de conflitos deverão ser estimulados por juízes, advogados, defensores públicos e membros do Ministério Público, vedada sua utilização depois de instaurado o processo judicial.",
     "gabarito": "E",
     "comentario": {
      "resumo": "O estímulo vale **inclusive no curso do processo judicial**. A banca acrescentou uma vedação que a lei não traz.",
      "lei": [
       {
        "lei": "L13105",
        "art": "3",
        "par": "",
        "inc": "",
        "rotulo": "CPC, art. 3º, § 3º",
        "texto": "A conciliação, a mediação e outros métodos de solução consensual de conflitos deverão ser estimulados por juízes, advogados, defensores públicos e membros do Ministério Público, inclusive no curso do processo judicial."
       }
      ],
      "pegadinha": "Troca de \"inclusive no curso do processo\" por \"vedada no curso do processo\".",
      "palavras_chave": [
       "autocomposição",
       "mediação",
       "conciliação"
      ],
      "correcao": {
       "erro": "Afirma que os métodos consensuais ficam vedados depois de instaurado o processo judicial.",
       "certo": "A conciliação, a mediação e outros métodos consensuais deverão ser estimulados por juízes, advogados, defensores públicos e membros do MP, inclusive no curso do processo judicial."
      },
      "aprofundamento": "O CPC adotou a ideia de um sistema **multiportas**: a sentença é apenas uma das formas de resolver o conflito, e nem sempre a melhor. O acordo construído pelas partes tende a ser cumprido voluntariamente, pacifica a relação e desafoga o Judiciário. Daí o dever, dirigido a todos os profissionais do processo, de estimular a solução consensual.\n\nEsse estímulo não se esgota antes da ação. O código o espalha pelo procedimento: audiência de conciliação ou mediação no início do procedimento comum, tentativa de conciliação na audiência de instrução e a possibilidade de homologar acordo a qualquer tempo, até em grau de recurso.\n\nA banca transforma a frase em errada acrescentando uma **vedação temporal** que a lei não traz. Desconfie de \"vedada\", \"somente antes\" ou \"exclusivamente na fase pré-processual\" quando o tema é autocomposição.",
      "memorize": "Autocomposição se estimula sempre, inclusive no curso do processo."
     }
    },
    {
     "id": "CPC-1-R1-03",
     "ponto": "DBA26-CPC-1",
     "tema": "Duração razoável e primazia do mérito",
     "assertiva": "As partes têm o direito de obter em prazo razoável a solução integral do mérito, incluída a atividade satisfativa.",
     "gabarito": "C",
     "comentario": {
      "resumo": "Art. 4º: a **duração razoável** abrange também a **atividade satisfativa** (cumprimento/execução), não só a sentença.",
      "lei": [
       {
        "lei": "L13105",
        "art": "4",
        "par": "",
        "inc": "",
        "rotulo": "CPC, art. 4º",
        "texto": "As partes têm o direito de obter em prazo razoável a solução integral do mérito, incluída a atividade satisfativa."
       }
      ],
      "palavras_chave": [
       "duração razoável",
       "primazia do mérito",
       "atividade satisfativa"
      ],
      "aprofundamento": "O art. 4º reúne duas ideias. A primeira é a **duração razoável**, garantia que também tem assento constitucional: processo que demora demais nega a própria tutela. A segunda é a **primazia do julgamento de mérito**: o processo existe para resolver o conflito, e não para terminar em extinção por vício formal sanável.\n\nO detalhe que a banca explora é a expressão \"incluída a atividade satisfativa\". De nada adianta uma sentença rápida se o credor leva anos para receber. Por isso a garantia alcança o cumprimento de sentença e a execução, isto é, a efetiva entrega do bem da vida.\n\nDessa norma derivam deveres concretos do juiz, como o de dar oportunidade para a parte corrigir vícios antes de extinguir o processo sem resolução do mérito.",
      "memorize": "Prazo razoável vale até a satisfação: mérito integral + atividade satisfativa."
     }
    },
    {
     "id": "CPC-1-R1-04",
     "ponto": "DBA26-CPC-1",
     "tema": "Cooperação",
     "assertiva": "O dever de cooperação previsto no CPC vincula apenas as partes e seus procuradores, não alcançando o juiz, que deve manter-se equidistante.",
     "gabarito": "E",
     "comentario": {
      "resumo": "Art. 6º: **todos os sujeitos do processo** devem cooperar — inclusive o juiz (deveres de esclarecimento, prevenção, consulta e auxílio).",
      "lei": [
       {
        "lei": "L13105",
        "art": "6",
        "par": "",
        "inc": "",
        "rotulo": "CPC, art. 6º",
        "texto": "Todos os sujeitos do processo devem cooperar entre si para que se obtenha, em tempo razoável, decisão de mérito justa e efetiva."
       }
      ],
      "palavras_chave": [
       "cooperação",
       "sujeitos do processo"
      ],
      "correcao": {
       "erro": "Restringe o dever de cooperação às partes e procuradores, excluindo o juiz.",
       "certo": "Todos os sujeitos do processo, inclusive o juiz, devem cooperar entre si para que se obtenha, em tempo razoável, decisão de mérito justa e efetiva."
      },
      "aprofundamento": "O modelo **cooperativo** do CPC rompe com a ideia de um juiz espectador e também com a de um juiz autoritário. O processo passa a ser uma comunidade de trabalho em que todos os sujeitos, inclusive o magistrado, contribuem para uma decisão de mérito justa e efetiva em tempo razoável.\n\nPara o juiz, a cooperação se traduz em deveres concretos: **esclarecimento** (pedir às partes que expliquem pontos obscuros), **prevenção** (apontar vícios e permitir a correção), **consulta** (ouvir antes de decidir) e **auxílio** (ajudar a parte a superar obstáculos). Cooperar não quebra a imparcialidade, porque não significa favorecer um lado, e sim conduzir o processo com lealdade e transparência.\n\nA pegadinha está na palavra \"apenas\": o texto legal fala em \"todos os sujeitos do processo\".",
      "memorize": "Cooperação: TODOS os sujeitos, juiz incluído (esclarecer, prevenir, consultar, auxiliar)."
     }
    },
    {
     "id": "CPC-1-R1-05",
     "ponto": "DBA26-CPC-1",
     "tema": "Contraditório prévio e exceções",
     "assertiva": "Não se proferirá decisão contra uma das partes sem que ela seja previamente ouvida, regra que não admite exceção nem mesmo para a tutela provisória de urgência.",
     "gabarito": "E",
     "comentario": {
      "resumo": "O art. 9º tem **exceções expressas** no parágrafo único: aí o contraditório é **diferido**, não suprimido.",
      "regra": "Contraditório prévio (art. 9º, caput).",
      "excecoes": [
       "Tutela provisória de urgência (art. 9º, par. ún., I)",
       "Tutela da evidência do art. 311, II e III (art. 9º, par. ún., II)",
       "Decisão do art. 701 — mandado monitório (art. 9º, par. ún., III)"
      ],
      "lei": [
       {
        "lei": "L13105",
        "art": "9",
        "par": "",
        "inc": "",
        "rotulo": "CPC, art. 9º",
        "texto": "Não se proferirá decisão contra uma das partes sem que ela seja previamente ouvida."
       }
      ],
      "palavras_chave": [
       "contraditório diferido",
       "tutela de urgência"
      ],
      "correcao": {
       "erro": "Diz que o contraditório prévio não admite exceção, nem para a tutela de urgência.",
       "certo": "Não se profere decisão contra a parte sem ouvi-la previamente, salvo nas exceções do parágrafo único do art. 9º, entre elas a tutela provisória de urgência, em que o contraditório é diferido."
      },
      "aprofundamento": "O contraditório prévio é a regra porque decisão tomada sem ouvir o atingido tende a ser pior e viola a garantia de participação. Mas há casos em que ouvir antes destruiria a utilidade da medida: o réu avisado pode dilapidar bens ou consumar o dano. Nesses casos a lei não suprime o contraditório; ela o **adia**.\n\nO parágrafo único do art. 9º lista as exceções: a tutela de urgência, certas hipóteses de tutela da evidência e a decisão que expede o mandado monitório. Em todas, a parte é ouvida depois e pode impugnar a decisão. Esse é o **contraditório diferido**.\n\nA banca erra a frase com termos absolutos (\"não admite exceção\", \"em hipótese alguma\"). Quando o tema é contraditório, lembre que o código prevê expressamente as hipóteses em que a oitiva é posterior.",
      "exemplo": "Ana pede liminar para impedir a demolição de sua casa marcada para o dia seguinte. O juiz concede sem ouvir o réu, que será intimado e poderá impugnar depois.",
      "memorize": "Contraditório prévio é regra; urgência, parte da evidência e monitória = contraditório diferido."
     }
    },
    {
     "id": "CPC-1-R1-06",
     "ponto": "DBA26-CPC-1",
     "tema": "Vedação à decisão surpresa",
     "assertiva": "O juiz não pode decidir, em grau algum de jurisdição, com base em fundamento sobre o qual não se tenha dado às partes oportunidade de se manifestar, ainda que se trate de matéria que deva decidir de ofício.",
     "gabarito": "C",
     "comentario": {
      "resumo": "Art. 10: **matéria de ofício** não dispensa o **contraditório**. O juiz pode conhecer de ofício, mas tem de ouvir antes.",
      "lei": [
       {
        "lei": "L13105",
        "art": "10",
        "par": "",
        "inc": "",
        "rotulo": "CPC, art. 10",
        "texto": "O juiz não pode decidir, em grau algum de jurisdição, com base em fundamento a respeito do qual não se tenha dado às partes oportunidade de se manifestar, ainda que se trate de matéria sobre a qual deva decidir de ofício."
       }
      ],
      "pegadinha": "A banca costuma dizer que a vedação \"não se aplica às matérias de ordem pública\" — errado.",
      "palavras_chave": [
       "decisão surpresa",
       "matéria de ofício"
      ],
      "aprofundamento": "O art. 10 consagra a **vedação à decisão surpresa**, que é a face substancial do contraditório. Não basta a parte poder falar; ela precisa ter a chance de influenciar a decisão sobre o fundamento que será efetivamente usado. Se o juiz decide por um argumento que ninguém debateu, a participação foi apenas formal.\n\nO ponto delicado é separar **conhecer de ofício** de **decidir sem ouvir**. Prescrição, decadência, incompetência absoluta e outras matérias de ordem pública podem ser suscitadas pelo juiz sem provocação. O que a regra exige é que, antes de decidir com base nelas, ele abra oportunidade para as partes se manifestarem.\n\nA regra vale \"em grau algum de jurisdição\", ou seja, também nos tribunais. Frase que exclua as matérias de ordem pública da vedação está errada.",
      "exemplo": "O juiz percebe, sozinho, que o crédito pode estar prescrito. Antes de sentenciar, intima autor e réu para se manifestarem sobre a prescrição.",
      "memorize": "Matéria de ofício não dispensa ouvir as partes: pode conhecer, mas tem de consultar antes."
     }
    },
    {
     "id": "CPC-1-R1-07",
     "ponto": "DBA26-CPC-1",
     "tema": "Publicidade e fundamentação",
     "assertiva": "Todos os julgamentos dos órgãos do Poder Judiciário serão públicos, e fundamentadas todas as decisões, sob pena de nulidade.",
     "gabarito": "C",
     "comentario": {
      "resumo": "Art. 11, caput, que repete o art. 93, IX, da CF: **publicidade** + **fundamentação**, sob pena de **nulidade**.",
      "excecoes": [
       "Segredo de justiça: pode ser autorizada a presença somente das partes, advogados, defensores públicos ou MP (art. 11, par. ún.)"
      ],
      "lei": [
       {
        "lei": "L13105",
        "art": "11",
        "par": "",
        "inc": "",
        "rotulo": "CPC, art. 11",
        "texto": "Todos os julgamentos dos órgãos do Poder Judiciário serão públicos, e fundamentadas todas as decisões, sob pena de nulidade."
       }
      ],
      "palavras_chave": [
       "publicidade",
       "fundamentação",
       "nulidade"
      ],
      "aprofundamento": "Publicidade e fundamentação são garantias de **controle**. A publicidade permite que a sociedade e as partes fiscalizem a atuação judicial; a fundamentação permite saber por que se decidiu assim e, com isso, recorrer de forma útil. Decisão sem motivação é arbítrio, e por isso a sanção é a **nulidade**.\n\nA publicidade, porém, não é absoluta. Nos casos de segredo de justiça, a lei autoriza restringir a presença às partes, advogados, defensores e MP, para proteger a intimidade ou o interesse público. Já a fundamentação não tem exceção: todas as decisões devem ser fundamentadas, inclusive as que tramitam em segredo.\n\nA banca costuma trocar a consequência (\"mera irregularidade\" no lugar de nulidade) ou estender o segredo de justiça à dispensa de motivação.",
      "memorize": "Julgamento público (salvo segredo) e TODA decisão fundamentada, sob pena de nulidade."
     }
    },
    {
     "id": "CPC-1-R1-08",
     "ponto": "DBA26-CPC-1",
     "tema": "Ordem cronológica de conclusão",
     "assertiva": "Os juízes e os tribunais atenderão obrigatoriamente à ordem cronológica de conclusão para proferir sentença ou acórdão.",
     "gabarito": "E",
     "comentario": {
      "resumo": "Desde a Lei 13.256/2016 o art. 12 diz **preferencialmente**, não \"obrigatoriamente\".",
      "lei": [
       {
        "lei": "L13105",
        "art": "12",
        "par": "",
        "inc": "",
        "rotulo": "CPC, art. 12",
        "texto": "Os juízes e os tribunais atenderão, preferencialmente, à ordem cronológica de conclusão para proferir sentença ou acórdão."
       }
      ],
      "pegadinha": "\"Preferencialmente\" x \"obrigatoriamente\" — troca clássica.",
      "palavras_chave": [
       "ordem cronológica",
       "preferencialmente"
      ],
      "correcao": {
       "erro": "Diz que a observância da ordem cronológica é obrigatória.",
       "certo": "Os juízes e os tribunais atenderão, preferencialmente, à ordem cronológica de conclusão para proferir sentença ou acórdão."
      },
      "aprofundamento": "A ordem cronológica de conclusão nasceu para dar **isonomia e transparência**: evitar que processos sejam escolhidos para julgamento por critérios pessoais. Na redação original do CPC, o comando era impositivo, mas a experiência mostrou que a rigidez travava a gestão dos gabinetes.\n\nA Lei 13.256/2016 trocou a expressão por \"**preferencialmente**\". Continua existindo a lista de processos conclusos, que deve estar disponível para consulta pública, mas o juiz tem margem para gerir a pauta.\n\nÉ uma das pegadinhas mais frequentes do CPC: a banca reproduz o texto original, revogado, com o advérbio \"obrigatoriamente\". Diante desse tema, procure o advérbio antes de tudo.",
      "memorize": "Ordem cronológica: PREFERENCIALMENTE (Lei 13.256/2016), não obrigatoriamente."
     }
    },
    {
     "id": "CPC-1-R1-09",
     "ponto": "DBA26-CPC-1",
     "tema": "Jurisdição civil e tratados",
     "assertiva": "A jurisdição civil será regida unicamente pelas normas processuais brasileiras, ressalvadas as disposições específicas previstas em tratados, convenções ou acordos internacionais de que o Brasil seja parte.",
     "gabarito": "C",
     "comentario": {
      "resumo": "Art. 13: regra da **lex fori**, com ressalva dos **tratados** internacionais.",
      "lei": [
       {
        "lei": "L13105",
        "art": "13",
        "par": "",
        "inc": "",
        "rotulo": "CPC, art. 13",
        "texto": "A jurisdição civil será regida pelas normas processuais brasileiras, ressalvadas as disposições específicas previstas em tratados, convenções ou acordos internacionais de que o Brasil seja parte."
       }
      ],
      "palavras_chave": [
       "lex fori",
       "tratados"
      ],
      "aprofundamento": "O processo é instrumento de exercício do poder estatal, e por isso cada Estado aplica as **suas próprias normas processuais** quando julga (lex fori). Não faz sentido o juiz brasileiro seguir o rito de outro país só porque a causa tem um elemento estrangeiro.\n\nIsso não se confunde com o direito material: o juiz brasileiro pode ter de aplicar lei estrangeira para resolver o mérito, conforme as regras de direito internacional privado, mas o procedimento, os prazos e os recursos são os brasileiros.\n\nA ressalva dos **tratados** existe porque o Brasil, ao aderir a um acordo internacional, incorpora regras específicas (de cooperação, citação, prova no exterior) que prevalecem naquele ponto. A palavra \"unicamente\" da assertiva convive com a ressalva expressa, por isso a frase está correta.",
      "memorize": "Processo no Brasil segue a lei processual brasileira, ressalvados os tratados."
     }
    },
    {
     "id": "CPC-1-R1-10",
     "ponto": "DBA26-CPC-1",
     "tema": "Lei processual no tempo",
     "assertiva": "A norma processual nova aplica-se somente aos processos ajuizados após o início de sua vigência.",
     "gabarito": "E",
     "comentario": {
      "resumo": "Art. 14: a norma processual **não retroage**, mas tem **aplicação imediata aos processos em curso**, respeitados os atos praticados (teoria do **isolamento dos atos processuais**).",
      "lei": [
       {
        "lei": "L13105",
        "art": "14",
        "par": "",
        "inc": "",
        "rotulo": "CPC, art. 14",
        "texto": "A norma processual não retroagirá e será aplicável imediatamente aos processos em curso, respeitados os atos processuais praticados e as situações jurídicas consolidadas sob a vigência da norma revogada."
       }
      ],
      "palavras_chave": [
       "isolamento dos atos processuais",
       "aplicação imediata"
      ],
      "correcao": {
       "erro": "Restringe a lei processual nova aos processos ajuizados após sua vigência.",
       "certo": "A norma processual não retroage e aplica-se imediatamente aos processos em curso, respeitados os atos praticados e as situações consolidadas sob a lei revogada."
      },
      "aprofundamento": "Lei processual nova enfrenta um problema prático: milhares de processos estão em andamento. O sistema brasileiro adota a teoria do **isolamento dos atos processuais**: cada ato é regido pela lei vigente no momento em que é praticado. A nova norma não atinge o que já foi feito, mas governa os atos futuros, mesmo em processos antigos.\n\nA razão é dupla. Não retroagir protege a segurança jurídica e as situações consolidadas; aplicar de imediato evita que convivam por décadas dois códigos para processos semelhantes.\n\nO erro típico da banca é dizer que a lei nova vale \"somente\" para processos ajuizados depois de sua vigência. Isso corresponde à teoria da unidade processual, que o código não adotou.",
      "exemplo": "Um processo está em curso quando entra em vigor lei que muda um prazo recursal. O recurso interposto antes segue a lei velha; o interposto depois, a lei nova.",
      "memorize": "Lei processual: não retroage, mas vale já nos processos em curso (isolamento dos atos)."
     }
    },
    {
     "id": "CPC-1-R1-11",
     "ponto": "DBA26-CPC-1",
     "tema": "Aplicação supletiva e subsidiária",
     "assertiva": "Na ausência de normas que regulem processos eleitorais, trabalhistas ou administrativos, as disposições do CPC lhes serão aplicadas supletiva e subsidiariamente.",
     "gabarito": "C",
     "comentario": {
      "resumo": "Art. 15: o CPC é o **diploma geral** do processo — aplicação **supletiva e subsidiária** a esses três ramos.",
      "lei": [
       {
        "lei": "L13105",
        "art": "15",
        "par": "",
        "inc": "",
        "rotulo": "CPC, art. 15",
        "texto": "Na ausência de normas que regulem processos eleitorais, trabalhistas ou administrativos, as disposições deste Código lhes serão aplicadas supletiva e subsidiariamente."
       }
      ],
      "palavras_chave": [
       "supletiva",
       "subsidiária"
      ],
      "aprofundamento": "O CPC funciona como o **código geral** do processo brasileiro. Os processos eleitoral, trabalhista e administrativo têm leis próprias, mas elas não regulam tudo, e o CPC preenche os espaços.\n\nAs duas palavras têm sentidos distintos. Aplicação **subsidiária** ocorre quando a lei especial é omissa sobre um instituto inteiro. Aplicação **supletiva** ocorre quando a lei especial trata do tema, mas de forma incompleta, e o CPC complementa. Em ambos os casos, o CPC não se sobrepõe à norma especial compatível.\n\nA banca costuma trocar o rol (incluir o processo penal, por exemplo) ou dizer que a aplicação é \"apenas subsidiária\". Fixe os três ramos do artigo e os dois advérbios.",
      "memorize": "CPC supre e subsidia: eleitoral, trabalhista e administrativo."
     }
    },
    {
     "id": "CPC-1-R1-12",
     "ponto": "DBA26-CPC-1",
     "tema": "Aplicação do ordenamento pelo juiz",
     "assertiva": "Ao aplicar o ordenamento jurídico, o juiz atenderá aos fins sociais e às exigências do bem comum, resguardando e promovendo a dignidade da pessoa humana e observando a proporcionalidade, a razoabilidade, a legalidade, a publicidade e a eficiência.",
     "gabarito": "C",
     "comentario": {
      "resumo": "Art. 8º: **fins sociais**, **bem comum**, **dignidade** e os vetores da proporcionalidade, razoabilidade, legalidade, publicidade e eficiência.",
      "lei": [
       {
        "lei": "L13105",
        "art": "8",
        "par": "",
        "inc": "",
        "rotulo": "CPC, art. 8º",
        "texto": "Ao aplicar o ordenamento jurídico, o juiz atenderá aos fins sociais e às exigências do bem comum, resguardando e promovendo a dignidade da pessoa humana e observando a proporcionalidade, a razoabilidade, a legalidade, a publicidade e a eficiência."
       }
      ],
      "palavras_chave": [
       "fins sociais",
       "dignidade",
       "proporcionalidade"
      ],
      "aprofundamento": "O art. 8º traz os **vetores de interpretação** que o juiz deve observar ao aplicar o direito. A referência aos fins sociais e ao bem comum vem da tradição da Lei de Introdução; a dignidade da pessoa humana e os princípios da administração pública mostram a leitura constitucional do processo.\n\nA presença de legalidade, publicidade e eficiência, típicos do direito administrativo, sinaliza que a jurisdição também é atividade estatal e deve ser prestada de forma eficiente e controlável. Proporcionalidade e razoabilidade servem para ponderar quando há colisão de valores.\n\nNa prova, a banca costuma suprimir um dos vetores ou trocá-lo por outro que não está no artigo, como \"moralidade\" ou \"impessoalidade\". Vale memorizar a lista na ordem do texto.",
      "memorize": "Fins sociais, bem comum, dignidade + proporcionalidade, razoabilidade, legalidade, publicidade, eficiência."
     }
    },
    {
     "id": "CPC-2-R1-01",
     "ponto": "DBA26-CPC-2",
     "tema": "Jurisdição civil",
     "assertiva": "A jurisdição civil é exercida pelos juízes e pelos tribunais em todo o território nacional, conforme as disposições do CPC.",
     "gabarito": "C",
     "comentario": {
      "resumo": "Art. 16: a jurisdição é **una** e exercida em **todo o território nacional**; a competência é que a reparte.",
      "lei": [
       {
        "lei": "L13105",
        "art": "16",
        "par": "",
        "inc": "",
        "rotulo": "CPC, art. 16",
        "texto": "A jurisdição civil é exercida pelos juízes e pelos tribunais em todo o território nacional, conforme as disposições deste Código."
       }
      ],
      "palavras_chave": [
       "jurisdição",
       "competência"
      ],
      "aprofundamento": "A **jurisdição é una**: é a mesma função estatal, seja exercida por um juiz de primeiro grau, seja por um tribunal superior. Todo juiz tem jurisdição; o que varia é a parcela dela que ele pode exercer em cada caso, e essa medida chama-se **competência**.\n\nPor isso a assertiva fala em \"todo o território nacional\": não há uma jurisdição estadual e outra federal no sentido de poderes diferentes, e sim uma única função, repartida por critérios de competência (matéria, pessoa, função, valor e território).\n\nA banca costuma confundir os conceitos, dizendo, por exemplo, que o juiz incompetente \"não tem jurisdição\". Ele tem jurisdição, mas não competência para aquela causa.",
      "memorize": "Jurisdição é una e nacional; competência é a medida dela."
     }
    },
    {
     "id": "CPC-2-R1-02",
     "ponto": "DBA26-CPC-2",
     "tema": "Condições da ação",
     "assertiva": "Para postular em juízo é necessário ter interesse, legitimidade e possibilidade jurídica do pedido.",
     "gabarito": "E",
     "comentario": {
      "resumo": "O art. 17 exige só **interesse e legitimidade**. A possibilidade jurídica do pedido saiu do rol no CPC/2015 (virou questão de mérito).",
      "lei": [
       {
        "lei": "L13105",
        "art": "17",
        "par": "",
        "inc": "",
        "rotulo": "CPC, art. 17",
        "texto": "Para postular em juízo é necessário ter interesse e legitimidade."
       }
      ],
      "pegadinha": "Inclusão da \"possibilidade jurídica do pedido\", que era do CPC/1973.",
      "palavras_chave": [
       "interesse",
       "legitimidade",
       "possibilidade jurídica"
      ],
      "correcao": {
       "erro": "Inclui a possibilidade jurídica do pedido entre os requisitos para postular em juízo.",
       "certo": "Para postular em juízo é necessário ter interesse e legitimidade."
      },
      "aprofundamento": "As condições da ação são requisitos para que o juiz possa examinar o mérito. O CPC atual manteve apenas duas: **interesse** (necessidade e utilidade da tutela pedida) e **legitimidade** (pertinência subjetiva entre as partes e a relação discutida).\n\nA possibilidade jurídica do pedido saiu do rol porque, na prática, examinar se o pedido é admitido pelo ordenamento já é julgar o mérito. Um pedido juridicamente impossível hoje leva à improcedência, com sentença de mérito apta a fazer coisa julgada material, e não à extinção sem resolução do mérito.\n\nA banca reaproveita a fórmula tríplice do código anterior. Se a assertiva tratar a possibilidade jurídica como requisito para postular no CPC vigente, está errada.",
      "memorize": "CPC atual: interesse + legitimidade. Possibilidade jurídica virou mérito."
     }
    },
    {
     "id": "CPC-2-R1-03",
     "ponto": "DBA26-CPC-2",
     "tema": "Legitimação extraordinária",
     "assertiva": "Ninguém poderá pleitear direito alheio em nome próprio, salvo quando autorizado por lei em sentido estrito.",
     "gabarito": "E",
     "comentario": {
      "resumo": "O art. 18 fala em autorização pelo **ordenamento jurídico** — conceito mais amplo que \"lei\".",
      "lei": [
       {
        "lei": "L13105",
        "art": "18",
        "par": "",
        "inc": "",
        "rotulo": "CPC, art. 18",
        "texto": "Ninguém poderá pleitear direito alheio em nome próprio, salvo quando autorizado pelo ordenamento jurídico."
       }
      ],
      "pegadinha": "\"Ordenamento jurídico\" trocado por \"lei\".",
      "palavras_chave": [
       "substituição processual",
       "legitimação extraordinária"
      ],
      "correcao": {
       "erro": "Exige autorização por lei em sentido estrito para a legitimação extraordinária.",
       "certo": "Ninguém poderá pleitear direito alheio em nome próprio, salvo quando autorizado pelo ordenamento jurídico."
      },
      "aprofundamento": "A regra é a **legitimação ordinária**: cada um defende em juízo o próprio direito. A exceção é a **legitimação extraordinária** (substituição processual), em que alguém atua em nome próprio na defesa de direito alheio, como ocorre com o MP, as associações ou o sindicato em ações coletivas.\n\nO código atual ampliou a fonte dessa autorização. O texto revogado exigia lei; o vigente fala em \"ordenamento jurídico\", o que permite extrair a autorização do sistema como um todo, e não apenas de dispositivo legal expresso. Parte da doutrina admite inclusive legitimação extraordinária de origem negocial.\n\nA troca de \"ordenamento jurídico\" por \"lei\" (ou \"lei em sentido estrito\") é a pegadinha clássica.",
      "memorize": "Substituição processual: autorizada pelo ORDENAMENTO JURÍDICO, não só pela lei."
     }
    },
    {
     "id": "CPC-2-R1-04",
     "ponto": "DBA26-CPC-2",
     "tema": "Ação declaratória",
     "assertiva": "É admissível a ação meramente declaratória ainda que tenha ocorrido a violação do direito.",
     "gabarito": "C",
     "comentario": {
      "resumo": "**Art. 20.** E o interesse pode limitar-se à declaração da existência, inexistência ou modo de ser de relação jurídica ou da autenticidade/falsidade de documento (art. 19).",
      "lei": [
       {
        "lei": "L13105",
        "art": "20",
        "par": "",
        "inc": "",
        "rotulo": "CPC, art. 20",
        "texto": "É admissível a ação meramente declaratória, ainda que tenha ocorrido a violação do direito."
       }
      ],
      "palavras_chave": [
       "ação declaratória"
      ],
      "aprofundamento": "A ação declaratória busca apenas **certeza jurídica**: dizer se uma relação existe, não existe ou qual o seu modo de ser, ou se um documento é autêntico ou falso. O interesse está em eliminar a dúvida, que por si só já causa prejuízo.\n\nO art. 20 resolve uma questão que gerava debate: se o direito já foi violado, a parte poderia pedir uma condenação, então haveria interesse em pedir só a declaração? O código responde que sim. Cabe ao autor escolher a tutela que lhe interessa, e ele pode preferir só a declaração.\n\nA banca costuma dizer que, ocorrida a violação, faltaria interesse e só caberia ação condenatória. É exatamente o que o artigo afasta.",
      "memorize": "Declaratória cabe mesmo depois da violação do direito."
     }
    },
    {
     "id": "CPC-2-R1-05",
     "ponto": "DBA26-CPC-2",
     "tema": "Competência internacional exclusiva",
     "assertiva": "Compete à autoridade judiciária brasileira, com exclusão de qualquer outra, conhecer de ações relativas a imóveis situados no Brasil.",
     "gabarito": "C",
     "comentario": {
      "resumo": "Art. 23, I: **competência exclusiva**; decisão estrangeira sobre isso não é homologada (art. 964).",
      "lei": [
       {
        "lei": "L13105",
        "art": "23",
        "par": "",
        "inc": "",
        "rotulo": "CPC, art. 23, I",
        "texto": "Compete à autoridade judiciária brasileira, com exclusão de qualquer outra:\nI - conhecer de ações relativas a imóveis situados no Brasil;"
       }
      ],
      "palavras_chave": [
       "competência exclusiva",
       "imóveis"
      ],
      "aprofundamento": "A competência internacional pode ser **concorrente** (o Brasil julga, mas aceita também decisão estrangeira) ou **exclusiva** (só o Brasil julga). Imóveis situados no território nacional estão no segundo grupo porque envolvem soberania sobre o território, registro imobiliário e eficácia prática: a sentença sobre o imóvel terá de ser cumprida aqui.\n\nA consequência da exclusividade aparece na homologação: decisão estrangeira sobre esse tema não é homologada no Brasil, porque invadiria competência que a lei reserva à autoridade brasileira.\n\nA banca costuma tratar ações sobre imóveis no Brasil como competência concorrente ou dizer que bastaria a homologação para valer aqui. Note a expressão \"com exclusão de qualquer outra\", que é a marca da exclusividade.",
      "memorize": "Imóvel no Brasil = competência exclusiva; sentença estrangeira sobre ele não se homologa."
     }
    },
    {
     "id": "CPC-2-R1-06",
     "ponto": "DBA26-CPC-2",
     "tema": "Litispendência internacional",
     "assertiva": "A ação proposta perante tribunal estrangeiro induz litispendência e obsta que a autoridade judiciária brasileira conheça da mesma causa.",
     "gabarito": "E",
     "comentario": {
      "resumo": "Art. 24: **não induz litispendência** nem obsta o conhecimento da mesma causa no Brasil (ressalvados tratados).",
      "lei": [
       {
        "lei": "L13105",
        "art": "24",
        "par": "",
        "inc": "",
        "rotulo": "CPC, art. 24",
        "texto": "A ação proposta perante tribunal estrangeiro não induz litispendência e não obsta a que a autoridade judiciária brasileira conheça da mesma causa e das que lhe são conexas"
       }
      ],
      "palavras_chave": [
       "litispendência",
       "tribunal estrangeiro"
      ],
      "correcao": {
       "erro": "Afirma que a ação estrangeira induz litispendência e impede o juiz brasileiro de conhecer a causa.",
       "certo": "A ação proposta perante tribunal estrangeiro não induz litispendência e não obsta que a autoridade judiciária brasileira conheça da mesma causa e das conexas, ressalvados tratados."
      },
      "aprofundamento": "Litispendência é o impedimento de haver dois processos idênticos ao mesmo tempo. No plano internacional, porém, o processo estrangeiro não produz esse efeito no Brasil, porque é expressão da soberania de outro Estado, e o juiz brasileiro não fica vinculado a ele enquanto não houver decisão homologada.\n\nNa prática, as duas ações podem correr em paralelo. O que vai prevalecer depende do que primeiro se tornar eficaz no Brasil: a sentença brasileira transitada em julgado ou a sentença estrangeira homologada.\n\nA ressalva fica por conta de tratados internacionais que disponham em sentido diverso. A banca inverte a regra afirmando que a ação estrangeira \"induz litispendência\"; o texto diz exatamente o contrário.",
      "memorize": "Ação lá fora não gera litispendência aqui (salvo tratado)."
     }
    },
    {
     "id": "CPC-2-R1-07",
     "ponto": "DBA26-CPC-2",
     "tema": "Perpetuação da jurisdição",
     "assertiva": "A competência é determinada no momento do registro ou da distribuição da petição inicial, sendo irrelevantes as modificações de fato ou de direito ocorridas posteriormente, salvo quando suprimirem órgão judiciário ou alterarem a competência absoluta.",
     "gabarito": "C",
     "comentario": {
      "resumo": "Art. 43: **perpetuatio jurisdictionis**, com duas exceções: **supressão do órgão** e **alteração da competência absoluta**.",
      "lei": [
       {
        "lei": "L13105",
        "art": "43",
        "par": "",
        "inc": "",
        "rotulo": "CPC, art. 43",
        "texto": "Determina-se a competência no momento do registro ou da distribuição da petição inicial, sendo irrelevantes as modificações do estado de fato ou de direito ocorridas posteriormente, salvo quando suprimirem órgão judiciário ou alterarem a competência absoluta."
       }
      ],
      "palavras_chave": [
       "perpetuatio jurisdictionis",
       "registro ou distribuição"
      ],
      "aprofundamento": "A **perpetuação da jurisdição** dá estabilidade ao processo. Se cada mudança de domicílio, de valor ou de lei deslocasse a causa, o processo nunca terminaria e a parte poderia manipular a competência. Por isso o marco é fixo: o registro ou a distribuição da petição inicial.\n\nAs exceções têm lógica própria. Se o órgão judiciário é **suprimido**, não há como manter ali a causa. Se a lei altera a **competência absoluta**, prevalece o interesse público que justificou a mudança, e o processo é redistribuído.\n\nA banca costuma incluir exceções que não existem, como a mudança de domicílio do réu, ou fixar o marco na citação. Guarde: o marco é a distribuição ou o registro, e as exceções são só duas.",
      "exemplo": "João ajuíza ação no foro do domicílio do réu; meses depois o réu se muda para outro Estado. A causa continua no mesmo juízo.",
      "memorize": "Competência fixa-se no registro/distribuição; só muda se suprimir órgão ou alterar competência absoluta."
     }
    },
    {
     "id": "CPC-2-R1-08",
     "ponto": "DBA26-CPC-2",
     "tema": "Foro geral",
     "assertiva": "A ação fundada em direito pessoal ou em direito real sobre bens móveis será proposta, em regra, no foro de domicílio do réu.",
     "gabarito": "C",
     "comentario": {
      "resumo": "Art. 46: **foro comum = domicílio do réu**.",
      "lei": [
       {
        "lei": "L13105",
        "art": "46",
        "par": "",
        "inc": "",
        "rotulo": "CPC, art. 46",
        "texto": "A ação fundada em direito pessoal ou em direito real sobre bens móveis será proposta, em regra, no foro de domicílio do réu."
       }
      ],
      "palavras_chave": [
       "domicílio do réu",
       "foro comum"
      ],
      "aprofundamento": "O foro do domicílio do réu é o **foro comum** porque quem é chamado a juízo sem ter escolhido estar ali merece a facilidade de se defender perto de casa. O autor, que toma a iniciativa, suporta o ônus de litigar no foro do adversário.\n\nA regra cobre as ações fundadas em **direito pessoal** (contratos, responsabilidade civil, cobranças) e em direito real sobre **bens móveis**. Ela é geral e residual: aplica-se sempre que não houver foro especial previsto em lei. Trata-se de competência territorial, portanto relativa e modificável por eleição de foro.\n\nA expressão \"em regra\" é importante. A banca cobra a fronteira com os imóveis, que seguem o foro da situação da coisa, e com os foros especiais do código.",
      "memorize": "Direito pessoal ou real sobre móvel: domicílio do réu (regra, competência relativa)."
     }
    },
    {
     "id": "CPC-2-R1-09",
     "ponto": "DBA26-CPC-2",
     "tema": "Ações reais imobiliárias",
     "assertiva": "Para as ações fundadas em direito real sobre imóveis é competente, em regra, o foro de domicílio do réu.",
     "gabarito": "E",
     "comentario": {
      "resumo": "Art. 47: competente é o **foro de situação da coisa** (forum rei sitae).",
      "lei": [
       {
        "lei": "L13105",
        "art": "47",
        "par": "",
        "inc": "",
        "rotulo": "CPC, art. 47",
        "texto": "Para as ações fundadas em direito real sobre imóveis é competente o foro de situação da coisa."
       }
      ],
      "palavras_chave": [
       "forum rei sitae",
       "situação da coisa"
      ],
      "correcao": {
       "erro": "Aplica o foro do domicílio do réu às ações fundadas em direito real sobre imóveis.",
       "certo": "Para as ações fundadas em direito real sobre imóveis é competente o foro de situação da coisa."
      },
      "aprofundamento": "Nas ações reais imobiliárias, o foro é o da **situação da coisa** porque é ali que estão o imóvel, o cartório de registro e as provas (perícia, inspeção, testemunhas da região). Concentrar o processo nesse local facilita a instrução e o cumprimento da sentença.\n\nO critério é territorial, mas tem tratamento especial: nas ações sobre propriedade, vizinhança, servidão, divisão, demarcação, nunciação de obra nova e posse, a competência é absoluta, e o autor não pode escolher outro foro.\n\nA pegadinha da assertiva é aplicar a regra geral do domicílio do réu, que vale para direito pessoal e para bens móveis, a uma ação que envolve direito real sobre imóvel.",
      "memorize": "Direito real sobre imóvel: foro da situação da coisa (forum rei sitae)."
     }
    },
    {
     "id": "CPC-2-R1-10",
     "ponto": "DBA26-CPC-2",
     "tema": "Foro de eleição",
     "assertiva": "As partes podem modificar, por cláusula de eleição de foro, a competência em razão da matéria, da pessoa ou da função.",
     "gabarito": "E",
     "comentario": {
      "resumo": "Art. 62: essas competências são **inderrogáveis**. Por convenção só se mudam a competência em razão do **valor** e do **território** (art. 63).",
      "lei": [
       {
        "lei": "L13105",
        "art": "62",
        "par": "",
        "inc": "",
        "rotulo": "CPC, art. 62",
        "texto": "A competência determinada em razão da matéria, da pessoa ou da função é inderrogável por convenção das partes."
       },
       {
        "lei": "L13105",
        "art": "63",
        "par": "",
        "inc": "",
        "rotulo": "CPC, art. 63",
        "texto": "As partes podem modificar a competência em razão do valor e do território"
       }
      ],
      "palavras_chave": [
       "competência absoluta",
       "foro de eleição",
       "inderrogável"
      ],
      "correcao": {
       "erro": "Admite que a cláusula de eleição de foro altere a competência em razão da matéria, da pessoa ou da função.",
       "certo": "A competência em razão da matéria, da pessoa ou da função é inderrogável por convenção; as partes só podem modificar a competência em razão do valor e do território."
      },
      "aprofundamento": "A distinção entre competência **absoluta** e **relativa** está no interesse protegido. Matéria, pessoa e função são critérios fixados por interesse público na boa organização da justiça, e por isso as partes não podem negociá-los. Valor e território atendem sobretudo à conveniência das partes, e por isso admitem convenção.\n\nO foro de eleição é cláusula contratual escrita, que se refere a negócio jurídico determinado, e obriga herdeiros e sucessores. Se for abusiva, o juiz pode declará-la ineficaz.\n\nA banca transforma a frase em errada trocando os critérios: dizer que se pode eleger foro em razão da matéria ou da função é sempre falso, porque essas competências são inderrogáveis.",
      "memorize": "Eleição de foro: só valor e território. Matéria, pessoa e função são inderrogáveis."
     }
    },
    {
     "id": "CPC-2-R1-11",
     "ponto": "DBA26-CPC-2",
     "tema": "Incompetência absoluta",
     "assertiva": "A incompetência absoluta pode ser alegada em qualquer tempo e grau de jurisdição e deve ser declarada de ofício.",
     "gabarito": "C",
     "comentario": {
      "resumo": "Art. 64, § 1º. Mas atenção: decidida a questão e transitada em julgado, ela só se ataca por **rescisória** (art. 966, II).",
      "lei": [
       {
        "lei": "L13105",
        "art": "64",
        "par": "",
        "inc": "",
        "rotulo": "CPC, art. 64, § 1º",
        "texto": "A incompetência absoluta pode ser alegada em qualquer tempo e grau de jurisdição e deve ser declarada de ofício."
       }
      ],
      "palavras_chave": [
       "incompetência absoluta",
       "de ofício"
      ],
      "aprofundamento": "A incompetência absoluta viola regra de interesse público, e por isso não se convalida pela omissão das partes. Pode ser alegada a qualquer momento, por qualquer das partes, e o juiz deve reconhecê-la mesmo sem provocação, sempre ouvindo antes as partes, por força da vedação à decisão surpresa.\n\nReconhecida a incompetência, os autos vão ao juízo competente, e os efeitos das decisões do juízo incompetente são conservados até que o competente decida se as mantém.\n\nO limite está no **trânsito em julgado**: depois dele, a incompetência absoluta só pode ser atacada por **ação rescisória**. A banca costuma dizer que a alegação seria possível \"a qualquer tempo, mesmo após o trânsito\", o que ignora essa fronteira.",
      "memorize": "Incompetência absoluta: qualquer tempo e grau, de ofício; após o trânsito, só rescisória."
     }
    },
    {
     "id": "CPC-2-R1-12",
     "ponto": "DBA26-CPC-2",
     "tema": "Prorrogação da competência relativa",
     "assertiva": "Prorroga-se a competência relativa se o réu não a alegar por meio de exceção de incompetência, em peça autônoma, no prazo de 15 dias.",
     "gabarito": "E",
     "comentario": {
      "resumo": "No CPC/2015 a incompetência (absoluta ou relativa) é alegada como **preliminar de contestação** (art. 64); se o réu não alegar, **prorroga-se** (art. 65). Não há mais exceção em peça autônoma.",
      "lei": [
       {
        "lei": "L13105",
        "art": "64",
        "par": "",
        "inc": "",
        "rotulo": "CPC, art. 64",
        "texto": "A incompetência, absoluta ou relativa, será alegada como questão preliminar de contestação."
       },
       {
        "lei": "L13105",
        "art": "65",
        "par": "",
        "inc": "",
        "rotulo": "CPC, art. 65",
        "texto": "Prorrogar-se-á a competência relativa se o réu não alegar a incompetência em preliminar de contestação."
       }
      ],
      "pegadinha": "\"Exceção de incompetência\" é peça do CPC/1973.",
      "palavras_chave": [
       "prorrogação",
       "preliminar de contestação"
      ],
      "correcao": {
       "erro": "Exige a alegação da incompetência relativa por exceção, em peça autônoma.",
       "certo": "A incompetência relativa é alegada como preliminar de contestação; se o réu não a alegar, prorroga-se a competência."
      },
      "aprofundamento": "O CPC atual simplificou a defesa do réu: em vez de várias peças, concentra quase tudo na **contestação**. A incompetência, absoluta ou relativa, é alegada como **preliminar**, sem peça autônoma.\n\nA consequência da omissão é diferente conforme o tipo. A relativa, que protege interesse das partes, é **prorrogada** se o réu não a alegar: o juiz originalmente incompetente passa a ser competente. A absoluta não se prorroga e pode ser alegada depois.\n\nA assertiva erra ao manter a figura da \"exceção de incompetência\" em peça autônoma, típica do código revogado. Na prova, sempre que aparecer \"exceção de incompetência\", desconfie.",
      "memorize": "Incompetência (absoluta ou relativa) = preliminar de contestação. Relativa não alegada prorroga."
     }
    },
    {
     "id": "CPC-3-R1-01",
     "ponto": "DBA26-CPC-3",
     "tema": "Capacidade processual",
     "assertiva": "Toda pessoa que se encontre no exercício de seus direitos tem capacidade para estar em juízo.",
     "gabarito": "C",
     "comentario": {
      "resumo": "Art. 70: **capacidade processual** acompanha a capacidade de exercício.",
      "lei": [
       {
        "lei": "L13105",
        "art": "70",
        "par": "",
        "inc": "",
        "rotulo": "CPC, art. 70",
        "texto": "Toda pessoa que se encontre no exercício de seus direitos tem capacidade para estar em juízo."
       }
      ],
      "palavras_chave": [
       "capacidade processual"
      ],
      "aprofundamento": "O processo distingue três ideias. **Capacidade de ser parte** é a aptidão para figurar num processo. **Capacidade processual** (de estar em juízo) é a aptidão para praticar atos processuais sozinho, e acompanha a capacidade civil de exercício. **Capacidade postulatória** é a de falar tecnicamente nos autos, em regra do advogado.\n\nQuem não está no pleno exercício de seus direitos tem capacidade de ser parte, mas precisa ser representado ou assistido. Por isso um menor pode ser autor de ação de alimentos, desde que representado.\n\nA banca costuma embaralhar as três capacidades. Se a frase disser que a capacidade de estar em juízo depende da inscrição na OAB, está confundindo processual com postulatória.",
      "memorize": "Capacidade processual = capacidade civil de exercício; incapaz é parte, mas representado ou assistido."
     }
    },
    {
     "id": "CPC-3-R1-02",
     "ponto": "DBA26-CPC-3",
     "tema": "Curador especial",
     "assertiva": "O juiz nomeará curador especial ao réu preso, ainda que ele tenha comparecido aos autos e contestado por advogado constituído.",
     "gabarito": "E",
     "comentario": {
      "resumo": "Art. 72, II: curador especial ao **réu preso revel** e ao revel citado por edital ou hora certa **enquanto não constituído advogado**. Função exercida pela **Defensoria Pública** (par. ún.).",
      "lei": [
       {
        "lei": "L13105",
        "art": "72",
        "par": "",
        "inc": "",
        "rotulo": "CPC, art. 72, II",
        "texto": "II - réu preso revel, bem como ao réu revel citado por edital ou com hora certa, enquanto não for constituído advogado."
       }
      ],
      "palavras_chave": [
       "curador especial",
       "réu preso revel",
       "Defensoria Pública"
      ],
      "correcao": {
       "erro": "Determina curador especial ao réu preso mesmo que ele tenha contestado por advogado constituído.",
       "certo": "O juiz nomeará curador especial ao réu preso revel e ao revel citado por edital ou com hora certa, enquanto não for constituído advogado."
      },
      "aprofundamento": "O curador especial existe para garantir o contraditório de quem, por circunstâncias do processo, não tem condições reais de se defender. No caso do réu preso, a lei presume a dificuldade de contratar advogado e acompanhar o feito; no revel citado por edital ou por hora certa, há dúvida de que ele tenha efetivamente sabido da ação.\n\nPor isso a lei exige dois elementos: a **revelia** e a ausência de advogado constituído. Se o réu preso contestou por advogado, a defesa técnica já existe, e não há razão para nomear curador. A função é exercida pela **Defensoria Pública**.\n\nA assertiva erra ao dispensar o requisito da revelia. A expressão \"ainda que tenha contestado\" é o que a torna falsa.",
      "memorize": "Curador especial: réu preso REVEL e revel citado por edital/hora certa, sem advogado."
     }
    },
    {
     "id": "CPC-3-R1-03",
     "ponto": "DBA26-CPC-3",
     "tema": "Multa por litigância de má-fé",
     "assertiva": "O litigante de má-fé será condenado a pagar multa superior a 1% e inferior a 20% do valor corrigido da causa.",
     "gabarito": "E",
     "comentario": {
      "resumo": "Art. 81: multa **superior a 1% e inferior a 10%** do valor corrigido da causa, além de indenizar os prejuízos e pagar honorários e despesas.",
      "excecoes": [
       "Valor da causa irrisório ou inestimável: multa de até 10 salários mínimos (art. 81, § 2º)"
      ],
      "lei": [
       {
        "lei": "L13105",
        "art": "81",
        "par": "",
        "inc": "",
        "rotulo": "CPC, art. 81",
        "texto": "De ofício ou a requerimento, o juiz condenará o litigante de má-fé a pagar multa, que deverá ser superior a um por cento e inferior a dez por cento do valor corrigido da causa, a indenizar a parte contrária pelos prejuízos que esta sofreu e a arcar com os honorários advocatícios e com todas as despesas que efetuou."
       }
      ],
      "palavras_chave": [
       "má-fé",
       "multa",
       "10%"
      ],
      "correcao": {
       "erro": "Fixa o teto da multa por litigância de má-fé em 20% do valor da causa.",
       "certo": "A multa deve ser superior a 1% e inferior a 10% do valor corrigido da causa, além da indenização dos prejuízos, dos honorários e das despesas."
      },
      "aprofundamento": "A multa por litigância de má-fé tem natureza **punitiva**: sanciona a violação do dever de lealdade e boa-fé, como alterar a verdade dos fatos ou usar o processo para objetivo ilegal. Ela é diferente da indenização pelos prejuízos, que tem natureza reparatória, e as duas podem ser cumuladas, junto com honorários e despesas.\n\nA multa pode ser imposta de ofício ou a requerimento, e reverte em favor da parte contrária. Quando o valor da causa é irrisório ou inestimável, a lei troca a base percentual por um teto em salários mínimos.\n\nA banca altera o percentual. O intervalo correto é superior a 1% e inferior a 10%; o teto de 20% é o dos honorários de sucumbência, e é dessa confusão que vem a pegadinha.",
      "memorize": "Má-fé: multa entre 1% e 10%. Honorários: 10% a 20%. Não troque."
     }
    },
    {
     "id": "CPC-3-R1-04",
     "ponto": "DBA26-CPC-3",
     "tema": "Honorários de sucumbência",
     "assertiva": "Os honorários serão fixados entre o mínimo de 10% e o máximo de 20% sobre o valor da condenação, do proveito econômico obtido ou, não sendo possível mensurá-lo, sobre o valor atualizado da causa.",
     "gabarito": "C",
     "comentario": {
      "resumo": "Art. 85, § 2º: faixa de **10% a 20%**, nessa ordem de base de cálculo. Contra a Fazenda, as faixas escalonadas do § 3º.",
      "lei": [
       {
        "lei": "L13105",
        "art": "85",
        "par": "",
        "inc": "",
        "rotulo": "CPC, art. 85, § 2º",
        "texto": "Os honorários serão fixados entre o mínimo de dez e o máximo de vinte por cento sobre o valor da condenação, do proveito econômico obtido ou, não sendo possível mensurá-lo, sobre o valor atualizado da causa"
       }
      ],
      "palavras_chave": [
       "honorários",
       "10% a 20%"
      ],
      "aprofundamento": "Os honorários de sucumbência remuneram o advogado do vencedor e pertencem a ele, não à parte. A lei fixa uma faixa para que o juiz gradue conforme critérios como o grau de zelo, o lugar da prestação do serviço, a natureza e importância da causa e o trabalho realizado.\n\nA **base de cálculo** segue uma ordem preferencial: primeiro o valor da condenação; não havendo condenação, o proveito econômico obtido; e, não sendo possível mensurá-lo, o valor atualizado da causa. O juiz não escolhe livremente a base.\n\nQuando a Fazenda Pública é parte, o código prevê faixas escalonadas e menores conforme o valor. A banca costuma trocar a ordem das bases ou confundir a faixa com o percentual da multa por má-fé.",
      "memorize": "Honorários: 10% a 20% sobre condenação, depois proveito econômico, depois valor atualizado da causa."
     }
    },
    {
     "id": "CPC-3-R1-05",
     "ponto": "DBA26-CPC-3",
     "tema": "Gratuidade — presunção",
     "assertiva": "Presume-se verdadeira a alegação de insuficiência de recursos deduzida por pessoa jurídica.",
     "gabarito": "E",
     "comentario": {
      "resumo": "Art. 99, § 3º: a presunção vale para a alegação deduzida **exclusivamente por pessoa natural**. Pessoa jurídica tem de comprovar.",
      "lei": [
       {
        "lei": "L13105",
        "art": "99",
        "par": "",
        "inc": "",
        "rotulo": "CPC, art. 99, § 3º",
        "texto": "Presume-se verdadeira a alegação de insuficiência deduzida exclusivamente por pessoa natural."
       }
      ],
      "palavras_chave": [
       "gratuidade",
       "pessoa natural",
       "presunção"
      ],
      "correcao": {
       "erro": "Estende à pessoa jurídica a presunção de veracidade da alegação de insuficiência.",
       "certo": "Presume-se verdadeira a alegação de insuficiência deduzida exclusivamente por pessoa natural; a pessoa jurídica deve comprová-la."
      },
      "aprofundamento": "A gratuidade da justiça garante acesso ao Judiciário a quem não pode pagar custas e honorários sem prejuízo do próprio sustento. Para a **pessoa natural**, a lei facilita: basta a declaração de insuficiência, que se presume verdadeira, cabendo à parte contrária impugnar ou ao juiz indeferir se houver elementos que a contradigam.\n\nA pessoa jurídica também pode receber o benefício, mas sem presunção. Ela precisa **comprovar** a impossibilidade de arcar com os encargos, porque sua situação financeira é aferível por documentos contábeis.\n\nA palavra-chave é \"exclusivamente\". Se a banca estender a presunção à pessoa jurídica, a frase está errada.",
      "memorize": "Presunção de insuficiência: só pessoa natural. Pessoa jurídica comprova."
     }
    },
    {
     "id": "CPC-3-R1-06",
     "ponto": "DBA26-CPC-3",
     "tema": "Gratuidade e advogado particular",
     "assertiva": "A assistência do requerente por advogado particular não impede a concessão de gratuidade da justiça.",
     "gabarito": "C",
     "comentario": {
      "resumo": "Art. 99, § 4º. A gratuidade depende da **insuficiência de recursos**, não de quem patrocina a causa.",
      "lei": [
       {
        "lei": "L13105",
        "art": "99",
        "par": "",
        "inc": "",
        "rotulo": "CPC, art. 99, § 4º",
        "texto": "A assistência do requerente por advogado particular não impede a concessão de gratuidade da justiça."
       }
      ],
      "palavras_chave": [
       "gratuidade",
       "advogado particular"
      ],
      "aprofundamento": "A gratuidade se mede pela **situação econômica** do requerente, não pela forma como ele obteve representação. Contratar advogado particular não prova riqueza: o advogado pode atuar por honorários de êxito, por valor reduzido ou até sem cobrar.\n\nPor isso o fato de não estar assistido pela Defensoria não serve, sozinho, para indeferir o pedido. O juiz pode indeferir se houver nos autos elementos concretos de capacidade financeira, e antes disso deve dar à parte oportunidade de comprovar os pressupostos.\n\nA banca explora o raciocínio intuitivo e errado de que \"quem paga advogado pode pagar custas\".",
      "exemplo": "Carlos contrata advogado que cobra apenas um percentual do que for obtido ao final. Ele pode pedir gratuidade e obtê-la, se não puder pagar as custas.",
      "memorize": "Advogado particular não impede a gratuidade."
     }
    },
    {
     "id": "CPC-3-R1-07",
     "ponto": "DBA26-CPC-3",
     "tema": "Litisconsórcio multitudinário",
     "assertiva": "O juiz poderá limitar o litisconsórcio facultativo quanto ao número de litigantes na fase de conhecimento, na liquidação de sentença ou na execução, quando comprometer a rápida solução do litígio ou dificultar a defesa.",
     "gabarito": "C",
     "comentario": {
      "resumo": "Art. 113, § 1º: limitação do **litisconsórcio facultativo multitudinário**. O pedido de limitação **interrompe** o prazo de resposta (§ 2º).",
      "lei": [
       {
        "lei": "L13105",
        "art": "113",
        "par": "",
        "inc": "",
        "rotulo": "CPC, art. 113, § 1º",
        "texto": "O juiz poderá limitar o litisconsórcio facultativo quanto ao número de litigantes na fase de conhecimento, na liquidação de sentença ou na execução, quando este comprometer a rápida solução do litígio ou dificultar a defesa ou o cumprimento da sentença."
       }
      ],
      "palavras_chave": [
       "litisconsórcio multitudinário"
      ],
      "aprofundamento": "O litisconsórcio facultativo é útil porque permite resolver num só processo questões comuns de várias pessoas. Quando o número de litigantes é excessivo, porém, o ganho vira problema: o réu não consegue se defender de centenas de situações ao mesmo tempo e o juiz não consegue instruir o feito. É o chamado **litisconsórcio multitudinário**.\n\nA solução é o desmembramento, que pode ocorrer na fase de conhecimento, na liquidação ou na execução. O pedido de limitação **interrompe** o prazo de resposta, que recomeça da intimação da decisão, para não prejudicar o réu.\n\nA limitação só vale para o litisconsórcio **facultativo**. No necessário, a presença de todos é exigida, e não há como desmembrar. Essa é a troca que a banca costuma fazer.",
      "memorize": "Só o litisconsórcio FACULTATIVO pode ser limitado; o pedido interrompe o prazo de resposta."
     }
    },
    {
     "id": "CPC-3-R1-08",
     "ponto": "DBA26-CPC-3",
     "tema": "Assistência",
     "assertiva": "A assistência só é admitida até o saneamento do processo, não podendo o assistente ingressar em grau recursal.",
     "gabarito": "E",
     "comentario": {
      "resumo": "Art. 119, par. ún.: assistência cabe **em qualquer procedimento e em todos os graus de jurisdição**; o assistente recebe o processo **no estado em que se encontre**.",
      "lei": [
       {
        "lei": "L13105",
        "art": "119",
        "par": "",
        "inc": "",
        "rotulo": "CPC, art. 119, par. ún.",
        "texto": "A assistência será admitida em qualquer procedimento e em todos os graus de jurisdição, recebendo o assistente o processo no estado em que se encontre."
       }
      ],
      "palavras_chave": [
       "assistência",
       "interesse jurídico"
      ],
      "correcao": {
       "erro": "Limita a assistência até o saneamento e veda o ingresso do assistente em grau recursal.",
       "certo": "A assistência é admitida em qualquer procedimento e em todos os graus de jurisdição, recebendo o assistente o processo no estado em que se encontre."
      },
      "aprofundamento": "Na assistência, um terceiro com **interesse jurídico** em que a sentença seja favorável a uma das partes ingressa para ajudá-la. Esse interesse pode surgir ou se revelar em qualquer momento, e a lei não quer impedir que o terceiro proteja sua esfera jurídica só porque o processo já avançou.\n\nPor isso a assistência cabe em qualquer procedimento e em **todos os graus de jurisdição**. O preço da entrada tardia é que o assistente recebe o processo **no estado em que se encontra**: não reabre fases já encerradas nem refaz provas já produzidas.\n\nA assertiva cria um limite temporal (até o saneamento) que a lei não prevê. Termos como \"só até\" ou \"não podendo em grau recursal\" são o sinal do erro.",
      "memorize": "Assistência: qualquer procedimento, todos os graus, processo no estado em que está."
     }
    },
    {
     "id": "CPC-3-R1-09",
     "ponto": "DBA26-CPC-3",
     "tema": "Denunciação da lide",
     "assertiva": "A denunciação da lide é obrigatória, sob pena de perda do direito de regresso.",
     "gabarito": "E",
     "comentario": {
      "resumo": "O art. 125 diz que a denunciação é **admissível**. Se indeferida, não promovida ou não permitida, o regresso vai por **ação autônoma** (§ 1º).",
      "lei": [
       {
        "lei": "L13105",
        "art": "125",
        "par": "",
        "inc": "",
        "rotulo": "CPC, art. 125, § 1º",
        "texto": "O direito regressivo será exercido por ação autônoma quando a denunciação da lide for indeferida, deixar de ser promovida ou não for permitida."
       }
      ],
      "pegadinha": "\"Obrigatória\" era a leitura do art. 70 do CPC/1973.",
      "palavras_chave": [
       "denunciação da lide",
       "ação autônoma"
      ],
      "correcao": {
       "erro": "Afirma que a denunciação da lide é obrigatória, sob pena de perda do direito de regresso.",
       "certo": "A denunciação da lide é admissível; se indeferida, não promovida ou não permitida, o direito regressivo é exercido por ação autônoma."
      },
      "aprofundamento": "A denunciação da lide permite que a parte traga ao processo quem tem o dever de indenizá-la caso perca a demanda, como o alienante na evicção ou a seguradora. É uma ação regressiva antecipada, julgada no mesmo processo, por economia.\n\nNo código atual ela é **admissível**, não obrigatória. Se a parte não denunciar, ou se a denunciação for indeferida ou não permitida, o direito de regresso não se perde: será exercido em **ação autônoma**. A lei preferiu não punir com a perda do direito material uma escolha processual.\n\nA ideia de obrigatoriedade vinha da leitura do código anterior e é a pegadinha recorrente. A expressão \"sob pena de perda do direito de regresso\" denuncia o erro.",
      "exemplo": "Pedro compra um imóvel, perde-o em ação de terceiro e não denunciou o vendedor. Ele ainda pode cobrar o vendedor em ação própria.",
      "memorize": "Denunciação é admissível, não obrigatória; sem ela, regresso por ação autônoma."
     }
    },
    {
     "id": "CPC-3-R1-10",
     "ponto": "DBA26-CPC-3",
     "tema": "Desconsideração da personalidade jurídica",
     "assertiva": "O incidente de desconsideração da personalidade jurídica pode ser instaurado de ofício pelo juiz.",
     "gabarito": "E",
     "comentario": {
      "resumo": "Art. 133: instaura-se **a pedido da parte ou do Ministério Público**, quando lhe couber intervir. Não há instauração de ofício.",
      "lei": [
       {
        "lei": "L13105",
        "art": "133",
        "par": "",
        "inc": "",
        "rotulo": "CPC, art. 133",
        "texto": "O incidente de desconsideração da personalidade jurídica será instaurado a pedido da parte ou do Ministério Público, quando lhe couber intervir no processo."
       }
      ],
      "palavras_chave": [
       "IDPJ",
       "de ofício"
      ],
      "correcao": {
       "erro": "Admite a instauração do incidente de desconsideração de ofício pelo juiz.",
       "certo": "O incidente de desconsideração da personalidade jurídica é instaurado a pedido da parte ou do Ministério Público, quando lhe couber intervir no processo."
      },
      "aprofundamento": "A desconsideração da personalidade jurídica é medida grave: atinge o patrimônio de quem não foi parte originária. Por isso o CPC criou um **incidente** com contraditório prévio, e não uma decisão surpresa.\n\nA legitimidade para provocar o incidente é da **parte** ou do **Ministério Público**, quando lhe couber intervir. O juiz não o instaura de ofício, porque a desconsideração depende da demonstração dos pressupostos do direito material e de pedido de quem tem interesse em alcançar o patrimônio do sócio ou da sociedade.\n\nO incidente cabe em todas as fases do processo e é dispensado se a desconsideração for pedida já na petição inicial. A banca costuma acrescentar a instauração de ofício, que a lei não autoriza.",
      "memorize": "Desconsideração: a pedido da parte ou do MP. Nunca de ofício."
     }
    },
    {
     "id": "CPC-3-R1-11",
     "ponto": "DBA26-CPC-3",
     "tema": "Suspeição",
     "assertiva": "Ser o juiz amigo íntimo de qualquer das partes é causa de impedimento.",
     "gabarito": "E",
     "comentario": {
      "resumo": "Amizade íntima ou inimizade é **suspeição** (art. 145, I). Impedimento (art. 144) envolve hipóteses objetivas (parente advogado, ter atuado como mandatário etc.).",
      "lei": [
       {
        "lei": "L13105",
        "art": "145",
        "par": "",
        "inc": "",
        "rotulo": "CPC, art. 145, I",
        "texto": "amigo íntimo ou inimigo de qualquer das partes ou de seus advogados"
       }
      ],
      "palavras_chave": [
       "suspeição",
       "impedimento"
      ],
      "correcao": {
       "erro": "Classifica a amizade íntima do juiz com a parte como impedimento.",
       "certo": "Ser o juiz amigo íntimo ou inimigo de qualquer das partes ou de seus advogados é causa de suspeição."
      },
      "aprofundamento": "Impedimento e suspeição protegem a imparcialidade, mas de formas diferentes. O **impedimento** trabalha com hipóteses **objetivas**, verificáveis sem avaliar sentimentos: parentesco com advogado ou parte, ter atuado como mandatário, ser parte no processo. A lei presume a parcialidade de modo absoluto.\n\nA **suspeição** envolve vínculos **subjetivos**: amizade íntima, inimizade, interesse no julgamento, aconselhamento. Exige apreciação concreta e tem tratamento mais brando.\n\nA diferença tem consequência prática: a sentença proferida por juiz impedido pode ser rescindida, o que não ocorre com a suspeição. A banca troca a classificação, colocando amizade íntima como impedimento. Pergunte-se: é fato objetivo ou sentimento? Sentimento é suspeição.",
      "memorize": "Amizade íntima ou inimizade = SUSPEIÇÃO (subjetivo). Impedimento = fato objetivo."
     }
    },
    {
     "id": "CPC-3-R1-12",
     "ponto": "DBA26-CPC-3",
     "tema": "MP como fiscal da ordem jurídica",
     "assertiva": "A participação da Fazenda Pública não configura, por si só, hipótese de intervenção do Ministério Público.",
     "gabarito": "C",
     "comentario": {
      "resumo": "Art. 178, par. ún. O MP intervém por **interesse público ou social**, **interesse de incapaz** e **litígios coletivos pela posse de terra**.",
      "lei": [
       {
        "lei": "L13105",
        "art": "178",
        "par": "",
        "inc": "",
        "rotulo": "CPC, art. 178, par. ún.",
        "texto": "A participação da Fazenda Pública não configura, por si só, hipótese de intervenção do Ministério Público."
       }
      ],
      "palavras_chave": [
       "fiscal da ordem jurídica",
       "Fazenda Pública"
      ],
      "aprofundamento": "O MP intervém como fiscal da ordem jurídica para proteger interesses que justificam sua atuação: interesse público ou social, interesse de incapaz e litígios coletivos pela posse de terra. Nessas causas, ele não representa nenhuma parte; zela pela correta aplicação do direito.\n\nO parágrafo único corta uma confusão antiga: a Fazenda Pública tem advocacia própria e defende o **interesse público secundário**, o interesse patrimonial do ente. Isso não se confunde com o **interesse público primário**, que é o da coletividade e o que justifica a presença do MP.\n\nAssim, uma ação de cobrança contra o Município não exige, só por isso, a intervenção ministerial. A banca costuma afirmar o contrário, dizendo que toda causa com a Fazenda exige o MP.",
      "memorize": "Fazenda Pública no processo não atrai, por si só, o MP."
     }
    },
    {
     "id": "CPC-4-R1-01",
     "ponto": "DBA26-CPC-4",
     "tema": "Negócio jurídico processual",
     "assertiva": "Versando o processo sobre direitos que admitam autocomposição, é lícito às partes plenamente capazes estipular mudanças no procedimento e convencionar sobre seus ônus, poderes, faculdades e deveres processuais, antes ou durante o processo.",
     "gabarito": "C",
     "comentario": {
      "resumo": "Art. 190: **cláusula geral de negócio processual** — partes **plenamente capazes** + direitos que admitam **autocomposição**.",
      "lei": [
       {
        "lei": "L13105",
        "art": "190",
        "par": "",
        "inc": "",
        "rotulo": "CPC, art. 190",
        "texto": "Versando o processo sobre direitos que admitam autocomposição, é lícito às partes plenamente capazes estipular mudanças no procedimento para ajustá-lo às especificidades da causa e convencionar sobre os seus ônus, poderes, faculdades e deveres processuais, antes ou durante o processo."
       }
      ],
      "palavras_chave": [
       "negócio processual",
       "autocomposição"
      ],
      "aprofundamento": "O art. 190 é a **cláusula geral de negócio processual**: as partes podem ajustar o procedimento às peculiaridades da causa e dispor sobre seus próprios ônus, poderes, faculdades e deveres. É expressão do autorregramento da vontade no processo, coerente com o modelo cooperativo.\n\nOs requisitos são dois: o direito deve admitir **autocomposição** e as partes devem ser **plenamente capazes**. O acordo pode ser feito antes do processo, num contrato, ou durante ele.\n\nO controle cabe ao juiz, de ofício ou a requerimento, que recusará validade nos casos de nulidade, de inserção abusiva em contrato de adesão ou quando uma parte estiver em manifesta situação de vulnerabilidade. A banca costuma exigir homologação judicial prévia ou estender o negócio a partes relativamente incapazes.",
      "exemplo": "Duas empresas, num contrato, combinam que eventual litígio dispensará a audiência de conciliação. O juiz só afastará o acordo se houver nulidade, abuso ou vulnerabilidade.",
      "memorize": "Negócio processual: direito que admite autocomposição + partes plenamente capazes, antes ou durante o processo."
     }
    },
    {
     "id": "CPC-4-R1-02",
     "ponto": "DBA26-CPC-4",
     "tema": "Conceito de sentença",
     "assertiva": "Sentença é o pronunciamento por meio do qual o juiz, com fundamento nos arts. 485 e 487, põe fim à fase cognitiva do procedimento comum, bem como extingue a execução.",
     "gabarito": "C",
     "comentario": {
      "resumo": "Art. 203, § 1º: conceito por **conteúdo + finalidade** (encerrar a fase). Interlocutória é residual (§ 2º).",
      "lei": [
       {
        "lei": "L13105",
        "art": "203",
        "par": "",
        "inc": "",
        "rotulo": "CPC, art. 203, § 1º",
        "texto": "Ressalvadas as disposições expressas dos procedimentos especiais, sentença é o pronunciamento por meio do qual o juiz, com fundamento nos arts. 485 e 487, põe fim à fase cognitiva do procedimento comum, bem como extingue a execução."
       }
      ],
      "palavras_chave": [
       "sentença",
       "decisão interlocutória"
      ],
      "aprofundamento": "O conceito de sentença no CPC atual combina dois critérios. O **conteúdo**: a decisão se funda nas hipóteses de extinção sem resolução do mérito ou com resolução do mérito. A **finalidade**: ela encerra a fase cognitiva do procedimento comum ou extingue a execução.\n\nO segundo critério é o decisivo. Uma decisão que julga parcialmente o mérito, mas deixa o processo prosseguir para o restante, tem conteúdo de mérito e não encerra a fase, por isso é **interlocutória**. A interlocutória é definida por exclusão: todo pronunciamento decisório que não seja sentença.\n\nA classificação importa para o recurso: sentença desafia apelação; interlocutória, nas hipóteses legais, agravo de instrumento. A banca costuma definir sentença só pelo conteúdo, o que leva ao erro.",
      "memorize": "Sentença = conteúdo (extinção sem/com mérito) + fim da fase cognitiva ou da execução."
     }
    },
    {
     "id": "CPC-4-R1-03",
     "ponto": "DBA26-CPC-4",
     "tema": "Horário dos atos",
     "assertiva": "Os atos processuais serão realizados em dias úteis, das 6 às 18 horas.",
     "gabarito": "E",
     "comentario": {
      "resumo": "Art. 212: das **6 às 20 horas**. Concluem-se depois das 20h os atos iniciados antes, se o adiamento prejudicar a diligência (§ 1º).",
      "lei": [
       {
        "lei": "L13105",
        "art": "212",
        "par": "",
        "inc": "",
        "rotulo": "CPC, art. 212",
        "texto": "Os atos processuais serão realizados em dias úteis, das 6 (seis) às 20 (vinte) horas."
       }
      ],
      "palavras_chave": [
       "dias úteis",
       "6 às 20 horas"
      ],
      "correcao": {
       "erro": "Fixa o término do horário dos atos processuais às 18 horas.",
       "certo": "Os atos processuais serão realizados em dias úteis, das 6 às 20 horas."
      },
      "aprofundamento": "O horário dos atos processuais equilibra a eficiência do serviço com a proteção da intimidade e do descanso das pessoas. Por isso os atos externos, como citações e penhoras, não podem ser feitos a qualquer hora.\n\nA lei admite flexibilidade: atos iniciados antes do fim do horário podem ser concluídos depois, se o adiamento prejudicar a diligência ou causar grave dano. Citações, intimações e penhoras podem ocorrer também em férias forenses e feriados, observada a proteção constitucional do domicílio.\n\nNão confunda o horário dos atos com o horário de protocolo de petições em autos físicos, que segue o expediente forense. A banca troca o limite final; o correto é das 6 às 20 horas.",
      "memorize": "Atos processuais: dias úteis, das 6 às 20 horas."
     }
    },
    {
     "id": "CPC-4-R1-04",
     "ponto": "DBA26-CPC-4",
     "tema": "Contagem em dias úteis",
     "assertiva": "Na contagem de prazo em dias, estabelecido por lei ou pelo juiz, computar-se-ão somente os dias úteis, regra que se aplica apenas aos prazos processuais.",
     "gabarito": "C",
     "comentario": {
      "resumo": "Art. 219 e parágrafo único: **dias úteis** só para **prazos processuais** (não para os de direito material).",
      "lei": [
       {
        "lei": "L13105",
        "art": "219",
        "par": "",
        "inc": "",
        "rotulo": "CPC, art. 219",
        "texto": "Na contagem de prazo em dias, estabelecido por lei ou pelo juiz, computar-se-ão somente os dias úteis."
       },
       {
        "lei": "L13105",
        "art": "219",
        "par": "",
        "inc": "",
        "rotulo": "CPC, art. 219, par. ún.",
        "texto": "O disposto neste artigo aplica-se somente aos prazos processuais."
       }
      ],
      "palavras_chave": [
       "dias úteis",
       "prazos processuais"
      ],
      "aprofundamento": "A contagem em **dias úteis** foi uma das novidades do CPC atual. Ela atende ao advogado, que deixa de ter o prazo consumido por fins de semana e feriados, e torna a contagem mais previsível.\n\nA restrição aos **prazos processuais** é essencial. Prazos de direito material, como os de prescrição e decadência, ou o prazo para cumprir uma obrigação contratual, continuam correndo em dias corridos, porque não dizem respeito à prática de atos no processo.\n\nA banca costuma dizer que a contagem em dias úteis vale \"para todos os prazos\", ou o contrário, que vale também para a prescrição.",
      "memorize": "Dias úteis: só para prazos processuais; prescrição e decadência correm em dias corridos."
     }
    },
    {
     "id": "CPC-4-R1-05",
     "ponto": "DBA26-CPC-4",
     "tema": "Suspensão de fim de ano",
     "assertiva": "Suspende-se o curso do prazo processual nos dias compreendidos entre 20 de dezembro e 6 de janeiro, inclusive.",
     "gabarito": "E",
     "comentario": {
      "resumo": "Art. 220: de **20 de dezembro a 20 de janeiro**, inclusive.",
      "lei": [
       {
        "lei": "L13105",
        "art": "220",
        "par": "",
        "inc": "",
        "rotulo": "CPC, art. 220",
        "texto": "Suspende-se o curso do prazo processual nos dias compreendidos entre 20 de dezembro e 20 de janeiro, inclusive."
       }
      ],
      "palavras_chave": [
       "recesso",
       "20 de dezembro",
       "20 de janeiro"
      ],
      "correcao": {
       "erro": "Encerra a suspensão dos prazos em 6 de janeiro.",
       "certo": "Suspende-se o curso do prazo processual nos dias compreendidos entre 20 de dezembro e 20 de janeiro, inclusive."
      },
      "aprofundamento": "A suspensão de fim de ano atende a uma reivindicação antiga da advocacia: garantir um período de **descanso** em que os prazos não corram, sem que o profissional precise abandonar a causa ou temer a perda de um prazo.\n\nDurante esse período os prazos ficam **suspensos**: o que já correu é aproveitado e a contagem retoma pelo saldo depois do fim do recesso. Não se realizam audiências nem sessões de julgamento, mas juízes, membros do MP, da Defensoria e da Advocacia Pública continuam exercendo suas atribuições normalmente, ressalvadas férias individuais.\n\nA pegadinha é o termo final. O recesso forense de fim de ano do Judiciário costuma terminar no início de janeiro, e a banca usa essa data para confundir. A suspensão dos prazos processuais vai até 20 de janeiro, inclusive.",
      "memorize": "Prazos suspensos de 20 de dezembro a 20 de janeiro, inclusive."
     }
    },
    {
     "id": "CPC-4-R1-06",
     "ponto": "DBA26-CPC-4",
     "tema": "Prazo supletivo",
     "assertiva": "Inexistindo preceito legal ou prazo determinado pelo juiz, será de 5 dias o prazo para a prática de ato processual a cargo da parte.",
     "gabarito": "C",
     "comentario": {
      "resumo": "Art. 218, § 3º: **5 dias** é o prazo supletivo.",
      "lei": [
       {
        "lei": "L13105",
        "art": "218",
        "par": "",
        "inc": "",
        "rotulo": "CPC, art. 218, § 3º",
        "texto": "Inexistindo preceito legal ou prazo determinado pelo juiz, será de 5 (cinco) dias o prazo para a prática de ato processual a cargo da parte."
       }
      ],
      "palavras_chave": [
       "prazo supletivo",
       "5 dias"
      ],
      "aprofundamento": "O prazo supletivo resolve um problema prático: há atos que a parte precisa praticar sem que a lei ou o juiz tenham fixado prazo. Sem uma regra residual, o processo ficaria parado à espera de uma manifestação indefinida.\n\nA ordem de aplicação é: primeiro o prazo previsto em lei; na falta dele, o prazo que o juiz fixar, considerando a complexidade do ato; e, se nenhum existir, o prazo supletivo de 5 dias. Por ser processual, conta-se em dias úteis.\n\nO dispositivo fala em ato \"a cargo da parte\". Os prazos do próprio juiz e dos auxiliares da justiça têm regras específicas. A banca costuma trocar o número ou estender a regra aos atos do juiz.",
      "memorize": "Sem prazo na lei nem fixado pelo juiz: 5 dias para a parte."
     }
    },
    {
     "id": "CPC-4-R1-07",
     "ponto": "DBA26-CPC-4",
     "tema": "Contagem do prazo",
     "assertiva": "Os prazos são contados incluindo o dia do começo e excluindo o dia do vencimento.",
     "gabarito": "E",
     "comentario": {
      "resumo": "Art. 224: **exclui o dia do começo e inclui o do vencimento**.",
      "lei": [
       {
        "lei": "L13105",
        "art": "224",
        "par": "",
        "inc": "",
        "rotulo": "CPC, art. 224",
        "texto": "Salvo disposição em contrário, os prazos serão contados excluindo o dia do começo e incluindo o dia do vencimento."
       }
      ],
      "palavras_chave": [
       "contagem",
       "dies a quo"
      ],
      "correcao": {
       "erro": "Inverte a regra, incluindo o dia do começo e excluindo o do vencimento.",
       "certo": "Salvo disposição em contrário, os prazos são contados excluindo o dia do começo e incluindo o dia do vencimento."
      },
      "aprofundamento": "A regra de contagem evita que a parte perca parte do prazo no próprio dia em que é intimada. Se o dia do começo contasse, uma intimação recebida no fim do expediente consumiria um dia inteiro sem que fosse possível trabalhar.\n\nPor isso **exclui-se o dia do começo** e **inclui-se o dia do vencimento**: a parte tem o último dia inteiro para praticar o ato. O início e o vencimento são protraídos para o primeiro dia útil seguinte se coincidirem com dia sem expediente ou com expediente encerrado antes do horário normal.\n\nA assertiva simplesmente inverte a fórmula. Ela é fácil de memorizar se lembrar da lógica: o dia em que você toma ciência não conta; o último dia conta inteiro.",
      "memorize": "Exclui o começo, inclui o vencimento."
     }
    },
    {
     "id": "CPC-4-R1-08",
     "ponto": "DBA26-CPC-4",
     "tema": "Efeitos da citação",
     "assertiva": "A citação válida, quando ordenada por juízo incompetente, não induz litispendência nem constitui em mora o devedor.",
     "gabarito": "E",
     "comentario": {
      "resumo": "Art. 240: a citação válida, **ainda quando ordenada por juízo incompetente**, induz litispendência, torna litigiosa a coisa e constitui em mora o devedor.",
      "lei": [
       {
        "lei": "L13105",
        "art": "240",
        "par": "",
        "inc": "",
        "rotulo": "CPC, art. 240",
        "texto": "A citação válida, ainda quando ordenada por juízo incompetente, induz litispendência, torna litigiosa a coisa e constitui em mora o devedor"
       }
      ],
      "palavras_chave": [
       "citação",
       "litispendência",
       "mora"
      ],
      "correcao": {
       "erro": "Nega os efeitos da citação válida quando ordenada por juízo incompetente.",
       "certo": "A citação válida, ainda quando ordenada por juízo incompetente, induz litispendência, torna litigiosa a coisa e constitui em mora o devedor."
      },
      "aprofundamento": "A citação válida produz efeitos processuais e materiais. Processuais: **induz litispendência** (impede nova ação idêntica) e **torna litigiosa a coisa** (a alienação do bem passa a ter repercussões no processo). Material: **constitui o devedor em mora**, quando ele ainda não estava.\n\nA lei preserva esses efeitos mesmo quando a citação foi ordenada por juízo incompetente. A razão é proteger o autor: ele não pode ser prejudicado por erro na escolha do juízo, que será corrigido com a remessa dos autos ao competente. O que importa é que o réu tomou conhecimento válido da demanda.\n\nA assertiva troca o \"ainda quando\" por uma negação. Na prova, a expressão \"juízo incompetente\" ao lado de efeitos da citação quase sempre vem para testar essa preservação.",
      "memorize": "Citação válida, mesmo por juízo incompetente: litispendência, coisa litigiosa e mora."
     }
    },
    {
     "id": "CPC-4-R1-09",
     "ponto": "DBA26-CPC-4",
     "tema": "Interrupção da prescrição",
     "assertiva": "A interrupção da prescrição, operada pelo despacho que ordena a citação, ainda que proferido por juízo incompetente, retroagirá à data de propositura da ação.",
     "gabarito": "C",
     "comentario": {
      "resumo": "Art. 240, § 1º. Quem interrompe é o **despacho que ordena a citação**, com efeito **retroativo** à propositura.",
      "lei": [
       {
        "lei": "L13105",
        "art": "240",
        "par": "",
        "inc": "",
        "rotulo": "CPC, art. 240, § 1º",
        "texto": "A interrupção da prescrição, operada pelo despacho que ordena a citação, ainda que proferido por juízo incompetente, retroagirá à data de propositura da ação."
       }
      ],
      "palavras_chave": [
       "interrupção da prescrição",
       "retroação"
      ],
      "aprofundamento": "A prescrição pune a inércia do titular do direito. Quem ajuíza a ação já deixou de ser inerte, e por isso não pode ser prejudicado pela demora do cartório ou do juiz em despachar. Daí a **retroação** do efeito interruptivo à data da propositura.\n\nO ato que interrompe é o **despacho que ordena a citação**, e não a citação em si. Mesmo proferido por juízo incompetente, ele produz o efeito, pela mesma lógica de proteger o autor diligente. Cabe ao autor, porém, adotar as providências necessárias para viabilizar a citação; a demora imputável exclusivamente ao serviço judiciário não o prejudica.\n\nA banca costuma dizer que a interrupção ocorre com a citação válida, ou que o efeito vale só a partir do despacho, sem retroagir.",
      "exemplo": "Paula ajuíza a ação no último dia antes da prescrição; o juiz só despacha semanas depois. A prescrição considera-se interrompida na data da propositura.",
      "memorize": "Despacho que ordena a citação interrompe a prescrição e retroage à propositura."
     }
    },
    {
     "id": "CPC-4-R1-10",
     "ponto": "DBA26-CPC-4",
     "tema": "Citação eletrônica",
     "assertiva": "A citação será feita preferencialmente pelo correio, para qualquer comarca do país.",
     "gabarito": "E",
     "comentario": {
      "resumo": "Desde a Lei 14.195/2021, o art. 246 manda citar **preferencialmente por meio eletrônico**, em até 2 dias úteis da decisão que a determinar.",
      "lei": [
       {
        "lei": "L13105",
        "art": "246",
        "par": "",
        "inc": "",
        "rotulo": "CPC, art. 246",
        "texto": "A citação será feita preferencialmente por meio eletrônico, no prazo de até 2 (dois) dias úteis, contado da decisão que a determinar"
       }
      ],
      "palavras_chave": [
       "citação eletrônica",
       "Lei 14.195/2021"
      ],
      "correcao": {
       "erro": "Indica o correio como meio preferencial de citação.",
       "certo": "A citação será feita preferencialmente por meio eletrônico, no prazo de até 2 dias úteis contado da decisão que a determinar."
      },
      "aprofundamento": "A citação eletrônica foi adotada como regra para dar **rapidez e economia** ao processo. Empresas e órgãos públicos mantêm cadastro nos sistemas de processo eletrônico, e a citação por esse meio chega em pouco tempo, sem custo de postagem ou de oficial de justiça.\n\nA Lei 14.195/2021 alterou o artigo para tornar o meio eletrônico preferencial, com prazo de até 2 dias úteis contado da decisão que determinar a citação. Os demais meios (correio, oficial de justiça, escrivão, edital) passaram a ser subsidiários, usados quando a via eletrônica não for possível ou não for confirmada.\n\nA assertiva reproduz a regra anterior, em que o correio era o meio preferencial. Na prova, guarde a ordem atual: primeiro o eletrônico.",
      "memorize": "Citação: preferencialmente eletrônica (Lei 14.195/2021), em até 2 dias úteis."
     }
    },
    {
     "id": "CPC-4-R1-11",
     "ponto": "DBA26-CPC-4",
     "tema": "Citação com hora certa",
     "assertiva": "Quando, por 3 vezes, o oficial de justiça houver procurado o citando em seu domicílio sem o encontrar, deverá, havendo suspeita de ocultação, intimar pessoa da família ou vizinho de que voltará para efetuar a citação.",
     "gabarito": "E",
     "comentario": {
      "resumo": "Art. 252: bastam **2 vezes** + **suspeita de ocultação**.",
      "lei": [
       {
        "lei": "L13105",
        "art": "252",
        "par": "",
        "inc": "",
        "rotulo": "CPC, art. 252",
        "texto": "Quando, por 2 (duas) vezes, o oficial de justiça houver procurado o citando em seu domicílio ou residência sem o encontrar, deverá, havendo suspeita de ocultação, intimar qualquer pessoa da família ou, em sua falta, qualquer vizinho de que, no dia útil imediato, voltará a fim de efetuar a citação, na hora que designar."
       }
      ],
      "palavras_chave": [
       "hora certa",
       "ocultação"
      ],
      "correcao": {
       "erro": "Exige 3 tentativas do oficial de justiça para a citação com hora certa.",
       "certo": "Bastam 2 procuras sem encontrar o citando, havendo suspeita de ocultação, para o oficial intimar pessoa da família ou vizinho de que voltará no dia útil imediato."
      },
      "aprofundamento": "A citação com hora certa é uma **citação ficta**: presume-se que o réu soube da ação, embora não tenha sido encontrado pessoalmente. Ela existe para impedir que o réu frustre o processo escondendo-se do oficial de justiça.\n\nOs requisitos são cumulativos: o oficial deve ter procurado o citando em seu domicílio ou residência pelo número de vezes que a lei exige e deve haver **suspeita de ocultação**. Então intima um familiar ou, na falta, um vizinho de que voltará no dia útil seguinte, em hora designada. Se o réu ficar revel, recebe curador especial.\n\nA banca troca o número de tentativas. O texto exige 2 procuras, e não 3. Também costuma omitir a suspeita de ocultação, que é indispensável.",
      "memorize": "Hora certa: 2 procuras + suspeita de ocultação. Revel recebe curador especial."
     }
    },
    {
     "id": "CPC-4-R1-12",
     "ponto": "DBA26-CPC-4",
     "tema": "Instrumentalidade das formas",
     "assertiva": "Quando a lei prescrever determinada forma, o juiz considerará válido o ato se, realizado de outro modo, lhe alcançar a finalidade.",
     "gabarito": "C",
     "comentario": {
      "resumo": "Art. 277: **instrumentalidade das formas** — sem prejuízo, não há nulidade.",
      "lei": [
       {
        "lei": "L13105",
        "art": "277",
        "par": "",
        "inc": "",
        "rotulo": "CPC, art. 277",
        "texto": "Quando a lei prescrever determinada forma, o juiz considerará válido o ato se, realizado de outro modo, lhe alcançar a finalidade."
       }
      ],
      "palavras_chave": [
       "instrumentalidade",
       "nulidade"
      ],
      "aprofundamento": "A forma no processo não é um fim em si mesma: serve para garantir segurança, contraditório e previsibilidade. Se o ato, embora praticado de modo diverso, atingiu sua **finalidade** e não causou prejuízo, anulá-lo só atrasaria o processo sem proteger ninguém.\n\nDaí decorrem duas máximas do sistema de nulidades: não há nulidade sem prejuízo, e o ato que alcança seu objetivo é válido. O juiz deve aproveitar ao máximo os atos praticados.\n\nA fronteira está nos vícios que, por si, comprometem a própria finalidade, como a falta de citação que impede o réu de se defender. A banca costuma dizer que o descumprimento de forma prescrita em lei gera nulidade \"automática\", o que contraria a regra.",
      "exemplo": "O réu foi citado por meio diverso do previsto, mas compareceu e contestou no prazo. A citação é considerada válida, porque cumpriu sua finalidade.",
      "memorize": "Forma é meio: alcançada a finalidade sem prejuízo, o ato vale."
     }
    },
    {
     "id": "CPC-5-R1-01",
     "ponto": "DBA26-CPC-5",
     "tema": "Espécies",
     "assertiva": "A tutela provisória pode fundamentar-se em urgência ou evidência, e a tutela de urgência, cautelar ou antecipada, pode ser concedida em caráter antecedente ou incidental.",
     "gabarito": "C",
     "comentario": {
      "resumo": "Art. 294: **urgência** (cautelar ou antecipada; antecedente ou incidental) x **evidência** (sempre incidental).",
      "lei": [
       {
        "lei": "L13105",
        "art": "294",
        "par": "",
        "inc": "",
        "rotulo": "CPC, art. 294",
        "texto": "A tutela provisória pode fundamentar-se em urgência ou evidência.\nParágrafo único. A tutela provisória de urgência, cautelar ou antecipada, pode ser concedida em caráter antecedente ou incidental."
       }
      ],
      "palavras_chave": [
       "urgência",
       "evidência",
       "antecedente",
       "incidental"
      ],
      "aprofundamento": "A tutela provisória responde a um problema central do processo: o tempo. Ela permite que o juiz conceda proteção antes da decisão final, com base em cognição sumária.\n\nA **urgência** pressupõe perigo e se divide em **cautelar**, que conserva o bem ou a prova para garantir o resultado futuro, e **antecipada**, que entrega desde logo os efeitos práticos do pedido. Ambas podem ser pedidas de forma **antecedente** (antes do pedido principal, quando a urgência é contemporânea à propositura) ou **incidental** (no curso do processo já instaurado).\n\nA **evidência** dispensa o perigo: o direito se mostra tão provável que não é justo fazer o autor esperar. Ela é sempre incidental. A banca costuma admitir tutela da evidência antecedente ou trocar cautelar por antecipada.",
      "memorize": "Urgência (cautelar ou antecipada, antecedente ou incidental) x evidência (sem perigo, incidental)."
     }
    },
    {
     "id": "CPC-5-R1-02",
     "ponto": "DBA26-CPC-5",
     "tema": "Revogabilidade",
     "assertiva": "A tutela provisória conserva sua eficácia na pendência do processo, mas pode, a qualquer tempo, ser revogada ou modificada.",
     "gabarito": "C",
     "comentario": {
      "resumo": "Art. 296: **precariedade** — eficácia durante o processo, revogável a qualquer tempo. Na suspensão do processo, conserva eficácia (par. ún.).",
      "lei": [
       {
        "lei": "L13105",
        "art": "296",
        "par": "",
        "inc": "",
        "rotulo": "CPC, art. 296",
        "texto": "A tutela provisória conserva sua eficácia na pendência do processo, mas pode, a qualquer tempo, ser revogada ou modificada."
       }
      ],
      "palavras_chave": [
       "precariedade",
       "revogação"
      ],
      "aprofundamento": "A tutela provisória é concedida com base em **cognição sumária**, isto é, num exame superficial das provas. Por isso ela é precária: nasce para durar enquanto o processo não chega à decisão definitiva e pode ser revista a qualquer momento se o quadro mudar.\n\nEssa revogabilidade não é arbitrária. O juiz deve fundamentar a revogação ou a modificação, normalmente diante de fatos novos ou de prova que altere a avaliação inicial. A tutela também mantém a eficácia durante a suspensão do processo, salvo decisão em contrário.\n\nA banca costuma dizer que a tutela provisória só pode ser revogada na sentença, ou que perde a eficácia com a suspensão do processo. Ambas as afirmações contrariam o regime legal.",
      "memorize": "Tutela provisória: eficácia durante o processo, revogável ou modificável a qualquer tempo."
     }
    },
    {
     "id": "CPC-5-R1-03",
     "ponto": "DBA26-CPC-5",
     "tema": "Requisitos da urgência",
     "assertiva": "A tutela de urgência será concedida quando houver prova inequívoca que convença o juiz da verossimilhança da alegação.",
     "gabarito": "E",
     "comentario": {
      "resumo": "Art. 300: **probabilidade do direito** + **perigo de dano ou risco ao resultado útil do processo**. \"Prova inequívoca/verossimilhança\" é linguagem do CPC/1973.",
      "lei": [
       {
        "lei": "L13105",
        "art": "300",
        "par": "",
        "inc": "",
        "rotulo": "CPC, art. 300",
        "texto": "A tutela de urgência será concedida quando houver elementos que evidenciem a probabilidade do direito e o perigo de dano ou o risco ao resultado útil do processo."
       }
      ],
      "pegadinha": "Requisitos do CPC/1973 apresentados como atuais.",
      "palavras_chave": [
       "probabilidade do direito",
       "perigo de dano"
      ],
      "correcao": {
       "erro": "Usa os requisitos do código revogado (prova inequívoca e verossimilhança) e omite o perigo de dano.",
       "certo": "A tutela de urgência será concedida quando houver elementos que evidenciem a probabilidade do direito e o perigo de dano ou o risco ao resultado útil do processo."
      },
      "aprofundamento": "O CPC atual unificou os requisitos das tutelas de urgência, cautelar e antecipada. Exige-se a **probabilidade do direito** (o chamado fumus boni iuris) e o **perigo de dano ou risco ao resultado útil do processo** (periculum in mora).\n\nO código anterior tinha requisitos diferentes para cada espécie, e para a antecipação exigia \"prova inequívoca\" que convencesse da \"verossimilhança\". A fórmula era criticada por ser contraditória: prova inequívoca leva à certeza, não à mera verossimilhança. O texto atual adotou um padrão mais coerente com a cognição sumária.\n\nA banca reaproveita a linguagem revogada. Se aparecer \"prova inequívoca\" ou \"verossimilhança\" como requisito atual, a frase está errada. Repare também que a assertiva omite o perigo de dano.",
      "memorize": "Urgência = probabilidade do direito + perigo de dano/risco ao resultado útil."
     }
    },
    {
     "id": "CPC-5-R1-04",
     "ponto": "DBA26-CPC-5",
     "tema": "Irreversibilidade",
     "assertiva": "A tutela de urgência de natureza antecipada não será concedida quando houver perigo de irreversibilidade dos efeitos da decisão.",
     "gabarito": "C",
     "comentario": {
      "resumo": "Art. 300, § 3º. A vedação é para a **antecipada** (a cautelar só conserva).",
      "lei": [
       {
        "lei": "L13105",
        "art": "300",
        "par": "",
        "inc": "",
        "rotulo": "CPC, art. 300, § 3º",
        "texto": "A tutela de urgência de natureza antecipada não será concedida quando houver perigo de irreversibilidade dos efeitos da decisão."
       }
      ],
      "palavras_chave": [
       "irreversibilidade",
       "antecipada"
      ],
      "aprofundamento": "A tutela antecipada entrega desde logo o resultado prático do pedido. Se esse resultado não puder ser desfeito, a decisão provisória se tornaria, na prática, definitiva, sem que o réu tivesse tido defesa plena. A vedação protege o contraditório e o devido processo.\n\nA cautelar não sofre a mesma restrição com a mesma intensidade, porque apenas **conserva** (arresta, sequestra, guarda), sem satisfazer o direito.\n\nA vedação, porém, não é absoluta na prática dos tribunais: quando há irreversibilidade recíproca (negar a tutela também causaria dano irreversível ao autor), o juiz pondera os valores em jogo, como nos casos de saúde. A banca costuma estender a vedação à cautelar ou trocar \"antecipada\" por \"de urgência\" em geral.",
      "memorize": "Perigo de irreversibilidade barra a tutela ANTECIPADA (a cautelar só conserva)."
     }
    },
    {
     "id": "CPC-5-R1-05",
     "ponto": "DBA26-CPC-5",
     "tema": "Liminar ou justificação prévia",
     "assertiva": "A tutela de urgência só pode ser concedida após justificação prévia, vedada a concessão liminar.",
     "gabarito": "E",
     "comentario": {
      "resumo": "Art. 300, § 2º: pode ser concedida **liminarmente ou após justificação prévia**.",
      "lei": [
       {
        "lei": "L13105",
        "art": "300",
        "par": "",
        "inc": "",
        "rotulo": "CPC, art. 300, § 2º",
        "texto": "A tutela de urgência pode ser concedida liminarmente ou após justificação prévia."
       }
      ],
      "palavras_chave": [
       "liminar",
       "justificação prévia"
      ],
      "correcao": {
       "erro": "Exige justificação prévia e veda a concessão liminar da tutela de urgência.",
       "certo": "A tutela de urgência pode ser concedida liminarmente ou após justificação prévia."
      },
      "aprofundamento": "A tutela de urgência existe justamente para situações em que esperar é perigoso. Exigir sempre uma audiência prévia esvaziaria a medida em muitos casos. Por isso o juiz tem duas opções: conceder **liminarmente**, só com os documentos da inicial, ou designar **justificação prévia**, ouvindo testemunhas antes de decidir, quando a prova documental não for suficiente.\n\nA escolha depende do caso concreto e da urgência. Concedida a liminar sem ouvir o réu, o contraditório é diferido, e ele poderá impugnar a decisão por agravo de instrumento.\n\nO juiz pode ainda exigir **caução** para ressarcir danos que a outra parte possa sofrer, dispensando-a se a parte for hipossuficiente. A assertiva erra ao vedar a liminar, que é justamente a forma mais comum de concessão.",
      "memorize": "Urgência: liminar OU após justificação prévia, a critério do juiz."
     }
    },
    {
     "id": "CPC-5-R1-06",
     "ponto": "DBA26-CPC-5",
     "tema": "Antecipada antecedente — aditamento",
     "assertiva": "Concedida a tutela antecipada em caráter antecedente, o autor deverá aditar a petição inicial no prazo de 30 dias ou em outro maior que o juiz fixar.",
     "gabarito": "E",
     "comentario": {
      "resumo": "Art. 303, § 1º, I: aditamento em **15 dias** (ou maior fixado pelo juiz). Os **30 dias** são da **cautelar** antecedente (art. 308).",
      "lei": [
       {
        "lei": "L13105",
        "art": "303",
        "par": "",
        "inc": "",
        "rotulo": "CPC, art. 303, § 1º, I",
        "texto": "o autor deverá aditar a petição inicial, com a complementação de sua argumentação, a juntada de novos documentos e a confirmação do pedido de tutela final, em 15 (quinze) dias ou em outro prazo maior que o juiz fixar;"
       }
      ],
      "pegadinha": "Mistura dos prazos: 15 dias (antecipada) x 30 dias (cautelar).",
      "palavras_chave": [
       "aditamento",
       "15 dias",
       "antecipada antecedente"
      ],
      "correcao": {
       "erro": "Atribui à tutela antecipada antecedente o prazo de 30 dias para o aditamento.",
       "certo": "Concedida a tutela antecipada antecedente, o autor deve aditar a petição inicial em 15 dias ou em outro prazo maior que o juiz fixar."
      },
      "aprofundamento": "A tutela antecipada antecedente permite que o autor, diante de urgência contemporânea à propositura, apresente só o pedido urgente e indique o pedido final, completando a inicial depois. Concedida a tutela, ele deve **aditar** a petição inicial, complementando argumentos, juntando documentos e confirmando o pedido final.\n\nO prazo do aditamento é de 15 dias ou outro maior fixado pelo juiz. Se o autor não aditar, o processo é extinto sem resolução do mérito. A lógica é evitar que a parte se beneficie da tutela provisória sem levar adiante a discussão do mérito.\n\nA pegadinha é a mistura com a cautelar antecedente, em que o pedido principal deve ser formulado em 30 dias da efetivação da medida (art. 308). Antecipada: 15. Cautelar: 30.",
      "memorize": "Antecipada antecedente: aditar em 15 dias. Cautelar antecedente: pedido principal em 30 dias."
     }
    },
    {
     "id": "CPC-5-R1-07",
     "ponto": "DBA26-CPC-5",
     "tema": "Estabilização",
     "assertiva": "A tutela antecipada concedida em caráter antecedente torna-se estável se da decisão que a conceder não for interposto o respectivo recurso.",
     "gabarito": "C",
     "comentario": {
      "resumo": "Art. 304, caput: **estabilização** pela inércia recursal do réu; o processo é extinto (§ 1º).",
      "lei": [
       {
        "lei": "L13105",
        "art": "304",
        "par": "",
        "inc": "",
        "rotulo": "CPC, art. 304",
        "texto": "A tutela antecipada, concedida nos termos do art. 303, torna-se estável se da decisão que a conceder não for interposto o respectivo recurso."
       }
      ],
      "palavras_chave": [
       "estabilização",
       "recurso"
      ],
      "aprofundamento": "A **estabilização** é uma técnica de monitorização do processo: se o réu, diante da tutela antecipada antecedente, não se insurge, presume-se que ele se conforma com a situação, e não faz sentido obrigar as partes a prosseguir num processo que ninguém quer. O processo é extinto e a decisão continua produzindo efeitos.\n\nOs requisitos são específicos: tutela **antecipada** (não cautelar), requerida em **caráter antecedente** e ausência de **recurso** contra a decisão. A tutela estabilizada pode ser revista por ação própria, dentro do prazo legal.\n\nA banca costuma estender a estabilização à tutela cautelar ou à incidental. Há debate sobre se outra forma de impugnação, além do recurso, impede a estabilização, mas o texto legal fala em recurso.",
      "memorize": "Estabilização: só tutela antecipada antecedente sem recurso do réu; processo extinto."
     }
    },
    {
     "id": "CPC-5-R1-08",
     "ponto": "DBA26-CPC-5",
     "tema": "Prazo para rever a tutela estabilizada",
     "assertiva": "O direito de rever, reformar ou invalidar a tutela antecipada estabilizada extingue-se após 5 anos, contados da ciência da decisão que extinguiu o processo.",
     "gabarito": "E",
     "comentario": {
      "resumo": "Art. 304, § 5º: **2 anos**.",
      "lei": [
       {
        "lei": "L13105",
        "art": "304",
        "par": "",
        "inc": "",
        "rotulo": "CPC, art. 304, § 5º",
        "texto": "O direito de rever, reformar ou invalidar a tutela antecipada, previsto no § 2º deste artigo, extingue-se após 2 (dois) anos, contados da ciência da decisão que extinguiu o processo"
       }
      ],
      "palavras_chave": [
       "estabilização",
       "2 anos"
      ],
      "correcao": {
       "erro": "Fixa em 5 anos o prazo para rever, reformar ou invalidar a tutela estabilizada.",
       "certo": "O direito de rever, reformar ou invalidar a tutela antecipada estabilizada extingue-se após 2 anos, contados da ciência da decisão que extinguiu o processo."
      },
      "aprofundamento": "A tutela estabilizada não é imutável. Qualquer das partes pode propor ação para **rever, reformar ou invalidar** a decisão, e o juízo que concedeu a tutela fica prevento. Enquanto isso, a tutela conserva seus efeitos.\n\nEsse direito, porém, tem limite temporal. O prazo de 2 anos conta da ciência da decisão que extinguiu o processo, e não da decisão que concedeu a tutela. Passado esse prazo, discute-se na doutrina se a decisão se torna imutável, mas o texto legal afirma que ela não faz coisa julgada.\n\nA banca altera o número. O prazo de 2 anos coincide com o da ação rescisória, o que ajuda a memorizar; o de 5 anos não tem previsão nesse ponto.",
      "memorize": "Rever tutela estabilizada: 2 anos da ciência da decisão que extinguiu o processo."
     }
    },
    {
     "id": "CPC-5-R1-09",
     "ponto": "DBA26-CPC-5",
     "tema": "Estabilização x coisa julgada",
     "assertiva": "A decisão que concede a tutela antecipada estabilizada faz coisa julgada material.",
     "gabarito": "E",
     "comentario": {
      "resumo": "Art. 304, § 6º: **não faz coisa julgada**; a estabilidade só cai por decisão na ação do § 2º.",
      "lei": [
       {
        "lei": "L13105",
        "art": "304",
        "par": "",
        "inc": "",
        "rotulo": "CPC, art. 304, § 6º",
        "texto": "A decisão que concede a tutela não fará coisa julgada"
       }
      ],
      "palavras_chave": [
       "coisa julgada",
       "estabilidade"
      ],
      "correcao": {
       "erro": "Atribui coisa julgada material à decisão que concede a tutela antecipada estabilizada.",
       "certo": "A decisão que concede a tutela estabilizada não faz coisa julgada; sua estabilidade só é afastada por decisão na ação de revisão, reforma ou invalidação."
      },
      "aprofundamento": "Estabilidade e coisa julgada são fenômenos distintos. A **coisa julgada material** pressupõe cognição exauriente: o juiz examinou o mérito em profundidade, com contraditório pleno. A tutela estabilizada nasce de **cognição sumária** e da inércia do réu, sem que o mérito tenha sido debatido.\n\nPor isso a lei diz expressamente que a decisão não faz coisa julgada. A estabilidade só é afastada por decisão de mérito na ação própria de revisão, reforma ou invalidação.\n\nUma consequência prática debatida é que, como não há coisa julgada, não cabe ação rescisória contra a decisão estabilizada. A banca tenta igualar os dois institutos; a resposta é sempre que estabilização não é coisa julgada.",
      "memorize": "Tutela estabilizada: estável, mas NÃO faz coisa julgada."
     }
    },
    {
     "id": "CPC-5-R1-10",
     "ponto": "DBA26-CPC-5",
     "tema": "Cautelar antecedente — pedido principal",
     "assertiva": "Efetivada a tutela cautelar, o pedido principal terá de ser formulado pelo autor no prazo de 30 dias, nos mesmos autos, sem adiantamento de novas custas.",
     "gabarito": "C",
     "comentario": {
      "resumo": "**Art. 308.**",
      "lei": [
       {
        "lei": "L13105",
        "art": "308",
        "par": "",
        "inc": "",
        "rotulo": "CPC, art. 308",
        "texto": "Efetivada a tutela cautelar, o pedido principal terá de ser formulado pelo autor no prazo de 30 (trinta) dias, caso em que será apresentado nos mesmos autos em que deduzido o pedido de tutela cautelar, não dependendo do adiantamento de novas custas processuais."
       }
      ],
      "palavras_chave": [
       "cautelar antecedente",
       "30 dias"
      ],
      "aprofundamento": "Na cautelar antecedente, o autor pede apenas a medida conservativa e indica a lide principal. Efetivada a medida, ele tem 30 dias para formular o **pedido principal**, porque a cautelar existe para servir a um processo de mérito, e não pode permanecer indefinidamente sem ele.\n\nO pedido principal é apresentado **nos mesmos autos**, sem novas custas: o CPC abandonou o modelo de processo cautelar autônomo. Se o prazo não for cumprido, a eficácia da tutela cautelar **cessa**.\n\nO marco inicial é a **efetivação** da medida, e não a decisão que a concede. A banca costuma trocar o prazo pelo da antecipada antecedente ou exigir ação principal autônoma, nos moldes do código revogado.",
      "exemplo": "Bruno obtém o arresto de bens do devedor, efetivado numa segunda-feira. A partir daí corre o prazo para ele formular, nos mesmos autos, o pedido de cobrança.",
      "memorize": "Cautelar antecedente: pedido principal em 30 dias da efetivação, nos mesmos autos, sem novas custas."
     }
    },
    {
     "id": "CPC-5-R1-11",
     "ponto": "DBA26-CPC-5",
     "tema": "Tutela da evidência",
     "assertiva": "A tutela da evidência exige a demonstração de perigo de dano ou de risco ao resultado útil do processo.",
     "gabarito": "E",
     "comentario": {
      "resumo": "Art. 311: a evidência é concedida **independentemente** da demonstração de perigo de dano.",
      "lei": [
       {
        "lei": "L13105",
        "art": "311",
        "par": "",
        "inc": "",
        "rotulo": "CPC, art. 311",
        "texto": "A tutela da evidência será concedida, independentemente da demonstração de perigo de dano ou de risco ao resultado útil do processo"
       }
      ],
      "palavras_chave": [
       "evidência",
       "sem urgência"
      ],
      "correcao": {
       "erro": "Exige demonstração de perigo de dano ou risco ao resultado útil para a tutela da evidência.",
       "certo": "A tutela da evidência é concedida independentemente da demonstração de perigo de dano ou de risco ao resultado útil do processo."
      },
      "aprofundamento": "A tutela da evidência parte de uma ideia de justiça na distribuição do **ônus do tempo**. Quando o direito do autor é evidente e a defesa do réu é frágil ou abusiva, não é justo que o autor suporte sozinho a demora do processo.\n\nPor isso ela é concedida **independentemente** de perigo de dano. As hipóteses legais incluem o abuso do direito de defesa ou o propósito protelatório, a prova documental com tese firmada em repetitivos ou súmula vinculante, o pedido reipersecutório fundado em contrato de depósito e a prova documental a que o réu não oponha dúvida razoável.\n\nA fronteira com a urgência é exatamente o perigo: urgência exige probabilidade e perigo; evidência dispensa o perigo. A assertiva inverte isso.",
      "memorize": "Evidência dispensa perigo; urgência exige."
     }
    },
    {
     "id": "CPC-5-R1-12",
     "ponto": "DBA26-CPC-5",
     "tema": "Responsabilidade do requerente",
     "assertiva": "Independentemente da reparação por dano processual, a parte responde pelo prejuízo que a efetivação da tutela de urgência causar à parte adversa se a sentença lhe for desfavorável.",
     "gabarito": "C",
     "comentario": {
      "resumo": "Art. 302, I: responsabilidade **objetiva** do beneficiário da tutela.",
      "lei": [
       {
        "lei": "L13105",
        "art": "302",
        "par": "",
        "inc": "",
        "rotulo": "CPC, art. 302, I",
        "texto": "Independentemente da reparação por dano processual, a parte responde pelo prejuízo que a efetivação da tutela de urgência causar à parte adversa, se:\nI - a sentença lhe for desfavorável;"
       }
      ],
      "palavras_chave": [
       "responsabilidade objetiva"
      ],
      "aprofundamento": "Quem obtém tutela de urgência age por sua conta e risco. A medida é concedida com base em cognição sumária, e se ao final se verificar que o beneficiário não tinha razão, ele deve reparar o prejuízo causado ao adversário.\n\nA responsabilidade é **objetiva**: independe de culpa ou de má-fé. Basta o dano decorrente da efetivação e uma das hipóteses legais, como a sentença desfavorável. Isso é diferente da reparação por dano processual, que pressupõe litigância de má-fé, e as duas podem coexistir.\n\nA indenização é liquidada, sempre que possível, nos próprios autos. A banca costuma exigir dolo ou culpa do requerente, o que contraria o caráter objetivo da responsabilidade.",
      "exemplo": "Lucas obtém liminar que suspende as vendas de um concorrente. Ao final, perde a ação: deve indenizar o concorrente pelos prejuízos, ainda que tenha agido de boa-fé.",
      "memorize": "Tutela de urgência: responsabilidade objetiva do beneficiário se a sentença lhe for desfavorável."
     }
    },
    {
     "id": "CPC-6-R1-01",
     "ponto": "DBA26-CPC-6",
     "tema": "Formação do processo",
     "assertiva": "Considera-se proposta a ação quando a petição inicial for protocolada, mas a propositura só produz quanto ao réu os efeitos do art. 240 depois que ele for validamente citado.",
     "gabarito": "C",
     "comentario": {
      "resumo": "**Art. 312.**",
      "lei": [
       {
        "lei": "L13105",
        "art": "312",
        "par": "",
        "inc": "",
        "rotulo": "CPC, art. 312",
        "texto": "Considera-se proposta a ação quando a petição inicial for protocolada, todavia, a propositura da ação só produz quanto ao réu os efeitos mencionados no art. 240 depois que for validamente citado."
       }
      ],
      "palavras_chave": [
       "propositura",
       "citação"
      ],
      "aprofundamento": "O artigo separa dois momentos. Para o **autor**, a ação existe desde o protocolo da petição inicial: é aí que se fixa a competência e se marca a propositura. Para o **réu**, os efeitos só começam com a citação válida, porque não seria justo que ele sofresse consequências de um processo do qual nem sabe.\n\nOs efeitos referidos são os da citação: litispendência, litigiosidade da coisa e constituição em mora. Até a citação, a relação processual é linear, entre autor e juiz; com ela, torna-se triangular.\n\nA banca costuma dizer que a ação só se considera proposta com a citação, ou que os efeitos atingem o réu desde o protocolo. As duas trocas desfazem a distinção que o artigo faz.",
      "memorize": "Ação proposta com o protocolo; efeitos para o réu só com a citação válida."
     }
    },
    {
     "id": "CPC-6-R1-02",
     "ponto": "DBA26-CPC-6",
     "tema": "Suspensão por morte",
     "assertiva": "Suspende-se o processo pela morte ou pela perda da capacidade processual de qualquer das partes, de seu representante legal ou de seu procurador.",
     "gabarito": "C",
     "comentario": {
      "resumo": "**Art. 313, I**.",
      "lei": [
       {
        "lei": "L13105",
        "art": "313",
        "par": "",
        "inc": "",
        "rotulo": "CPC, art. 313, I",
        "texto": "pela morte ou pela perda da capacidade processual de qualquer das partes, de seu representante legal ou de seu procurador;"
       }
      ],
      "palavras_chave": [
       "suspensão",
       "morte"
      ],
      "aprofundamento": "A suspensão por morte ou perda da capacidade protege o **contraditório**. Se a parte morre, alguém precisa sucedê-la; se o procurador morre, a parte fica sem defesa técnica. Seguir com o processo nessas condições geraria atos praticados contra quem não pode reagir.\n\nO juiz, ao tomar conhecimento do fato, suspende o processo e adota as providências para a habilitação dos sucessores ou para que a parte constitua novo advogado, com prazos e consequências previstos em lei para o caso de inércia.\n\nA regra abrange três figuras: a parte, o **representante legal** e o **procurador**. A banca costuma restringir a hipótese à morte da parte, excluindo o advogado ou o representante.",
      "memorize": "Morte ou perda de capacidade da parte, do representante legal ou do procurador suspende o processo."
     }
    },
    {
     "id": "CPC-6-R1-03",
     "ponto": "DBA26-CPC-6",
     "tema": "Suspensão convencional — prazo",
     "assertiva": "A suspensão do processo por convenção das partes pode durar até 1 ano.",
     "gabarito": "E",
     "comentario": {
      "resumo": "Art. 313, § 4º: convenção → **nunca mais de 6 meses**; prejudicialidade (inciso V) → **nunca mais de 1 ano**.",
      "lei": [
       {
        "lei": "L13105",
        "art": "313",
        "par": "",
        "inc": "",
        "rotulo": "CPC, art. 313, § 4º",
        "texto": "O prazo de suspensão do processo nunca poderá exceder 1 (um) ano nas hipóteses do inciso V e 6 (seis) meses naquela prevista no inciso II."
       }
      ],
      "palavras_chave": [
       "convenção",
       "6 meses"
      ],
      "correcao": {
       "erro": "Fixa em 1 ano o prazo máximo da suspensão convencional.",
       "certo": "A suspensão por convenção das partes nunca pode exceder 6 meses; o limite de 1 ano é das hipóteses do inciso V (prejudicialidade)."
      },
      "aprofundamento": "A suspensão convencional respeita a autonomia das partes: elas podem querer tempo para negociar um acordo. Mas o processo é também serviço público, e não pode ficar parado indefinidamente por vontade das partes. Por isso a lei fixa um teto curto.\n\nO teto é de 6 meses para a suspensão por convenção (inciso II). Já a suspensão por **prejudicialidade externa** (inciso V), quando o julgamento depende de outra causa ou de fato a ser verificado, pode chegar a 1 ano, porque ali o motivo independe da vontade das partes. Esgotado o prazo, o processo retoma seu curso.\n\nA assertiva troca os limites: aplica à convenção o prazo próprio da prejudicialidade.",
      "memorize": "Suspensão: convenção até 6 meses; prejudicialidade até 1 ano."
     }
    },
    {
     "id": "CPC-6-R1-04",
     "ponto": "DBA26-CPC-6",
     "tema": "Atos durante a suspensão",
     "assertiva": "Durante a suspensão é vedado praticar qualquer ato processual, inclusive os urgentes destinados a evitar dano irreparável.",
     "gabarito": "E",
     "comentario": {
      "resumo": "Art. 314: o juiz **pode determinar atos urgentes** para evitar dano irreparável (salvo na arguição de impedimento e suspeição).",
      "lei": [
       {
        "lei": "L13105",
        "art": "314",
        "par": "",
        "inc": "",
        "rotulo": "CPC, art. 314",
        "texto": "Durante a suspensão é vedado praticar qualquer ato processual, podendo o juiz, todavia, determinar a realização de atos urgentes a fim de evitar dano irreparável, salvo no caso de arguição de impedimento e de suspeição."
       }
      ],
      "palavras_chave": [
       "suspensão",
       "atos urgentes"
      ],
      "correcao": {
       "erro": "Veda, durante a suspensão, até os atos urgentes destinados a evitar dano irreparável.",
       "certo": "Durante a suspensão é vedado praticar atos processuais, mas o juiz pode determinar atos urgentes para evitar dano irreparável, salvo na arguição de impedimento e de suspeição."
      },
      "aprofundamento": "A suspensão paralisa a marcha do processo, e por isso, como regra, nenhum ato pode ser praticado. Mas paralisar não pode significar deixar perecer o direito. Se houver risco de dano irreparável, o juiz pode determinar **atos urgentes**, como a produção antecipada de uma prova ou uma medida conservativa.\n\nA exceção da exceção é a arguição de **impedimento ou suspeição**: enquanto se discute a imparcialidade do juiz, não faz sentido que ele mesmo pratique atos, ainda que urgentes. Nesse caso, a tutela de urgência é requerida ao substituto legal.\n\nA assertiva erra ao vedar inclusive os atos urgentes. Fique atento à estrutura em três camadas: regra (vedação), exceção (atos urgentes) e contraexceção (impedimento e suspeição).",
      "memorize": "Suspenso: nada se pratica, salvo atos urgentes; mas não na arguição de impedimento/suspeição."
     }
    },
    {
     "id": "CPC-6-R1-05",
     "ponto": "DBA26-CPC-6",
     "tema": "Extinção sem mérito",
     "assertiva": "O juiz não resolverá o mérito quando verificar ausência de legitimidade ou de interesse processual.",
     "gabarito": "C",
     "comentario": {
      "resumo": "**Art. 485, VI**.",
      "lei": [
       {
        "lei": "L13105",
        "art": "485",
        "par": "",
        "inc": "",
        "rotulo": "CPC, art. 485, VI",
        "texto": "VI - verificar ausência de legitimidade ou de interesse processual;"
       }
      ],
      "palavras_chave": [
       "extinção sem mérito",
       "condições da ação"
      ],
      "aprofundamento": "Legitimidade e interesse são as **condições da ação** do CPC atual. Sem elas, o juiz não pode examinar o mérito, porque a demanda foi proposta por quem não deveria ou sem necessidade e utilidade da tutela pedida.\n\nA consequência é a extinção **sem resolução do mérito**, o que permite, em regra, nova propositura, desde que corrigido o vício. Essa matéria pode ser conhecida de ofício, em qualquer tempo e grau, até o trânsito em julgado.\n\nHá uma discussão doutrinária relevante: pela teoria da asserção, as condições da ação são aferidas pelo que o autor afirma na inicial; se só se constata a ilegitimidade depois da instrução, parte da doutrina entende que a decisão é de mérito. Na prova objetiva, prevalece a letra da lei.",
      "memorize": "Sem legitimidade ou interesse: extinção sem resolução do mérito."
     }
    },
    {
     "id": "CPC-6-R1-06",
     "ponto": "DBA26-CPC-6",
     "tema": "Mérito x sem mérito",
     "assertiva": "Haverá resolução de mérito quando o juiz homologar a desistência da ação.",
     "gabarito": "E",
     "comentario": {
      "resumo": "Desistência → **sem mérito** (art. 485, VIII). Com mérito é a homologação de **reconhecimento da procedência, transação ou renúncia** (art. 487, III).",
      "lei": [
       {
        "lei": "L13105",
        "art": "485",
        "par": "",
        "inc": "",
        "rotulo": "CPC, art. 485, VIII",
        "texto": "VIII - homologar a desistência da ação;"
       },
       {
        "lei": "L13105",
        "art": "487",
        "par": "",
        "inc": "",
        "rotulo": "CPC, art. 487, III",
        "texto": "III - homologar:\na) o reconhecimento da procedência do pedido formulado na ação ou na reconvenção;\nb) a transação;\nc) a renúncia à pretensão formulada na ação ou na reconvenção."
       }
      ],
      "pegadinha": "Trocar \"desistência\" (da ação) por \"renúncia\" (ao direito).",
      "palavras_chave": [
       "desistência",
       "renúncia"
      ],
      "correcao": {
       "erro": "Classifica a homologação da desistência da ação como resolução de mérito.",
       "certo": "A homologação da desistência da ação extingue o processo sem resolução do mérito; há resolução de mérito na homologação do reconhecimento da procedência, da transação ou da renúncia."
      },
      "aprofundamento": "A distinção depende do objeto da manifestação de vontade. Na **desistência da ação**, o autor abre mão apenas do processo: o direito material fica intacto e ele pode propor nova ação. Por isso a sentença é **sem resolução do mérito**.\n\nNa **renúncia à pretensão**, o autor abre mão do próprio direito; no **reconhecimento da procedência**, o réu admite o pedido; na **transação**, as partes fazem concessões recíprocas. Nesses três casos o conflito material é resolvido, e a homologação é sentença **com resolução do mérito**, apta a fazer coisa julgada material.\n\nA banca troca desistência por renúncia. Pergunte-se: o direito material foi atingido? Se não, é sem mérito.",
      "memorize": "Desistência = sem mérito (larga o processo). Renúncia = com mérito (larga o direito)."
     }
    },
    {
     "id": "CPC-6-R1-07",
     "ponto": "DBA26-CPC-6",
     "tema": "Desistência após a contestação",
     "assertiva": "Oferecida a contestação, o autor não poderá, sem o consentimento do réu, desistir da ação.",
     "gabarito": "C",
     "comentario": {
      "resumo": "**Art. 485, § 4º**.",
      "lei": [
       {
        "lei": "L13105",
        "art": "485",
        "par": "",
        "inc": "",
        "rotulo": "CPC, art. 485, § 4º",
        "texto": "Oferecida a contestação, o autor não poderá, sem o consentimento do réu, desistir da ação."
       }
      ],
      "palavras_chave": [
       "desistência",
       "consentimento do réu"
      ],
      "aprofundamento": "Depois da contestação, o réu já investiu na defesa e pode ter interesse legítimo em obter uma sentença de mérito que o proteja definitivamente. Se o autor pudesse desistir livremente, poderia repropor a ação depois, mantendo o réu sob ameaça permanente.\n\nPor isso a desistência, a partir desse momento, exige o **consentimento do réu**. A recusa, porém, deve ser motivada; a jurisprudência tende a não admitir oposição sem fundamento razoável.\n\nAntes da contestação, a desistência é ato unilateral do autor, que só depende de homologação. A banca costuma trocar o marco temporal (citação no lugar de contestação) ou dispensar o consentimento.",
      "memorize": "Após a contestação, desistência só com o consentimento do réu."
     }
    },
    {
     "id": "CPC-6-R1-08",
     "ponto": "DBA26-CPC-6",
     "tema": "Limite temporal da desistência",
     "assertiva": "A desistência da ação pode ser apresentada até o trânsito em julgado.",
     "gabarito": "E",
     "comentario": {
      "resumo": "Art. 485, § 5º: **até a sentença**.",
      "lei": [
       {
        "lei": "L13105",
        "art": "485",
        "par": "",
        "inc": "",
        "rotulo": "CPC, art. 485, § 5º",
        "texto": "A desistência da ação pode ser apresentada até a sentença."
       }
      ],
      "palavras_chave": [
       "desistência",
       "até a sentença"
      ],
      "correcao": {
       "erro": "Admite a desistência da ação até o trânsito em julgado.",
       "certo": "A desistência da ação pode ser apresentada até a sentença."
      },
      "aprofundamento": "A desistência só faz sentido enquanto não há julgamento. Depois da sentença, o autor já obteve uma decisão sobre a causa, e permitir a desistência seria deixá-lo apagar um resultado desfavorável para tentar de novo.\n\nDepois da sentença, o caminho para a parte que não quer prosseguir é outro: ela pode **desistir do recurso**, o que não depende da concordância da parte contrária, ou **renunciar ao direito** de recorrer. Nesses casos, a sentença prevalece.\n\nA assertiva estende o prazo até o trânsito em julgado. Não confunda desistência da ação, que tem limite na sentença, com desistência do recurso, que pode ocorrer enquanto o recurso estiver pendente.",
      "memorize": "Desistência da ação: até a sentença. Depois, só desistência do recurso."
     }
    },
    {
     "id": "CPC-6-R1-09",
     "ponto": "DBA26-CPC-6",
     "tema": "Matérias de ofício",
     "assertiva": "O juiz conhecerá de ofício, em qualquer tempo e grau de jurisdição, enquanto não ocorrer o trânsito em julgado, da ausência de pressupostos processuais, da perempção, litispendência ou coisa julgada e da ausência de legitimidade ou interesse.",
     "gabarito": "C",
     "comentario": {
      "resumo": "**Art. 485, § 3º** (incisos IV, V, VI e IX).",
      "lei": [
       {
        "lei": "L13105",
        "art": "485",
        "par": "",
        "inc": "",
        "rotulo": "CPC, art. 485, § 3º",
        "texto": "O juiz conhecerá de ofício da matéria constante dos incisos IV, V, VI e IX, em qualquer tempo e grau de jurisdição, enquanto não ocorrer o trânsito em julgado."
       }
      ],
      "palavras_chave": [
       "ordem pública",
       "de ofício"
      ],
      "aprofundamento": "Algumas matérias dizem respeito à **regularidade do próprio processo** e não podem ficar à disposição das partes: pressupostos processuais, perempção, litispendência, coisa julgada, legitimidade e interesse. Por isso o juiz as conhece de ofício e em qualquer grau.\n\nO limite é o **trânsito em julgado**. Depois dele, vícios graves só podem ser atacados pelos meios próprios, como a ação rescisória. E, mesmo conhecendo de ofício, o juiz deve ouvir as partes antes de decidir, pela vedação à decisão surpresa.\n\nRepare que a lista não inclui a convenção de arbitragem nem o abandono da causa após a contestação, que dependem de alegação ou requerimento da parte. É aí que a banca costuma colocar a pegadinha.",
      "memorize": "De ofício, até o trânsito: pressupostos, perempção, litispendência, coisa julgada, legitimidade e interesse."
     }
    },
    {
     "id": "CPC-6-R1-10",
     "ponto": "DBA26-CPC-6",
     "tema": "Perempção",
     "assertiva": "Se o autor der causa, por 2 vezes, a sentença fundada em abandono da causa, não poderá propor nova ação contra o réu com o mesmo objeto.",
     "gabarito": "E",
     "comentario": {
      "resumo": "Art. 486, § 3º: **3 vezes**. Fica ressalvada a alegação do direito em defesa.",
      "lei": [
       {
        "lei": "L13105",
        "art": "486",
        "par": "",
        "inc": "",
        "rotulo": "CPC, art. 486, § 3º",
        "texto": "Se o autor der causa, por 3 (três) vezes, a sentença fundada em abandono da causa, não poderá propor nova ação contra o réu com o mesmo objeto, ficando-lhe ressalvada, entretanto, a possibilidade de alegar em defesa o seu direito."
       }
      ],
      "palavras_chave": [
       "perempção",
       "3 vezes"
      ],
      "correcao": {
       "erro": "Fixa em 2 o número de abandonos que gera a perempção.",
       "certo": "Se o autor der causa, por 3 vezes, a sentença fundada em abandono, não poderá propor nova ação contra o réu com o mesmo objeto, ressalvada a alegação do direito em defesa."
      },
      "aprofundamento": "A **perempção** é uma sanção à litigância irresponsável. O autor que, repetidas vezes, ajuíza ação e a abandona, movimentando a máquina judiciária e obrigando o réu a se defender sem levar a causa adiante, perde o direito de demandar de novo sobre o mesmo objeto.\n\nO número exigido é de 3 sentenças por abandono. A perda, porém, é apenas do **direito de ação**: o direito material sobrevive, e o autor pode alegá-lo **em defesa** se for demandado pelo réu.\n\nA perempção é pressuposto processual negativo, conhecível de ofício. A banca reduz o número de vezes ou afirma que o autor perde o próprio direito material, inclusive como matéria de defesa.",
      "memorize": "Perempção: 3 abandonos. Perde a ação, não o direito (pode alegá-lo em defesa)."
     }
    },
    {
     "id": "CPC-6-R1-11",
     "ponto": "DBA26-CPC-6",
     "tema": "Abandono da causa",
     "assertiva": "Mesmo depois de oferecida a contestação, a extinção do processo por abandono da causa pelo autor pode ser decretada de ofício.",
     "gabarito": "E",
     "comentario": {
      "resumo": "Art. 485, § 6º e Súmula 240/STJ: após a contestação, depende de **requerimento do réu**.",
      "lei": [
       {
        "lei": "L13105",
        "art": "485",
        "par": "",
        "inc": "",
        "rotulo": "CPC, art. 485, § 6º",
        "texto": "Oferecida a contestação, a extinção do processo por abandono da causa pelo autor depende de requerimento do réu."
       }
      ],
      "juris": [
       {
        "tribunal": "STJ",
        "fonte": "Súmula 240/STJ",
        "data": "02/08/2000",
        "texto": "A extinção do processo, por abandono da causa pelo autor, depende de requerimento do réu."
       }
      ],
      "palavras_chave": [
       "abandono",
       "requerimento do réu"
      ],
      "correcao": {
       "erro": "Permite a extinção de ofício por abandono do autor mesmo depois da contestação.",
       "certo": "Oferecida a contestação, a extinção do processo por abandono da causa pelo autor depende de requerimento do réu (Súmula 240/STJ)."
      },
      "aprofundamento": "Depois da contestação, o réu tem interesse em obter uma sentença de mérito, que lhe dá segurança definitiva. A extinção por abandono, sem mérito, permite que o autor volte com a mesma ação. Por isso a lei condiciona essa extinção ao **requerimento do réu**: cabe a ele escolher se prefere encerrar o processo ou prosseguir até o julgamento.\n\nA Súmula 240 do STJ já firmava essa orientação antes do código atual, que a incorporou ao texto. Antes da contestação, o juiz pode extinguir por abandono de ofício, desde que intime a parte pessoalmente para dar andamento e ela permaneça inerte.\n\nA assertiva erra ao permitir a extinção de ofício depois da contestação, exatamente o momento em que a lei passa a exigir o pedido do réu.",
      "memorize": "Abandono após contestação: só a requerimento do réu (Súmula 240/STJ)."
     }
    },
    {
     "id": "CPC-6-R1-12",
     "ponto": "DBA26-CPC-6",
     "tema": "Primazia do mérito",
     "assertiva": "Antes de proferir decisão sem resolução de mérito, o juiz deverá conceder à parte oportunidade para, se possível, corrigir o vício.",
     "gabarito": "C",
     "comentario": {
      "resumo": "Art. 317: **primazia do julgamento de mérito**.",
      "lei": [
       {
        "lei": "L13105",
        "art": "317",
        "par": "",
        "inc": "",
        "rotulo": "CPC, art. 317",
        "texto": "Antes de proferir decisão sem resolução de mérito, o juiz deverá conceder à parte oportunidade para, se possível, corrigir o vício."
       }
      ],
      "palavras_chave": [
       "primazia do mérito",
       "sanabilidade"
      ],
      "aprofundamento": "Esta é uma das manifestações mais concretas da **primazia do julgamento de mérito**. O processo existe para resolver o conflito; extingui-lo por vício formal que poderia ser corrigido frustra o direito da parte e desperdiça o trabalho já feito.\n\nPor isso o juiz tem o **dever** de oportunizar a correção antes de extinguir sem mérito. A expressão \"se possível\" reconhece que há vícios insanáveis, como a coisa julgada, em que não há o que corrigir.\n\nO mesmo espírito aparece em vários pontos do código: emenda da inicial, correção de vício em recurso, complementação de preparo. A banca costuma transformar o dever em faculdade (\"poderá\") ou dizer que o juiz pode extinguir diretamente.",
      "memorize": "Antes de extinguir sem mérito, o juiz DEVE dar chance de corrigir o vício sanável."
     }
    },
    {
     "id": "CPC-7-R1-01",
     "ponto": "DBA26-CPC-7",
     "tema": "Petição inicial — requisitos",
     "assertiva": "A petição inicial indicará a opção do autor pela realização ou não de audiência de conciliação ou de mediação.",
     "gabarito": "C",
     "comentario": {
      "resumo": "**Art. 319, VII**.",
      "lei": [
       {
        "lei": "L13105",
        "art": "319",
        "par": "",
        "inc": "",
        "rotulo": "CPC, art. 319, VII",
        "texto": "VII - a opção do autor pela realização ou não de audiência de conciliação ou de mediação."
       }
      ],
      "palavras_chave": [
       "petição inicial",
       "requisitos"
      ],
      "aprofundamento": "A exigência de que o autor declare sua opção sobre a audiência de conciliação ou mediação reflete o estímulo do CPC à **autocomposição**. Logo na petição inicial, o autor diz se quer ou não tentar um acordo.\n\nEssa manifestação tem consequência prática: a audiência só deixa de ser realizada se **ambas as partes** manifestarem desinteresse, ou se o direito não admitir autocomposição. O autor declara na inicial; o réu, por petição, com antecedência em relação à data designada.\n\nA banca costuma dizer que a simples manifestação do autor basta para dispensar a audiência, ou omitir esse requisito do rol da petição inicial. Lembre que a manifestação do autor é só uma das duas necessárias para afastar a audiência.",
      "memorize": "Inicial indica se o autor quer ou não a audiência; dispensa só se ambos recusarem."
     }
    },
    {
     "id": "CPC-7-R1-02",
     "ponto": "DBA26-CPC-7",
     "tema": "Emenda da inicial",
     "assertiva": "Verificando defeitos na petição inicial, o juiz determinará que o autor a emende ou complete no prazo de 10 dias.",
     "gabarito": "E",
     "comentario": {
      "resumo": "Art. 321: **15 dias**, indicando com precisão o que deve ser corrigido.",
      "lei": [
       {
        "lei": "L13105",
        "art": "321",
        "par": "",
        "inc": "",
        "rotulo": "CPC, art. 321",
        "texto": "determinará que o autor, no prazo de 15 (quinze) dias, a emende ou a complete, indicando com precisão o que deve ser corrigido ou completado."
       }
      ],
      "pegadinha": "10 dias era o prazo do CPC/1973.",
      "palavras_chave": [
       "emenda",
       "15 dias"
      ],
      "correcao": {
       "erro": "Fixa em 10 dias o prazo para emenda da petição inicial.",
       "certo": "Verificando defeitos na inicial, o juiz determinará que o autor a emende ou complete em 15 dias, indicando com precisão o que deve ser corrigido ou completado."
      },
      "aprofundamento": "A emenda da inicial é expressão da **primazia do mérito** e do **dever de prevenção** do juiz. Antes de indeferir a petição por defeito sanável, ele deve dar ao autor a chance de corrigir.\n\nO CPC atual ampliou o prazo para 15 dias e exige que o juiz **indique com precisão** o que deve ser corrigido ou completado. O despacho genérico (\"emende a inicial\") não atende à exigência, porque o autor não sabe o que fazer. Se o autor não cumprir a diligência, a petição é indeferida.\n\nO prazo de 10 dias era o do código revogado, e a banca o reaproveita. A falta de indicação precisa do vício também é ponto cobrado.",
      "memorize": "Emenda da inicial: 15 dias, com indicação precisa do vício."
     }
    },
    {
     "id": "CPC-7-R1-03",
     "ponto": "DBA26-CPC-7",
     "tema": "Improcedência liminar",
     "assertiva": "Nas causas que dispensem a fase instrutória, o juiz, independentemente da citação do réu, julgará liminarmente improcedente o pedido que contrariar enunciado de súmula do STF ou do STJ.",
     "gabarito": "C",
     "comentario": {
      "resumo": "**Art. 332, I**. Também: repetitivos, IRDR/IAC, súmula de TJ sobre direito local e prescrição/decadência (§ 1º).",
      "lei": [
       {
        "lei": "L13105",
        "art": "332",
        "par": "",
        "inc": "",
        "rotulo": "CPC, art. 332, I",
        "texto": "Nas causas que dispensem a fase instrutória, o juiz, independentemente da citação do réu, julgará liminarmente improcedente o pedido que contrariar:\nI - enunciado de súmula do Supremo Tribunal Federal ou do Superior Tribunal de Justiça;"
       }
      ],
      "palavras_chave": [
       "improcedência liminar"
      ],
      "aprofundamento": "A improcedência liminar permite que o juiz julgue o mérito **antes da citação**, quando o pedido contraria entendimento já consolidado. Não faz sentido movimentar o processo e incomodar o réu se o resultado é previsível.\n\nDois requisitos se somam: a causa deve **dispensar a fase instrutória** (questão de direito ou fatos provados por documento) e o pedido deve contrariar um dos precedentes listados, como súmula do STF ou do STJ, acórdão em repetitivos, entendimento em IRDR ou IAC, ou súmula de TJ sobre direito local. O juiz também pode julgar liminarmente improcedente quando verificar prescrição ou decadência.\n\nComo a sentença favorece o réu, a citação é dispensável. Se o autor apelar, o juiz pode se retratar. A banca costuma exigir a citação prévia ou admitir procedência liminar, que não existe.",
      "memorize": "Improcedência liminar: sem citação, causa sem instrução, pedido contra súmula ou precedente qualificado."
     }
    },
    {
     "id": "CPC-7-R1-04",
     "ponto": "DBA26-CPC-7",
     "tema": "Audiência de conciliação — antecedência",
     "assertiva": "A audiência de conciliação ou mediação será designada com antecedência mínima de 30 dias, devendo o réu ser citado com pelo menos 20 dias de antecedência.",
     "gabarito": "C",
     "comentario": {
      "resumo": "Art. 334, caput: **30 dias** (designação) e **20 dias** (citação).",
      "lei": [
       {
        "lei": "L13105",
        "art": "334",
        "par": "",
        "inc": "",
        "rotulo": "CPC, art. 334",
        "texto": "designará audiência de conciliação ou de mediação com antecedência mínima de 30 (trinta) dias, devendo ser citado o réu com pelo menos 20 (vinte) dias de antecedência."
       }
      ],
      "palavras_chave": [
       "audiência de conciliação",
       "30 dias",
       "20 dias"
      ],
      "aprofundamento": "Os prazos da audiência de conciliação existem para dar **tempo útil** a cada etapa. A antecedência mínima de 30 dias na designação permite organizar a pauta e o trabalho dos conciliadores; a citação com pelo menos 20 dias de antecedência garante ao réu tempo para avaliar o caso e comparecer preparado para negociar.\n\nA audiência é conduzida preferencialmente por conciliador ou mediador, e as partes devem estar acompanhadas de advogado ou defensor. A contestação só começa a correr depois dela, se não houver acordo.\n\nA banca troca os números ou inverte qual prazo se refere à designação e qual à citação. Fixe a ordem: 30 para designar, 20 para citar.",
      "memorize": "Audiência de conciliação: designada com 30 dias; réu citado com 20 dias de antecedência."
     }
    },
    {
     "id": "CPC-7-R1-05",
     "ponto": "DBA26-CPC-7",
     "tema": "Dispensa da audiência",
     "assertiva": "A audiência de conciliação não será realizada se qualquer das partes manifestar desinteresse na composição consensual.",
     "gabarito": "E",
     "comentario": {
      "resumo": "Art. 334, § 4º, I: só se **ambas as partes** manifestarem desinteresse (ou quando não se admitir autocomposição).",
      "lei": [
       {
        "lei": "L13105",
        "art": "334",
        "par": "",
        "inc": "",
        "rotulo": "CPC, art. 334, § 4º, I",
        "texto": "I - se ambas as partes manifestarem, expressamente, desinteresse na composição consensual;"
       }
      ],
      "palavras_chave": [
       "ambas as partes",
       "desinteresse"
      ],
      "correcao": {
       "erro": "Dispensa a audiência pela manifestação de desinteresse de apenas uma das partes.",
       "certo": "A audiência não será realizada se ambas as partes manifestarem, expressamente, desinteresse na composição consensual, ou quando não se admitir a autocomposição."
      },
      "aprofundamento": "O CPC aposta na audiência de conciliação como momento privilegiado para o acordo. Mesmo quem diz não querer conversar pode mudar de ideia diante de um mediador qualificado. Por isso a lei não deixa que uma só parte, sozinha, afaste a tentativa de composição.\n\nA audiência só deixa de ser realizada em duas hipóteses: se **ambas as partes** manifestarem expressamente desinteresse, ou quando o direito **não admitir autocomposição**. Havendo litisconsórcio, o desinteresse deve ser manifestado por todos os litisconsortes.\n\nA assertiva troca \"ambas\" por \"qualquer\". Se a frase disser que basta uma parte recusar, está errada. Lembre também que a ausência injustificada é punida com multa.",
      "memorize": "Audiência só é dispensada se AMBAS recusarem (ou se o direito não admitir autocomposição)."
     }
    },
    {
     "id": "CPC-7-R1-06",
     "ponto": "DBA26-CPC-7",
     "tema": "Ausência injustificada",
     "assertiva": "O não comparecimento injustificado do autor ou do réu à audiência de conciliação é ato atentatório à dignidade da justiça, sancionado com multa de até 2% da vantagem econômica pretendida ou do valor da causa.",
     "gabarito": "C",
     "comentario": {
      "resumo": "**Art. 334, § 8º**: multa revertida em favor da União ou do Estado.",
      "lei": [
       {
        "lei": "L13105",
        "art": "334",
        "par": "",
        "inc": "",
        "rotulo": "CPC, art. 334, § 8º",
        "texto": "O não comparecimento injustificado do autor ou do réu à audiência de conciliação é considerado ato atentatório à dignidade da justiça e será sancionado com multa de até dois por cento da vantagem econômica pretendida ou do valor da causa, revertida em favor da União ou do Estado."
       }
      ],
      "palavras_chave": [
       "ato atentatório",
       "2%"
      ],
      "aprofundamento": "A multa pela ausência injustificada reforça a seriedade da audiência de conciliação. Se as partes pudessem simplesmente não comparecer, o esforço de organizar a pauta e mobilizar conciliadores seria desperdiçado, e a política de autocomposição perderia força.\n\nO não comparecimento é qualificado como **ato atentatório à dignidade da justiça**, porque ofende o próprio serviço judiciário, e não apenas a parte contrária. Por isso a multa, de até 2% da vantagem econômica ou do valor da causa, reverte em favor da **União ou do Estado**, e não do adversário.\n\nA parte pode se fazer representar por procurador com poderes para negociar e transigir. A banca costuma dizer que a multa vai para a parte contrária ou alterar o percentual.",
      "memorize": "Falta injustificada à conciliação: ato atentatório, multa de até 2% para União ou Estado."
     }
    },
    {
     "id": "CPC-7-R1-07",
     "ponto": "DBA26-CPC-7",
     "tema": "Preliminares de ofício",
     "assertiva": "O juiz pode conhecer de ofício da convenção de arbitragem, como das demais preliminares de contestação.",
     "gabarito": "E",
     "comentario": {
      "resumo": "Art. 337, § 5º: exceto **convenção de arbitragem** e **incompetência relativa**, o juiz conhece de ofício.",
      "excecoes": [
       "Convenção de arbitragem — não se conhece de ofício (art. 337, § 5º)",
       "Incompetência relativa — não se conhece de ofício (art. 337, § 5º)"
      ],
      "lei": [
       {
        "lei": "L13105",
        "art": "337",
        "par": "",
        "inc": "",
        "rotulo": "CPC, art. 337, § 5º",
        "texto": "Excetuadas a convenção de arbitragem e a incompetência relativa, o juiz conhecerá de ofício das matérias enumeradas neste artigo."
       }
      ],
      "palavras_chave": [
       "arbitragem",
       "incompetência relativa"
      ],
      "correcao": {
       "erro": "Inclui a convenção de arbitragem entre as matérias que o juiz conhece de ofício.",
       "certo": "Excetuadas a convenção de arbitragem e a incompetência relativa, o juiz conhecerá de ofício das matérias preliminares da contestação."
      },
      "aprofundamento": "A regra é que as preliminares de contestação, por dizerem respeito à regularidade do processo, sejam conhecidas de ofício. As duas exceções têm em comum o fato de protegerem **interesses disponíveis das partes**.\n\nA **convenção de arbitragem** é escolha das partes de levar o conflito a um árbitro. Se o réu, demandado no Judiciário, não alega a convenção, entende-se que renunciou ao juízo arbitral e aceitou a jurisdição estatal. A **incompetência relativa** também protege conveniência das partes e se prorroga se não alegada.\n\nA banca inclui a arbitragem entre as matérias de ofício. Lembre a dupla de exceções: arbitragem e incompetência relativa.",
      "memorize": "De ofício, todas as preliminares, menos convenção de arbitragem e incompetência relativa."
     }
    },
    {
     "id": "CPC-7-R1-08",
     "ponto": "DBA26-CPC-7",
     "tema": "Efeitos da revelia",
     "assertiva": "Na revelia, presumem-se verdadeiras as alegações de fato formuladas pelo autor, ainda que o litígio verse sobre direitos indisponíveis.",
     "gabarito": "E",
     "comentario": {
      "resumo": "Art. 345, II: a presunção **não se aplica** a direitos indisponíveis.",
      "excecoes": [
       "Pluralidade de réus e algum contestar (art. 345, I)",
       "Direitos indisponíveis (II)",
       "Falta de instrumento indispensável à prova do ato (III)",
       "Alegações inverossímeis ou contrárias à prova dos autos (IV)"
      ],
      "lei": [
       {
        "lei": "L13105",
        "art": "345",
        "par": "",
        "inc": "",
        "rotulo": "CPC, art. 345",
        "texto": "A revelia não produz o efeito mencionado no art. 344 se:"
       },
       {
        "lei": "L13105",
        "art": "345",
        "par": "",
        "inc": "",
        "rotulo": "CPC, art. 345, II",
        "texto": "II - o litígio versar sobre direitos indisponíveis;"
       }
      ],
      "palavras_chave": [
       "revelia",
       "direitos indisponíveis"
      ],
      "correcao": {
       "erro": "Aplica a presunção de veracidade da revelia mesmo quando o litígio versa sobre direitos indisponíveis.",
       "certo": "A revelia não produz a presunção de veracidade se o litígio versar sobre direitos indisponíveis, entre outras exceções legais."
      },
      "aprofundamento": "A revelia gera a presunção de veracidade dos fatos alegados pelo autor porque o réu, citado, preferiu não contestá-los. Mas essa presunção é **relativa** e tem limites: há casos em que a omissão do réu não pode, sozinha, levar à verdade dos fatos.\n\nUm deles é o dos **direitos indisponíveis**. Se o réu não pode renunciar ao direito nem confessar validamente sobre ele, não faz sentido que sua inércia produza efeito equivalente a uma confissão. Os outros casos são: pluralidade de réus com algum contestando, falta de instrumento indispensável à prova do ato e alegações inverossímeis ou contrariadas pela prova.\n\nA revelia ainda produz outro efeito: os prazos correm contra o revel sem patrono a partir da publicação. A assertiva ignora a exceção dos direitos indisponíveis.",
      "memorize": "Revelia não presume verdade em direito indisponível, litisconsorte que contesta, falta de documento essencial ou alegação inverossímil."
     }
    },
    {
     "id": "CPC-7-R1-09",
     "ponto": "DBA26-CPC-7",
     "tema": "Ônus da prova",
     "assertiva": "O ônus da prova incumbe ao autor, quanto ao fato constitutivo de seu direito, e ao réu, quanto à existência de fato impeditivo, modificativo ou extintivo do direito do autor.",
     "gabarito": "C",
     "comentario": {
      "resumo": "Art. 373, caput: distribuição **estática**; o § 1º permite a **dinâmica**.",
      "lei": [
       {
        "lei": "L13105",
        "art": "373",
        "par": "",
        "inc": "",
        "rotulo": "CPC, art. 373",
        "texto": "O ônus da prova incumbe:\nI - ao autor, quanto ao fato constitutivo de seu direito;\nII - ao réu, quanto à existência de fato impeditivo, modificativo ou extintivo do direito do autor."
       }
      ],
      "palavras_chave": [
       "ônus da prova",
       "fato constitutivo"
      ],
      "aprofundamento": "A regra do ônus da prova responde a uma pergunta prática: se o fato não ficar provado, quem perde? O sistema atribui a cada parte o ônus de provar os fatos que lhe favorecem. O autor prova o **fato constitutivo** (o que fez nascer seu direito); o réu prova o fato **impeditivo, modificativo ou extintivo** (o que impede, altera ou extingue esse direito).\n\nÉ a chamada distribuição **estática**, fixada pela lei de antemão. O próprio código permite, porém, a distribuição **dinâmica**: diante de peculiaridades da causa, de impossibilidade ou excessiva dificuldade de uma parte, ou de maior facilidade da outra, o juiz pode redistribuir o ônus por decisão fundamentada, dando à parte a oportunidade de se desincumbir.\n\nO ônus é também regra de julgamento: o juiz só recorre a ele quando, encerrada a instrução, persiste a dúvida.",
      "exemplo": "Rui cobra uma dívida e prova o contrato (fato constitutivo). O réu alega que pagou: cabe a ele provar o pagamento (fato extintivo).",
      "memorize": "Autor: fato constitutivo. Réu: impeditivo, modificativo ou extintivo. Juiz pode dinamizar."
     }
    },
    {
     "id": "CPC-7-R1-10",
     "ponto": "DBA26-CPC-7",
     "tema": "Limites objetivos da coisa julgada",
     "assertiva": "Fazem coisa julgada os motivos, ainda que importantes para determinar o alcance da parte dispositiva da sentença.",
     "gabarito": "E",
     "comentario": {
      "resumo": "Art. 504, I: **não** fazem coisa julgada os motivos, nem a verdade dos fatos (II).",
      "lei": [
       {
        "lei": "L13105",
        "art": "504",
        "par": "",
        "inc": "",
        "rotulo": "CPC, art. 504, I",
        "texto": "Não fazem coisa julgada:\nI - os motivos, ainda que importantes para determinar o alcance da parte dispositiva da sentença;"
       }
      ],
      "palavras_chave": [
       "coisa julgada",
       "motivos"
      ],
      "correcao": {
       "erro": "Afirma que os motivos importantes para o alcance do dispositivo fazem coisa julgada.",
       "certo": "Não fazem coisa julgada os motivos, ainda que importantes para determinar o alcance da parte dispositiva da sentença, nem a verdade dos fatos tomada como fundamento."
      },
      "aprofundamento": "A coisa julgada torna imutável o **dispositivo** da sentença, a parte em que o juiz efetivamente decide o pedido. Os motivos servem para explicar a decisão e ajudam a interpretá-la, mas não se tornam indiscutíveis em outros processos.\n\nA razão é delimitar com precisão o que ficou decidido. Se os fundamentos fizessem coisa julgada, um raciocínio usado de passagem num processo amarraria as partes em litígios futuros sobre outros pedidos, sem que tivesse sido objeto de debate específico. Pelo mesmo motivo, a verdade dos fatos estabelecida como fundamento também não faz coisa julgada.\n\nO código atual criou uma regra especial para a **questão prejudicial** decidida expressa e incidentalmente, que pode fazer coisa julgada se preenchidos requisitos próprios. A assertiva erra ao estender a coisa julgada aos motivos em geral.",
      "memorize": "Coisa julgada atinge o dispositivo; motivos e verdade dos fatos, não."
     }
    },
    {
     "id": "CPC-7-R1-11",
     "ponto": "DBA26-CPC-7",
     "tema": "Cumprimento — multa e honorários",
     "assertiva": "No cumprimento definitivo de sentença por quantia certa, não ocorrendo o pagamento voluntário em 15 dias, o débito será acrescido de multa de 10% e de honorários de advogado de 10%.",
     "gabarito": "C",
     "comentario": {
      "resumo": "**Art. 523**, caput e § 1º.",
      "lei": [
       {
        "lei": "L13105",
        "art": "523",
        "par": "",
        "inc": "",
        "rotulo": "CPC, art. 523, § 1º",
        "texto": "Não ocorrendo pagamento voluntário no prazo do caput , o débito será acrescido de multa de dez por cento e, também, de honorários de advogado de dez por cento."
       }
      ],
      "palavras_chave": [
       "cumprimento de sentença",
       "multa de 10%"
      ],
      "aprofundamento": "No cumprimento de sentença por quantia, o devedor já foi condenado com contraditório pleno. A lei lhe dá um prazo para pagar voluntariamente e, se ele não o faz, impõe consequências pesadas para estimular o pagamento e remunerar o trabalho adicional do advogado do credor.\n\nA **multa** tem caráter coercitivo e sancionatório; os **honorários** remuneram a nova fase. São acréscimos distintos, ambos de 10%, e incidem sobre o débito não pago. Se houver pagamento parcial, incidem apenas sobre o restante.\n\nA banca costuma alterar os percentuais, dizer que a multa depende de nova intimação pessoal ou confundir o prazo com o da execução de título extrajudicial, que é bem menor. No cumprimento de sentença são 15 dias para pagar.",
      "memorize": "Cumprimento por quantia: 15 dias para pagar; senão, multa de 10% + honorários de 10%."
     }
    },
    {
     "id": "CPC-7-R1-12",
     "ponto": "DBA26-CPC-7",
     "tema": "Impugnação ao cumprimento",
     "assertiva": "A impugnação ao cumprimento de sentença depende de prévia garantia do juízo por penhora.",
     "gabarito": "E",
     "comentario": {
      "resumo": "Art. 525: o executado apresenta impugnação em 15 dias **independentemente de penhora ou nova intimação**.",
      "lei": [
       {
        "lei": "L13105",
        "art": "525",
        "par": "",
        "inc": "",
        "rotulo": "CPC, art. 525",
        "texto": "Transcorrido o prazo previsto no art. 523 sem o pagamento voluntário, inicia-se o prazo de 15 (quinze) dias para que o executado, independentemente de penhora ou nova intimação, apresente, nos próprios autos, sua impugnação."
       }
      ],
      "palavras_chave": [
       "impugnação",
       "sem penhora"
      ],
      "correcao": {
       "erro": "Condiciona a apresentação da impugnação ao cumprimento de sentença à prévia garantia do juízo por penhora.",
       "certo": "Transcorrido o prazo de pagamento voluntário, inicia-se o prazo de 15 dias para o executado, independentemente de penhora ou nova intimação, apresentar impugnação nos próprios autos."
      },
      "aprofundamento": "No código revogado, a defesa do executado dependia, em regra, de **garantia do juízo**. O código atual rompeu com essa exigência: o executado não precisa ter bens penhorados para se defender, o que amplia o acesso à defesa e evita que o devedor sem patrimônio fique sem voz.\n\nO prazo de 15 dias para a impugnação começa automaticamente quando termina o prazo de pagamento voluntário, sem nova intimação. A impugnação é apresentada **nos próprios autos**, porque o cumprimento é fase do mesmo processo.\n\nA garantia continua relevante para outro efeito: para que a impugnação suspenda os atos executivos, o juiz exige garantia por penhora, caução ou depósito, além dos requisitos de relevância e risco. A banca mistura esses dois planos.",
      "memorize": "Impugnação: 15 dias após o prazo de pagamento, sem penhora e sem nova intimação."
     }
    },
    {
     "id": "CPC-8-R1-01",
     "ponto": "DBA26-CPC-8",
     "tema": "Requisitos do título",
     "assertiva": "A execução para cobrança de crédito fundar-se-á sempre em título de obrigação certa, líquida e exigível.",
     "gabarito": "C",
     "comentario": {
      "resumo": "Art. 783: **certeza, liquidez e exigibilidade**.",
      "lei": [
       {
        "lei": "L13105",
        "art": "783",
        "par": "",
        "inc": "",
        "rotulo": "CPC, art. 783",
        "texto": "A execução para cobrança de crédito fundar-se-á sempre em título de obrigação certa, líquida e exigível."
       }
      ],
      "palavras_chave": [
       "título executivo",
       "certa, líquida e exigível"
      ],
      "aprofundamento": "A execução é atividade invasiva: o Estado retira bens do devedor para satisfazer o credor. Por isso só pode se apoiar num título que demonstre, com segurança, a existência da obrigação e o que exatamente se deve.\n\nOs três atributos têm sentidos distintos. **Certeza** é a definição da existência e da natureza da obrigação. **Liquidez** é a determinação do seu objeto e valor, ainda que dependa de simples cálculo aritmético. **Exigibilidade** é a ausência de termo ou condição pendente: a obrigação já pode ser cobrada.\n\nSe faltar liquidez numa sentença, o caminho é a liquidação antes do cumprimento. A banca costuma trocar um atributo por outro ou dizer que um deles é dispensável. A palavra \"sempre\" do artigo é intencional.",
      "memorize": "Título executivo: obrigação certa, líquida e exigível. Sempre."
     }
    },
    {
     "id": "CPC-8-R1-02",
     "ponto": "DBA26-CPC-8",
     "tema": "Documento particular",
     "assertiva": "É título executivo extrajudicial o documento particular assinado pelo devedor e por 3 testemunhas.",
     "gabarito": "E",
     "comentario": {
      "resumo": "Art. 784, III: bastam **2 testemunhas**.",
      "lei": [
       {
        "lei": "L13105",
        "art": "784",
        "par": "",
        "inc": "",
        "rotulo": "CPC, art. 784, III",
        "texto": "III - o documento particular assinado pelo devedor e por 2 (duas) testemunhas;"
       }
      ],
      "palavras_chave": [
       "título extrajudicial",
       "2 testemunhas"
      ],
      "correcao": {
       "erro": "Exige 3 testemunhas no documento particular para que seja título executivo.",
       "certo": "É título executivo extrajudicial o documento particular assinado pelo devedor e por 2 testemunhas."
      },
      "aprofundamento": "O documento particular vira título executivo porque a assinatura do devedor, testemunhada, dá segurança suficiente sobre a existência da obrigação. As testemunhas reforçam a autenticidade do ato e reduzem o risco de fraude.\n\nO número exigido é de 2 testemunhas, e não 3. Sem as testemunhas, o documento continua valendo como prova da dívida, mas o credor terá de cobrá-la pela via de conhecimento ou monitória.\n\nA mesma lista de títulos extrajudiciais inclui a escritura pública, o documento público assinado pelo devedor e o instrumento de transação referendado por MP, Defensoria ou advogados. A banca costuma aumentar o número de testemunhas ou exigir reconhecimento de firma, que a lei não pede.",
      "memorize": "Documento particular: devedor + 2 testemunhas."
     }
    },
    {
     "id": "CPC-8-R1-03",
     "ponto": "DBA26-CPC-8",
     "tema": "Citação na execução por quantia",
     "assertiva": "Na execução por quantia certa, o executado será citado para pagar a dívida no prazo de 15 dias.",
     "gabarito": "E",
     "comentario": {
      "resumo": "Art. 829: **3 dias** contados da citação. 15 dias é o prazo do cumprimento de sentença (art. 523) e dos embargos (art. 915).",
      "lei": [
       {
        "lei": "L13105",
        "art": "829",
        "par": "",
        "inc": "",
        "rotulo": "CPC, art. 829",
        "texto": "O executado será citado para pagar a dívida no prazo de 3 (três) dias, contado da citação."
       }
      ],
      "pegadinha": "Troca entre 3 dias (execução) e 15 dias (cumprimento de sentença).",
      "palavras_chave": [
       "execução por quantia",
       "3 dias"
      ],
      "correcao": {
       "erro": "Fixa em 15 dias o prazo para o executado pagar na execução por quantia certa.",
       "certo": "Na execução por quantia certa, o executado é citado para pagar a dívida no prazo de 3 dias, contado da citação."
      },
      "aprofundamento": "Na execução de título extrajudicial, o prazo para pagar é curto porque o credor já tem um título com força executiva, e o processo nasce voltado à satisfação, não à discussão. O executado é citado para pagar em 3 dias; se não o fizer, o oficial procede à penhora.\n\nHá incentivo para o pagamento rápido: se o executado pagar integralmente nesse prazo, os honorários fixados de início são reduzidos pela metade. A defesa, por sua vez, vai por embargos, em prazo próprio e maior.\n\nA pegadinha é a confusão entre prazos. 15 dias é o prazo de pagamento voluntário no cumprimento de sentença (art. 523) e também o dos embargos (art. 915). Na execução por quantia de título extrajudicial, para pagar, são 3 dias.",
      "memorize": "Execução extrajudicial: 3 dias para pagar. Cumprimento de sentença e embargos: 15 dias."
     }
    },
    {
     "id": "CPC-8-R1-04",
     "ponto": "DBA26-CPC-8",
     "tema": "Penhora em dinheiro",
     "assertiva": "É prioritária a penhora em dinheiro, podendo o juiz, nas demais hipóteses, alterar a ordem preferencial de acordo com as circunstâncias do caso concreto.",
     "gabarito": "C",
     "comentario": {
      "resumo": "**Art. 835, § 1º**.",
      "lei": [
       {
        "lei": "L13105",
        "art": "835",
        "par": "",
        "inc": "",
        "rotulo": "CPC, art. 835, § 1º",
        "texto": "É prioritária a penhora em dinheiro, podendo o juiz, nas demais hipóteses, alterar a ordem prevista no caput de acordo com as circunstâncias do caso concreto."
       }
      ],
      "palavras_chave": [
       "penhora",
       "dinheiro"
      ],
      "aprofundamento": "A ordem de penhora existe para tornar a execução eficiente: começa pelos bens mais fáceis de converter em pagamento. O **dinheiro** está no topo e tem prioridade absoluta, porque dispensa avaliação, leilão e todas as etapas de expropriação.\n\nQuanto aos demais bens, a ordem é preferencial, não rígida. O juiz pode alterá-la conforme as circunstâncias, equilibrando a efetividade para o credor e a **menor onerosidade** para o devedor. Por exemplo, pode preferir um imóvel livre a um veículo de difícil venda.\n\nA banca costuma dizer que toda a ordem é absoluta, ou que o juiz pode deixar de penhorar dinheiro disponível para atender à conveniência do devedor. Guarde a estrutura: dinheiro é prioritário; o resto, flexível.",
      "memorize": "Dinheiro é prioritário; nos demais bens, o juiz pode alterar a ordem conforme o caso."
     }
    },
    {
     "id": "CPC-8-R1-05",
     "ponto": "DBA26-CPC-8",
     "tema": "Poupança",
     "assertiva": "É impenhorável a quantia depositada em caderneta de poupança até o limite de 60 salários mínimos.",
     "gabarito": "E",
     "comentario": {
      "resumo": "Art. 833, X: até **40 salários mínimos**.",
      "lei": [
       {
        "lei": "L13105",
        "art": "833",
        "par": "",
        "inc": "",
        "rotulo": "CPC, art. 833, X",
        "texto": "X - a quantia depositada em caderneta de poupança, até o limite de 40 (quarenta) salários-mínimos;"
       }
      ],
      "palavras_chave": [
       "impenhorabilidade",
       "40 salários mínimos"
      ],
      "correcao": {
       "erro": "Fixa em 60 salários mínimos o limite da impenhorabilidade da poupança.",
       "certo": "É impenhorável a quantia depositada em caderneta de poupança até o limite de 40 salários mínimos."
      },
      "aprofundamento": "A impenhorabilidade de certos bens protege o **mínimo existencial** do devedor. A execução busca satisfazer o credor, mas não pode reduzir o executado à miséria. A poupança de pequeno valor é tratada como reserva de segurança da família.\n\nO limite é de 40 salários mínimos. A proteção, porém, cede diante de dívidas de natureza alimentar, porque aí o próprio sustento do credor está em jogo.\n\nA banca costuma trocar o valor. Lembre que 40 é o número da poupança; outros valores costumam aparecer para confundir.",
      "memorize": "Poupança impenhorável até 40 salários mínimos."
     }
    },
    {
     "id": "CPC-8-R1-06",
     "ponto": "DBA26-CPC-8",
     "tema": "Embargos sem garantia",
     "assertiva": "O executado, independentemente de penhora, depósito ou caução, poderá se opor à execução por meio de embargos.",
     "gabarito": "C",
     "comentario": {
      "resumo": "**Art. 914.**",
      "lei": [
       {
        "lei": "L13105",
        "art": "914",
        "par": "",
        "inc": "",
        "rotulo": "CPC, art. 914",
        "texto": "O executado, independentemente de penhora, depósito ou caução, poderá se opor à execução por meio de embargos."
       }
      ],
      "palavras_chave": [
       "embargos à execução",
       "sem garantia"
      ],
      "aprofundamento": "No código revogado, a defesa do executado dependia de garantia prévia. O código atual eliminou essa exigência para os embargos à execução: qualquer executado pode se defender, tenha ou não bens. Exigir garantia excluiria justamente quem não tem patrimônio, e o direito de defesa não pode depender da riqueza.\n\nOs embargos são **ação autônoma** de conhecimento, distribuída por dependência à execução. Neles o executado pode alegar matérias amplas, porque o título extrajudicial não passou por contraditório judicial prévio.\n\nA garantia volta a ter peso quando se trata do efeito suspensivo: para que os embargos suspendam a execução, é preciso que ela esteja garantida. A banca mistura a admissibilidade com o efeito suspensivo.",
      "memorize": "Embargos sem garantia: cabem sempre. Garantia só importa para o efeito suspensivo."
     }
    },
    {
     "id": "CPC-8-R1-07",
     "ponto": "DBA26-CPC-8",
     "tema": "Prazo dos embargos",
     "assertiva": "Os embargos à execução serão oferecidos no prazo de 15 dias, contados da juntada aos autos do auto de penhora.",
     "gabarito": "E",
     "comentario": {
      "resumo": "Art. 915: 15 dias contados **na forma do art. 231** — isto é, a partir da **citação**, não da penhora.",
      "lei": [
       {
        "lei": "L13105",
        "art": "915",
        "par": "",
        "inc": "",
        "rotulo": "CPC, art. 915",
        "texto": "Os embargos serão oferecidos no prazo de 15 (quinze) dias, contado, conforme o caso, na forma do art. 231"
       }
      ],
      "palavras_chave": [
       "embargos",
       "termo inicial"
      ],
      "correcao": {
       "erro": "Conta o prazo dos embargos a partir da juntada do auto de penhora.",
       "certo": "Os embargos são oferecidos em 15 dias, contados na forma do art. 231, isto é, a partir da citação, independentemente de penhora."
      },
      "aprofundamento": "O prazo dos embargos começa a contar segundo as regras gerais de início de prazo: normalmente da juntada do mandado de citação cumprido, do aviso de recebimento ou do fim da dilação no edital. O marco é a **citação**, e não a penhora.\n\nEssa escolha é coerente com a dispensa de garantia: se os embargos não dependem de penhora, não faria sentido esperar a penhora para começar a contar o prazo. O executado já pode se defender logo após ser citado.\n\nHá regras próprias para litisconsortes: o prazo de cada executado corre de forma independente, salvo entre cônjuges ou companheiros. A assertiva reproduz o marco do código revogado.",
      "memorize": "Embargos: 15 dias contados da citação (forma do art. 231), não da penhora."
     }
    },
    {
     "id": "CPC-8-R1-08",
     "ponto": "DBA26-CPC-8",
     "tema": "Efeito suspensivo dos embargos",
     "assertiva": "Os embargos à execução não terão efeito suspensivo, mas o juiz poderá atribuí-lo quando verificados os requisitos da tutela provisória e desde que a execução já esteja garantida por penhora, depósito ou caução suficientes.",
     "gabarito": "C",
     "comentario": {
      "resumo": "**Art. 919**, caput e § 1º.",
      "lei": [
       {
        "lei": "L13105",
        "art": "919",
        "par": "",
        "inc": "",
        "rotulo": "CPC, art. 919, § 1º",
        "texto": "O juiz poderá, a requerimento do embargante, atribuir efeito suspensivo aos embargos quando verificados os requisitos para a concessão da tutela provisória e desde que a execução já esteja garantida por penhora, depósito ou caução suficientes."
       }
      ],
      "palavras_chave": [
       "efeito suspensivo",
       "garantia do juízo"
      ],
      "aprofundamento": "Os embargos não suspendem a execução automaticamente porque o credor tem título executivo, que goza de presunção de certeza. Se toda defesa paralisasse a cobrança, o devedor teria estímulo para embargar só para ganhar tempo.\n\nO efeito suspensivo é, então, **excepcional** e depende de três elementos: **requerimento** do embargante, presença dos **requisitos da tutela provisória** (probabilidade e perigo, ou evidência) e **garantia** suficiente da execução por penhora, depósito ou caução. Mesmo concedido, não impede a substituição, o reforço ou a redução da penhora e a avaliação dos bens.\n\nA banca costuma permitir a concessão de ofício, dispensar a garantia ou dizer que os embargos suspendem por regra. Os três requisitos são cumulativos.",
      "memorize": "Embargos não suspendem; o juiz pode suspender a pedido, com requisitos da tutela provisória + garantia."
     }
    },
    {
     "id": "CPC-8-R1-09",
     "ponto": "DBA26-CPC-8",
     "tema": "Parcelamento",
     "assertiva": "No prazo para embargos, reconhecendo o crédito e depositando 30% do valor em execução, acrescido de custas e honorários, o executado poderá requerer o pagamento do restante em até 6 parcelas mensais, com correção e juros de 1% ao mês.",
     "gabarito": "C",
     "comentario": {
      "resumo": "**Art. 916**, caput (moratória legal).",
      "lei": [
       {
        "lei": "L13105",
        "art": "916",
        "par": "",
        "inc": "",
        "rotulo": "CPC, art. 916",
        "texto": "No prazo para embargos, reconhecendo o crédito do exequente e comprovando o depósito de trinta por cento do valor em execução, acrescido de custas e de honorários de advogado, o executado poderá requerer que lhe seja permitido pagar o restante em até 6 (seis) parcelas mensais, acrescidas de correção monetária e de juros de um por cento ao mês."
       }
      ],
      "palavras_chave": [
       "parcelamento",
       "30%",
       "6 parcelas"
      ],
      "aprofundamento": "O parcelamento é uma **moratória legal**: o executado que reconhece a dívida ganha o direito de pagá-la em parcelas, desde que cumpra os requisitos. A vantagem para o credor é receber sem a demora e o desgaste dos embargos e da expropriação.\n\nOs requisitos são: pedido no prazo dos embargos, reconhecimento do crédito e depósito de 30% do valor, acrescido de custas e honorários. O restante é pago em até 6 parcelas mensais, com correção e juros de 1% ao mês. Ao pedir o parcelamento, o executado renuncia ao direito de embargar.\n\nSe deixar de pagar alguma parcela, as seguintes vencem antecipadamente, a execução retoma o curso e incide multa sobre as parcelas não pagas. O instituto é próprio da execução de título extrajudicial e não se aplica ao cumprimento de sentença.",
      "memorize": "Parcelamento: 30% + custas e honorários, saldo em até 6 parcelas, juros de 1% ao mês; renuncia aos embargos."
     }
    },
    {
     "id": "CPC-8-R1-10",
     "ponto": "DBA26-CPC-8",
     "tema": "Fraude à execução",
     "assertiva": "O reconhecimento da fraude à execução depende do registro da penhora do bem alienado ou da prova de má-fé do terceiro adquirente.",
     "gabarito": "C",
     "comentario": {
      "resumo": "**Súmula 375/STJ**, em linha com o art. 792 (averbação da pendência do processo, da penhora ou hipoteca judiciária).",
      "lei": [
       {
        "lei": "L13105",
        "art": "792",
        "par": "",
        "inc": "",
        "rotulo": "CPC, art. 792",
        "texto": "A alienação ou a oneração de bem é considerada fraude à execução:"
       }
      ],
      "juris": [
       {
        "tribunal": "STJ",
        "fonte": "Súmula 375/STJ",
        "data": "18/03/2009",
        "texto": "O reconhecimento da fraude à execução depende do registro da penhora do bem alienado ou da prova de má-fé do terceiro adquirente."
       }
      ],
      "palavras_chave": [
       "fraude à execução",
       "má-fé",
       "registro da penhora"
      ],
      "aprofundamento": "A fraude à execução protege o credor contra o devedor que se desfaz dos bens para não pagar. Mas há outro interesse em jogo: o do **terceiro adquirente** de boa-fé, que comprou o bem sem saber da dívida. A Súmula 375/STJ equilibra os dois.\n\nO terceiro só é prejudicado se havia **registro da penhora**, o que dá publicidade ao gravame e afasta a alegação de desconhecimento, ou se ficar provada a sua **má-fé**. Sem uma coisa nem outra, prevalece a segurança do negócio. O código prestigia a mesma lógica ao tratar da averbação da pendência do processo, da penhora ou da hipoteca judiciária.\n\nReconhecida a fraude, a alienação é **ineficaz** perante o exequente: o bem continua sujeito à execução, sem que o negócio seja anulado entre as partes. Não confunda com a fraude contra credores, que exige ação própria.",
      "memorize": "Fraude à execução: registro da penhora ou prova da má-fé do adquirente (Súmula 375/STJ)."
     }
    },
    {
     "id": "CPC-8-R1-11",
     "ponto": "DBA26-CPC-8",
     "tema": "Suspensão por falta de bens",
     "assertiva": "Não localizados bens penhoráveis, a execução será suspensa pelo prazo de 2 anos, durante o qual se suspende a prescrição.",
     "gabarito": "E",
     "comentario": {
      "resumo": "Art. 921, § 1º: suspensão por **1 ano**; depois, arquivamento e curso da **prescrição intercorrente**.",
      "lei": [
       {
        "lei": "L13105",
        "art": "921",
        "par": "",
        "inc": "",
        "rotulo": "CPC, art. 921, § 1º",
        "texto": "Na hipótese do inciso III, o juiz suspenderá a execução pelo prazo de 1 (um) ano, durante o qual se suspenderá a prescrição."
       }
      ],
      "palavras_chave": [
       "prescrição intercorrente",
       "1 ano"
      ],
      "correcao": {
       "erro": "Fixa em 2 anos o prazo de suspensão da execução por falta de bens.",
       "certo": "Não localizados bens penhoráveis, o juiz suspende a execução por 1 ano, durante o qual se suspende a prescrição; depois, arquiva os autos e começa a correr a prescrição intercorrente."
      },
      "aprofundamento": "Quando não se encontram bens penhoráveis, a execução não pode ficar parada indefinidamente, nem pode ser extinta de imediato, porque o devedor pode adquirir bens depois. A lei cria uma solução em etapas.\n\nPrimeiro, o juiz suspende a execução por 1 ano, durante o qual a **prescrição fica suspensa**. Esgotado esse prazo sem localização de bens, os autos são arquivados e começa a correr a **prescrição intercorrente**. Se o prazo prescricional se completar, o juiz, ouvidas as partes, reconhece a prescrição e extingue a execução. Encontrados bens a qualquer tempo, os autos são desarquivados.\n\nA assertiva troca o período de suspensão. São 2 anos no enunciado; a lei fala em 1 ano.",
      "memorize": "Sem bens: suspensão por 1 ano (prescrição suspensa); depois arquivamento e prescrição intercorrente."
     }
    },
    {
     "id": "CPC-8-R1-12",
     "ponto": "DBA26-CPC-8",
     "tema": "Prisão civil do devedor de alimentos",
     "assertiva": "O cumprimento da pena de prisão civil exime o devedor de alimentos do pagamento das prestações vencidas e vincendas.",
     "gabarito": "E",
     "comentario": {
      "resumo": "Art. 528, § 5º: **não exime**. A prisão é de **1 a 3 meses**, em regime fechado, separado dos presos comuns (§§ 3º e 4º).",
      "lei": [
       {
        "lei": "L13105",
        "art": "528",
        "par": "",
        "inc": "",
        "rotulo": "CPC, art. 528, § 5º",
        "texto": "O cumprimento da pena não exime o executado do pagamento das prestações vencidas e vincendas."
       }
      ],
      "palavras_chave": [
       "prisão civil",
       "alimentos"
      ],
      "correcao": {
       "erro": "Afirma que o cumprimento da prisão civil exime o devedor das prestações vencidas e vincendas.",
       "certo": "O cumprimento da prisão civil não exime o executado do pagamento das prestações vencidas e vincendas."
      },
      "aprofundamento": "A prisão civil do devedor de alimentos é **meio de coerção**, e não pena. Seu objetivo é pressionar o devedor a pagar, diante da urgência de quem depende dos alimentos para sobreviver. Por isso cumprir o período de prisão não quita nada: a dívida permanece integralmente.\n\nA prisão dura de 1 a 3 meses, em regime fechado, com o preso separado dos presos comuns. Se o devedor pagar, a prisão é imediatamente suspensa. A própria lei limita esse rito às prestações mais recentes; o débito antigo segue pelo rito da penhora.\n\nA assertiva trata a prisão como se fosse pena que extingue a obrigação. Raciocine pela finalidade: se a prisão quitasse a dívida, o devedor escolheria ser preso em vez de pagar.",
      "memorize": "Prisão civil coage, não quita: 1 a 3 meses, regime fechado, dívida continua."
     }
    },
    {
     "id": "CPC-9-R1-01",
     "ponto": "DBA26-CPC-9",
     "tema": "Rol de recursos",
     "assertiva": "São cabíveis no CPC os embargos infringentes contra acórdão não unânime que reformar sentença de mérito.",
     "gabarito": "E",
     "comentario": {
      "resumo": "O art. 994 **não prevê embargos infringentes**. No lugar deles entrou a **técnica de ampliação do colegiado** (art. 942), que não é recurso.",
      "lei": [
       {
        "lei": "L13105",
        "art": "994",
        "par": "",
        "inc": "",
        "rotulo": "CPC, art. 994",
        "texto": "São cabíveis os seguintes recursos:\nI - apelação;\nII - agravo de instrumento;\nIII - agravo interno;\nIV - embargos de declaração;\nV - recurso ordinário;\nVI - recurso especial;\nVII - recurso extraordinário;\nVIII - agravo em recurso especial ou extraordinário;\nIX - embargos de divergência."
       }
      ],
      "palavras_chave": [
       "rol taxativo",
       "embargos infringentes",
       "art. 942"
      ],
      "correcao": {
       "erro": "Inclui os embargos infringentes entre os recursos cabíveis no CPC.",
       "certo": "O CPC não prevê embargos infringentes; em seu lugar, aplica-se a técnica de ampliação do colegiado do art. 942, que não é recurso."
      },
      "aprofundamento": "Os embargos infringentes eram um recurso contra acórdão não unânime. Foram criticados por prolongar os processos, e o código atual os extinguiu. O rol de recursos é **taxativo**: só existe recurso previsto em lei.\n\nEm seu lugar, o código criou a **técnica de ampliação do colegiado** (art. 942). Quando o julgamento não é unânime, novos julgadores são convocados para prosseguir o julgamento na mesma sessão ou em outra, sem necessidade de provocação da parte. Não é recurso: é uma etapa do próprio julgamento, que ocorre de ofício.\n\nA banca costuma manter os infringentes no rol ou tratar a técnica do art. 942 como recurso que depende de interposição. Fixe a lista dos recursos e lembre que infringentes não estão nela.",
      "memorize": "Embargos infringentes não existem mais; agora há ampliação do colegiado (não é recurso)."
     }
    },
    {
     "id": "CPC-9-R1-02",
     "ponto": "DBA26-CPC-9",
     "tema": "Prazo recursal",
     "assertiva": "Excetuados os embargos de declaração, o prazo para interpor os recursos e para responder-lhes é de 15 dias.",
     "gabarito": "C",
     "comentario": {
      "resumo": "Art. 1.003, § 5º. Embargos de declaração: **5 dias** (art. 1.023).",
      "lei": [
       {
        "lei": "L13105",
        "art": "1003",
        "par": "",
        "inc": "",
        "rotulo": "CPC, art. 1.003, § 5º",
        "texto": "Excetuados os embargos de declaração, o prazo para interpor os recursos e para responder-lhes é de 15 (quinze) dias."
       }
      ],
      "palavras_chave": [
       "prazo recursal",
       "15 dias"
      ],
      "aprofundamento": "O código atual **uniformizou os prazos recursais** em 15 dias, para simplificar a vida do advogado e reduzir erros de contagem. A mesma regra vale para responder ao recurso (contrarrazões).\n\nA única exceção no código são os **embargos de declaração**, com prazo de 5 dias. A razão é que eles não buscam rediscutir a causa, apenas esclarecer, completar ou corrigir a decisão, e por isso exigem menos tempo de preparação.\n\nOs prazos são contados em dias úteis e podem ser dobrados para a Fazenda Pública, o MP, a Defensoria e os litisconsortes com procuradores diferentes em autos físicos. A banca costuma atribuir prazos distintos a recursos específicos, como um prazo menor para o agravo, que era regra do código anterior.",
      "memorize": "Todos os recursos: 15 dias. Exceção: embargos de declaração, 5 dias."
     }
    },
    {
     "id": "CPC-9-R1-03",
     "ponto": "DBA26-CPC-9",
     "tema": "Interlocutórias não agraváveis",
     "assertiva": "As questões resolvidas na fase de conhecimento cuja decisão não comporte agravo de instrumento não são cobertas pela preclusão e devem ser suscitadas em preliminar de apelação ou nas contrarrazões.",
     "gabarito": "C",
     "comentario": {
      "resumo": "Art. 1.009, § 1º: **preclusão diferida**.",
      "lei": [
       {
        "lei": "L13105",
        "art": "1009",
        "par": "",
        "inc": "",
        "rotulo": "CPC, art. 1.009, § 1º",
        "texto": "As questões resolvidas na fase de conhecimento, se a decisão a seu respeito não comportar agravo de instrumento, não são cobertas pela preclusão e devem ser suscitadas em preliminar de apelação, eventualmente interposta contra a decisão final, ou nas contrarrazões."
       }
      ],
      "palavras_chave": [
       "preclusão",
       "preliminar de apelação"
      ],
      "aprofundamento": "O código atual restringiu o agravo de instrumento a hipóteses previstas em lei. Mas restringir o recurso não poderia significar deixar as demais decisões imunes ao controle. A solução foi a **preclusão diferida**: as interlocutórias não agraváveis não precluem de imediato e podem ser impugnadas depois, na apelação.\n\nO vencido as suscita em **preliminar de apelação**; o vencedor, que não tem interesse em apelar, pode fazê-lo nas **contrarrazões**. Nesse segundo caso, o apelante é intimado para se manifestar sobre essas questões.\n\nA lógica é concentrar a impugnação num único momento, sem multiplicar recursos durante o processo. A banca costuma dizer que essas decisões precluem se não forem impugnadas por protesto ou que seriam irrecorríveis.",
      "memorize": "Interlocutória não agravável não preclui: vai em preliminar de apelação ou contrarrazões."
     }
    },
    {
     "id": "CPC-9-R1-04",
     "ponto": "DBA26-CPC-9",
     "tema": "Efeito suspensivo da apelação",
     "assertiva": "A apelação contra sentença que condena a pagar alimentos é recebida, em regra, com efeito suspensivo.",
     "gabarito": "E",
     "comentario": {
      "resumo": "Regra: a apelação tem efeito suspensivo (art. 1.012). Mas a sentença que **condena a pagar alimentos** produz efeitos **imediatamente** (§ 1º, II).",
      "excecoes": [
       "Homologa divisão ou demarcação (I)",
       "Condena a pagar alimentos (II)",
       "Extingue sem mérito ou julga improcedentes os embargos do executado (III)",
       "Julga procedente a instituição de arbitragem (IV)",
       "Confirma, concede ou revoga tutela provisória (V)",
       "Decreta a interdição (VI)"
      ],
      "lei": [
       {
        "lei": "L13105",
        "art": "1012",
        "par": "",
        "inc": "",
        "rotulo": "CPC, art. 1.012",
        "texto": "A apelação terá efeito suspensivo."
       },
       {
        "lei": "L13105",
        "art": "1012",
        "par": "",
        "inc": "",
        "rotulo": "CPC, art. 1.012, § 1º, II",
        "texto": "II - condena a pagar alimentos;"
       }
      ],
      "palavras_chave": [
       "efeito suspensivo",
       "alimentos"
      ],
      "correcao": {
       "erro": "Aplica o efeito suspensivo, em regra, à apelação contra sentença que condena a pagar alimentos.",
       "certo": "A apelação tem efeito suspensivo como regra, mas a sentença que condena a pagar alimentos começa a produzir efeitos imediatamente após a publicação."
      },
      "aprofundamento": "A apelação tem, como regra, **efeito suspensivo**: a sentença não produz efeitos enquanto o tribunal não julgar o recurso. A lei, porém, abre exceções quando esperar o julgamento causaria prejuízo grave ou quando a sentença apenas confirma situação já existente.\n\nA sentença que condena a pagar **alimentos** é o exemplo mais lembrado. Quem precisa de alimentos precisa deles agora; suspender a sentença enquanto o recurso tramita frustraria a própria tutela. Por isso ela produz efeitos imediatamente após a publicação, e o credor pode promover o cumprimento provisório.\n\nO apelante pode pedir ao tribunal a concessão de efeito suspensivo nessas hipóteses, demonstrando probabilidade de provimento ou risco de dano grave. A assertiva aplica a regra geral a uma exceção expressa.",
      "memorize": "Apelação suspende, salvo exceções: alimentos, tutela provisória, interdição, entre outras."
     }
    },
    {
     "id": "CPC-9-R1-05",
     "ponto": "DBA26-CPC-9",
     "tema": "Taxatividade mitigada",
     "assertiva": "Para o STJ, o rol do art. 1.015 do CPC é de taxatividade mitigada, admitindo agravo de instrumento quando verificada urgência decorrente da inutilidade do julgamento da questão no recurso de apelação.",
     "gabarito": "C",
     "comentario": {
      "resumo": "**Tema 988**/STJ.",
      "lei": [
       {
        "lei": "L13105",
        "art": "1015",
        "par": "",
        "inc": "",
        "rotulo": "CPC, art. 1.015",
        "texto": "Cabe agravo de instrumento contra as decisões interlocutórias que versarem sobre:"
       }
      ],
      "juris": [
       {
        "tribunal": "STJ",
        "fonte": "Tema 988/STJ — REsp 1.704.520/MT e REsp 1.696.396/MT",
        "data": "05/12/2018",
        "texto": "O rol do art. 1.015 do CPC é de taxatividade mitigada: admite agravo de instrumento quando verificada urgência decorrente da inutilidade do julgamento da questão na apelação."
       }
      ],
      "palavras_chave": [
       "agravo de instrumento",
       "taxatividade mitigada",
       "Tema 988"
      ],
      "aprofundamento": "O rol do agravo de instrumento foi pensado para ser **taxativo**, evitando a enxurrada de agravos. Mas surgiram situações em que esperar a apelação tornaria inútil a impugnação, como decisões sobre competência ou segredo de justiça. O STJ, no **Tema 988**, criou um meio-termo: a **taxatividade mitigada**.\n\nO rol continua sendo a regra, mas admite-se agravo fora dele quando houver **urgência** decorrente da inutilidade do julgamento da questão só na apelação. Não se trata de interpretação extensiva livre, mas de uma válvula de escape para casos em que a demora esvaziaria o direito.\n\nA banca costuma dizer que o rol é absolutamente taxativo, ou que é exemplificativo. As duas estão erradas segundo o STJ.",
      "memorize": "Rol do agravo: taxatividade mitigada (Tema 988/STJ) se a espera pela apelação tornar a questão inútil."
     }
    },
    {
     "id": "CPC-9-R1-06",
     "ponto": "DBA26-CPC-9",
     "tema": "Admissibilidade da apelação",
     "assertiva": "Interposta a apelação, o juiz de primeiro grau exerce o juízo de admissibilidade antes de remeter os autos ao tribunal.",
     "gabarito": "E",
     "comentario": {
      "resumo": "Art. 1.010, § 3º: os autos sobem **independentemente de juízo de admissibilidade**. Se o juiz trancar a apelação, cabe **reclamação** (Tema 1.267/STJ).",
      "lei": [
       {
        "lei": "L13105",
        "art": "1010",
        "par": "",
        "inc": "",
        "rotulo": "CPC, art. 1.010, § 3º",
        "texto": "Após as formalidades previstas nos §§ 1º e 2º, os autos serão remetidos ao tribunal pelo juiz, independentemente de juízo de admissibilidade."
       }
      ],
      "juris": [
       {
        "tribunal": "STJ",
        "fonte": "Tema 1.267/STJ — REsp 2.072.867/MA e outros",
        "data": "19/03/2025",
        "texto": "O juiz de 1º grau que obsta o processamento da apelação viola o art. 1.010, § 3º, e usurpa a competência do tribunal: cabe reclamação (art. 988, I); em execução ou cumprimento de sentença, cabe também agravo de instrumento."
       }
      ],
      "palavras_chave": [
       "juízo de admissibilidade",
       "reclamação",
       "Tema 1.267"
      ],
      "correcao": {
       "erro": "Atribui ao juiz de primeiro grau o juízo de admissibilidade da apelação.",
       "certo": "Interposta a apelação, os autos são remetidos ao tribunal independentemente de juízo de admissibilidade; se o juiz obstar o processamento, cabe reclamação (Tema 1.267/STJ)."
      },
      "aprofundamento": "No código revogado, o juiz de primeiro grau fazia um primeiro exame da apelação e podia negar seu seguimento. Isso gerava um recurso a mais, contra a decisão que trancava a apelação, e atrasava o processo. O código atual concentrou o juízo de admissibilidade no **tribunal**.\n\nO juiz de origem apenas intima o apelado para contrarrazões, cumpre as formalidades e remete os autos, **independentemente de juízo de admissibilidade**. Ele não avalia tempestividade, preparo ou cabimento.\n\nSe o juiz, mesmo assim, obstar a apelação, usurpa a competência do tribunal. O STJ, no Tema 1.267, fixou que cabe **reclamação** nesse caso, e, em execução ou cumprimento de sentença, também agravo de instrumento. A assertiva reproduz o sistema revogado.",
      "memorize": "Apelação: juiz de 1º grau não faz admissibilidade; se trancar, cabe reclamação."
     }
    },
    {
     "id": "CPC-9-R1-07",
     "ponto": "DBA26-CPC-9",
     "tema": "Embargos de declaração — cabimento e prazo",
     "assertiva": "Cabem embargos de declaração contra qualquer decisão judicial, no prazo de 5 dias, para esclarecer obscuridade, eliminar contradição, suprir omissão ou corrigir erro material.",
     "gabarito": "C",
     "comentario": {
      "resumo": "**Arts. 1.022** e 1.023.",
      "lei": [
       {
        "lei": "L13105",
        "art": "1022",
        "par": "",
        "inc": "",
        "rotulo": "CPC, art. 1.022",
        "texto": "Cabem embargos de declaração contra qualquer decisão judicial para:"
       },
       {
        "lei": "L13105",
        "art": "1023",
        "par": "",
        "inc": "",
        "rotulo": "CPC, art. 1.023",
        "texto": "Os embargos serão opostos, no prazo de 5 (cinco) dias"
       }
      ],
      "palavras_chave": [
       "embargos de declaração",
       "5 dias"
      ],
      "aprofundamento": "Os embargos de declaração têm finalidade **integrativa**: não buscam reformar a decisão por injustiça, mas aperfeiçoá-la. Servem para esclarecer o que está obscuro, eliminar contradição interna, suprir omissão sobre ponto que o juiz deveria ter enfrentado e corrigir erro material.\n\nCabem contra **qualquer decisão judicial**, inclusive despachos com conteúdo decisório, interlocutórias, sentenças e acórdãos, porque toda decisão deve ser clara e completa. O prazo de 5 dias é a única exceção à regra geral, mais longa, dos demais recursos.\n\nEles podem ter efeito modificativo quando o acolhimento implicar alteração da decisão, e nesse caso a parte contrária deve ser ouvida. A banca costuma restringir o cabimento a sentenças e acórdãos ou omitir o erro material das hipóteses.",
      "memorize": "Embargos de declaração: qualquer decisão, 5 dias, obscuridade, contradição, omissão ou erro material."
     }
    },
    {
     "id": "CPC-9-R1-08",
     "ponto": "DBA26-CPC-9",
     "tema": "Embargos de declaração — efeitos",
     "assertiva": "Os embargos de declaração não possuem efeito suspensivo e suspendem o prazo para a interposição de recurso.",
     "gabarito": "E",
     "comentario": {
      "resumo": "Art. 1.026: não têm efeito suspensivo (certo), mas **interrompem** — não suspendem — o prazo: ele volta a correr do zero.",
      "lei": [
       {
        "lei": "L13105",
        "art": "1026",
        "par": "",
        "inc": "",
        "rotulo": "CPC, art. 1.026",
        "texto": "Os embargos de declaração não possuem efeito suspensivo e interrompem o prazo para a interposição de recurso."
       }
      ],
      "pegadinha": "Interromper (o prazo recomeça inteiro) x suspender (retoma o que sobrou).",
      "palavras_chave": [
       "interrupção",
       "efeito suspensivo"
      ],
      "correcao": {
       "erro": "Diz que os embargos de declaração suspendem o prazo para a interposição de recurso.",
       "certo": "Os embargos de declaração não possuem efeito suspensivo e interrompem o prazo para a interposição de recurso."
      },
      "aprofundamento": "A diferença entre **interromper** e **suspender** é decisiva. Na suspensão, o prazo para e depois retoma pelo saldo que faltava. Na interrupção, ele é zerado e recomeça por inteiro.\n\nOs embargos de declaração **interrompem** o prazo para os demais recursos, para ambas as partes, porque a decisão pode mudar ao ser integrada, e não seria razoável que a parte recorresse de algo que ainda pode ser alterado. Ao mesmo tempo, eles **não têm efeito suspensivo**: a decisão embargada continua produzindo efeitos, salvo se o juiz ou relator suspender sua eficácia.\n\nA assertiva acerta a primeira parte e erra a segunda. Muitas vezes a banca monta frases assim, metade certa e metade errada, e a palavra trocada é \"suspendem\".",
      "memorize": "Embargos de declaração INTERROMPEM o prazo (recomeça inteiro) e não têm efeito suspensivo."
     }
    },
    {
     "id": "CPC-9-R1-09",
     "ponto": "DBA26-CPC-9",
     "tema": "Prazo da rescisória",
     "assertiva": "O direito à rescisão se extingue em 2 anos contados do trânsito em julgado da última decisão proferida no processo.",
     "gabarito": "C",
     "comentario": {
      "resumo": "**Art. 975**, caput.",
      "lei": [
       {
        "lei": "L13105",
        "art": "975",
        "par": "",
        "inc": "",
        "rotulo": "CPC, art. 975",
        "texto": "O direito à rescisão se extingue em 2 (dois) anos contados do trânsito em julgado da última decisão proferida no processo."
       }
      ],
      "palavras_chave": [
       "ação rescisória",
       "2 anos"
      ],
      "aprofundamento": "A ação rescisória permite desfazer a coisa julgada em hipóteses graves. Como ela ataca a estabilidade das decisões, a lei impõe um prazo **decadencial** curto, para que a segurança jurídica não fique em risco permanente.\n\nO marco inicial é o trânsito em julgado da **última decisão** proferida no processo, ainda que ela não tenha examinado o mérito, como um recurso não conhecido. Isso evita que a parte tenha de propor várias rescisórias enquanto o processo ainda tramita nos tribunais.\n\nHá marcos especiais em casos específicos, como na rescisória fundada em prova nova ou em simulação ou colusão, mas a regra geral é a do caput. A banca costuma alterar o prazo ou contar da primeira decisão de mérito transitada.",
      "memorize": "Rescisória: 2 anos do trânsito em julgado da ÚLTIMA decisão do processo."
     }
    },
    {
     "id": "CPC-9-R1-10",
     "ponto": "DBA26-CPC-9",
     "tema": "Hipóteses da rescisória",
     "assertiva": "Cabe ação rescisória contra decisão de mérito transitada em julgado proferida por juiz suspeito.",
     "gabarito": "E",
     "comentario": {
      "resumo": "Art. 966, II: juiz **impedido** ou juízo **absolutamente incompetente**. Suspeição e incompetência relativa não rendem rescisória.",
      "lei": [
       {
        "lei": "L13105",
        "art": "966",
        "par": "",
        "inc": "",
        "rotulo": "CPC, art. 966, II",
        "texto": "II - for proferida por juiz impedido ou por juízo absolutamente incompetente;"
       }
      ],
      "pegadinha": "\"Impedido\" trocado por \"suspeito\".",
      "palavras_chave": [
       "rescisória",
       "impedimento",
       "suspeição"
      ],
      "correcao": {
       "erro": "Admite ação rescisória contra decisão proferida por juiz suspeito.",
       "certo": "Cabe ação rescisória contra decisão de mérito transitada em julgado proferida por juiz impedido ou por juízo absolutamente incompetente; a suspeição não autoriza a rescisória."
      },
      "aprofundamento": "A rescisória só cabe em hipóteses **taxativas** e graves, porque desfaz a coisa julgada. Entre elas está a decisão proferida por juiz **impedido** ou por juízo **absolutamente incompetente**. Nesses casos, o vício é objetivo e atinge a própria validade da atuação jurisdicional.\n\nA **suspeição** e a incompetência relativa ficaram de fora. A suspeição envolve vínculos subjetivos e deve ser arguida no curso do processo; se a parte não a alegou a tempo, a questão se estabiliza. A incompetência relativa se prorroga quando não alegada.\n\nÉ a mesma lógica que distingue impedimento e suspeição: o impedimento é tão grave que sobrevive ao trânsito em julgado; a suspeição, não. A banca troca \"impedido\" por \"suspeito\".",
      "memorize": "Rescisória: juiz IMPEDIDO ou juízo absolutamente incompetente. Suspeição não."
     }
    },
    {
     "id": "CPC-9-R1-11",
     "ponto": "DBA26-CPC-9",
     "tema": "IRDR — cabimento",
     "assertiva": "É cabível o incidente de resolução de demandas repetitivas quando houver, simultaneamente, efetiva repetição de processos que contenham controvérsia sobre a mesma questão unicamente de direito e risco de ofensa à isonomia e à segurança jurídica.",
     "gabarito": "C",
     "comentario": {
      "resumo": "Art. 976: dois requisitos **cumulativos**. Não cabe IRDR preventivo nem sobre questão de fato.",
      "lei": [
       {
        "lei": "L13105",
        "art": "976",
        "par": "",
        "inc": "",
        "rotulo": "CPC, art. 976",
        "texto": "É cabível a instauração do incidente de resolução de demandas repetitivas quando houver, simultaneamente:\nI - efetiva repetição de processos que contenham controvérsia sobre a mesma questão unicamente de direito;\nII - risco de ofensa à isonomia e à segurança jurídica."
       }
      ],
      "palavras_chave": [
       "IRDR",
       "questão de direito"
      ],
      "aprofundamento": "O IRDR é uma técnica para julgar de uma só vez uma questão jurídica que se repete em muitos processos. O tribunal fixa uma tese que vincula todos os casos, presentes e futuros, na sua área de jurisdição, garantindo **isonomia** e **segurança jurídica**.\n\nOs dois requisitos são **cumulativos**: deve haver efetiva repetição de processos (não basta a mera possibilidade, por isso não há IRDR preventivo) e risco de ofensa à isonomia e à segurança. A controvérsia deve ser **unicamente de direito**; questões de fato variam de caso para caso e não se prestam a uma tese única.\n\nO incidente não cabe se um tribunal superior já tiver afetado recurso repetitivo sobre a mesma questão. A banca costuma tornar os requisitos alternativos ou admitir IRDR sobre questão de fato.",
      "memorize": "IRDR: repetição efetiva + risco à isonomia/segurança, cumulativos, questão só de direito."
     }
    },
    {
     "id": "CPC-9-R1-12",
     "ponto": "DBA26-CPC-9",
     "tema": "Reclamação após o trânsito",
     "assertiva": "É admissível a reclamação proposta após o trânsito em julgado da decisão reclamada, desde que dentro de 2 anos.",
     "gabarito": "E",
     "comentario": {
      "resumo": "Art. 988, § 5º, I e Súmula 734/STF: a reclamação proposta após o trânsito em julgado é **liminarmente indeferida** (redação da Lei 15.484/2026; antes, \"inadmissível\").",
      "lei": [
       {
        "lei": "L13105",
        "art": "988",
        "par": "",
        "inc": "",
        "rotulo": "CPC, art. 988, § 5º (Lei 15.484/2026)",
        "texto": "Será liminarmente indeferida a reclamação:"
       },
       {
        "lei": "L13105",
        "art": "988",
        "par": "",
        "inc": "",
        "rotulo": "CPC, art. 988, § 5º, I",
        "texto": "I – proposta após o trânsito em julgado da decisão reclamada;"
       }
      ],
      "juris": [
       {
        "tribunal": "STF",
        "fonte": "Súmula 734/STF",
        "data": "26/11/2003",
        "texto": "Não cabe reclamação quando já houver transitado em julgado o ato judicial que se alega ter desrespeitado decisão do STF."
       }
      ],
      "palavras_chave": [
       "reclamação",
       "trânsito em julgado"
      ],
      "correcao": {
       "erro": "Admite a reclamação após o trânsito em julgado, desde que proposta em 2 anos.",
       "certo": "A reclamação proposta após o trânsito em julgado da decisão reclamada é liminarmente indeferida (Lei 15.484/2026 e Súmula 734/STF)."
      },
      "aprofundamento": "A reclamação serve para preservar a competência dos tribunais e garantir a autoridade de suas decisões e precedentes. Mas ela não é sucedâneo de ação rescisória. Se a decisão reclamada já transitou em julgado, admitir a reclamação seria permitir desfazer a coisa julgada por um caminho sem prazo e sem os requisitos da rescisória.\n\nPor isso o código, na redação da Lei 15.484/2026, determina que a reclamação proposta após o trânsito em julgado seja **liminarmente indeferida**. A Súmula 734/STF já firmava essa orientação.\n\nA assertiva cria um prazo de 2 anos que mistura a reclamação com a rescisória. Na reclamação, o limite é o trânsito em julgado da decisão reclamada; depois dele, o caminho é outro.",
      "memorize": "Transitou em julgado? Reclamação não cabe (indeferimento liminar)."
     }
    },
    {
     "id": "CPC-10-R1-01",
     "ponto": "DBA26-CPC-10",
     "tema": "ACP — objeto vedado",
     "assertiva": "É cabível ação civil pública para veicular pretensões que envolvam tributos, desde que os contribuintes sejam indeterminados.",
     "gabarito": "E",
     "comentario": {
      "resumo": "Art. 1º, par. ún., da LACP: **não cabe** ACP sobre tributos, contribuições previdenciárias, FGTS ou fundos institucionais de beneficiários individualizáveis.",
      "lei": [
       {
        "lei": "L7347",
        "art": "1",
        "par": "",
        "inc": "",
        "rotulo": "Lei 7.347/1985, art. 1º, par. ún.",
        "texto": "Não será cabível ação civil pública para veicular pretensões que envolvam tributos, contribuições previdenciárias, o Fundo de Garantia do Tempo de Serviço - FGTS ou outros fundos de natureza institucional cujos beneficiários podem ser individualmente determinados."
       }
      ],
      "palavras_chave": [
       "ACP",
       "tributos",
       "FGTS"
      ],
      "correcao": {
       "erro": "Admite a ação civil pública sobre tributos quando os contribuintes forem indeterminados.",
       "certo": "Não é cabível ação civil pública para veicular pretensões que envolvam tributos, contribuições previdenciárias, FGTS ou outros fundos institucionais de beneficiários individualmente determináveis."
      },
      "aprofundamento": "A ação civil pública é instrumento de tutela de direitos difusos, coletivos e individuais homogêneos. A vedação em matéria tributária tem uma razão central: nas relações de tributo, contribuição previdenciária e FGTS, os beneficiários são **individualmente determináveis**, e cada contribuinte tem uma relação jurídica própria com o fisco.\n\nO legislador entendeu que permitir a ACP nesses temas transformaria a ação coletiva num meio de afastar tributos de forma ampla, com efeitos parecidos com os do controle abstrato de constitucionalidade, sem as garantias próprias desse controle.\n\nA ressalva da assertiva (\"desde que os contribuintes sejam indeterminados\") não existe na lei. A vedação é direta, sem condição. A banca costuma acrescentar ressalvas para tornar a frase aparentemente razoável.",
      "memorize": "ACP não cabe para tributos, contribuições previdenciárias, FGTS e fundos institucionais."
     }
    },
    {
     "id": "CPC-10-R1-02",
     "ponto": "DBA26-CPC-10",
     "tema": "ACP — legitimidade da associação",
     "assertiva": "A associação tem legitimidade para a ação civil pública desde que esteja constituída há pelo menos 2 anos e inclua entre suas finalidades a proteção do bem tutelado.",
     "gabarito": "E",
     "comentario": {
      "resumo": "Art. 5º, V, \"a\": **1 ano** de constituição — requisito que o juiz pode dispensar diante de manifesto interesse social (§ 4º). Os demais legitimados: MP, **Defensoria Pública**, entes federativos e administração indireta.",
      "lei": [
       {
        "lei": "L7347",
        "art": "5",
        "par": "",
        "inc": "",
        "rotulo": "Lei 7.347/1985, art. 5º, V, \"a\"",
        "texto": "a) esteja constituída há pelo menos 1 (um) ano nos termos da lei civil;"
       },
       {
        "lei": "L7347",
        "art": "5",
        "par": "",
        "inc": "",
        "rotulo": "Lei 7.347/1985, art. 5º, § 4º",
        "texto": "O requisito da pré-constituição poderá ser dispensado pelo juiz, quando haja manifesto interesse social evidenciado pela dimensão ou característica do dano, ou pela relevância do bem jurídico a ser protegido."
       }
      ],
      "palavras_chave": [
       "associação",
       "pré-constituição",
       "1 ano"
      ],
      "correcao": {
       "erro": "Exige que a associação esteja constituída há pelo menos 2 anos para propor ACP.",
       "certo": "A associação deve estar constituída há pelo menos 1 ano e ter entre suas finalidades a proteção do bem tutelado; o juiz pode dispensar a pré-constituição diante de manifesto interesse social."
      },
      "aprofundamento": "A exigência de pré-constituição da associação busca evitar que entidades sejam criadas às pressas apenas para propor uma ação específica, sem representatividade real. O tempo mínimo de existência é um indício de que a associação tem vínculo efetivo com o bem que pretende proteger.\n\nOs requisitos são dois: estar constituída há pelo menos 1 ano e incluir entre suas finalidades a proteção do bem tutelado (pertinência temática). O primeiro pode ser **dispensado** pelo juiz quando houver manifesto interesse social, pela dimensão do dano ou relevância do bem.\n\nA banca altera o prazo para 2 anos ou nega a possibilidade de dispensa. Lembre também os demais legitimados, que não têm essa exigência: MP, Defensoria Pública, entes federativos e entidades da administração indireta.",
      "memorize": "Associação na ACP: 1 ano de constituição (dispensável) + pertinência temática."
     }
    },
    {
     "id": "CPC-10-R1-03",
     "ponto": "DBA26-CPC-10",
     "tema": "ACP — competência",
     "assertiva": "As ações civis públicas serão propostas no foro do local onde ocorrer o dano, cujo juízo terá competência funcional para processar e julgar a causa.",
     "gabarito": "C",
     "comentario": {
      "resumo": "Art. 2º: competência **funcional** = **absoluta**.",
      "lei": [
       {
        "lei": "L7347",
        "art": "2",
        "par": "",
        "inc": "",
        "rotulo": "Lei 7.347/1985, art. 2º",
        "texto": "As ações previstas nesta Lei serão propostas no foro do local onde ocorrer o dano, cujo juízo terá competência funcional para processar e julgar a causa."
       }
      ],
      "palavras_chave": [
       "competência funcional",
       "local do dano"
      ],
      "aprofundamento": "A ação civil pública é proposta no foro do **local do dano** porque é ali que estão as provas, as vítimas e as consequências do fato. O juiz desse local tem melhores condições de avaliar a extensão do dano e acompanhar o cumprimento da decisão.\n\nO detalhe técnico é que a lei qualifica a competência como **funcional**. Embora o critério seja territorial, a qualificação de funcional significa que ela é **absoluta**: não pode ser modificada pela vontade das partes, não se prorroga e pode ser reconhecida de ofício.\n\nA banca explora a aparente contradição entre foro territorial e competência absoluta, dizendo que se trata de competência relativa. Na ACP, o critério territorial ganha natureza absoluta.",
      "memorize": "ACP: foro do local do dano, competência funcional = absoluta."
     }
    },
    {
     "id": "CPC-10-R1-04",
     "ponto": "DBA26-CPC-10",
     "tema": "ACP — limite territorial da coisa julgada",
     "assertiva": "Conforme a jurisprudência atual do STF, a sentença da ação civil pública faz coisa julgada erga omnes apenas nos limites da competência territorial do órgão prolator.",
     "gabarito": "E",
     "comentario": {
      "resumo": "O STF (Tema 1.075) declarou **inconstitucional** a redação do art. 16 dada pela Lei 9.494/1997 — que ainda aparece no texto do Planalto. ACP nacional ou regional segue o art. 93, II, do CDC.",
      "lei": [
       {
        "lei": "L7347",
        "art": "16",
        "par": "",
        "inc": "",
        "rotulo": "Lei 7.347/1985, art. 16 (redação declarada inconstitucional)",
        "texto": "A sentença civil fará coisa julgada erga omnes, nos limites da competência territorial do órgão prolator"
       }
      ],
      "juris": [
       {
        "tribunal": "STF",
        "fonte": "Tema 1.075/RG — RE 1.101.937 (sessão virtual finalizada em 7/4/2021)",
        "data": "07/04/2021",
        "texto": "É inconstitucional a redação do art. 16 da Lei 7.347/1985 dada pela Lei 9.494/1997 (limite territorial da coisa julgada); ACP de efeito nacional ou regional segue o art. 93, II, do CDC, com prevenção do juízo que primeiro conheceu."
       }
      ],
      "pegadinha": "O texto do art. 16 continua publicado — a banca cobra a letra da lei contra a tese do STF.",
      "palavras_chave": [
       "art. 16",
       "Tema 1.075",
       "erga omnes"
      ],
      "correcao": {
       "erro": "Afirma que, segundo o STF, a coisa julgada da ACP se limita à competência territorial do órgão prolator.",
       "certo": "O STF (Tema 1.075) declarou inconstitucional a redação do art. 16 dada pela Lei 9.494/1997; a ACP de efeito nacional ou regional segue o art. 93, II, do CDC, com prevenção do juízo que primeiro conheceu."
      },
      "aprofundamento": "A redação do art. 16 dada pela Lei 9.494/1997 limitava os efeitos da sentença coletiva ao território do juízo que a proferiu. O resultado era absurdo: o mesmo dano a consumidores de todo o país exigiria uma ação em cada comarca, multiplicando processos e decisões contraditórias.\n\nO STF, no **Tema 1.075**, declarou essa redação **inconstitucional**. Para danos de âmbito nacional ou regional, aplica-se o art. 93, II, do CDC, com prevenção do juízo que primeiro conheceu da causa. Os efeitos da coisa julgada seguem a extensão do dano e do pedido, não os limites territoriais do juiz.\n\nA pegadinha é que o texto declarado inconstitucional continua publicado. A banca cobra a letra da lei como se fosse o entendimento atual; a pergunta, porém, fala da jurisprudência do STF.",
      "memorize": "Limite territorial da coisa julgada na ACP: inconstitucional (Tema 1.075/STF)."
     }
    },
    {
     "id": "CPC-10-R1-05",
     "ponto": "DBA26-CPC-10",
     "tema": "Ação popular — legitimidade",
     "assertiva": "Qualquer cidadão é parte legítima para propor ação popular, mas a pessoa jurídica não tem essa legitimidade.",
     "gabarito": "C",
     "comentario": {
      "resumo": "Art. 1º da Lei 4.717/1965 e Súmula 365/STF. A cidadania se prova com o **título eleitoral** (art. 1º, § 3º). E o MS não substitui a ação popular (Súmula 101/STF).",
      "lei": [
       {
        "lei": "L4717",
        "art": "1",
        "par": "",
        "inc": "",
        "rotulo": "Lei 4.717/1965, art. 1º",
        "texto": "Qualquer cidadão será parte legítima"
       },
       {
        "lei": "L4717",
        "art": "1",
        "par": "",
        "inc": "",
        "rotulo": "Lei 4.717/1965, art. 1º, § 3º",
        "texto": "A prova da cidadania, para ingresso em juízo, será feita com o título eleitoral"
       }
      ],
      "juris": [
       {
        "tribunal": "STF",
        "fonte": "Súmula 365/STF",
        "data": "13/12/1963",
        "texto": "Pessoa jurídica não tem legitimidade para propor ação popular."
       },
       {
        "tribunal": "STF",
        "fonte": "Súmula 101/STF",
        "data": "13/12/1963",
        "texto": "O mandado de segurança não substitui a ação popular."
       }
      ],
      "palavras_chave": [
       "cidadão",
       "título eleitoral",
       "pessoa jurídica"
      ],
      "aprofundamento": "A ação popular é instrumento de **participação política**: permite que o cidadão fiscalize a gestão pública e peça a anulação de atos lesivos ao patrimônio público, à moralidade administrativa, ao meio ambiente e ao patrimônio histórico e cultural.\n\nComo é expressão da cidadania, a legitimidade é do **cidadão**, entendido como o eleitor, cuja condição se prova com o título eleitoral. A pessoa jurídica não exerce direitos políticos, e por isso não tem legitimidade, como fixou a Súmula 365/STF.\n\nA Súmula 101/STF completa o quadro: o mandado de segurança não substitui a ação popular, porque protege direito líquido e certo próprio, e não o interesse da coletividade. A banca costuma estender a legitimidade a associações, ao MP ou a pessoas jurídicas.",
      "memorize": "Ação popular: só o cidadão-eleitor (título eleitoral); pessoa jurídica não (Súmula 365/STF)."
     }
    },
    {
     "id": "CPC-10-R1-06",
     "ponto": "DBA26-CPC-10",
     "tema": "Ação popular — prescrição",
     "assertiva": "A ação popular prescreve em 3 anos.",
     "gabarito": "E",
     "comentario": {
      "resumo": "Art. 21: **5 anos**.",
      "lei": [
       {
        "lei": "L4717",
        "art": "21",
        "par": "",
        "inc": "",
        "rotulo": "Lei 4.717/1965, art. 21",
        "texto": "A ação prevista nesta lei prescreve em 5 (cinco) anos."
       }
      ],
      "palavras_chave": [
       "ação popular",
       "5 anos"
      ],
      "correcao": {
       "erro": "Fixa em 3 anos o prazo prescricional da ação popular.",
       "certo": "A ação popular prescreve em 5 anos."
      },
      "aprofundamento": "O prazo da ação popular busca equilibrar dois valores: permitir ao cidadão controlar atos lesivos ao patrimônio público e, ao mesmo tempo, dar estabilidade às relações administrativas. Sem prazo, qualquer ato antigo poderia ser questionado indefinidamente.\n\nO prazo é de 5 anos, coerente com o padrão quinquenal que aparece em diversos pontos do direito público. Ele se refere à pretensão de anular o ato lesivo pela via popular.\n\nA banca troca o número, colocando 3 anos, prazo que lembra a reparação civil no direito privado.",
      "memorize": "Ação popular prescreve em 5 anos."
     }
    },
    {
     "id": "CPC-10-R1-07",
     "ponto": "DBA26-CPC-10",
     "tema": "Ação popular — papel do MP",
     "assertiva": "Na ação popular, o Ministério Público pode assumir a defesa do ato impugnado quando entender que ele é legal.",
     "gabarito": "E",
     "comentario": {
      "resumo": "Art. 6º, § 4º: o MP acompanha a ação, é-lhe **vedado, em qualquer hipótese**, assumir a defesa do ato impugnado ou de seus autores.",
      "lei": [
       {
        "lei": "L4717",
        "art": "6",
        "par": "",
        "inc": "",
        "rotulo": "Lei 4.717/1965, art. 6º, § 4º",
        "texto": "O Ministério Público acompanhará a ação, cabendo-lhe apressar a produção da prova e promover a responsabilidade, civil ou criminal, dos que nela incidirem, sendo-lhe vedado, em qualquer hipótese, assumir a defesa do ato impugnado ou dos seus autores."
       }
      ],
      "palavras_chave": [
       "MP",
       "ação popular",
       "vedação"
      ],
      "correcao": {
       "erro": "Permite que o MP assuma a defesa do ato impugnado quando o considerar legal.",
       "certo": "Na ação popular, o MP acompanha a ação, apressa a prova e promove a responsabilidade dos envolvidos, sendo-lhe vedado, em qualquer hipótese, assumir a defesa do ato impugnado ou de seus autores."
      },
      "aprofundamento": "Na ação popular, o MP atua como **fiscal da ordem jurídica**, com uma postura de reforço à tutela do patrimônio público. Ele acompanha a ação, apressa a produção da prova e promove a responsabilidade civil ou criminal dos envolvidos.\n\nA lei proíbe, **em qualquer hipótese**, que ele assuma a defesa do ato impugnado ou de seus autores. A razão é a coerência institucional: o MP é defensor do interesse público e da moralidade administrativa, e não pode atuar como advogado do administrador acusado de lesar o patrimônio.\n\nIsso não obriga o MP a concordar com o autor: ele pode opinar pela improcedência se entender que não há lesão. O que não pode é atuar como defensor do ato. Se o autor desistir, o MP pode assumir o polo ativo.",
      "memorize": "Ação popular: MP fiscaliza, nunca defende o ato impugnado."
     }
    },
    {
     "id": "CPC-10-R1-08",
     "ponto": "DBA26-CPC-10",
     "tema": "MS — cabimento",
     "assertiva": "Conceder-se-á mandado de segurança para proteger direito líquido e certo, não amparado por habeas corpus ou habeas data, contra ilegalidade ou abuso de poder de autoridade.",
     "gabarito": "C",
     "comentario": {
      "resumo": "Art. 1º da Lei 12.016/2009: **residualidade** em relação ao HC e ao HD.",
      "lei": [
       {
        "lei": "L12016",
        "art": "1",
        "par": "",
        "inc": "",
        "rotulo": "Lei 12.016/2009, art. 1º",
        "texto": "Conceder-se-á mandado de segurança para proteger direito líquido e certo, não amparado por habeas corpus ou habeas data, sempre que, ilegalmente ou com abuso de poder, qualquer pessoa física ou jurídica sofrer violação ou houver justo receio de sofrê-la por parte de autoridade, seja de que categoria for e sejam quais forem as funções que exerça."
       }
      ],
      "palavras_chave": [
       "direito líquido e certo",
       "residualidade"
      ],
      "aprofundamento": "O mandado de segurança é uma ação constitucional de rito célere, para proteger **direito líquido e certo**, aquele cujos fatos podem ser comprovados de plano, por documentos, sem necessidade de produção de outras provas.\n\nO caráter **residual** se explica pela divisão de tarefas entre os remédios constitucionais. A liberdade de locomoção é protegida pelo habeas corpus; o acesso e a retificação de dados pessoais, pelo habeas data. O mandado de segurança cobre o restante.\n\nO ato impugnado deve vir de **autoridade**, ou de agente de pessoa jurídica no exercício de atribuições do poder público. A banca costuma dizer que o MS exige dilação probatória, ou que cabe contra ato de particular sem delegação pública.",
      "memorize": "MS: direito líquido e certo (prova pré-constituída), residual a HC e HD, contra autoridade."
     }
    },
    {
     "id": "CPC-10-R1-09",
     "ponto": "DBA26-CPC-10",
     "tema": "MS — prazo decadencial",
     "assertiva": "O direito de requerer mandado de segurança extingue-se decorridos 90 dias contados da ciência, pelo interessado, do ato impugnado.",
     "gabarito": "E",
     "comentario": {
      "resumo": "Art. 23: **120 dias** — prazo **decadencial**, constitucional segundo a Súmula 632/STF e a ADI 4.296.",
      "lei": [
       {
        "lei": "L12016",
        "art": "23",
        "par": "",
        "inc": "",
        "rotulo": "Lei 12.016/2009, art. 23",
        "texto": "O direito de requerer mandado de segurança extinguir-se-á decorridos 120 (cento e vinte) dias, contados da ciência, pelo interessado, do ato impugnado."
       }
      ],
      "palavras_chave": [
       "120 dias",
       "decadência"
      ],
      "correcao": {
       "erro": "Fixa em 90 dias o prazo decadencial do mandado de segurança.",
       "certo": "O direito de requerer mandado de segurança extingue-se decorridos 120 dias, contados da ciência, pelo interessado, do ato impugnado."
      },
      "aprofundamento": "O prazo do mandado de segurança é **decadencial**: não se suspende nem se interrompe. Ele existe porque o MS é via privilegiada e célere; quem deixa passar o tempo perde essa via especial, mas não o direito material, que pode ser buscado pelas vias ordinárias.\n\nO prazo é de 120 dias, contados da ciência do ato impugnado. A constitucionalidade desse limite foi afirmada pelo STF na Súmula 632 e na ADI 4.296. Em atos de trato sucessivo, como descontos mensais, o prazo se renova a cada ato.\n\nA banca troca o número, colocando 90 dias, ou chama o prazo de prescricional. Lembre: 120 dias, decadencial, a partir da ciência.",
      "memorize": "MS: 120 dias decadenciais da ciência do ato (Súmula 632/STF)."
     }
    },
    {
     "id": "CPC-10-R1-10",
     "ponto": "DBA26-CPC-10",
     "tema": "MS — hipóteses de não cabimento",
     "assertiva": "Não se concederá mandado de segurança contra ato do qual caiba recurso administrativo com efeito suspensivo, independentemente de caução, nem contra decisão judicial transitada em julgado.",
     "gabarito": "C",
     "comentario": {
      "resumo": "**Art. 5º, I** e III.",
      "lei": [
       {
        "lei": "L12016",
        "art": "5",
        "par": "",
        "inc": "",
        "rotulo": "Lei 12.016/2009, art. 5º, I",
        "texto": "I - de ato do qual caiba recurso administrativo com efeito suspensivo, independentemente de caução;"
       },
       {
        "lei": "L12016",
        "art": "5",
        "par": "",
        "inc": "",
        "rotulo": "Lei 12.016/2009, art. 5º, III",
        "texto": "III - de decisão judicial transitada em julgado."
       }
      ],
      "palavras_chave": [
       "MS",
       "não cabimento"
      ],
      "aprofundamento": "As hipóteses de não cabimento do MS seguem a lógica da **subsidiariedade**. Se existe outro meio igualmente eficaz para afastar a lesão, não há necessidade da via excepcional.\n\nNo recurso administrativo com efeito suspensivo, **independentemente de caução**, a própria administração já paralisa o ato, e o administrado não sofre lesão atual. Se o recurso exigir caução, o MS volta a ser cabível, porque a garantia impõe ônus. Na decisão judicial **transitada em julgado**, o meio próprio é a ação rescisória; admitir o MS seria contornar a coisa julgada.\n\nA lei também veda o MS contra decisão judicial da qual caiba recurso com efeito suspensivo. A banca costuma omitir a expressão \"independentemente de caução\" ou admitir MS contra decisão transitada.",
      "memorize": "MS não cabe contra ato com recurso administrativo suspensivo sem caução nem contra decisão transitada em julgado."
     }
    },
    {
     "id": "CPC-10-R1-11",
     "ponto": "DBA26-CPC-10",
     "tema": "MS — honorários",
     "assertiva": "Não cabe, no mandado de segurança, condenação ao pagamento de honorários advocatícios, sem prejuízo das sanções por litigância de má-fé.",
     "gabarito": "C",
     "comentario": {
      "resumo": "**Art. 25** da Lei 12.016/2009; Súmulas 105/STJ e 512/STF.",
      "lei": [
       {
        "lei": "L12016",
        "art": "25",
        "par": "",
        "inc": "",
        "rotulo": "Lei 12.016/2009, art. 25",
        "texto": "Não cabem, no processo de mandado de segurança, a interposição de embargos infringentes e a condenação ao pagamento dos honorários advocatícios, sem prejuízo da aplicação de sanções no caso de litigância de má-fé."
       }
      ],
      "juris": [
       {
        "tribunal": "STJ",
        "fonte": "Súmula 105/STJ",
        "data": "26/05/1994",
        "texto": "Na ação de mandado de segurança não se admite condenação em honorários advocatícios."
       },
       {
        "tribunal": "STF",
        "fonte": "Súmula 512/STF",
        "data": "03/12/1969",
        "texto": "Não cabe condenação em honorários de advogado na ação de mandado de segurança."
       }
      ],
      "palavras_chave": [
       "honorários",
       "mandado de segurança"
      ],
      "aprofundamento": "A ausência de honorários no mandado de segurança tem razão histórica e funcional: o MS é garantia constitucional de proteção do cidadão contra o poder público, e a lei quis evitar que o risco de pagar honorários inibisse seu uso.\n\nA regra, consolidada nas Súmulas 105/STJ e 512/STF e depois incorporada à lei, vale para ambas as partes: nem o impetrante vencido nem a autoridade vencida pagam honorários. O mesmo artigo também veda os embargos infringentes no MS.\n\nA ressalva é a **litigância de má-fé**: quem usa o MS de forma abusiva continua sujeito às sanções processuais. A banca costuma dizer que só o impetrante fica isento, ou que a regra afasta também as sanções por má-fé.",
      "memorize": "MS: sem honorários (Súmulas 105/STJ e 512/STF), mas com sanções por má-fé."
     }
    },
    {
     "id": "CPC-10-R1-12",
     "ponto": "DBA26-CPC-10",
     "tema": "MS coletivo — legitimados",
     "assertiva": "O mandado de segurança coletivo pode ser impetrado por associação legalmente constituída e em funcionamento há pelo menos 1 ano, exigida autorização especial dos associados.",
     "gabarito": "E",
     "comentario": {
      "resumo": "Art. 21: o requisito de **1 ano** de funcionamento está certo, mas a autorização especial é **dispensada** (Súmula 629/STF).",
      "lei": [
       {
        "lei": "L12016",
        "art": "21",
        "par": "",
        "inc": "",
        "rotulo": "Lei 12.016/2009, art. 21",
        "texto": "ou por organização sindical, entidade de classe ou associação legalmente constituída e em funcionamento há, pelo menos, 1 (um) ano, em defesa de direitos líquidos e certos da totalidade, ou de parte, dos seus membros ou associados, na forma dos seus estatutos e desde que pertinentes às suas finalidades, dispensada, para tanto, autorização especial."
       }
      ],
      "juris": [
       {
        "tribunal": "STF",
        "fonte": "Súmula 629/STF",
        "data": "24/09/2003",
        "texto": "A impetração de MS coletivo por entidade de classe em favor dos associados independe da autorização destes."
       }
      ],
      "palavras_chave": [
       "MS coletivo",
       "1 ano",
       "autorização"
      ],
      "correcao": {
       "erro": "Exige autorização especial dos associados para a impetração do MS coletivo.",
       "certo": "O MS coletivo pode ser impetrado por associação legalmente constituída e em funcionamento há pelo menos 1 ano, dispensada autorização especial dos associados (Súmula 629/STF)."
      },
      "aprofundamento": "O mandado de segurança coletivo é ajuizado por entidades em defesa dos direitos de seus membros. A associação deve estar legalmente constituída e em funcionamento há pelo menos 1 ano, o que garante representatividade e evita entidades criadas para um único caso.\n\nO ponto central é a **dispensa de autorização especial** dos associados. A entidade atua como **substituta processual**, em nome próprio, na defesa de direito alheio, e a autorização decorre do próprio estatuto e da pertinência com suas finalidades. Exigir autorização específica esvaziaria a ação coletiva. A Súmula 629/STF consolidou esse entendimento.\n\nA assertiva acerta o prazo e erra na autorização. É o padrão de frase meio certa: a banca deixa um elemento correto para dar credibilidade ao erro.",
      "memorize": "MS coletivo: associação com 1 ano, sem autorização especial dos associados (Súmula 629/STF)."
     }
    },
    {
     "id": "CPC-11-R1-01",
     "ponto": "DBA26-CPC-11",
     "tema": "Critérios do JEC",
     "assertiva": "O processo nos Juizados Especiais orienta-se pelos critérios da oralidade, simplicidade, informalidade, economia processual e celeridade, buscando, sempre que possível, a conciliação ou a transação.",
     "gabarito": "C",
     "comentario": {
      "resumo": "**Art. 2º** da Lei 9.099/1995.",
      "lei": [
       {
        "lei": "L9099",
        "art": "2",
        "par": "",
        "inc": "",
        "rotulo": "Lei 9.099/1995, art. 2º",
        "texto": "O processo orientar-se-á pelos critérios da oralidade, simplicidade, informalidade, economia processual e celeridade, buscando, sempre que possível, a conciliação ou a transação."
       }
      ],
      "palavras_chave": [
       "oralidade",
       "informalidade",
       "celeridade"
      ],
      "aprofundamento": "Os Juizados Especiais foram criados para ampliar o **acesso à justiça** nas causas de menor complexidade. O processo comum, com seus ritos, prazos e formalidades, é caro e demorado demais para conflitos do dia a dia, e muitas pessoas simplesmente desistiam de buscar seus direitos.\n\nOs critérios orientadores traduzem essa finalidade. **Oralidade**: os atos se concentram em audiência, com registro só do essencial. **Simplicidade e informalidade**: o ato vale se atingir a finalidade. **Economia processual e celeridade**: menos atos, menos tempo. E a busca constante pela **conciliação ou transação**, que é o objetivo preferencial.\n\nA banca costuma incluir critérios que não estão no artigo, como \"publicidade\" ou \"formalidade moderada\", ou omitir um deles. Vale decorar os cinco.",
      "memorize": "JEC: oralidade, simplicidade, informalidade, economia processual e celeridade + conciliação."
     }
    },
    {
     "id": "CPC-11-R1-02",
     "ponto": "DBA26-CPC-11",
     "tema": "Competência pelo valor",
     "assertiva": "O Juizado Especial Cível tem competência para as causas cujo valor não exceda 60 salários mínimos.",
     "gabarito": "E",
     "comentario": {
      "resumo": "JEC estadual: **40 SM** (art. 3º, I, Lei 9.099). **60 SM** é o teto do **Juizado da Fazenda Pública** (art. 2º, Lei 12.153).",
      "lei": [
       {
        "lei": "L9099",
        "art": "3",
        "par": "",
        "inc": "",
        "rotulo": "Lei 9.099/1995, art. 3º, I",
        "texto": "I - as causas cujo valor não exceda a quarenta vezes o salário mínimo;"
       }
      ],
      "pegadinha": "Mistura dos tetos de 40 SM (JEC) e 60 SM (JEFP/JEF).",
      "palavras_chave": [
       "40 salários mínimos",
       "competência"
      ],
      "correcao": {
       "erro": "Atribui ao Juizado Especial Cível estadual o teto de 60 salários mínimos.",
       "certo": "O Juizado Especial Cível tem competência para causas cujo valor não exceda 40 salários mínimos; o teto de 60 é dos Juizados da Fazenda Pública."
      },
      "aprofundamento": "O sistema de Juizados tem tetos diferentes conforme o tipo. O **Juizado Especial Cível** estadual (Lei 9.099/1995) julga causas até 40 salários mínimos. O **Juizado Especial da Fazenda Pública** (Lei 12.153) e o Juizado Federal vão até 60 salários mínimos.\n\nA diferença se explica pela natureza das causas: nas que envolvem o poder público, os valores tendem a ser maiores e o legislador quis abranger mais demandas, como as previdenciárias e as de servidores.\n\nNo JEC estadual, a opção pelo Juizado é do autor, e se ele quiser propor ali causa de valor maior, renuncia ao excedente, salvo conciliação. A banca troca os tetos, aplicando ao JEC o limite dos Juizados fazendários.",
      "memorize": "JEC: 40 salários mínimos. Juizado da Fazenda Pública: 60."
     }
    },
    {
     "id": "CPC-11-R1-03",
     "ponto": "DBA26-CPC-11",
     "tema": "Causas excluídas",
     "assertiva": "Ficam excluídas da competência do Juizado Especial Cível as causas de natureza alimentar, falimentar, fiscal e de interesse da Fazenda Pública, e as relativas a acidentes de trabalho, a resíduos e ao estado e capacidade das pessoas.",
     "gabarito": "C",
     "comentario": {
      "resumo": "Art. 3º, § 2º — **ainda que de cunho patrimonial**.",
      "lei": [
       {
        "lei": "L9099",
        "art": "3",
        "par": "",
        "inc": "",
        "rotulo": "Lei 9.099/1995, art. 3º, § 2º",
        "texto": "Ficam excluídas da competência do Juizado Especial as causas de natureza alimentar, falimentar, fiscal e de interesse da Fazenda Pública, e também as relativas a acidentes de trabalho, a resíduos e ao estado e capacidade das pessoas, ainda que de cunho patrimonial."
       }
      ],
      "palavras_chave": [
       "exclusões",
       "Fazenda Pública"
      ],
      "aprofundamento": "A exclusão dessas causas tem uma razão comum: são matérias que exigem **cognição mais profunda**, envolvem **interesse público** ou **direitos indisponíveis**, e não combinam com o rito simplificado e informal dos Juizados.\n\nAlimentos e estado e capacidade das pessoas envolvem direitos indisponíveis e situações familiares delicadas. Falência e questões fiscais têm procedimentos e interesses próprios. Acidente de trabalho e resíduos exigem perícia complexa. A Fazenda Pública tem Juizado próprio.\n\nO detalhe que a banca cobra é a expressão final do dispositivo: as causas são excluídas **ainda que de cunho patrimonial**. Não importa se o pedido é só de dinheiro; a natureza da matéria afasta o Juizado.",
      "memorize": "Fora do JEC: alimentar, falimentar, fiscal, Fazenda, acidente de trabalho, resíduos, estado e capacidade."
     }
    },
    {
     "id": "CPC-11-R1-04",
     "ponto": "DBA26-CPC-11",
     "tema": "Assistência por advogado",
     "assertiva": "Nas causas de valor até 40 salários mínimos, as partes comparecerão pessoalmente, sendo facultativa a assistência por advogado.",
     "gabarito": "E",
     "comentario": {
      "resumo": "Art. 9º: assistência facultativa até **20 SM**; acima disso, **obrigatória**. No recurso, advogado sempre (art. 41, § 2º).",
      "lei": [
       {
        "lei": "L9099",
        "art": "9",
        "par": "",
        "inc": "",
        "rotulo": "Lei 9.099/1995, art. 9º",
        "texto": "Nas causas de valor até vinte salários mínimos, as partes comparecerão pessoalmente, podendo ser assistidas por advogado; nas de valor superior, a assistência é obrigatória."
       }
      ],
      "palavras_chave": [
       "advogado",
       "20 salários mínimos"
      ],
      "correcao": {
       "erro": "Estende a assistência facultativa por advogado até 40 salários mínimos.",
       "certo": "Nas causas de valor até 20 salários mínimos a assistência por advogado é facultativa; nas de valor superior, é obrigatória."
      },
      "aprofundamento": "A dispensa de advogado nos Juizados busca **facilitar o acesso** de quem tem causas pequenas, para as quais contratar advogado seria desproporcional. Mas a lei fixa um limite: quanto maior o valor, maior a complexidade e o risco, e mais importante a defesa técnica.\n\nAté 20 salários mínimos, a assistência é **facultativa**. Acima disso, até o teto do Juizado, é **obrigatória**. E, no recurso, a presença de advogado é sempre exigida, independentemente do valor, porque a fase recursal é técnica.\n\nSe uma das partes comparece com advogado e a outra não, esta pode pedir assistência judiciária. A banca troca o limite da facultatividade pelo teto do Juizado.",
      "memorize": "JEC: sem advogado até 20 salários mínimos; acima disso e no recurso, advogado obrigatório."
     }
    },
    {
     "id": "CPC-11-R1-05",
     "ponto": "DBA26-CPC-11",
     "tema": "Intervenção de terceiros",
     "assertiva": "No processo do Juizado Especial Cível não se admite qualquer forma de intervenção de terceiro nem de assistência, mas admite-se o litisconsórcio.",
     "gabarito": "C",
     "comentario": {
      "resumo": "Art. 10 da Lei 9.099. O CPC abriu uma exceção: o **incidente de desconsideração da personalidade jurídica** (art. 1.062).",
      "excecoes": [
       "IDPJ é aplicável aos Juizados (CPC, art. 1.062)"
      ],
      "lei": [
       {
        "lei": "L9099",
        "art": "10",
        "par": "",
        "inc": "",
        "rotulo": "Lei 9.099/1995, art. 10",
        "texto": "Não se admitirá, no processo, qualquer forma de intervenção de terceiro nem de assistência. Admitir-se-á o litisconsórcio."
       },
       {
        "lei": "L13105",
        "art": "1062",
        "par": "",
        "inc": "",
        "rotulo": "CPC, art. 1.062",
        "texto": "O incidente de desconsideração da personalidade jurídica aplica-se ao processo de competência dos juizados especiais."
       }
      ],
      "palavras_chave": [
       "intervenção de terceiros",
       "litisconsórcio",
       "IDPJ"
      ],
      "aprofundamento": "A vedação à intervenção de terceiros decorre dos critérios de **simplicidade e celeridade**. Denunciação da lide, chamamento ao processo e assistência ampliam o objeto do processo, multiplicam partes e atrasam o julgamento, o que contraria a lógica dos Juizados.\n\nO **litisconsórcio**, por outro lado, é admitido, porque não traz terceiro estranho à demanda: as partes já integram a relação original desde o início.\n\nO CPC abriu uma exceção expressa: o **incidente de desconsideração da personalidade jurídica** aplica-se aos Juizados, porque é instrumento de efetividade, especialmente em relações de consumo. A banca costuma dizer que o IDPJ também é vedado, ou que o litisconsórcio não é admitido.",
      "memorize": "JEC: sem intervenção de terceiros nem assistência; litisconsórcio sim; IDPJ é exceção admitida."
     }
    },
    {
     "id": "CPC-11-R1-06",
     "ponto": "DBA26-CPC-11",
     "tema": "Recurso inominado",
     "assertiva": "O recurso contra a sentença do Juizado Especial Cível será interposto no prazo de 15 dias, contados da ciência da sentença.",
     "gabarito": "E",
     "comentario": {
      "resumo": "Art. 42: **10 dias**; preparo em **48 horas** (§ 1º).",
      "lei": [
       {
        "lei": "L9099",
        "art": "42",
        "par": "",
        "inc": "",
        "rotulo": "Lei 9.099/1995, art. 42",
        "texto": "O recurso será interposto no prazo de dez dias, contados da ciência da sentença, por petição escrita, da qual constarão as razões e o pedido do recorrente."
       }
      ],
      "palavras_chave": [
       "recurso inominado",
       "10 dias"
      ],
      "correcao": {
       "erro": "Fixa em 15 dias o prazo do recurso contra sentença do Juizado Especial Cível.",
       "certo": "O recurso contra a sentença do JEC é interposto no prazo de 10 dias, contados da ciência da sentença, com preparo nas 48 horas seguintes."
      },
      "aprofundamento": "O recurso inominado é o recurso próprio contra a sentença dos Juizados, julgado por **turma recursal** formada por juízes de primeiro grau. O prazo é de 10 dias, e não de 15, porque o sistema dos Juizados tem regras próprias, mais céleres, que não seguem a uniformização do CPC.\n\nO **preparo** deve ser feito nas 48 horas seguintes à interposição, independentemente de intimação, sob pena de deserção. No recurso, a parte precisa estar representada por advogado.\n\nA banca transporta para os Juizados o prazo geral de 15 dias do CPC. Lembre: a lei especial prevalece sobre a geral nesse ponto.",
      "memorize": "Recurso inominado: 10 dias; preparo em 48 horas."
     }
    },
    {
     "id": "CPC-11-R1-07",
     "ponto": "DBA26-CPC-11",
     "tema": "Ausência do autor",
     "assertiva": "Extingue-se o processo no Juizado Especial Cível quando o autor deixar de comparecer a qualquer das audiências do processo.",
     "gabarito": "C",
     "comentario": {
      "resumo": "**Art. 51, I** — independentemente de intimação pessoal prévia (§ 1º).",
      "lei": [
       {
        "lei": "L9099",
        "art": "51",
        "par": "",
        "inc": "",
        "rotulo": "Lei 9.099/1995, art. 51, I",
        "texto": "I - quando o autor deixar de comparecer a qualquer das audiências do processo;"
       }
      ],
      "palavras_chave": [
       "extinção",
       "ausência do autor"
      ],
      "aprofundamento": "Nos Juizados, a **presença do autor** é essencial porque o procedimento é oral e concentrado na audiência, e a conciliação depende da participação pessoal das partes. Se o autor não comparece, demonstra desinteresse e impede o andamento do processo.\n\nPor isso a lei prevê a extinção sem resolução do mérito, **independentemente de intimação pessoal prévia**. O autor pode ser condenado em custas, salvo se comprovar que a ausência decorreu de força maior.\n\nO contraste é com o réu: se ele não comparece, ocorre a **revelia**, com presunção de veracidade dos fatos alegados pelo autor. A banca costuma inverter as consequências ou exigir intimação pessoal antes da extinção.",
      "memorize": "JEC: autor ausente = extinção; réu ausente = revelia."
     }
    },
    {
     "id": "CPC-11-R1-08",
     "ponto": "DBA26-CPC-11",
     "tema": "Sucumbência em primeiro grau",
     "assertiva": "A sentença de primeiro grau do Juizado Especial Cível não condenará o vencido em custas e honorários de advogado, ressalvados os casos de litigância de má-fé.",
     "gabarito": "C",
     "comentario": {
      "resumo": "Art. 55. Em segundo grau, o **recorrente vencido** paga custas e honorários de 10% a 20%.",
      "lei": [
       {
        "lei": "L9099",
        "art": "55",
        "par": "",
        "inc": "",
        "rotulo": "Lei 9.099/1995, art. 55",
        "texto": "A sentença de primeiro grau não condenará o vencido em custas e honorários de advogado, ressalvados os casos de litigância de má-fé."
       }
      ],
      "palavras_chave": [
       "custas",
       "honorários",
       "má-fé"
      ],
      "aprofundamento": "A gratuidade em primeiro grau nos Juizados é um estímulo ao **acesso à justiça**: a parte pode buscar seu direito sem medo de pagar custas e honorários se perder. É coerente com a dispensa de advogado nas causas menores.\n\nA ressalva da **litigância de má-fé** impede que essa gratuidade seja usada como escudo para demandas abusivas ou temerárias.\n\nNo segundo grau, a lógica muda: o **recorrente vencido** paga custas e honorários, fixados entre 10% e 20%. O objetivo é desestimular recursos e valorizar a decisão de primeiro grau. Note que só o recorrente vencido paga; se o recorrente vencer, não há condenação. A banca costuma estender a isenção ao segundo grau.",
      "memorize": "JEC: sem custas e honorários no 1º grau (salvo má-fé); no recurso, paga o recorrente vencido."
     }
    },
    {
     "id": "CPC-11-R1-09",
     "ponto": "DBA26-CPC-11",
     "tema": "Recurso especial nos Juizados",
     "assertiva": "Cabe recurso especial contra decisão proferida por turma recursal dos Juizados Especiais.",
     "gabarito": "E",
     "comentario": {
      "resumo": "Súmula 203/STJ: **não cabe REsp** — turma recursal não é \"tribunal\" (CF, art. 105, III).",
      "juris": [
       {
        "tribunal": "STJ",
        "fonte": "Súmula 203/STJ (redação alterada em 23/05/2002)",
        "data": "23/05/2002",
        "texto": "Não cabe recurso especial contra decisão proferida por órgão de segundo grau dos Juizados Especiais."
       }
      ],
      "palavras_chave": [
       "recurso especial",
       "turma recursal"
      ],
      "correcao": {
       "erro": "Admite recurso especial contra decisão de turma recursal dos Juizados Especiais.",
       "certo": "Não cabe recurso especial contra decisão proferida por órgão de segundo grau dos Juizados Especiais (Súmula 203/STJ), porque turma recursal não é tribunal."
      },
      "aprofundamento": "O recurso especial cabe contra causas decididas por **tribunais**, conforme a Constituição. As turmas recursais dos Juizados são órgãos formados por juízes de primeiro grau, e não são tribunais no sentido constitucional. Por isso a Súmula 203/STJ afasta o REsp contra suas decisões.\n\nO recurso extraordinário, por outro lado, cabe contra causas decididas em única ou última instância, sem exigir que a decisão venha de tribunal. Assim, das decisões das turmas recursais cabe RE ao STF, se houver questão constitucional com repercussão geral.\n\nPara uniformizar a interpretação de lei federal nos Juizados, há mecanismos próprios, como os pedidos de uniformização. A banca costuma admitir o REsp ou negar também o RE.",
      "memorize": "Turma recursal: não cabe REsp (Súmula 203/STJ); cabe RE."
     }
    },
    {
     "id": "CPC-11-R1-10",
     "ponto": "DBA26-CPC-11",
     "tema": "JEFP — competência",
     "assertiva": "É de competência dos Juizados Especiais da Fazenda Pública processar, conciliar e julgar causas cíveis de interesse dos Estados, do DF, dos Territórios e dos Municípios até o valor de 60 salários mínimos, competência que é absoluta no foro onde estiver instalado.",
     "gabarito": "C",
     "comentario": {
      "resumo": "**Art. 2º**, caput e § 4º, da Lei 12.153/2009.",
      "lei": [
       {
        "lei": "L12153",
        "art": "2",
        "par": "",
        "inc": "",
        "rotulo": "Lei 12.153/2009, art. 2º",
        "texto": "É de competência dos Juizados Especiais da Fazenda Pública processar, conciliar e julgar causas cíveis de interesse dos Estados, do Distrito Federal, dos Territórios e dos Municípios, até o valor de 60 (sessenta) salários mínimos."
       },
       {
        "lei": "L12153",
        "art": "2",
        "par": "",
        "inc": "",
        "rotulo": "Lei 12.153/2009, art. 2º, § 4º",
        "texto": "No foro onde estiver instalado Juizado Especial da Fazenda Pública, a sua competência é absoluta."
       }
      ],
      "palavras_chave": [
       "JEFP",
       "60 salários mínimos",
       "competência absoluta"
      ],
      "aprofundamento": "O Juizado Especial da Fazenda Pública estende a lógica dos Juizados às causas contra **Estados, DF, Territórios e Municípios**. Muitas demandas contra o poder público são repetitivas e de valor moderado, como diferenças de remuneração de servidores, e se beneficiam de um rito mais simples.\n\nO teto é de 60 salários mínimos, maior que o do JEC estadual. E, diferentemente do JEC, a competência é **absoluta** no foro onde o Juizado estiver instalado: o autor não pode optar pela vara comum. A razão é organizar a distribuição e garantir que o Juizado cumpra sua finalidade.\n\nA banca costuma tornar a competência facultativa, como no JEC, ou trocar o teto.",
      "memorize": "Juizado da Fazenda Pública: até 60 salários mínimos, competência absoluta onde instalado."
     }
    },
    {
     "id": "CPC-11-R1-11",
     "ponto": "DBA26-CPC-11",
     "tema": "JEFP — partes",
     "assertiva": "Podem ser réus no Juizado Especial da Fazenda Pública os Estados, o DF, os Territórios e os Municípios, bem como autarquias, fundações, empresas públicas e sociedades de economia mista a eles vinculadas.",
     "gabarito": "E",
     "comentario": {
      "resumo": "Art. 5º, II: **autarquias, fundações e empresas públicas** — a lei **não** inclui as sociedades de economia mista.",
      "lei": [
       {
        "lei": "L12153",
        "art": "5",
        "par": "",
        "inc": "",
        "rotulo": "Lei 12.153/2009, art. 5º, II",
        "texto": "II – como réus, os Estados, o Distrito Federal, os Territórios e os Municípios, bem como autarquias, fundações e empresas públicas a eles vinculadas."
       }
      ],
      "palavras_chave": [
       "JEFP",
       "réus",
       "sociedade de economia mista"
      ],
      "correcao": {
       "erro": "Inclui as sociedades de economia mista entre os réus admitidos no Juizado Especial da Fazenda Pública.",
       "certo": "Podem ser réus os Estados, o DF, os Territórios e os Municípios, bem como autarquias, fundações e empresas públicas a eles vinculadas; as sociedades de economia mista não estão no rol."
      },
      "aprofundamento": "O Juizado da Fazenda Pública admite como réus os entes federativos e as entidades da administração indireta a eles vinculadas que têm regime de direito público ou próximo dele: **autarquias, fundações e empresas públicas**.\n\nAs **sociedades de economia mista** ficaram de fora. Elas têm capital privado e público, regime predominantemente privado, e respondem às ações pelas vias comuns. A lei optou por não incluí-las.\n\nA pegadinha é a lista ampliada. Diante da enumeração das entidades, procure a que foi acrescentada. No caso, a sociedade de economia mista é o elemento estranho.",
      "memorize": "JEFP como réu: entes, autarquias, fundações e empresas públicas. Sociedade de economia mista não."
     }
    },
    {
     "id": "CPC-11-R1-12",
     "ponto": "DBA26-CPC-11",
     "tema": "JEFP — prazos",
     "assertiva": "No Juizado Especial da Fazenda Pública, as pessoas jurídicas de direito público têm prazo em dobro para recorrer.",
     "gabarito": "E",
     "comentario": {
      "resumo": "Art. 7º: **não há prazo diferenciado** para qualquer ato, **inclusive recursos**; citação para a audiência com antecedência mínima de 30 dias.",
      "lei": [
       {
        "lei": "L12153",
        "art": "7",
        "par": "",
        "inc": "",
        "rotulo": "Lei 12.153/2009, art. 7º",
        "texto": "Não haverá prazo diferenciado para a prática de qualquer ato processual pelas pessoas jurídicas de direito público, inclusive a interposição de recursos, devendo a citação para a audiência de conciliação ser efetuada com antecedência mínima de 30 (trinta) dias."
       }
      ],
      "palavras_chave": [
       "prazo simples",
       "Fazenda Pública"
      ],
      "correcao": {
       "erro": "Atribui prazo em dobro para recorrer às pessoas jurídicas de direito público no Juizado da Fazenda Pública.",
       "certo": "No Juizado da Fazenda Pública não há prazo diferenciado para qualquer ato das pessoas jurídicas de direito público, inclusive recursos; a citação para a audiência deve ter antecedência mínima de 30 dias."
      },
      "aprofundamento": "No processo comum, as pessoas jurídicas de direito público têm prazo em dobro, justificado pelo volume de processos e pela estrutura da advocacia pública. Nos Juizados da Fazenda Pública, porém, a lei optou por **igualar** as partes, em nome da celeridade.\n\nNão há prazo diferenciado para **qualquer ato processual**, inclusive recursos. Como compensação, a citação para a audiência de conciliação deve ocorrer com antecedência mínima de 30 dias, dando ao ente tempo para preparar a defesa e avaliar a possibilidade de acordo.\n\nA banca leva para o Juizado a prerrogativa do processo comum. A expressão \"inclusive a interposição de recursos\" do texto legal foi escrita justamente para afastar essa ideia.",
      "memorize": "JEFP: sem prazo em dobro para a Fazenda, nem para recorrer; citação com 30 dias de antecedência."
     }
    },
    {
     "id": "CPC-12-R1-01",
     "ponto": "DBA26-CPC-12",
     "tema": "Incompetência relativa",
     "assertiva": "Segundo o STJ, a incompetência relativa pode ser declarada de ofício pelo juiz.",
     "gabarito": "E",
     "comentario": {
      "resumo": "Súmula 33/STJ: **não pode** ser declarada de ofício (CPC, art. 337, § 5º). Exceção: cláusula de eleição abusiva, **antes da citação** (art. 63, § 3º).",
      "excecoes": [
       "Cláusula de eleição de foro abusiva, antes da citação (CPC, art. 63, § 3º)"
      ],
      "juris": [
       {
        "tribunal": "STJ",
        "fonte": "Súmula 33/STJ",
        "data": "24/10/1991",
        "texto": "A incompetência relativa não pode ser declarada de ofício."
       }
      ],
      "palavras_chave": [
       "incompetência relativa",
       "Súmula 33"
      ],
      "correcao": {
       "erro": "Afirma que, segundo o STJ, a incompetência relativa pode ser declarada de ofício.",
       "certo": "A incompetência relativa não pode ser declarada de ofício (Súmula 33/STJ), salvo a ineficácia da cláusula de eleição de foro abusiva reconhecida antes da citação."
      },
      "aprofundamento": "A incompetência relativa protege **interesse das partes**, e não interesse público. Se o réu não a alega, entende-se que aceitou litigar naquele foro, e a competência se prorroga. Por isso o juiz não pode declará-la de ofício, como fixou a Súmula 33/STJ e como reproduz o código.\n\nA exceção é a **cláusula de eleição de foro abusiva**, que o juiz pode reputar ineficaz de ofício, mas apenas **antes da citação**. Depois de citado, cabe ao réu alegar a abusividade na contestação, sob pena de preclusão.\n\nA lógica é proteger a parte vulnerável, normalmente o consumidor, de uma cláusula imposta em contrato de adesão. A banca costuma ignorar a súmula ou estender a exceção para depois da citação.",
      "memorize": "Incompetência relativa: nunca de ofício (Súmula 33/STJ); cláusula abusiva, de ofício só antes da citação."
     }
    },
    {
     "id": "CPC-12-R1-02",
     "ponto": "DBA26-CPC-12",
     "tema": "Interesse da União",
     "assertiva": "Compete à Justiça Federal decidir sobre a existência de interesse jurídico que justifique a presença, no processo, da União, de suas autarquias ou empresas públicas.",
     "gabarito": "C",
     "comentario": {
      "resumo": "**Súmula 150**/STJ.",
      "juris": [
       {
        "tribunal": "STJ",
        "fonte": "Súmula 150/STJ",
        "data": "07/02/1996",
        "texto": "Compete à Justiça Federal decidir sobre a existência de interesse jurídico que justifique a presença da União, suas autarquias ou empresas públicas."
       }
      ],
      "palavras_chave": [
       "Justiça Federal",
       "Súmula 150"
      ],
      "aprofundamento": "Quando a União, suas autarquias ou empresas públicas pedem para ingressar num processo, surge a dúvida: há realmente interesse jurídico que justifique o deslocamento para a Justiça Federal? A Súmula 150/STJ responde quem decide: a **própria Justiça Federal**.\n\nA lógica é que a competência da Justiça Federal é fixada pela Constituição em razão da pessoa. Só o juiz federal pode dizer se o ente federal tem ou não interesse; o juiz estadual não pode negar esse interesse e manter a causa.\n\nSe o juiz federal concluir que não há interesse, devolve os autos à Justiça estadual, sem suscitar conflito. A banca costuma atribuir ao juiz estadual o poder de decidir sobre o interesse da União.",
      "memorize": "Interesse da União no processo: quem decide é a Justiça Federal (Súmula 150/STJ)."
     }
    },
    {
     "id": "CPC-12-R1-03",
     "ponto": "DBA26-CPC-12",
     "tema": "Investigação de paternidade com alimentos",
     "assertiva": "Na ação de investigação de paternidade cumulada com alimentos, é competente o foro do domicílio ou da residência do alimentando.",
     "gabarito": "C",
     "comentario": {
      "resumo": "**Súmula 1**/STJ, em linha com o art. 53, II, do CPC.",
      "juris": [
       {
        "tribunal": "STJ",
        "fonte": "Súmula 1/STJ",
        "data": "25/04/1990",
        "texto": "Na investigação de paternidade cumulada com alimentos, o foro competente é o do domicílio ou da residência do alimentando."
       }
      ],
      "palavras_chave": [
       "alimentando",
       "Súmula 1"
      ],
      "aprofundamento": "A regra geral de competência é o domicílio do réu, mas nas ações de alimentos a lei protege a parte **vulnerável**: o alimentando, que precisa dos alimentos para sobreviver e muitas vezes não tem condições de litigar longe de casa.\n\nA Súmula 1/STJ estende esse foro à ação de investigação de paternidade quando cumulada com alimentos. Embora a investigação seja ação de estado, a cumulação atrai o foro protetivo, porque o pedido de alimentos é o que motiva a proteção.\n\nO CPC segue a mesma lógica no foro do domicílio ou residência do alimentando. A banca costuma aplicar a regra geral do domicílio do réu, que nessa situação não prevalece.",
      "memorize": "Investigação de paternidade + alimentos: foro do alimentando (Súmula 1/STJ)."
     }
    },
    {
     "id": "CPC-12-R1-04",
     "ponto": "DBA26-CPC-12",
     "tema": "MP e patrimônio público",
     "assertiva": "O Ministério Público não tem legitimidade para propor ação civil pública em defesa do patrimônio público, que cabe exclusivamente ao ente lesado.",
     "gabarito": "E",
     "comentario": {
      "resumo": "Súmula 329/STJ: o MP **tem legitimidade** (também CF, art. 129, III).",
      "juris": [
       {
        "tribunal": "STJ",
        "fonte": "Súmula 329/STJ",
        "data": "02/08/2006",
        "texto": "O Ministério Público tem legitimidade para propor ação civil pública em defesa do patrimônio público."
       }
      ],
      "palavras_chave": [
       "MP",
       "patrimônio público",
       "Súmula 329"
      ],
      "correcao": {
       "erro": "Nega a legitimidade do MP para propor ACP em defesa do patrimônio público e a atribui exclusivamente ao ente lesado.",
       "certo": "O Ministério Público tem legitimidade para propor ação civil pública em defesa do patrimônio público (Súmula 329/STJ)."
      },
      "aprofundamento": "A defesa do **patrimônio público** é interesse da coletividade, e não apenas do ente que sofreu o prejuízo. Por isso a Constituição atribui ao Ministério Público a promoção da ação civil pública para proteger o patrimônio público e social, e a Súmula 329/STJ confirma essa legitimidade.\n\nA razão prática é evidente: muitas vezes o ente lesado é governado justamente por quem causou o dano, e não teria interesse em processá-lo. A legitimidade do MP garante que a lesão não fique sem resposta.\n\nA legitimidade é **concorrente**: o ente lesado também pode agir, assim como outros colegitimados. A assertiva erra ao falar em legitimidade exclusiva do ente, o que contraria tanto a súmula quanto a lógica do sistema.",
      "memorize": "MP tem legitimidade para ACP em defesa do patrimônio público (Súmula 329/STJ)."
     }
    },
    {
     "id": "CPC-12-R1-05",
     "ponto": "DBA26-CPC-12",
     "tema": "MP e consumidor de serviço público",
     "assertiva": "O Ministério Público tem legitimidade ativa para atuar na defesa de direitos difusos, coletivos e individuais homogêneos dos consumidores, ainda que decorrentes da prestação de serviço público.",
     "gabarito": "C",
     "comentario": {
      "resumo": "**Súmula 601**/STJ.",
      "juris": [
       {
        "tribunal": "STJ",
        "fonte": "Súmula 601/STJ",
        "data": "07/02/2018",
        "texto": "O MP tem legitimidade ativa para a defesa de direitos difusos, coletivos e individuais homogêneos dos consumidores, ainda que decorrentes da prestação de serviço público."
       }
      ],
      "palavras_chave": [
       "MP",
       "individuais homogêneos",
       "Súmula 601"
      ],
      "aprofundamento": "A Súmula 601/STJ resolveu uma dúvida recorrente: quando o consumidor é usuário de serviço público, como energia, água ou telefonia, o MP pode atuar em sua defesa coletiva? A resposta é sim.\n\nO fundamento é que a relação entre usuário e prestador de serviço público também é de **consumo**, e o MP tem legitimidade para tutelar direitos difusos, coletivos e individuais homogêneos dos consumidores. Nos individuais homogêneos, a legitimidade se justifica pela relevância social, pela quantidade de pessoas atingidas.\n\nA banca costuma tentar afastar a legitimidade dizendo que, por se tratar de serviço público, a defesa caberia apenas às agências reguladoras ou aos próprios usuários. A súmula afirma o contrário.",
      "memorize": "MP defende consumidores, inclusive de serviço público, em direitos difusos, coletivos e individuais homogêneos (Súmula 601/STJ)."
     }
    },
    {
     "id": "CPC-12-R1-06",
     "ponto": "DBA26-CPC-12",
     "tema": "Continência entre ACPs",
     "assertiva": "Reconhecida a continência entre ação civil pública proposta na Justiça Federal e outra na Justiça estadual, ambas devem ser reunidas na Justiça estadual, por ser a de competência residual.",
     "gabarito": "E",
     "comentario": {
      "resumo": "Súmula 489/STJ: reúnem-se na **Justiça Federal**.",
      "juris": [
       {
        "tribunal": "STJ",
        "fonte": "Súmula 489/STJ",
        "data": "28/06/2012",
        "texto": "Reconhecida a continência, devem ser reunidas na Justiça Federal as ações civis públicas propostas nesta e na Justiça estadual."
       }
      ],
      "palavras_chave": [
       "continência",
       "Súmula 489"
      ],
      "correcao": {
       "erro": "Determina a reunião das ACPs conexas por continência na Justiça estadual.",
       "certo": "Reconhecida a continência, devem ser reunidas na Justiça Federal as ações civis públicas propostas nesta e na Justiça estadual (Súmula 489/STJ)."
      },
      "aprofundamento": "Na **continência**, uma ação tem objeto mais amplo que abrange o da outra, com as mesmas partes e causa de pedir. Para evitar decisões contraditórias, as ações devem ser reunidas. O problema surge quando uma tramita na Justiça Federal e a outra na estadual.\n\nA Súmula 489/STJ resolve: a reunião se faz na **Justiça Federal**. A razão é que a competência federal é fixada pela Constituição, em razão da pessoa ou da matéria, e não pode ser afastada. Já a competência estadual é residual e cede.\n\nA assertiva inverte o raciocínio, usando o caráter residual da Justiça estadual como argumento para atrair a causa. Na verdade, é justamente por ser residual que ela cede à competência federal.",
      "memorize": "ACPs em continência (federal + estadual): reúnem-se na Justiça Federal (Súmula 489/STJ)."
     }
    },
    {
     "id": "CPC-12-R1-07",
     "ponto": "DBA26-CPC-12",
     "tema": "MS contra lei em tese",
     "assertiva": "Cabe mandado de segurança contra lei em tese, desde que demonstrado o justo receio de sua aplicação.",
     "gabarito": "E",
     "comentario": {
      "resumo": "Súmula 266/STF: **não cabe** MS contra lei em tese (cabe contra o ato concreto que a aplica, ou contra lei de efeitos concretos).",
      "juris": [
       {
        "tribunal": "STF",
        "fonte": "Súmula 266/STF",
        "data": "13/12/1963",
        "texto": "Não cabe mandado de segurança contra lei em tese."
       }
      ],
      "palavras_chave": [
       "lei em tese",
       "Súmula 266"
      ],
      "correcao": {
       "erro": "Admite mandado de segurança contra lei em tese diante de justo receio de sua aplicação.",
       "certo": "Não cabe mandado de segurança contra lei em tese (Súmula 266/STF); cabe contra o ato concreto que a aplica ou contra lei de efeitos concretos."
      },
      "aprofundamento": "Lei em tese é norma geral e abstrata, que ainda não atingiu concretamente ninguém. O mandado de segurança protege direito líquido e certo contra **ato concreto** de autoridade. Contra lei em tese não há lesão individual a reparar, e o MS se transformaria num controle abstrato de constitucionalidade, que tem vias próprias.\n\nA Súmula 266/STF expressa essa ideia. O justo receio de aplicação da lei não basta; é preciso que haja um ato concreto que a aplique, ou ameaça concreta e iminente.\n\nA exceção é a lei de **efeitos concretos**, que, embora tenha forma de lei, produz efeitos diretos e imediatos sobre pessoas determinadas, funcionando materialmente como ato administrativo. Contra ela cabe o MS. A assertiva usa o \"justo receio\" para tentar justificar o cabimento.",
      "memorize": "MS contra lei em tese: não (Súmula 266/STF). Contra lei de efeitos concretos ou ato que aplica: sim."
     }
    },
    {
     "id": "CPC-12-R1-08",
     "ponto": "DBA26-CPC-12",
     "tema": "MS contra ato judicial",
     "assertiva": "Não cabe mandado de segurança contra ato judicial passível de recurso ou correição.",
     "gabarito": "C",
     "comentario": {
      "resumo": "**Súmula 267**/STF, hoje refletida no art. 5º, II, da Lei 12.016 (recurso com efeito suspensivo).",
      "juris": [
       {
        "tribunal": "STF",
        "fonte": "Súmula 267/STF",
        "data": "13/12/1963",
        "texto": "Não cabe mandado de segurança contra ato judicial passível de recurso ou correição."
       }
      ],
      "palavras_chave": [
       "ato judicial",
       "Súmula 267"
      ],
      "aprofundamento": "O mandado de segurança não é sucedâneo de recurso. Se a decisão judicial pode ser impugnada por recurso ou por correição, é por esse caminho que a parte deve ir. Admitir o MS nesses casos criaria um atalho que desorganizaria o sistema recursal.\n\nA Súmula 267/STF consagrou essa ideia, hoje refletida na Lei do MS, que veda o mandado contra decisão judicial da qual caiba recurso com efeito suspensivo.\n\nAdmite-se o MS contra ato judicial em situações excepcionais: decisão teratológica, manifestamente ilegal ou abusiva, sem recurso apto a evitar dano grave, ou impetrado por terceiro prejudicado que não foi parte. A banca costuma tratar o MS como alternativa livre ao recurso.",
      "memorize": "MS não substitui recurso: não cabe contra ato judicial recorrível (Súmula 267/STF)."
     }
    },
    {
     "id": "CPC-12-R1-09",
     "ponto": "DBA26-CPC-12",
     "tema": "MS e cobrança",
     "assertiva": "O mandado de segurança pode substituir a ação de cobrança quando o direito a valores pretéritos for líquido e certo.",
     "gabarito": "E",
     "comentario": {
      "resumo": "Súmula 269/STF: o MS **não é substitutivo de ação de cobrança**.",
      "juris": [
       {
        "tribunal": "STF",
        "fonte": "Súmula 269/STF",
        "data": "13/12/1963",
        "texto": "O mandado de segurança não é substitutivo de ação de cobrança."
       }
      ],
      "palavras_chave": [
       "ação de cobrança",
       "Súmula 269"
      ],
      "correcao": {
       "erro": "Admite que o mandado de segurança substitua a ação de cobrança de valores pretéritos.",
       "certo": "O mandado de segurança não é substitutivo de ação de cobrança (Súmula 269/STF); valores pretéritos se cobram pela via própria."
      },
      "aprofundamento": "O mandado de segurança é ação de natureza **mandamental**: a decisão ordena à autoridade que faça ou deixe de fazer algo. Ele não foi pensado para obter condenação ao pagamento de valores passados, que é função da ação de cobrança, com rito próprio e contraditório amplo.\n\nA Súmula 269/STF afirma que o MS não substitui a ação de cobrança. Os valores anteriores à impetração devem ser buscados pela via própria, administrativa ou judicial.\n\nOs efeitos patrimoniais da concessão da segurança alcançam apenas as parcelas a partir do ajuizamento. A assertiva tenta usar a liquidez e certeza do direito para justificar a cobrança de pretéritos, mas a natureza da ação continua sendo a de ordem, não a de condenação.",
      "memorize": "MS não é ação de cobrança (Súmula 269/STF)."
     }
    },
    {
     "id": "CPC-12-R1-10",
     "ponto": "DBA26-CPC-12",
     "tema": "Prazo decadencial do MS",
     "assertiva": "É constitucional lei que fixa o prazo de decadência para a impetração de mandado de segurança.",
     "gabarito": "C",
     "comentario": {
      "resumo": "**Súmula 632**/STF; o prazo de 120 dias do art. 23 foi mantido na ADI 4.296.",
      "juris": [
       {
        "tribunal": "STF",
        "fonte": "Súmula 632/STF",
        "data": "24/09/2003",
        "texto": "É constitucional lei que fixa o prazo de decadência para a impetração de mandado de segurança."
       }
      ],
      "palavras_chave": [
       "decadência",
       "Súmula 632"
      ],
      "aprofundamento": "O prazo decadencial do mandado de segurança foi questionado por limitar uma garantia constitucional. O STF afastou o argumento na Súmula 632: a Constituição garante o MS, mas não proíbe que a lei regule seu exercício, inclusive com prazo.\n\nO prazo não fere o direito material. Quem perde o prazo perde apenas a **via especial**, célere e privilegiada, e pode buscar o mesmo direito pelas vias ordinárias. Por isso não há supressão do acesso à justiça.\n\nO prazo de 120 dias do art. 23 foi mantido também na ADI 4.296. A banca costuma afirmar que o prazo seria inconstitucional por restringir garantia fundamental, ou que seria prescricional.",
      "memorize": "Prazo decadencial do MS é constitucional (Súmula 632/STF); perde-se a via, não o direito."
     }
    }
   ]
  },
  {
   "n": 2,
   "titulo": "Rodada 2 · Aprofundamento",
   "itens": [
    {
     "id": "CPC-1-R2-01",
     "ponto": "DBA26-CPC-1",
     "tema": "Solução consensual pelo Estado",
     "assertiva": "O Estado promoverá, obrigatoriamente e em todos os casos, a solução consensual dos conflitos.",
     "gabarito": "E",
     "comentario": {
      "resumo": "Art. 3º, § 2º: o Estado promoverá a solução consensual **sempre que possível**.",
      "lei": [
       {
        "lei": "L13105",
        "art": "3",
        "par": "",
        "inc": "",
        "rotulo": "CPC, art. 3º, § 2º",
        "texto": "O Estado promoverá, sempre que possível, a solução consensual dos conflitos."
       }
      ],
      "pegadinha": "\"Sempre que possível\" virou \"obrigatoriamente\".",
      "palavras_chave": [
       "sempre que possível",
       "solução consensual"
      ],
      "correcao": {
       "erro": "Torna obrigatória, em todos os casos, a promoção da solução consensual pelo Estado.",
       "certo": "O Estado promoverá, sempre que possível, a solução consensual dos conflitos."
      },
      "aprofundamento": "O dever do Estado de promover a solução consensual é uma **política pública**, e não uma imposição a qualquer custo. Há conflitos em que o acordo não é possível ou não é adequado: direitos indisponíveis que não admitem transação, situações de violência ou de grave desequilíbrio entre as partes, ou casos em que uma delas simplesmente não quer negociar.\n\nPor isso a lei usa a expressão \"**sempre que possível**\". O Estado deve estruturar centros de conciliação, capacitar mediadores e criar oportunidades de acordo, mas não pode forçar as partes a transigir.\n\nA banca transforma a política em obrigação absoluta, com expressões como \"obrigatoriamente\" e \"em todos os casos\". Termos absolutos em normas de estímulo costumam indicar erro.",
      "memorize": "Estado promove a solução consensual SEMPRE QUE POSSÍVEL, não obrigatoriamente."
     }
    },
    {
     "id": "CPC-1-R2-02",
     "ponto": "DBA26-CPC-1",
     "tema": "Evidência e contraditório diferido",
     "assertiva": "Admite-se decisão contra a parte sem sua oitiva prévia em todas as hipóteses de tutela da evidência, inclusive quando caracterizado o abuso do direito de defesa.",
     "gabarito": "E",
     "comentario": {
      "resumo": "Só a evidência dos incisos **II e III** do art. 311 dispensa a oitiva prévia. O **abuso do direito de defesa** (inciso I) pressupõe que o réu já se manifestou.",
      "lei": [
       {
        "lei": "L13105",
        "art": "9",
        "par": "",
        "inc": "",
        "rotulo": "CPC, art. 9º, par. ún., II",
        "texto": "II - às hipóteses de tutela da evidência previstas no art. 311, incisos II e III;"
       },
       {
        "lei": "L13105",
        "art": "311",
        "par": "",
        "inc": "",
        "rotulo": "CPC, art. 311, par. ún.",
        "texto": "Parágrafo único. Nas hipóteses dos incisos II e III, o juiz poderá decidir liminarmente."
       }
      ],
      "palavras_chave": [
       "tutela da evidência",
       "liminar",
       "abuso do direito de defesa"
      ],
      "correcao": {
       "erro": "Estende a dispensa de oitiva prévia a todas as hipóteses de tutela da evidência, inclusive o abuso do direito de defesa.",
       "certo": "Só as hipóteses de tutela da evidência dos incisos II e III do art. 311 admitem decisão liminar; o abuso do direito de defesa pressupõe a manifestação do réu."
      },
      "aprofundamento": "A tutela da evidência tem hipóteses de naturezas diferentes. Nas dos incisos II e III do art. 311, o direito se mostra evidente pela própria prova documental do autor, combinada com tese firmada ou com contrato de depósito. Não há o que esperar da defesa para concluir, e por isso o juiz pode decidir **liminarmente**.\n\nJá a hipótese de **abuso do direito de defesa** ou manifesto propósito protelatório pressupõe, por definição, que o réu já se defendeu e que essa defesa foi abusiva. Não faz sentido concedê-la sem ouvir o réu, porque é justamente a conduta dele no processo que a justifica.\n\nO mesmo raciocínio vale para a hipótese de prova documental sem dúvida razoável oposta pelo réu, que também depende de sua manifestação. A assertiva generaliza o contraditório diferido para todas as hipóteses.",
      "memorize": "Evidência liminar só nos incisos II e III; abuso de defesa exige que o réu já tenha se manifestado."
     }
    },
    {
     "id": "CPC-1-R2-03",
     "ponto": "DBA26-CPC-1",
     "tema": "Exclusões da ordem cronológica",
     "assertiva": "Estão excluídas da regra da ordem cronológica de conclusão as sentenças proferidas em audiência, homologatórias de acordo ou de improcedência liminar do pedido.",
     "gabarito": "C",
     "comentario": {
      "resumo": "É o art. 12, § 2º, I. Outras **exclusões**: julgamento em bloco de casos repetitivos, decisões dos arts. 485 e 932, embargos de declaração, agravo interno, preferências legais.",
      "lei": [
       {
        "lei": "L13105",
        "art": "12",
        "par": "",
        "inc": "",
        "rotulo": "CPC, art. 12, § 2º, I",
        "texto": "I - as sentenças proferidas em audiência, homologatórias de acordo ou de improcedência liminar do pedido;"
       }
      ],
      "palavras_chave": [
       "ordem cronológica",
       "exclusões"
      ],
      "aprofundamento": "A ordem cronológica busca impedir que o juiz escolha quais processos julgar primeiro. Mas há decisões que não fazem sentido entrar na fila, porque são simples, rápidas ou praticamente automáticas, e retardá-las só prejudicaria as partes.\n\nA **sentença proferida em audiência** é dada no momento, com as partes presentes. A **homologação de acordo** apenas chancela o que as partes já resolveram. A **improcedência liminar** encerra demanda que contraria precedente, sem citação. Em todos esses casos, esperar a ordem cronológica não teria justificativa.\n\nO dispositivo tem outras exclusões, como o julgamento em bloco de repetitivos, os embargos de declaração e o agravo interno. A banca costuma incluir na lista das exclusões decisões que não estão nela, ou negar alguma das previstas.",
      "memorize": "Fora da ordem cronológica: sentença em audiência, homologação de acordo, improcedência liminar, entre outras."
     }
    },
    {
     "id": "CPC-1-R2-04",
     "ponto": "DBA26-CPC-1",
     "tema": "Alcance da vedação à decisão surpresa",
     "assertiva": "A vedação à decisão surpresa aplica-se apenas ao juízo de primeiro grau, pois nos tribunais o relator pode decidir com base em fundamento não debatido.",
     "gabarito": "E",
     "comentario": {
      "resumo": "O art. 10 fala em **\"grau algum de jurisdição\"**; no tribunal, o art. 933 manda o relator intimar as partes sobre fato superveniente ou questão apreciável de ofício.",
      "lei": [
       {
        "lei": "L13105",
        "art": "10",
        "par": "",
        "inc": "",
        "rotulo": "CPC, art. 10",
        "texto": "em grau algum de jurisdição"
       },
       {
        "lei": "L13105",
        "art": "933",
        "par": "",
        "inc": "",
        "rotulo": "CPC, art. 933",
        "texto": "Se o relator constatar a ocorrência de fato superveniente à decisão recorrida ou a existência de questão apreciável de ofício ainda não examinada que devam ser considerados no julgamento do recurso, intimará as partes para que se manifestem no prazo de 5 (cinco) dias."
       }
      ],
      "palavras_chave": [
       "decisão surpresa",
       "tribunais"
      ],
      "correcao": {
       "erro": "Restringe a vedação à decisão surpresa ao primeiro grau, liberando o relator nos tribunais.",
       "certo": "O juiz não pode decidir, em grau algum de jurisdição, com base em fundamento não submetido às partes; no tribunal, o relator deve intimá-las para se manifestarem (art. 933)."
      },
      "aprofundamento": "A vedação à decisão surpresa é uma garantia do **contraditório** em todas as instâncias. Seria incoerente exigir que o juiz de primeiro grau ouvisse as partes antes de decidir por fundamento novo e permitir que o tribunal o fizesse livremente, justamente na fase em que a decisão tende a se tornar definitiva.\n\nO código reforça isso no art. 933: se o relator perceber fato superveniente ou questão apreciável de ofício ainda não examinada, deve intimar as partes para se manifestarem em 5 dias. Se a questão surgir durante a sessão de julgamento, o julgamento é suspenso para que as partes falem.\n\nA assertiva cria uma restrição que o texto legal expressamente afasta com a expressão \"em grau algum de jurisdição\".",
      "memorize": "Vedação à decisão surpresa vale em TODOS os graus; no tribunal, o relator intima as partes."
     }
    },
    {
     "id": "CPC-1-R2-05",
     "ponto": "DBA26-CPC-1",
     "tema": "Boa-fé processual",
     "assertiva": "O dever de comportar-se de acordo com a boa-fé restringe-se às partes, não alcançando terceiros intervenientes nem o juiz.",
     "gabarito": "E",
     "comentario": {
      "resumo": "Art. 5º: **aquele que de qualquer forma participa do processo** deve agir com boa-fé — boa-fé **objetiva**, para todos.",
      "lei": [
       {
        "lei": "L13105",
        "art": "5",
        "par": "",
        "inc": "",
        "rotulo": "CPC, art. 5º",
        "texto": "Aquele que de qualquer forma participa do processo deve comportar-se de acordo com a boa-fé."
       }
      ],
      "palavras_chave": [
       "boa-fé objetiva"
      ],
      "correcao": {
       "erro": "Restringe o dever de boa-fé às partes, excluindo terceiros intervenientes e o juiz.",
       "certo": "Aquele que de qualquer forma participa do processo, inclusive terceiros e o juiz, deve comportar-se de acordo com a boa-fé."
      },
      "aprofundamento": "A boa-fé processual é **objetiva**: não se pergunta se o sujeito tinha boa ou má intenção, mas se seu comportamento corresponde ao padrão de lealdade esperado. Ela impede condutas contraditórias, abuso de direitos processuais e surpresas desleais.\n\nO dever alcança **todos** que participam do processo: partes, advogados, terceiros intervenientes, peritos, testemunhas, membros do MP e o próprio juiz. A expressão legal \"aquele que de qualquer forma participa\" foi escolhida para não deixar ninguém de fora.\n\nA boa-fé também orienta a interpretação dos atos processuais, inclusive o pedido e a decisão judicial. A banca restringe o dever às partes, criando uma exclusão que o texto não autoriza.",
      "memorize": "Boa-fé objetiva: todos que de qualquer forma participam do processo."
     }
    },
    {
     "id": "CPC-1-R2-06",
     "ponto": "DBA26-CPC-1",
     "tema": "Isonomia processual",
     "assertiva": "É assegurada às partes paridade de tratamento em relação ao exercício de direitos e faculdades processuais, competindo ao juiz zelar pelo efetivo contraditório.",
     "gabarito": "C",
     "comentario": {
      "resumo": "Art. 7º: **paridade de armas** e dever judicial de zelar pelo **contraditório efetivo**.",
      "lei": [
       {
        "lei": "L13105",
        "art": "7",
        "par": "",
        "inc": "",
        "rotulo": "CPC, art. 7º",
        "texto": "É assegurada às partes paridade de tratamento em relação ao exercício de direitos e faculdades processuais, aos meios de defesa, aos ônus, aos deveres e à aplicação de sanções processuais, competindo ao juiz zelar pelo efetivo contraditório."
       }
      ],
      "palavras_chave": [
       "paridade de armas",
       "contraditório efetivo"
      ],
      "aprofundamento": "A **paridade de armas** é a dimensão processual da isonomia. As partes devem ter as mesmas oportunidades de exercer direitos e faculdades, de se defender, de cumprir ônus e deveres, e devem estar sujeitas às mesmas sanções.\n\nIgualdade, porém, não significa tratamento idêntico em qualquer situação. Quando há desigualdade real, a lei pode criar regras diferenciadas para equilibrar, como o prazo em dobro para a Defensoria ou a inversão do ônus da prova. É a isonomia **material**.\n\nO juiz tem o dever de zelar pelo **efetivo contraditório**: não basta abrir oportunidade formal, é preciso que ela seja real. A banca costuma dizer que a isonomia impede qualquer tratamento diferenciado, o que confunde igualdade formal e material.",
      "memorize": "Paridade de armas + dever do juiz de zelar pelo contraditório efetivo."
     }
    },
    {
     "id": "CPC-1-R2-07",
     "ponto": "DBA26-CPC-1",
     "tema": "Segredo de justiça",
     "assertiva": "Nos casos de segredo de justiça, pode ser autorizada a presença somente das partes, de seus advogados, de defensores públicos ou do Ministério Público.",
     "gabarito": "C",
     "comentario": {
      "resumo": "Art. 11, parágrafo único: a **publicidade restrita** não afasta as partes nem os seus representantes.",
      "lei": [
       {
        "lei": "L13105",
        "art": "11",
        "par": "",
        "inc": "",
        "rotulo": "CPC, art. 11, par. ún.",
        "texto": "Nos casos de segredo de justiça, pode ser autorizada a presença somente das partes, de seus advogados, de defensores públicos ou do Ministério Público."
       }
      ],
      "palavras_chave": [
       "segredo de justiça",
       "publicidade restrita"
      ],
      "aprofundamento": "O segredo de justiça é exceção à publicidade, aplicada quando a exposição do processo prejudicaria a intimidade das partes ou o interesse público, como em ações de família ou processos com dados sensíveis.\n\nMas a restrição atinge apenas o **público externo**. As partes, seus advogados, os defensores públicos e o MP continuam tendo acesso pleno, porque sem isso não haveria contraditório nem fiscalização. O segredo protege as partes da curiosidade alheia, não as exclui do próprio processo.\n\nO terceiro que demonstrar interesse jurídico pode pedir ao juiz certidão do dispositivo da sentença e de inventário e partilha. A banca costuma dizer que o segredo afasta também o MP ou os advogados, o que contraria o texto.",
      "memorize": "Segredo de justiça: restrito a partes, advogados, defensores e MP."
     }
    },
    {
     "id": "CPC-1-R2-08",
     "ponto": "DBA26-CPC-1",
     "tema": "Supletividade — processo penal",
     "assertiva": "O art. 15 do CPC prevê expressamente a aplicação supletiva e subsidiária de suas normas ao processo penal.",
     "gabarito": "E",
     "comentario": {
      "resumo": "O art. 15 só cita processos **eleitorais, trabalhistas e administrativos**. No processo penal a ponte é o art. 3º do CPP (analogia).",
      "lei": [
       {
        "lei": "L13105",
        "art": "15",
        "par": "",
        "inc": "",
        "rotulo": "CPC, art. 15",
        "texto": "processos eleitorais, trabalhistas ou administrativos"
       }
      ],
      "pegadinha": "Banca inclui \"penais\" na lista do art. 15.",
      "palavras_chave": [
       "art. 15",
       "processo penal"
      ],
      "correcao": {
       "erro": "Inclui o processo penal entre os ramos de aplicação supletiva e subsidiária expressamente previstos no art. 15 do CPC.",
       "certo": "O art. 15 do CPC prevê aplicação supletiva e subsidiária apenas aos processos eleitorais, trabalhistas e administrativos; no processo penal, a ponte é o art. 3º do CPP."
      },
      "aprofundamento": "O art. 15 lista apenas três ramos para a aplicação supletiva e subsidiária do CPC: **eleitoral, trabalhista e administrativo**. O processo penal não está nessa lista.\n\nIsso não significa que o CPC nunca se aplique ao processo penal. A ponte é feita pelo próprio CPP, que, em seu art. 3º, admite interpretação extensiva, aplicação analógica e o suplemento dos princípios gerais de direito. É por essa via que institutos do CPC são usados no processo penal, quando compatíveis.\n\nA pegadinha é sutil: a assertiva fala em previsão \"expressa\" no art. 15 do CPC. A previsão expressa não existe; a aplicação ao processo penal decorre de outra norma.",
      "memorize": "Art. 15 do CPC: eleitoral, trabalhista e administrativo. Penal fica de fora (vai pelo art. 3º do CPP)."
     }
    },
    {
     "id": "CPC-2-R2-01",
     "ponto": "DBA26-CPC-2",
     "tema": "Risco de decisões conflitantes",
     "assertiva": "Serão reunidos para julgamento conjunto os processos que possam gerar risco de prolação de decisões conflitantes ou contraditórias caso decididos separadamente, mesmo sem conexão entre eles.",
     "gabarito": "C",
     "comentario": {
      "resumo": "Art. 55, § 3º: o CPC/2015 permite a reunião **mesmo sem conexão**, para evitar decisões conflitantes.",
      "lei": [
       {
        "lei": "L13105",
        "art": "55",
        "par": "",
        "inc": "",
        "rotulo": "CPC, art. 55, § 3º",
        "texto": "Serão reunidos para julgamento conjunto os processos que possam gerar risco de prolação de decisões conflitantes ou contraditórias caso decididos separadamente, mesmo sem conexão entre eles."
       }
      ],
      "palavras_chave": [
       "conexão",
       "decisões conflitantes"
      ],
      "aprofundamento": "Tradicionalmente, a reunião de processos dependia de **conexão** (mesmo pedido ou mesma causa de pedir) ou de continência. O CPC atual ampliou essa possibilidade com um critério funcional: o **risco de decisões conflitantes**.\n\nHá casos em que as ações não têm o mesmo pedido nem a mesma causa de pedir, mas a decisão de uma pode contradizer a outra. Pense numa ação de despejo e numa ação revisional sobre o mesmo contrato. Julgá-las separadamente poderia gerar resultados incompatíveis.\n\nA norma privilegia a **coerência** e a segurança jurídica sobre o rigor técnico dos conceitos de conexão. A banca costuma exigir conexão como requisito indispensável para a reunião, o que o código expressamente dispensa.",
      "memorize": "Risco de decisões conflitantes justifica reunir processos, mesmo sem conexão."
     }
    },
    {
     "id": "CPC-2-R2-02",
     "ponto": "DBA26-CPC-2",
     "tema": "Conexão e processo já sentenciado",
     "assertiva": "Os processos de ações conexas devem ser reunidos para decisão conjunta ainda que um deles já tenha sido sentenciado.",
     "gabarito": "E",
     "comentario": {
      "resumo": "Art. 55, § 1º: reúnem-se **salvo se um deles já houver sido sentenciado** — no mesmo sentido a Súmula 235/STJ.",
      "lei": [
       {
        "lei": "L13105",
        "art": "55",
        "par": "",
        "inc": "",
        "rotulo": "CPC, art. 55, § 1º",
        "texto": "Os processos de ações conexas serão reunidos para decisão conjunta, salvo se um deles já houver sido sentenciado."
       }
      ],
      "juris": [
       {
        "tribunal": "STJ",
        "fonte": "Súmula 235/STJ",
        "data": "01/02/2000",
        "texto": "A conexão não determina a reunião dos processos, se um deles já foi julgado."
       }
      ],
      "palavras_chave": [
       "conexão",
       "sentenciado"
      ],
      "correcao": {
       "erro": "Determina a reunião de ações conexas mesmo que uma delas já tenha sido sentenciada.",
       "certo": "Os processos de ações conexas serão reunidos para decisão conjunta, salvo se um deles já houver sido sentenciado (Súmula 235/STJ)."
      },
      "aprofundamento": "A reunião de processos conexos existe para que eles sejam **julgados juntos**, evitando decisões contraditórias e economizando atos. Se um deles já foi sentenciado, essa finalidade se perde: não há mais como julgá-los conjuntamente.\n\nPor isso a lei ressalva expressamente o caso em que um dos processos já foi sentenciado, e a Súmula 235/STJ caminha no mesmo sentido. O processo pendente segue seu curso; eventual incompatibilidade será tratada pelos meios próprios, como recursos.\n\nNote que o marco é a **sentença**, e não o trânsito em julgado. Basta que um dos processos tenha sido julgado em primeiro grau. A banca costuma afastar essa ressalva ou colocá-la no trânsito em julgado.",
      "memorize": "Conexão não reúne processo já sentenciado (Súmula 235/STJ)."
     }
    },
    {
     "id": "CPC-2-R2-03",
     "ponto": "DBA26-CPC-2",
     "tema": "Prevenção",
     "assertiva": "No CPC vigente, é a citação válida que torna prevento o juízo.",
     "gabarito": "E",
     "comentario": {
      "resumo": "Art. 59: **o registro ou a distribuição da petição inicial** torna prevento o juízo. A citação válida induz litispendência (art. 240), não prevenção.",
      "lei": [
       {
        "lei": "L13105",
        "art": "59",
        "par": "",
        "inc": "",
        "rotulo": "CPC, art. 59",
        "texto": "O registro ou a distribuição da petição inicial torna prevento o juízo."
       }
      ],
      "palavras_chave": [
       "prevenção",
       "distribuição"
      ],
      "correcao": {
       "erro": "Atribui à citação válida o efeito de tornar prevento o juízo.",
       "certo": "O registro ou a distribuição da petição inicial torna prevento o juízo; a citação válida induz litispendência, não prevenção."
      },
      "aprofundamento": "A **prevenção** define qual juízo, entre vários igualmente competentes, fica responsável por julgar as ações conexas. O código atual adotou um critério objetivo e simples: o registro ou a distribuição da petição inicial.\n\nNo sistema revogado, havia critérios diferentes conforme o caso, ora o despacho que ordenava a citação, ora a citação válida, o que gerava confusão. O CPC unificou o marco, o que facilita a identificação do juízo prevento.\n\nA citação válida continua relevante, mas para outros efeitos: induz **litispendência**, torna litigiosa a coisa e constitui o devedor em mora. A banca mistura esses efeitos com a prevenção.",
      "memorize": "Prevenção: registro ou distribuição da inicial. Citação válida: litispendência."
     }
    },
    {
     "id": "CPC-2-R2-04",
     "ponto": "DBA26-CPC-2",
     "tema": "Intervenção da União",
     "assertiva": "Intervindo a União no processo que tramita na Justiça estadual, os autos serão remetidos à Justiça Federal, a quem compete decidir sobre a existência de interesse jurídico que justifique a presença do ente federal.",
     "gabarito": "C",
     "comentario": {
      "resumo": "Art. 45 + Súmula 150/STJ: quem decide se há interesse da União é a **Justiça Federal**. Exceções no próprio art. 45: recuperação judicial, falência, insolvência, acidente de trabalho, Justiça Eleitoral e do Trabalho.",
      "excecoes": [
       "Recuperação judicial, falência, insolvência civil e acidente de trabalho (art. 45, I)",
       "Causas da Justiça Eleitoral e da Justiça do Trabalho (art. 45, II)"
      ],
      "lei": [
       {
        "lei": "L13105",
        "art": "45",
        "par": "",
        "inc": "",
        "rotulo": "CPC, art. 45",
        "texto": "Tramitando o processo perante outro juízo, os autos serão remetidos ao juízo federal competente se nele intervier a União, suas empresas públicas, entidades autárquicas e fundações, ou conselho de fiscalização de atividade profissional, na qualidade de parte ou de terceiro interveniente"
       }
      ],
      "juris": [
       {
        "tribunal": "STJ",
        "fonte": "Súmula 150/STJ",
        "data": "07/02/1996",
        "texto": "Compete à Justiça Federal decidir sobre a existência de interesse jurídico que justifique a presença da União, suas autarquias ou empresas públicas."
       }
      ],
      "palavras_chave": [
       "Justiça Federal",
       "interesse da União"
      ],
      "aprofundamento": "A competência da Justiça Federal é definida pela Constituição em razão da pessoa: causas em que a União, suas autarquias, fundações e empresas públicas forem partes ou interessadas. Quando um desses entes intervém em processo na Justiça estadual, os autos devem ir à Justiça Federal.\n\nQuem decide se o interesse do ente federal realmente existe é a **Justiça Federal**, conforme a Súmula 150/STJ. O juiz estadual não pode negar esse interesse e manter a causa. Se o juiz federal afastar o interesse, devolve os autos sem suscitar conflito.\n\nA própria lei traz exceções em que o processo não se desloca, mesmo com a intervenção da União: recuperação judicial, falência, insolvência civil, acidente de trabalho e causas das Justiças Eleitoral e do Trabalho.",
      "memorize": "União intervém: autos à Justiça Federal, que decide sobre o interesse (Súmula 150/STJ)."
     }
    },
    {
     "id": "CPC-2-R2-05",
     "ponto": "DBA26-CPC-2",
     "tema": "Foro do alimentando",
     "assertiva": "É competente o foro de domicílio ou residência do alimentando para a ação em que se pedem alimentos.",
     "gabarito": "C",
     "comentario": {
      "resumo": "Art. 53, II: **foro privilegiado do alimentando** (parte presumidamente vulnerável).",
      "lei": [
       {
        "lei": "L13105",
        "art": "53",
        "par": "",
        "inc": "",
        "rotulo": "CPC, art. 53, II",
        "texto": "de domicílio ou residência do alimentando, para a ação em que se pedem alimentos;"
       }
      ],
      "palavras_chave": [
       "alimentos",
       "foro do alimentando"
      ],
      "aprofundamento": "O foro do alimentando é uma regra de **proteção da parte vulnerável**. Quem pede alimentos normalmente depende deles para sobreviver e não tem condições de litigar em outra cidade, onde mora o alimentante.\n\nA regra afasta o foro geral do domicílio do réu. Ela vale para a ação em que se pedem alimentos e, pela Súmula do STJ, também para a investigação de paternidade cumulada com alimentos.\n\nTrata-se de competência territorial, portanto relativa, estabelecida em favor do alimentando. A banca costuma aplicar a regra geral do domicílio do réu ou dizer que o foro seria o do domicílio do alimentante.",
      "memorize": "Ação de alimentos: foro do domicílio ou residência do alimentando."
     }
    },
    {
     "id": "CPC-2-R2-06",
     "ponto": "DBA26-CPC-2",
     "tema": "Cláusula de eleição abusiva",
     "assertiva": "A cláusula de eleição de foro abusiva pode ser reputada ineficaz de ofício pelo juiz a qualquer tempo, ainda que o réu, citado, não a tenha impugnado na contestação.",
     "gabarito": "E",
     "comentario": {
      "resumo": "De ofício, só **antes da citação** (art. 63, § 3º). Citado o réu, cabe a ele alegar na contestação, **sob pena de preclusão** (§ 4º).",
      "lei": [
       {
        "lei": "L13105",
        "art": "63",
        "par": "",
        "inc": "",
        "rotulo": "CPC, art. 63, § 4º",
        "texto": "Citado, incumbe ao réu alegar a abusividade da cláusula de eleição de foro na contestação, sob pena de preclusão."
       }
      ],
      "palavras_chave": [
       "foro de eleição",
       "abusividade",
       "preclusão"
      ],
      "correcao": {
       "erro": "Permite ao juiz declarar de ofício, a qualquer tempo, a ineficácia da cláusula de eleição abusiva, mesmo depois da citação.",
       "certo": "O juiz pode reputar ineficaz de ofício a cláusula abusiva apenas antes da citação; citado, cabe ao réu alegar a abusividade na contestação, sob pena de preclusão."
      },
      "aprofundamento": "O controle da cláusula de eleição de foro abusiva busca proteger a parte vulnerável, normalmente em contratos de adesão. O juiz pode agir de ofício, mas há um limite temporal: **antes da citação**.\n\nDepois de citado, o réu passa a ter o ônus de alegar a abusividade na contestação. Se não o fizer, ocorre **preclusão**: a cláusula prevalece, porque a competência é relativa e se prorroga. A lógica é que, citado, o réu tem condições de defender seus próprios interesses, e sua inércia é interpretada como aceitação.\n\nA assertiva elimina o limite temporal, criando um controle de ofício a qualquer tempo. É o tipo de troca em que a banca apaga o marco processual que delimita o poder do juiz.",
      "memorize": "Cláusula de foro abusiva: de ofício só antes da citação; depois, o réu alega na contestação ou preclui."
     }
    },
    {
     "id": "CPC-2-R2-07",
     "ponto": "DBA26-CPC-2",
     "tema": "Efeitos da decisão do juízo incompetente",
     "assertiva": "Reconhecida a incompetência, são nulos todos os atos decisórios praticados pelo juízo incompetente.",
     "gabarito": "E",
     "comentario": {
      "resumo": "Art. 64, § 4º: **conservam-se os efeitos** da decisão do juízo incompetente até que outra seja proferida pelo competente, salvo decisão judicial em sentido contrário (translatio iudicii).",
      "lei": [
       {
        "lei": "L13105",
        "art": "64",
        "par": "",
        "inc": "",
        "rotulo": "CPC, art. 64, § 4º",
        "texto": "Salvo decisão judicial em sentido contrário, conservar-se-ão os efeitos de decisão proferida pelo juízo incompetente até que outra seja proferida, se for o caso, pelo juízo competente."
       }
      ],
      "pegadinha": "\"Nulos os atos decisórios\" era a regra do CPC/1973.",
      "palavras_chave": [
       "translatio iudicii",
       "conservação dos efeitos"
      ],
      "correcao": {
       "erro": "Declara nulos todos os atos decisórios do juízo incompetente.",
       "certo": "Salvo decisão judicial em sentido contrário, conservam-se os efeitos das decisões do juízo incompetente até que outra seja proferida pelo juízo competente."
      },
      "aprofundamento": "O CPC atual adotou a ideia de **translatio iudicii**: reconhecida a incompetência, o processo é transferido ao juízo competente com o aproveitamento máximo do que já foi feito. Anular tudo seria desperdiçar atos válidos e punir a parte pelo erro na escolha do juízo.\n\nPor isso os efeitos das decisões do juízo incompetente são **conservados** até que o juízo competente decida mantê-las ou revogá-las. Uma liminar concedida pelo juízo incompetente, por exemplo, continua valendo até nova decisão.\n\nA ressalva é a decisão judicial em sentido contrário: o próprio juiz pode afastar essa conservação. A assertiva reproduz a regra do código revogado, que considerava nulos os atos decisórios.",
      "exemplo": "Uma liminar é concedida por juízo que depois se declara incompetente. Ela continua produzindo efeitos até que o juízo competente a reexamine.",
      "memorize": "Incompetência: decisões conservam efeitos até o juízo competente decidir (translatio iudicii)."
     }
    },
    {
     "id": "CPC-2-R2-08",
     "ponto": "DBA26-CPC-2",
     "tema": "Estado ou DF como réu",
     "assertiva": "Se o Estado for o demandado, a ação poderá ser proposta no foro de domicílio do autor, no de ocorrência do ato ou fato que originou a demanda, no de situação da coisa ou na capital do respectivo ente federado.",
     "gabarito": "C",
     "comentario": {
      "resumo": "Art. 52, par. ún.: **foros concorrentes** à escolha do autor quando Estado ou DF é réu.",
      "lei": [
       {
        "lei": "L13105",
        "art": "52",
        "par": "",
        "inc": "",
        "rotulo": "CPC, art. 52, par. ún.",
        "texto": "Se Estado ou o Distrito Federal for o demandado, a ação poderá ser proposta no foro de domicílio do autor, no de ocorrência do ato ou fato que originou a demanda, no de situação da coisa ou na capital do respectivo ente federado."
       }
      ],
      "palavras_chave": [
       "foros concorrentes",
       "Fazenda Pública"
      ],
      "aprofundamento": "Quando o Estado ou o DF é réu, a lei cria **foros concorrentes** à escolha do autor. A ideia é não impor ao cidadão o ônus de litigar sempre na capital, onde fica a sede do ente, o que seria desproporcional diante da estrutura que o poder público tem em todo o território.\n\nO autor pode escolher entre seu domicílio, o local do ato ou fato que originou a demanda, o local da coisa ou a capital do ente. É uma regra de facilitação do acesso à justiça.\n\nQuando o Estado ou DF é autor, a regra é a geral: a ação é proposta no domicílio do réu. A banca costuma dizer que a ação contra o Estado deve ser proposta obrigatoriamente na capital, o que elimina a escolha do autor.",
      "memorize": "Estado ou DF réu: autor escolhe entre seu domicílio, local do fato, da coisa ou a capital."
     }
    },
    {
     "id": "CPC-2-R2-09",
     "ponto": "DBA26-CPC-2",
     "tema": "Carta rogatória",
     "assertiva": "Na carta rogatória, a defesa restringe-se à discussão quanto ao atendimento dos requisitos para que o pronunciamento judicial estrangeiro produza efeitos no Brasil, vedada a revisão do mérito.",
     "gabarito": "C",
     "comentario": {
      "resumo": "Art. 36, §§ 1º e 2º: juízo de **delibação** — sem revisão do mérito.",
      "lei": [
       {
        "lei": "L13105",
        "art": "36",
        "par": "",
        "inc": "",
        "rotulo": "CPC, art. 36, § 1º",
        "texto": "A defesa restringir-se-á à discussão quanto ao atendimento dos requisitos para que o pronunciamento judicial estrangeiro produza efeitos no Brasil."
       }
      ],
      "palavras_chave": [
       "carta rogatória",
       "delibação"
      ],
      "aprofundamento": "A carta rogatória é instrumento de **cooperação jurídica internacional**: um juízo estrangeiro pede ao Brasil que pratique um ato, como uma citação ou a produção de prova. Para que esse ato produza efeito aqui, há um controle chamado **juízo de delibação**.\n\nNesse controle, não se reexamina se a decisão estrangeira está certa ou errada. Verificam-se apenas os requisitos formais e a compatibilidade com a ordem pública brasileira. Rever o mérito seria desrespeitar a soberania do Estado estrangeiro e inviabilizar a cooperação.\n\nPor isso a defesa é restrita ao atendimento dos requisitos. A banca costuma dizer que o réu pode discutir o mérito da causa na carta rogatória, o que contraria o sistema de delibação.",
      "memorize": "Carta rogatória: juízo de delibação, sem revisão do mérito."
     }
    },
    {
     "id": "CPC-3-R2-01",
     "ponto": "DBA26-CPC-3",
     "tema": "Outorga conjugal",
     "assertiva": "O cônjuge necessitará do consentimento do outro para propor ação que verse sobre direito real imobiliário, salvo quando casados sob o regime de separação absoluta de bens.",
     "gabarito": "C",
     "comentario": {
      "resumo": "**Art. 73**, caput. Vale também para união estável comprovada nos autos (§ 3º).",
      "lei": [
       {
        "lei": "L13105",
        "art": "73",
        "par": "",
        "inc": "",
        "rotulo": "CPC, art. 73",
        "texto": "O cônjuge necessitará do consentimento do outro para propor ação que verse sobre direito real imobiliário, salvo quando casados sob o regime de separação absoluta de bens."
       }
      ],
      "palavras_chave": [
       "outorga conjugal",
       "direito real imobiliário"
      ],
      "aprofundamento": "A **outorga conjugal** para ações sobre direito real imobiliário protege o patrimônio da família. Um cônjuge poderia, por meio de uma ação mal conduzida ou de um acordo desvantajoso, comprometer imóvel que interessa a ambos. Exigir o consentimento do outro evita esse risco.\n\nA exceção é o regime de **separação absoluta de bens**: nele, cada cônjuge tem patrimônio próprio e independente, e não há interesse comum que justifique a exigência. A regra se estende à união estável comprovada nos autos.\n\nSe um cônjuge recusar o consentimento sem justo motivo, ou estiver impossibilitado de dá-lo, o juiz pode supri-lo. A falta de consentimento não suprida invalida o processo. A banca costuma estender a exigência a ações sobre direito pessoal ou retirar a exceção da separação absoluta.",
      "memorize": "Ação sobre direito real imobiliário: consentimento do cônjuge, salvo separação absoluta."
     }
    },
    {
     "id": "CPC-3-R2-02",
     "ponto": "DBA26-CPC-3",
     "tema": "Amicus curiae — recursos",
     "assertiva": "O amicus curiae pode interpor qualquer recurso contra as decisões proferidas no processo em que intervém.",
     "gabarito": "E",
     "comentario": {
      "resumo": "Art. 138, § 1º: só **embargos de declaração** e recurso contra a decisão que julga o **IRDR** (§ 3º). A decisão que o admite ou inadmite é irrecorrível.",
      "excecoes": [
       "Embargos de declaração (art. 138, § 1º)",
       "Recurso contra decisão que julga o IRDR (art. 138, § 3º)"
      ],
      "lei": [
       {
        "lei": "L13105",
        "art": "138",
        "par": "",
        "inc": "",
        "rotulo": "CPC, art. 138, § 1º",
        "texto": "A intervenção de que trata o caput não implica alteração de competência nem autoriza a interposição de recursos, ressalvadas a oposição de embargos de declaração"
       }
      ],
      "palavras_chave": [
       "amicus curiae",
       "recursos"
      ],
      "correcao": {
       "erro": "Admite que o amicus curiae interponha qualquer recurso no processo.",
       "certo": "O amicus curiae não pode interpor recursos, ressalvados os embargos de declaração e o recurso contra a decisão que julga o IRDR."
      },
      "aprofundamento": "O **amicus curiae** ingressa no processo para fornecer elementos técnicos, sociais ou jurídicos que ajudem o juiz a decidir causas relevantes ou de repercussão social. Ele não é parte e não defende interesse próprio na vitória de um dos lados; seu papel é qualificar o debate.\n\nPor isso seus poderes são limitados. Ele não pode interpor recursos em geral, porque isso o transformaria em parte. As exceções são os **embargos de declaração**, que servem para esclarecer a decisão, e o recurso contra a decisão que julga o **IRDR**, em que a tese fixada afeta toda a coletividade. A decisão que admite ou inadmite o amicus é irrecorrível.\n\nA banca amplia os poderes recursais com expressões como \"qualquer recurso\".",
      "memorize": "Amicus curiae recorre só por embargos de declaração e contra o julgamento do IRDR."
     }
    },
    {
     "id": "CPC-3-R2-03",
     "ponto": "DBA26-CPC-3",
     "tema": "Chamamento ao processo",
     "assertiva": "É admissível o chamamento ao processo, requerido pelo réu, dos demais devedores solidários quando o credor exigir de um ou de alguns o pagamento da dívida comum.",
     "gabarito": "C",
     "comentario": {
      "resumo": "Art. 130, III. Também: o **afiançado** (I) e os **demais fiadores** (II).",
      "lei": [
       {
        "lei": "L13105",
        "art": "130",
        "par": "",
        "inc": "",
        "rotulo": "CPC, art. 130, III",
        "texto": "dos demais devedores solidários, quando o credor exigir de um ou de alguns o pagamento da dívida comum."
       }
      ],
      "palavras_chave": [
       "chamamento ao processo",
       "solidariedade"
      ],
      "aprofundamento": "O **chamamento ao processo** é intervenção provocada pelo réu para trazer ao processo outros coobrigados. A ideia é que todos os responsáveis pela dívida respondam juntos e que a sentença sirva de título para quem pagar cobrar dos demais sua parte.\n\nAs hipóteses são três: o **afiançado**, na ação contra o fiador; os **demais fiadores**, quando só um ou alguns forem demandados; e os **demais devedores solidários**, quando o credor exigir de um ou de alguns o pagamento da dívida comum.\n\nA fronteira com a denunciação da lide é importante. No chamamento, o chamado é **devedor do autor** junto com o réu. Na denunciação, o denunciado tem relação apenas com o denunciante, que pretende reaver dele o que perder. A banca costuma trocar esses institutos.",
      "memorize": "Chamamento: réu traz afiançado, outros fiadores ou outros devedores solidários."
     }
    },
    {
     "id": "CPC-3-R2-04",
     "ponto": "DBA26-CPC-3",
     "tema": "IDPJ — citação do sócio",
     "assertiva": "Instaurado o incidente de desconsideração, o sócio ou a pessoa jurídica será citado para manifestar-se e requerer as provas cabíveis no prazo de 5 dias.",
     "gabarito": "E",
     "comentario": {
      "resumo": "Art. 135: o prazo é de **15 dias**. Requerida na inicial, dispensa-se o incidente (art. 134, § 2º); instaurado, **suspende** o processo (§ 3º).",
      "lei": [
       {
        "lei": "L13105",
        "art": "135",
        "par": "",
        "inc": "",
        "rotulo": "CPC, art. 135",
        "texto": "Instaurado o incidente, o sócio ou a pessoa jurídica será citado para manifestar-se e requerer as provas cabíveis no prazo de 15 (quinze) dias."
       }
      ],
      "palavras_chave": [
       "IDPJ",
       "15 dias"
      ],
      "correcao": {
       "erro": "Fixa em 5 dias o prazo para o sócio ou a pessoa jurídica se manifestar no incidente de desconsideração.",
       "certo": "Instaurado o incidente, o sócio ou a pessoa jurídica será citado para manifestar-se e requerer as provas cabíveis no prazo de 15 dias."
      },
      "aprofundamento": "O incidente de desconsideração busca alcançar o patrimônio de quem não era parte originária. Como isso é grave, a lei garante ao sócio ou à pessoa jurídica um **contraditório pleno**, com prazo adequado para se defender e requerer provas.\n\nO prazo é de 15 dias, coerente com a regra geral dos prazos de defesa. Instaurado o incidente, o processo principal fica **suspenso**, para que não se pratiquem atos de constrição antes da decisão. Se a desconsideração for pedida já na petição inicial, o incidente é dispensado e o sócio é citado como réu.\n\nA banca reduz o prazo para 5 dias, que lembra o prazo supletivo. Lembre que, sendo defesa contra a desconsideração, o prazo é o mesmo da contestação.",
      "memorize": "IDPJ: citação para defesa em 15 dias; suspende o processo; dispensado se pedido na inicial."
     }
    },
    {
     "id": "CPC-3-R2-05",
     "ponto": "DBA26-CPC-3",
     "tema": "Honorários por equidade",
     "assertiva": "Quando o valor da condenação ou da causa for muito elevado, o juiz pode fixar honorários por apreciação equitativa para evitar remuneração excessiva.",
     "gabarito": "E",
     "comentario": {
      "resumo": "Tema 1.076/STJ: equidade é **vedada** quando os valores são elevados; aplica-se a faixa dos §§ 2º ou 3º. Equidade só se o proveito for **inestimável ou irrisório** ou o valor da causa muito baixo (§ 8º).",
      "lei": [
       {
        "lei": "L13105",
        "art": "85",
        "par": "",
        "inc": "",
        "rotulo": "CPC, art. 85, § 8º",
        "texto": "Nas causas em que for inestimável ou irrisório o proveito econômico ou, ainda, quando o valor da causa for muito baixo, o juiz fixará o valor dos honorários por apreciação equitativa, observando o disposto nos incisos do § 2º."
       }
      ],
      "juris": [
       {
        "tribunal": "STJ",
        "fonte": "Tema 1.076/STJ — REsp 1.850.512/SP e outros",
        "data": "16/03/2022",
        "texto": "A fixação de honorários por equidade não é permitida quando forem elevados a condenação, o proveito econômico ou o valor da causa; só cabe se o proveito for inestimável ou irrisório, ou o valor da causa muito baixo."
       }
      ],
      "palavras_chave": [
       "equidade",
       "honorários",
       "Tema 1.076"
      ],
      "correcao": {
       "erro": "Permite ao juiz fixar honorários por equidade quando o valor da condenação ou da causa for muito elevado.",
       "certo": "A equidade é vedada quando os valores são elevados (Tema 1.076/STJ); aplica-se a faixa dos §§ 2º ou 3º, e a equidade só cabe se o proveito for inestimável ou irrisório ou o valor da causa muito baixo."
      },
      "aprofundamento": "A apreciação equitativa permite ao juiz fixar honorários sem a faixa percentual, por critério de razoabilidade. Ela foi pensada para casos em que o percentual levaria a valores ínfimos: proveito **inestimável ou irrisório**, ou valor da causa muito baixo.\n\nNa prática, muitos juízes passaram a usar a equidade também para **reduzir** honorários em causas de valor elevado. O STJ, no **Tema 1.076**, vedou essa prática: quando a condenação, o proveito ou o valor da causa forem elevados, aplicam-se obrigatoriamente as faixas percentuais dos §§ 2º ou 3º.\n\nA lógica é a segurança jurídica e a valorização do trabalho do advogado: a equidade serve para elevar honorários ínfimos, não para reduzir honorários altos. A banca apresenta a redução por equidade como permitida.",
      "memorize": "Honorários por equidade: só para proveito inestimável/irrisório ou causa de valor muito baixo (Tema 1.076/STJ)."
     }
    },
    {
     "id": "CPC-3-R2-06",
     "ponto": "DBA26-CPC-3",
     "tema": "Prazo em dobro da Advocacia Pública",
     "assertiva": "A União, os Estados, o DF, os Municípios e suas autarquias e fundações gozam de prazo em dobro para todas as manifestações processuais, inclusive quando a lei estabelecer, de forma expressa, prazo próprio para o ente público.",
     "gabarito": "E",
     "comentario": {
      "resumo": "Art. 183, § 2º: **não** se aplica o benefício quando a lei estabelecer prazo próprio para o ente público. O prazo em dobro conta da **intimação pessoal** (caput).",
      "lei": [
       {
        "lei": "L13105",
        "art": "183",
        "par": "",
        "inc": "",
        "rotulo": "CPC, art. 183, § 2º",
        "texto": "Não se aplica o benefício da contagem em dobro quando a lei estabelecer, de forma expressa, prazo próprio para o ente público."
       }
      ],
      "palavras_chave": [
       "prazo em dobro",
       "prazo próprio"
      ],
      "correcao": {
       "erro": "Aplica o prazo em dobro mesmo quando a lei estabelece, de forma expressa, prazo próprio para o ente público.",
       "certo": "A Advocacia Pública tem prazo em dobro contado da intimação pessoal, mas o benefício não se aplica quando a lei estabelece, de forma expressa, prazo próprio para o ente público."
      },
      "aprofundamento": "O prazo em dobro da Advocacia Pública se justifica pelo volume de processos e pela estrutura burocrática dos entes públicos. Ele conta a partir da **intimação pessoal** do procurador.\n\nMas a prerrogativa tem limite: quando a lei estabelece de forma expressa um **prazo próprio** para o ente público, não se aplica a dobra. Se o legislador já fixou um prazo específico pensando no ente público, dobrar esse prazo seria aplicar um benefício duas vezes.\n\nUm exemplo é o prazo para a Fazenda impugnar o cumprimento de sentença, que já foi pensado para ela. A assertiva estende a dobra justamente à hipótese que a lei exclui.",
      "memorize": "Prazo em dobro da Fazenda: não vale se a lei fixar prazo próprio para o ente."
     }
    },
    {
     "id": "CPC-3-R2-07",
     "ponto": "DBA26-CPC-3",
     "tema": "Recurso do MP fiscal",
     "assertiva": "O Ministério Público tem legitimidade para recorrer no processo em que oficiou como fiscal da ordem jurídica, ainda que não haja recurso da parte.",
     "gabarito": "C",
     "comentario": {
      "resumo": "Art. 996 (o recurso pode ser interposto pelo **MP** como parte ou como fiscal) e Súmula 99/STJ.",
      "lei": [
       {
        "lei": "L13105",
        "art": "996",
        "par": "",
        "inc": "",
        "rotulo": "CPC, art. 996",
        "texto": "O recurso pode ser interposto pela parte vencida, pelo terceiro prejudicado e pelo Ministério Público, como parte ou como fiscal da ordem jurídica."
       }
      ],
      "juris": [
       {
        "tribunal": "STJ",
        "fonte": "Súmula 99/STJ",
        "data": "14/04/1994",
        "texto": "O MP tem legitimidade para recorrer no processo em que oficiou como fiscal da lei, ainda que não haja recurso da parte."
       }
      ],
      "palavras_chave": [
       "MP",
       "legitimidade recursal"
      ],
      "aprofundamento": "Quando o MP atua como fiscal da ordem jurídica, sua função é zelar pela correta aplicação do direito, e não defender interesse de uma das partes. Por isso ele tem **legitimidade recursal autônoma**: pode recorrer mesmo que as partes se conformem com a decisão.\n\nA razão é que o interesse que justificou sua intervenção, como o interesse de incapaz ou o interesse público, não se confunde com o interesse das partes. Se a decisão violar esse interesse, o MP deve poder impugná-la, independentemente da conduta delas.\n\nA Súmula 99/STJ consolidou esse entendimento, e o CPC o incorporou ao dispor que o MP pode recorrer como parte ou como fiscal. A banca costuma condicionar o recurso do MP ao recurso da parte.",
      "memorize": "MP fiscal pode recorrer mesmo sem recurso da parte (Súmula 99/STJ)."
     }
    },
    {
     "id": "CPC-3-R2-08",
     "ponto": "DBA26-CPC-3",
     "tema": "Litisconsórcio e atos de um litisconsorte",
     "assertiva": "Os litisconsortes serão considerados litigantes distintos em suas relações com a parte adversa, exceto no litisconsórcio unitário, caso em que os atos e as omissões de um não prejudicarão os outros, mas os poderão beneficiar.",
     "gabarito": "C",
     "comentario": {
      "resumo": "Art. 117: regime da **autonomia** dos litisconsortes, mitigado no **unitário**.",
      "lei": [
       {
        "lei": "L13105",
        "art": "117",
        "par": "",
        "inc": "",
        "rotulo": "CPC, art. 117",
        "texto": "Os litisconsortes serão considerados, em suas relações com a parte adversa, como litigantes distintos, exceto no litisconsórcio unitário, caso em que os atos e as omissões de um não prejudicarão os outros, mas os poderão beneficiar."
       }
      ],
      "palavras_chave": [
       "litisconsórcio unitário",
       "autonomia"
      ],
      "aprofundamento": "No litisconsórcio, a regra é a **autonomia**: cada litisconsorte é tratado como litigante distinto, e os atos de um não afetam os outros. Se um confessa, a confissão não prejudica os demais; se um recorre, o recurso, em regra, aproveita só a ele.\n\nNo litisconsórcio **unitário**, porém, a decisão tem de ser igual para todos, porque a relação jurídica é incindível. Não faz sentido que o ato de um prejudique os demais, mas também não seria lógico ignorar um ato que beneficie todos. Por isso os atos e omissões de um **não prejudicam** os outros, mas **podem beneficiá-los**.\n\nUm exemplo é o recurso: no unitário, o recurso interposto por um aproveita a todos. A banca costuma inverter a regra ou aplicar o regime do unitário ao litisconsórcio simples.",
      "memorize": "Litisconsortes são autônomos; no unitário, ato de um não prejudica, mas pode beneficiar os outros."
     }
    },
    {
     "id": "CPC-4-R2-01",
     "ponto": "DBA26-CPC-4",
     "tema": "Prazo em dobro de litisconsortes",
     "assertiva": "Os litisconsortes com diferentes procuradores, de escritórios de advocacia distintos, terão prazos contados em dobro, inclusive em processos em autos eletrônicos.",
     "gabarito": "E",
     "comentario": {
      "resumo": "Art. 229, § 2º: o prazo em dobro **não se aplica aos autos eletrônicos**.",
      "excecoes": [
       "Não se aplica a processos em autos eletrônicos (art. 229, § 2º)",
       "Cessa se, havendo só 2 réus, apenas um oferecer defesa (art. 229, § 1º)"
      ],
      "lei": [
       {
        "lei": "L13105",
        "art": "229",
        "par": "",
        "inc": "",
        "rotulo": "CPC, art. 229, § 2º",
        "texto": "Não se aplica o disposto no caput aos processos em autos eletrônicos."
       }
      ],
      "palavras_chave": [
       "prazo em dobro",
       "autos eletrônicos"
      ],
      "correcao": {
       "erro": "Estende o prazo em dobro dos litisconsortes com procuradores distintos aos processos em autos eletrônicos.",
       "certo": "Litisconsortes com procuradores diferentes, de escritórios distintos, têm prazo em dobro, mas o benefício não se aplica aos processos em autos eletrônicos."
      },
      "aprofundamento": "O prazo em dobro para litisconsortes com procuradores diferentes nasceu de uma dificuldade prática dos autos **físicos**: só um advogado podia retirar o processo do cartório por vez, e os demais ficavam sem acesso. A dobra compensava esse obstáculo.\n\nNos **autos eletrônicos**, todos os advogados têm acesso simultâneo e permanente ao processo. A razão de ser do benefício desaparece, e por isso a lei o afasta expressamente.\n\nHá outra limitação: se houver só 2 réus e apenas um oferecer defesa, a dobra cessa. A banca estende o benefício aos autos eletrônicos, que é justamente a exceção expressa.",
      "memorize": "Prazo em dobro de litisconsortes: só em autos físicos, nunca em eletrônicos."
     }
    },
    {
     "id": "CPC-4-R2-02",
     "ponto": "DBA26-CPC-4",
     "tema": "Termo inicial na citação eletrônica",
     "assertiva": "Na citação por meio eletrônico, o prazo começa no quinto dia útil seguinte à confirmação do recebimento da citação.",
     "gabarito": "C",
     "comentario": {
      "resumo": "**Art. 231, I**X (Lei 14.195/2021).",
      "lei": [
       {
        "lei": "L13105",
        "art": "231",
        "par": "",
        "inc": "",
        "rotulo": "CPC, art. 231, IX",
        "texto": "o quinto dia útil seguinte à confirmação, na forma prevista na mensagem de citação, do recebimento da citação realizada por meio eletrônico"
       }
      ],
      "palavras_chave": [
       "termo inicial",
       "citação eletrônica"
      ],
      "aprofundamento": "A citação eletrônica passou a ser o meio preferencial com a Lei 14.195/2021, e precisava de uma regra própria para o início do prazo. A lei escolheu o **quinto dia útil** seguinte à confirmação do recebimento.\n\nA lógica é dar ao citado um pequeno intervalo depois de confirmar que recebeu a citação, para que ele possa procurar advogado e se organizar. A confirmação deve seguir a forma prevista na mensagem de citação.\n\nSe o citado não confirmar o recebimento, a citação eletrônica não se aperfeiçoa, e o juízo deve tentar os outros meios. A banca costuma alterar o termo, colocando-o no dia da confirmação ou no dia útil seguinte.",
      "memorize": "Citação eletrônica: prazo começa no 5º dia útil após a confirmação do recebimento."
     }
    },
    {
     "id": "CPC-4-R2-03",
     "ponto": "DBA26-CPC-4",
     "tema": "Citação nas ações de estado",
     "assertiva": "Nas ações de estado, admite-se a citação por meio eletrônico, desde que confirmada pelo réu.",
     "gabarito": "E",
     "comentario": {
      "resumo": "Art. 247, I: nas **ações de estado** não se cita por meio eletrônico nem pelo correio — a citação é **pessoal**, por oficial (art. 695, § 3º).",
      "excecoes": [
       "Também não cabem citação eletrônica/correio: incapaz, pessoa de direito público, local não atendido pelo correio e quando o autor justificadamente requerer outra forma (art. 247, II a V)"
      ],
      "lei": [
       {
        "lei": "L13105",
        "art": "247",
        "par": "",
        "inc": "",
        "rotulo": "CPC, art. 247, I",
        "texto": "I - nas ações de estado"
       }
      ],
      "palavras_chave": [
       "ações de estado",
       "citação pessoal"
      ],
      "correcao": {
       "erro": "Admite a citação por meio eletrônico nas ações de estado, desde que confirmada pelo réu.",
       "certo": "Nas ações de estado não se faz citação por meio eletrônico nem pelo correio; a citação é pessoal, por oficial de justiça."
      },
      "aprofundamento": "As **ações de estado** envolvem questões de família e de identidade das pessoas, como divórcio, investigação de paternidade e reconhecimento de união estável. São temas sensíveis, que tratam de direitos indisponíveis e da própria condição jurídica da pessoa.\n\nPor isso a lei exige mais segurança na citação: não se admite citação eletrônica nem pelo correio. Nas ações de família, a citação é feita **pessoalmente**, por oficial de justiça, e o mandado não traz cópia da petição inicial, para preservar o ambiente de conciliação.\n\nA mesma vedação vale para o incapaz, para a pessoa de direito público, para local não atendido pelo correio e quando o autor justificadamente pedir outra forma. A banca tenta admitir a citação eletrônica com a condição da confirmação, que não supera a vedação.",
      "memorize": "Ação de estado: sem citação eletrônica ou por correio; citação pessoal."
     }
    },
    {
     "id": "CPC-4-R2-04",
     "ponto": "DBA26-CPC-4",
     "tema": "Citação por edital — diligências",
     "assertiva": "Segundo o STJ, a expedição de ofícios a cadastros de órgãos públicos e a concessionárias de serviços públicos é requisito obrigatório de validade da citação por edital.",
     "gabarito": "E",
     "comentario": {
      "resumo": "Tema 1.338/STJ: **não é requisito obrigatório**; em regra basta a frustração da busca nos endereços dos autos e nos **sistemas informatizados** do juízo, com decisão motivada.",
      "lei": [
       {
        "lei": "L13105",
        "art": "256",
        "par": "",
        "inc": "",
        "rotulo": "CPC, art. 256, § 3º",
        "texto": "O réu será considerado em local ignorado ou incerto se infrutíferas as tentativas de sua localização, inclusive mediante requisição pelo juízo de informações sobre seu endereço nos cadastros de órgãos públicos ou de concessionárias de serviços públicos."
       }
      ],
      "juris": [
       {
        "tribunal": "STJ",
        "fonte": "Tema 1.338/STJ — REsp 2.166.983/AP e REsp 2.162.483/AP",
        "data": "18/03/2026",
        "texto": "Ofícios a cadastros públicos ou concessionárias não são requisito obrigatório da citação por edital; basta, em regra, a frustração das tentativas nos endereços dos autos e nos sistemas informatizados do juízo."
       }
      ],
      "palavras_chave": [
       "citação por edital",
       "Tema 1.338"
      ],
      "correcao": {
       "erro": "Trata a expedição de ofícios a cadastros públicos e concessionárias como requisito obrigatório da citação por edital.",
       "certo": "Para o STJ (Tema 1.338), esses ofícios não são requisito obrigatório; em regra basta a frustração das tentativas nos endereços dos autos e nos sistemas informatizados do juízo."
      },
      "aprofundamento": "A citação por edital é **ficta**: presume-se que o réu soube da ação pela publicação. Por isso ela só é admitida quando o réu está em local ignorado ou incerto, depois de esgotados os meios razoáveis de localização.\n\nO código prevê que o juízo pode requisitar informações a cadastros públicos e concessionárias. O STJ, no **Tema 1.338**, esclareceu que essa requisição **não é requisito obrigatório**. Em regra, basta a frustração das tentativas nos endereços constantes dos autos e nos **sistemas informatizados** do juízo, com decisão motivada.\n\nA lógica é evitar que a citação por edital se torne excessivamente difícil, sem deixar de exigir diligência razoável. A banca transforma a faculdade em requisito de validade.",
      "memorize": "Edital: ofícios a cadastros não são obrigatórios; basta esgotar endereços e sistemas do juízo (Tema 1.338/STJ)."
     }
    },
    {
     "id": "CPC-4-R2-05",
     "ponto": "DBA26-CPC-4",
     "tema": "Momento de alegar nulidade",
     "assertiva": "A nulidade dos atos deve ser alegada na primeira oportunidade em que couber à parte falar nos autos, sob pena de preclusão, o que não se aplica às nulidades que o juiz deva decretar de ofício.",
     "gabarito": "C",
     "comentario": {
      "resumo": "**Art. 278** e parágrafo único.",
      "lei": [
       {
        "lei": "L13105",
        "art": "278",
        "par": "",
        "inc": "",
        "rotulo": "CPC, art. 278",
        "texto": "A nulidade dos atos deve ser alegada na primeira oportunidade em que couber à parte falar nos autos, sob pena de preclusão."
       }
      ],
      "palavras_chave": [
       "nulidade",
       "preclusão"
      ],
      "aprofundamento": "A exigência de alegar a nulidade na primeira oportunidade protege a **lealdade processual**. Sem ela, a parte poderia guardar o vício como uma carta na manga, esperar o resultado e só alegar a nulidade se perdesse. É a chamada nulidade de algibeira, que o sistema repudia.\n\nPor isso a nulidade não alegada no primeiro momento preclui. A exceção são as nulidades que o juiz deve decretar **de ofício**, como as absolutas ligadas a interesse público, que não dependem da iniciativa da parte e não se sujeitam à preclusão.\n\nO parágrafo único também ressalva a parte que provar legítimo impedimento. A banca costuma dizer que toda nulidade pode ser alegada a qualquer tempo, ou o contrário, que até as nulidades conhecíveis de ofício precluem.",
      "memorize": "Nulidade se alega na primeira oportunidade, senão preclui; exceto as que o juiz decreta de ofício."
     }
    },
    {
     "id": "CPC-4-R2-06",
     "ponto": "DBA26-CPC-4",
     "tema": "Falta de intimação do MP",
     "assertiva": "A falta de intimação do Ministério Público, quando obrigatória sua intervenção, gera nulidade automática do processo, independentemente de manifestação do órgão sobre a existência de prejuízo.",
     "gabarito": "E",
     "comentario": {
      "resumo": "Art. 279, § 2º: a nulidade **só pode ser decretada após a intimação do MP**, que dirá se houve ou não **prejuízo**.",
      "lei": [
       {
        "lei": "L13105",
        "art": "279",
        "par": "",
        "inc": "",
        "rotulo": "CPC, art. 279, § 2º",
        "texto": "A nulidade só pode ser decretada após a intimação do Ministério Público, que se manifestará sobre a existência ou a inexistência de prejuízo."
       }
      ],
      "palavras_chave": [
       "MP",
       "prejuízo",
       "nulidade"
      ],
      "correcao": {
       "erro": "Afirma que a falta de intimação do MP gera nulidade automática, independentemente de sua manifestação sobre o prejuízo.",
       "certo": "A nulidade pela falta de intimação do MP só pode ser decretada depois de intimado o órgão, que se manifestará sobre a existência ou inexistência de prejuízo."
      },
      "aprofundamento": "A intervenção do MP como fiscal existe para proteger determinados interesses. Se ele não foi intimado, há vício. Mas o sistema de nulidades do CPC é guiado pela **instrumentalidade**: não há nulidade sem prejuízo.\n\nPor isso a lei prevê um procedimento específico: antes de decretar a nulidade, o juiz deve **intimar o MP**, que dirá se houve ou não prejuízo ao interesse que justificava sua atuação. Se o MP disser que não houve prejuízo, por exemplo porque o incapaz saiu vitorioso, não há razão para anular.\n\nA banca descreve uma nulidade automática, que o código afasta. A palavra \"automática\" ou \"independentemente de prejuízo\" denuncia o erro.",
      "memorize": "Falta de intimação do MP: antes de anular, ouve-se o MP sobre o prejuízo."
     }
    },
    {
     "id": "CPC-4-R2-07",
     "ponto": "DBA26-CPC-4",
     "tema": "Preclusão temporal",
     "assertiva": "Decorrido o prazo, extingue-se o direito de praticar ou de emendar o ato processual, independentemente de declaração judicial, ficando assegurado à parte provar que não o realizou por justa causa.",
     "gabarito": "C",
     "comentario": {
      "resumo": "Art. 223: **preclusão temporal**, com ressalva da **justa causa**.",
      "lei": [
       {
        "lei": "L13105",
        "art": "223",
        "par": "",
        "inc": "",
        "rotulo": "CPC, art. 223",
        "texto": "Decorrido o prazo, extingue-se o direito de praticar ou de emendar o ato processual, independentemente de declaração judicial, ficando assegurado, porém, à parte provar que não o realizou por justa causa."
       }
      ],
      "palavras_chave": [
       "preclusão temporal",
       "justa causa"
      ],
      "aprofundamento": "A **preclusão temporal** é a perda da faculdade de praticar um ato pelo decurso do prazo. Ela dá ritmo e previsibilidade ao processo: se os prazos pudessem ser descumpridos sem consequência, o processo não teria fim.\n\nA preclusão opera **automaticamente**, sem necessidade de declaração judicial. Terminado o prazo, o direito de praticar ou emendar o ato se extingue, e o processo segue.\n\nA válvula de escape é a **justa causa**: evento alheio à vontade da parte que a impediu de praticar o ato, como uma doença grave ou falha no sistema eletrônico. Provada a justa causa, o juiz permite a prática do ato no prazo que fixar. A banca costuma exigir declaração judicial ou negar a ressalva da justa causa.",
      "memorize": "Preclusão temporal: automática, salvo justa causa provada."
     }
    },
    {
     "id": "CPC-4-R2-08",
     "ponto": "DBA26-CPC-4",
     "tema": "Controle judicial do negócio processual",
     "assertiva": "Em respeito à autonomia da vontade, o juiz não pode recusar aplicação a convenção processual celebrada por partes capazes.",
     "gabarito": "E",
     "comentario": {
      "resumo": "Art. 190, par. ún.: o juiz controla a validade **de ofício ou a requerimento** e recusa aplicação em caso de nulidade, **contrato de adesão** abusivo ou **vulnerabilidade** manifesta.",
      "lei": [
       {
        "lei": "L13105",
        "art": "190",
        "par": "",
        "inc": "",
        "rotulo": "CPC, art. 190, par. ún.",
        "texto": "De ofício ou a requerimento, o juiz controlará a validade das convenções previstas neste artigo, recusando-lhes aplicação somente nos casos de nulidade ou de inserção abusiva em contrato de adesão ou em que alguma parte se encontre em manifesta situação de vulnerabilidade."
       }
      ],
      "palavras_chave": [
       "negócio processual",
       "vulnerabilidade",
       "contrato de adesão"
      ],
      "correcao": {
       "erro": "Impede o juiz de recusar aplicação a convenção processual celebrada por partes capazes.",
       "certo": "O juiz controla a validade das convenções processuais, de ofício ou a requerimento, e recusa aplicação em caso de nulidade, inserção abusiva em contrato de adesão ou manifesta vulnerabilidade de uma parte."
      },
      "aprofundamento": "O negócio processual é expressão da **autonomia da vontade**, mas não é ilimitado. O juiz continua sendo o guardião da validade do processo e deve controlar as convenções, de ofício ou a requerimento.\n\nAs hipóteses de recusa são três: **nulidade** (o negócio viola norma cogente ou tem vício), **inserção abusiva em contrato de adesão** (a parte não teve escolha real) e **manifesta vulnerabilidade** de uma das partes. Fora delas, o juiz deve respeitar o acordo, ainda que discorde de sua conveniência.\n\nA assertiva impede qualquer controle, o que contraria a lei. O equilíbrio está entre respeitar a vontade das partes e impedir que ela seja usada para abusos.",
      "memorize": "Negócio processual: juiz controla e recusa só por nulidade, adesão abusiva ou vulnerabilidade."
     }
    },
    {
     "id": "CPC-4-R2-09",
     "ponto": "DBA26-CPC-4",
     "tema": "Demora na citação",
     "assertiva": "Proposta a ação no prazo, a demora na citação por motivos inerentes ao mecanismo da Justiça não justifica o acolhimento da prescrição.",
     "gabarito": "C",
     "comentario": {
      "resumo": "Súmula 106/STJ, em sintonia com o art. 240, § 3º: a parte não é prejudicada pela demora imputável **exclusivamente ao serviço judiciário**.",
      "lei": [
       {
        "lei": "L13105",
        "art": "240",
        "par": "",
        "inc": "",
        "rotulo": "CPC, art. 240, § 3º",
        "texto": "A parte não será prejudicada pela demora imputável exclusivamente ao serviço judiciário."
       }
      ],
      "juris": [
       {
        "tribunal": "STJ",
        "fonte": "Súmula 106/STJ",
        "data": "26/05/1994",
        "texto": "Proposta a ação no prazo, a demora na citação por motivos inerentes ao mecanismo da Justiça não justifica o acolhimento da prescrição ou da decadência."
       }
      ],
      "palavras_chave": [
       "prescrição",
       "demora na citação"
      ],
      "aprofundamento": "A prescrição pune a **inércia** do titular. Se o autor propôs a ação dentro do prazo, ele agiu. A demora posterior na citação, quando causada pelo próprio funcionamento da Justiça, não pode ser imputada a ele.\n\nA Súmula 106/STJ consagra essa ideia, e o CPC a incorporou: a parte não é prejudicada pela demora imputável **exclusivamente** ao serviço judiciário. A interrupção da prescrição retroage à data da propositura.\n\nO advérbio \"exclusivamente\" é importante. Se a demora decorreu de culpa do autor, como a indicação de endereço errado ou a falta de pagamento de diligências, a proteção não se aplica. A banca costuma generalizar a proteção para qualquer demora ou retirá-la.",
      "memorize": "Demora na citação por culpa só da Justiça não prejudica o autor (Súmula 106/STJ)."
     }
    },
    {
     "id": "CPC-4-R2-10",
     "ponto": "DBA26-CPC-4",
     "tema": "Valor da causa — alimentos",
     "assertiva": "Na ação de alimentos, o valor da causa será a soma de 6 prestações mensais pedidas pelo autor.",
     "gabarito": "E",
     "comentario": {
      "resumo": "Art. 292, III: soma de **12 prestações** mensais.",
      "lei": [
       {
        "lei": "L13105",
        "art": "292",
        "par": "",
        "inc": "",
        "rotulo": "CPC, art. 292, III",
        "texto": "na ação de alimentos, a soma de 12 (doze) prestações mensais"
       }
      ],
      "palavras_chave": [
       "valor da causa",
       "12 prestações"
      ],
      "correcao": {
       "erro": "Fixa o valor da causa na ação de alimentos na soma de 6 prestações mensais.",
       "certo": "Na ação de alimentos, o valor da causa é a soma de 12 prestações mensais pedidas pelo autor."
      },
      "aprofundamento": "O valor da causa deve corresponder ao **conteúdo econômico** do pedido. Na ação de alimentos, a prestação é periódica e indefinida, e a lei precisava de um critério objetivo. Escolheu a soma de 12 prestações mensais, o que corresponde a um ano de alimentos.\n\nO valor da causa importa para vários efeitos: custas, honorários, competência dos Juizados e multas processuais. Por isso a lei fixa critérios específicos para vários tipos de ação, evitando discussões.\n\nA banca reduz o número de prestações. Associe o critério ao ano: 12 meses de alimentos.",
      "memorize": "Valor da causa em alimentos: 12 prestações mensais."
     }
    },
    {
     "id": "CPC-5-R2-01",
     "ponto": "DBA26-CPC-5",
     "tema": "Competência",
     "assertiva": "A tutela provisória antecedente será requerida ao juízo competente para conhecer do pedido principal.",
     "gabarito": "C",
     "comentario": {
      "resumo": "Art. 299: incidental → juízo da causa; antecedente → juízo competente para o **pedido principal**.",
      "lei": [
       {
        "lei": "L13105",
        "art": "299",
        "par": "",
        "inc": "",
        "rotulo": "CPC, art. 299",
        "texto": "A tutela provisória será requerida ao juízo da causa e, quando antecedente, ao juízo competente para conhecer do pedido principal."
       }
      ],
      "palavras_chave": [
       "competência",
       "pedido principal"
      ],
      "aprofundamento": "A tutela provisória é sempre **instrumental** em relação ao pedido principal: serve para garantir ou antecipar o resultado de um processo de mérito. Por isso a competência acompanha esse pedido.\n\nSe a tutela for **incidental**, já existe o processo, e ela é pedida ao juízo da causa. Se for **antecedente**, o processo principal ainda não começou, e a tutela é requerida ao juízo que será competente para conhecer do pedido principal. Assim, o mesmo juízo que conceder a medida julgará o mérito.\n\nNos tribunais, a tutela em recurso ou ação de competência originária é pedida ao órgão competente para apreciar o mérito. A banca costuma dizer que a tutela antecedente pode ser pedida a qualquer juízo por causa da urgência.",
      "memorize": "Tutela antecedente: juízo competente para o pedido principal; incidental: juízo da causa."
     }
    },
    {
     "id": "CPC-5-R2-02",
     "ponto": "DBA26-CPC-5",
     "tema": "Medidas cautelares",
     "assertiva": "A tutela de urgência cautelar pode ser efetivada mediante arresto, sequestro, arrolamento de bens, registro de protesto contra alienação de bem e qualquer outra medida idônea para asseguração do direito.",
     "gabarito": "C",
     "comentario": {
      "resumo": "Art. 301: rol **exemplificativo** — o poder geral de cautela permanece.",
      "lei": [
       {
        "lei": "L13105",
        "art": "301",
        "par": "",
        "inc": "",
        "rotulo": "CPC, art. 301",
        "texto": "A tutela de urgência de natureza cautelar pode ser efetivada mediante arresto, sequestro, arrolamento de bens, registro de protesto contra alienação de bem e qualquer outra medida idônea para asseguração do direito."
       }
      ],
      "palavras_chave": [
       "poder geral de cautela",
       "arresto",
       "sequestro"
      ],
      "aprofundamento": "O código anterior tinha um rol de **cautelares nominadas**, cada uma com procedimento próprio. O CPC atual simplificou: mantém a referência a algumas medidas tradicionais, mas deixa claro que o rol é **exemplificativo**.\n\nO **arresto** apreende bens para garantir execução por quantia; o **sequestro** apreende bem determinado objeto de litígio; o **arrolamento** documenta bens para evitar seu extravio; o **protesto contra alienação** dá publicidade ao risco de alienação. Mas o juiz pode determinar \"qualquer outra medida idônea\", com base no **poder geral de cautela**.\n\nA banca costuma dizer que as cautelares se limitam às medidas listadas, o que contraria a expressão final do artigo.",
      "memorize": "Cautelares: arresto, sequestro, arrolamento, protesto contra alienação e qualquer medida idônea (rol exemplificativo)."
     }
    },
    {
     "id": "CPC-5-R2-03",
     "ponto": "DBA26-CPC-5",
     "tema": "Fungibilidade",
     "assertiva": "Se o juiz entender que o pedido cautelar antecedente tem natureza antecipada, deve indeferi-lo, pois é vedada a fungibilidade entre as tutelas de urgência.",
     "gabarito": "E",
     "comentario": {
      "resumo": "Art. 305, par. ún.: o juiz **observará o art. 303** — há **fungibilidade**.",
      "lei": [
       {
        "lei": "L13105",
        "art": "305",
        "par": "",
        "inc": "",
        "rotulo": "CPC, art. 305, par. ún.",
        "texto": "Caso entenda que o pedido a que se refere o caput tem natureza antecipada, o juiz observará o disposto no art. 303"
       }
      ],
      "palavras_chave": [
       "fungibilidade"
      ],
      "correcao": {
       "erro": "Determina o indeferimento do pedido cautelar com natureza antecipada, vedando a fungibilidade.",
       "certo": "Se o juiz entender que o pedido cautelar antecedente tem natureza antecipada, observará o procedimento do art. 303; há fungibilidade entre as tutelas de urgência."
      },
      "aprofundamento": "A distinção entre tutela cautelar e antecipada nem sempre é nítida. Há medidas que, conforme o ângulo, podem ser vistas como conservativas ou satisfativas. Se o juiz tivesse de indeferir o pedido por um erro de rótulo, a parte perderia a proteção por mera formalidade.\n\nPor isso o código consagra a **fungibilidade**: se o juiz entender que o pedido cautelar antecedente tem natureza antecipada, ele aplica o procedimento da tutela antecipada antecedente (art. 303), em vez de indeferir. É expressão da primazia do mérito e da instrumentalidade.\n\nA doutrina majoritária admite a fungibilidade também no sentido inverso, de antecipada para cautelar. A assertiva cria uma vedação que contraria o texto legal.",
      "memorize": "Cautelar com cara de antecipada: o juiz converte e segue o art. 303 (fungibilidade)."
     }
    },
    {
     "id": "CPC-5-R2-04",
     "ponto": "DBA26-CPC-5",
     "tema": "Cessação da eficácia da cautelar",
     "assertiva": "Cessa a eficácia da tutela cautelar concedida em caráter antecedente se ela não for efetivada dentro de 30 dias.",
     "gabarito": "C",
     "comentario": {
      "resumo": "**Art. 309, II**. Também cessa se o pedido principal não for deduzido no prazo (I) ou se o juiz julgar improcedente o principal ou extinguir sem mérito (III).",
      "lei": [
       {
        "lei": "L13105",
        "art": "309",
        "par": "",
        "inc": "",
        "rotulo": "CPC, art. 309, II",
        "texto": "II - não for efetivada dentro de 30 (trinta) dias;"
       }
      ],
      "palavras_chave": [
       "cessação da eficácia"
      ],
      "aprofundamento": "A tutela cautelar antecedente existe para proteger um direito diante de uma urgência. Se o próprio autor não a efetiva no prazo legal, demonstra que a urgência não era tão grave, ou que perdeu o interesse. A medida não pode ficar indefinidamente pendente, gerando insegurança para a outra parte.\n\nPor isso a eficácia cessa se a cautelar não for efetivada em 30 dias. As outras hipóteses de cessação são: o pedido principal não ser deduzido no prazo legal, ou o juiz julgar improcedente o pedido principal ou extinguir o processo sem mérito.\n\nCessada a eficácia, a parte não pode renovar o pedido pelo mesmo fundamento, salvo novo fundamento. A banca costuma trocar o prazo ou omitir alguma hipótese de cessação.",
      "memorize": "Cautelar antecedente perde eficácia se não efetivada em 30 dias (e nas demais hipóteses legais)."
     }
    },
    {
     "id": "CPC-5-R2-05",
     "ponto": "DBA26-CPC-5",
     "tema": "Indeferimento da cautelar",
     "assertiva": "O indeferimento da tutela cautelar não obsta a formulação do pedido principal nem influi no seu julgamento em nenhuma hipótese.",
     "gabarito": "E",
     "comentario": {
      "resumo": "Art. 310: há exceção — quando o motivo do indeferimento for o reconhecimento de **decadência ou prescrição**.",
      "excecoes": [
       "Indeferimento por decadência ou prescrição influi no pedido principal (art. 310)"
      ],
      "lei": [
       {
        "lei": "L13105",
        "art": "310",
        "par": "",
        "inc": "",
        "rotulo": "CPC, art. 310",
        "texto": "O indeferimento da tutela cautelar não obsta a que a parte formule o pedido principal, nem influi no julgamento desse, salvo se o motivo do indeferimento for o reconhecimento de decadência ou de prescrição."
       }
      ],
      "palavras_chave": [
       "prescrição",
       "decadência"
      ],
      "correcao": {
       "erro": "Afirma que o indeferimento da cautelar nunca influi no pedido principal, sem exceção.",
       "certo": "O indeferimento da tutela cautelar não obsta o pedido principal nem influi no seu julgamento, salvo se o motivo for o reconhecimento de decadência ou de prescrição."
      },
      "aprofundamento": "A regra é que o indeferimento da cautelar não afeta o pedido principal, porque a cautelar é examinada em cognição sumária, voltada apenas para a urgência. O mérito será discutido em profundidade no processo principal.\n\nHá, porém, uma exceção lógica: se o juiz indeferiu a cautelar por reconhecer **decadência ou prescrição**, ele já decidiu uma questão de mérito. Seria incoerente permitir que o mesmo direito, já declarado extinto, fosse discutido no pedido principal.\n\nA assertiva elimina a exceção com a expressão \"em nenhuma hipótese\". Termos absolutos em regras que têm ressalvas expressas são sinal de erro.",
      "memorize": "Indeferir cautelar não afeta o principal, salvo se o motivo for prescrição ou decadência."
     }
    },
    {
     "id": "CPC-5-R2-06",
     "ponto": "DBA26-CPC-5",
     "tema": "Evidência liminar",
     "assertiva": "A tutela da evidência fundada no abuso do direito de defesa ou no manifesto propósito protelatório da parte pode ser concedida liminarmente.",
     "gabarito": "E",
     "comentario": {
      "resumo": "Liminar só nos incisos **II e III** do art. 311. O abuso de defesa (inciso I) pressupõe a defesa já apresentada.",
      "lei": [
       {
        "lei": "L13105",
        "art": "311",
        "par": "",
        "inc": "",
        "rotulo": "CPC, art. 311, par. ún.",
        "texto": "Nas hipóteses dos incisos II e III, o juiz poderá decidir liminarmente."
       }
      ],
      "palavras_chave": [
       "evidência",
       "liminar"
      ],
      "correcao": {
       "erro": "Admite a concessão liminar da tutela da evidência fundada no abuso do direito de defesa.",
       "certo": "A tutela da evidência só pode ser concedida liminarmente nas hipóteses dos incisos II e III do art. 311; o abuso do direito de defesa pressupõe a defesa já apresentada."
      },
      "aprofundamento": "A concessão liminar da tutela da evidência só é possível quando o direito é evidente **sem depender da conduta do réu**. Nos incisos II e III, a evidência vem dos documentos do autor, combinados com tese firmada ou com o contrato de depósito.\n\nO **abuso do direito de defesa** e o **manifesto propósito protelatório** são condutas do réu no processo. Para que existam, é preciso que o réu já tenha se manifestado. Logo, essa hipótese é, por natureza, incompatível com a concessão liminar.\n\nA mesma lógica vale para a hipótese de prova documental sem dúvida razoável oposta pelo réu. A assertiva ignora a restrição expressa do parágrafo único, que limita a liminar aos incisos II e III.",
      "memorize": "Abuso de defesa nunca é liminar: só os incisos II e III admitem liminar."
     }
    },
    {
     "id": "CPC-5-R2-07",
     "ponto": "DBA26-CPC-5",
     "tema": "Emenda na antecipada antecedente",
     "assertiva": "Se entender que não há elementos para a concessão de tutela antecipada antecedente, o órgão jurisdicional determinará a emenda da petição inicial em até 5 dias, sob pena de indeferimento e extinção sem resolução de mérito.",
     "gabarito": "C",
     "comentario": {
      "resumo": "**Art. 303, § 6º**.",
      "lei": [
       {
        "lei": "L13105",
        "art": "303",
        "par": "",
        "inc": "",
        "rotulo": "CPC, art. 303, § 6º",
        "texto": "Caso entenda que não há elementos para a concessão de tutela antecipada, o órgão jurisdicional determinará a emenda da petição inicial em até 5 (cinco) dias, sob pena de ser indeferida e de o processo ser extinto sem resolução de mérito."
       }
      ],
      "palavras_chave": [
       "emenda",
       "5 dias"
      ],
      "aprofundamento": "Na tutela antecipada antecedente, o autor apresenta uma petição inicial simplificada, focada na urgência. Se o juiz entender que não há elementos para conceder a tutela, o processo não pode seguir com essa petição incompleta.\n\nA lei, então, manda o juiz determinar a **emenda** da inicial em até 5 dias, para que o autor complete a argumentação e transforme o pedido em uma inicial completa, apta a seguir pelo procedimento comum. Se não houver emenda, a petição é indeferida e o processo extinto sem resolução do mérito.\n\nO prazo é curto porque a situação já era urgente. A banca costuma trocar esse prazo pelo prazo geral de emenda da inicial, que é maior.",
      "memorize": "Antecipada antecedente negada: emenda em até 5 dias, sob pena de extinção."
     }
    },
    {
     "id": "CPC-5-R2-08",
     "ponto": "DBA26-CPC-5",
     "tema": "Ação para rever a estabilização",
     "assertiva": "Somente o réu tem legitimidade para demandar a revisão, reforma ou invalidação da tutela antecipada estabilizada.",
     "gabarito": "E",
     "comentario": {
      "resumo": "Art. 304, § 2º: **qualquer das partes** pode demandar a outra.",
      "lei": [
       {
        "lei": "L13105",
        "art": "304",
        "par": "",
        "inc": "",
        "rotulo": "CPC, art. 304, § 2º",
        "texto": "Qualquer das partes poderá demandar a outra com o intuito de rever, reformar ou invalidar a tutela antecipada estabilizada nos termos do caput"
       }
      ],
      "palavras_chave": [
       "estabilização",
       "qualquer das partes"
      ],
      "correcao": {
       "erro": "Restringe ao réu a legitimidade para a ação de revisão da tutela estabilizada.",
       "certo": "Qualquer das partes pode demandar a outra com o intuito de rever, reformar ou invalidar a tutela antecipada estabilizada."
      },
      "aprofundamento": "A estabilização da tutela antecipada não faz coisa julgada, e por isso a lei permite que a decisão seja revista. A ação de revisão, reforma ou invalidação pode ser proposta por **qualquer das partes**.\n\nO réu tem interesse evidente: quer afastar a tutela que o prejudica. Mas o autor também pode ter interesse, por exemplo, em obter uma decisão de mérito com cognição exauriente, que faça coisa julgada, ou em ampliar a tutela concedida.\n\nO juízo que concedeu a tutela fica prevento, e qualquer das partes pode requerer o desarquivamento dos autos para instruir a ação. A assertiva restringe a legitimidade ao réu, contrariando o texto.",
      "memorize": "Rever tutela estabilizada: qualquer das partes."
     }
    },
    {
     "id": "CPC-5-R2-09",
     "ponto": "DBA26-CPC-5",
     "tema": "Liquidação do prejuízo",
     "assertiva": "A indenização pelo prejuízo causado pela efetivação da tutela de urgência será liquidada nos autos em que a medida tiver sido concedida, sempre que possível.",
     "gabarito": "C",
     "comentario": {
      "resumo": "**Art. 302**, par. ún.",
      "lei": [
       {
        "lei": "L13105",
        "art": "302",
        "par": "",
        "inc": "",
        "rotulo": "CPC, art. 302, par. ún.",
        "texto": "A indenização será liquidada nos autos em que a medida tiver sido concedida, sempre que possível."
       }
      ],
      "palavras_chave": [
       "liquidação",
       "mesmos autos"
      ],
      "aprofundamento": "A responsabilidade pelo prejuízo causado pela tutela de urgência é **objetiva**: quem se beneficiou da medida e depois perdeu deve indenizar. Para que essa indenização seja efetiva, a lei simplifica o procedimento.\n\nA liquidação ocorre **nos próprios autos** em que a medida foi concedida, sempre que possível. A vítima não precisa ajuizar uma nova ação de indenização, com todo o tempo e custo envolvidos.\n\nA ressalva \"sempre que possível\" reconhece que há casos em que a complexidade do dano exige via própria. A banca costuma exigir ação autônoma como regra, o que contraria a lógica de simplificação.",
      "memorize": "Indenização pela tutela de urgência: liquidada nos próprios autos, sempre que possível."
     }
    },
    {
     "id": "CPC-5-R2-10",
     "ponto": "DBA26-CPC-5",
     "tema": "Caução",
     "assertiva": "Para a concessão da tutela de urgência, a caução real ou fidejussória é sempre obrigatória.",
     "gabarito": "E",
     "comentario": {
      "resumo": "Art. 300, § 1º: a caução é **faculdade do juiz** (\"pode\") e pode ser **dispensada** se a parte economicamente hipossuficiente não puder oferecê-la.",
      "lei": [
       {
        "lei": "L13105",
        "art": "300",
        "par": "",
        "inc": "",
        "rotulo": "CPC, art. 300, § 1º",
        "texto": "Para a concessão da tutela de urgência, o juiz pode, conforme o caso, exigir caução real ou fidejussória idônea para ressarcir os danos que a outra parte possa vir a sofrer, podendo a caução ser dispensada se a parte economicamente hipossuficiente não puder oferecê-la."
       }
      ],
      "pegadinha": "\"Pode\" virou \"sempre obrigatória\".",
      "palavras_chave": [
       "caução",
       "hipossuficiente"
      ],
      "correcao": {
       "erro": "Torna a caução sempre obrigatória para a concessão da tutela de urgência.",
       "certo": "O juiz pode, conforme o caso, exigir caução real ou fidejussória idônea, podendo dispensá-la se a parte economicamente hipossuficiente não puder oferecê-la."
      },
      "aprofundamento": "A caução na tutela de urgência serve para garantir o ressarcimento dos danos que a medida possa causar à outra parte, caso o beneficiário perca. É uma contrapartida razoável ao risco da decisão provisória.\n\nMas a lei a trata como **faculdade** do juiz, que pode exigi-la **conforme o caso**. E ela pode ser **dispensada** se a parte economicamente hipossuficiente não puder oferecê-la. Exigir sempre a caução excluiria da tutela de urgência justamente quem mais precisa dela.\n\nA assertiva transforma o \"pode\" em \"sempre obrigatória\", uma das trocas mais comuns da banca. Leia com atenção o verbo do dispositivo.",
      "memorize": "Caução na urgência: o juiz PODE exigir; dispensável para o hipossuficiente."
     }
    },
    {
     "id": "CPC-6-R2-01",
     "ponto": "DBA26-CPC-6",
     "tema": "Prejudicialidade criminal",
     "assertiva": "Se o conhecimento do mérito depender da verificação da existência de fato delituoso, o juiz pode suspender o processo; se a ação penal não for proposta em 6 meses, cessa o efeito da suspensão.",
     "gabarito": "E",
     "comentario": {
      "resumo": "Art. 315, § 1º: o prazo é de **3 meses** contados da intimação do ato de suspensão.",
      "lei": [
       {
        "lei": "L13105",
        "art": "315",
        "par": "",
        "inc": "",
        "rotulo": "CPC, art. 315, § 1º",
        "texto": "Se a ação penal não for proposta no prazo de 3 (três) meses, contado da intimação do ato de suspensão, cessará o efeito desse, incumbindo ao juiz cível examinar incidentemente a questão prévia."
       }
      ],
      "palavras_chave": [
       "prejudicial criminal",
       "3 meses"
      ],
      "correcao": {
       "erro": "Fixa em 6 meses o prazo para propositura da ação penal sob pena de cessar a suspensão.",
       "certo": "Se a ação penal não for proposta em 3 meses, contados da intimação do ato de suspensão, cessa o efeito da suspensão e o juiz cível examina incidentemente a questão prévia."
      },
      "aprofundamento": "Quando o julgamento cível depende da verificação de um fato delituoso, o juiz pode suspender o processo para aguardar a esfera criminal. A razão é evitar decisões contraditórias sobre o mesmo fato.\n\nMas a suspensão não pode ser indefinida. Se a ação penal não for proposta em 3 meses da intimação do ato de suspensão, a suspensão cessa, e o próprio juiz cível examina a questão prejudicial incidentemente. Proposta a ação penal, o processo civil fica suspenso por no máximo 1 ano.\n\nA banca troca o prazo para 6 meses, que é o prazo da suspensão convencional. Fique atento à confusão entre os prazos de suspensão.",
      "memorize": "Prejudicial criminal: ação penal em 3 meses; proposta, suspensão por até 1 ano."
     }
    },
    {
     "id": "CPC-6-R2-02",
     "ponto": "DBA26-CPC-6",
     "tema": "Prejudicialidade criminal — duração",
     "assertiva": "Proposta a ação penal, o processo civil ficará suspenso pelo prazo máximo de 1 ano, ao final do qual o juiz cível examinará incidentemente a questão prévia.",
     "gabarito": "C",
     "comentario": {
      "resumo": "**Art. 315, § 2º**.",
      "lei": [
       {
        "lei": "L13105",
        "art": "315",
        "par": "",
        "inc": "",
        "rotulo": "CPC, art. 315, § 2º",
        "texto": "Proposta a ação penal, o processo ficará suspenso pelo prazo máximo de 1 (um) ano, ao final do qual aplicar-se-á o disposto na parte final do § 1º."
       }
      ],
      "palavras_chave": [
       "independência das instâncias",
       "1 ano"
      ],
      "aprofundamento": "Proposta a ação penal, a suspensão do processo civil continua, mas tem limite. O tempo da Justiça criminal é imprevisível, e o processo cível não pode ficar paralisado indefinidamente à espera.\n\nO prazo máximo é de 1 ano. Esgotado esse prazo, o juiz cível examina **incidentemente** a questão prévia, ou seja, decide ele mesmo, para fins do processo civil, sobre a existência do fato delituoso.\n\nEssa solução equilibra dois valores: evitar decisões contraditórias, aguardando um tempo razoável, e garantir a duração razoável do processo civil. A banca costuma alterar o prazo ou dizer que a suspensão dura até o trânsito em julgado da ação penal.",
      "memorize": "Ação penal proposta: suspensão cível por até 1 ano; depois, o juiz cível decide incidentemente."
     }
    },
    {
     "id": "CPC-6-R2-03",
     "ponto": "DBA26-CPC-6",
     "tema": "Paternidade do advogado",
     "assertiva": "Suspende-se o processo por 8 dias quando o advogado responsável pelo processo constituir o único patrono da causa e tornar-se pai.",
     "gabarito": "C",
     "comentario": {
      "resumo": "Art. 313, X e § 7º: **8 dias** para o pai; **30 dias** para a advogada, pelo parto ou adoção (IX e § 6º).",
      "lei": [
       {
        "lei": "L13105",
        "art": "313",
        "par": "",
        "inc": "",
        "rotulo": "CPC, art. 313, § 7º",
        "texto": "No caso do inciso X, o período de suspensão será de 8 (oito) dias"
       }
      ],
      "palavras_chave": [
       "suspensão",
       "advogado pai"
      ],
      "aprofundamento": "A suspensão pela paternidade do advogado protege o **direito à convivência familiar** e garante que o profissional possa acompanhar o nascimento ou a adoção de um filho sem prejudicar o cliente.\n\nOs requisitos são: o advogado deve ser o **único patrono** da causa, e deve comprovar o fato e notificar o cliente. A suspensão dura 8 dias, contados do parto ou da adoção.\n\nPara a advogada, a suspensão pelo parto ou adoção é maior, de 30 dias, porque envolve também a recuperação física e a amamentação. A banca costuma trocar os prazos ou dispensar o requisito de único patrono.",
      "memorize": "Advogado único patrono que se torna pai: suspensão por 8 dias. Advogada: 30 dias."
     }
    },
    {
     "id": "CPC-6-R2-04",
     "ponto": "DBA26-CPC-6",
     "tema": "Maternidade da advogada",
     "assertiva": "Pelo parto ou concessão de adoção, quando a advogada for a única patrona da causa, o processo fica suspenso por 60 dias.",
     "gabarito": "E",
     "comentario": {
      "resumo": "Art. 313, § 6º: **30 dias** contados do parto ou da adoção, mediante comprovação e notificação ao cliente.",
      "lei": [
       {
        "lei": "L13105",
        "art": "313",
        "par": "",
        "inc": "",
        "rotulo": "CPC, art. 313, § 6º",
        "texto": "No caso do inciso IX, o período de suspensão será de 30 (trinta) dias"
       }
      ],
      "palavras_chave": [
       "suspensão",
       "advogada",
       "30 dias"
      ],
      "correcao": {
       "erro": "Fixa em 60 dias a suspensão do processo pelo parto ou adoção da advogada.",
       "certo": "Pelo parto ou adoção, sendo a advogada a única patrona da causa, o processo fica suspenso por 30 dias, mediante comprovação e notificação ao cliente."
      },
      "aprofundamento": "A suspensão pelo parto ou adoção da advogada protege a **maternidade** e o vínculo inicial com o filho. Ela permite que a profissional se afaste por um período sem que o cliente sofra com a perda de prazos.\n\nOs requisitos são: a advogada deve ser a **única patrona** da causa, comprovar o parto ou a adoção e notificar o cliente. A suspensão dura 30 dias, contados do parto ou da concessão da adoção.\n\nA banca aumenta o prazo para 60 dias. Lembre que esse prazo não se confunde com a licença-maternidade, que é instituto trabalhista ou previdenciário, com outra duração.",
      "memorize": "Advogada única patrona: parto ou adoção suspende por 30 dias."
     }
    },
    {
     "id": "CPC-6-R2-05",
     "ponto": "DBA26-CPC-6",
     "tema": "Retratação na apelação",
     "assertiva": "Interposta apelação contra sentença sem resolução de mérito, o juiz terá 5 dias para retratar-se.",
     "gabarito": "C",
     "comentario": {
      "resumo": "**Art. 485, § 7º**.",
      "lei": [
       {
        "lei": "L13105",
        "art": "485",
        "par": "",
        "inc": "",
        "rotulo": "CPC, art. 485, § 7º",
        "texto": "Interposta a apelação em qualquer dos casos de que tratam os incisos deste artigo, o juiz terá 5 (cinco) dias para retratar-se."
       }
      ],
      "palavras_chave": [
       "retratação",
       "efeito regressivo"
      ],
      "aprofundamento": "A **retratação** do juiz na apelação contra sentença sem resolução de mérito é uma expressão da **primazia do mérito**. Se o juiz perceber que errou ao extinguir o processo, pode corrigir a decisão sem que o caso precise subir ao tribunal.\n\nO prazo é de 5 dias. Se o juiz se retratar, o processo retoma seu curso; se não, os autos sobem ao tribunal.\n\nA regra se aplica a qualquer sentença sem resolução de mérito. Não confunda com a retratação nas sentenças com mérito, que só ocorre em hipóteses específicas, como a improcedência liminar. A banca costuma estender a retratação a qualquer apelação ou alterar o prazo.",
      "memorize": "Apelação contra sentença sem mérito: juiz pode se retratar em 5 dias."
     }
    },
    {
     "id": "CPC-6-R2-06",
     "ponto": "DBA26-CPC-6",
     "tema": "Repropositura",
     "assertiva": "A sentença que extingue o processo por ilegitimidade de parte impede, em qualquer caso, a propositura de nova ação.",
     "gabarito": "E",
     "comentario": {
      "resumo": "Art. 486, § 1º: nova ação é possível, mas depende da **correção do vício** que levou à extinção.",
      "lei": [
       {
        "lei": "L13105",
        "art": "486",
        "par": "",
        "inc": "",
        "rotulo": "CPC, art. 486, § 1º",
        "texto": "No caso de extinção em razão de litispendência e nos casos dos incisos I, IV, VI e VII do art. 485, a propositura da nova ação depende da correção do vício que levou à sentença sem resolução do mérito."
       }
      ],
      "palavras_chave": [
       "repropositura",
       "correção do vício"
      ],
      "correcao": {
       "erro": "Afirma que a extinção por ilegitimidade impede, em qualquer caso, a propositura de nova ação.",
       "certo": "Extinto o processo por ilegitimidade, a propositura de nova ação é possível, mas depende da correção do vício que levou à sentença sem resolução do mérito."
      },
      "aprofundamento": "A sentença sem resolução do mérito, em regra, **não impede** a propositura de nova ação, porque não decidiu o conflito. Mas, em alguns casos, a nova ação só é possível se o vício que levou à extinção for corrigido.\n\nA ilegitimidade é um desses casos. Se a primeira ação foi extinta porque o autor não era parte legítima, propor a mesma ação, com o mesmo autor, levaria ao mesmo resultado. É preciso corrigir o vício, por exemplo, trazendo a parte legítima.\n\nAs outras hipóteses em que a repropositura depende da correção do vício são a litispendência, o indeferimento da inicial, a falta de pressupostos processuais, a falta de interesse e a convenção de arbitragem. A assertiva cria uma vedação absoluta que a lei não prevê.",
      "memorize": "Extinção por ilegitimidade: nova ação só corrigindo o vício."
     }
    },
    {
     "id": "CPC-6-R2-07",
     "ponto": "DBA26-CPC-6",
     "tema": "Intimação pessoal antes da extinção",
     "assertiva": "Nos casos de paralisação do processo por mais de 1 ano por negligência das partes e de abandono pelo autor, a parte será intimada pessoalmente para suprir a falta no prazo de 5 dias.",
     "gabarito": "C",
     "comentario": {
      "resumo": "**Art. 485, § 1º**.",
      "lei": [
       {
        "lei": "L13105",
        "art": "485",
        "par": "",
        "inc": "",
        "rotulo": "CPC, art. 485, § 1º",
        "texto": "Nas hipóteses descritas nos incisos II e III, a parte será intimada pessoalmente para suprir a falta no prazo de 5 (cinco) dias."
       }
      ],
      "palavras_chave": [
       "intimação pessoal",
       "abandono"
      ],
      "aprofundamento": "A paralisação do processo por negligência das partes e o abandono da causa pelo autor levam à extinção sem resolução do mérito. Mas a lei não permite que isso ocorra sem dar à parte uma última chance.\n\nA **intimação pessoal** é exigida porque a inércia pode ter várias causas, inclusive falhas na comunicação com o advogado. Intimar a própria parte garante que ela saiba do risco e possa agir. O prazo para suprir a falta é de 5 dias.\n\nA paralisação por negligência de ambas as partes deve durar mais de 1 ano; o abandono pelo autor caracteriza-se por ele não promover os atos e diligências que lhe incumbem. Lembre que, depois da contestação, a extinção por abandono depende de requerimento do réu.",
      "memorize": "Antes de extinguir por paralisação ou abandono: intimação pessoal da parte, 5 dias para suprir."
     }
    },
    {
     "id": "CPC-6-R2-08",
     "ponto": "DBA26-CPC-6",
     "tema": "Prescrição e contraditório",
     "assertiva": "Ressalvada a improcedência liminar, a prescrição e a decadência não serão reconhecidas sem que antes seja dada às partes oportunidade de manifestar-se.",
     "gabarito": "C",
     "comentario": {
      "resumo": "**Art. 487**, par. ún. — aplicação direta do art. 10.",
      "lei": [
       {
        "lei": "L13105",
        "art": "487",
        "par": "",
        "inc": "",
        "rotulo": "CPC, art. 487, par. ún.",
        "texto": "Ressalvada a hipótese do § 1º do art. 332, a prescrição e a decadência não serão reconhecidas sem que antes seja dada às partes oportunidade de manifestar-se."
       }
      ],
      "palavras_chave": [
       "prescrição",
       "contraditório"
      ],
      "aprofundamento": "A prescrição e a decadência são matérias que o juiz pode conhecer de ofício. Mas conhecer de ofício não significa decidir sem ouvir: a **vedação à decisão surpresa** se aplica plenamente.\n\nPor isso o juiz deve dar às partes oportunidade de se manifestar antes de reconhecer a prescrição ou a decadência. A parte pode demonstrar, por exemplo, que houve causa interruptiva ou suspensiva que o juiz não conhecia.\n\nA exceção é a **improcedência liminar**: nesse caso, o réu nem foi citado, e o juiz pode reconhecer a prescrição ou decadência de plano. Mesmo assim, o autor pode apelar, e o juiz pode se retratar. A banca costuma dispensar o contraditório por se tratar de matéria de ordem pública.",
      "memorize": "Prescrição e decadência: ouvir as partes antes, salvo improcedência liminar."
     }
    },
    {
     "id": "CPC-6-R2-09",
     "ponto": "DBA26-CPC-6",
     "tema": "Questão prejudicial externa",
     "assertiva": "A suspensão do processo por depender o julgamento do mérito de outra causa pode durar até 2 anos.",
     "gabarito": "E",
     "comentario": {
      "resumo": "Art. 313, § 4º: **nunca mais de 1 ano** nas hipóteses do inciso V; findo o prazo, o juiz manda prosseguir (§ 5º).",
      "lei": [
       {
        "lei": "L13105",
        "art": "313",
        "par": "",
        "inc": "",
        "rotulo": "CPC, art. 313, § 4º",
        "texto": "O prazo de suspensão do processo nunca poderá exceder 1 (um) ano nas hipóteses do inciso V"
       }
      ],
      "palavras_chave": [
       "prejudicialidade",
       "1 ano"
      ],
      "correcao": {
       "erro": "Fixa em 2 anos o prazo máximo da suspensão por questão prejudicial externa.",
       "certo": "A suspensão do processo por depender o julgamento de outra causa nunca pode exceder 1 ano; findo o prazo, o juiz manda prosseguir."
      },
      "aprofundamento": "A suspensão por **questão prejudicial externa** ocorre quando o julgamento do mérito depende do resultado de outra causa ou da verificação de fato ou prova a ser obtida em outro juízo. Ela evita decisões contraditórias.\n\nMas a lei impõe um teto: a suspensão nunca pode exceder 1 ano. Findo esse prazo, o juiz manda prosseguir o processo, e decide a questão incidentemente, se necessário.\n\nA lógica é equilibrar a coerência entre decisões com a duração razoável do processo. A banca aumenta o prazo para 2 anos. Lembre a dupla: prejudicialidade, 1 ano; convenção das partes, 6 meses.",
      "memorize": "Prejudicialidade externa: suspensão por no máximo 1 ano."
     }
    },
    {
     "id": "CPC-7-R2-01",
     "ponto": "DBA26-CPC-7",
     "tema": "Autonomia da reconvenção",
     "assertiva": "A desistência da ação ou a ocorrência de causa extintiva que impeça o exame de seu mérito não obsta o prosseguimento do processo quanto à reconvenção.",
     "gabarito": "C",
     "comentario": {
      "resumo": "Art. 343, § 2º: **autonomia** da reconvenção.",
      "lei": [
       {
        "lei": "L13105",
        "art": "343",
        "par": "",
        "inc": "",
        "rotulo": "CPC, art. 343, § 2º",
        "texto": "A desistência da ação ou a ocorrência de causa extintiva que impeça o exame de seu mérito não obsta ao prosseguimento do processo quanto à reconvenção."
       }
      ],
      "palavras_chave": [
       "reconvenção",
       "autonomia"
      ],
      "aprofundamento": "A **reconvenção** é a ação do réu contra o autor, proposta no mesmo processo. Embora tramite junto com a ação principal, ela tem **autonomia**: é uma demanda própria, com pedido e causa de pedir próprios.\n\nPor isso, se a ação principal for extinta, seja por desistência do autor, seja por qualquer causa que impeça o exame do mérito, a reconvenção continua. Seria injusto que o réu-reconvinte perdesse sua demanda por um fato que diz respeito apenas à ação do autor.\n\nA reconvenção pode ser proposta inclusive contra o autor e terceiro, ou pelo réu em litisconsórcio com terceiro. A banca costuma tratar a reconvenção como acessória, extinguindo-a junto com a ação principal.",
      "memorize": "Reconvenção é autônoma: segue mesmo com desistência ou extinção da ação principal."
     }
    },
    {
     "id": "CPC-7-R2-02",
     "ponto": "DBA26-CPC-7",
     "tema": "Julgamento antecipado parcial",
     "assertiva": "A decisão que julga antecipadamente parte do mérito é impugnável por apelação.",
     "gabarito": "E",
     "comentario": {
      "resumo": "Art. 356, § 5º: cabe **agravo de instrumento** (decisão interlocutória de mérito).",
      "lei": [
       {
        "lei": "L13105",
        "art": "356",
        "par": "",
        "inc": "",
        "rotulo": "CPC, art. 356, § 5º",
        "texto": "A decisão proferida com base neste artigo é impugnável por agravo de instrumento."
       }
      ],
      "palavras_chave": [
       "julgamento parcial",
       "agravo de instrumento"
      ],
      "correcao": {
       "erro": "Indica a apelação como recurso contra a decisão que julga antecipadamente parte do mérito.",
       "certo": "A decisão que julga antecipadamente parte do mérito é impugnável por agravo de instrumento."
      },
      "aprofundamento": "O **julgamento antecipado parcial do mérito** permite que o juiz decida desde logo a parte do pedido que já está madura, enquanto o restante segue para instrução. É expressão da efetividade: não há razão para fazer o autor esperar por algo que já pode ser decidido.\n\nComo essa decisão não encerra a fase de conhecimento, ela não é sentença, e sim **interlocutória de mérito**. Por isso o recurso cabível é o **agravo de instrumento**, e não a apelação.\n\nA decisão parcial pode fazer coisa julgada material sobre a parte decidida e permite liquidação e execução imediata. A banca confunde o conteúdo (mérito) com a natureza (interlocutória), sugerindo apelação.",
      "memorize": "Julgamento parcial do mérito = interlocutória = agravo de instrumento."
     }
    },
    {
     "id": "CPC-7-R2-03",
     "ponto": "DBA26-CPC-7",
     "tema": "Saneamento consensual",
     "assertiva": "As partes podem apresentar ao juiz, para homologação, delimitação consensual das questões de fato e de direito, que, se homologada, vincula as partes e o juiz.",
     "gabarito": "C",
     "comentario": {
      "resumo": "Art. 357, § 2º: **saneamento consensual**.",
      "lei": [
       {
        "lei": "L13105",
        "art": "357",
        "par": "",
        "inc": "",
        "rotulo": "CPC, art. 357, § 2º",
        "texto": "As partes podem apresentar ao juiz, para homologação, delimitação consensual das questões de fato e de direito a que se referem os incisos II e IV, a qual, se homologada, vincula as partes e o juiz."
       }
      ],
      "palavras_chave": [
       "saneamento",
       "negócio processual"
      ],
      "aprofundamento": "O **saneamento consensual** é uma forma de negócio processual típico: as partes, em vez de esperar que o juiz delimite as questões controvertidas, apresentam elas mesmas essa delimitação. É expressão do modelo cooperativo do processo.\n\nSe o juiz homologar, a delimitação **vincula as partes e o juiz**. A questão de fato e de direito que ficou de fora não será mais discutida, e a instrução se concentrará no que as partes indicaram.\n\nO juiz não é obrigado a homologar; pode recusar se a delimitação for inadequada. Mas, homologada, ele também fica vinculado. A banca costuma dizer que a delimitação vincula só as partes, ou que o juiz pode desconsiderá-la livremente depois de homologada.",
      "memorize": "Saneamento consensual homologado vincula partes e juiz."
     }
    },
    {
     "id": "CPC-7-R2-04",
     "ponto": "DBA26-CPC-7",
     "tema": "Coisa julgada sobre questão prejudicial",
     "assertiva": "A coisa julgada alcança a questão prejudicial decidida expressa e incidentemente, ainda que o réu tenha sido revel.",
     "gabarito": "E",
     "comentario": {
      "resumo": "Art. 503, § 1º, II: exige **contraditório prévio e efetivo**, **não se aplicando no caso de revelia**.",
      "lei": [
       {
        "lei": "L13105",
        "art": "503",
        "par": "",
        "inc": "",
        "rotulo": "CPC, art. 503, § 1º, II",
        "texto": "II - a seu respeito tiver havido contraditório prévio e efetivo, não se aplicando no caso de revelia;"
       }
      ],
      "palavras_chave": [
       "questão prejudicial",
       "revelia"
      ],
      "correcao": {
       "erro": "Estende a coisa julgada à questão prejudicial mesmo no caso de revelia.",
       "certo": "A coisa julgada sobre a questão prejudicial exige contraditório prévio e efetivo, não se aplicando no caso de revelia."
      },
      "aprofundamento": "O CPC atual inovou ao permitir que a **questão prejudicial**, decidida expressa e incidentalmente, faça coisa julgada. Antes, só o pedido fazia coisa julgada. Mas, para isso, a lei exige requisitos que garantam que a questão foi realmente debatida.\n\nUm desses requisitos é o **contraditório prévio e efetivo**. Na revelia, o réu não se defendeu, e não houve debate real sobre a questão. Estender a coisa julgada a ela seria impor ao réu uma decisão sobre algo que ele não discutiu.\n\nOs demais requisitos são: a resolução da questão deve ser necessária para o julgamento do mérito, e o juízo deve ser competente em razão da matéria e da pessoa para resolvê-la como questão principal. A assertiva ignora a exclusão expressa da revelia.",
      "memorize": "Prejudicial faz coisa julgada só com contraditório efetivo; revelia afasta."
     }
    },
    {
     "id": "CPC-7-R2-05",
     "ponto": "DBA26-CPC-7",
     "tema": "Remessa necessária — Estados",
     "assertiva": "Não se aplica a remessa necessária quando a condenação ou o proveito econômico for inferior a 500 salários mínimos para os Estados, o DF, suas autarquias e fundações e os Municípios que sejam capitais.",
     "gabarito": "C",
     "comentario": {
      "resumo": "**Art. 496, § 3º, II**. União: 1.000 SM; demais Municípios: 100 SM.",
      "lei": [
       {
        "lei": "L13105",
        "art": "496",
        "par": "",
        "inc": "",
        "rotulo": "CPC, art. 496, § 3º, II",
        "texto": "II - 500 (quinhentos) salários-mínimos para os Estados, o Distrito Federal, as respectivas autarquias e fundações de direito público e os Municípios que constituam capitais dos Estados;"
       }
      ],
      "palavras_chave": [
       "remessa necessária",
       "500 salários mínimos"
      ],
      "aprofundamento": "A **remessa necessária** obriga o reexame pelo tribunal de sentenças contrárias à Fazenda Pública, mesmo sem recurso. A ideia é proteger o patrimônio público contra erros ou omissões na defesa. Mas reexaminar todas as condenações, inclusive as de pequeno valor, sobrecarregaria os tribunais sem justificativa.\n\nPor isso a lei fixa **limites de valor** escalonados conforme o porte do ente: 1.000 salários mínimos para a União e suas autarquias e fundações; 500 para os Estados, o DF, suas autarquias e fundações e os Municípios que sejam capitais; e 100 para os demais Municípios.\n\nA lógica é proporcional: quanto maior o ente, maior o valor que ele suporta sem risco relevante. A banca costuma trocar os limites entre os entes.",
      "memorize": "Remessa dispensada abaixo de: União 1.000 SM; Estados, DF e capitais 500 SM; demais Municípios 100 SM."
     }
    },
    {
     "id": "CPC-7-R2-06",
     "ponto": "DBA26-CPC-7",
     "tema": "Remessa necessária — Municípios",
     "assertiva": "O limite de 500 salários mínimos para dispensa da remessa necessária aplica-se a todos os Municípios.",
     "gabarito": "E",
     "comentario": {
      "resumo": "Só aos **Municípios capitais**. Os demais Municípios têm limite de **100 SM** (art. 496, § 3º, III).",
      "lei": [
       {
        "lei": "L13105",
        "art": "496",
        "par": "",
        "inc": "",
        "rotulo": "CPC, art. 496, § 3º, III",
        "texto": "III - 100 (cem) salários-mínimos para todos os demais Municípios e respectivas autarquias e fundações de direito público."
       }
      ],
      "palavras_chave": [
       "remessa necessária",
       "100 salários mínimos"
      ],
      "correcao": {
       "erro": "Aplica a todos os Municípios o limite de 500 salários mínimos para dispensa da remessa necessária.",
       "certo": "O limite de 500 salários mínimos vale para Estados, DF, suas autarquias e fundações e Municípios capitais; os demais Municípios têm limite de 100 salários mínimos."
      },
      "aprofundamento": "Os limites da remessa necessária variam conforme a **capacidade financeira** do ente. Municípios que são capitais têm orçamentos maiores e estrutura jurídica mais robusta, e por isso estão no mesmo patamar dos Estados, com limite de 500 salários mínimos.\n\nOs **demais Municípios**, com orçamentos menores, ficam no limite de 100 salários mínimos. Para eles, condenações de valor menor já representam impacto relevante, e o reexame obrigatório continua justificado.\n\nA assertiva generaliza para todos os Municípios o limite que vale só para as capitais. Na prova, atenção à palavra \"todos\": a lei distingue capitais dos demais.",
      "memorize": "500 SM: só Municípios capitais. Demais Municípios: 100 SM."
     }
    },
    {
     "id": "CPC-7-R2-07",
     "ponto": "DBA26-CPC-7",
     "tema": "Cumprimento provisório",
     "assertiva": "O cumprimento provisório corre por iniciativa e responsabilidade do exequente, que se obriga, se a sentença for reformada, a reparar os danos que o executado haja sofrido.",
     "gabarito": "C",
     "comentario": {
      "resumo": "Art. 520, I: responsabilidade **objetiva** do exequente.",
      "lei": [
       {
        "lei": "L13105",
        "art": "520",
        "par": "",
        "inc": "",
        "rotulo": "CPC, art. 520, I",
        "texto": "corre por iniciativa e responsabilidade do exequente, que se obriga, se a sentença for reformada, a reparar os danos que o executado haja sofrido;"
       }
      ],
      "palavras_chave": [
       "cumprimento provisório",
       "responsabilidade"
      ],
      "aprofundamento": "O **cumprimento provisório** permite executar uma sentença ainda sujeita a recurso sem efeito suspensivo. É uma forma de dar efetividade à decisão sem esperar o trânsito em julgado. Mas há um risco: a sentença pode ser reformada.\n\nPor isso a lei coloca o risco sobre quem escolheu executar antes do tempo. O exequente age **por sua iniciativa e responsabilidade**, e se a sentença for reformada, deve reparar os danos sofridos pelo executado. Essa responsabilidade é **objetiva**: independe de culpa.\n\nA lei também prevê que o levantamento de dinheiro e a prática de atos que importem transferência de posse ou alienação dependem, em regra, de caução. A banca costuma exigir culpa do exequente ou dizer que o cumprimento provisório começa de ofício.",
      "memorize": "Cumprimento provisório: por conta e risco do exequente, que repara os danos se a sentença cair."
     }
    },
    {
     "id": "CPC-7-R2-08",
     "ponto": "DBA26-CPC-7",
     "tema": "Astreintes — intimação pessoal",
     "assertiva": "Para o STJ, a prévia intimação pessoal do devedor é pressuposto para a incidência da multa coercitiva pelo descumprimento de obrigação de fazer ou não fazer, entendimento mantido após o CPC/2015.",
     "gabarito": "C",
     "comentario": {
      "resumo": "Súmula 410/STJ, reafirmada pela Corte Especial no **Tema 1.296** (2026).",
      "lei": [
       {
        "lei": "L13105",
        "art": "537",
        "par": "",
        "inc": "",
        "rotulo": "CPC, art. 537",
        "texto": "A multa independe de requerimento da parte e poderá ser aplicada na fase de conhecimento, em tutela provisória ou na sentença, ou na fase de execução, desde que seja suficiente e compatível com a obrigação e que se determine prazo razoável para cumprimento do preceito."
       }
      ],
      "juris": [
       {
        "tribunal": "STJ",
        "fonte": "Súmula 410/STJ",
        "data": "25/11/2009",
        "texto": "A prévia intimação pessoal do devedor é condição necessária para a cobrança de multa pelo descumprimento de obrigação de fazer ou não fazer."
       },
       {
        "tribunal": "STJ",
        "fonte": "Tema 1.296/STJ — REsp 2.096.505/SP e outros",
        "data": "04/03/2026",
        "texto": "A prévia intimação pessoal do devedor para cumprir obrigação de fazer ou não fazer é pressuposto da multa coercitiva; a Súmula 410 permanece hígida após o CPC/2015."
       }
      ],
      "palavras_chave": [
       "astreintes",
       "intimação pessoal",
       "Tema 1.296"
      ],
      "aprofundamento": "A multa coercitiva, ou **astreinte**, pressiona o devedor a cumprir obrigação de fazer ou não fazer. Para que ela incida, é preciso que o devedor saiba, de forma inequívoca, que deve cumprir a ordem e qual a consequência do descumprimento.\n\nA Súmula 410/STJ exige a **intimação pessoal** do devedor como condição para cobrar a multa. Com o CPC atual, discutiu-se se bastaria a intimação do advogado. O STJ, no **Tema 1.296**, reafirmou a súmula: a intimação pessoal continua sendo pressuposto.\n\nA razão é que a obrigação de fazer depende de conduta pessoal do devedor, e não do advogado. A banca costuma dizer que a súmula foi superada pelo CPC, ou que basta a intimação pelo advogado.",
      "memorize": "Astreintes: exige intimação pessoal do devedor (Súmula 410 e Tema 1.296/STJ)."
     }
    },
    {
     "id": "CPC-7-R2-09",
     "ponto": "DBA26-CPC-7",
     "tema": "Astreintes — de ofício",
     "assertiva": "A multa coercitiva para cumprimento de obrigação de fazer depende de requerimento da parte.",
     "gabarito": "E",
     "comentario": {
      "resumo": "Art. 537: a multa **independe de requerimento** e pode ser fixada em qualquer fase; o juiz pode alterar a **multa vincenda** de ofício (§ 1º).",
      "lei": [
       {
        "lei": "L13105",
        "art": "537",
        "par": "",
        "inc": "",
        "rotulo": "CPC, art. 537",
        "texto": "A multa independe de requerimento da parte"
       }
      ],
      "palavras_chave": [
       "astreintes",
       "de ofício"
      ],
      "correcao": {
       "erro": "Condiciona a multa coercitiva ao requerimento da parte.",
       "certo": "A multa coercitiva independe de requerimento da parte e pode ser aplicada em qualquer fase do processo; o juiz pode alterar de ofício a multa vincenda."
      },
      "aprofundamento": "A multa coercitiva é instrumento do juiz para garantir a **efetividade** de suas decisões. Por isso não depende de pedido da parte: o juiz pode fixá-la de ofício, sempre que entender necessária para compelir o devedor a cumprir a obrigação.\n\nEla pode ser aplicada em qualquer fase: na fase de conhecimento, em tutela provisória, na sentença ou na execução. Deve ser suficiente e compatível com a obrigação, e o juiz deve fixar prazo razoável para o cumprimento.\n\nO juiz pode, também de ofício, alterar o valor ou a periodicidade da **multa vincenda** se ela se tornar insuficiente ou excessiva. Repare que o texto fala em multa vincenda, isto é, a que ainda vai incidir. A banca costuma exigir requerimento da parte.",
      "memorize": "Astreintes: independe de pedido, cabe em qualquer fase; juiz altera a vincenda de ofício."
     }
    },
    {
     "id": "CPC-7-R2-10",
     "ponto": "DBA26-CPC-7",
     "tema": "Pagamento parcial",
     "assertiva": "Efetuado o pagamento parcial no prazo do cumprimento de sentença, ficam afastados integralmente a multa e os honorários de 10%.",
     "gabarito": "E",
     "comentario": {
      "resumo": "Art. 523, § 2º: multa e honorários incidem **sobre o restante**.",
      "lei": [
       {
        "lei": "L13105",
        "art": "523",
        "par": "",
        "inc": "",
        "rotulo": "CPC, art. 523, § 2º",
        "texto": "Efetuado o pagamento parcial no prazo previsto no caput , a multa e os honorários previstos no § 1º incidirão sobre o restante."
       }
      ],
      "palavras_chave": [
       "pagamento parcial",
       "restante"
      ],
      "correcao": {
       "erro": "Afasta integralmente a multa e os honorários quando há pagamento parcial no prazo.",
       "certo": "Efetuado o pagamento parcial no prazo, a multa e os honorários de 10% incidem sobre o restante."
      },
      "aprofundamento": "A multa e os honorários do cumprimento de sentença servem para estimular o pagamento voluntário. Se o devedor paga parte da dívida no prazo, demonstra boa vontade, e seria desproporcional aplicar a multa sobre o valor que já foi pago.\n\nPor isso a lei determina que, havendo pagamento parcial, multa e honorários incidam **apenas sobre o restante**. O devedor não fica isento, mas também não é punido pelo que já pagou.\n\nEsse critério é proporcional: incentiva o pagamento, ainda que parcial, sem eliminar a pressão sobre o saldo devedor. A assertiva elimina totalmente a multa e os honorários, o que contraria o texto legal.",
      "memorize": "Pagamento parcial: multa e honorários só sobre o saldo."
     }
    },
    {
     "id": "CPC-8-R2-01",
     "ponto": "DBA26-CPC-8",
     "tema": "Averbação premonitória",
     "assertiva": "Presume-se em fraude à execução a alienação ou a oneração de bens efetuada após a averbação da certidão de admissão da execução.",
     "gabarito": "C",
     "comentario": {
      "resumo": "**Art. 828, § 4º**.",
      "lei": [
       {
        "lei": "L13105",
        "art": "828",
        "par": "",
        "inc": "",
        "rotulo": "CPC, art. 828, § 4º",
        "texto": "Presume-se em fraude à execução a alienação ou a oneração de bens efetuada após a averbação."
       }
      ],
      "palavras_chave": [
       "averbação premonitória",
       "fraude"
      ],
      "aprofundamento": "A **averbação premonitória** permite ao exequente averbar, no registro de imóveis, veículos ou outros bens, a certidão de que a execução foi admitida. É uma forma de dar publicidade à existência da execução antes mesmo da penhora.\n\nA consequência é que, depois da averbação, a alienação ou oneração dos bens **presume-se em fraude à execução**. O terceiro adquirente não poderá alegar desconhecimento, porque o registro era público.\n\nO instituto protege o credor contra o devedor que tenta se desfazer dos bens no início da execução. Em contrapartida, o exequente responde por averbação manifestamente indevida ou que não cancele quando os bens não forem penhorados. A banca costuma exigir a penhora para a presunção.",
      "memorize": "Averbação da admissão da execução: alienação posterior presume-se fraude."
     }
    },
    {
     "id": "CPC-8-R2-02",
     "ponto": "DBA26-CPC-8",
     "tema": "Intimação do terceiro adquirente",
     "assertiva": "Antes de declarar a fraude à execução, o juiz deverá intimar o terceiro adquirente, que poderá opor embargos de terceiro no prazo de 5 dias.",
     "gabarito": "E",
     "comentario": {
      "resumo": "Art. 792, § 4º: prazo de **15 dias**.",
      "lei": [
       {
        "lei": "L13105",
        "art": "792",
        "par": "",
        "inc": "",
        "rotulo": "CPC, art. 792, § 4º",
        "texto": "Antes de declarar a fraude à execução, o juiz deverá intimar o terceiro adquirente, que, se quiser, poderá opor embargos de terceiro, no prazo de 15 (quinze) dias."
       }
      ],
      "palavras_chave": [
       "embargos de terceiro",
       "15 dias"
      ],
      "correcao": {
       "erro": "Fixa em 5 dias o prazo para o terceiro adquirente opor embargos de terceiro.",
       "certo": "Antes de declarar a fraude à execução, o juiz deve intimar o terceiro adquirente, que poderá opor embargos de terceiro no prazo de 15 dias."
      },
      "aprofundamento": "A fraude à execução atinge o terceiro que adquiriu o bem do devedor. Antes de declarar essa fraude, a lei exige que o juiz **intime o terceiro**, garantindo-lhe o contraditório. Ele pode demonstrar, por exemplo, que agiu de boa-fé ou que o bem não estava sujeito à execução.\n\nO meio de defesa são os **embargos de terceiro**, no prazo de 15 dias. É o mesmo prazo geral de defesa, adequado para que o terceiro organize sua argumentação e prova.\n\nA banca reduz o prazo para 5 dias. Lembre a lógica do sistema: prazos de defesa costumam ser de 15 dias, e esse é um deles.",
      "memorize": "Fraude à execução: terceiro intimado pode embargar em 15 dias."
     }
    },
    {
     "id": "CPC-8-R2-03",
     "ponto": "DBA26-CPC-8",
     "tema": "Salário e prestação alimentícia",
     "assertiva": "A impenhorabilidade de salários e vencimentos não se aplica à penhora para pagamento de prestação alimentícia, independentemente de sua origem.",
     "gabarito": "C",
     "comentario": {
      "resumo": "**Art. 833, § 2º**. A mesma ressalva vale para importâncias que excedam 50 salários mínimos mensais.",
      "lei": [
       {
        "lei": "L13105",
        "art": "833",
        "par": "",
        "inc": "",
        "rotulo": "CPC, art. 833, § 2º",
        "texto": "O disposto nos incisos IV e X do caput não se aplica à hipótese de penhora para pagamento de prestação alimentícia, independentemente de sua origem"
       }
      ],
      "palavras_chave": [
       "impenhorabilidade",
       "alimentos"
      ],
      "aprofundamento": "A impenhorabilidade de salários e da poupança protege o **sustento** do devedor e de sua família. Mas, quando a dívida é de alimentos, há um conflito entre o sustento do devedor e o sustento do credor, que muitas vezes depende dos alimentos para sobreviver.\n\nA lei resolve esse conflito em favor do credor de alimentos. A impenhorabilidade dos incisos IV e X não se aplica à penhora para pagamento de prestação alimentícia, **independentemente de sua origem**, ou seja, alimentos decorrentes de parentesco, de ato ilícito ou de qualquer outra fonte.\n\nA mesma ressalva vale para as importâncias que excedam 50 salários mínimos mensais, que perdem a proteção. A banca costuma restringir a exceção aos alimentos de família.",
      "memorize": "Salário e poupança são penhoráveis para alimentos de qualquer origem."
     }
    },
    {
     "id": "CPC-8-R2-04",
     "ponto": "DBA26-CPC-8",
     "tema": "Medidas executivas atípicas",
     "assertiva": "Segundo o STJ, nas execuções cíveis o juiz pode adotar meios executivos atípicos de forma prioritária, dispensada a ponderação com a menor onerosidade do executado.",
     "gabarito": "E",
     "comentario": {
      "resumo": "Tema 1.137/STJ: cabem, mas **cumulativamente** com ponderação efetividade x **menor onerosidade**, uso **prioritariamente subsidiário**, fundamentação e contraditório/proporcionalidade.",
      "lei": [
       {
        "lei": "L13105",
        "art": "139",
        "par": "",
        "inc": "",
        "rotulo": "CPC, art. 139, IV",
        "texto": "IV - determinar todas as medidas indutivas, coercitivas, mandamentais ou sub-rogatórias necessárias para assegurar o cumprimento de ordem judicial, inclusive nas ações que tenham por objeto prestação pecuniária;"
       }
      ],
      "juris": [
       {
        "tribunal": "STJ",
        "fonte": "Tema 1.137/STJ — REsp 1.955.539/SP e REsp 1.955.574/SP",
        "data": "04/12/2025",
        "texto": "Meios executivos atípicos cabem desde que, cumulativamente: ponderadas efetividade e menor onerosidade; uso prioritariamente subsidiário; fundamentação adequada; contraditório, proporcionalidade e razoabilidade, inclusive quanto à duração."
       }
      ],
      "palavras_chave": [
       "medidas atípicas",
       "Tema 1.137",
       "subsidiariedade"
      ],
      "correcao": {
       "erro": "Admite os meios atípicos de forma prioritária e sem ponderação com a menor onerosidade.",
       "certo": "Para o STJ (Tema 1.137), meios executivos atípicos cabem de forma prioritariamente subsidiária, com ponderação entre efetividade e menor onerosidade, fundamentação adequada, contraditório e proporcionalidade."
      },
      "aprofundamento": "O código permite ao juiz adotar **medidas executivas atípicas**, como a suspensão da CNH ou a apreensão de passaporte, para forçar o cumprimento de obrigações. A finalidade é dar efetividade à execução quando os meios típicos falham.\n\nMas essas medidas atingem direitos fundamentais e exigem cautela. O STJ, no **Tema 1.137**, fixou requisitos **cumulativos**: ponderação entre efetividade e **menor onerosidade**; uso **prioritariamente subsidiário**, depois de esgotados os meios típicos; fundamentação adequada; e contraditório, proporcionalidade e razoabilidade, inclusive quanto à duração.\n\nA assertiva inverte a lógica: trata as medidas atípicas como prioritárias e dispensa a ponderação. Na verdade, elas são excepcionais.",
      "memorize": "Medidas atípicas: subsidiárias, ponderadas com a menor onerosidade, fundamentadas (Tema 1.137/STJ)."
     }
    },
    {
     "id": "CPC-8-R2-05",
     "ponto": "DBA26-CPC-8",
     "tema": "Parcelamento x embargos",
     "assertiva": "A opção pelo parcelamento do art. 916 importa renúncia ao direito de opor embargos.",
     "gabarito": "C",
     "comentario": {
      "resumo": "**Art. 916, § 6º**.",
      "lei": [
       {
        "lei": "L13105",
        "art": "916",
        "par": "",
        "inc": "",
        "rotulo": "CPC, art. 916, § 6º",
        "texto": "A opção pelo parcelamento de que trata este artigo importa renúncia ao direito de opor embargos"
       }
      ],
      "palavras_chave": [
       "parcelamento",
       "renúncia"
      ],
      "aprofundamento": "O parcelamento do art. 916 é um benefício para o executado que **reconhece o crédito**. Ao pedir o parcelamento, ele admite que deve e se compromete a pagar. Seria contraditório, depois disso, permitir que ele questionasse a dívida por meio de embargos.\n\nPor isso a opção pelo parcelamento importa **renúncia** ao direito de opor embargos. É a aplicação da vedação ao comportamento contraditório, decorrente da boa-fé processual.\n\nO executado faz uma escolha estratégica: ou discute a dívida por embargos, ou reconhece e parcela. Não pode fazer as duas coisas. A banca costuma dizer que o parcelamento é compatível com os embargos ou que o executado pode embargar depois de parcelar.",
      "memorize": "Pediu parcelamento? Renunciou aos embargos."
     }
    },
    {
     "id": "CPC-8-R2-06",
     "ponto": "DBA26-CPC-8",
     "tema": "Parcelamento no cumprimento de sentença",
     "assertiva": "O parcelamento do art. 916 aplica-se também ao cumprimento da sentença.",
     "gabarito": "E",
     "comentario": {
      "resumo": "Art. 916, § 7º: **não se aplica** ao cumprimento de sentença.",
      "lei": [
       {
        "lei": "L13105",
        "art": "916",
        "par": "",
        "inc": "",
        "rotulo": "CPC, art. 916, § 7º",
        "texto": "O disposto neste artigo não se aplica ao cumprimento da sentença."
       }
      ],
      "palavras_chave": [
       "parcelamento",
       "cumprimento de sentença"
      ],
      "correcao": {
       "erro": "Estende o parcelamento do art. 916 ao cumprimento de sentença.",
       "certo": "O parcelamento do art. 916 não se aplica ao cumprimento da sentença; é próprio da execução de título extrajudicial."
      },
      "aprofundamento": "O parcelamento do art. 916 foi pensado para a **execução de título extrajudicial**, em que o devedor ainda não teve a oportunidade de discutir a dívida em juízo. Ele funciona como alternativa aos embargos.\n\nNo **cumprimento de sentença**, a situação é diferente: o devedor já foi condenado depois de contraditório pleno, e já teve prazo para pagar voluntariamente. Permitir o parcelamento legal seria dar a ele um benefício adicional que a lei não quis conceder, contrariando a efetividade da sentença.\n\nNada impede que credor e devedor façam um acordo de parcelamento no cumprimento de sentença; o que não existe é o direito potestativo do devedor ao parcelamento legal. A banca estende o benefício ao cumprimento de sentença.",
      "memorize": "Parcelamento do art. 916: só execução extrajudicial, nunca cumprimento de sentença."
     }
    },
    {
     "id": "CPC-8-R2-07",
     "ponto": "DBA26-CPC-8",
     "tema": "Curador especial nos embargos",
     "assertiva": "O curador especial nomeado ao executado revel citado por edital não tem legitimidade para opor embargos à execução.",
     "gabarito": "E",
     "comentario": {
      "resumo": "Súmula 196/STJ: o curador especial **tem legitimidade** para apresentar embargos.",
      "lei": [
       {
        "lei": "L13105",
        "art": "72",
        "par": "",
        "inc": "",
        "rotulo": "CPC, art. 72, II",
        "texto": "revel citado por edital ou com hora certa"
       }
      ],
      "juris": [
       {
        "tribunal": "STJ",
        "fonte": "Súmula 196/STJ",
        "data": "01/10/1997",
        "texto": "Ao executado citado por edital ou por hora certa que permanecer revel será nomeado curador especial, com legitimidade para apresentar embargos."
       }
      ],
      "palavras_chave": [
       "curador especial",
       "embargos"
      ],
      "correcao": {
       "erro": "Nega ao curador especial do executado revel citado por edital legitimidade para opor embargos.",
       "certo": "Ao executado citado por edital ou hora certa que permanecer revel será nomeado curador especial, com legitimidade para apresentar embargos (Súmula 196/STJ)."
      },
      "aprofundamento": "O curador especial é nomeado ao executado citado por edital ou hora certa que permanece revel, porque há dúvida de que ele tenha efetivamente sabido da execução. Sua função é garantir o **contraditório** e a **ampla defesa**.\n\nSe o curador não pudesse opor embargos, sua nomeação seria inútil na execução, em que os embargos são o principal meio de defesa. Por isso a Súmula 196/STJ reconhece expressamente sua **legitimidade** para apresentá-los.\n\nO curador, normalmente a Defensoria Pública, pode alegar todas as matérias de defesa, inclusive por negação geral, se não tiver elementos concretos. A assertiva nega essa legitimidade, contrariando a súmula.",
      "memorize": "Curador especial do executado revel pode embargar (Súmula 196/STJ)."
     }
    },
    {
     "id": "CPC-8-R2-08",
     "ponto": "DBA26-CPC-8",
     "tema": "Exceção de pré-executividade",
     "assertiva": "A exceção de pré-executividade é admissível na execução fiscal relativamente às matérias conhecíveis de ofício que não demandem dilação probatória.",
     "gabarito": "C",
     "comentario": {
      "resumo": "Súmula 393/STJ: dois requisitos — matéria de **ordem pública** + **prova pré-constituída**.",
      "juris": [
       {
        "tribunal": "STJ",
        "fonte": "Súmula 393/STJ",
        "data": "23/09/2009",
        "texto": "A exceção de pré-executividade é admissível na execução fiscal relativamente às matérias conhecíveis de ofício que não demandem dilação probatória."
       }
      ],
      "palavras_chave": [
       "exceção de pré-executividade",
       "dilação probatória"
      ],
      "aprofundamento": "A **exceção de pré-executividade** é uma criação da doutrina e da jurisprudência: permite que o executado alegue certos vícios por simples petição nos autos da execução, sem precisar dos embargos. Na execução fiscal, onde os embargos exigem garantia, ela tem especial importância.\n\nA Súmula 393/STJ fixa dois requisitos **cumulativos**: a matéria deve ser **conhecível de ofício** (ordem pública, como prescrição, ilegitimidade ou nulidade do título) e não pode **demandar dilação probatória** (a prova deve ser pré-constituída, documental).\n\nA lógica é que, se o juiz poderia reconhecer o vício sozinho e há prova pronta, não faz sentido exigir os embargos. A banca costuma admitir a exceção para matérias que exigem perícia ou testemunhas.",
      "memorize": "Exceção de pré-executividade: matéria de ofício + sem dilação probatória (Súmula 393/STJ)."
     }
    },
    {
     "id": "CPC-8-R2-09",
     "ponto": "DBA26-CPC-8",
     "tema": "Execução contra a Fazenda",
     "assertiva": "Na execução fundada em título extrajudicial, a Fazenda Pública será citada para opor embargos em 15 dias.",
     "gabarito": "E",
     "comentario": {
      "resumo": "Art. 910: **30 dias**.",
      "lei": [
       {
        "lei": "L13105",
        "art": "910",
        "par": "",
        "inc": "",
        "rotulo": "CPC, art. 910",
        "texto": "a Fazenda Pública será citada para opor embargos em 30 (trinta) dias."
       }
      ],
      "palavras_chave": [
       "Fazenda Pública",
       "30 dias"
      ],
      "correcao": {
       "erro": "Fixa em 15 dias o prazo para a Fazenda Pública opor embargos na execução de título extrajudicial.",
       "certo": "Na execução fundada em título extrajudicial, a Fazenda Pública será citada para opor embargos em 30 dias."
      },
      "aprofundamento": "A execução contra a Fazenda Pública tem regime especial porque os bens públicos são **impenhoráveis** e o pagamento segue a ordem de precatórios ou requisições de pequeno valor. A Fazenda não é citada para pagar, mas para **opor embargos**.\n\nO prazo é de 30 dias, maior que o prazo geral de 15 dias dos embargos, em razão da estrutura da advocacia pública e da complexidade das defesas. Não se aplica a dobra, porque a lei já fixou prazo próprio para o ente.\n\nSe não houver embargos ou se forem rejeitados, expede-se precatório ou requisição de pequeno valor. A banca aplica à Fazenda o prazo geral dos embargos.",
      "memorize": "Execução contra a Fazenda: citada para embargar em 30 dias (sem dobra)."
     }
    },
    {
     "id": "CPC-8-R2-10",
     "ponto": "DBA26-CPC-8",
     "tema": "Menor onerosidade",
     "assertiva": "Quando por vários meios o exequente puder promover a execução, o juiz mandará que se faça pelo modo menos gravoso para o executado.",
     "gabarito": "C",
     "comentario": {
      "resumo": "Art. 805. Mas o executado que alegar maior gravosidade deve **indicar outros meios mais eficazes e menos onerosos**, sob pena de manutenção dos atos (par. ún.).",
      "lei": [
       {
        "lei": "L13105",
        "art": "805",
        "par": "",
        "inc": "",
        "rotulo": "CPC, art. 805",
        "texto": "Quando por vários meios o exequente puder promover a execução, o juiz mandará que se faça pelo modo menos gravoso para o executado."
       }
      ],
      "palavras_chave": [
       "menor onerosidade"
      ],
      "aprofundamento": "O princípio da **menor onerosidade** busca evitar que a execução cause ao devedor sacrifício maior que o necessário. Se há vários meios igualmente eficazes, deve-se escolher o menos gravoso.\n\nMas esse princípio não pode ser usado como escudo para frustrar a execução. A execução existe para **satisfazer o credor**, e a efetividade é o seu objetivo principal. Por isso o executado que alegar que a medida é mais gravosa tem o ônus de **indicar outros meios mais eficazes e menos onerosos**, sob pena de manutenção dos atos já determinados.\n\nO equilíbrio está entre efetividade e menor sacrifício. A banca costuma dizer que basta ao executado alegar a gravosidade para que o juiz altere a medida.",
      "memorize": "Menor onerosidade: o executado que alega deve indicar meio mais eficaz e menos oneroso."
     }
    },
    {
     "id": "CPC-9-R2-01",
     "ponto": "DBA26-CPC-9",
     "tema": "Ampliação do colegiado — exclusões",
     "assertiva": "A técnica de ampliação do colegiado do art. 942 aplica-se ao julgamento não unânime do IRDR e da remessa necessária.",
     "gabarito": "E",
     "comentario": {
      "resumo": "Art. 942, § 4º: **não** se aplica ao IAC, ao IRDR, à remessa necessária nem ao julgamento do plenário ou da corte especial.",
      "excecoes": [
       "IAC e IRDR (§ 4º, I)",
       "Remessa necessária (§ 4º, II)",
       "Não unânime do plenário ou corte especial (§ 4º, III)"
      ],
      "lei": [
       {
        "lei": "L13105",
        "art": "942",
        "par": "",
        "inc": "",
        "rotulo": "CPC, art. 942, § 4º",
        "texto": "Não se aplica o disposto neste artigo ao julgamento:\nI - do incidente de assunção de competência e ao de resolução de demandas repetitivas;\nII - da remessa necessária;\nIII - não unânime proferido, nos tribunais, pelo plenário ou pela corte especial."
       }
      ],
      "palavras_chave": [
       "art. 942",
       "ampliação do colegiado"
      ],
      "correcao": {
       "erro": "Aplica a técnica de ampliação do colegiado ao julgamento não unânime do IRDR e da remessa necessária.",
       "certo": "A técnica do art. 942 não se aplica ao julgamento do IAC, do IRDR, da remessa necessária nem ao julgamento não unânime do plenário ou da corte especial."
      },
      "aprofundamento": "A **técnica de ampliação do colegiado** substituiu os embargos infringentes: quando o julgamento não é unânime, novos julgadores são convocados para garantir a possibilidade de inversão do resultado. Mas há situações em que essa técnica não faz sentido.\n\nNo **IRDR** e no **IAC**, os órgãos julgadores já são ampliados, porque esses incidentes fixam teses vinculantes. Na **remessa necessária**, não há recurso da parte, e a técnica de ampliação perderia sua razão. E nos julgamentos do **plenário ou corte especial**, o órgão já é o mais amplo do tribunal.\n\nA assertiva inclui justamente duas das exclusões expressas. A banca costuma testar se o candidato conhece as hipóteses em que a técnica não se aplica.",
      "memorize": "Ampliação do colegiado não vale para IAC, IRDR, remessa necessária, plenário e corte especial."
     }
    },
    {
     "id": "CPC-9-R2-02",
     "ponto": "DBA26-CPC-9",
     "tema": "Ratificação do recurso",
     "assertiva": "Não é necessário ratificar o recurso especial interposto na pendência do julgamento dos embargos de declaração, quando inalterado o resultado anterior.",
     "gabarito": "C",
     "comentario": {
      "resumo": "**Súmula 579/STJ** e art. 1.024, § 5º.",
      "lei": [
       {
        "lei": "L13105",
        "art": "1024",
        "par": "",
        "inc": "",
        "rotulo": "CPC, art. 1.024, § 5º",
        "texto": "Se os embargos de declaração forem rejeitados ou não alterarem a conclusão do julgamento anterior, o recurso interposto pela outra parte antes da publicação do julgamento dos embargos de declaração será processado e julgado independentemente de ratificação."
       }
      ],
      "juris": [
       {
        "tribunal": "STJ",
        "fonte": "Súmula 579/STJ",
        "data": "01/07/2016",
        "texto": "Não é necessário ratificar o REsp interposto na pendência dos embargos de declaração quando inalterado o resultado anterior."
       }
      ],
      "palavras_chave": [
       "ratificação",
       "embargos de declaração"
      ],
      "aprofundamento": "Quando uma parte interpõe recurso e a outra opõe embargos de declaração contra a mesma decisão, surge a dúvida: o recurso interposto antes do julgamento dos embargos precisa ser ratificado depois? Antes, a jurisprudência exigia essa ratificação, sob pena de não conhecimento.\n\nO CPC atual e a Súmula 579/STJ afastaram essa exigência quando os embargos forem rejeitados ou **não alterarem a conclusão** do julgamento. Se nada mudou, não há razão para exigir que a parte reitere o que já disse.\n\nSe os embargos alterarem a decisão, a parte que já recorreu pode complementar ou alterar suas razões, nos limites da modificação. A banca costuma exigir ratificação em qualquer caso.",
      "memorize": "Recurso interposto antes do julgamento dos embargos não precisa ser ratificado se nada mudar (Súmula 579/STJ)."
     }
    },
    {
     "id": "CPC-9-R2-03",
     "ponto": "DBA26-CPC-9",
     "tema": "Prequestionamento ficto",
     "assertiva": "Consideram-se incluídos no acórdão os elementos que o embargante suscitou para fins de prequestionamento, ainda que os embargos de declaração sejam inadmitidos ou rejeitados, caso o tribunal superior considere existentes erro, omissão, contradição ou obscuridade.",
     "gabarito": "C",
     "comentario": {
      "resumo": "Art. 1.025: **prequestionamento ficto**, que superou na prática a lógica da Súmula 211/STJ.",
      "lei": [
       {
        "lei": "L13105",
        "art": "1025",
        "par": "",
        "inc": "",
        "rotulo": "CPC, art. 1.025",
        "texto": "Consideram-se incluídos no acórdão os elementos que o embargante suscitou, para fins de pré-questionamento, ainda que os embargos de declaração sejam inadmitidos ou rejeitados, caso o tribunal superior considere existentes erro, omissão, contradição ou obscuridade."
       }
      ],
      "juris": [
       {
        "tribunal": "STJ",
        "fonte": "Súmula 211/STJ",
        "data": "01/07/1998",
        "texto": "Inadmissível REsp quanto à questão que, a despeito dos embargos declaratórios, não foi apreciada pelo tribunal a quo."
       }
      ],
      "palavras_chave": [
       "prequestionamento ficto"
      ],
      "aprofundamento": "O **prequestionamento** é a exigência de que a questão federal ou constitucional tenha sido debatida no acórdão recorrido, para que possa ser levada ao STJ ou ao STF. Quando o tribunal de origem se omite, a parte opõe embargos de declaração.\n\nNo regime anterior, se o tribunal rejeitasse os embargos sem enfrentar a questão, o recurso especial não era admitido (lógica da Súmula 211/STJ). O CPC criou o **prequestionamento ficto**: consideram-se incluídos no acórdão os elementos suscitados nos embargos, desde que o tribunal superior reconheça a existência de erro, omissão, contradição ou obscuridade.\n\nAssim, a parte não é prejudicada pela omissão do tribunal de origem. A banca costuma dizer que o prequestionamento só existe se o tribunal efetivamente enfrentar a questão.",
      "memorize": "Prequestionamento ficto: embargos suscitados valem, se o tribunal superior reconhecer o vício (art. 1.025)."
     }
    },
    {
     "id": "CPC-9-R2-04",
     "ponto": "DBA26-CPC-9",
     "tema": "Embargos protelatórios",
     "assertiva": "Quando manifestamente protelatórios os embargos de declaração, o embargante será condenado, já na primeira oposição, a multa de até 10% sobre o valor atualizado da causa.",
     "gabarito": "E",
     "comentario": {
      "resumo": "Art. 1.026, § 2º: na primeira vez, multa **não excedente a 2%**; na **reiteração**, até **10%** (§ 3º).",
      "lei": [
       {
        "lei": "L13105",
        "art": "1026",
        "par": "",
        "inc": "",
        "rotulo": "CPC, art. 1.026, § 2º",
        "texto": "Quando manifestamente protelatórios os embargos de declaração, o juiz ou o tribunal, em decisão fundamentada, condenará o embargante a pagar ao embargado multa não excedente a dois por cento sobre o valor atualizado da causa."
       }
      ],
      "palavras_chave": [
       "embargos protelatórios",
       "2%",
       "10%"
      ],
      "correcao": {
       "erro": "Aplica multa de até 10% já na primeira oposição de embargos protelatórios.",
       "certo": "Na primeira oposição de embargos manifestamente protelatórios, a multa não excede 2% do valor atualizado da causa; na reiteração, pode chegar a 10%."
      },
      "aprofundamento": "Os embargos de declaração **interrompem** o prazo recursal, e isso cria uma tentação: usá-los apenas para ganhar tempo. A lei combate esse abuso com multas progressivas.\n\nNa **primeira** oposição de embargos manifestamente protelatórios, a multa não excede 2% do valor atualizado da causa. Na **reiteração**, ela sobe para até 10%, e a interposição de qualquer outro recurso fica condicionada ao depósito prévio do valor, exceto para a Fazenda Pública e o beneficiário da gratuidade, que pagam ao final. E não se admitem novos embargos se os anteriores tiverem sido considerados protelatórios.\n\nA progressão é proporcional à gravidade do abuso. A banca aplica a multa maior já na primeira oposição.",
      "memorize": "Embargos protelatórios: 1ª vez até 2%; reiteração até 10%."
     }
    },
    {
     "id": "CPC-9-R2-05",
     "ponto": "DBA26-CPC-9",
     "tema": "RE contra liminar",
     "assertiva": "Cabe recurso extraordinário contra acórdão que defere medida liminar, desde que demonstrada a repercussão geral.",
     "gabarito": "E",
     "comentario": {
      "resumo": "Súmula 735/STF: **não cabe** RE contra acórdão que defere liminar (decisão provisória, sem juízo definitivo). Na mesma linha, a Súmula 7/STJ veda o reexame de prova no REsp.",
      "juris": [
       {
        "tribunal": "STF",
        "fonte": "Súmula 735/STF",
        "data": "26/11/2003",
        "texto": "Não cabe recurso extraordinário contra acórdão que defere medida liminar."
       },
       {
        "tribunal": "STJ",
        "fonte": "Súmula 7/STJ",
        "data": "28/06/1990",
        "texto": "A pretensão de simples reexame de prova não enseja recurso especial."
       }
      ],
      "palavras_chave": [
       "recurso extraordinário",
       "liminar"
      ],
      "correcao": {
       "erro": "Admite recurso extraordinário contra acórdão que defere medida liminar, desde que demonstrada a repercussão geral.",
       "certo": "Não cabe recurso extraordinário contra acórdão que defere medida liminar (Súmula 735/STF), por se tratar de decisão provisória."
      },
      "aprofundamento": "O recurso extraordinário é um recurso de **estrito direito**, voltado à proteção da Constituição. Ele pressupõe uma decisão definitiva sobre a questão constitucional. A liminar, por sua natureza, é **provisória**: baseia-se em cognição sumária e pode ser revista a qualquer momento.\n\nPor isso a Súmula 735/STF afasta o RE contra acórdão que defere liminar. Não há juízo definitivo a ser revisto; o tribunal apenas avaliou a probabilidade do direito e o perigo. Além disso, a análise dos requisitos da liminar envolve, normalmente, o exame de fatos e provas.\n\nA mesma lógica de proteção do papel dos tribunais superiores aparece na Súmula 7/STJ, que impede o reexame de provas no REsp. A banca tenta salvar o RE com a demonstração de repercussão geral, mas o óbice é anterior.",
      "memorize": "RE contra liminar: não cabe (Súmula 735/STF)."
     }
    },
    {
     "id": "CPC-9-R2-06",
     "ponto": "DBA26-CPC-9",
     "tema": "Repercussão geral presumida",
     "assertiva": "Haverá repercussão geral sempre que o recurso impugnar acórdão que contrarie súmula ou jurisprudência dominante do Supremo Tribunal Federal.",
     "gabarito": "C",
     "comentario": {
      "resumo": "**Art. 1.035, § 3º, I**.",
      "lei": [
       {
        "lei": "L13105",
        "art": "1035",
        "par": "",
        "inc": "",
        "rotulo": "CPC, art. 1.035, § 3º, I",
        "texto": "I - contrarie súmula ou jurisprudência dominante do Supremo Tribunal Federal;"
       }
      ],
      "palavras_chave": [
       "repercussão geral",
       "presunção"
      ],
      "aprofundamento": "A **repercussão geral** é requisito de admissibilidade do RE: o recorrente deve demonstrar que a questão constitucional tem relevância econômica, política, social ou jurídica que ultrapassa os interesses das partes. É um filtro para que o STF julgue apenas as causas mais importantes.\n\nMas há casos em que a lei **presume** a repercussão geral. Um deles é quando o acórdão recorrido contraria súmula ou jurisprudência dominante do STF. A lógica é que a desobediência ao entendimento do Supremo, por si só, já justifica sua intervenção, para garantir a autoridade de suas decisões e a uniformidade do direito.\n\nA banca costuma exigir a demonstração de repercussão mesmo nessa hipótese, ou ampliar a presunção para contrariedade a jurisprudência de outros tribunais.",
      "memorize": "Acórdão contra súmula ou jurisprudência dominante do STF: repercussão geral presumida."
     }
    },
    {
     "id": "CPC-9-R2-07",
     "ponto": "DBA26-CPC-9",
     "tema": "Rescisória e interpretação controvertida",
     "assertiva": "Não cabe ação rescisória por ofensa a literal disposição de lei quando a decisão rescindenda se tiver baseado em texto legal de interpretação controvertida nos tribunais.",
     "gabarito": "C",
     "comentario": {
      "resumo": "**Súmula 343**/STF.",
      "juris": [
       {
        "tribunal": "STF",
        "fonte": "Súmula 343/STF",
        "data": "13/12/1963",
        "texto": "Não cabe ação rescisória por ofensa a literal disposição de lei quando a decisão rescindenda se baseou em texto de interpretação controvertida nos tribunais."
       }
      ],
      "palavras_chave": [
       "rescisória",
       "Súmula 343"
      ],
      "aprofundamento": "A rescisória por violação manifesta de norma jurídica busca corrigir decisões que contrariam a lei de forma evidente. Mas, se o texto legal tinha **interpretação controvertida** nos tribunais à época da decisão, não se pode dizer que a decisão violou a lei; ela apenas adotou uma das interpretações possíveis.\n\nA Súmula 343/STF consagra essa ideia. Permitir a rescisória nesses casos seria usar a ação para uniformizar jurisprudência retroativamente, desfazendo decisões que eram razoáveis quando proferidas, em prejuízo da segurança jurídica.\n\nA súmula é aplicada principalmente em matéria infraconstitucional. A banca costuma afirmar que a superveniência de jurisprudência pacífica autoriza a rescisória contra decisões anteriores, o que contraria a lógica da súmula.",
      "memorize": "Interpretação controvertida nos tribunais: não cabe rescisória por violação de lei (Súmula 343/STF)."
     }
    },
    {
     "id": "CPC-9-R2-08",
     "ponto": "DBA26-CPC-9",
     "tema": "Rescisória por prova nova",
     "assertiva": "Fundada a rescisória em prova nova, o termo inicial é a data de sua descoberta, observado o prazo máximo de 10 anos contado do trânsito em julgado.",
     "gabarito": "E",
     "comentario": {
      "resumo": "Art. 975, § 2º: prazo máximo de **5 anos**.",
      "lei": [
       {
        "lei": "L13105",
        "art": "975",
        "par": "",
        "inc": "",
        "rotulo": "CPC, art. 975, § 2º",
        "texto": "Se fundada a ação no inciso VII do art. 966, o termo inicial do prazo será a data de descoberta da prova nova, observado o prazo máximo de 5 (cinco) anos, contado do trânsito em julgado da última decisão proferida no processo."
       }
      ],
      "palavras_chave": [
       "prova nova",
       "5 anos"
      ],
      "correcao": {
       "erro": "Fixa em 10 anos o prazo máximo da rescisória fundada em prova nova.",
       "certo": "Fundada a rescisória em prova nova, o termo inicial é a data da descoberta, observado o prazo máximo de 5 anos contado do trânsito em julgado da última decisão do processo."
      },
      "aprofundamento": "A rescisória fundada em **prova nova** tem regra especial de prazo. A parte pode não ter tido acesso à prova durante o processo, e só descobri-la depois. Por isso o prazo começa a correr da **descoberta da prova**, e não do trânsito em julgado.\n\nMas essa regra precisa de um limite, sob pena de a coisa julgada ficar eternamente ameaçada. A lei fixa um **prazo máximo** de 5 anos, contado do trânsito em julgado da última decisão do processo. Mesmo que a prova seja descoberta depois, a rescisória não cabe mais.\n\nO equilíbrio é entre justiça (permitir a correção com base em prova desconhecida) e segurança (não deixar a decisão indefinidamente instável). A banca dobra o prazo máximo.",
      "memorize": "Rescisória por prova nova: conta da descoberta, limite de 5 anos do trânsito."
     }
    },
    {
     "id": "CPC-9-R2-09",
     "ponto": "DBA26-CPC-9",
     "tema": "Depósito da rescisória",
     "assertiva": "O autor da rescisória deve depositar 5% sobre o valor da causa, exigência que não se aplica à Fazenda Pública, ao Ministério Público, à Defensoria Pública e aos beneficiários da gratuidade.",
     "gabarito": "C",
     "comentario": {
      "resumo": "**Art. 968, II** e § 1º; limite de 1.000 salários mínimos (§ 2º).",
      "lei": [
       {
        "lei": "L13105",
        "art": "968",
        "par": "",
        "inc": "",
        "rotulo": "CPC, art. 968, II",
        "texto": "II - depositar a importância de cinco por cento sobre o valor da causa, que se converterá em multa caso a ação seja, por unanimidade de votos, declarada inadmissível ou improcedente."
       },
       {
        "lei": "L13105",
        "art": "968",
        "par": "",
        "inc": "",
        "rotulo": "CPC, art. 968, § 1º",
        "texto": "Não se aplica o disposto no inciso II à União, aos Estados, ao Distrito Federal, aos Municípios, às suas respectivas autarquias e fundações de direito público, ao Ministério Público, à Defensoria Pública e aos que tenham obtido o benefício de gratuidade da justiça."
       }
      ],
      "palavras_chave": [
       "rescisória",
       "depósito de 5%"
      ],
      "aprofundamento": "O **depósito** na ação rescisória desestimula o ajuizamento temerário. Quem quer desfazer a coisa julgada deve demonstrar seriedade, e o depósito se converte em **multa** em favor do réu se a ação for declarada inadmissível ou improcedente por unanimidade.\n\nO valor é de 5% sobre o valor da causa, com limite de 1.000 salários mínimos. A exigência não se aplica aos entes públicos e suas autarquias e fundações de direito público, ao MP, à Defensoria e aos beneficiários da gratuidade, porque a exigência poderia impedir o acesso à justiça ou porque esses entes têm presunção de seriedade institucional.\n\nA banca costuma alterar o percentual ou retirar algum dos isentos.",
      "memorize": "Rescisória: depósito de 5% (teto de 1.000 SM); isentos Fazenda, MP, Defensoria e gratuidade."
     }
    },
    {
     "id": "CPC-9-R2-10",
     "ponto": "DBA26-CPC-9",
     "tema": "Feriado local",
     "assertiva": "Se o recorrente não comprovar o feriado local no ato de interposição, o recurso é intempestivo, sem possibilidade de correção.",
     "gabarito": "E",
     "comentario": {
      "resumo": "Art. 1.003, § 6º (Lei 14.939/2024): o tribunal **determinará a correção do vício formal**, ou o desconsiderará se a informação já constar do processo eletrônico.",
      "lei": [
       {
        "lei": "L13105",
        "art": "1003",
        "par": "",
        "inc": "",
        "rotulo": "CPC, art. 1.003, § 6º",
        "texto": "O recorrente comprovará a ocorrência de feriado local no ato de interposição do recurso, e, se não o fizer, o tribunal determinará a correção do vício formal, ou poderá desconsiderá-lo caso a informação já conste do processo eletrônico."
       }
      ],
      "palavras_chave": [
       "feriado local",
       "vício sanável",
       "Lei 14.939/2024"
      ],
      "correcao": {
       "erro": "Declara intempestivo, sem possibilidade de correção, o recurso em que o feriado local não foi comprovado na interposição.",
       "certo": "Se o recorrente não comprovar o feriado local na interposição, o tribunal determinará a correção do vício formal, ou poderá desconsiderá-lo se a informação já constar do processo eletrônico."
      },
      "aprofundamento": "O feriado local, como um feriado municipal, não é de conhecimento geral do tribunal superior, e por isso o recorrente deve comprovar sua ocorrência para demonstrar a tempestividade do recurso. Antes, a falta dessa comprovação levava à inadmissão do recurso, sem chance de correção.\n\nA Lei 14.939/2024 mudou esse cenário. Se o recorrente não comprovar o feriado no ato de interposição, o tribunal deve **determinar a correção do vício formal**, ou pode desconsiderá-lo se a informação já constar do processo eletrônico.\n\nÉ uma aplicação da **primazia do julgamento de mérito**: um vício formal sanável não deve impedir o exame do recurso. A assertiva reproduz o entendimento anterior à lei.",
      "memorize": "Feriado local não comprovado: vício sanável (Lei 14.939/2024)."
     }
    },
    {
     "id": "CPC-10-R2-01",
     "ponto": "DBA26-CPC-10",
     "tema": "ACP — MP fiscal",
     "assertiva": "Na ação civil pública, o Ministério Público, se não intervier no processo como parte, atuará obrigatoriamente como fiscal da lei.",
     "gabarito": "C",
     "comentario": {
      "resumo": "**Art. 5º, § 1º**.",
      "lei": [
       {
        "lei": "L7347",
        "art": "5",
        "par": "",
        "inc": "",
        "rotulo": "Lei 7.347/1985, art. 5º, § 1º",
        "texto": "O Ministério Público, se não intervier no processo como parte, atuará obrigatoriamente como fiscal da lei."
       }
      ],
      "palavras_chave": [
       "MP",
       "fiscal da lei"
      ],
      "aprofundamento": "Na ação civil pública, o MP tem papel central na defesa dos interesses difusos e coletivos. Quando ele não é o autor, a lei exige que atue **obrigatoriamente** como fiscal da ordem jurídica.\n\nA razão é que a ACP envolve interesses que transcendem as partes. Mesmo quando proposta por uma associação ou por um ente público, a atuação do MP garante que os interesses da coletividade sejam adequadamente defendidos e que a ação não seja usada de forma inadequada.\n\nSe a associação autora desistir ou abandonar a ação, o MP ou outro legitimado pode assumir a titularidade ativa. A banca costuma dizer que a intervenção do MP é facultativa quando ele não é parte.",
      "memorize": "ACP: MP que não é parte atua obrigatoriamente como fiscal."
     }
    },
    {
     "id": "CPC-10-R2-02",
     "ponto": "DBA26-CPC-10",
     "tema": "Compromisso de ajustamento de conduta",
     "assertiva": "O compromisso de ajustamento de conduta tomado pelos órgãos públicos legitimados tem eficácia de título executivo judicial.",
     "gabarito": "E",
     "comentario": {
      "resumo": "Art. 5º, § 6º: título executivo **extrajudicial**.",
      "lei": [
       {
        "lei": "L7347",
        "art": "5",
        "par": "",
        "inc": "",
        "rotulo": "Lei 7.347/1985, art. 5º, § 6º",
        "texto": "Os órgãos públicos legitimados poderão tomar dos interessados compromisso de ajustamento de sua conduta às exigências legais, mediante cominações, que terá eficácia de título executivo extrajudicial."
       }
      ],
      "palavras_chave": [
       "TAC",
       "título extrajudicial"
      ],
      "correcao": {
       "erro": "Atribui ao compromisso de ajustamento de conduta eficácia de título executivo judicial.",
       "certo": "O compromisso de ajustamento de conduta tomado pelos órgãos públicos legitimados tem eficácia de título executivo extrajudicial."
      },
      "aprofundamento": "O **compromisso de ajustamento de conduta** (TAC) é um acordo extrajudicial em que o causador de um dano coletivo se compromete a adequar sua conduta às exigências legais, mediante cominações. Ele é tomado pelos órgãos públicos legitimados, como o MP.\n\nComo é celebrado **fora do processo judicial**, o TAC tem eficácia de **título executivo extrajudicial**. Se descumprido, pode ser executado diretamente, sem necessidade de ação de conhecimento.\n\nSe o TAC for homologado em juízo, aí sim passa a ter natureza de título judicial. A banca troca a natureza do título. Lembre: o TAC tomado pelo órgão público, sem homologação, é extrajudicial.",
      "memorize": "TAC = título executivo extrajudicial."
     }
    },
    {
     "id": "CPC-10-R2-03",
     "ponto": "DBA26-CPC-10",
     "tema": "Inquérito civil",
     "assertiva": "O inquérito civil pode ser instaurado por qualquer dos legitimados à ação civil pública, inclusive pelas associações.",
     "gabarito": "E",
     "comentario": {
      "resumo": "Art. 8º, § 1º: o inquérito civil é **exclusivo do MP**, que o preside.",
      "lei": [
       {
        "lei": "L7347",
        "art": "8",
        "par": "",
        "inc": "",
        "rotulo": "Lei 7.347/1985, art. 8º, § 1º",
        "texto": "O Ministério Público poderá instaurar, sob sua presidência, inquérito civil, ou requisitar, de qualquer organismo público ou particular, certidões, informações, exames ou perícias, no prazo que assinalar, o qual não poderá ser inferior a 10 (dez) dias úteis."
       }
      ],
      "palavras_chave": [
       "inquérito civil",
       "exclusividade do MP"
      ],
      "correcao": {
       "erro": "Admite a instauração do inquérito civil por qualquer legitimado à ação civil pública, inclusive associações.",
       "certo": "O inquérito civil é instaurado e presidido exclusivamente pelo Ministério Público."
      },
      "aprofundamento": "O **inquérito civil** é um procedimento investigatório para reunir elementos que fundamentem uma eventual ação civil pública. Ele permite ao MP requisitar documentos, informações, exames e perícias, com poderes próprios.\n\nPor envolver poderes de requisição e investigação, o inquérito civil é **exclusivo do Ministério Público**, que o instaura e preside. Os demais legitimados à ACP, como associações e entes públicos, podem colher provas por outros meios, mas não instauram inquérito civil.\n\nO inquérito não é pressuposto para a ACP: a ação pode ser proposta sem ele. A banca costuma estender o inquérito civil a outros legitimados ou torná-lo obrigatório.",
      "memorize": "Inquérito civil: exclusivo do MP; não é pressuposto da ACP."
     }
    },
    {
     "id": "CPC-10-R2-04",
     "ponto": "DBA26-CPC-10",
     "tema": "Ônus da associação autora",
     "assertiva": "Vencida na ação civil pública, a associação autora será sempre condenada em honorários de advogado, custas e despesas processuais.",
     "gabarito": "E",
     "comentario": {
      "resumo": "Art. 18: **não há** condenação da associação autora, **salvo comprovada má-fé**.",
      "lei": [
       {
        "lei": "L7347",
        "art": "18",
        "par": "",
        "inc": "",
        "rotulo": "Lei 7.347/1985, art. 18",
        "texto": "Nas ações de que trata esta lei, não haverá adiantamento de custas, emolumentos, honorários periciais e quaisquer outras despesas, nem condenação da associação autora, salvo comprovada má-fé, em honorários de advogado, custas e despesas processuais."
       }
      ],
      "palavras_chave": [
       "associação",
       "má-fé",
       "custas"
      ],
      "correcao": {
       "erro": "Afirma que a associação autora vencida na ACP será sempre condenada em honorários, custas e despesas.",
       "certo": "Na ACP não há condenação da associação autora em honorários, custas e despesas processuais, salvo comprovada má-fé."
      },
      "aprofundamento": "A isenção de custas e honorários para a associação autora na ACP é um estímulo à **tutela coletiva**. Associações normalmente têm poucos recursos, e o risco de pagar honorários e custas desestimularia a propositura de ações em defesa de interesses difusos e coletivos.\n\nPor isso a lei afasta a condenação da associação autora em honorários, custas e despesas, **salvo comprovada má-fé**. Também não há adiantamento de custas, emolumentos, honorários periciais e outras despesas.\n\nA ressalva da má-fé impede que a isenção seja usada para ações abusivas ou temerárias. Se houver má-fé, a associação e seus diretores respondem solidariamente. A assertiva elimina a isenção com a palavra \"sempre\".",
      "memorize": "ACP: associação autora não paga sucumbência, salvo má-fé."
     }
    },
    {
     "id": "CPC-10-R2-05",
     "ponto": "DBA26-CPC-10",
     "tema": "Ação popular — ente público réu",
     "assertiva": "A pessoa jurídica de direito público cujo ato seja impugnado na ação popular poderá abster-se de contestar o pedido ou atuar ao lado do autor, se isso se afigurar útil ao interesse público.",
     "gabarito": "C",
     "comentario": {
      "resumo": "Art. 6º, § 3º: **intervenção móvel** (migração de polo).",
      "lei": [
       {
        "lei": "L4717",
        "art": "6",
        "par": "",
        "inc": "",
        "rotulo": "Lei 4.717/1965, art. 6º, § 3º",
        "texto": "cujo ato seja objeto de impugnação, poderá abster-se de contestar o pedido, ou poderá atuar ao lado do autor, desde que isso se afigure útil ao interesse público, a juízo do respectivo representante legal ou dirigente."
       }
      ],
      "palavras_chave": [
       "intervenção móvel",
       "ação popular"
      ],
      "aprofundamento": "Na ação popular, o ente público cujo ato é impugnado figura inicialmente como réu. Mas pode acontecer que o próprio ente reconheça que o ato é lesivo, por exemplo quando a nova administração discorda do ato da anterior.\n\nPor isso a lei permite a **intervenção móvel** ou migração de polo: o ente pode abster-se de contestar ou até **atuar ao lado do autor**, se isso for útil ao interesse público, a juízo de seu representante legal. A lógica é que o ente defende o interesse público, não necessariamente o ato praticado.\n\nO mesmo mecanismo é aplicado, por analogia, na ação de improbidade. A banca costuma dizer que o ente público réu é obrigado a defender o ato impugnado.",
      "memorize": "Ação popular: ente réu pode não contestar ou migrar para o lado do autor (intervenção móvel)."
     }
    },
    {
     "id": "CPC-10-R2-06",
     "ponto": "DBA26-CPC-10",
     "tema": "Vedações de liminar em MS",
     "assertiva": "Permanece válida a vedação legal de liminar em mandado de segurança que tenha por objeto a compensação de créditos tributários ou a entrega de mercadorias provenientes do exterior.",
     "gabarito": "E",
     "comentario": {
      "resumo": "O STF, na **ADI 4.296**, declarou **inconstitucional** o art. 7º, § 2º, da Lei 12.016/2009 (e o art. 22, § 2º). Ficou válida a faculdade de exigir **caução** (art. 7º, III).",
      "lei": [
       {
        "lei": "L12016",
        "art": "7",
        "par": "",
        "inc": "",
        "rotulo": "Lei 12.016/2009, art. 7º, § 2º (declarado inconstitucional)",
        "texto": "Não será concedida medida liminar que tenha por objeto a compensação de créditos tributários"
       }
      ],
      "juris": [
       {
        "tribunal": "STF",
        "fonte": "ADI 4.296/DF (Informativo STF 1.021)",
        "data": "09/06/2021",
        "texto": "São inconstitucionais o art. 7º, § 2º (vedações de liminar em MS) e o art. 22, § 2º (oitiva prévia do ente público para liminar em MS coletivo) da Lei 12.016/2009; mantidos a caução do art. 7º, III, e o prazo de 120 dias do art. 23."
       }
      ],
      "palavras_chave": [
       "liminar",
       "ADI 4.296"
      ],
      "correcao": {
       "erro": "Afirma que permanece válida a vedação legal de liminar em MS para compensação de créditos tributários ou entrega de mercadorias do exterior.",
       "certo": "O STF, na ADI 4.296, declarou inconstitucional o art. 7º, § 2º, da Lei 12.016/2009, que vedava essas liminares; ficou válida a faculdade de exigir caução."
      },
      "aprofundamento": "A Lei do MS previa vedações à concessão de liminar em certas matérias, como compensação de créditos tributários e entrega de mercadorias do exterior. A ideia era proteger o erário contra liminares de difícil reversão.\n\nO STF, na **ADI 4.296**, declarou essas vedações **inconstitucionais**. O fundamento é que o MS é garantia constitucional, e a lei não pode impedir o juiz de conceder a tutela necessária para evitar o perecimento do direito. Também caiu a exigência de oitiva prévia do ente público para liminar em MS coletivo.\n\nForam mantidas a faculdade de exigir **caução** e o prazo de 120 dias. A pegadinha é que o texto declarado inconstitucional continua publicado, e a banca o apresenta como válido.",
      "memorize": "Vedações de liminar em MS: inconstitucionais (ADI 4.296); caução continua possível."
     }
    },
    {
     "id": "CPC-10-R2-07",
     "ponto": "DBA26-CPC-10",
     "tema": "Teoria da encampação",
     "assertiva": "A teoria da encampação aplica-se ao mandado de segurança quando presentes, cumulativamente, vínculo hierárquico entre a autoridade que prestou informações e a que ordenou o ato, manifestação a respeito do mérito nas informações e ausência de modificação de competência constitucional.",
     "gabarito": "C",
     "comentario": {
      "resumo": "Súmula 628/STJ: requisitos **cumulativos**.",
      "juris": [
       {
        "tribunal": "STJ",
        "fonte": "Súmula 628/STJ",
        "data": "12/12/2018",
        "texto": "A teoria da encampação aplica-se ao MS quando presentes, cumulativamente: vínculo hierárquico, manifestação sobre o mérito nas informações e ausência de modificação de competência constitucional."
       }
      ],
      "palavras_chave": [
       "encampação",
       "autoridade coatora"
      ],
      "aprofundamento": "No mandado de segurança, o impetrante deve indicar a **autoridade coatora** correta. Mas a estrutura administrativa é complexa, e é comum o erro de indicar autoridade superior ou inferior à que efetivamente praticou o ato. A teoria da **encampação** evita que esse erro leve à extinção do processo.\n\nSe a autoridade indicada, ao prestar informações, defende o mérito do ato, ela o \"encampa\", assumindo-o como seu. A Súmula 628/STJ exige três requisitos **cumulativos**: vínculo hierárquico entre as autoridades; manifestação sobre o mérito nas informações; e ausência de modificação de competência constitucional.\n\nO último requisito impede que a encampação desloque a causa para outro tribunal, por exemplo do TJ para o STJ. A banca costuma tornar os requisitos alternativos.",
      "memorize": "Encampação: vínculo hierárquico + defesa do mérito + sem mudança de competência constitucional (Súmula 628/STJ)."
     }
    },
    {
     "id": "CPC-10-R2-08",
     "ponto": "DBA26-CPC-10",
     "tema": "MS coletivo e ação individual",
     "assertiva": "O mandado de segurança coletivo induz litispendência para as ações individuais.",
     "gabarito": "E",
     "comentario": {
      "resumo": "Art. 22, § 1º: **não induz litispendência**; mas o impetrante individual só se beneficia se desistir do seu MS em **30 dias** da ciência do coletivo.",
      "lei": [
       {
        "lei": "L12016",
        "art": "22",
        "par": "",
        "inc": "",
        "rotulo": "Lei 12.016/2009, art. 22, § 1º",
        "texto": "O mandado de segurança coletivo não induz litispendência para as ações individuais, mas os efeitos da coisa julgada não beneficiarão o impetrante a título individual se não requerer a desistência de seu mandado de segurança no prazo de 30 (trinta) dias a contar da ciência comprovada da impetração da segurança coletiva."
       }
      ],
      "palavras_chave": [
       "MS coletivo",
       "litispendência",
       "30 dias"
      ],
      "correcao": {
       "erro": "Afirma que o mandado de segurança coletivo induz litispendência para as ações individuais.",
       "certo": "O MS coletivo não induz litispendência para as ações individuais, mas o impetrante individual só se beneficia da coisa julgada coletiva se desistir de seu MS em 30 dias da ciência comprovada da impetração coletiva."
      },
      "aprofundamento": "O **mandado de segurança coletivo** e o individual podem coexistir, porque os titulares e os objetos são diferentes: o coletivo é proposto por entidade em defesa da categoria; o individual, pelo próprio interessado. Por isso o coletivo **não induz litispendência** para as ações individuais.\n\nMas a lei cria um mecanismo para evitar decisões contraditórias e duplicidade de benefício. O impetrante individual só se beneficia da coisa julgada do coletivo se **desistir** de seu mandado de segurança no prazo de 30 dias, contados da ciência comprovada da impetração coletiva.\n\nA escolha é do impetrante: ou mantém seu MS individual, ou desiste e aproveita o coletivo. A assertiva afirma a litispendência, que a lei expressamente afasta.",
      "memorize": "MS coletivo não gera litispendência; para aproveitar, o individual desiste em 30 dias."
     }
    },
    {
     "id": "CPC-10-R2-09",
     "ponto": "DBA26-CPC-10",
     "tema": "Reexame necessário no MS",
     "assertiva": "Concedida a segurança, a sentença estará sujeita obrigatoriamente ao duplo grau de jurisdição.",
     "gabarito": "C",
     "comentario": {
      "resumo": "**Art. 14, § 1º**. A autoridade coatora também pode recorrer (§ 2º).",
      "lei": [
       {
        "lei": "L12016",
        "art": "14",
        "par": "",
        "inc": "",
        "rotulo": "Lei 12.016/2009, art. 14, § 1º",
        "texto": "Concedida a segurança, a sentença estará sujeita obrigatoriamente ao duplo grau de jurisdição."
       }
      ],
      "palavras_chave": [
       "duplo grau",
       "remessa necessária"
      ],
      "aprofundamento": "A sentença que **concede** a segurança está sujeita ao **reexame necessário**. A razão é a mesma que justifica a remessa necessária no CPC: proteger o interesse público contra decisões desfavoráveis ao poder público, garantindo um segundo exame pelo tribunal.\n\nA Lei do MS traz essa regra de forma expressa e própria. A sentença que denega a segurança, por outro lado, não se sujeita, porque não prejudica o poder público.\n\nA lei também confere à **autoridade coatora** o direito de recorrer, além da pessoa jurídica a que ela pertence. A banca costuma estender o reexame à sentença denegatória.",
      "memorize": "MS: sentença que concede a segurança vai obrigatoriamente ao duplo grau."
     }
    },
    {
     "id": "CPC-10-R2-10",
     "ponto": "DBA26-CPC-10",
     "tema": "Entidade de classe e parte da categoria",
     "assertiva": "A entidade de classe tem legitimação para o mandado de segurança ainda quando a pretensão veiculada interesse apenas a uma parte da respectiva categoria.",
     "gabarito": "C",
     "comentario": {
      "resumo": "**Súmula 630/STF**, refletida no art. 21 (\"da totalidade, ou de parte, dos seus membros\").",
      "lei": [
       {
        "lei": "L12016",
        "art": "21",
        "par": "",
        "inc": "",
        "rotulo": "Lei 12.016/2009, art. 21",
        "texto": "em defesa de direitos líquidos e certos da totalidade, ou de parte, dos seus membros ou associados"
       }
      ],
      "juris": [
       {
        "tribunal": "STF",
        "fonte": "Súmula 630/STF",
        "data": "24/09/2003",
        "texto": "A entidade de classe tem legitimação para o MS ainda quando a pretensão interesse apenas a uma parte da categoria."
       }
      ],
      "palavras_chave": [
       "MS coletivo",
       "parte da categoria"
      ],
      "aprofundamento": "A entidade de classe defende os interesses de seus membros, mas nem toda pretensão interessa a todos. Às vezes, uma questão afeta apenas uma parte da categoria, como os servidores de determinado cargo.\n\nA Súmula 630/STF reconhece que a entidade tem legitimação mesmo nesse caso. A razão é que a defesa de parte da categoria continua sendo defesa de interesses da categoria, e exigir que a pretensão interessasse a todos esvaziaria o mandado de segurança coletivo.\n\nA Lei do MS incorporou essa orientação ao falar em direitos \"da totalidade, ou de parte\" dos membros ou associados. O requisito essencial é a **pertinência temática** com as finalidades da entidade. A banca costuma exigir que a pretensão interesse a toda a categoria.",
      "memorize": "Entidade de classe pode impetrar MS coletivo para parte da categoria (Súmula 630/STF)."
     }
    },
    {
     "id": "CPC-11-R2-01",
     "ponto": "DBA26-CPC-11",
     "tema": "Renúncia ao excedente",
     "assertiva": "A opção pelo procedimento do Juizado Especial Cível importa renúncia ao crédito excedente ao limite legal, excetuada a hipótese de conciliação.",
     "gabarito": "C",
     "comentario": {
      "resumo": "**Art. 3º, § 3º**.",
      "lei": [
       {
        "lei": "L9099",
        "art": "3",
        "par": "",
        "inc": "",
        "rotulo": "Lei 9.099/1995, art. 3º, § 3º",
        "texto": "A opção pelo procedimento previsto nesta Lei importará em renúncia ao crédito excedente ao limite estabelecido neste artigo, excetuada a hipótese de conciliação."
       }
      ],
      "palavras_chave": [
       "renúncia",
       "excedente"
      ],
      "aprofundamento": "O Juizado Especial Cível é uma **opção** do autor nas causas de sua competência. Mas, se ele escolhe esse rito simplificado, aceita também o limite de valor que o caracteriza. Não pode usar o Juizado para obter condenação superior ao teto.\n\nPor isso a opção importa **renúncia ao crédito excedente** ao limite legal. É uma troca: o autor ganha celeridade, informalidade e gratuidade em primeiro grau, mas abre mão do que ultrapassar o teto.\n\nA exceção é a **conciliação**: se as partes fizerem acordo, podem estabelecer valor acima do limite. A lógica é estimular a autocomposição, que é o objetivo preferencial dos Juizados. A banca costuma eliminar essa exceção ou dizer que o excedente pode ser cobrado depois.",
      "memorize": "Escolheu o JEC: renuncia ao excedente do teto, salvo conciliação."
     }
    },
    {
     "id": "CPC-11-R2-02",
     "ponto": "DBA26-CPC-11",
     "tema": "Foro nas ações de reparação",
     "assertiva": "Nas ações para reparação de dano de qualquer natureza, é competente o Juizado do foro do domicílio do autor ou do local do ato ou fato.",
     "gabarito": "C",
     "comentario": {
      "resumo": "**Art. 4º, III**; em qualquer hipótese, pode-se propor no domicílio do réu (par. ún.).",
      "lei": [
       {
        "lei": "L9099",
        "art": "4",
        "par": "",
        "inc": "",
        "rotulo": "Lei 9.099/1995, art. 4º, III",
        "texto": "III - do domicílio do autor ou do local do ato ou fato, nas ações para reparação de dano de qualquer natureza."
       }
      ],
      "palavras_chave": [
       "competência territorial",
       "reparação de dano"
      ],
      "aprofundamento": "As regras de competência territorial dos Juizados buscam facilitar o acesso à justiça. Nas ações de **reparação de dano**, a vítima pode escolher entre o foro de seu próprio domicílio e o do local do ato ou fato.\n\nA razão é proteger quem sofreu o dano: não seria justo obrigá-la a litigar no domicílio do causador, muitas vezes distante. O local do fato também é relevante porque ali estão as provas e testemunhas.\n\nAlém disso, a lei garante que, em qualquer hipótese, a ação pode ser proposta no foro do domicílio do réu. A banca costuma restringir a escolha a um único foro ou excluir o domicílio do autor.",
      "memorize": "JEC, reparação de dano: domicílio do autor ou local do fato (e sempre o do réu)."
     }
    },
    {
     "id": "CPC-11-R2-03",
     "ponto": "DBA26-CPC-11",
     "tema": "Citação por edital",
     "assertiva": "No Juizado Especial Cível admite-se a citação por edital quando o réu estiver em local incerto.",
     "gabarito": "E",
     "comentario": {
      "resumo": "Art. 18, § 2º: **não se fará citação por edital**. Réu não encontrado → extinção/remessa à Justiça comum.",
      "lei": [
       {
        "lei": "L9099",
        "art": "18",
        "par": "",
        "inc": "",
        "rotulo": "Lei 9.099/1995, art. 18, § 2º",
        "texto": "Não se fará citação por edital."
       }
      ],
      "palavras_chave": [
       "citação por edital",
       "vedação"
      ],
      "correcao": {
       "erro": "Admite a citação por edital no Juizado Especial Cível quando o réu estiver em local incerto.",
       "certo": "No Juizado Especial Cível não se faz citação por edital; não encontrado o réu, o caso segue para a Justiça comum."
      },
      "aprofundamento": "A citação por edital é **ficta**: presume-se que o réu soube da ação, embora não tenha sido encontrado. Ela é incompatível com os Juizados porque o procedimento é **oral e concentrado**, centrado na audiência de conciliação e na participação pessoal das partes.\n\nSe o réu não pode ser encontrado, o Juizado não tem como prosseguir de forma adequada. Um processo com réu citado por edital exigiria curador especial e uma defesa mais formal, o que contraria a simplicidade do rito.\n\nPor isso a lei veda a citação por edital. Não encontrado o réu, o processo é extinto ou remetido à Justiça comum, onde essa forma de citação é possível. A banca tenta admitir o edital nos Juizados como se valesse a regra do CPC.",
      "memorize": "JEC: sem citação por edital."
     }
    },
    {
     "id": "CPC-11-R2-04",
     "ponto": "DBA26-CPC-11",
     "tema": "Embargos de declaração no JEC",
     "assertiva": "Nos Juizados Especiais, os embargos de declaração interrompem o prazo para a interposição de recurso.",
     "gabarito": "C",
     "comentario": {
      "resumo": "**Art. 50** da Lei 9.099, com a redação do CPC/2015 (antes, suspendiam contra sentença).",
      "lei": [
       {
        "lei": "L9099",
        "art": "50",
        "par": "",
        "inc": "",
        "rotulo": "Lei 9.099/1995, art. 50",
        "texto": "Os embargos de declaração interrompem o prazo para a interposição de recurso."
       }
      ],
      "palavras_chave": [
       "embargos de declaração",
       "interrupção"
      ],
      "aprofundamento": "Na redação original da Lei dos Juizados, os embargos de declaração contra sentença **suspendiam** o prazo para recurso, enquanto no CPC eles interrompiam. Essa diferença gerava confusão e armadilhas para as partes.\n\nO CPC atual alterou a Lei dos Juizados para **uniformizar** o regime: os embargos de declaração **interrompem** o prazo, que recomeça por inteiro depois de seu julgamento. É a mesma regra do processo comum.\n\nA uniformização dá segurança jurídica e evita que as partes percam prazos por uma diferença técnica. A banca pode cobrar a regra antiga, de suspensão. Lembre: hoje, nos Juizados como no CPC, os embargos interrompem.",
      "memorize": "Juizados: embargos de declaração interrompem o prazo, como no CPC."
     }
    },
    {
     "id": "CPC-11-R2-05",
     "ponto": "DBA26-CPC-11",
     "tema": "MS contra ato de juizado",
     "assertiva": "Compete à turma recursal processar e julgar o mandado de segurança contra ato de juizado especial.",
     "gabarito": "C",
     "comentario": {
      "resumo": "**Súmula 376/STJ**.",
      "juris": [
       {
        "tribunal": "STJ",
        "fonte": "Súmula 376/STJ",
        "data": "18/03/2009",
        "texto": "Compete à turma recursal processar e julgar o mandado de segurança contra ato de juizado especial."
       }
      ],
      "palavras_chave": [
       "mandado de segurança",
       "turma recursal"
      ],
      "aprofundamento": "O mandado de segurança contra ato de juiz do Juizado Especial deve ser julgado por um órgão dentro do próprio sistema dos Juizados. A Súmula 376/STJ atribui essa competência à **turma recursal**.\n\nA razão é que a turma recursal é o órgão revisor das decisões do Juizado. Se o MS fosse ao Tribunal de Justiça, haveria uma quebra na estrutura dos Juizados, e o TJ passaria a revisar atos de um sistema que tem órgãos recursais próprios.\n\nO MS nos Juizados é usado excepcionalmente, porque as decisões interlocutórias, em regra, não são recorríveis de imediato. A banca costuma atribuir a competência ao Tribunal de Justiça.",
      "memorize": "MS contra ato de juizado especial: turma recursal (Súmula 376/STJ)."
     }
    },
    {
     "id": "CPC-11-R2-06",
     "ponto": "DBA26-CPC-11",
     "tema": "RE nos Juizados",
     "assertiva": "Não cabe recurso extraordinário contra decisão proferida por turma recursal de juizado especial cível.",
     "gabarito": "E",
     "comentario": {
      "resumo": "Súmula 640/STF: **cabe RE** (o art. 102, III, da CF fala em \"causas decididas em única ou última instância\", sem exigir tribunal). Contraste com a Súmula 203/STJ (não cabe REsp).",
      "juris": [
       {
        "tribunal": "STF",
        "fonte": "Súmula 640/STF",
        "data": "24/09/2003",
        "texto": "É cabível RE contra decisão de juiz de 1º grau nas causas de alçada, ou de turma recursal de juizado especial cível e criminal."
       }
      ],
      "pegadinha": "Inverter as regras de RE (cabe) e REsp (não cabe).",
      "palavras_chave": [
       "recurso extraordinário",
       "turma recursal"
      ],
      "correcao": {
       "erro": "Nega o cabimento de recurso extraordinário contra decisão de turma recursal de juizado especial cível.",
       "certo": "Cabe recurso extraordinário contra decisão de turma recursal de juizado especial (Súmula 640/STF); o que não cabe é recurso especial (Súmula 203/STJ)."
      },
      "aprofundamento": "Os recursos aos tribunais superiores têm requisitos constitucionais diferentes. O **recurso especial** exige que a causa tenha sido decidida por **tribunal**, e a turma recursal não é tribunal. Por isso não cabe REsp (Súmula 203/STJ).\n\nO **recurso extraordinário**, por outro lado, exige apenas que a causa tenha sido decidida **em única ou última instância**, sem mencionar tribunal. A turma recursal decide em última instância no sistema dos Juizados, e por isso cabe RE, conforme a Súmula 640/STF.\n\nEssa é uma das pegadinhas mais frequentes: inverter as regras de RE e REsp. Lembre o critério constitucional de cada um: REsp exige tribunal; RE exige última instância.",
      "memorize": "Turma recursal: cabe RE (Súmula 640/STF), não cabe REsp (Súmula 203/STJ)."
     }
    },
    {
     "id": "CPC-11-R2-07",
     "ponto": "DBA26-CPC-11",
     "tema": "JEFP — tutela provisória",
     "assertiva": "No Juizado Especial da Fazenda Pública, o juiz poderá, de ofício ou a requerimento das partes, deferir quaisquer providências cautelares e antecipatórias no curso do processo para evitar dano de difícil ou de incerta reparação.",
     "gabarito": "C",
     "comentario": {
      "resumo": "**Art. 3º** da Lei 12.153/2009.",
      "lei": [
       {
        "lei": "L12153",
        "art": "3",
        "par": "",
        "inc": "",
        "rotulo": "Lei 12.153/2009, art. 3º",
        "texto": "O juiz poderá, de ofício ou a requerimento das partes, deferir quaisquer providências cautelares e antecipatórias no curso do processo, para evitar dano de difícil ou de incerta reparação."
       }
      ],
      "palavras_chave": [
       "JEFP",
       "de ofício",
       "cautelar"
      ],
      "aprofundamento": "O Juizado da Fazenda Pública não abre mão da **tutela de urgência**. Mesmo com o rito simplificado, há situações em que esperar o julgamento final causaria dano irreparável, como no fornecimento de medicamentos.\n\nA lei permite ao juiz deferir quaisquer providências **cautelares e antecipatórias** no curso do processo, para evitar dano de difícil ou incerta reparação. Note que ele pode agir **de ofício**, sem requerimento da parte, o que é uma peculiaridade do sistema.\n\nA lógica é a efetividade: o Juizado da Fazenda Pública trata de muitas demandas sensíveis, como saúde e direitos de servidores, e a tutela de urgência é essencial. A banca costuma exigir requerimento da parte ou vedar a tutela antecipada contra a Fazenda nesse sistema.",
      "memorize": "JEFP: juiz pode conceder cautelar ou antecipação de ofício ou a requerimento."
     }
    },
    {
     "id": "CPC-11-R2-08",
     "ponto": "DBA26-CPC-11",
     "tema": "JEFP — reexame necessário",
     "assertiva": "As sentenças condenatórias proferidas no Juizado Especial da Fazenda Pública estão sujeitas a reexame necessário.",
     "gabarito": "E",
     "comentario": {
      "resumo": "Art. 11: **não haverá reexame necessário**.",
      "lei": [
       {
        "lei": "L12153",
        "art": "11",
        "par": "",
        "inc": "",
        "rotulo": "Lei 12.153/2009, art. 11",
        "texto": "Nas causas de que trata esta Lei, não haverá reexame necessário."
       }
      ],
      "palavras_chave": [
       "reexame necessário"
      ],
      "correcao": {
       "erro": "Sujeita ao reexame necessário as sentenças condenatórias do Juizado Especial da Fazenda Pública.",
       "certo": "Nas causas do Juizado Especial da Fazenda Pública não há reexame necessário."
      },
      "aprofundamento": "O **reexame necessário** protege a Fazenda Pública contra sentenças desfavoráveis. Nos Juizados da Fazenda Pública, porém, a lei afasta esse instituto, em nome da **celeridade**.\n\nA razão é que as causas dos Juizados têm valor limitado e menor complexidade, e o reexame obrigatório anularia a vantagem de rapidez do sistema. A Fazenda continua podendo recorrer, se quiser, mas não há remessa automática.\n\nÉ coerente com a lógica do sistema, que também afasta o prazo diferenciado para os entes públicos. Os Juizados da Fazenda tratam o poder público em condições mais próximas das do particular. A banca aplica o reexame como se valesse a regra do processo comum.",
      "memorize": "JEFP: sem reexame necessário e sem prazo diferenciado."
     }
    },
    {
     "id": "CPC-11-R2-09",
     "ponto": "DBA26-CPC-11",
     "tema": "JEFP — causas excluídas",
     "assertiva": "Incluem-se na competência do Juizado Especial da Fazenda Pública os mandados de segurança de valor até 60 salários mínimos.",
     "gabarito": "E",
     "comentario": {
      "resumo": "Art. 2º, § 1º, I: excluídos **MS, desapropriação, divisão e demarcação, ações populares, improbidade, execução fiscal** e demandas sobre direitos difusos e coletivos.",
      "excecoes": [
       "MS, desapropriação, divisão/demarcação, populares, improbidade, execuções fiscais, difusos e coletivos (§ 1º, I)",
       "Bens imóveis dos entes (§ 1º, II)",
       "Impugnação de demissão de servidor ou sanção disciplinar a militar (§ 1º, III)"
      ],
      "lei": [
       {
        "lei": "L12153",
        "art": "2",
        "par": "",
        "inc": "",
        "rotulo": "Lei 12.153/2009, art. 2º, § 1º, I",
        "texto": "I – as ações de mandado de segurança, de desapropriação, de divisão e demarcação, populares, por improbidade administrativa, execuções fiscais e as demandas sobre direitos ou interesses difusos e coletivos;"
       }
      ],
      "palavras_chave": [
       "exclusões",
       "mandado de segurança"
      ],
      "correcao": {
       "erro": "Inclui na competência do Juizado da Fazenda Pública os mandados de segurança de valor até 60 salários mínimos.",
       "certo": "Estão excluídos da competência do Juizado da Fazenda Pública os mandados de segurança, entre outras causas, independentemente do valor."
      },
      "aprofundamento": "O Juizado da Fazenda Pública tem competência para causas de até 60 salários mínimos, mas algumas causas ficam fora, independentemente do valor. São causas que exigem **cognição mais profunda**, têm **rito próprio** ou envolvem **interesses coletivos**.\n\nO **mandado de segurança** tem rito especial e constitucional. A desapropriação, a divisão e a demarcação, a ação popular, a improbidade e a execução fiscal também têm procedimentos próprios. As demandas sobre direitos difusos e coletivos são incompatíveis com a lógica individual dos Juizados.\n\nTambém ficam fora as causas sobre bens imóveis dos entes e as impugnações a demissão de servidor ou sanção disciplinar a militar. A banca inclui o MS com a condição do valor, mas a exclusão é pela matéria.",
      "memorize": "Fora do JEFP: MS, desapropriação, divisão/demarcação, popular, improbidade, execução fiscal, difusos e coletivos."
     }
    },
    {
     "id": "CPC-11-R2-10",
     "ponto": "DBA26-CPC-11",
     "tema": "JEFP — conciliação pelo ente",
     "assertiva": "Os representantes judiciais dos réus presentes à audiência poderão conciliar, transigir ou desistir nos processos dos Juizados Especiais da Fazenda Pública, nos termos e hipóteses previstos na lei do respectivo ente.",
     "gabarito": "C",
     "comentario": {
      "resumo": "**Art. 8º.**",
      "lei": [
       {
        "lei": "L12153",
        "art": "8",
        "par": "",
        "inc": "",
        "rotulo": "Lei 12.153/2009, art. 8º",
        "texto": "Os representantes judiciais dos réus presentes à audiência poderão conciliar, transigir ou desistir nos processos da competência dos Juizados Especiais, nos termos e nas hipóteses previstas na lei do respectivo ente da Federação."
       }
      ],
      "palavras_chave": [
       "conciliação",
       "Fazenda Pública"
      ],
      "aprofundamento": "A **conciliação** é o objetivo preferencial dos Juizados, e isso vale também quando o réu é a Fazenda Pública. Mas o poder público não pode transigir livremente: os procuradores precisam de autorização legal para dispor de interesses públicos.\n\nPor isso a lei permite que os representantes judiciais dos réus conciliem, transijam ou desistam nos processos dos Juizados da Fazenda, **nos termos e hipóteses previstos na lei do respectivo ente**. Cada ente federativo define, por lei própria, os limites dessa autorização.\n\nA regra equilibra a busca pela autocomposição com o princípio da **indisponibilidade do interesse público**. A banca costuma dizer que o procurador pode transigir livremente ou que a conciliação é vedada à Fazenda.",
      "memorize": "JEFP: procurador concilia, transige ou desiste nos limites da lei do ente."
     }
    },
    {
     "id": "CPC-12-R2-01",
     "ponto": "DBA26-CPC-12",
     "tema": "Efeitos patrimoniais do MS",
     "assertiva": "A concessão de mandado de segurança não produz efeitos patrimoniais em relação a período pretérito, que devem ser reclamados administrativamente ou pela via judicial própria.",
     "gabarito": "C",
     "comentario": {
      "resumo": "**Súmula 271**/STF; no mesmo sentido, o art. 14, § 4º, da Lei 12.016 (servidor: só parcelas vencidas a partir do ajuizamento).",
      "lei": [
       {
        "lei": "L12016",
        "art": "14",
        "par": "",
        "inc": "",
        "rotulo": "Lei 12.016/2009, art. 14, § 4º",
        "texto": "somente será efetuado relativamente às prestações que se vencerem a contar da data do ajuizamento da inicial."
       }
      ],
      "juris": [
       {
        "tribunal": "STF",
        "fonte": "Súmula 271/STF",
        "data": "13/12/1963",
        "texto": "A concessão de MS não produz efeitos patrimoniais quanto a período pretérito, que devem ser reclamados administrativamente ou pela via judicial própria."
       }
      ],
      "palavras_chave": [
       "efeitos patrimoniais",
       "Súmula 271"
      ],
      "aprofundamento": "O mandado de segurança é ação **mandamental**: ordena à autoridade que faça ou deixe de fazer algo, corrigindo uma ilegalidade presente ou futura. Ele não foi pensado para reparar prejuízos passados.\n\nA Súmula 271/STF afirma que a concessão do MS não produz efeitos patrimoniais quanto a período pretérito. Os valores anteriores à impetração devem ser reclamados administrativamente ou por ação própria. A Lei do MS segue a mesma lógica ao limitar o pagamento de vencimentos de servidores às prestações vencidas a partir do ajuizamento.\n\nA lógica é a mesma que impede usar o MS como substituto da ação de cobrança. A banca costuma dizer que o MS pode abranger os valores passados se o direito for líquido e certo.",
      "memorize": "MS não produz efeitos patrimoniais pretéritos (Súmula 271/STF)."
     }
    },
    {
     "id": "CPC-12-R2-02",
     "ponto": "DBA26-CPC-12",
     "tema": "Controvérsia jurídica no MS",
     "assertiva": "A existência de controvérsia sobre matéria de direito impede a concessão de mandado de segurança, por afastar a liquidez e certeza do direito.",
     "gabarito": "E",
     "comentario": {
      "resumo": "Súmula 625/STF: **não impede**. \"Líquido e certo\" refere-se aos **fatos** provados de plano, não à tese jurídica.",
      "juris": [
       {
        "tribunal": "STF",
        "fonte": "Súmula 625/STF",
        "data": "24/09/2003",
        "texto": "Controvérsia sobre matéria de direito não impede concessão de mandado de segurança."
       }
      ],
      "palavras_chave": [
       "direito líquido e certo",
       "Súmula 625"
      ],
      "correcao": {
       "erro": "Afirma que a controvérsia sobre matéria de direito afasta a liquidez e certeza e impede o mandado de segurança.",
       "certo": "Controvérsia sobre matéria de direito não impede a concessão de mandado de segurança (Súmula 625/STF); a liquidez e certeza diz respeito aos fatos provados de plano."
      },
      "aprofundamento": "Um erro comum é confundir **direito líquido e certo** com direito sobre o qual não há discussão jurídica. Na verdade, a expressão se refere aos **fatos**: eles devem estar provados de plano, por documentos, sem necessidade de instrução.\n\nA questão de direito, por mais complexa e controvertida que seja, pode ser resolvida pelo juiz no MS. A Súmula 625/STF afirma que a controvérsia sobre matéria de direito não impede a concessão da segurança.\n\nA lógica é que interpretar o direito é função do juiz, e não exige produção de prova. O que impede o MS é a necessidade de dilação probatória sobre fatos. A banca confunde os dois planos.",
      "memorize": "Líquido e certo = fatos provados de plano; controvérsia jurídica não impede o MS (Súmula 625/STF)."
     }
    },
    {
     "id": "CPC-12-R2-03",
     "ponto": "DBA26-CPC-12",
     "tema": "MS em licitação de estatal",
     "assertiva": "Não cabe mandado de segurança contra ato praticado em licitação promovida por sociedade de economia mista, por se tratar de pessoa jurídica de direito privado.",
     "gabarito": "E",
     "comentario": {
      "resumo": "Súmula 333/STJ: **cabe** MS (o ato de licitação é de autoridade). Não cabe, sim, contra **atos de gestão comercial** (Lei 12.016, art. 1º, § 2º).",
      "lei": [
       {
        "lei": "L12016",
        "art": "1",
        "par": "",
        "inc": "",
        "rotulo": "Lei 12.016/2009, art. 1º, § 2º",
        "texto": "Não cabe mandado de segurança contra os atos de gestão comercial praticados pelos administradores de empresas públicas, de sociedade de economia mista e de concessionárias de serviço público."
       }
      ],
      "juris": [
       {
        "tribunal": "STJ",
        "fonte": "Súmula 333/STJ",
        "data": "13/12/2006",
        "texto": "Cabe mandado de segurança contra ato praticado em licitação promovida por sociedade de economia mista ou empresa pública."
       }
      ],
      "palavras_chave": [
       "licitação",
       "estatais",
       "Súmula 333"
      ],
      "correcao": {
       "erro": "Nega o cabimento de mandado de segurança contra ato de licitação de sociedade de economia mista por ser pessoa jurídica de direito privado.",
       "certo": "Cabe mandado de segurança contra ato praticado em licitação promovida por sociedade de economia mista ou empresa pública (Súmula 333/STJ); não cabe contra atos de gestão comercial."
      },
      "aprofundamento": "Sociedades de economia mista e empresas públicas são pessoas jurídicas de direito privado, mas, quando fazem **licitação**, exercem uma função pública, sujeita aos princípios da administração. O ato praticado na licitação é **ato de autoridade**.\n\nPor isso a Súmula 333/STJ admite o mandado de segurança contra ato praticado em licitação promovida por essas entidades. A natureza privada da entidade não afasta a natureza pública do ato.\n\nA fronteira está nos **atos de gestão comercial**, como a venda de produtos ou a celebração de contratos no mercado. Nesses, a entidade atua como qualquer empresa privada, e a Lei do MS afasta expressamente o cabimento. A banca usa a natureza privada da entidade para negar o MS na licitação.",
      "memorize": "Licitação de estatal: cabe MS (Súmula 333/STJ). Ato de gestão comercial: não."
     }
    },
    {
     "id": "CPC-12-R2-04",
     "ponto": "DBA26-CPC-12",
     "tema": "MS e compensação tributária",
     "assertiva": "O mandado de segurança constitui ação adequada para a declaração do direito à compensação tributária.",
     "gabarito": "C",
     "comentario": {
      "resumo": "Súmula 213/STJ. Atenção ao contraponto: **não cabe** MS para convalidar compensação **já realizada** pelo contribuinte (Súmula 460/STJ).",
      "juris": [
       {
        "tribunal": "STJ",
        "fonte": "Súmula 213/STJ",
        "data": "23/09/1998",
        "texto": "O mandado de segurança constitui ação adequada para a declaração do direito à compensação tributária."
       }
      ],
      "palavras_chave": [
       "compensação tributária",
       "Súmula 213"
      ],
      "aprofundamento": "A **compensação tributária** é o encontro de contas entre o crédito do contribuinte contra o fisco e o débito tributário dele. O contribuinte que entende ter direito a compensar pode buscar uma declaração judicial desse direito.\n\nA Súmula 213/STJ reconhece que o mandado de segurança é ação **adequada** para isso. O MS declara o direito, com base em prova documental, e a compensação será feita depois, sob fiscalização da administração.\n\nO contraponto é a Súmula 460/STJ: o MS **não serve** para convalidar compensação já realizada pelo contribuinte por conta própria. Nesse caso, seria preciso examinar a regularidade dos valores compensados, o que exige dilação probatória. A banca costuma misturar as duas súmulas.",
      "memorize": "MS declara o direito à compensação (Súmula 213/STJ), mas não convalida a já feita (Súmula 460/STJ)."
     }
    },
    {
     "id": "CPC-12-R2-05",
     "ponto": "DBA26-CPC-12",
     "tema": "Convalidação de compensação",
     "assertiva": "É cabível mandado de segurança para convalidar a compensação tributária já realizada pelo contribuinte.",
     "gabarito": "E",
     "comentario": {
      "resumo": "Súmula 460/STJ: **incabível**. O MS serve para **declarar o direito** à compensação (Súmula 213), não para chancelar a que já foi feita.",
      "juris": [
       {
        "tribunal": "STJ",
        "fonte": "Súmula 460/STJ",
        "data": "25/08/2010",
        "texto": "É incabível o mandado de segurança para convalidar a compensação tributária realizada pelo contribuinte."
       }
      ],
      "palavras_chave": [
       "compensação",
       "Súmula 460"
      ],
      "correcao": {
       "erro": "Admite mandado de segurança para convalidar compensação tributária já realizada pelo contribuinte.",
       "certo": "É incabível o mandado de segurança para convalidar a compensação tributária realizada pelo contribuinte (Súmula 460/STJ); cabe apenas para declarar o direito à compensação."
      },
      "aprofundamento": "Quando o contribuinte já fez a compensação por conta própria, o fisco pode questioná-la. Se o contribuinte impetra MS para que o juiz confirme a regularidade da compensação já feita, o juiz teria de verificar os valores, os créditos e os débitos, o que exige **exame de provas** e cálculos complexos.\n\nO MS não comporta essa dilação probatória. Por isso a Súmula 460/STJ o considera **incabível** para convalidar compensação já realizada.\n\nO caminho correto é o MS **preventivo**, para declarar o direito à compensação antes de realizá-la (Súmula 213/STJ). A diferença está no momento: antes da compensação, cabe MS para declarar; depois, não cabe para convalidar.",
      "memorize": "Compensação já feita: MS não convalida (Súmula 460/STJ)."
     }
    },
    {
     "id": "CPC-12-R2-06",
     "ponto": "DBA26-CPC-12",
     "tema": "MS contra decisão transitada",
     "assertiva": "Admite-se mandado de segurança contra decisão judicial transitada em julgado quando houver ilegalidade manifesta.",
     "gabarito": "E",
     "comentario": {
      "resumo": "Súmula 268/STF e art. 5º, III, da Lei 12.016: **não cabe**. O caminho é a **ação rescisória**.",
      "juris": [
       {
        "tribunal": "STF",
        "fonte": "Súmula 268/STF",
        "data": "13/12/1963",
        "texto": "Não cabe mandado de segurança contra decisão judicial com trânsito em julgado."
       }
      ],
      "palavras_chave": [
       "coisa julgada",
       "Súmula 268"
      ],
      "correcao": {
       "erro": "Admite mandado de segurança contra decisão judicial transitada em julgado quando houver ilegalidade manifesta.",
       "certo": "Não cabe mandado de segurança contra decisão judicial com trânsito em julgado (Súmula 268/STF); o caminho é a ação rescisória."
      },
      "aprofundamento": "A **coisa julgada** é garantia constitucional de estabilidade das decisões. O mandado de segurança não pode ser usado para desfazê-la, porque isso equivaleria a uma rescisória sem os requisitos e o prazo dessa ação.\n\nA Súmula 268/STF e a Lei do MS vedam o mandado contra decisão judicial transitada em julgado. Mesmo uma ilegalidade manifesta não autoriza o MS, porque a lei já prevê o meio próprio para atacar a coisa julgada: a **ação rescisória**.\n\nA lógica é preservar o sistema: cada vício tem seu instrumento de correção, e o MS não pode ser atalho para contornar a coisa julgada. A banca usa a \"ilegalidade manifesta\" como justificativa para admitir o MS.",
      "memorize": "Decisão transitada em julgado: não cabe MS (Súmula 268/STF); cabe rescisória."
     }
    },
    {
     "id": "CPC-12-R2-07",
     "ponto": "DBA26-CPC-12",
     "tema": "Vara privativa",
     "assertiva": "A existência de vara privativa, instituída por lei estadual, não altera a competência territorial resultante das leis de processo.",
     "gabarito": "C",
     "comentario": {
      "resumo": "**Súmula 206/STJ**.",
      "juris": [
       {
        "tribunal": "STJ",
        "fonte": "Súmula 206/STJ",
        "data": "01/04/1998",
        "texto": "A existência de vara privativa, instituída por lei estadual, não altera a competência territorial resultante das leis de processo."
       }
      ],
      "palavras_chave": [
       "vara privativa",
       "competência territorial"
      ],
      "aprofundamento": "A competência territorial é matéria de **lei processual**, de competência da União. As leis estaduais de organização judiciária podem criar varas especializadas, mas não podem alterar a distribuição territorial das causas fixada pelo CPC.\n\nA Súmula 206/STJ afirma que a existência de vara privativa, instituída por lei estadual, não altera a competência territorial. Por exemplo, a criação de uma vara da Fazenda Pública na capital não obriga que todas as ações contra o Estado sejam propostas ali, se a lei processual permite o ajuizamento em outro foro.\n\nA vara privativa organiza a distribuição **dentro** de uma comarca, mas não desloca causas de uma comarca para outra. A banca costuma dizer que a vara privativa atrai todas as causas da matéria.",
      "memorize": "Vara privativa por lei estadual não altera a competência territorial (Súmula 206/STJ)."
     }
    },
    {
     "id": "CPC-12-R2-08",
     "ponto": "DBA26-CPC-12",
     "tema": "MS coletivo sem autorização",
     "assertiva": "Segundo o STF, a impetração de mandado de segurança coletivo por entidade de classe em favor dos associados depende de autorização expressa destes.",
     "gabarito": "E",
     "comentario": {
      "resumo": "Súmula 629/STF: **independe** de autorização (substituição processual — CF, art. 5º, LXX). Diferente da ação coletiva ordinária de associação (CF, art. 5º, XXI).",
      "juris": [
       {
        "tribunal": "STF",
        "fonte": "Súmula 629/STF",
        "data": "24/09/2003",
        "texto": "A impetração de MS coletivo por entidade de classe em favor dos associados independe da autorização destes."
       }
      ],
      "palavras_chave": [
       "MS coletivo",
       "substituição processual"
      ],
      "correcao": {
       "erro": "Exige, segundo o STF, autorização expressa dos associados para a impetração do MS coletivo pela entidade de classe.",
       "certo": "A impetração de mandado de segurança coletivo por entidade de classe em favor dos associados independe da autorização destes (Súmula 629/STF)."
      },
      "aprofundamento": "No mandado de segurança coletivo, a entidade de classe atua como **substituta processual**: defende, em nome próprio, direitos de seus associados. A Constituição atribui essa legitimidade diretamente à entidade, e por isso a Súmula 629/STF dispensa a autorização dos associados.\n\nÉ preciso distinguir essa situação da **representação processual** nas ações coletivas ordinárias propostas por associações. Nesses casos, a Constituição exige autorização expressa dos associados, porque a associação atua como representante, e não como substituta.\n\nA diferença tem consequências práticas sobre quem se beneficia da decisão. Na prova, lembre: no MS coletivo, substituição, sem autorização; na ação coletiva ordinária de associação, representação, com autorização.",
      "memorize": "MS coletivo: substituição processual, sem autorização (Súmula 629/STF)."
     }
    }
   ]
  }
 ]
};
