# Pente Fino de Direito Processual Penal — CPP-1 (noções), 1.1 (princípios), 1.2 (fontes), 1.3 (lei processual) e
# 1.4 (sistemas, estrutura acusatória e juiz das garantias) (08/11/2026).
from base import I
from cpp_juris import J

CPP = 'CPP:'
CF = 'CF:'

# ======================= CPP-1 · Direito processual penal =======================
P = 'DBA26-CPP-1'
I(P, 1, 'Competência legislativa',
  'Compete privativamente à União legislar sobre direito processual, o que inclui o processo penal.', 'C',
  'É a **competência privativa da União** (CF, art. 22, I). Lei complementar pode autorizar os Estados a legislar sobre questões específicas (art. 22, par. ún.).',
  lei=[(CF + '22', 'Compete privativamente à União legislar sobre', 'penal, processual', 'CF, art. 22, I')],
  kw=['competência privativa da União', 'direito processual'])
I(P, 1, 'Procedimentos em matéria processual',
  'Estados e Distrito Federal não têm competência alguma para legislar sobre procedimentos em matéria processual, matéria reservada com exclusividade à União.', 'E',
  'Sobre **procedimentos em matéria processual** a competência é **concorrente** (CF, art. 24, XI): a União fixa normas gerais e os Estados suplementam. Processo é privativo da União; procedimento é concorrente.',
  lei=[(CF + '24', 'procedimentos em matéria processual', None, 'CF, art. 24, XI')],
  peg='Confundir processo (art. 22, I, privativa) com procedimento (art. 24, XI, concorrente).',
  kw=['concorrente', 'procedimentos em matéria processual'])
I(P, 1, 'Aplicação territorial do CPP',
  'O processo penal rege-se, em todo o território brasileiro, pelo Código de Processo Penal, ressalvados, entre outros, os tratados, as convenções e as regras de direito internacional.', 'C',
  'Art. 1º do CPP: regra da **territorialidade** (lex fori), com ressalvas como os **tratados e convenções** e as prerrogativas constitucionais de certas autoridades.',
  lei=[(CPP + '1', 'O processo penal reger-se-á, em todo o território brasileiro, por este Código, ressalvados:', None, 'CPP, art. 1º, caput')],
  kw=['territorialidade', 'tratados'])
I(P, 1, 'Devido processo legal',
  'Ninguém será privado da liberdade ou de seus bens sem o devido processo legal, garantia que, no processo penal, impede a imposição de pena sem processo.', 'C',
  'O **devido processo legal** (CF, art. 5º, LIV) é a matriz das demais garantias: não há pena sem processo (nulla poena sine judicio).',
  lei=[(CF + '5', 'ninguém será privado da liberdade ou de seus bens sem o devido processo legal', None, 'CF, art. 5º, LIV')],
  kw=['devido processo legal', 'nulla poena sine judicio'])
I(P, 1, 'Razoável duração',
  'A razoável duração do processo é assegurada apenas no âmbito judicial, não alcançando os procedimentos administrativos, como o inquérito policial.', 'E',
  'A CF assegura a **razoável duração do processo** "no âmbito judicial **e administrativo**" (art. 5º, LXXVIII). O excesso de prazo também se controla na investigação.',
  lei=[(CF + '5', 'a todos, no âmbito judicial e administrativo, são assegurados a razoável duração do processo', None, 'CF, art. 5º, LXXVIII')],
  peg='Retirar o "administrativo" do texto constitucional.',
  kw=['razoável duração do processo', 'judicial e administrativo'])
I(P, 1, 'Ação penal pública e o MP',
  'A promoção da ação penal pública é função institucional privativa do Ministério Público, na forma da lei.', 'C',
  'CF, art. 129, I: **privativamente** ao MP. A exceção constitucional é a **ação penal privada subsidiária** (art. 5º, LIX).',
  lei=[(CF + '129', 'promover, privativamente, a ação penal pública, na forma da lei', None, 'CF, art. 129, I')],
  exc=['Ação privada subsidiária da pública, se o MP não agir no prazo legal (CF, art. 5º, LIX; CPP, art. 29)'],
  kw=['privativamente', 'ação penal pública'])
