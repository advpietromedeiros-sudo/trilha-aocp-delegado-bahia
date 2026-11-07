from base import I, J

P = 'DBA26-CPC-1'
# ---------------- PONTO 1 · Normas fundamentais — RODADA 1
I(P, 1, 'Princípio dispositivo e impulso oficial',
  'O processo civil começa por iniciativa da parte e se desenvolve por impulso oficial, salvo as exceções previstas em lei.', 'C',
  'É a literalidade do art. 2º: **inércia** para começar (iniciativa da parte) e **impulso oficial** para andar.',
  lei=[('L13105:2', 'O processo começa', 'previstas em lei.', 'CPC, art. 2º')],
  kw=['inércia', 'impulso oficial'])
I(P, 1, 'Métodos consensuais',
  'A conciliação, a mediação e outros métodos de solução consensual de conflitos deverão ser estimulados por juízes, advogados, defensores públicos e membros do Ministério Público, vedada sua utilização depois de instaurado o processo judicial.', 'E',
  'O estímulo vale **inclusive no curso do processo judicial**. A banca acrescentou uma vedação que a lei não traz.',
  lei=[('L13105:3', 'A conciliação, a mediação', 'no curso do processo judicial.', 'CPC, art. 3º, § 3º')],
  peg='Troca de "inclusive no curso do processo" por "vedada no curso do processo".',
  kw=['autocomposição', 'mediação', 'conciliação'])
I(P, 1, 'Duração razoável e primazia do mérito',
  'As partes têm o direito de obter em prazo razoável a solução integral do mérito, incluída a atividade satisfativa.', 'C',
  'Art. 4º: a **duração razoável** abrange também a **atividade satisfativa** (cumprimento/execução), não só a sentença.',
  lei=[('L13105:4', 'As partes têm o direito', 'atividade satisfativa.', 'CPC, art. 4º')],
  kw=['duração razoável', 'primazia do mérito', 'atividade satisfativa'])
I(P, 1, 'Cooperação',
  'O dever de cooperação previsto no CPC vincula apenas as partes e seus procuradores, não alcançando o juiz, que deve manter-se equidistante.', 'E',
  'Art. 6º: **todos os sujeitos do processo** devem cooperar — inclusive o juiz (deveres de esclarecimento, prevenção, consulta e auxílio).',
  lei=[('L13105:6', 'Todos os sujeitos do processo', 'justa e efetiva.', 'CPC, art. 6º')],
  kw=['cooperação', 'sujeitos do processo'])
I(P, 1, 'Contraditório prévio e exceções',
  'Não se proferirá decisão contra uma das partes sem que ela seja previamente ouvida, regra que não admite exceção nem mesmo para a tutela provisória de urgência.', 'E',
  'O art. 9º tem **exceções expressas** no parágrafo único: aí o contraditório é **diferido**, não suprimido.',
  regra='Contraditório prévio (art. 9º, caput).',
  exc=['Tutela provisória de urgência (art. 9º, par. ún., I)', 'Tutela da evidência do art. 311, II e III (art. 9º, par. ún., II)', 'Decisão do art. 701 — mandado monitório (art. 9º, par. ún., III)'],
  lei=[('L13105:9', 'Não se proferirá decisão', 'previamente ouvida.', 'CPC, art. 9º')],
  kw=['contraditório diferido', 'tutela de urgência'])
I(P, 1, 'Vedação à decisão surpresa',
  'O juiz não pode decidir, em grau algum de jurisdição, com base em fundamento sobre o qual não se tenha dado às partes oportunidade de se manifestar, ainda que se trate de matéria que deva decidir de ofício.', 'C',
  'Art. 10: **matéria de ofício** não dispensa o **contraditório**. O juiz pode conhecer de ofício, mas tem de ouvir antes.',
  lei=[('L13105:10', 'O juiz não pode decidir', 'decidir de ofício.', 'CPC, art. 10')],
  peg='A banca costuma dizer que a vedação "não se aplica às matérias de ordem pública" — errado.',
  kw=['decisão surpresa', 'matéria de ofício'])
I(P, 1, 'Publicidade e fundamentação',
  'Todos os julgamentos dos órgãos do Poder Judiciário serão públicos, e fundamentadas todas as decisões, sob pena de nulidade.', 'C',
  'Art. 11, caput, que repete o art. 93, IX, da CF: **publicidade** + **fundamentação**, sob pena de **nulidade**.',
  exc=['Segredo de justiça: pode ser autorizada a presença somente das partes, advogados, defensores públicos ou MP (art. 11, par. ún.)'],
  lei=[('L13105:11', 'Todos os julgamentos', 'sob pena de nulidade.', 'CPC, art. 11')],
  kw=['publicidade', 'fundamentação', 'nulidade'])
I(P, 1, 'Ordem cronológica de conclusão',
  'Os juízes e os tribunais atenderão obrigatoriamente à ordem cronológica de conclusão para proferir sentença ou acórdão.', 'E',
  'Desde a Lei 13.256/2016 o art. 12 diz **preferencialmente**, não "obrigatoriamente".',
  lei=[('L13105:12', 'Os juízes e os tribunais atenderão', 'sentença ou acórdão.', 'CPC, art. 12')],
  peg='"Preferencialmente" x "obrigatoriamente" — troca clássica.',
  kw=['ordem cronológica', 'preferencialmente'])
I(P, 1, 'Jurisdição civil e tratados',
  'A jurisdição civil será regida unicamente pelas normas processuais brasileiras, ressalvadas as disposições específicas previstas em tratados, convenções ou acordos internacionais de que o Brasil seja parte.', 'C',
  'Art. 13: regra da **lex fori**, com ressalva dos **tratados** internacionais.',
  lei=[('L13105:13', 'A jurisdição civil será regida', 'o Brasil seja parte.', 'CPC, art. 13')],
  kw=['lex fori', 'tratados'])
I(P, 1, 'Lei processual no tempo',
  'A norma processual nova aplica-se somente aos processos ajuizados após o início de sua vigência.', 'E',
  'Art. 14: a norma processual **não retroage**, mas tem **aplicação imediata aos processos em curso**, respeitados os atos praticados (teoria do **isolamento dos atos processuais**).',
  lei=[('L13105:14', 'A norma processual não retroagirá', 'sob a vigência da norma revogada.', 'CPC, art. 14')],
  kw=['isolamento dos atos processuais', 'aplicação imediata'])
