from base import I
from civ_juris import J

CC = 'L10406:'
P = 'DBA26-CIV-1'
# ---------------- PONTO 1 · Das pessoas — RODADA 1
I(P, 1, 'Início da personalidade e nascituro',
  'A personalidade civil da pessoa começa do nascimento com vida, mas a lei põe a salvo, desde a concepção, os direitos do nascituro.', 'C',
  'É o art. 2º: a **personalidade** nasce com o **nascimento com vida**; o **nascituro** tem seus direitos resguardados desde a concepção.',
  lei=[(CC + '2', 'A personalidade civil da pessoa', 'os direitos do nascituro.', 'CC, art. 2º')],
  kw=['nascimento com vida', 'nascituro'])
I(P, 1, 'Incapacidade absoluta',
  'São absolutamente incapazes de exercer pessoalmente os atos da vida civil os menores de dezesseis anos e os que, por enfermidade ou deficiência mental, não tiverem o necessário discernimento.', 'E',
  'Desde o Estatuto da Pessoa com Deficiência (Lei 13.146/2015), o art. 3º só traz os **menores de 16 anos**. A deficiência **não** gera incapacidade absoluta.',
  lei=[(CC + '3', 'São absolutamente incapazes', '(dezesseis) anos.', 'CC, art. 3º')],
  peg='A banca reproduz a redação antiga do art. 3º (anterior a 2015), com o inciso sobre deficiência mental.',
  kw=['absolutamente incapazes', 'menores de 16 anos'])
I(P, 1, 'Incapacidade relativa',
  'São relativamente incapazes os maiores de dezesseis e menores de dezoito anos, os ébrios habituais e os viciados em tóxico, aqueles que, por causa transitória ou permanente, não puderem exprimir sua vontade, e os pródigos.', 'C',
  'É o rol atual do art. 4º. Quem **não pode exprimir a vontade** passou a ser **relativamente** incapaz em 2015.',
  lei=[(CC + '4', 'I - os maiores de dezesseis e menores de dezoito anos;', 'IV - os pródigos.', 'CC, art. 4º')],
  exc=['A capacidade dos indígenas é regulada por legislação especial (art. 4º, par. ún.)'],
  kw=['relativamente incapazes', 'pródigos'])
I(P, 1, 'Emancipação voluntária',
  'A emancipação concedida pelos pais ao menor com dezesseis anos completos exige instrumento público e homologação judicial.', 'E',
  'A emancipação **voluntária** se faz por **instrumento público**, **independentemente de homologação judicial**. Sentença só há na emancipação judicial (menor sob tutela, ouvido o tutor).',
  lei=[(CC + '5', 'I - pela concessão dos pais', 'dezesseis anos completos;', 'CC, art. 5º, par. ún., I')],
  exc=['Emancipação legal: casamento, emprego público efetivo, colação de grau em curso de ensino superior, estabelecimento civil ou comercial ou relação de emprego com economia própria, aos 16 anos completos (art. 5º, par. ún., II a V)'],
  peg='Acrescentar "homologação judicial" onde a lei diz "independentemente de homologação judicial".',
  kw=['emancipação voluntária', 'instrumento público'])
I(P, 1, 'Morte presumida sem ausência',
  'Pode ser declarada a morte presumida, sem decretação de ausência, se for extremamente provável a morte de quem estava em perigo de vida, e a declaração só pode ser requerida depois de esgotadas as buscas e averiguações, devendo a sentença fixar a data provável do falecimento.', 'C',
  'Art. 7º: **morte presumida sem ausência** (perigo de vida; desaparecido em campanha ou prisioneiro não encontrado até 2 anos após a guerra). Exige **esgotamento das buscas** e a sentença fixa a **data provável** da morte.',
  lei=[(CC + '7', 'Pode ser declarada a morte presumida', 'esgotadas as buscas e averiguações', 'CC, art. 7º')],
  kw=['morte presumida', 'perigo de vida'])
I(P, 1, 'Comoriência',
  'Se dois ou mais indivíduos falecerem na mesma ocasião, não se podendo averiguar se algum precedeu aos outros, presume-se que o mais velho morreu primeiro.', 'E',
  'Art. 8º: a lei civil brasileira adota a **comoriência** — presumem-se **simultaneamente mortos**. Não há presunção por idade.',
  lei=[(CC + '8', 'Se dois ou mais indivíduos falecerem', 'simultaneamente mortos.', 'CC, art. 8º')],
  peg='Trocar a presunção de morte simultânea por uma ordem de idade (critério de outros sistemas).',
  kw=['comoriência', 'simultaneamente mortos'])