# --- CPP-1 · Rodada 2
I(P, 2, 'Inércia e processo',
  'Por força do sistema acusatório, o juiz pode, excepcionalmente, iniciar a ação penal de ofício nas contravenções penais, como previa a redação originária do CPP.', 'E',
  'O antigo **processo judicialiforme** (ação iniciada por portaria do juiz ou da autoridade policial) **não foi recepcionado**: a CF deu ao MP a titularidade **privativa** da ação pública (art. 129, I).',
  lei=[(CF + '129', 'promover, privativamente, a ação penal pública, na forma da lei', None, 'CF, art. 129, I')],
  peg='Ressuscitar o procedimento judicialiforme das contravenções.',
  kw=['processo judicialiforme', 'não recepcionado'])
I(P, 2, 'Lei estadual e matéria processual',
  'Lei complementar federal pode autorizar os Estados a legislar sobre questões específicas das matérias de competência privativa da União, entre elas o direito processual.', 'C',
  'É o **parágrafo único do art. 22** da CF: delegação por **lei complementar**, para **questões específicas**.',
  lei=[(CF + '22', 'Lei complementar poderá autorizar os Estados a legislar sobre questões específicas', None, 'CF, art. 22, par. ún.')],
  kw=['lei complementar', 'questões específicas'])
I(P, 2, 'Persecução penal',
  'A persecução penal compreende duas fases: a investigação preliminar, de natureza administrativa e em regra conduzida pela polícia judiciária, e a ação penal, de natureza judicial.', 'C',
  '**Persecutio criminis**: fase **pré-processual** (investigação, administrativa) e fase **processual** (ação penal). À polícia civil cabe a polícia judiciária e a apuração de infrações (CF, art. 144, § 4º).',
  lei=[(CF + '144', 'Às polícias civis, dirigidas por delegados de polícia de carreira', 'exceto as militares', 'CF, art. 144, § 4º')],
  kw=['persecução penal', 'polícia judiciária'])
I(P, 2, 'Jurisdição e prisão',
  'Ninguém será preso senão em flagrante delito ou por ordem escrita e fundamentada de autoridade judiciária competente, sem exceção.', 'E',
  'A CF ressalva a **transgressão militar** e o **crime propriamente militar**, definidos em lei (art. 5º, LXI).',
  lei=[(CF + '5', 'ninguém será preso senão em flagrante delito', 'crime propriamente militar, definidos em lei', 'CF, art. 5º, LXI')],
  peg='Apagar a ressalva militar com "sem exceção".',
  kw=['ordem escrita e fundamentada', 'transgressão militar'])

# ======================= CPP-1.1 · Princípios, conceito, finalidade, características =======================
P = 'DBA26-CPP-1.1'
I(P, 1, 'Presunção de inocência',
  'Ninguém será considerado culpado até o trânsito em julgado de sentença penal condenatória.', 'C',
  'É a **presunção de inocência** (ou de não culpabilidade), CF, art. 5º, LVII. Dela decorrem a regra de tratamento e a regra probatória (in dubio pro reo).',
  lei=[(CF + '5', 'ninguém será considerado culpado até o trânsito em julgado de sentença penal condenatória', None, 'CF, art. 5º, LVII')],
  kw=['presunção de inocência', 'trânsito em julgado'])
I(P, 1, 'Contraditório e ampla defesa',
  'O contraditório e a ampla defesa são assegurados aos acusados em geral apenas no processo judicial, não alcançando os litigantes em processo administrativo.', 'E',
  'CF, art. 5º, LV: **contraditório e ampla defesa** aos litigantes em processo **judicial ou administrativo** e aos acusados em geral.',
  lei=[(CF + '5', 'aos litigantes, em processo judicial ou administrativo, e aos acusados em geral', 'meios e recursos a ela inerentes', 'CF, art. 5º, LV')],
  peg='Restringir a garantia ao processo judicial.',
  kw=['contraditório e ampla defesa', 'processo administrativo'])
I(P, 1, 'Direito ao silêncio',
  'O silêncio do acusado no interrogatório não importa confissão e não pode ser interpretado em prejuízo da defesa.', 'C',
  'É o **nemo tenetur se detegere**: CF, art. 5º, LXIII, e CPP, art. 186, par. ún. A parte final do art. 198 (silêncio como elemento de convicção) é tida por **não recepcionada**.',
  lei=[(CPP + '186', 'O silêncio, que não importará em confissão, não poderá ser interpretado em prejuízo da defesa', None, 'CPP, art. 186, par. ún.')],
  kw=['silêncio', 'nemo tenetur se detegere'])