I(P, 1, 'Aplicação supletiva e subsidiária',
  'Na ausência de normas que regulem processos eleitorais, trabalhistas ou administrativos, as disposições do CPC lhes serão aplicadas supletiva e subsidiariamente.', 'C',
  'Art. 15: o CPC é o **diploma geral** do processo — aplicação **supletiva e subsidiária** a esses três ramos.',
  lei=[('L13105:15', 'Na ausência de normas', 'supletiva e subsidiariamente.', 'CPC, art. 15')],
  kw=['supletiva', 'subsidiária'])
I(P, 1, 'Aplicação do ordenamento pelo juiz',
  'Ao aplicar o ordenamento jurídico, o juiz atenderá aos fins sociais e às exigências do bem comum, resguardando e promovendo a dignidade da pessoa humana e observando a proporcionalidade, a razoabilidade, a legalidade, a publicidade e a eficiência.', 'C',
  'Art. 8º: **fins sociais**, **bem comum**, **dignidade** e os vetores da proporcionalidade, razoabilidade, legalidade, publicidade e eficiência.',
  lei=[('L13105:8', 'Ao aplicar o ordenamento jurídico', 'a publicidade e a eficiência.', 'CPC, art. 8º')],
  kw=['fins sociais', 'dignidade', 'proporcionalidade'])

# ---------------- PONTO 1 — RODADA 2
I(P, 2, 'Solução consensual pelo Estado',
  'O Estado promoverá, obrigatoriamente e em todos os casos, a solução consensual dos conflitos.', 'E',
  'Art. 3º, § 2º: o Estado promoverá a solução consensual **sempre que possível**.',
  lei=[('L13105:3', 'O Estado promoverá', 'solução consensual dos conflitos.', 'CPC, art. 3º, § 2º')],
  peg='"Sempre que possível" virou "obrigatoriamente".',
  kw=['sempre que possível', 'solução consensual'])
I(P, 2, 'Evidência e contraditório diferido',
  'Admite-se decisão contra a parte sem sua oitiva prévia em todas as hipóteses de tutela da evidência, inclusive quando caracterizado o abuso do direito de defesa.', 'E',
  'Só a evidência dos incisos **II e III** do art. 311 dispensa a oitiva prévia. O **abuso do direito de defesa** (inciso I) pressupõe que o réu já se manifestou.',
  lei=[('L13105:9', 'II - às hipóteses de tutela da evidência', 'incisos II e III;', 'CPC, art. 9º, par. ún., II'),
       ('L13105:311', 'Parágrafo único. Nas hipóteses dos incisos II e III', 'decidir liminarmente.', 'CPC, art. 311, par. ún.')],
  kw=['tutela da evidência', 'liminar', 'abuso do direito de defesa'])
I(P, 2, 'Exclusões da ordem cronológica',
  'Estão excluídas da regra da ordem cronológica de conclusão as sentenças proferidas em audiência, homologatórias de acordo ou de improcedência liminar do pedido.', 'C',
  'É o art. 12, § 2º, I. Outras exclusões: julgamento em bloco de casos repetitivos, decisões dos arts. 485 e 932, embargos de declaração, agravo interno, preferências legais.',
  lei=[('L13105:12', 'I - as sentenças proferidas em audiência', 'improcedência liminar do pedido;', 'CPC, art. 12, § 2º, I')],
  kw=['ordem cronológica', 'exclusões'])
I(P, 2, 'Alcance da vedação à decisão surpresa',
  'A vedação à decisão surpresa aplica-se apenas ao juízo de primeiro grau, pois nos tribunais o relator pode decidir com base em fundamento não debatido.', 'E',
  'O art. 10 fala em **"grau algum de jurisdição"**; no tribunal, o art. 933 manda o relator intimar as partes sobre fato superveniente ou questão apreciável de ofício.',
  lei=[('L13105:10', 'em grau algum de jurisdição', None, 'CPC, art. 10'),
       ('L13105:933', 'Se o relator constatar', 'no prazo de 5 (cinco) dias.', 'CPC, art. 933')],
  kw=['decisão surpresa', 'tribunais'])
I(P, 2, 'Boa-fé processual',
  'O dever de comportar-se de acordo com a boa-fé restringe-se às partes, não alcançando terceiros intervenientes nem o juiz.', 'E',
  'Art. 5º: **aquele que de qualquer forma participa do processo** deve agir com boa-fé — boa-fé **objetiva**, para todos.',
  lei=[('L13105:5', 'Aquele que de qualquer forma participa', 'de acordo com a boa-fé.', 'CPC, art. 5º')],
  kw=['boa-fé objetiva'])
I(P, 2, 'Isonomia processual',
  'É assegurada às partes paridade de tratamento em relação ao exercício de direitos e faculdades processuais, competindo ao juiz zelar pelo efetivo contraditório.', 'C',
  'Art. 7º: **paridade de armas** e dever judicial de zelar pelo **contraditório efetivo**.',
  lei=[('L13105:7', 'É assegurada às partes paridade', 'zelar pelo efetivo contraditório.', 'CPC, art. 7º')],
  kw=['paridade de armas', 'contraditório efetivo'])
I(P, 2, 'Segredo de justiça',
  'Nos casos de segredo de justiça, pode ser autorizada a presença somente das partes, de seus advogados, de defensores públicos ou do Ministério Público.', 'C',
  'Art. 11, parágrafo único: a **publicidade restrita** não afasta as partes nem os seus representantes.',
  lei=[('L13105:11', 'Nos casos de segredo de justiça', 'do Ministério Público.', 'CPC, art. 11, par. ún.')],
  kw=['segredo de justiça', 'publicidade restrita'])
I(P, 2, 'Supletividade — processo penal',
  'O art. 15 do CPC prevê expressamente a aplicação supletiva e subsidiária de suas normas ao processo penal.', 'E',
  'O art. 15 só cita processos **eleitorais, trabalhistas e administrativos**. No processo penal a ponte é o art. 3º do CPP (analogia).',
  lei=[('L13105:15', 'processos eleitorais, trabalhistas ou administrativos', None, 'CPC, art. 15')],
  peg='Banca inclui "penais" na lista do art. 15.',
  kw=['art. 15', 'processo penal'])