I(P, 1, 'Características dos direitos da personalidade',
  'Com exceção dos casos previstos em lei, os direitos da personalidade são intransmissíveis e irrenunciáveis, não podendo o seu exercício sofrer limitação voluntária.', 'C',
  'Literalidade do art. 11: **intransmissíveis** e **irrenunciáveis**, ressalvados os casos legais.',
  lei=[(CC + '11', 'Com exceção dos casos previstos em lei', 'limitação voluntária.', 'CC, art. 11')],
  kw=['direitos da personalidade', 'intransmissíveis', 'irrenunciáveis'])
I(P, 1, 'Disposição do próprio corpo post mortem',
  'É válida a disposição do próprio corpo, no todo ou em parte, para depois da morte, com objetivo científico ou altruístico, ainda que onerosa, sendo o ato irrevogável depois de formalizado.', 'E',
  'Art. 14: a disposição tem de ser **gratuita** e pode ser **livremente revogada a qualquer tempo**. A assertiva erra duas vezes.',
  lei=[(CC + '14', 'É válida, com objetivo científico', 'para depois da morte.', 'CC, art. 14'),
       (CC + '14', 'O ato de disposição pode ser livremente revogado', 'a qualquer tempo.', 'CC, art. 14, par. ún.')],
  kw=['gratuita', 'revogado a qualquer tempo'])
I(P, 1, 'Pessoas jurídicas de direito privado',
  'Os partidos políticos e as organizações religiosas são pessoas jurídicas de direito público interno.', 'E',
  'Art. 44: associações, sociedades, fundações, **organizações religiosas** e **partidos políticos** são pessoas jurídicas de **direito privado**.',
  lei=[(CC + '44', 'São pessoas jurídicas de direito privado', 'os partidos políticos.', 'CC, art. 44')],
  exc=['Direito público interno: União, Estados, DF, Territórios, Municípios, autarquias (inclusive associações públicas) e demais entidades de caráter público criadas por lei (art. 41)'],
  kw=['direito privado', 'partidos políticos'])
I(P, 1, 'Início da existência da pessoa jurídica',
  'Começa a existência legal das pessoas jurídicas de direito privado com a inscrição do ato constitutivo no respectivo registro, precedida, quando necessário, de autorização ou aprovação do Poder Executivo.', 'C',
  'Art. 45: o **registro** do ato constitutivo é constitutivo da personalidade da pessoa jurídica de direito privado.',
  lei=[(CC + '45', 'Começa a existência legal', 'Poder Executivo', 'CC, art. 45')],
  kw=['inscrição do ato constitutivo', 'registro'])
I(P, 1, 'Desconsideração da personalidade jurídica',
  'Em caso de abuso da personalidade jurídica, caracterizado pelo desvio de finalidade ou pela confusão patrimonial, o juiz pode, de ofício, desconsiderá-la para atingir os bens particulares dos sócios.', 'E',
  'Art. 50: a desconsideração depende de **requerimento da parte ou do Ministério Público**, quando lhe couber intervir. E só atinge administradores ou sócios **beneficiados direta ou indiretamente** pelo abuso.',
  regra='Teoria maior: abuso (desvio de finalidade ou confusão patrimonial) + requerimento.',
  lei=[(CC + '50', 'Em caso de abuso da personalidade jurídica', 'direta ou indiretamente pelo abuso.', 'CC, art. 50')],
  juris=[J['T1210']],
  peg='"De ofício" — a lei exige requerimento.',
  kw=['desconsideração', 'requerimento da parte', 'teoria maior'])
I(P, 1, 'Domicílio e pluralidade de residências',
  'O domicílio da pessoa natural é o lugar onde ela estabelece a sua residência com ânimo definitivo; se tiver diversas residências onde alternadamente viva, considera-se domicílio seu qualquer delas.', 'C',
  'Arts. 70 e 71: **residência + ânimo definitivo**; o CC admite a **pluralidade de domicílios**.',
  lei=[(CC + '70', 'O domicílio da pessoa natural', 'ânimo definitivo.', 'CC, art. 70'),
       (CC + '71', 'Se, porém, a pessoa natural tiver diversas residências', 'qualquer delas.', 'CC, art. 71')],
  kw=['ânimo definitivo', 'pluralidade de domicílios'])

# ---------------- PONTO 1 — RODADA 2
I(P, 2, 'Domicílio necessário do preso',
  'O preso tem domicílio necessário, que é o do lugar em que o crime foi cometido.', 'E',
  'Art. 76, par. ún.: o domicílio do preso é o lugar em que **cumprir a sentença**.',
  lei=[(CC + '76', 'Têm domicílio necessário', 'e o preso.', 'CC, art. 76'),
       (CC + '76', 'e o do preso, o lugar em que cumprir a sentença.', None, 'CC, art. 76, par. ún.')],
  exc=['Incapaz: o do representante ou assistente', 'Servidor público: onde exerce permanentemente suas funções', 'Militar: onde servir (Marinha e Aeronáutica: sede do comando)', 'Marítimo: onde o navio estiver matriculado'],
  kw=['domicílio necessário', 'cumprir a sentença'])
