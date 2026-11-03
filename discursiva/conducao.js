/* Condução "Entender o caso" do Treino de Discursiva — pedido do titular de 03/11/2026 (D-015).
   Antes de escrever, o aluno percorre 5 etapas: a peça, a competência e o endereçamento, o crime, a lógica dos
   fundamentos e os pedidos. Cada etapa tem perguntas com o porquê de cada alternativa e os artigos, cujo texto
   OFICIAL vem de artigos.js (gerado do Planalto). Referências: artigo, artigo:§N, artigo:inciso romano, artigo:pu (parágrafo único).
   Texto autoral; carrega depois das peças. Op = [alternativa, 1 se certa, por quê]. */

/* O método que vale para TODA peça: é ele que o aluno deve levar para a prova. */
const METODO = {
  passos: [
    ['Em que momento estamos?', 'Há inquérito instaurado? Há alguém preso em flagrante? A investigação está começando, em curso ou terminando? Isso já elimina metade das peças.'],
    ['O que o caso quer obter?', 'Leia o comando e os fatos e pergunte: o problema é a PESSOA (solta e perigosa), a PROVA (está escondida), os BENS (vão sumir ou estragar), a VÍTIMA (corre risco) ou o PRÓPRIO PROCEDIMENTO (abrir, concluir)?'],
    ['Quem pode dar isso?', 'Se a medida restringe direito fundamental sob reserva de jurisdição, só o JUIZ dá: a peça é uma REPRESENTAÇÃO. Se o próprio delegado decide, a peça é ato dele: portaria, despacho ou relatório.'],
    ['Qual é o nome técnico e a lei?', 'Dê o nome exato da medida e a lei que a prevê. A banca dá pontos ao nome certo da peça e ao fundamento legal no preâmbulo.'],
  ],
  mapa: [
    ['Pessoa solta e perigosa; crime com pena máxima acima de 4 anos', 'Prisão preventiva (CPP, arts. 311 a 313)'],
    ['Investigação travada; suspeito sem residência ou identidade; crime do rol', 'Prisão temporária (Lei 7.960/89)'],
    ['Prisão desproporcional, mas há risco a conter', 'Cautelares diversas (CPP, art. 319)'],
    ['Preso em flagrante e auto lavrado', 'Despacho de conclusão do APF + representação pela conversão'],
    ['Prova dentro de uma casa', 'Busca e apreensão domiciliar (CPP, art. 240)'],
    ['Prova em ligações telefônicas', 'Interceptação (Lei 9.296, arts. 1º a 5º)'],
    ['Prova em conversas presenciais, num local', 'Captação ambiental (Lei 9.296, art. 8º-A)'],
    ['Prova no dinheiro (contas, renda)', 'Quebra de sigilo bancário e fiscal (LC 105)'],
    ['Prova no DNA ou na digital', 'Identificação criminal com perfil genético (Lei 12.037)'],
    ['Grupo fechado, só alguém de dentro descobre', 'Infiltração de agentes (Lei 12.850, art. 10)'],
    ['Bens comprados com dinheiro do crime', 'Sequestro (CPP, arts. 125 a 132)'],
    ['Bens já apreendidos que estragam ou perdem valor', 'Alienação antecipada (CPP, art. 144-A)'],
    ['Mulher em violência doméstica', 'Medidas protetivas (Lei 11.340, art. 22) + preventiva, se preciso'],
    ['Vítima em poder dos autores, crime em curso', 'Meios técnicos de localização (CPP, art. 13-B)'],
    ['Adolescente apreendido em ato grave', 'Internação provisória (ECA, art. 108)'],
    ['Notícia de crime e nada instaurado', 'Portaria de instauração do inquérito'],
    ['Diligências concluídas', 'Relatório final do inquérito'],
  ],
};