P = 'DBA26-CPC-2'
# ---------------- PONTO 2 · Função jurisdicional — RODADA 1
I(P, 1, 'Jurisdição civil',
  'A jurisdição civil é exercida pelos juízes e pelos tribunais em todo o território nacional, conforme as disposições do CPC.', 'C',
  'Art. 16: a jurisdição é **una** e exercida em **todo o território nacional**; a competência é que a reparte.',
  lei=[('L13105:16', 'A jurisdição civil é exercida', 'conforme as disposições deste Código.', 'CPC, art. 16')],
  kw=['jurisdição', 'competência'])
I(P, 1, 'Condições da ação',
  'Para postular em juízo é necessário ter interesse, legitimidade e possibilidade jurídica do pedido.', 'E',
  'O art. 17 exige só **interesse e legitimidade**. A possibilidade jurídica do pedido saiu do rol no CPC/2015 (virou questão de mérito).',
  lei=[('L13105:17', 'Para postular em juízo', 'interesse e legitimidade.', 'CPC, art. 17')],
  peg='Inclusão da "possibilidade jurídica do pedido", que era do CPC/1973.',
  kw=['interesse', 'legitimidade', 'possibilidade jurídica'])
I(P, 1, 'Legitimação extraordinária',
  'Ninguém poderá pleitear direito alheio em nome próprio, salvo quando autorizado por lei em sentido estrito.', 'E',
  'O art. 18 fala em autorização pelo **ordenamento jurídico** — conceito mais amplo que "lei".',
  lei=[('L13105:18', 'Ninguém poderá pleitear', 'pelo ordenamento jurídico.', 'CPC, art. 18')],
  peg='"Ordenamento jurídico" trocado por "lei".',
  kw=['substituição processual', 'legitimação extraordinária'])
I(P, 1, 'Ação declaratória',
  'É admissível a ação meramente declaratória ainda que tenha ocorrido a violação do direito.', 'C',
  'Art. 20. E o interesse pode limitar-se à declaração da existência, inexistência ou modo de ser de relação jurídica ou da autenticidade/falsidade de documento (art. 19).',
  lei=[('L13105:20', 'É admissível a ação meramente declaratória', 'violação do direito.', 'CPC, art. 20')],
  kw=['ação declaratória'])
I(P, 1, 'Competência internacional exclusiva',
  'Compete à autoridade judiciária brasileira, com exclusão de qualquer outra, conhecer de ações relativas a imóveis situados no Brasil.', 'C',
  'Art. 23, I: **competência exclusiva**; decisão estrangeira sobre isso não é homologada (art. 964).',
  lei=[('L13105:23', 'Compete à autoridade judiciária brasileira, com exclusão', 'imóveis situados no Brasil;', 'CPC, art. 23, I')],
  kw=['competência exclusiva', 'imóveis'])
I(P, 1, 'Litispendência internacional',
  'A ação proposta perante tribunal estrangeiro induz litispendência e obsta que a autoridade judiciária brasileira conheça da mesma causa.', 'E',
  'Art. 24: **não induz litispendência** nem obsta o conhecimento da mesma causa no Brasil (ressalvados tratados).',
  lei=[('L13105:24', 'A ação proposta perante tribunal estrangeiro não induz litispendência', 'que lhe são conexas', 'CPC, art. 24')],
  kw=['litispendência', 'tribunal estrangeiro'])
I(P, 1, 'Perpetuação da jurisdição',
  'A competência é determinada no momento do registro ou da distribuição da petição inicial, sendo irrelevantes as modificações de fato ou de direito ocorridas posteriormente, salvo quando suprimirem órgão judiciário ou alterarem a competência absoluta.', 'C',
  'Art. 43: **perpetuatio jurisdictionis**, com duas exceções: **supressão do órgão** e **alteração da competência absoluta**.',
  lei=[('L13105:43', 'Determina-se a competência', 'alterarem a competência absoluta.', 'CPC, art. 43')],
  kw=['perpetuatio jurisdictionis', 'registro ou distribuição'])
I(P, 1, 'Foro geral',
  'A ação fundada em direito pessoal ou em direito real sobre bens móveis será proposta, em regra, no foro de domicílio do réu.', 'C',
  'Art. 46: **foro comum = domicílio do réu**.',
  lei=[('L13105:46', 'A ação fundada em direito pessoal', 'no foro de domicílio do réu.', 'CPC, art. 46')],
  kw=['domicílio do réu', 'foro comum'])
I(P, 1, 'Ações reais imobiliárias',
  'Para as ações fundadas em direito real sobre imóveis é competente, em regra, o foro de domicílio do réu.', 'E',
  'Art. 47: competente é o **foro de situação da coisa** (forum rei sitae).',
  lei=[('L13105:47', 'Para as ações fundadas em direito real sobre imóveis', 'foro de situação da coisa.', 'CPC, art. 47')],
  kw=['forum rei sitae', 'situação da coisa'])
I(P, 1, 'Foro de eleição',
  'As partes podem modificar, por cláusula de eleição de foro, a competência em razão da matéria, da pessoa ou da função.', 'E',
  'Art. 62: essas competências são **inderrogáveis**. Por convenção só se mudam a competência em razão do **valor** e do **território** (art. 63).',
  lei=[('L13105:62', 'A competência determinada em razão da matéria', 'inderrogável por convenção das partes.', 'CPC, art. 62'),
       ('L13105:63', 'As partes podem modificar a competência em razão do valor e do território', None, 'CPC, art. 63')],
  kw=['competência absoluta', 'foro de eleição', 'inderrogável'])
I(P, 1, 'Incompetência absoluta',
  'A incompetência absoluta pode ser alegada em qualquer tempo e grau de jurisdição e deve ser declarada de ofício.', 'C',
  'Art. 64, § 1º. Mas atenção: decidida a questão e transitada em julgado, ela só se ataca por **rescisória** (art. 966, II).',
  lei=[('L13105:64', 'A incompetência absoluta pode ser alegada', 'deve ser declarada de ofício.', 'CPC, art. 64, § 1º')],
  kw=['incompetência absoluta', 'de ofício'])