I(P, 2, 'Sucessão provisória do ausente',
  'Decorrido um ano da arrecadação dos bens do ausente, ou três anos, se ele deixou representante ou procurador, os interessados podem requerer que se declare a ausência e se abra provisoriamente a sucessão.', 'C',
  'Art. 26: **1 ano** (sem representante) ou **3 anos** (com representante ou procurador) para a **sucessão provisória**.',
  lei=[(CC + '26', 'Decorrido um ano da arrecadação', 'provisoriamente a sucessão.', 'CC, art. 26')],
  kw=['ausência', 'sucessão provisória'])
I(P, 2, 'Sucessão definitiva do ausente',
  'A sucessão definitiva pode ser requerida cinco anos depois de passada em julgado a sentença que concede a abertura da sucessão provisória.', 'E',
  'Art. 37: são **dez anos** do trânsito da sentença da provisória. Cinco anos aparecem no art. 38, para o ausente que já conta **oitenta anos** de idade.',
  lei=[(CC + '37', 'Dez anos depois de passada em julgado a sentença', None, 'CC, art. 37'),
       (CC + '38', 'Pode-se requerer a sucessão definitiva', 'as últimas notícias dele.', 'CC, art. 38')],
  peg='Misturar o prazo do art. 38 (80 anos de idade + 5 anos de notícias) com o do art. 37 (10 anos).',
  kw=['sucessão definitiva', 'dez anos'])
I(P, 2, 'Biografias não autorizadas',
  'Segundo o STF, a publicação de biografia de pessoa pública depende de consentimento prévio do biografado ou, se falecido, de seus familiares, sob pena de violação aos arts. 20 e 21 do Código Civil.', 'E',
  'Na **ADI 4.815**, o STF deu interpretação conforme aos arts. 20 e 21: é **inexigível o consentimento** para obras biográficas. Abusos se resolvem por **reparação**, não por censura prévia.',
  juris=[J['ADI4815']],
  kw=['biografias', 'inexigível o consentimento'])
I(P, 2, 'Direito ao esquecimento',
  'O STF reconheceu, em repercussão geral, a existência de um direito ao esquecimento, que permite à vítima ou aos familiares impedir a divulgação de fatos verídicos em razão da passagem do tempo.', 'E',
  'No **Tema 786** o STF declarou **incompatível com a Constituição** a ideia de direito ao esquecimento. Excessos são analisados **caso a caso** (honra, imagem, privacidade).',
  juris=[J['RG786']],
  kw=['direito ao esquecimento', 'Tema 786'])
I(P, 2, 'Pessoa jurídica e direitos da personalidade',
  'Aplica-se às pessoas jurídicas, no que couber, a proteção dos direitos da personalidade, e a pessoa jurídica pode sofrer dano moral.', 'C',
  'Art. 52 + **Súmula 227/STJ**: a pessoa jurídica tem **honra objetiva** (reputação), passível de dano moral.',
  lei=[(CC + '52', 'Aplica-se às pessoas jurídicas', 'direitos da personalidade.', 'CC, art. 52')],
  juris=[J['S227']],
  kw=['honra objetiva', 'dano moral'])
I(P, 2, 'Desconsideração: encerramento irregular e grupo econômico',
  'Nas relações civis e empresariais, o encerramento irregular das atividades da sociedade, somado à inexistência de bens penhoráveis, basta para a desconsideração da personalidade jurídica.', 'E',
  'O STJ (**Tema 1.210**) reafirmou a **teoria maior**: é preciso provar **abuso** (desvio de finalidade ou confusão patrimonial). Pelo art. 50, § 4º, nem a mera existência de grupo econômico autoriza a medida.',
  lei=[(CC + '50', 'A mera existência de grupo econômico', 'não autoriza a desconsideração da personalidade da pessoa jurídica.', 'CC, art. 50, § 4º')],
  juris=[J['T1210']],
  exc=['No CDC (art. 28, § 5º) vale a teoria menor: basta que a personalidade seja obstáculo ao ressarcimento do consumidor'],
  kw=['teoria maior', 'encerramento irregular'])
I(P, 2, 'Criação de fundação',
  'Para criar uma fundação, o instituidor fará, por escritura pública ou testamento, dotação especial de bens livres, especificando o fim a que se destina e declarando, se quiser, a maneira de administrá-la.', 'C',
  'Art. 62: **escritura pública ou testamento** + **dotação de bens livres** + **finalidade**. O Ministério Público velará pelas fundações (art. 66).',
  lei=[(CC + '62', 'Para criar uma fundação', 'a maneira de administrá-la.', 'CC, art. 62')],
  kw=['fundação', 'dotação especial de bens livres'])