I(P, 1, 'Juiz natural',
  'Ninguém será processado nem sentenciado senão pela autoridade competente, e não haverá juízo ou tribunal de exceção.', 'C',
  '**Juiz natural**: CF, art. 5º, XXXVII e LIII. A competência deve ser fixada por regras gerais e prévias ao fato.',
  lei=[(CF + '5', 'ninguém será processado nem sentenciado senão pela autoridade competente', None, 'CF, art. 5º, LIII')],
  kw=['juiz natural', 'tribunal de exceção'])
I(P, 1, 'Publicidade',
  'A publicidade dos atos processuais é absoluta e não admite restrição por lei, por ser garantia do acusado.', 'E',
  'A **publicidade** é a regra, mas a lei pode restringi-la quando a **defesa da intimidade** ou o **interesse social** o exigirem (CF, art. 5º, LX).',
  lei=[(CF + '5', 'a lei só poderá restringir a publicidade dos atos processuais quando a defesa da intimidade ou o interesse social o exigirem', None, 'CF, art. 5º, LX')],
  kw=['publicidade', 'interesse social'])
I(P, 1, 'Falta e deficiência da defesa',
  'No processo penal, tanto a falta quanto a deficiência da defesa constituem nulidade absoluta, dispensada a prova de prejuízo.', 'E',
  'Súmula 523/STF: **falta** de defesa = nulidade **absoluta**; **deficiência** só anula se houver **prova de prejuízo**.',
  juris=[J['STF523']],
  peg='Equiparar deficiência à falta de defesa.',
  kw=['deficiência', 'prova de prejuízo'])
I(P, 1, 'Provas ilícitas como princípio',
  'São inadmissíveis, no processo, as provas obtidas por meios ilícitos.', 'C',
  '**Vedação constitucional** (CF, art. 5º, LVI), desenvolvida no art. 157 do CPP (desentranhamento e derivadas).',
  lei=[(CF + '5', 'são inadmissíveis, no processo, as provas obtidas por meios ilícitos', None, 'CF, art. 5º, LVI')],
  kw=['provas ilícitas', 'inadmissíveis'])
# --- CPP-1.1 · Rodada 2
I(P, 2, 'Silêncio e qualificação',
  'O direito ao silêncio abrange as perguntas sobre a qualificação do acusado, de modo que ele pode recusar-se a informar nome e dados pessoais sem qualquer consequência.', 'E',
  'Para a posição majoritária, o **silêncio** alcança o **interrogatório de mérito**; a **qualificação** não está coberta, e a recusa ou a falsa identidade podem ter reflexo penal (ex.: CP, art. 307; LCP, art. 68). O art. 186 fala em informar o direito "antes de iniciar o interrogatório", após a qualificação.',
  lei=[(CPP + '186', 'Depois de devidamente qualificado e cientificado do inteiro teor da acusação', 'do seu direito de permanecer calado', 'CPP, art. 186, caput')],
  peg='Estender o silêncio à qualificação.',
  kw=['qualificação', 'interrogatório de mérito'])
I(P, 2, 'Identidade física do juiz',
  'Não há no CPP regra de identidade física do juiz, que é princípio exclusivo do processo civil.', 'E',
  'Desde 2008, o CPP prevê a **identidade física do juiz** (art. 399, § 2º): o juiz que presidiu a instrução deve proferir a sentença.',
  lei=[(CPP + '399', 'O juiz que presidiu a instrução deverá proferir a sentença', None, 'CPP, art. 399, § 2º')],
  peg='Negar regra expressa do CPP.',
  kw=['identidade física do juiz', 'instrução'])
I(P, 2, 'Motivação das decisões',
  'Todas as decisões do Poder Judiciário serão fundamentadas, sob pena de nulidade.', 'C',
  'CF, art. 93, IX: **motivação** obrigatória, sob pena de **nulidade**. No CPP, a preventiva exige decisão motivada e fundamentada (art. 315).',
  lei=[(CF + '93', 'fundamentadas todas as decisões, sob pena de nulidade', None, 'CF, art. 93, IX')],
  kw=['motivação', 'nulidade'])