I(P, 1, 'Prorrogação da competência relativa',
  'Prorroga-se a competência relativa se o réu não a alegar por meio de exceção de incompetência, em peça autônoma, no prazo de 15 dias.', 'E',
  'No CPC/2015 a incompetência (absoluta ou relativa) é alegada como **preliminar de contestação** (art. 64); se o réu não alegar, **prorroga-se** (art. 65). Não há mais exceção em peça autônoma.',
  lei=[('L13105:64', 'A incompetência, absoluta ou relativa, será alegada como questão preliminar de contestação.', None, 'CPC, art. 64'),
       ('L13105:65', 'Prorrogar-se-á a competência relativa', 'preliminar de contestação.', 'CPC, art. 65')],
  peg='"Exceção de incompetência" é peça do CPC/1973.',
  kw=['prorrogação', 'preliminar de contestação'])

# ---------------- PONTO 2 — RODADA 2
I(P, 2, 'Risco de decisões conflitantes',
  'Serão reunidos para julgamento conjunto os processos que possam gerar risco de prolação de decisões conflitantes ou contraditórias caso decididos separadamente, mesmo sem conexão entre eles.', 'C',
  'Art. 55, § 3º: o CPC/2015 permite a reunião **mesmo sem conexão**, para evitar decisões conflitantes.',
  lei=[('L13105:55', 'Serão reunidos para julgamento conjunto os processos que possam gerar risco', 'mesmo sem conexão entre eles.', 'CPC, art. 55, § 3º')],
  kw=['conexão', 'decisões conflitantes'])
I(P, 2, 'Conexão e processo já sentenciado',
  'Os processos de ações conexas devem ser reunidos para decisão conjunta ainda que um deles já tenha sido sentenciado.', 'E',
  'Art. 55, § 1º: reúnem-se **salvo se um deles já houver sido sentenciado** — no mesmo sentido a Súmula 235/STJ.',
  lei=[('L13105:55', 'Os processos de ações conexas serão reunidos', 'já houver sido sentenciado.', 'CPC, art. 55, § 1º')],
  juris=[J['S235']],
  kw=['conexão', 'sentenciado'])
I(P, 2, 'Prevenção',
  'No CPC vigente, é a citação válida que torna prevento o juízo.', 'E',
  'Art. 59: **o registro ou a distribuição da petição inicial** torna prevento o juízo. A citação válida induz litispendência (art. 240), não prevenção.',
  lei=[('L13105:59', 'O registro ou a distribuição da petição inicial torna prevento o juízo.', None, 'CPC, art. 59')],
  kw=['prevenção', 'distribuição'])
I(P, 2, 'Intervenção da União',
  'Intervindo a União no processo que tramita na Justiça estadual, os autos serão remetidos à Justiça Federal, a quem compete decidir sobre a existência de interesse jurídico que justifique a presença do ente federal.', 'C',
  'Art. 45 + Súmula 150/STJ: quem decide se há interesse da União é a **Justiça Federal**. Exceções no próprio art. 45: recuperação judicial, falência, insolvência, acidente de trabalho, Justiça Eleitoral e do Trabalho.',
  exc=['Recuperação judicial, falência, insolvência civil e acidente de trabalho (art. 45, I)', 'Causas da Justiça Eleitoral e da Justiça do Trabalho (art. 45, II)'],
  lei=[('L13105:45', 'Tramitando o processo perante outro juízo', 'na qualidade de parte ou de terceiro interveniente', 'CPC, art. 45')],
  juris=[J['S150']],
  kw=['Justiça Federal', 'interesse da União'])
I(P, 2, 'Foro do alimentando',
  'É competente o foro de domicílio ou residência do alimentando para a ação em que se pedem alimentos.', 'C',
  'Art. 53, II: **foro privilegiado do alimentando** (parte presumidamente vulnerável).',
  lei=[('L13105:53', 'de domicílio ou residência do alimentando', 'pedem alimentos;', 'CPC, art. 53, II')],
  kw=['alimentos', 'foro do alimentando'])
I(P, 2, 'Cláusula de eleição abusiva',
  'A cláusula de eleição de foro abusiva pode ser reputada ineficaz de ofício pelo juiz a qualquer tempo, ainda que o réu, citado, não a tenha impugnado na contestação.', 'E',
  'De ofício, só **antes da citação** (art. 63, § 3º). Citado o réu, cabe a ele alegar na contestação, **sob pena de preclusão** (§ 4º).',
  lei=[('L13105:63', 'Citado, incumbe ao réu alegar', 'sob pena de preclusão.', 'CPC, art. 63, § 4º')],
  kw=['foro de eleição', 'abusividade', 'preclusão'])
I(P, 2, 'Efeitos da decisão do juízo incompetente',
  'Reconhecida a incompetência, são nulos todos os atos decisórios praticados pelo juízo incompetente.', 'E',
  'Art. 64, § 4º: **conservam-se os efeitos** da decisão do juízo incompetente até que outra seja proferida pelo competente, salvo decisão judicial em sentido contrário (translatio iudicii).',
  lei=[('L13105:64', 'Salvo decisão judicial em sentido contrário, conservar-se-ão os efeitos', 'pelo juízo competente.', 'CPC, art. 64, § 4º')],
  peg='"Nulos os atos decisórios" era a regra do CPC/1973.',
  kw=['translatio iudicii', 'conservação dos efeitos'])
I(P, 2, 'Estado ou DF como réu',
  'Se o Estado for o demandado, a ação poderá ser proposta no foro de domicílio do autor, no de ocorrência do ato ou fato que originou a demanda, no de situação da coisa ou na capital do respectivo ente federado.', 'C',
  'Art. 52, par. ún.: **foros concorrentes** à escolha do autor quando Estado ou DF é réu.',
  lei=[('L13105:52', 'Se Estado ou o Distrito Federal for o demandado', 'na capital do respectivo ente federado.', 'CPC, art. 52, par. ún.')],
  kw=['foros concorrentes', 'Fazenda Pública'])