I(P, 2, 'Associações',
  'Constituem-se as associações pela união de pessoas que se organizem para fins não econômicos, não havendo, entre os associados, direitos e obrigações recíprocos.', 'C',
  'Art. 53 e parágrafo único: **fins não econômicos** e **ausência de direitos e obrigações recíprocos** entre associados.',
  lei=[(CC + '53', 'Constituem-se as associações', 'fins não econômicos.', 'CC, art. 53'),
       (CC + '53', 'Não há, entre os associados, direitos e obrigações recíprocos.', None, 'CC, art. 53, par. ún.')],
  kw=['associações', 'fins não econômicos'])

P = 'DBA26-CIV-2'
# ---------------- PONTO 2 · Dos bens — RODADA 1
I(P, 1, 'Bens imóveis',
  'São bens imóveis o solo e tudo quanto se lhe incorporar natural ou artificialmente.', 'C',
  'Literalidade do art. 79: **solo** + **incorporação natural ou artificial**.',
  lei=[(CC + '79', 'São bens imóveis o solo', 'natural ou artificialmente.', 'CC, art. 79')],
  kw=['bens imóveis', 'solo'])
I(P, 1, 'Imóveis por determinação legal',
  'Consideram-se imóveis para os efeitos legais os direitos reais sobre imóveis e as ações que os asseguram, bem como o direito à sucessão aberta.', 'C',
  'Art. 80: imóveis **por determinação legal** — direitos reais sobre imóveis e ações que os asseguram; **direito à sucessão aberta**.',
  lei=[(CC + '80', 'Consideram-se imóveis para os efeitos legais', 'o direito à sucessão aberta.', 'CC, art. 80')],
  kw=['determinação legal', 'sucessão aberta'])
I(P, 1, 'Materiais separados provisoriamente',
  'Perdem o caráter de imóveis os materiais provisoriamente separados de um prédio, para nele se reempregarem.', 'E',
  'Art. 81, II: esses materiais **não perdem** o caráter de imóveis. O mesmo vale para edificações separadas do solo que, conservando sua unidade, forem removidas para outro local.',
  lei=[(CC + '81', 'Não perdem o caráter de imóveis', 'para nele se reempregarem.', 'CC, art. 81')],
  exc=['Os materiais provenientes de demolição readquirem a qualidade de móveis (art. 84)'],
  kw=['não perdem o caráter de imóveis', 'reempregarem'])
I(P, 1, 'Móveis por determinação legal',
  'Consideram-se móveis para os efeitos legais as energias que tenham valor econômico, os direitos reais sobre objetos móveis e as ações correspondentes, e os direitos pessoais de caráter patrimonial e respectivas ações.', 'C',
  'Art. 83: **energias com valor econômico**, direitos reais sobre móveis e **direitos pessoais patrimoniais**.',
  lei=[(CC + '83', 'Consideram-se móveis para os efeitos legais', 'respectivas ações.', 'CC, art. 83')],
  kw=['energias', 'direitos pessoais de caráter patrimonial'])
I(P, 1, 'Bens fungíveis',
  'São fungíveis os móveis que podem substituir-se por outros da mesma espécie, qualidade e quantidade.', 'C',
  'Art. 85: **fungibilidade** é a substituição por outro da **mesma espécie, qualidade e quantidade**; o CC a refere aos móveis.',
  lei=[(CC + '85', 'São fungíveis os móveis', 'qualidade e quantidade.', 'CC, art. 85')],
  kw=['fungíveis'])
I(P, 1, 'Indivisibilidade',
  'Os bens naturalmente divisíveis não podem tornar-se indivisíveis, nem por determinação da lei, nem por vontade das partes.', 'E',
  'Art. 88: os bens naturalmente divisíveis **podem** tornar-se indivisíveis **por determinação da lei ou por vontade das partes**.',
  lei=[(CC + '88', 'Os bens naturalmente divisíveis', 'vontade das partes.', 'CC, art. 88')],
  kw=['indivisíveis', 'vontade das partes'])
I(P, 1, 'Pertenças',
  'Os negócios jurídicos que dizem respeito ao bem principal abrangem as pertenças, salvo se o contrário resultar da lei ou da manifestação de vontade.', 'E',
  'Art. 94: a regra é o inverso — os negócios sobre o principal **não abrangem as pertenças**, salvo se o contrário resultar da lei, da manifestação de vontade ou das circunstâncias do caso. Pertença não segue o principal automaticamente.',
  lei=[(CC + '94', 'Os negócios jurídicos que dizem respeito ao bem principal', 'circunstâncias do caso.', 'CC, art. 94')],
  peg='A AOCP já cobrou o art. 94 trocando "não abrangem" por "abrangem".',
  kw=['pertenças', 'não abrangem'])
I(P, 1, 'Bem principal e acessório',
  'Principal é o bem que existe sobre si, abstrata ou concretamente; acessório, aquele cuja existência supõe a do principal.', 'C',
  'Art. 92: definição de **principal** e **acessório**.',
  lei=[(CC + '92', 'Principal é o bem que existe sobre si', 'supõe a do principal.', 'CC, art. 92')],
  kw=['principal', 'acessório'])