I(P, 2, 'Silêncio e advertência',
  'O preso será informado de seus direitos, entre os quais o de permanecer calado, sendo-lhe assegurada a assistência da família e de advogado.', 'C',
  'CF, art. 5º, LXIII. Prevalece na jurisprudência que a falta do aviso ("aviso de Miranda") gera nulidade **relativa**, a depender de prejuízo.',
  lei=[(CF + '5', 'o preso será informado de seus direitos, entre os quais o de permanecer calado', None, 'CF, art. 5º, LXIII')],
  kw=['aviso de Miranda', 'permanecer calado'])
I(P, 2, 'Contraditório no inquérito',
  'Em razão da garantia do contraditório, o inquérito policial é nulo se o investigado não for intimado para acompanhar cada diligência.', 'E',
  'O inquérito é **inquisitivo**: não há contraditório pleno; a defesa tem **acesso** aos elementos já documentados (SV 14) e pode requerer diligências, sem obrigação de intimação prévia a cada ato.',
  juris=[J['SV14']],
  peg='Transpor ao inquérito o contraditório do processo.',
  kw=['inquisitivo', 'acesso aos autos'])

# ======================= CPP-1.2 · Fontes =======================
P = 'DBA26-CPP-1.2'
I(P, 1, 'Fonte material',
  'Fonte material (de produção) do processo penal é o ente que cria a norma: em regra, a União, por sua competência privativa para legislar sobre direito processual.', 'C',
  '**Fonte material** = quem produz a norma: a **União** (CF, art. 22, I); os Estados de forma concorrente quanto a **procedimentos** (art. 24, XI) e por delegação (art. 22, par. ún.).',
  lei=[(CF + '22', 'Compete privativamente à União legislar sobre', 'penal, processual', 'CF, art. 22, I')],
  kw=['fonte material', 'União'])
I(P, 1, 'Fonte formal imediata',
  'A lei é a fonte formal imediata do processo penal, e os tratados e convenções internacionais também podem ser fonte formal, como reconhece o próprio CPP.', 'C',
  '**Fontes formais** (de cognição): a **lei** (imediata) e, nos termos do art. 1º, I, do CPP, **tratados, convenções e regras de direito internacional**.',
  lei=[(CPP + '1', 'os tratados, as convenções e regras de direito internacional', None, 'CPP, art. 1º, I')],
  kw=['fonte formal', 'tratados'])
I(P, 1, 'Princípios gerais do direito',
  'O CPP veda o suplemento dos princípios gerais de direito, admitindo apenas a interpretação literal da lei processual.', 'E',
  'O art. 3º do CPP **admite** interpretação extensiva, aplicação analógica **e o suplemento dos princípios gerais de direito**.',
  lei=[(CPP + '3', 'A lei processual penal admitirá interpretação extensiva e aplicação analógica', 'princípios gerais de direito', 'CPP, art. 3º')],
  peg='Inverter o art. 3º, que é permissivo.',
  kw=['princípios gerais de direito', 'aplicação analógica'])
I(P, 1, 'Súmula vinculante',
  'As súmulas vinculantes do STF, por terem efeito vinculante para o Judiciário e a administração pública, funcionam como fonte formal no processo penal, a exemplo da que trata do acesso do defensor aos elementos de prova do inquérito.', 'C',
  'A **súmula vinculante** obriga juízes e administração (CF, art. 103-A) e é apontada como **fonte formal**. Exemplo: **SV 14** (acesso do defensor aos autos da investigação).',
  juris=[J['SV14']],
  kw=['súmula vinculante', 'fonte formal'])
I(P, 1, 'Costume',
  'O costume pode revogar norma processual penal que caiu em desuso, por força da desuetudo.', 'E',
  'O **costume** é fonte formal **mediata** (ou indireta) e serve à **interpretação**; não revoga lei (LINDB, art. 2º: a lei vigora até que outra a modifique ou revogue).',
  lei=[('LINDB:2', 'Não se destinando à vigência temporária, a lei terá vigor até que outra a modifique ou revogue', None, 'LINDB, art. 2º')],
  peg='Atribuir ao desuso força revogatória.',
  kw=['costume', 'desuetudo'])