I(P, 2, 'Carta rogatória',
  'Na carta rogatória, a defesa restringe-se à discussão quanto ao atendimento dos requisitos para que o pronunciamento judicial estrangeiro produza efeitos no Brasil, vedada a revisão do mérito.', 'C',
  'Art. 36, §§ 1º e 2º: juízo de **delibação** — sem revisão do mérito.',
  lei=[('L13105:36', 'A defesa restringir-se-á', 'produza efeitos no Brasil.', 'CPC, art. 36, § 1º')],
  kw=['carta rogatória', 'delibação'])

P = 'DBA26-CPC-3'
# ---------------- PONTO 3 · Sujeitos do processo — RODADA 1
I(P, 1, 'Capacidade processual',
  'Toda pessoa que se encontre no exercício de seus direitos tem capacidade para estar em juízo.', 'C',
  'Art. 70: **capacidade processual** acompanha a capacidade de exercício.',
  lei=[('L13105:70', 'Toda pessoa que se encontre no exercício', 'capacidade para estar em juízo.', 'CPC, art. 70')],
  kw=['capacidade processual'])
I(P, 1, 'Curador especial',
  'O juiz nomeará curador especial ao réu preso, ainda que ele tenha comparecido aos autos e contestado por advogado constituído.', 'E',
  'Art. 72, II: curador especial ao **réu preso revel** e ao revel citado por edital ou hora certa **enquanto não constituído advogado**. Função exercida pela **Defensoria Pública** (par. ún.).',
  lei=[('L13105:72', 'II - réu preso revel', 'não for constituído advogado.', 'CPC, art. 72, II')],
  kw=['curador especial', 'réu preso revel', 'Defensoria Pública'])
I(P, 1, 'Multa por litigância de má-fé',
  'O litigante de má-fé será condenado a pagar multa superior a 1% e inferior a 20% do valor corrigido da causa.', 'E',
  'Art. 81: multa **superior a 1% e inferior a 10%** do valor corrigido da causa, além de indenizar os prejuízos e pagar honorários e despesas.',
  lei=[('L13105:81', 'De ofício ou a requerimento, o juiz condenará', 'despesas que efetuou.', 'CPC, art. 81')],
  exc=['Valor da causa irrisório ou inestimável: multa de até 10 salários mínimos (art. 81, § 2º)'],
  kw=['má-fé', 'multa', '10%'])
I(P, 1, 'Honorários de sucumbência',
  'Os honorários serão fixados entre o mínimo de 10% e o máximo de 20% sobre o valor da condenação, do proveito econômico obtido ou, não sendo possível mensurá-lo, sobre o valor atualizado da causa.', 'C',
  'Art. 85, § 2º: faixa de **10% a 20%**, nessa ordem de base de cálculo. Contra a Fazenda, as faixas escalonadas do § 3º.',
  lei=[('L13105:85', 'Os honorários serão fixados entre o mínimo de dez', 'sobre o valor atualizado da causa', 'CPC, art. 85, § 2º')],
  kw=['honorários', '10% a 20%'])
I(P, 1, 'Gratuidade — presunção',
  'Presume-se verdadeira a alegação de insuficiência de recursos deduzida por pessoa jurídica.', 'E',
  'Art. 99, § 3º: a presunção vale para a alegação deduzida **exclusivamente por pessoa natural**. Pessoa jurídica tem de comprovar.',
  lei=[('L13105:99', 'Presume-se verdadeira a alegação de insuficiência deduzida exclusivamente por pessoa natural.', None, 'CPC, art. 99, § 3º')],
  kw=['gratuidade', 'pessoa natural', 'presunção'])
I(P, 1, 'Gratuidade e advogado particular',
  'A assistência do requerente por advogado particular não impede a concessão de gratuidade da justiça.', 'C',
  'Art. 99, § 4º. A gratuidade depende da **insuficiência de recursos**, não de quem patrocina a causa.',
  lei=[('L13105:99', 'A assistência do requerente por advogado particular', 'gratuidade da justiça.', 'CPC, art. 99, § 4º')],
  kw=['gratuidade', 'advogado particular'])
I(P, 1, 'Litisconsórcio multitudinário',
  'O juiz poderá limitar o litisconsórcio facultativo quanto ao número de litigantes na fase de conhecimento, na liquidação de sentença ou na execução, quando comprometer a rápida solução do litígio ou dificultar a defesa.', 'C',
  'Art. 113, § 1º: limitação do **litisconsórcio facultativo multitudinário**. O pedido de limitação **interrompe** o prazo de resposta (§ 2º).',
  lei=[('L13105:113', 'O juiz poderá limitar o litisconsórcio facultativo', 'cumprimento da sentença.', 'CPC, art. 113, § 1º')],
  kw=['litisconsórcio multitudinário'])
I(P, 1, 'Assistência',
  'A assistência só é admitida até o saneamento do processo, não podendo o assistente ingressar em grau recursal.', 'E',
  'Art. 119, par. ún.: assistência cabe **em qualquer procedimento e em todos os graus de jurisdição**; o assistente recebe o processo **no estado em que se encontre**.',
  lei=[('L13105:119', 'A assistência será admitida em qualquer procedimento', 'no estado em que se encontre.', 'CPC, art. 119, par. ún.')],
  kw=['assistência', 'interesse jurídico'])
I(P, 1, 'Denunciação da lide',
  'A denunciação da lide é obrigatória, sob pena de perda do direito de regresso.', 'E',
  'O art. 125 diz que a denunciação é **admissível**. Se indeferida, não promovida ou não permitida, o regresso vai por **ação autônoma** (§ 1º).',
  lei=[('L13105:125', 'O direito regressivo será exercido por ação autônoma', 'não for permitida.', 'CPC, art. 125, § 1º')],
  peg='"Obrigatória" era a leitura do art. 70 do CPC/1973.',
  kw=['denunciação da lide', 'ação autônoma'])
I(P, 1, 'Desconsideração da personalidade jurídica',
  'O incidente de desconsideração da personalidade jurídica pode ser instaurado de ofício pelo juiz.', 'E',
  'Art. 133: instaura-se **a pedido da parte ou do Ministério Público**, quando lhe couber intervir. Não há instauração de ofício.',
  lei=[('L13105:133', 'O incidente de desconsideração da personalidade jurídica será instaurado a pedido da parte', 'intervir no processo.', 'CPC, art. 133')],
  kw=['IDPJ', 'de ofício'])