I(P, 1, 'Espécies de benfeitorias',
  'São necessárias as benfeitorias que aumentam ou facilitam o uso do bem, e úteis as que têm por fim conservá-lo ou evitar que se deteriore.', 'E',
  'Art. 96 inverteu-se: **úteis** aumentam ou facilitam o uso; **necessárias** conservam ou evitam a deterioração; **voluptuárias** são de mero deleite ou recreio.',
  lei=[(CC + '96', 'São voluptuárias as de mero deleite', 'evitar que se deteriore.', 'CC, art. 96, §§ 1º a 3º')],
  peg='Trocar as definições de úteis e necessárias.',
  kw=['benfeitorias', 'necessárias', 'úteis'])
I(P, 1, 'Classificação dos bens públicos',
  'Os edifícios ou terrenos destinados a serviço ou estabelecimento da administração federal, estadual ou municipal, inclusive de suas autarquias, são bens dominicais.', 'E',
  'Art. 99, II: são bens de **uso especial**. **Dominicais** são os que constituem o patrimônio das pessoas jurídicas de direito público, como objeto de direito pessoal ou real (inciso III).',
  lei=[(CC + '99', 'II - os de uso especial', 'inclusive os de suas autarquias;', 'CC, art. 99, II')],
  peg='A AOCP já cobrou o art. 99, II; a troca entre uso especial e dominical é a clássica.',
  kw=['uso especial', 'dominicais'])
I(P, 1, 'Alienabilidade dos bens públicos e usucapião',
  'Os bens públicos dominicais podem ser alienados, observadas as exigências da lei, mas nenhum bem público está sujeito a usucapião.', 'C',
  'Arts. 101 e 102: **dominicais são alienáveis** (observada a lei); uso comum e especial são inalienáveis enquanto conservarem a qualificação. **Nenhum bem público** é usucapível (Súmula 340/STF).',
  lei=[(CC + '101', 'Os bens públicos dominicais podem ser alienados', 'exigências da lei.', 'CC, art. 101'),
       (CC + '102', 'Os bens públicos não estão sujeitos a usucapião.', None, 'CC, art. 102')],
  juris=[J['STF340']],
  kw=['dominicais', 'usucapião'])

# ---------------- PONTO 2 — RODADA 2
I(P, 2, 'Acréscimos sem intervenção humana',
  'Consideram-se benfeitorias os melhoramentos ou acréscimos sobrevindos ao bem sem a intervenção do proprietário, possuidor ou detentor.', 'E',
  'Art. 97: esses acréscimos **não se consideram benfeitorias** (são, por exemplo, acessões naturais). Benfeitoria pressupõe obra humana.',
  lei=[(CC + '97', 'Não se consideram benfeitorias', 'possuidor ou detentor.', 'CC, art. 97')],
  kw=['benfeitorias', 'sem a intervenção'])
I(P, 2, 'Frutos e produtos',
  'Apesar de ainda não separados do bem principal, os frutos e produtos podem ser objeto de negócio jurídico.', 'C',
  'Art. 95: **frutos e produtos** pendentes podem ser negociados (ex.: venda de safra futura).',
  lei=[(CC + '95', 'Apesar de ainda não separados', 'objeto de negócio jurídico.', 'CC, art. 95')],
  kw=['frutos', 'produtos'])
I(P, 2, 'Uso comum retribuído',
  'O uso comum dos bens públicos é sempre gratuito, vedada a cobrança de qualquer retribuição.', 'E',
  'Art. 103: o uso comum **pode ser gratuito ou retribuído**, conforme estabelecido legalmente pela entidade a cuja administração pertencerem (ex.: pedágio).',
  lei=[(CC + '103', 'O uso comum dos bens públicos pode ser gratuito ou retribuído', None, 'CC, art. 103')],
  kw=['uso comum', 'retribuído'])
I(P, 2, 'Materiais de construção e demolição',
  'Os materiais destinados a alguma construção, enquanto não forem empregados, conservam sua qualidade de móveis; readquirem essa qualidade os provenientes da demolição de algum prédio.', 'C',
  'Art. 84: a **destinação** não imobiliza o material; a **demolição** o torna móvel de novo.',
  lei=[(CC + '84', 'Os materiais destinados a alguma construção', 'demolição de algum prédio.', 'CC, art. 84')],
  kw=['materiais', 'demolição'])
I(P, 2, 'Vaga de garagem e bem de família',
  'A vaga de garagem com matrícula própria no registro de imóveis integra o bem de família e é, por isso, impenhorável.', 'E',
  '**Súmula 449/STJ**: a vaga com **matrícula própria** **não** constitui bem de família para efeito de penhora.',
  juris=[J['S449']],
  kw=['vaga de garagem', 'matrícula própria'])