const CONDUCAO = {
  /* ------------------------------------------------------------ Ilhéus: o caso-base */
  preventiva: {
    pistas: ['armados com revólver', 'reconhecido pela vítima em procedimento formal', 'ameaçando-as de morte', 'condenação definitiva anterior', 'não foi localizado no endereço informado', 'Comarca de Ilhéus/BA', 'IP nº 123/2026'],
    etapas: [
      { t: 'Qual é a peça?', qs: [
          { p: 'Pelo método: o IP já existe, ninguém está preso, e o problema é o que o investigado faz SOLTO (ameaça testemunhas, sumiu do endereço). O que você quer obter?', op: [
            ['A prisão do investigado, por representação ao juiz', 1, 'Isso. O problema é a pessoa, e prender exige ordem judicial (CF, art. 5º, LXI): o delegado REPRESENTA.'],
            ['Uma busca e apreensão na casa de Marcos', 0, 'Não há prova a buscar: a autoria já está indicada pelo reconhecimento e pelas imagens. O risco está na liberdade dele.'],
            ['A instauração do inquérito por portaria', 0, 'O IP nº 123/2026 já está instaurado. Portaria é para quando nada foi aberto.'],
          ] },
          { p: 'Qual prisão?', op: [
            ['Preventiva', 1, 'Certo. Há prova do crime, indício de autoria e perigo concreto na liberdade (art. 312), e o crime tem pena máxima acima de 4 anos (art. 313, I).'],
            ['Temporária', 0, 'A temporária serve para quando a prisão é IMPRESCINDÍVEL ÀS INVESTIGAÇÕES (Lei 7.960, art. 1º, I). Aqui a autoria já está esclarecida; o perigo é para a instrução e para a aplicação da lei penal, que são finalidades da preventiva.'],
            ['Cautelar diversa (art. 319)', 0, 'Quem ameaça de morte testemunhas e some do endereço não é contido por comparecimento em juízo ou monitoração: a preventiva é a única adequada (art. 282, § 6º).'],
          ] },
        ],
        logica: 'A preventiva responde ao PERIGO DA LIBERDADE. As três pistas do enunciado são as três finalidades que você vai usar: ameaça às testemunhas (conveniência da instrução), paradeiro incerto (aplicação da lei penal) e reincidência com arma de fogo (ordem pública). Quem pede é o delegado, por representação; o juiz não decreta de ofício (art. 311; STJ, Súmula 676).',
        arts: ['CPP:311', 'CPP:312', 'CF:5:LXI', 'SUM-STJ-676'] },
      { t: 'Competência e endereçamento', qs: [
          { p: 'Roubo em Ilhéus, sem interesse da União. A quem você endereça?', op: [
            ['Ao Juiz de Direito da Vara Criminal da Comarca de Ilhéus/BA', 1, 'Certo: justiça estadual, pelo lugar da infração (CPP, art. 70). Use lacuna para o número da vara.'],
            ['Ao Juiz Federal da Subseção de Ilhéus', 0, 'Não há bem, serviço ou interesse da União (CF, art. 109, IV): a competência é da Justiça Estadual.'],
            ['Ao Juiz Presidente do Tribunal do Júri', 0, 'O Júri julga crimes dolosos contra a VIDA (CF, art. 5º, XXXVIII, "d"). Roubo é crime contra o patrimônio.'],
            ['Ao Promotor de Justiça da Comarca', 0, 'Representação vai ao JUIZ; o MP é ouvido depois (art. 282, § 3º, e pedido de oitiva).'],
          ] },
        ],
        logica: 'Três perguntas, nessa ordem: (1) Justiça Federal ou Estadual? (CF, art. 109); (2) há juízo especializado? (Júri, violência doméstica, infância, tóxicos); (3) qual comarca? (lugar da consumação, CPP, art. 70). Onde houver juiz das garantias, é ele o competente na fase do inquérito (art. 3º-B). Nunca invente número de vara nem nome de juiz.',
        arts: ['CPP:70', 'CF:109:IV', 'CF:5:XXXVIII', 'CPP:3-B'] },
      { t: 'O crime: tipificação completa', qs: [
          { p: 'Marcos e um comparsa, armados com revólver, tomaram celular e carteira. Qual a tipificação do fato principal?', op: [
            ['Roubo majorado: art. 157, § 2º, II (concurso), e § 2º-A, I (arma de fogo)', 1, 'Certo. Duas majorantes: o concurso de pessoas (§ 2º, II) e o emprego de arma de fogo (§ 2º-A, I).'],
            ['Furto qualificado pelo concurso de agentes (art. 155, § 4º, IV)', 0, 'Houve grave ameaça com arma: é roubo. E a majorante do roubo não se aplica ao furto (STJ, Súmula 442).'],
            ['Roubo simples (art. 157, caput)', 0, 'Faltam as majorantes: a banca pontua cada uma.'],
          ] },
          { p: 'E as ameaças de morte às testemunhas do IP, para que não falassem com a polícia?', op: [
            ['Coação no curso do processo (art. 344 do CP), em concurso material com o roubo', 1, 'Certo. Grave ameaça contra quem é chamado a intervir em processo POLICIAL, para favorecer interesse próprio: art. 344. São condutas autônomas: concurso material (art. 69).'],
            ['Só ameaça (art. 147), absorvida pelo roubo', 0, 'A ameaça veio depois do roubo e teve outra finalidade (atrapalhar a investigação): é coação no curso do processo, crime autônomo.'],
            ['Nada: é só um dado do periculum', 0, 'É também periculum, mas tipificar completo dá pontos: o art. 344 alcança o processo policial.'],
          ] },
        ],
        logica: 'Faça o checklist da tipificação completa: consumado ou tentado? (art. 14); qualificadoras e majorantes (aqui, duas); vários agentes (concurso de pessoas, art. 29); vários crimes (concurso material, art. 69). Confira no texto oficial abaixo: a pena-base do roubo foi alterada em 2026.',
        arts: ['CP:157', 'CP:344', 'CP:29', 'CP:69', 'SUM-STJ-442', 'SUM-STJ-443'] },
      { t: 'A lógica dos fundamentos', qs: [
          { p: 'Em que ORDEM você constrói a fundamentação da preventiva?', op: [
            ['Cabimento (313) → fumus comissi delicti (312) → periculum libertatis (312) → insuficiência das cautelares (282, § 6º)', 1, 'Certo: primeiro mostra que a prisão é admitida, depois os dois requisitos do art. 312, e por fim que nada menos grave resolve.'],
            ['Periculum → pedidos → fumus', 0, 'Sem cabimento e sem fumus, o periculum não sustenta a prisão.'],
          ] },
          { p: 'Qual cuidado o Pacote Anticrime exige no periculum?', op: [
            ['Fatos novos ou contemporâneos, apontados concretamente (art. 312, § 2º; art. 315)', 1, 'Certo. Gravidade abstrata do crime não basta; aponte os fatos atuais: as ameaças e o paradeiro incerto.'],
            ['Basta dizer que o roubo é crime grave', 0, 'Fundamentação genérica é nula (art. 315, § 2º). Use os fatos do caso.'],
          ] },
        ],
        logica: 'Cada fundamento responde a uma pergunta do juiz: PODE prender? (art. 313) · HÁ crime e autor? (fumus) · POR QUE prender agora? (periculum, com fatos contemporâneos) · NÃO HÁ algo menos grave? (art. 282, § 6º). O texto oficial do art. 312 traz o § 3º novo, com critérios da periculosidade (modus operandi, reiteração).',
        arts: ['CPP:313', 'CPP:312', 'CPP:282', 'CPP:315'] },
      { t: 'Os pedidos', qs: [
          { p: 'Qual pedido NÃO pode faltar, além da decretação da preventiva?', op: [
            ['A expedição do mandado e o registro no BNMP (art. 289-A)', 1, 'Certo. Sem mandado não se cumpre a prisão; o registro no banco nacional é exigência legal.'],
            ['A condenação de Marcos', 0, 'Delegado não pede condenação: isso é do MP na denúncia.'],
            ['A fixação de fiança', 0, 'Fiança é o contrário do que você quer, e o roubo majorado está fora da fiança policial (art. 322).'],
          ] },
        ],
        logica: 'Pedidos numerados: o principal (decretação), os acessórios (mandado e BNMP), a oitiva do MP, o sigilo e a urgência. A banca pontua CADA pleito, então o que não está pedido não conta.',
        arts: ['CPP:289-A', 'CPP:282:§3'] },
    ],
  },
  /* ------------------------------------------------------------ temporária */
  temporaria: {
    pistas: ['morto com disparos de arma de fogo', 'não tem residência fixa', 'se recusou a fornecer dados de identificação', 'imprescindíveis para avançar', 'pretende deixar o Estado', 'Feira de Santana/BA'],
    etapas: [
      { t: 'Qual é a peça?', qs: [
          { p: 'A investigação depende de ouvir Paulo e de reconhecê-lo, e ele não tem residência nem se identifica. Que prisão serve à INVESTIGAÇÃO?', op: [
            ['Prisão temporária (Lei 7.960/89)', 1, 'Certo. É a prisão imprescindível às investigações do inquérito (art. 1º, I), somada à falta de residência e de identificação (inciso II), em crime do rol (inciso III, "a": homicídio doloso).'],
            ['Prisão preventiva', 0, 'Poderia ser cogitada, mas o enunciado aponta a necessidade PARA A INVESTIGAÇÃO (oitiva e reconhecimento). Essa é a marca da temporária, que só existe no inquérito.'],
            ['Condução coercitiva para interrogatório', 0, 'O STF vedou a condução coercitiva para interrogatório (ADPFs 395 e 444). E o reconhecimento exige a pessoa disponível por mais tempo.'],
          ] },
        ],
        logica: 'A temporária é a prisão da FASE DE INVESTIGAÇÃO. O STF (ADIs 3360 e 4109) fixou os requisitos cumulativos: imprescindível às investigações (inciso I) OU falta de residência/identidade (inciso II), sempre com fundadas razões de autoria em crime do rol (inciso III), além de fatos contemporâneos e de insuficiência das cautelares.',
        arts: ['L7960:1', 'L7960:2', 'L8072:2'] },
      { t: 'Competência e endereçamento', qs: [
          { p: 'Homicídio doloso em Feira de Santana. A quem vai a representação?', op: [
            ['Ao Juízo da Vara do Júri (ou Criminal) da Comarca de Feira de Santana/BA', 1, 'Certo: crime doloso contra a vida, justiça estadual, lugar da infração.'],
            ['Ao Juiz da Vara Criminal comum, mesmo havendo Vara do Júri', 0, 'Onde houver Vara do Júri, ela concentra os crimes dolosos contra a vida, inclusive as cautelares do inquérito.'],
          ] },
        ],
        logica: 'Crime doloso contra a vida = Júri (CF, art. 5º, XXXVIII, "d"). Na fase do inquérito, a medida vai ao juízo com competência para o júri na comarca (ou ao juiz das garantias, onde implantado).',
        arts: ['CF:5:XXXVIII', 'CPP:70'] },
      { t: 'O crime: tipificação completa', qs: [
          { p: 'O enunciado fala só em "morto com disparos". A tipificação e o prazo da temporária:', op: [
            ['Homicídio (art. 121); se não houver qualificadora, a temporária é de 5 + 5 dias', 1, 'Certo. Sem qualificadora descrita, o homicídio simples só é hediondo se praticado em atividade típica de grupo de extermínio. Peça 30 dias apenas se houver base para a hediondez, e 5 dias como alternativa.'],
            ['Homicídio qualificado, temporária de 30 dias', 0, 'Não invente qualificadora: o enunciado não traz motivo, meio nem recurso. Arrisque a hediondez só com dado do caso.'],
          ] },
        ],
        logica: 'O prazo depende da natureza do crime: 5 dias, prorrogáveis por igual período (Lei 7.960, art. 2º), ou 30 + 30 nos hediondos e equiparados (Lei 8.072, art. 2º, § 4º). Por isso a tipificação vem antes do pedido.',
        arts: ['CP:121', 'L8072:1'] },
      { t: 'A lógica dos fundamentos', qs: [
          { p: 'Qual combinação de incisos do art. 1º da Lei 7.960 você demonstra?', op: [
            ['Inciso III (homicídio doloso) + inciso I (imprescindível) e/ou inciso II (sem residência ou identidade)', 1, 'Certo: o inciso III é sempre necessário; com ele, o I ou o II (STF, ADI 4109).'],
            ['Só o inciso II: basta não ter residência fixa', 0, 'Sozinho, o inciso II não basta: falta a fundada razão de autoria em crime do rol (inciso III).'],
          ] },
        ],
        logica: 'Monte assim: o crime está no rol (III) → há fundadas razões de autoria (testemunhas + identificação de "Neguinho") → a prisão é imprescindível (I: oitiva e reconhecimento) e ele não tem residência nem identificação (II) → há risco atual (vai deixar o Estado).',
        arts: ['L7960:1'] },
      { t: 'Os pedidos', qs: [
          { p: 'Quem deve ser ouvido antes da decisão sobre a temporária representada pelo delegado?', op: [
            ['O Ministério Público (Lei 7.960, art. 2º, § 1º)', 1, 'Certo: na representação da autoridade policial, o juiz ouve o MP antes de decidir.'],
            ['O investigado, em contraditório prévio', 0, 'O contraditório prévio frustraria a medida; não é exigido.'],
          ] },
        ],
        logica: 'Pedidos: a decretação com o prazo (30 ou 5 dias), o mandado e o BNMP, a oitiva do MP, sigilo e urgência.',
        arts: ['L7960:2'] },
    ],
  },
  /* ------------------------------------------------------------ busca */
  busca: {
    pistas: ['guarda e vende cocaína na casa', 'Rua das Flores, nº 45, Bairro Centro', 'anotações da contabilidade do tráfico', 'aparelho celular usado nas negociações', 'Vitória da Conquista/BA'],
    etapas: [
      { t: 'Qual é a peça?', qs: [
          { p: 'O problema é a PROVA: droga, anotações e celular dentro de uma CASA. O que você pede?', op: [
            ['Mandado de busca e apreensão domiciliar, com acesso aos dados do celular', 1, 'Certo. A casa é asilo inviolável e só se entra de dia com ordem judicial (CF, art. 5º, XI); o conteúdo do celular também depende de ordem.'],
            ['Interceptação telefônica', 0, 'A prova está guardada na casa e no aparelho, não em ligações futuras.'],
            ['Prisão preventiva de Carla', 0, 'O enunciado não traz perigo da liberdade; traz prova a apreender.'],
          ] },
        ],
        logica: 'Busca domiciliar: fundadas razões (art. 240, § 1º) + o mandado deve indicar a CASA, o MOTIVO e os FINS (art. 243). Cuidado: o tráfico na modalidade "guardar" é crime permanente, o que permitiria flagrante, mas a entrada sem mandado exige fundadas razões prévias (STF, Tema 280). Na prova, a peça é a representação.',
        arts: ['CF:5:XI', 'CPP:240', 'CPP:243'] },
      { t: 'Competência e endereçamento', qs: [
          { p: 'Tráfico interno em Vitória da Conquista:', op: [
            ['Vara Criminal (ou de Tóxicos, se houver) da Comarca de Vitória da Conquista/BA', 1, 'Certo: tráfico sem transnacionalidade é da Justiça Estadual (STF, Súmula 522).'],
            ['Justiça Federal, porque droga é tema de tratado internacional', 0, 'Só o tráfico com o exterior atrai a Justiça Federal (Súmula 522; CF, art. 109, V).'],
          ] },
        ],
        logica: 'Federal só com transnacionalidade. Se a comarca tem vara especializada em tóxicos, endereça a ela.',
        arts: ['SUM-STF-522', 'CF:109:V'] },
      { t: 'O crime: tipificação completa', qs: [
          { p: 'Carla "guarda e vende" cocaína em casa:', op: [
            ['Tráfico de drogas (Lei 11.343, art. 33, caput): "ter em depósito", "guardar" e "vender"', 1, 'Certo: tipo misto alternativo; vários verbos no mesmo contexto são um só crime. "Guardar" e "ter em depósito" são permanentes.'],
            ['Posse para consumo pessoal (art. 28)', 0, 'Há venda e contabilidade: destinação comercial.'],
          ] },
        ],
        logica: 'Use os verbos do art. 33 que o enunciado traz. Saber que é permanente explica por que a busca pode encontrar o crime em curso.',
        arts: ['L11343:33'] },
      { t: 'A lógica dos fundamentos', qs: [
          { p: 'O que o juiz precisa ver para expedir o mandado?', op: [
            ['Fundadas razões ligadas às finalidades do art. 240, § 1º, e o endereço exato', 1, 'Certo: alíneas "b" (coisas obtidas por meios criminosos), "e" (instrumentos), "h" (elementos de convicção), entre outras, com o imóvel individualizado.'],
            ['Só a denúncia anônima', 0, 'Denúncia anônima isolada não basta; aqui há relatórios, fotos e depoimento.'],
          ] },
        ],
        logica: 'Fundadas razões → finalidade (alíneas do art. 240, § 1º) → individualização do local (art. 243) → cumprimento de dia (art. 245) → dados do celular (ordem expressa).',
        arts: ['CPP:240', 'CPP:245'] },
      { t: 'Os pedidos', qs: [
          { p: 'Qual pedido acessório costuma ser esquecido nessa peça?', op: [
            ['A autorização de acesso e extração dos dados do celular apreendido', 1, 'Certo: apreender o aparelho não autoriza abrir o conteúdo; peça expressamente.'],
            ['A prisão temporária de Carla', 0, 'Não há base no enunciado.'],
          ] },
        ],
        logica: 'Mandado com casa, motivo e fins; acesso aos dados; oitiva do MP; sigilo e urgência.',
        arts: ['CPP:243'] },
    ],
  },
  /* ------------------------------------------------------------ interceptação */
  interceptacao: {
    pistas: ['combinam entregas por ligações telefônicas', '(71) 9XXXX-1111 e (71) 9XXXX-2222', 'Buscas anteriores não alcançaram o fornecedor', 'mudam de ponto constantemente', 'associação para o tráfico'],
    etapas: [
      { t: 'Qual é a peça?', qs: [
          { p: 'A prova está nas LIGAÇÕES que eles ainda vão fazer, e os outros meios falharam. A peça:', op: [
            ['Interceptação das comunicações telefônicas (Lei 9.296)', 1, 'Certo: prova futura, em comunicação telefônica, com outros meios esgotados (art. 2º, II).'],
            ['Quebra do sigilo de dados (extratos) apenas', 0, 'Extratos mostram com quem falaram, não o que combinaram. Peça-os como acessório.'],
            ['Captação ambiental', 0, 'Eles falam ao TELEFONE; captação ambiental é para conversa presencial num local.'],
          ] },
        ],
        logica: 'Interceptação = comunicação em curso, por telefone ou telemática, autorizada pelo juiz, com três requisitos negativos do art. 2º: há indícios de autoria, a prova não pode ser feita por outro meio e o crime é punido com reclusão.',
        arts: ['CF:5:XII', 'L9296:1', 'L9296:2'] },
      { t: 'Competência e endereçamento', qs: [
          { p: 'Quem é o juiz da interceptação?', op: [
            ['O juiz competente para a ação principal: Vara Criminal (ou de Tóxicos) de Salvador', 1, 'Certo: art. 1º da Lei 9.296.'],
            ['Qualquer juiz de plantão, à escolha do delegado', 0, 'É o juiz da futura ação penal; o plantão só em urgência.'],
          ] },
        ],
        logica: 'A Lei 9.296 amarra a medida ao juiz da ação principal, sob segredo de justiça.',
        arts: ['L9296:1'] },
      { t: 'O crime: tipificação completa', qs: [
          { p: 'Diego, Lucas e Ana, de forma estável, combinam entregas:', op: [
            ['Associação para o tráfico (Lei 11.343, art. 35) e tráfico (art. 33)', 1, 'Certo: 2 ou mais pessoas, com estabilidade, para o tráfico; reclusão, o que atende ao art. 2º, III, da Lei 9.296.'],
            ['Associação criminosa (CP, art. 288)', 0, 'Para o tráfico, há tipo especial: o art. 35 da Lei de Drogas.'],
          ] },
        ],
        logica: 'A pena de reclusão é requisito da interceptação: tipifique para mostrar que ela cabe.',
        arts: ['L11343:35', 'L11343:33'] },
      { t: 'A lógica dos fundamentos', qs: [
          { p: 'O que o art. 4º exige do pedido?', op: [
            ['Demonstrar a necessidade e indicar os meios a empregar', 1, 'Certo: e o prazo é de 15 dias, renovável se comprovada a indispensabilidade (art. 5º).'],
            ['Apresentar a transcrição de conversas anteriores', 0, 'Não há conversas ainda: é o que se quer obter.'],
          ] },
        ],
        logica: 'Requisitos do art. 2º → necessidade e meios (art. 4º) → prazo de 15 dias renovável (art. 5º) → condução pela polícia com ciência ao MP (art. 6º).',
        arts: ['L9296:4', 'L9296:5', 'L9296:6'] },
      { t: 'Os pedidos', qs: [
          { p: 'Qual pedido completa a interceptação?', op: [
            ['Ofícios às operadoras com dados cadastrais, extratos e ERBs, em autos apartados e sigilosos', 1, 'Certo: autos apartados e segredo (arts. 1º e 8º).'],
            ['Intimação dos investigados', 0, 'Arruinaria a medida.'],
          ] },
        ],
        logica: 'Os terminais exatos, o prazo, os ofícios, os autos apartados, a oitiva do MP.',
        arts: ['L9296:8'] },
    ],
  },
  /* ------------------------------------------------------------ Maria da Penha */
  'maria-penha': {
    pistas: ['ex-companheiro', 'agrediu com socos (laudo de lesão corporal confirma)', '"vai acabar com ela"', 'pediu medidas protetivas', 'já descumpriu medida protetiva anterior', 'rondando a casa da vítima', 'Juazeiro/BA'],
    etapas: [
      { t: 'Qual é a peça?', qs: [
          { p: 'A VÍTIMA corre risco, pediu protetivas, e o agressor já descumpriu medida antes. A peça:', op: [
            ['Encaminhamento do pedido de medidas protetivas + representação pela preventiva', 1, 'Certo. As protetivas vêm do pedido da ofendida, que o delegado remete em 48 h (art. 12, III). O descumprimento anterior e a ronda mostram que só a prisão garante a execução delas (CPP, art. 313, III).'],
            ['Só o despacho de afastamento do lar pelo delegado (art. 12-C)', 0, 'O 12-C, II, só vale se o município NÃO for sede de comarca. Juazeiro é sede, e o caso pede mais que o afastamento.'],
            ['Representação por prisão temporária', 0, 'A finalidade aqui é proteger a vítima e garantir as protetivas: é a preventiva.'],
          ] },
        ],
        logica: 'Na violência doméstica, a peça costuma ser dupla: protetivas (Lei 11.340, art. 22) e preventiva (art. 20; CPP, art. 313, III). A preventiva aqui tem fundamento próprio: garantir a execução das protetivas.',
        arts: ['L11340:12', 'L11340:22', 'CPP:313:III'] },
      { t: 'Competência e endereçamento', qs: [
          { p: 'Onde tramita?', op: [
            ['Juizado (ou Vara) de Violência Doméstica e Familiar contra a Mulher da Comarca de Juazeiro/BA', 1, 'Certo: art. 14 da Lei 11.340. Onde não houver, a vara criminal acumula (art. 33).'],
            ['Juizado Especial Criminal', 0, 'A Lei 9.099 não se aplica à violência doméstica (art. 41 da Lei 11.340; STJ, Súmula 536).'],
          ] },
        ],
        logica: 'Juízo especializado primeiro: Violência Doméstica. Sem ele, vara criminal com preferência.',
        arts: ['L11340:14', 'L11340:41', 'SUM-STJ-536'] },
      { t: 'O crime: tipificação completa', qs: [
          { p: 'Socos na ex-companheira + mensagens "vai acabar com ela" + descumprimento anterior:', op: [
            ['Lesão corporal contra a mulher (art. 129, § 13), ameaça (art. 147, com o § 1º) e descumprimento de protetiva (Lei 11.340, art. 24-A) no fato anterior', 1, 'Certo. Relação íntima de afeto, mesmo sem coabitação (art. 5º, III; STJ, Súmula 600). Confira as penas no texto oficial, alteradas pela Lei 14.994/2024.'],
            ['Lesão corporal leve no JECrim (art. 129, caput)', 0, 'Na violência doméstica contra a mulher há forma própria e a ação é pública incondicionada (STJ, Súmula 542).'],
          ] },
        ],
        logica: 'Tipifique cada conduta e diga a forma de violência (art. 7º: física e psicológica). A ação penal na lesão é incondicionada (Súmula 542).',
        arts: ['CP:129:§13', 'CP:147', 'L11340:24-A', 'L11340:5', 'L11340:7', 'SUM-STJ-600', 'SUM-STJ-542'] },
      { t: 'A lógica dos fundamentos', qs: [
          { p: 'Qual a ponte entre as protetivas e a preventiva?', op: [
            ['O art. 313, III, do CPP: a preventiva cabe para garantir a execução das medidas protetivas', 1, 'Certo: independe da pena máxima do crime. E o descumprimento anterior mostra que medida sozinha não basta.'],
            ['O art. 313, I: pena máxima acima de 4 anos', 0, 'Lesão e ameaça podem não chegar a isso; o fundamento próprio é o inciso III.'],
          ] },
        ],
        logica: 'Violência doméstica configurada → protetivas cabíveis (art. 22) → risco concreto (ronda, ameaça, descumprimento) → preventiva para garantir as protetivas (art. 20; CPP, art. 313, III) → monitoração eletrônica como alternativa ou cumulação.',
        arts: ['L11340:20', 'L11340:22', 'CPP:313:III'] },
      { t: 'Os pedidos', qs: [
          { p: 'Qual medida protetiva o descumprimento anterior torna prioritária?', op: [
            ['A monitoração eletrônica do agressor (art. 22, com o § 6º)', 1, 'Certo: confira no texto oficial o regime da monitoração prioritária.'],
            ['A suspensão da posse de arma, só', 0, 'Pode ser pedida, mas o enunciado aponta o descumprimento e a ronda.'],
          ] },
        ],
        logica: 'Protetivas específicas (afastamento, proibição de aproximação e contato com distância, monitoração), preventiva com mandado, intimações (art. 21), ciência ao MP, sigilo e urgência.',
        arts: ['L11340:22', 'L11340:21'] },
    ],
  },
  /* ------------------------------------------------------------ sequestro */
  sequestro: {
    pistas: ['valores do tráfico foram usados para comprar', 'apartamento na Av. Oceânica, nº 900', 'caminhonete placa ABC-1D23', 'sem renda lícita compatível', 'anunciou os bens para venda'],
    etapas: [
      { t: 'Qual é a peça?', qs: [
          { p: 'O problema são os BENS comprados com dinheiro do crime, que ele quer vender. A peça:', op: [
            ['Sequestro de bens (medida assecuratória)', 1, 'Certo: bens adquiridos com os proventos do crime (CPP, arts. 125 e 132), com indícios veementes da origem ilícita (art. 126).'],
            ['Arresto', 0, 'Arresto e hipoteca legal recaem sobre bens LÍCITOS, para garantir a reparação. Bem comprado com dinheiro do crime é sequestrado.'],
            ['Busca e apreensão', 0, 'Não se quer achar o bem, e sim torná-lo indisponível.'],
          ] },
        ],
        logica: 'Medidas assecuratórias: sequestro (bem de origem ilícita), arresto e hipoteca legal (bem lícito, para a reparação), alienação antecipada (bem que estraga). A pista "anunciou para venda" é o periculum.',
        arts: ['CPP:125', 'CPP:126', 'CPP:132'] },
      { t: 'Competência e endereçamento', qs: [
          { p: 'Lavagem de dinheiro do tráfico, em Salvador:', op: [
            ['Vara Criminal de Salvador/BA (especializada, se houver)', 1, 'Certo: sem bens ou interesse da União e sem antecedente federal, a lavagem é da Justiça Estadual (Lei 9.613, art. 2º, III).'],
            ['Justiça Federal, por ser lavagem', 0, 'Lavagem não é federal por natureza: depende do art. 2º, III, da Lei 9.613.'],
          ] },
        ],
        logica: 'Lavagem segue a regra do art. 2º, III, da Lei 9.613: federal só nas hipóteses ali previstas.',
        arts: ['L9613:2'] },
      { t: 'O crime: tipificação completa', qs: [
          { p: 'Comprar bens em nome próprio com dinheiro do tráfico, sem renda lícita:', op: [
            ['Lavagem de dinheiro (Lei 9.613, art. 1º), tendo o tráfico como infração antecedente', 1, 'Certo: converter em ativos lícitos para dissimular a origem.'],
            ['Receptação (art. 180)', 0, 'Ele não recebeu coisa produto de crime alheio; dissimulou o próprio proveito.'],
          ] },
        ],
        logica: 'Na lavagem, aponte a infração antecedente e a conduta de ocultar ou dissimular.',
        arts: ['L9613:1'] },
      { t: 'A lógica dos fundamentos', qs: [
          { p: 'Qual o padrão de prova para o sequestro?', op: [
            ['Indícios VEEMENTES da proveniência ilícita dos bens (art. 126)', 1, 'Certo: mais que meros indícios; use o COAF e a incompatibilidade de renda.'],
            ['Prova plena da lavagem', 0, 'Prova plena é para condenar; a cautelar exige indícios veementes.'],
          ] },
        ],
        logica: 'Indícios veementes (art. 126) → bens individualizados → urgência (venda anunciada) → legitimidade do delegado antes da denúncia (art. 127).',
        arts: ['CPP:126', 'CPP:127', 'L9613:4'] },
      { t: 'Os pedidos', qs: [
          { p: 'Como se torna efetivo o sequestro do imóvel?', op: [
            ['Pela inscrição no Registro de Imóveis (art. 128)', 1, 'Certo; no veículo, restrição no Renajud.'],
            ['Pela entrega das chaves ao delegado', 0, 'A indisponibilidade se dá pelo registro.'],
          ] },
        ],
        logica: 'Sequestro de cada bem com a forma de efetivação, alienação antecipada do que se deteriora, oitiva do MP, sigilo e urgência.',
        arts: ['CPP:128', 'CPP:144-A'] },
    ],
  },
  /* ------------------------------------------------------------ infiltração */
  infiltracao: {
    pistas: ['organização criminosa estruturada, com divisão de tarefas', 'roubos de carga e receptação', 'usa comunicação presencial e mudou seus integrantes', 'depende de um agente inserido no grupo', 'Camaçari/BA'],
    etapas: [
      { t: 'Qual é a peça?', qs: [
          { p: 'As interceptações deixaram de funcionar e só alguém DE DENTRO identifica a cúpula. A peça:', op: [
            ['Infiltração de agente de polícia (Lei 12.850, art. 10)', 1, 'Certo: meio de obtenção de prova subsidiário, quando a prova não pode ser produzida por outros meios (art. 10, § 2º).'],
            ['Ação controlada', 0, 'Ação controlada retarda a intervenção policial para flagrar no melhor momento; não insere ninguém no grupo.'],
            ['Colaboração premiada', 0, 'Depende de um integrante querer colaborar, o que o enunciado não traz.'],
          ] },
        ],
        logica: 'A infiltração é a ultima ratio entre os meios da Lei 12.850 (art. 3º, VII). A pista "interceptações não funcionaram" é a prova da subsidiariedade.',
        arts: ['L12850:3', 'L12850:10'] },
      { t: 'Competência e endereçamento', qs: [
          { p: 'Orcrim de roubo de carga em Camaçari:', op: [
            ['Vara Criminal da Comarca de Camaçari/BA (especializada em organização criminosa, se houver)', 1, 'Certo: crimes estaduais, lugar das infrações.'],
            ['Justiça Federal, por ser organização criminosa', 0, 'Orcrim não é federal por natureza; depende dos crimes praticados.'],
          ] },
        ],
        logica: 'A competência acompanha os crimes da organização.',
        arts: ['CPP:70'] },
      { t: 'O crime: tipificação completa', qs: [
          { p: 'Grupo estruturado, com divisão de tarefas, para roubos e receptação:', op: [
            ['Organização criminosa (Lei 12.850, art. 2º), além dos roubos e receptações', 1, 'Certo: 4 ou mais pessoas, estrutura ordenada, divisão de tarefas, crimes com pena máxima acima de 4 anos (art. 1º, § 1º).'],
            ['Associação criminosa (CP, art. 288)', 0, 'A estrutura e a divisão de tarefas caracterizam a orcrim; o art. 288 exige só 3 pessoas e não a estrutura.'],
          ] },
        ],
        logica: 'Demonstre os 4 elementos do art. 1º, § 1º. Confira no texto oficial se a lei de 2026 alterou o art. 2º.',
        arts: ['L12850:1', 'L12850:2', 'CP:288'] },
      { t: 'A lógica dos fundamentos', qs: [
          { p: 'O que o art. 11 manda o pedido conter?', op: [
            ['Demonstração da necessidade, alcance das tarefas dos agentes e, quando possível, nomes ou apelidos dos investigados e local', 1, 'Certo: o juiz autoriza de forma circunstanciada, motivada e sigilosa (art. 10).'],
            ['O nome verdadeiro do agente infiltrado', 0, 'A identidade do agente é preservada (art. 14).'],
          ] },
        ],
        logica: 'Orcrim configurada → subsidiariedade (art. 10, § 2º) → conteúdo do art. 11 → prazo de até 6 meses, renovável (art. 10, § 3º) → sigilo (art. 12).',
        arts: ['L12850:11', 'L12850:12', 'L12850:14'] },
      { t: 'Os pedidos', qs: [
          { p: 'Prazo da infiltração:', op: [
            ['Até 6 meses, renovável, comprovada a necessidade', 1, 'Certo: art. 10, § 3º.'],
            ['15 dias, renováveis', 0, 'Esse é o prazo da interceptação e da captação ambiental.'],
          ] },
        ],
        logica: 'Autorização circunstanciada com prazo, distribuição sigilosa, oitiva do MP, proteção da identidade do agente.',
        arts: ['L12850:10'] },
    ],
  },
  /* ------------------------------------------------------------ portaria */
  portaria: {
    pistas: ['chegou à Delegacia de Itabuna/BA notícia', 'subtraiu R$ 8.000,00 do caixa ao longo de duas semanas', 'aproveitando-se da confiança do gerente', 'imagens internas e a planilha de caixa', 'não foi preso', 'para iniciar a investigação'],
    etapas: [
      { t: 'Qual é a peça?', qs: [
          { p: 'Há notícia de crime, nada instaurado e ninguém preso; o comando pede para INICIAR a investigação. A peça:', op: [
            ['Portaria de instauração de inquérito policial', 1, 'Certo: instauração de ofício, em crime de ação pública (CPP, art. 5º, I). É ato do próprio delegado.'],
            ['Representação por busca e apreensão', 0, 'Nada indica prova escondida em casa; as imagens e a planilha estão com a loja.'],
            ['Auto de prisão em flagrante', 0, 'Eduardo não foi preso, e o fato já passou.'],
          ] },
        ],
        logica: 'Portaria é a peça de abertura: quem instaura, com que fundamento, o fato em tese e as diligências iniciais (art. 6º).',
        arts: ['CPP:5', 'CPP:6', 'L12830:2'] },
      { t: 'Atribuição (não é competência)', qs: [
          { p: 'A portaria é endereçada a quem?', op: [
            ['A ninguém: é ato interno, com o cabeçalho da Delegacia de Itabuna', 1, 'Certo. Não há juiz destinatário; o que importa é a ATRIBUIÇÃO da delegacia pelo lugar do fato (art. 4º).'],
            ['Ao Juiz da Vara Criminal de Itabuna', 0, 'O IP não depende de autorização judicial para ser instaurado.'],
          ] },
        ],
        logica: 'Delegado tem atribuição, juiz tem competência. A polícia judiciária atua na sua circunscrição (CPP, art. 4º).',
        arts: ['CPP:4'] },
      { t: 'O crime: tipificação completa', qs: [
          { p: 'Funcionário que tira dinheiro do caixa várias vezes, valendo-se da confiança:', op: [
            ['Furto qualificado pelo abuso de confiança (art. 155, § 4º, II), em continuidade delitiva (art. 71)', 1, 'Certo. Mesmas condições de tempo, lugar e modo: crime continuado.'],
            ['Apropriação indébita (art. 168)', 0, 'Na apropriação, o agente já tem a posse lícita e desvigiada do bem. O caixa da loja não estava na posse livre dele: subtraiu.'],
          ] },
        ],
        logica: 'Na portaria, a tipificação é PROVISÓRIA ("em tese"). Furto x apropriação: a diferença é a posse prévia.',
        arts: ['CP:155', 'CP:71', 'CP:168'] },
      { t: 'A lógica das diligências', qs: [
          { p: 'Qual diligência é a mais importante aqui?', op: [
            ['Requisitar as imagens e a planilha, com perícia, e ouvir o gerente', 1, 'Certo: art. 6º, II e III, e exame pericial.'],
            ['Decretar a prisão de Eduardo', 0, 'O delegado não decreta prisão; e nada indica perigo.'],
          ] },
        ],
        logica: 'Diligências do art. 6º, numeradas: ouvir a vítima e testemunhas, apreender e periciar a prova, ouvir o investigado, juntar antecedentes. Prazo: 30 dias, solto (art. 10).',
        arts: ['CPP:6', 'CPP:10'] },
      { t: 'O fecho', qs: [
          { p: 'Como a portaria termina?', op: [
            ['"Registre-se, autue-se e cumpra-se", local, data e "Delegado de Polícia Civil"', 1, 'Certo, sem nome ou rubrica (edital, item 7.2.11.4).'],
            ['"Nesses termos, pede deferimento"', 0, 'Não há pedido: a portaria DETERMINA.'],
          ] },
        ],
        logica: 'Ato do delegado determina; representação pede.',
        arts: ['CPP:10'] },
    ],
  },
};