I(P, 1, 'Suspeição',
  'Ser o juiz amigo íntimo de qualquer das partes é causa de impedimento.', 'E',
  'Amizade íntima ou inimizade é **suspeição** (art. 145, I). Impedimento (art. 144) envolve hipóteses objetivas (parente advogado, ter atuado como mandatário etc.).',
  lei=[('L13105:145', 'amigo íntimo ou inimigo de qualquer das partes ou de seus advogados', None, 'CPC, art. 145, I')],
  kw=['suspeição', 'impedimento'])
I(P, 1, 'MP como fiscal da ordem jurídica',
  'A participação da Fazenda Pública não configura, por si só, hipótese de intervenção do Ministério Público.', 'C',
  'Art. 178, par. ún. O MP intervém por **interesse público ou social**, **interesse de incapaz** e **litígios coletivos pela posse de terra**.',
  lei=[('L13105:178', 'A participação da Fazenda Pública não configura', 'intervenção do Ministério Público.', 'CPC, art. 178, par. ún.')],
  kw=['fiscal da ordem jurídica', 'Fazenda Pública'])

# ---------------- PONTO 3 — RODADA 2
I(P, 2, 'Outorga conjugal',
  'O cônjuge necessitará do consentimento do outro para propor ação que verse sobre direito real imobiliário, salvo quando casados sob o regime de separação absoluta de bens.', 'C',
  'Art. 73, caput. Vale também para união estável comprovada nos autos (§ 3º).',
  lei=[('L13105:73', 'O cônjuge necessitará do consentimento', 'separação absoluta de bens.', 'CPC, art. 73')],
  kw=['outorga conjugal', 'direito real imobiliário'])
I(P, 2, 'Amicus curiae — recursos',
  'O amicus curiae pode interpor qualquer recurso contra as decisões proferidas no processo em que intervém.', 'E',
  'Art. 138, § 1º: só **embargos de declaração** e recurso contra a decisão que julga o **IRDR** (§ 3º). A decisão que o admite ou inadmite é irrecorrível.',
  exc=['Embargos de declaração (art. 138, § 1º)', 'Recurso contra decisão que julga o IRDR (art. 138, § 3º)'],
  lei=[('L13105:138', 'A intervenção de que trata o caput não implica alteração de competência', 'embargos de declaração', 'CPC, art. 138, § 1º')],
  kw=['amicus curiae', 'recursos'])
I(P, 2, 'Chamamento ao processo',
  'É admissível o chamamento ao processo, requerido pelo réu, dos demais devedores solidários quando o credor exigir de um ou de alguns o pagamento da dívida comum.', 'C',
  'Art. 130, III. Também: o **afiançado** (I) e os **demais fiadores** (II).',
  lei=[('L13105:130', 'dos demais devedores solidários', 'dívida comum.', 'CPC, art. 130, III')],
  kw=['chamamento ao processo', 'solidariedade'])
I(P, 2, 'IDPJ — citação do sócio',
  'Instaurado o incidente de desconsideração, o sócio ou a pessoa jurídica será citado para manifestar-se e requerer as provas cabíveis no prazo de 5 dias.', 'E',
  'Art. 135: o prazo é de **15 dias**. Requerida na inicial, dispensa-se o incidente (art. 134, § 2º); instaurado, **suspende** o processo (§ 3º).',
  lei=[('L13105:135', 'Instaurado o incidente', 'no prazo de 15 (quinze) dias.', 'CPC, art. 135')],
  kw=['IDPJ', '15 dias'])
I(P, 2, 'Honorários por equidade',
  'Quando o valor da condenação ou da causa for muito elevado, o juiz pode fixar honorários por apreciação equitativa para evitar remuneração excessiva.', 'E',
  'Tema 1.076/STJ: equidade é **vedada** quando os valores são elevados; aplica-se a faixa dos §§ 2º ou 3º. Equidade só se o proveito for **inestimável ou irrisório** ou o valor da causa muito baixo (§ 8º).',
  lei=[('L13105:85', 'Nas causas em que for inestimável ou irrisório o proveito econômico', 'observando o disposto nos incisos do § 2º.', 'CPC, art. 85, § 8º')],
  juris=[J['T1076']],
  kw=['equidade', 'honorários', 'Tema 1.076'])
I(P, 2, 'Prazo em dobro da Advocacia Pública',
  'A União, os Estados, o DF, os Municípios e suas autarquias e fundações gozam de prazo em dobro para todas as manifestações processuais, inclusive quando a lei estabelecer, de forma expressa, prazo próprio para o ente público.', 'E',
  'Art. 183, § 2º: **não** se aplica o benefício quando a lei estabelecer prazo próprio para o ente público. O prazo em dobro conta da **intimação pessoal** (caput).',
  lei=[('L13105:183', 'Não se aplica o benefício da contagem em dobro', 'prazo próprio para o ente público.', 'CPC, art. 183, § 2º')],
  kw=['prazo em dobro', 'prazo próprio'])
I(P, 2, 'Recurso do MP fiscal',
  'O Ministério Público tem legitimidade para recorrer no processo em que oficiou como fiscal da ordem jurídica, ainda que não haja recurso da parte.', 'C',
  'Art. 996 (o recurso pode ser interposto pelo MP como parte ou como fiscal) e Súmula 99/STJ.',
  lei=[('L13105:996', 'O recurso pode ser interposto pela parte vencida', 'fiscal da ordem jurídica.', 'CPC, art. 996')],
  juris=[J['S99']],
  kw=['MP', 'legitimidade recursal'])
I(P, 2, 'Litisconsórcio e atos de um litisconsorte',
  'Os litisconsortes serão considerados litigantes distintos em suas relações com a parte adversa, exceto no litisconsórcio unitário, caso em que os atos e as omissões de um não prejudicarão os outros, mas os poderão beneficiar.', 'C',
  'Art. 117: regime da **autonomia** dos litisconsortes, mitigado no **unitário**.',
  lei=[('L13105:117', 'Os litisconsortes serão considerados', 'mas os poderão beneficiar.', 'CPC, art. 117')],
  kw=['litisconsórcio unitário', 'autonomia'])