I(P, 2, 'Imóvel único locado a terceiros',
  'É impenhorável o único imóvel residencial do devedor que esteja locado a terceiros, desde que a renda obtida com a locação seja revertida para a subsistência ou a moradia da sua família.', 'C',
  '**Súmula 486/STJ**: a proteção acompanha a **finalidade** — a renda tem de voltar para a **subsistência ou moradia** da família. A Súmula 364 estende a proteção a solteiros, separados e viúvos.',
  juris=[J['S486'], J['S364']],
  kw=['bem de família', 'locado a terceiros'])
I(P, 2, 'Fiador de locação comercial',
  'O STF firmou que é inconstitucional a penhora do bem de família do fiador quando a fiança garante contrato de locação comercial, por ofensa ao direito à moradia.', 'E',
  'No **Tema 1.127/RG**, o STF decidiu que é **constitucional** a penhora do bem de família do fiador **seja a locação residencial, seja comercial**. No STJ, a Súmula 549 já validava a penhora.',
  juris=[J['RG1127'], J['S549']],
  kw=['fiador', 'locação comercial'])
I(P, 2, 'Bens dominicais por estrutura de direito privado',
  'Não dispondo a lei em contrário, consideram-se dominicais os bens pertencentes às pessoas jurídicas de direito público a que se tenha dado estrutura de direito privado.', 'C',
  'Art. 99, parágrafo único: regra residual de classificação como **dominicais**.',
  lei=[(CC + '99', 'Não dispondo a lei em contrário, consideram-se dominicais', 'estrutura de direito privado.', 'CC, art. 99, par. ún.')],
  kw=['dominicais', 'estrutura de direito privado'])

P = 'DBA26-CIV-3'
# ---------------- PONTO 3 · Dos fatos jurídicos — RODADA 1
I(P, 1, 'Requisitos de validade do negócio jurídico',
  'A validade do negócio jurídico requer agente capaz, objeto lícito, possível, determinado ou determinável, e forma prescrita ou não defesa em lei.', 'C',
  'Art. 104: **agente capaz**, **objeto** lícito, possível, determinado ou determinável, **forma** prescrita ou não proibida.',
  lei=[(CC + '104', 'A validade do negócio jurídico requer', 'não defesa em lei.', 'CC, art. 104')],
  kw=['validade', 'agente capaz', 'objeto lícito'])
I(P, 1, 'Escritura pública',
  'Não dispondo a lei em contrário, a escritura pública é essencial à validade dos negócios jurídicos que visem à constituição, transferência, modificação ou renúncia de direitos reais sobre imóveis de valor superior a quarenta vezes o maior salário mínimo vigente no País.', 'E',
  'Art. 108: o limite é de **trinta vezes** o maior salário mínimo.',
  lei=[(CC + '108', 'Não dispondo a lei em contrário, a escritura pública', 'salário mínimo vigente no País.', 'CC, art. 108')],
  peg='Troca do múltiplo (30 → 40).',
  kw=['escritura pública', 'trinta vezes'])
I(P, 1, 'Reserva mental',
  'A manifestação de vontade subsiste ainda que o seu autor haja feito a reserva mental de não querer o que manifestou, salvo se dela o destinatário tinha conhecimento.', 'C',
  'Art. 110: a **reserva mental** desconhecida é irrelevante; conhecida pelo destinatário, a manifestação não subsiste.',
  lei=[(CC + '110', 'A manifestação de vontade subsiste', 'o destinatário tinha conhecimento.', 'CC, art. 110')],
  kw=['reserva mental'])
I(P, 1, 'Silêncio',
  'No direito civil brasileiro, o silêncio jamais importa anuência, pois toda declaração de vontade deve ser expressa.', 'E',
  'Art. 111: o **silêncio importa anuência** quando as **circunstâncias ou os usos** o autorizarem e não for necessária a declaração de vontade expressa.',
  lei=[(CC + '111', 'O silêncio importa anuência', 'declaração de vontade expressa.', 'CC, art. 111')],
  kw=['silêncio', 'anuência'])
I(P, 1, 'Erro substancial',
  'São anuláveis os negócios jurídicos quando as declarações de vontade emanarem de erro substancial que poderia ser percebido por pessoa de diligência normal, em face das circunstâncias do negócio.', 'C',
  'Art. 138: **erro substancial** + **cognoscibilidade** (percebível por pessoa de diligência normal) → **anulabilidade**.',
  lei=[(CC + '138', 'São anuláveis os negócios jurídicos', 'circunstâncias do negócio.', 'CC, art. 138')],
  kw=['erro substancial', 'anuláveis'])