# --- CPP-1.2 · Rodada 2
I(P, 2, 'Tratados e audiência de custódia',
  'A audiência de custódia, antes de prevista no CPP pela Lei 13.964/2019, já encontrava fundamento na Convenção Americana sobre Direitos Humanos, que assegura à pessoa presa ser conduzida, sem demora, à presença de um juiz.', 'C',
  'É exemplo de **tratado como fonte**: a CADH (art. 7.5) já exigia a apresentação **sem demora** ao juiz. Hoje, CPP, art. 310 (audiência em até 24 horas).',
  lei=[('CADH:7', 'Toda pessoa detida ou retida deve ser conduzida, sem demora, à presença de um juiz', None, 'CADH, art. 7.5')],
  kw=['CADH', 'audiência de custódia'])
I(P, 2, 'Constituição estadual como fonte',
  'A Constituição estadual pode criar foro por prerrogativa de função, mas esse foro não prevalece sobre a competência constitucional do Tribunal do Júri.', 'C',
  '**SV 45**: o júri (competência da CF) prevalece sobre foro **estabelecido exclusivamente pela Constituição Estadual**.',
  juris=[J['SV45']],
  kw=['Constituição Estadual', 'Tribunal do Júri'])
I(P, 2, 'Regimento interno como fonte',
  'Os regimentos internos dos tribunais não podem dispor sobre matéria processual penal em nenhuma hipótese.', 'E',
  'Os **regimentos internos** disciplinam a competência e o funcionamento dos órgãos jurisdicionais dos tribunais (CF, art. 96, I, a), observadas as normas de processo; por isso, são citados como fonte (ex.: procedimentos internos de recursos).',
  lei=[(CF + '96', 'elaborar seus regimentos internos, com observância das normas de processo', None, 'CF, art. 96, I, a')],
  peg='Negar qualquer papel ao regimento interno.',
  kw=['regimento interno', 'normas de processo'])
I(P, 2, 'Analogia e fonte',
  'Admite-se no processo penal a aplicação analógica, inclusive em desfavor do acusado, desde que se trate de norma genuinamente processual.', 'C',
  'Ao contrário do Direito Penal material, a lei **processual** admite **analogia** (CPP, art. 3º) sem a limitação in bonam partem. Norma **mista** (com conteúdo penal) segue as regras do direito material.',
  lei=[(CPP + '3', 'A lei processual penal admitirá interpretação extensiva e aplicação analógica', None, 'CPP, art. 3º')],
  exc=['Normas processuais mistas ou híbridas (ex.: ação penal, decadência, prisão) seguem a lógica penal: sem analogia in malam partem e com retroatividade benéfica'],
  kw=['analogia', 'norma genuinamente processual'])

# ======================= CPP-1.3 · Lei processual: eficácia, interpretação, analogia, imunidades =======================
P = 'DBA26-CPP-1.3'
I(P, 1, 'Tempus regit actum',
  'A lei processual penal aplica-se desde logo, devendo ser renovados os atos realizados sob a vigência da lei anterior.', 'E',
  'Art. 2º do CPP: **aplicação imediata** (tempus regit actum), **sem prejuízo da validade** dos atos já praticados.',
  lei=[(CPP + '2', 'A lei processual penal aplicar-se-á desde logo', 'sob a vigência da lei anterior', 'CPP, art. 2º')],
  peg='Anular atos válidos praticados sob a lei anterior.',
  kw=['aplicação imediata', 'tempus regit actum'])
I(P, 1, 'Retroatividade da lei processual',
  'A lei genuinamente processual penal mais benéfica ao réu retroage para invalidar os atos praticados validamente sob a lei anterior.', 'E',
  'A lei **puramente processual** não retroage nem anula atos passados: aplica-se **de imediato** (art. 2º). Quem retroage em benefício é a lei **penal** ou a norma **mista** (CF, art. 5º, XL).',
  lei=[(CPP + '2', 'A lei processual penal aplicar-se-á desde logo', 'sob a vigência da lei anterior', 'CPP, art. 2º'),
       (CF + '5', 'a lei penal não retroagirá, salvo para beneficiar o réu', None, 'CF, art. 5º, XL')],
  peg='Atribuir à norma processual pura a retroatividade da lei penal.',
  kw=['norma mista', 'retroatividade'])