P = 'DBA26-CPC-4'
# ---------------- PONTO 4 · Atos processuais — RODADA 1
I(P, 1, 'Negócio jurídico processual',
  'Versando o processo sobre direitos que admitam autocomposição, é lícito às partes plenamente capazes estipular mudanças no procedimento e convencionar sobre seus ônus, poderes, faculdades e deveres processuais, antes ou durante o processo.', 'C',
  'Art. 190: **cláusula geral de negócio processual** — partes **plenamente capazes** + direitos que admitam **autocomposição**.',
  lei=[('L13105:190', 'Versando o processo sobre direitos que admitam autocomposição', 'antes ou durante o processo.', 'CPC, art. 190')],
  kw=['negócio processual', 'autocomposição'])
I(P, 1, 'Conceito de sentença',
  'Sentença é o pronunciamento por meio do qual o juiz, com fundamento nos arts. 485 e 487, põe fim à fase cognitiva do procedimento comum, bem como extingue a execução.', 'C',
  'Art. 203, § 1º: conceito por **conteúdo + finalidade** (encerrar a fase). Interlocutória é residual (§ 2º).',
  lei=[('L13105:203', 'Ressalvadas as disposições expressas', 'extingue a execução.', 'CPC, art. 203, § 1º')],
  kw=['sentença', 'decisão interlocutória'])
I(P, 1, 'Horário dos atos',
  'Os atos processuais serão realizados em dias úteis, das 6 às 18 horas.', 'E',
  'Art. 212: das **6 às 20 horas**. Concluem-se depois das 20h os atos iniciados antes, se o adiamento prejudicar a diligência (§ 1º).',
  lei=[('L13105:212', 'Os atos processuais serão realizados em dias úteis', '20 (vinte) horas.', 'CPC, art. 212')],
  kw=['dias úteis', '6 às 20 horas'])
I(P, 1, 'Contagem em dias úteis',
  'Na contagem de prazo em dias, estabelecido por lei ou pelo juiz, computar-se-ão somente os dias úteis, regra que se aplica apenas aos prazos processuais.', 'C',
  'Art. 219 e parágrafo único: **dias úteis** só para **prazos processuais** (não para os de direito material).',
  lei=[('L13105:219', 'Na contagem de prazo em dias', 'somente os dias úteis.', 'CPC, art. 219'),
       ('L13105:219', 'O disposto neste artigo aplica-se somente aos prazos processuais.', None, 'CPC, art. 219, par. ún.')],
  kw=['dias úteis', 'prazos processuais'])
I(P, 1, 'Suspensão de fim de ano',
  'Suspende-se o curso do prazo processual nos dias compreendidos entre 20 de dezembro e 6 de janeiro, inclusive.', 'E',
  'Art. 220: de **20 de dezembro a 20 de janeiro**, inclusive.',
  lei=[('L13105:220', 'Suspende-se o curso do prazo processual', '20 de janeiro, inclusive.', 'CPC, art. 220')],
  kw=['recesso', '20 de dezembro', '20 de janeiro'])
I(P, 1, 'Prazo supletivo',
  'Inexistindo preceito legal ou prazo determinado pelo juiz, será de 5 dias o prazo para a prática de ato processual a cargo da parte.', 'C',
  'Art. 218, § 3º: **5 dias** é o prazo supletivo.',
  lei=[('L13105:218', 'Inexistindo preceito legal ou prazo determinado pelo juiz', 'a cargo da parte.', 'CPC, art. 218, § 3º')],
  kw=['prazo supletivo', '5 dias'])
I(P, 1, 'Contagem do prazo',
  'Os prazos são contados incluindo o dia do começo e excluindo o dia do vencimento.', 'E',
  'Art. 224: **exclui o dia do começo e inclui o do vencimento**.',
  lei=[('L13105:224', 'Salvo disposição em contrário, os prazos serão contados excluindo o dia do começo', 'dia do vencimento.', 'CPC, art. 224')],
  kw=['contagem', 'dies a quo'])
I(P, 1, 'Efeitos da citação',
  'A citação válida, quando ordenada por juízo incompetente, não induz litispendência nem constitui em mora o devedor.', 'E',
  'Art. 240: a citação válida, **ainda quando ordenada por juízo incompetente**, induz litispendência, torna litigiosa a coisa e constitui em mora o devedor.',
  lei=[('L13105:240', 'A citação válida, ainda quando ordenada por juízo incompetente', 'em mora o devedor', 'CPC, art. 240')],
  kw=['citação', 'litispendência', 'mora'])
I(P, 1, 'Interrupção da prescrição',
  'A interrupção da prescrição, operada pelo despacho que ordena a citação, ainda que proferido por juízo incompetente, retroagirá à data de propositura da ação.', 'C',
  'Art. 240, § 1º. Quem interrompe é o **despacho que ordena a citação**, com efeito **retroativo** à propositura.',
  lei=[('L13105:240', 'A interrupção da prescrição, operada pelo despacho', 'data de propositura da ação.', 'CPC, art. 240, § 1º')],
  kw=['interrupção da prescrição', 'retroação'])
I(P, 1, 'Citação eletrônica',
  'A citação será feita preferencialmente pelo correio, para qualquer comarca do país.', 'E',
  'Desde a Lei 14.195/2021, o art. 246 manda citar **preferencialmente por meio eletrônico**, em até 2 dias úteis da decisão que a determinar.',
  lei=[('L13105:246', 'A citação será feita preferencialmente por meio eletrônico', 'que a determinar', 'CPC, art. 246')],
  kw=['citação eletrônica', 'Lei 14.195/2021'])
I(P, 1, 'Citação com hora certa',
  'Quando, por 3 vezes, o oficial de justiça houver procurado o citando em seu domicílio sem o encontrar, deverá, havendo suspeita de ocultação, intimar pessoa da família ou vizinho de que voltará para efetuar a citação.', 'E',
  'Art. 252: bastam **2 vezes** + **suspeita de ocultação**.',
  lei=[('L13105:252', 'Quando, por 2 (duas) vezes', 'na hora que designar.', 'CPC, art. 252')],
  kw=['hora certa', 'ocultação'])