I(P, 1, 'Dolo acidental',
  'O dolo acidental, assim entendido aquele sem o qual o negócio seria realizado, embora por outro modo, torna o negócio jurídico anulável.', 'E',
  'Art. 146: o **dolo acidental** só obriga à **satisfação das perdas e danos**. Anulável é o negócio quando o dolo for a sua **causa** (dolo essencial, art. 145).',
  lei=[(CC + '145', 'São os negócios jurídicos anuláveis por dolo', 'for a sua causa.', 'CC, art. 145'),
       (CC + '146', 'O dolo acidental só obriga', 'embora por outro modo.', 'CC, art. 146')],
  kw=['dolo acidental', 'perdas e danos'])
I(P, 1, 'Temor reverencial',
  'O simples temor reverencial configura coação apta a viciar a declaração de vontade.', 'E',
  'Art. 153: **não se considera coação** a ameaça do exercício normal de um direito, **nem o simples temor reverencial**.',
  lei=[(CC + '153', 'Não se considera coação', 'simples temor reverencial.', 'CC, art. 153')],
  kw=['temor reverencial', 'coação'])
I(P, 1, 'Lesão',
  'Ocorre a lesão quando uma pessoa, sob premente necessidade, ou por inexperiência, se obriga a prestação manifestamente desproporcional ao valor da prestação oposta.', 'C',
  'Art. 157: **premente necessidade ou inexperiência** + **desproporção manifesta**. Não se exige dolo de aproveitamento da outra parte.',
  lei=[(CC + '157', 'Ocorre a lesão quando uma pessoa', 'valor da prestação oposta.', 'CC, art. 157')],
  exc=['Não se decreta a anulação se for oferecido suplemento suficiente, ou se a parte favorecida concordar com a redução do proveito (art. 157, § 2º)'],
  kw=['lesão', 'premente necessidade', 'inexperiência'])
I(P, 1, 'Simulação',
  'É anulável o negócio jurídico simulado, mas subsistirá o que se dissimulou, se válido for na substância e na forma.', 'E',
  'Art. 167: o negócio simulado é **nulo** (e não anulável). Subsiste o **dissimulado**, se válido na substância e na forma.',
  lei=[(CC + '167', 'É nulo o negócio jurídico simulado', 'na substância e na forma.', 'CC, art. 167')],
  peg='Simulação deixou de ser causa de anulabilidade com o CC/2002 — virou nulidade.',
  kw=['simulação', 'nulo'])
I(P, 1, 'Negócio nulo',
  'O negócio jurídico nulo não é suscetível de confirmação, nem convalesce pelo decurso do tempo.', 'C',
  'Art. 169: nulidade **não se confirma** e **não convalesce**. A anulabilidade, ao contrário, admite confirmação (art. 172).',
  lei=[(CC + '169', 'O negócio jurídico nulo não é suscetível de confirmação', 'decurso do tempo.', 'CC, art. 169')],
  kw=['nulo', 'confirmação', 'convalesce'])
I(P, 1, 'Prazo geral de prescrição',
  'Violado o direito, nasce para o titular a pretensão, que se extingue pela prescrição; quando a lei não fixar prazo menor, a prescrição ocorre em quinze anos.', 'E',
  'Arts. 189 e 205: o prazo geral do CC/2002 é de **dez anos** (o de 15 anos é da usucapião extraordinária).',
  lei=[(CC + '189', 'Violado o direito, nasce para o titular a pretensão', None, 'CC, art. 189'),
       (CC + '205', 'A prescrição ocorre em dez anos', 'prazo menor.', 'CC, art. 205')],
  kw=['prescrição', 'dez anos'])
I(P, 1, 'Renúncia à prescrição',
  'A renúncia da prescrição pode ser expressa ou tácita, e só valerá sendo feita, sem prejuízo de terceiro, depois que a prescrição se consumar.', 'C',
  'Art. 191: **só depois de consumada** e **sem prejuízo de terceiro**; tácita quando o interessado pratica fatos incompatíveis com a prescrição.',
  lei=[(CC + '191', 'A renúncia da prescrição pode ser expressa ou tácita', 'a prescrição se consumar', 'CC, art. 191')],
  kw=['renúncia da prescrição'])

# ---------------- PONTO 3 — RODADA 2
I(P, 2, 'Estado de perigo',
  'Configura-se o estado de perigo quando alguém, premido da necessidade de salvar-se, ou a pessoa de sua família, de grave dano conhecido pela outra parte, assume obrigação excessivamente onerosa.', 'C',
  'Art. 156: diferente da lesão, o **estado de perigo** exige que o grave dano seja **conhecido pela outra parte** (dolo de aproveitamento).',
  lei=[(CC + '156', 'Configura-se o estado de perigo', 'excessivamente onerosa.', 'CC, art. 156')],
  exc=['Tratando-se de pessoa não pertencente à família do declarante, o juiz decide segundo as circunstâncias (art. 156, par. ún.)'],
  kw=['estado de perigo', 'grave dano conhecido'])