Object.assign(CONDUCAO, {
  /* ------------------------------------------------------------ facção */
  faccao: {
    pistas: ['cerca de 15 integrantes e divisão de funções', 'liderado por Fábio', 'toque de recolher', 'taxa de segurança', 'barricadas incendiadas', 'loja de fachada', 'pretende fugir para o Paraguai'],
    etapas: [
      { t: 'Qual é a peça?', qs: [
          { p: 'Há um LÍDER perigoso que vai fugir e BENS em nome de terceiros. Uma peça só resolve os dois problemas?', op: [
            ['Sim: preventiva do líder + medidas assecuratórias sobre bens, direitos e valores (Lei 15.358/2026)', 1, 'Certo. Pessoa (preventiva, CPP, art. 313, I e V) e patrimônio (medidas do art. 9º da Lei 15.358) na mesma representação.'],
            ['Só a prisão temporária de Fábio', 0, 'A investigação já tem os elementos; o risco é de fuga e de continuidade do domínio: preventiva.'],
            ['Só o sequestro dos bens', 0, 'Deixaria solto o líder que vai fugir.'],
          ] },
        ],
        logica: 'Quando o enunciado traz mais de um problema (pessoa + bens), a peça cumula pedidos. A Lei 15.358/2026 criou o tipo do domínio social estruturado e medidas patrimoniais próprias; o CPP ganhou o art. 313, V.',
        arts: ['CPP:313:V', 'L15358:2', 'L15358:9'] },
      { t: 'Competência e endereçamento', qs: [
          { p: 'Facção que domina um bairro de Salvador:', op: [
            ['Vara Criminal de Salvador/BA (especializada em organização criminosa, se houver)', 1, 'Certo: crimes estaduais, lugar dos fatos. Confira no texto da Lei 15.358 regras próprias de processo.'],
            ['Juízo Federal, por haver plano de fuga para o exterior', 0, 'A intenção de fugir não desloca a competência.'],
          ] },
        ],
        logica: 'A competência segue os crimes do grupo; a fuga é periculum, não critério de competência.',
        arts: ['CPP:70'] },
      { t: 'O crime: tipificação completa', qs: [
          { p: 'Toque de recolher, taxa de segurança e barricadas, por grupo estruturado:', op: [
            ['Domínio social estruturado (Lei 15.358, art. 2º), com a causa de aumento da liderança', 1, 'Certo: confira os incisos e parágrafos no texto oficial abaixo.'],
            ['Só extorsão (art. 158)', 0, 'A cobrança é uma das condutas, mas o domínio territorial por grupo estruturado tem tipo próprio.'],
          ] },
        ],
        logica: 'Use o tipo novo e diga as condutas do enunciado que se encaixam em cada inciso; aponte a liderança de Fábio.',
        arts: ['L15358:2'] },
      { t: 'A lógica dos fundamentos', qs: [
          { p: 'Qual a ordem da fundamentação nessa peça cumulada?', op: [
            ['Tipificação → cabimento e fumus → periculum e insuficiência das cautelares → medidas assecuratórias', 1, 'Certo: primeiro a pessoa, depois os bens, cada um com seus requisitos.'],
            ['Bens primeiro, porque são a prova da lavagem', 0, 'A ordem que a banca espera segue o pedido principal (a prisão).'],
          ] },
        ],
        logica: 'Dois blocos: PRISÃO (313, I e V; 312; 282, § 6º) e PATRIMÔNIO (art. 9º da Lei 15.358, incluídas as interpostas pessoas: companheira e loja de fachada).',
        arts: ['CPP:312', 'CPP:282', 'L15358:9'] },
      { t: 'Os pedidos', qs: [
          { p: 'Qual pedido mostra que você leu a lei nova?', op: [
            ['O bloqueio de bens também em nome de interpostas pessoas e o sigilo das ordens até o cumprimento', 1, 'Certo: confira os incisos e parágrafos do art. 9º no texto oficial.'],
            ['A condenação de Fábio', 0, 'Delegado não pede condenação.'],
          ] },
        ],
        logica: 'Prisão com mandado e BNMP, recolhimento conforme a lei, medidas patrimoniais item a item, oitiva do MP, sigilo e urgência.',
        arts: ['L15358:9'] },
    ],
  },
  /* ------------------------------------------------------------ flagrante */
  apf: {
    pistas: ['saíram em perseguição ininterrupta', 'ainda com a motocicleta e o revólver municiado', 'duas condenações definitivas anteriores por roubo', 'ficou em silêncio e não indicou advogado', 'elabore a peça que conclui o procedimento'],
    etapas: [
      { t: 'Qual é a peça?', qs: [
          { p: 'O preso já foi apresentado e o auto lavrado; o comando pede a peça que CONCLUI o procedimento. A peça:', op: [
            ['Despacho de conclusão do APF, com representação pela conversão em preventiva', 1, 'Certo: o delegado decide sobre a legalidade, indicia, trata da fiança e das comunicações e representa pela conversão (CPP, art. 310, II).'],
            ['Representação por preventiva autônoma', 0, 'Ele está preso em flagrante: o caminho é a CONVERSÃO, pedida no despacho.'],
            ['Portaria de inquérito', 0, 'No flagrante, o IP começa pelo próprio auto.'],
          ] },
        ],
        logica: 'No flagrante, o delegado é quem decide primeiro: ratifica ou não a prisão. A conversão em preventiva depende de provocação (STJ, Súmula 676), daí a representação dentro do despacho.',
        arts: ['CPP:301', 'CPP:304', 'CPP:310', 'SUM-STJ-676'] },
      { t: 'Competência e destino do auto', qs: [
          { p: 'Para onde vai o auto, e em quanto tempo?', op: [
            ['Ao juiz competente em 24 horas, com cópia à Defensoria (preso sem advogado)', 1, 'Certo: art. 306, § 1º; e audiência de custódia em 24 horas (art. 310).'],
            ['Ao MP em 48 horas', 0, 'O auto vai ao juiz em 24 h; o MP é comunicado.'],
          ] },
        ],
        logica: 'Prazos de 24 horas: nota de culpa, remessa do auto, cópia à Defensoria, custódia. A comunicação da prisão ao juiz, ao MP e à família é IMEDIATA.',
        arts: ['CPP:306', 'CF:5:LXII'] },
      { t: 'O crime: tipificação completa', qs: [
          { p: 'Revólver municiado para tomar a motocicleta:', op: [
            ['Roubo majorado pelo emprego de arma de fogo (art. 157, § 2º-A, I)', 1, 'Certo. A arma é meio do roubo; o porte fica absorvido quando usado só para o crime.'],
            ['Roubo + porte ilegal de arma em concurso material', 0, 'Se a arma foi usada só no roubo, o porte é absorvido (consunção); concurso material exige porte autônomo.'],
          ] },
          { p: 'Que espécie de flagrante?', op: [
            ['Impróprio: perseguido logo após, sem interrupção (art. 302, III)', 1, 'Certo; e também se encaixa no presumido (inciso IV), por ter sido encontrado com a coisa e a arma.'],
            ['Preparado, logo inválido', 0, 'Flagrante preparado é quando a polícia provoca o crime (STF, Súmula 145). Não é o caso.'],
          ] },
        ],
        logica: 'No despacho, a tipificação vira INDICIAMENTO (Lei 12.830, art. 2º, § 6º). Confira a pena-base do roubo no texto oficial, alterada em 2026.',
        arts: ['CP:157', 'CPP:302', 'SUM-STF-145', 'L12830:2:§6'] },
      { t: 'A lógica do despacho', qs: [
          { p: 'O delegado arbitra fiança aqui?', op: [
            ['Não: pena máxima acima de 4 anos (art. 322) e presentes os motivos da preventiva (art. 324, IV)', 1, 'Certo.'],
            ['Sim, porque Diego ficou em silêncio', 0, 'O silêncio é direito (CF, art. 5º, LXIII) e não interfere na fiança.'],
          ] },
        ],
        logica: 'Ordem do despacho: legalidade (302) → indiciamento → fiança (322) → providências (306, exames, restituição) → representação pela conversão (310, II; 312; 313, I e II).',
        arts: ['CPP:322', 'CPP:324', 'CPP:313'] },
      { t: 'As providências', qs: [
          { p: 'Qual providência a banca procura, por Diego não ter indicado advogado?', op: [
            ['Cópia integral do auto à Defensoria Pública em 24 horas', 1, 'Certo: art. 306, § 1º.'],
            ['Nomear advogado dativo pelo delegado', 0, 'A lei manda remeter à Defensoria.'],
          ] },
        ],
        logica: 'Providências numeradas, e a representação pela conversão no fim.',
        arts: ['CPP:306'] },
    ],
  },
  /* ------------------------------------------------------------ cautelares diversas */
  'cautelar-diversa': {
    pistas: ['fiscal de obras do Município', 'solicitou R$ 5.000,00', 'é primário, tem residência fixa', 'continua fiscalizando obras', 'temer represálias', 'a prisão preventiva seria desproporcional'],
    etapas: [
      { t: 'Qual é a peça?', qs: [
          { p: 'O enunciado diz que a preventiva seria desproporcional, mas há risco ligado ao CARGO. A peça:', op: [
            ['Cautelares diversas: suspensão da função pública e proibição de contato (art. 319, VI e III)', 1, 'Certo: o risco nasce do exercício da função, e a medida que o contém é a suspensão.'],
            ['Prisão preventiva', 0, 'O próprio comando afasta a preventiva.'],
            ['Afastamento do cargo por portaria do delegado', 0, 'O delegado não afasta servidor: é medida judicial.'],
          ] },
        ],
        logica: 'Cautelar diversa responde à pergunta "o que resolve o risco sem prender?". A medida tem de ser ADEQUADA ao risco concreto (art. 282, II).',
        arts: ['CPP:282', 'CPP:319'] },
      { t: 'Competência e endereçamento', qs: [
          { p: 'Fiscal municipal em Lauro de Freitas:', op: [
            ['Vara Criminal da Comarca de Lauro de Freitas/BA', 1, 'Certo: servidor municipal não tem foro especial; justiça estadual.'],
            ['Tribunal de Justiça, por ser agente público', 0, 'Foro no TJ é do prefeito (CF, art. 29, X), não do fiscal.'],
          ] },
        ],
        logica: 'Verifique sempre se há foro por prerrogativa; servidor comum não tem.',
        arts: ['CF:29:X'] },
      { t: 'O crime: tipificação completa', qs: [
          { p: 'Pedir dinheiro para não embargar obra:', op: [
            ['Corrupção passiva, na modalidade "solicitar" (art. 317)', 1, 'Certo: crime formal, consuma-se com a solicitação.'],
            ['Concussão (art. 316)', 0, 'Concussão é EXIGIR (imposição). O enunciado diz que ele SOLICITOU.'],
          ] },
        ],
        logica: 'Corrupção passiva (solicitar, receber, aceitar promessa) x concussão (exigir): o verbo do enunciado decide.',
        arts: ['CP:317', 'CP:316'] },
      { t: 'A lógica dos fundamentos', qs: [
          { p: 'Qual expressão legal você precisa usar para a suspensão da função?', op: [
            ['"Justo receio de sua utilização para a prática de infrações penais"', 1, 'Certo: art. 319, VI.'],
            ['"Garantia da ordem econômica"', 0, 'É finalidade da preventiva, não requisito da suspensão.'],
          ] },
        ],
        logica: 'Fumus → periculum ligado ao cargo → medida adequada (VI) + proteção das vítimas (III) → por que não a prisão → advertência do art. 282, § 4º.',
        arts: ['CPP:319:VI', 'CPP:282:§4'] },
      { t: 'Os pedidos', qs: [
          { p: 'O que não pode faltar no pedido de suspensão da função?', op: [
            ['A comunicação ao Município, para que a suspensão produza efeito', 1, 'Certo.'],
            ['A exoneração do servidor', 0, 'Exoneração é sanção administrativa, não cautelar penal.'],
          ] },
        ],
        logica: 'Cada medida com o inciso, a advertência, a oitiva do MP, sigilo e urgência.',
        arts: ['CPP:319'] },
    ],
  },
  /* ------------------------------------------------------------ relatório */
  relatorio: {
    pistas: ['instaurado por portaria', 'em seis ocasiões ao longo de duas semanas', 'A perícia nas imagens internas confirmou', 'confessou e devolveu R$ 2.000,00', 'Encerradas as diligências', 'investigado solto'],
    etapas: [
      { t: 'Qual é a peça?', qs: [
          { p: 'As diligências estão ENCERRADAS. A peça:', op: [
            ['Relatório final do inquérito', 1, 'Certo: art. 10, § 1º, do CPP.'],
            ['Pedido de arquivamento', 0, 'O delegado não arquiva nem pede arquivamento como decisão própria (art. 17); pode, no relatório, sugerir, se for o caso.'],
            ['Denúncia', 0, 'Denúncia é do MP.'],
          ] },
        ],
        logica: 'Relatório = o que se apurou, como e por quê, com a conclusão técnico-jurídica. Termina com a remessa ao juízo.',
        arts: ['CPP:10', 'CPP:17'] },
      { t: 'Destino do relatório', qs: [
          { p: 'O relatório é dirigido a quem?', op: [
            ['Ao Juiz de Direito da Vara Criminal de Itabuna/BA', 1, 'Certo: os autos vão ao juiz competente (art. 10, § 1º), com vista ao MP.'],
            ['Ao Chefe de Polícia', 0, 'O destino dos autos é o Judiciário.'],
          ] },
        ],
        logica: 'Peça de inquérito endereçada ao juiz, sem pedido de deferimento.',
        arts: ['CPP:10'] },
      { t: 'O crime: tipificação completa', qs: [
          { p: 'Ele devolveu R$ 2.000,00 de R$ 8.000,00. Há arrependimento posterior?', op: [
            ['Não: a reparação foi parcial; o art. 16 exige reparação integral até o recebimento da denúncia', 1, 'Certo. Mas a confissão pode atenuar a pena (art. 65, III, "d").'],
            ['Sim, reduz a pena de 1/3 a 2/3', 0, 'Só com reparação integral do dano.'],
          ] },
        ],
        logica: 'Indicie com a tipificação completa: art. 155, § 4º, II, c/c art. 71 (seis vezes); registre a confissão e a devolução parcial.',
        arts: ['CP:155', 'CP:71', 'CP:16', 'CP:65'] },
      { t: 'A lógica do relatório', qs: [
          { p: 'Qual a ordem das partes?', op: [
            ['Fatos → diligências → materialidade → autoria → indiciamento → conclusão e remessa', 1, 'Certo.'],
            ['Pedidos → fatos → fundamentos', 0, 'Relatório não tem pedidos.'],
          ] },
        ],
        logica: 'O indiciamento é privativo do delegado, por ato fundamentado (Lei 12.830, art. 2º, § 6º).',
        arts: ['L12830:2:§6'] },
      { t: 'O encerramento', qs: [
          { p: 'O que você comunica ao encerrar?', op: [
            ['O indiciamento ao instituto de identificação e estatística (art. 23)', 1, 'Certo.'],
            ['A sentença ao investigado', 0, 'Não há sentença no inquérito.'],
          ] },
        ],
        logica: 'Remessa ao juízo, comunicação do art. 23, local, data e assinatura.',
        arts: ['CPP:23'] },
    ],
  },
  /* ------------------------------------------------------------ captação ambiental */
  captacao: {
    pistas: ['A interceptação telefônica autorizada anteriormente perdeu a utilidade', 'deixaram de falar ao telefone', 'dentro da caminhonete de Wagner', 'estacionada à noite na via pública', 'duas vezes por semana'],
    etapas: [
      { t: 'Qual é a peça?', qs: [
          { p: 'Eles abandonaram o telefone e falam PESSOALMENTE dentro de um veículo. A peça:', op: [
            ['Captação ambiental (Lei 9.296, art. 8º-A)', 1, 'Certo: sinais acústicos e ópticos de conversa presencial, num local determinado.'],
            ['Renovação da interceptação', 0, 'Perdeu a utilidade: eles não usam mais o telefone.'],
            ['Busca no veículo', 0, 'A busca apreende coisas; o que se quer é ouvir as reuniões.'],
          ] },
        ],
        logica: 'Telefone → interceptação; conversa presencial num local → captação ambiental; grupo fechado → infiltração.',
        arts: ['L9296:8-A'] },
      { t: 'Competência e endereçamento', qs: [
          { p: 'Tráfico em Salvador:', op: [
            ['Vara Criminal (ou de Tóxicos) de Salvador/BA', 1, 'Certo: o mesmo juízo da interceptação anterior (prevenção).'],
            ['Juizado Especial Criminal', 0, 'Tráfico não é infração de menor potencial ofensivo.'],
          ] },
        ],
        logica: 'Se já houve medida anterior no mesmo IP, o juízo está prevento.',
        arts: ['CPP:83'] },
      { t: 'O crime: tipificação completa', qs: [
          { p: 'O tráfico atende ao requisito do art. 8º-A, II?', op: [
            ['Sim: pena máxima acima de 4 anos', 1, 'Certo: confira a pena do art. 33 no texto oficial.'],
            ['Não: a captação só cabe em crime hediondo', 0, 'O critério é a pena máxima superior a 4 anos ou a conexão.'],
          ] },
        ],
        logica: 'Tipifique (tráfico e associação) para provar o requisito de pena.',
        arts: ['L11343:33', 'L11343:35'] },
      { t: 'A lógica dos fundamentos', qs: [
          { p: 'Pode instalar o dispositivo à noite?', op: [
            ['Sim, fora da casa: o veículo na via pública não é casa (art. 8º-A, § 2º)', 1, 'Certo.'],
            ['Não, nunca à noite', 0, 'A lei admite a instalação noturna e disfarçada, exceto na casa.'],
          ] },
        ],
        logica: 'Requisitos (I e II) → local e forma de instalação (§ 1º) → regra do § 2º → prazo de 15 dias renovável (§ 3º).',
        arts: ['L9296:8-A', 'CF:5:XI'] },
      { t: 'Os pedidos', qs: [
          { p: 'Prazo da captação:', op: [
            ['15 dias, renováveis se a atividade criminal for permanente, habitual ou continuada', 1, 'Certo: art. 8º-A, § 3º.'],
            ['6 meses', 0, 'Prazo da infiltração.'],
          ] },
        ],
        logica: 'Local exato, prazo, forma de instalação, MP, sem intimação prévia, sigilo.',
        arts: ['L9296:8-A'] },
    ],
  },
  /* ------------------------------------------------------------ sigilo bancário e fiscal */
  'sigilo-bancario': {
    pistas: ['tesoureiro da Câmara Municipal', 'desviou cerca de R$ 600.000,00', 'transferências para contas de terceiros', 'Relatório de Inteligência Financeira', 'depósitos fracionados', 'renda incompatível'],
    etapas: [
      { t: 'Qual é a peça?', qs: [
          { p: 'A prova está no CAMINHO DO DINHEIRO. A peça:', op: [
            ['Quebra de sigilo bancário e fiscal', 1, 'Certo: LC 105, art. 1º, § 4º, e CTN, art. 198, § 1º, I.'],
            ['Requisição direta aos bancos pelo delegado', 0, 'Para a polícia, há reserva de jurisdição.'],
            ['Sequestro de bens', 0, 'Pode vir depois; agora é preciso rastrear para onde foi o dinheiro.'],
          ] },
        ],
        logica: 'O RIF da UIF pode ser compartilhado com a polícia sem ordem judicial (STF, Tema 990), mas a QUEBRA dos extratos depende do juiz.',
        arts: ['LC105:1', 'L5172:198'] },
      { t: 'Competência e endereçamento', qs: [
          { p: 'Desvio de verba da Câmara Municipal de Feira de Santana:', op: [
            ['Vara Criminal da Comarca de Feira de Santana/BA', 1, 'Certo: verba municipal, servidor sem foro especial.'],
            ['Justiça Federal', 0, 'Só se a verba fosse federal sujeita a prestação de contas perante órgão federal.'],
          ] },
        ],
        logica: 'Verba municipal → justiça estadual.',
        arts: ['CF:109:IV'] },
      { t: 'O crime: tipificação completa', qs: [
          { p: 'Tesoureiro que desvia dinheiro de que tem a posse em razão do cargo:', op: [
            ['Peculato-desvio (art. 312, caput), e lavagem pelos depósitos fracionados', 1, 'Certo.'],
            ['Furto qualificado', 0, 'A posse em razão do cargo e a qualidade de funcionário fazem o peculato.'],
          ] },
        ],
        logica: 'Peculato + lavagem: o fracionamento é a dissimulação.',
        arts: ['CP:312', 'L9613:1'] },
      { t: 'A lógica dos fundamentos', qs: [
          { p: 'A quebra pode alcançar a companheira?', op: [
            ['Sim, porque há depósitos fracionados nas contas dela; justifique e delimite o período', 1, 'Certo: necessidade e adequação (art. 282, I e II).'],
            ['Não, só o investigado', 0, 'Alcança quem, pelos indícios, recebeu os valores.'],
          ] },
        ],
        logica: 'Fumus → cabimento (qualquer ilícito, em qualquer fase) → necessidade (rastrear destino, extensão e beneficiários) → período e pessoas delimitados.',
        arts: ['LC105:1', 'CPP:282'] },
      { t: 'Os pedidos', qs: [
          { p: 'Como se operacionaliza o sigilo fiscal?', op: [
            ['Ofício à Receita Federal para envio das declarações de IR do período', 1, 'Certo: CTN, art. 198, § 1º, I.'],
            ['Pedido ao Município', 0, 'O dado fiscal do IR está na Receita Federal.'],
          ] },
        ],
        logica: 'Bancário (com o Cadastro de Clientes do SFN) e fiscal, período delimitado, MP, sem intimação prévia, sigilo.',
        arts: ['L5172:198'] },
    ],
  },
  /* ------------------------------------------------------------ 13-B */
  'localizacao-13b': {
    pistas: ['abordada por dois homens armados', 'levada em um carro', 'exigindo R$ 200.000,00 pela libertação', 'celular de Larissa está desligado', 'registrada às 11h', 'com urgência'],
    etapas: [
      { t: 'Qual é a peça?', qs: [
          { p: 'A vítima está EM PODER dos autores, o crime está em curso, e é preciso achá-la já. A peça:', op: [
            ['Representação pelos meios técnicos de localização (CPP, art. 13-B)', 1, 'Certo: sinal das ERBs para localizar vítima e suspeitos em crime do rol do art. 13-A.'],
            ['Interceptação telefônica', 0, 'O conteúdo das ligações não localiza a vítima a tempo; o sinal sim.'],
            ['Prisão temporária dos autores', 0, 'Os autores nem foram identificados.'],
          ] },
        ],
        logica: 'O 13-B é a medida da URGÊNCIA DA VIDA: sinal, não conteúdo, com prazo de 12 h para o juiz decidir.',
        arts: ['CPP:13-A', 'CPP:13-B'] },
      { t: 'Competência e endereçamento', qs: [
          { p: 'Às 11h de um dia útil, em Salvador:', op: [
            ['Vara Criminal de Salvador/BA (ou o plantão judiciário, se fora do expediente)', 1, 'Certo.'],
            ['Diretamente às operadoras, sem juiz', 0, 'Só se o juiz não se manifestar em 12 horas (§ 4º).'],
          ] },
        ],
        logica: 'Primeiro o juiz; o silêncio dele por 12 h abre a requisição direta, com comunicação imediata.',
        arts: ['CPP:13-B:§4'] },
      { t: 'O crime: tipificação completa', qs: [
          { p: 'Sequestro com pedido de resgate:', op: [
            ['Extorsão mediante sequestro (art. 159), crime do rol do art. 13-A e hediondo', 1, 'Certo.'],
            ['Sequestro e cárcere privado (art. 148)', 0, 'O pedido de resgate faz a extorsão mediante sequestro.'],
          ] },
        ],
        logica: 'A tipificação abre a porta do 13-B: só os crimes do rol do 13-A.',
        arts: ['CP:159', 'L8072:1'] },
      { t: 'A lógica dos fundamentos', qs: [
          { p: 'Qual o alcance do sinal?', op: [
            ['Posição da estação de cobertura, setorização e intensidade de radiofrequência, sem acesso ao conteúdo', 1, 'Certo: §§ 1º e 2º, I.'],
            ['Todas as mensagens do celular', 0, 'Conteúdo depende de outra autorização.'],
          ] },
        ],
        logica: 'Crime do rol → urgência → alcance (sinal) → prazo (30 dias, renovável uma vez) → decisão em 12 h → IP em 72 h.',
        arts: ['CPP:13-B'] },
      { t: 'Os pedidos', qs: [
          { p: 'Qual prazo você PEDE ao juiz?', op: [
            ['Decisão em 12 horas (§ 4º)', 1, 'Certo.'],
            ['Decisão em 48 horas', 0, 'O prazo legal é de 12 horas.'],
          ] },
        ],
        logica: 'Os dois aparelhos, o prazo do sinal, as 12 h, ciência ao MP, sigilo.',
        arts: ['CPP:13-B:§3', 'CPP:13-B:§4'] },
    ],
  },
  /* ------------------------------------------------------------ alienação antecipada */
  alienacao: {
    pistas: ['foram sequestrados por ordem judicial', 'O pátio é descoberto', 'a lancha não tem onde ser guardada', 'ferrugem inicial', 'perda de valor de mercado estimada em 15%'],
    etapas: [
      { t: 'Qual é a peça?', qs: [
          { p: 'Os bens JÁ estão sequestrados, mas estão estragando e perdendo valor. A peça:', op: [
            ['Alienação antecipada (CPP, art. 144-A)', 1, 'Certo: para preservar o valor quando há deterioração, depreciação ou dificuldade de manutenção.'],
            ['Novo sequestro', 0, 'Já estão sequestrados.'],
            ['Restituição ao proprietário', 0, 'Os bens interessam ao processo e ao confisco.'],
          ] },
        ],
        logica: 'Sequestro torna indisponível; alienação antecipada converte em dinheiro para não perder valor.',
        arts: ['CPP:144-A'] },
      { t: 'Competência e endereçamento', qs: [
          { p: 'A quem se pede?', op: [
            ['Ao mesmo juízo que decretou o sequestro (Vara Criminal de Salvador/BA)', 1, 'Certo: prevenção.'],
            ['Ao juízo cível', 0, 'É incidente do processo penal.'],
          ] },
        ],
        logica: 'Medida acessória vai ao juízo da medida principal.',
        arts: ['CPP:83'] },
      { t: 'O crime de fundo', qs: [
          { p: 'Por que os bens foram sequestrados?', op: [
            ['Indícios veementes de origem ilícita na lavagem (Lei 9.613, art. 1º; CPP, art. 126)', 1, 'Certo.'],
            ['Para pagar a fiança', 0, 'Não há relação com fiança.'],
          ] },
        ],
        logica: 'Retome o fumus do sequestro em poucas linhas.',
        arts: ['L9613:1', 'L9613:4', 'CPP:126'] },
      { t: 'A lógica dos fundamentos', qs: [
          { p: 'Qual a pista mais forte do periculum?', op: [
            ['A perícia (ferrugem e 15% de perda em seis meses) e a falta de local para a lancha', 1, 'Certo: dados concretos.'],
            ['O fato de o investigado ser perigoso', 0, 'O periculum aqui é do BEM, não da pessoa.'],
          ] },
        ],
        logica: 'DDD do art. 144-A (deterioração, depreciação, dificuldade) → rito (avaliação, leilão, 80%) → depósito judicial.',
        arts: ['CPP:144-A'] },
      { t: 'Os pedidos', qs: [
          { p: 'O que se faz com o dinheiro?', op: [
            ['Depósito em conta vinculada ao juízo até a decisão final', 1, 'Certo: § 3º.'],
            ['Entrega imediata ao Estado', 0, 'Só com a condenação.'],
          ] },
        ],
        logica: 'Avaliação, leilão, depósito, ofício ao Detran e à Capitania, intimação do proprietário, MP.',
        arts: ['CPP:144-A'] },
    ],
  },
  /* ------------------------------------------------------------ perfil genético */
  'perfil-genetico': {
    pistas: ['colheu material biológico do agressor', 'Uma testemunha viu Fábio sair do terreno', 'não conseguiu reconhecê-lo com segurança', 'é civilmente identificado e se recusa a fornecer material'],
    etapas: [
      { t: 'Qual é a peça?', qs: [
          { p: 'Há um vestígio com DNA e um suspeito que se recusa a fornecer material. A peça:', op: [
            ['Identificação criminal com coleta de perfil genético e acesso aos bancos de dados (Lei 12.037)', 1, 'Certo: art. 3º, IV, e art. 5º, parágrafo único.'],
            ['Busca e apreensão de objetos pessoais de Fábio', 0, 'Poderia render material, mas a via legal específica é a identificação criminal.'],
            ['Prisão preventiva', 0, 'Os indícios ainda são frágeis: o DNA é o que vai confirmar ou afastar a autoria.'],
          ] },
        ],
        logica: 'Civilmente identificado só é identificado criminalmente nas hipóteses legais (CF, art. 5º, LVIII); a do caso é a essencial às investigações, por despacho judicial.',
        arts: ['CF:5:LVIII', 'L12037:3', 'L12037:5'] },
      { t: 'Competência e endereçamento', qs: [
          { p: 'Estupro por desconhecido em Itabuna:', op: [
            ['Vara Criminal da Comarca de Itabuna/BA', 1, 'Certo: não há relação doméstica nem vítima criança.'],
            ['Juizado de Violência Doméstica', 0, 'Exige relação doméstica, familiar ou íntima de afeto (Lei 11.340, art. 5º).'],
          ] },
        ],
        logica: 'Violência contra a mulher só vai ao juízo de violência doméstica se houver o vínculo do art. 5º da Lei Maria da Penha.',
        arts: ['L11340:5'] },
      { t: 'O crime: tipificação completa', qs: [
          { p: 'O fato:', op: [
            ['Estupro (art. 213), crime hediondo', 1, 'Certo: Lei 8.072, art. 1º, V.'],
            ['Importunação sexual (art. 215-A)', 0, 'Houve violência para o ato sexual: estupro.'],
          ] },
        ],
        logica: 'Tipifique e diga que o crime deixa vestígios: daí o corpo de delito (CPP, art. 158).',
        arts: ['CP:213', 'L8072:1', 'CPP:158'] },
      { t: 'A lógica dos fundamentos', qs: [
          { p: 'O que o perfil genético do banco NÃO pode revelar?', op: [
            ['Traços somáticos ou comportamentais, salvo o gênero', 1, 'Certo: art. 5º-A, § 1º.'],
            ['O nome do investigado', 0, 'A identificação é justamente a finalidade.'],
          ] },
        ],
        logica: 'Indício frágil → identificação essencial (art. 3º, IV) → coleta de DNA (art. 5º, parágrafo único) → limites (art. 5º-A) → acesso aos bancos (art. 7º-C; LEP, art. 9º-A, § 2º).',
        arts: ['L12037:5-A', 'L12037:7-C', 'L7210:9-A'] },
      { t: 'Os pedidos', qs: [
          { p: 'Qual pedido dá sentido à coleta?', op: [
            ['O confronto com o vestígio, consignado em laudo pericial', 1, 'Certo.'],
            ['A divulgação do resultado à imprensa', 0, 'Os dados são sigilosos.'],
          ] },
        ],
        logica: 'Identificação com DNA, confronto em laudo, acesso aos dois bancos, MP, sigilo.',
        arts: ['L12037:7-C'] },
    ],
  },
  /* ------------------------------------------------------------ internação provisória */
  internacao: {
    pistas: ['Kauã, de 16 anos', 'encostou uma faca no pescoço', 'auto de apreensão em flagrante de ato infracional', 'outros dois atos infracionais análogos a roubo', '"voltaria para pegá-la"', 'Os pais compareceram'],
    etapas: [
      { t: 'Qual é a peça?', qs: [
          { p: 'O autor é ADOLESCENTE, o ato teve grave ameaça e há risco à vítima. A peça:', op: [
            ['Representação pela internação provisória (ECA, art. 108)', 1, 'Certo: até 45 dias, antes da sentença, com necessidade imperiosa.'],
            ['Representação por prisão preventiva', 0, 'Adolescente não é preso preventivamente: o ECA tem regime próprio.'],
            ['Liberação aos pais, sem peça', 0, 'A gravidade e a ameaça à vítima afastam a liberação (art. 174).'],
          ] },
        ],
        logica: 'Menor de 18 anos é inimputável (CF, art. 228): pratica ATO INFRACIONAL. O procedimento começa pelo auto de apreensão (art. 173), não por inquérito.',
        arts: ['CF:228', 'L8069:103', 'L8069:108', 'L8069:173'] },
      { t: 'Competência e endereçamento', qs: [
          { p: 'A quem se endereça?', op: [
            ['Ao Juiz de Direito da Vara da Infância e Juventude da Comarca de Salvador/BA', 1, 'Certo: art. 148, I, do ECA.'],
            ['Ao Juiz da Vara Criminal', 0, 'Ato infracional é da Infância e Juventude.'],
          ] },
        ],
        logica: 'Ato infracional → Justiça da Infância e Juventude.',
        arts: ['L8069:148'] },
      { t: 'O ato infracional', qs: [
          { p: 'Faca no pescoço para levar o celular:', op: [
            ['Ato infracional análogo ao roubo majorado pelo emprego de arma branca (art. 157, § 2º, VII)', 1, 'Certo.'],
            ['Crime de roubo', 0, 'Adolescente não comete crime: ato infracional análogo (art. 103).'],
          ] },
        ],
        logica: 'Sempre "ato infracional análogo a…". A arma branca está no § 2º, VII (Pacote Anticrime).',
        arts: ['L8069:103', 'CP:157:§2'] },
      { t: 'A lógica dos fundamentos', qs: [
          { p: 'Quais incisos do art. 122 o caso preenche?', op: [
            ['I (grave ameaça) e II (reiteração em infrações graves)', 1, 'Certo; e a necessidade imperiosa do art. 108, parágrafo único.'],
            ['Só o III (descumprimento de medida)', 0, 'Não há medida anterior descumprida no enunciado.'],
          ] },
        ],
        logica: 'Indícios (108) → cabimento (122, I e II) → necessidade imperiosa (ameaça à vítima, reiteração) → nenhuma outra medida adequada (122, § 2º) → local (123 e 185).',
        arts: ['L8069:122', 'L8069:123', 'L8069:174', 'L8069:185'] },
      { t: 'Os pedidos', qs: [
          { p: 'Qual o prazo máximo que você pede?', op: [
            ['45 dias (art. 108)', 1, 'Certo; o procedimento deve terminar nesse prazo, improrrogável (art. 183).'],
            ['90 dias, como a revisão da preventiva', 0, 'O ECA fixa 45 dias.'],
          ] },
        ],
        logica: 'Internação por até 45 dias, entidade exclusiva, MP, ciência aos pais, sigilo.',
        arts: ['L8069:183', 'L8069:143'] },
    ],
  },
});