I(P, 1, 'Instrumentalidade das formas',
  'Quando a lei prescrever determinada forma, o juiz considerará válido o ato se, realizado de outro modo, lhe alcançar a finalidade.', 'C',
  'Art. 277: **instrumentalidade das formas** — sem prejuízo, não há nulidade.',
  lei=[('L13105:277', 'Quando a lei prescrever determinada forma', 'lhe alcançar a finalidade.', 'CPC, art. 277')],
  kw=['instrumentalidade', 'nulidade'])

# ---------------- PONTO 4 — RODADA 2
I(P, 2, 'Prazo em dobro de litisconsortes',
  'Os litisconsortes com diferentes procuradores, de escritórios de advocacia distintos, terão prazos contados em dobro, inclusive em processos em autos eletrônicos.', 'E',
  'Art. 229, § 2º: o prazo em dobro **não se aplica aos autos eletrônicos**.',
  exc=['Não se aplica a processos em autos eletrônicos (art. 229, § 2º)', 'Cessa se, havendo só 2 réus, apenas um oferecer defesa (art. 229, § 1º)'],
  lei=[('L13105:229', 'Não se aplica o disposto no caput aos processos em autos eletrônicos.', None, 'CPC, art. 229, § 2º')],
  kw=['prazo em dobro', 'autos eletrônicos'])
I(P, 2, 'Termo inicial na citação eletrônica',
  'Na citação por meio eletrônico, o prazo começa no quinto dia útil seguinte à confirmação do recebimento da citação.', 'C',
  'Art. 231, IX (Lei 14.195/2021).',
  lei=[('L13105:231', 'o quinto dia útil seguinte à confirmação', 'por meio eletrônico', 'CPC, art. 231, IX')],
  kw=['termo inicial', 'citação eletrônica'])
I(P, 2, 'Citação nas ações de estado',
  'Nas ações de estado, admite-se a citação por meio eletrônico, desde que confirmada pelo réu.', 'E',
  'Art. 247, I: nas **ações de estado** não se cita por meio eletrônico nem pelo correio — a citação é **pessoal**, por oficial (art. 695, § 3º).',
  exc=['Também não cabem citação eletrônica/correio: incapaz, pessoa de direito público, local não atendido pelo correio e quando o autor justificadamente requerer outra forma (art. 247, II a V)'],
  lei=[('L13105:247', 'I - nas ações de estado', None, 'CPC, art. 247, I')],
  kw=['ações de estado', 'citação pessoal'])
I(P, 2, 'Citação por edital — diligências',
  'Segundo o STJ, a expedição de ofícios a cadastros de órgãos públicos e a concessionárias de serviços públicos é requisito obrigatório de validade da citação por edital.', 'E',
  'Tema 1.338/STJ: **não é requisito obrigatório**; em regra basta a frustração da busca nos endereços dos autos e nos **sistemas informatizados** do juízo, com decisão motivada.',
  lei=[('L13105:256', 'O réu será considerado em local ignorado', 'concessionárias de serviços públicos.', 'CPC, art. 256, § 3º')],
  juris=[J['T1338']],
  kw=['citação por edital', 'Tema 1.338'])
I(P, 2, 'Momento de alegar nulidade',
  'A nulidade dos atos deve ser alegada na primeira oportunidade em que couber à parte falar nos autos, sob pena de preclusão, o que não se aplica às nulidades que o juiz deva decretar de ofício.', 'C',
  'Art. 278 e parágrafo único.',
  lei=[('L13105:278', 'A nulidade dos atos deve ser alegada', 'sob pena de preclusão.', 'CPC, art. 278')],
  kw=['nulidade', 'preclusão'])
I(P, 2, 'Falta de intimação do MP',
  'A falta de intimação do Ministério Público, quando obrigatória sua intervenção, gera nulidade automática do processo, independentemente de manifestação do órgão sobre a existência de prejuízo.', 'E',
  'Art. 279, § 2º: a nulidade **só pode ser decretada após a intimação do MP**, que dirá se houve ou não **prejuízo**.',
  lei=[('L13105:279', 'A nulidade só pode ser decretada após a intimação do Ministério Público', 'inexistência de prejuízo.', 'CPC, art. 279, § 2º')],
  kw=['MP', 'prejuízo', 'nulidade'])
I(P, 2, 'Preclusão temporal',
  'Decorrido o prazo, extingue-se o direito de praticar ou de emendar o ato processual, independentemente de declaração judicial, ficando assegurado à parte provar que não o realizou por justa causa.', 'C',
  'Art. 223: **preclusão temporal**, com ressalva da **justa causa**.',
  lei=[('L13105:223', 'Decorrido o prazo, extingue-se o direito', 'por justa causa.', 'CPC, art. 223')],
  kw=['preclusão temporal', 'justa causa'])
I(P, 2, 'Controle judicial do negócio processual',
  'Em respeito à autonomia da vontade, o juiz não pode recusar aplicação a convenção processual celebrada por partes capazes.', 'E',
  'Art. 190, par. ún.: o juiz controla a validade **de ofício ou a requerimento** e recusa aplicação em caso de nulidade, **contrato de adesão** abusivo ou **vulnerabilidade** manifesta.',
  lei=[('L13105:190', 'De ofício ou a requerimento, o juiz controlará a validade', 'situação de vulnerabilidade.', 'CPC, art. 190, par. ún.')],
  kw=['negócio processual', 'vulnerabilidade', 'contrato de adesão'])
I(P, 2, 'Demora na citação',
  'Proposta a ação no prazo, a demora na citação por motivos inerentes ao mecanismo da Justiça não justifica o acolhimento da prescrição.', 'C',
  'Súmula 106/STJ, em sintonia com o art. 240, § 3º: a parte não é prejudicada pela demora imputável **exclusivamente ao serviço judiciário**.',
  lei=[('L13105:240', 'A parte não será prejudicada pela demora', 'serviço judiciário.', 'CPC, art. 240, § 3º')],
  juris=[J['S106']],
  kw=['prescrição', 'demora na citação'])
I(P, 2, 'Valor da causa — alimentos',
  'Na ação de alimentos, o valor da causa será a soma de 6 prestações mensais pedidas pelo autor.', 'E',
  'Art. 292, III: soma de **12 prestações** mensais.',
  lei=[('L13105:292', 'na ação de alimentos, a soma de 12 (doze) prestações mensais', None, 'CPC, art. 292, III')],
  kw=['valor da causa', '12 prestações'])