I(P, 1, 'Interpretação extensiva',
  'A lei processual penal admite interpretação extensiva e aplicação analógica.', 'C',
  'Literal no **art. 3º** do CPP.',
  lei=[(CPP + '3', 'A lei processual penal admitirá interpretação extensiva e aplicação analógica', None, 'CPP, art. 3º')],
  kw=['interpretação extensiva', 'aplicação analógica'])
I(P, 1, 'Imunidade parlamentar',
  'Desde a expedição do diploma, os membros do Congresso Nacional não poderão ser presos, salvo em flagrante de qualquer crime doloso.', 'E',
  'A ressalva é só o **flagrante de crime inafiançável** (CF, art. 53, § 2º); os autos vão à Casa em 24 horas para que resolva sobre a prisão.',
  lei=[(CF + '53', 'Desde a expedição do diploma, os membros do Congresso Nacional não poderão ser presos, salvo em flagrante de crime inafiançável', None, 'CF, art. 53, § 2º')],
  peg='Trocar "crime inafiançável" por "qualquer crime doloso".',
  kw=['imunidade formal', 'crime inafiançável'])
I(P, 1, 'Imunidade diplomática',
  'A imunidade diplomática afasta a aplicação da lei processual brasileira por força de tratado, o que o CPP admite ao ressalvar os tratados e as regras de direito internacional.', 'C',
  'A Convenção de Viena sobre Relações Diplomáticas é exemplo da ressalva do **art. 1º, I**, do CPP: exceção à **territorialidade**.',
  lei=[(CPP + '1', 'os tratados, as convenções e regras de direito internacional', None, 'CPP, art. 1º, I')],
  kw=['imunidade diplomática', 'territorialidade'])
I(P, 1, 'Analogia e interpretação analógica',
  'Analogia e interpretação analógica são sinônimos no processo penal, pois ambas pressupõem lacuna da lei.', 'E',
  '**Analogia** é forma de **integração** (há lacuna). **Interpretação analógica** é **interpretação**: a própria lei traz fórmula casuística seguida de cláusula genérica.',
  lei=[(CPP + '3', 'A lei processual penal admitirá interpretação extensiva e aplicação analógica', None, 'CPP, art. 3º')],
  peg='Igualar integração (analogia) e interpretação analógica.',
  kw=['analogia', 'integração'])
# --- CPP-1.3 · Rodada 2
I(P, 2, 'Norma mista e ANPP',
  'Por ter conteúdo penal e processual, a norma do acordo de não persecução penal pode alcançar processos em andamento quando entrou em vigor a Lei 13.964/2019, desde que o pedido tenha sido feito antes do trânsito em julgado, segundo o STF.', 'C',
  'STF, **HC 185.913** (Plenário, 18/09/2024): ANPP cabe em processo em curso na vigência da lei nova, mesmo sem confissão anterior, se pedido **antes do trânsito em julgado**.',
  juris=[J['HC185913']],
  kw=['norma mista', 'ANPP'])
I(P, 2, 'Imunidade e Casa legislativa',
  'Em caso de crime cometido nas dependências da Câmara dos Deputados ou do Senado, o poder de polícia da Casa compreende, consoante o regimento, a prisão em flagrante do acusado e a realização do inquérito.', 'C',
  'É a **Súmula 397/STF**: polícia legislativa e inquérito, nos termos do regimento.',
  juris=[J['STF397']],
  kw=['poder de polícia', 'Súmula 397'])
I(P, 2, 'Prerrogativa e lei no tempo',
  'A lei que altera regra de competência por prerrogativa de função, por ser processual, aplica-se imediatamente aos processos em curso, preservados os atos já praticados.', 'C',
  'Competência é tema **processual**: incide o **art. 2º** do CPP (aplicação imediata, preservados os atos válidos).',
  lei=[(CPP + '2', 'A lei processual penal aplicar-se-á desde logo', 'sob a vigência da lei anterior', 'CPP, art. 2º')],
  kw=['aplicação imediata', 'competência'])