I(P, 2, 'Prazo para anular por coação',
  'É de quatro anos o prazo de decadência para pleitear a anulação do negócio jurídico, contado, no caso de coação, do dia em que se realizou o negócio.', 'E',
  'Art. 178: na **coação**, os 4 anos contam **do dia em que ela cessar**. Do dia do negócio contam erro, dolo, fraude contra credores, estado de perigo e lesão; do incapaz, do dia em que cessar a incapacidade.',
  lei=[(CC + '178', 'É de quatro anos o prazo de decadência', 'do dia em que ela cessar;', 'CC, art. 178, caput e I')],
  kw=['quatro anos', 'coação', 'decadência'])
I(P, 2, 'Prazo supletivo de anulação',
  'Quando a lei dispuser que determinado ato é anulável, sem estabelecer prazo para pleitear-se a anulação, será este de dois anos, a contar da data da conclusão do ato.', 'C',
  'Art. 179: prazo **supletivo de 2 anos** da conclusão do ato.',
  lei=[(CC + '179', 'Quando a lei dispuser que determinado ato é anulável', 'conclusão do ato.', 'CC, art. 179')],
  kw=['dois anos', 'anulável'])
I(P, 2, 'Reparação civil',
  'Prescreve em três anos a pretensão de reparação civil.', 'C',
  'Art. 206, § 3º, V: **3 anos** para a **reparação civil** extracontratual.',
  lei=[(CC + '206', 'V - a pretensão de reparação civil;', None, 'CC, art. 206, § 3º, V')],
  exc=['Fato do produto ou do serviço nas relações de consumo: 5 anos (CDC, art. 27)', 'Segurado contra segurador: 1 ano (art. 206, § 1º, II)'],
  kw=['reparação civil', 'três anos'])
I(P, 2, 'Causas que impedem a prescrição',
  'Não corre a prescrição contra os relativamente incapazes, entre eles os maiores de dezesseis e menores de dezoito anos.', 'E',
  'Art. 198, I: não corre contra os **absolutamente** incapazes (art. 3º). Contra o relativamente incapaz corre; ele tem ação contra o assistente que der causa à prescrição (art. 195).',
  lei=[(CC + '198', 'Também não corre a prescrição', 'I - contra os incapazes de que trata o art. 3', 'CC, art. 198, I')],
  kw=['absolutamente incapazes', 'não corre'])
I(P, 2, 'Interrupção da prescrição',
  'A interrupção da prescrição pode ocorrer quantas vezes forem necessárias, desde que por causas diversas.', 'E',
  'Art. 202, caput: a interrupção **somente poderá ocorrer uma vez**.',
  lei=[(CC + '202', 'A interrupção da prescrição, que somente poderá ocorrer uma vez', None, 'CC, art. 202')],
  kw=['interrupção', 'uma vez'])
I(P, 2, 'Decadência e causas suspensivas',
  'Salvo disposição legal em contrário, não se aplicam à decadência as normas que impedem, suspendem ou interrompem a prescrição.', 'C',
  'Art. 207: a decadência, em regra, **corre sem pausa**.',
  lei=[(CC + '207', 'Salvo disposição legal em contrário', 'interrompem a prescrição.', 'CC, art. 207')],
  exc=['Não corre a decadência contra os absolutamente incapazes (art. 208 c/c art. 198, I)'],
  kw=['decadência', 'não se aplicam'])
I(P, 2, 'Decadência convencional',
  'Deve o juiz, de ofício, conhecer da decadência, seja ela legal ou convencional.', 'E',
  'Arts. 210 e 211: o juiz conhece de ofício a decadência **legal**; a **convencional** pode ser alegada pela parte a quem aproveita, mas o juiz **não pode suprir a alegação**.',
  lei=[(CC + '210', 'Deve o juiz, de ofício, conhecer da decadência, quando estabelecida por lei.', None, 'CC, art. 210'),
       (CC + '211', 'Se a decadência for convencional', 'não pode suprir a alegação.', 'CC, art. 211')],
  kw=['decadência convencional', 'de ofício'])
I(P, 2, 'Alteração convencional dos prazos',
  'Os prazos de prescrição podem ser ampliados ou reduzidos por acordo das partes, desde que por escrito.', 'E',
  'Art. 192: os prazos de prescrição **não podem ser alterados por acordo das partes**. Já a decadência pode ser convencional.',
  lei=[(CC + '192', 'Os prazos de prescrição não podem ser alterados por acordo das partes.', None, 'CC, art. 192')],
  kw=['prazos de prescrição', 'não podem ser alterados'])
I(P, 2, 'Pedido à seguradora',
  'O pedido do pagamento de indenização à seguradora suspende o prazo de prescrição até que o segurado tenha ciência da decisão.', 'C',
  '**Súmula 229/STJ**: é causa de **suspensão** (não de interrupção). Lembre ainda: segurado em grupo contra seguradora, **1 ano** (Súmula 101/STJ).',
  juris=[J['S229'], J['S101']],
  kw=['seguradora', 'suspende'])