I(P, 2, 'Imunidade e processo de parlamentar',
  'Recebida a denúncia contra deputado federal por crime ocorrido após a diplomação, o STF não pode dar seguimento ao processo sem prévia licença da Câmara.', 'E',
  'Desde a EC 35/2001, **não há licença prévia**: o STF recebe a denúncia e dá **ciência à Casa**, que pode **sustar** o andamento por voto da maioria de seus membros (CF, art. 53, § 3º).',
  lei=[(CF + '53', 'Recebida a denúncia contra o Senador ou Deputado, por crime ocorrido após a diplomação', 'sustar o andamento da ação', 'CF, art. 53, § 3º')],
  peg='Ressuscitar a licença prévia anterior a 2001.',
  kw=['sustar o andamento', 'licença prévia'])

# ======================= CPP-1.4 · Sistemas, estrutura acusatória, juiz das garantias =======================
P = 'DBA26-CPP-1.4'
I(P, 1, 'Estrutura acusatória',
  'O processo penal terá estrutura acusatória, vedadas a iniciativa do juiz na fase de investigação e a substituição da atuação probatória do órgão de acusação.', 'C',
  'Literal no **art. 3º-A** (Lei 13.964/2019), declarado constitucional pelo STF nas ADIs do juiz das garantias.',
  lei=[(CPP + '3-A', 'O processo penal terá estrutura acusatória', 'atuação probatória do órgão de acusação', 'CPP, art. 3º-A')],
  kw=['estrutura acusatória', 'iniciativa do juiz'])
I(P, 1, 'Sistema inquisitivo',
  'No sistema inquisitivo, as funções de acusar, defender e julgar concentram-se em uma só pessoa, e o acusado é tratado como objeto do processo.', 'C',
  '**Inquisitivo**: concentração de funções, sigilo, ausência de contraditório, réu como **objeto**. **Acusatório**: funções separadas, réu como **sujeito de direitos**.',
  lei=[(CPP + '3-A', 'O processo penal terá estrutura acusatória', None, 'CPP, art. 3º-A')],
  kw=['sistema inquisitivo', 'concentração de funções'])
I(P, 1, 'Juiz das garantias — função',
  'O juiz das garantias é responsável pelo controle da legalidade da investigação criminal e pela salvaguarda dos direitos individuais cuja franquia tenha sido reservada à autorização prévia do Poder Judiciário.', 'C',
  'Caput do **art. 3º-B**. O STF declarou a implantação **obrigatória** (ADIs 6.298, 6.299, 6.300 e 6.305).',
  lei=[(CPP + '3-B', 'O juiz das garantias é responsável pelo controle da legalidade da investigação criminal', 'autorização prévia do Poder Judiciário', 'CPP, art. 3º-B, caput')],
  juris=[J['ADI6298']],
  kw=['juiz das garantias', 'controle da legalidade'])
I(P, 1, 'Juiz das garantias — implantação',
  'Segundo o STF, a implantação do juiz das garantias é facultativa, cabendo a cada tribunal decidir se a adota.', 'E',
  'O STF fixou implantação **obrigatória**, em **12 meses prorrogáveis por mais 12**, contados da publicação da ata do julgamento (24/08/2023).',
  juris=[J['ADI6298']],
  peg='Trocar "obrigatória" por "facultativa" (era a proposta vencida do relator).',
  kw=['obrigatória', '12 meses'])
I(P, 1, 'Juiz das garantias — término',
  'Segundo o STF, a competência do juiz das garantias cessa com o oferecimento da denúncia, cabendo ao juiz da instrução analisar o seu recebimento.', 'C',
  'O texto do art. 3º-C falava em **recebimento**; o STF deu interpretação para que a competência cesse com o **oferecimento** da denúncia.',
  lei=[(CPP + '3-C', 'A competência do juiz das garantias abrange todas as infrações penais', None, 'CPP, art. 3º-C, caput')],
  juris=[J['ADI6298']],
  peg='Repetir a letra do art. 3º-C ("recebimento"), superada pela interpretação do STF.',
  kw=['oferecimento da denúncia', 'juiz da instrução'])
I(P, 1, 'Juiz das garantias — exceções',
  'Segundo o STF, as regras do juiz das garantias aplicam-se aos processos do Tribunal do Júri e aos crimes de violência doméstica e familiar.', 'E',
  'O STF **excluiu** do juiz das garantias: processos de competência originária do **STF e STJ**, o **Tribunal do Júri**, a **violência doméstica e familiar** e as **infrações de menor potencial ofensivo**.',
  juris=[J['ADI6298']],
  peg='Incluir júri e violência doméstica, que o STF excluiu.',
  kw=['Tribunal do Júri', 'violência doméstica'])
I(P, 1, 'Conversão de ofício',
  'Após a Lei 13.964/2019, o juiz pode, de ofício, converter a prisão em flagrante em preventiva quando presentes os requisitos do art. 312 do CPP.', 'E',
  '**Súmula 676/STJ**: não é mais possível ao juiz, **de ofício**, decretar ou converter o flagrante em preventiva. O art. 311 exige requerimento do MP, do querelante ou do assistente, ou representação da autoridade policial.',
  lei=[(CPP + '311', 'caberá a prisão preventiva decretada pelo juiz, a requerimento do Ministério Público', 'representação da autoridade policial', 'CPP, art. 311')],
  juris=[J['S676']],
  peg='A banca mantém o "de ofício", retirado pela Lei 13.964/2019.',
  kw=['de ofício', 'Súmula 676'])
# --- CPP-1.4 · Rodada 2
I(P, 2, 'Sistema misto',
  'O sistema misto, ou francês, combina uma fase de instrução preliminar inquisitiva com uma fase judicial acusatória, com contraditório e publicidade.', 'C',
  'É o modelo do Código napoleônico (1808). O Brasil, com o **art. 3º-A**, declara expressamente a **estrutura acusatória**, embora a investigação seja inquisitiva.',
  lei=[(CPP + '3-A', 'O processo penal terá estrutura acusatória', None, 'CPP, art. 3º-A')],
  kw=['sistema misto', 'francês'])
I(P, 2, 'Juiz das garantias e excesso de prazo',
  'Segundo o STF, o decurso do prazo do inquérito com investigado preso acarreta o relaxamento automático da prisão, como prevê o art. 3º-B, § 2º, do CPP.', 'E',
  'O STF **afastou o relaxamento automático**: vencido o prazo, o juiz avalia os motivos que justificam a manutenção da prisão.',
  lei=[(CPP + '3-B', 'Se o investigado estiver preso, o juiz das garantias poderá', 'prorrogar, uma única vez, a duração do inquérito por até 15 (quinze) dias', 'CPP, art. 3º-B, § 2º')],
  juris=[J['ADI6298']],
  peg='Tomar a letra do § 2º sem a interpretação dada pelo STF.',
  kw=['relaxamento automático', 'excesso de prazo'])
I(P, 2, 'Prova inadmissível e impedimento',
  'O juiz que conhecer do conteúdo da prova declarada inadmissível fica impedido de proferir a sentença, regra do art. 157, § 5º, do CPP plenamente eficaz.', 'E',
  'O STF declarou **inconstitucional** o **art. 157, § 5º** (impedimento do juiz que conheceu da prova inadmissível).',
  juris=[J['ADI6298']],
  peg='Apresentar como vigente dispositivo declarado inconstitucional.',
  kw=['art. 157, § 5º', 'inconstitucional'])
I(P, 2, 'Juiz das garantias e Justiça Eleitoral',
  'Segundo o STF, o juiz das garantias atuará também nos processos criminais da Justiça Eleitoral.', 'C',
  'O STF ressalvou a aplicação aos processos criminais **eleitorais**, ao lado das exclusões (originários do STF/STJ, júri, violência doméstica e menor potencial ofensivo).',
  juris=[J['ADI6298']],
  kw=['Justiça Eleitoral', 'juiz das garantias'])
I(P, 2, 'Juiz e produção de prova',
  'Mesmo sob a estrutura acusatória, o juiz pode, no curso da instrução ou antes de sentenciar, determinar diligências para dirimir dúvida sobre ponto relevante.', 'C',
  'O **art. 156, II**, segue no Código: atuação **supletiva** do juiz na instrução, sem substituir a acusação (art. 3º-A).',
  lei=[(CPP + '156', 'determinar, no curso da instrução, ou antes de proferir sentença', 'ponto relevante', 'CPP, art. 156, II')],
  kw=['iniciativa probatória', 'supletiva'])
