# Pente Fino de Legislação Penal Extravagante — LPE-1 (Estatuto do Desarmamento), LPE-2 (crimes hediondos),
# LPE-3 (Lei 7.716/1989), LPE-4 (abuso de autoridade) e LPE-5 (tortura) (08/11/2026).
from base import I
from lpe_juris import J

AR = 'L10826:'
HD = 'L8072:'
RC = 'L7716:'
AB = 'L13869:'
TT = 'L9455:'
LEP = 'L7210:'

# ======================= LPE-1 · Estatuto do Desarmamento =======================
P = 'DBA26-LPE-1'
I(P, 1, 'Posse no local de trabalho',
  'Comete posse irregular de arma de fogo de uso permitido, e não porte, quem a mantém em desacordo com a lei no seu local de trabalho, desde que seja o titular ou o responsável legal do estabelecimento.', 'C',
  'Art. 12: a **posse irregular** abrange residência e local de trabalho do **titular ou responsável legal**; o empregado que guarda a arma no serviço responde por **porte** (art. 14).',
  lei=[(AR + '12', 'no seu local de trabalho, desde que seja o titular ou o responsável legal do estabelecimento ou empresa', None, 'Lei 10.826/2003, art. 12')],
  kw=['posse irregular', 'titular ou o responsável legal'])
I(P, 1, 'Pena do porte de uso permitido',
  'O porte ilegal de arma de fogo de uso permitido é punido com detenção, de 1 a 3 anos, e multa, como a posse irregular.', 'E',
  'Art. 14: **reclusão, de 2 a 4 anos**, e multa. A pena de detenção de 1 a 3 anos é a da **posse** (art. 12).',
  lei=[(AR + '14', 'Pena – reclusão, de 2 (dois) a 4 (quatro) anos, e multa.', None, 'Lei 10.826/2003, art. 14, pena')],
  peg='Igualar posse e porte.', kw=['porte ilegal', 'reclusão'])
I(P, 1, 'Numeração raspada',
  'Quem porta arma de fogo de uso permitido com numeração raspada responde pelas penas do art. 16 do Estatuto, e não pelas do art. 14.', 'C',
  'Art. 16, § 1º, IV: a arma com **numeração raspada**, suprimida ou adulterada leva à pena do uso restrito (3 a 6 anos), seja qual for o calibre.',
  lei=[(AR + '16', 'IV – portar, possuir, adquirir, transportar ou fornecer arma de fogo com numeração, marca ou qualquer outro sinal de identificação raspado, suprimido ou adulterado;', None, 'Lei 10.826/2003, art. 16, § 1º, IV')],
  kw=['numeração raspada', 'art. 16, § 1º, IV'])
I(P, 1, 'Arma de uso proibido',
  'A posse ou o porte de arma de fogo de uso proibido sujeita o agente à mesma pena prevista para a arma de uso restrito, de 3 a 6 anos de reclusão.', 'E',
  'Art. 16, § 2º (Lei 13.964/2019): com **arma de uso proibido**, a pena é de **reclusão, de 4 a 12 anos**.',
  lei=[(AR + '16', '§ 2º Se as condutas descritas no caput e no § 1º deste artigo envolverem arma de fogo de uso proibido, a pena é de reclusão, de 4 (quatro) a 12 (doze) anos.', None, 'Lei 10.826/2003, art. 16, § 2º')],
  peg='Ignorar a forma qualificada do § 2º.', kw=['uso proibido', '4 a 12 anos'])
I(P, 1, 'Hediondez da arma de uso restrito',
  'A posse ou o porte ilegal de arma de fogo de uso restrito é crime hediondo, por força da Lei 8.072/1990.', 'E',
  'A Lei 8.072/1990 (art. 1º, par. ún., II) só faz **hediondo** o art. 16 quando a arma é de **uso proibido**; também são hediondos o comércio ilegal (art. 17) e o tráfico internacional (art. 18).',
  lei=[(HD + '1', 'II - o crime de posse ou porte ilegal de arma de fogo de uso proibido, previsto no art. 16 da Lei nº 10.826, de 22 de dezembro de 2003;', None, 'Lei 8.072/1990, art. 1º, par. ún., II')],
  peg='Estender a hediondez ao uso restrito.', kw=['hediondo', 'uso proibido'])
I(P, 1, 'Súmula 668/STJ',
  'Não é hediondo o porte ou a posse de arma de fogo de uso permitido, ainda que com numeração raspada, suprimida ou adulterada.', 'C',
  '**Súmula 668/STJ** (18/04/2024): a equiparação de pena do art. 16, § 1º, IV, não transporta a hediondez, que a lei reserva à arma de **uso proibido**.',
  juris=[J['S668']], kw=['Súmula 668/STJ', 'não é hediondo'])
I(P, 1, 'Arma a serviço do tráfico (2026)',
  'Nos crimes de posse e de porte de arma de fogo, a pena é aumentada da metade se o crime for praticado em concurso com crime da Lei de Drogas ou se a arma assegurar o sucesso da mercancia.', 'E',
  'Art. 21-A (incluído pela **Lei 15.358/2026**): o aumento é de **2/3** e alcança os arts. 12, 14 e 16. O aumento de metade é o do art. 20 (agente de órgão de segurança ou reincidente específico).',
  lei=[(AR + '21-A', 'Nos crimes previstos nos arts. 12, 14 e 16 desta Lei, a pena é aumentada de 2/3 (dois terços)', None, 'Lei 10.826/2003, art. 21-A')],
  peg='Trocar 2/3 por metade.', kw=['Lei 15.358/2026', '2/3'])
I(P, 1, 'Disparo de arma de fogo',
  'O disparo de arma de fogo em via pública só configura o crime do art. 15 do Estatuto se a conduta não tiver como finalidade a prática de outro crime.', 'C',
  'Art. 15: tipo **expressamente subsidiário** — se o disparo visa a outro crime (ex.: homicídio tentado), este o absorve.',
  lei=[(AR + '15', 'desde que essa conduta não tenha como finalidade a prática de outro crime', None, 'Lei 10.826/2003, art. 15')],
  kw=['subsidiário', 'disparo'])
I(P, 1, 'Porte e embriaguez',
  'A autorização de porte de arma de fogo de uso permitido perde automaticamente a eficácia se o portador for detido ou abordado em estado de embriaguez.', 'C',
  'Art. 10, § 2º: a **perda automática** da eficácia alcança também quem esteja sob efeito de substâncias químicas ou alucinógenas.',
  lei=[(AR + '10', 'perderá automaticamente sua eficácia caso o portador dela seja detido ou abordado em estado de embriaguez', None, 'Lei 10.826/2003, art. 10, § 2º')],
  kw=['perda automática', 'embriaguez'])
# --- LPE-1 · Rodada 2
I(P, 2, 'Omissão de cautela',
  'Comete o crime de omissão de cautela quem deixa de observar as cautelas necessárias para impedir que menor de 14 anos se apodere de arma de fogo que esteja sob sua posse.', 'E',
  'Art. 13: o tipo protege o **menor de 18 anos** ou a pessoa com deficiência mental; é o único crime **culposo** do Estatuto (detenção, de 1 a 2 anos, e multa).',
  lei=[(AR + '13', 'Deixar de observar as cautelas necessárias para impedir que menor de 18 (dezoito) anos ou pessoa portadora de deficiência mental se apodere de arma de fogo', None, 'Lei 10.826/2003, art. 13')],
  peg='Trocar 18 por 14 anos.', kw=['omissão de cautela', 'menor de 18'])
I(P, 2, 'Agente policial disfarçado',
  'Incorre nas penas do comércio ilegal de arma de fogo quem vende arma a agente policial disfarçado, quando presentes elementos probatórios razoáveis de conduta criminal preexistente.', 'C',
  'Art. 17, § 2º (Lei 13.964/2019): a figura do **agente policial disfarçado** exige **conduta criminal preexistente**, o que a distingue do flagrante preparado (Súmula 145/STF).',
  lei=[(AR + '17', 'a agente policial disfarçado, quando presentes elementos probatórios razoáveis de conduta criminal preexistente', None, 'Lei 10.826/2003, art. 17, § 2º')],
  kw=['agente policial disfarçado', 'conduta criminal preexistente'])
I(P, 2, 'Aumento do art. 20',
  'Nos crimes de porte, disparo, posse de uso restrito, comércio ilegal e tráfico internacional de arma, a pena é aumentada da metade se o agente for reincidente específico em crimes dessa natureza.', 'C',
  'Art. 20, II (Lei 13.964/2019); o inciso I aumenta a pena quando o crime é praticado por integrante dos órgãos e empresas dos arts. 6º, 7º e 8º.',
  lei=[(AR + '20', 'II - o agente for reincidente específico em crimes dessa natureza.', None, 'Lei 10.826/2003, art. 20, II')],
  kw=['reincidente específico', 'metade'])
I(P, 2, 'Abolitio criminis temporária',
  'A abolitio criminis temporária do Estatuto do Desarmamento alcança a posse de arma de uso permitido com numeração raspada praticada até 31/12/2009.', 'E',
  '**Súmula 513/STJ**: para a numeração raspada, a vacatio vale só para a posse praticada **até 23/10/2005**.',
  juris=[J['S513']], peg='Esticar o prazo da numeração raspada.', kw=['Súmula 513/STJ', '23/10/2005'])
I(P, 2, 'Tráfico internacional de arma',
  'O tráfico internacional de arma de fogo é punido com reclusão de 4 a 8 anos, e multa.', 'E',
  'Art. 18: **reclusão, de 8 a 16 anos**, e multa (Lei 13.964/2019), com aumento de metade se a arma for de uso proibido ou restrito (art. 19).',
  lei=[(AR + '18', 'Pena - reclusão, de 8 (oito) a 16 (dezesseis) anos, e multa.', None, 'Lei 10.826/2003, art. 18, pena')],
  peg='Reduzir a pena do art. 18.', kw=['tráfico internacional', '8 a 16 anos'])
I(P, 2, 'Residência rural',
  'Para o residente em área rural, considera-se residência ou domicílio, para fins do registro de arma de fogo, toda a extensão do respectivo imóvel rural.', 'C',
  'Art. 5º, § 5º (Lei 13.870/2019): manter a arma em qualquer ponto do imóvel rural é **posse**, não porte.',
  lei=[(AR + '5', 'Aos residentes em área rural, para os fins do disposto no caput deste artigo, considera-se residência ou domicílio toda a extensão do respectivo imóvel rural.', None, 'Lei 10.826/2003, art. 5º, § 5º')],
  kw=['área rural', 'toda a extensão'])

# ======================= LPE-2 · Crimes hediondos =======================
P = 'DBA26-LPE-2'
I(P, 1, 'Vedações do art. 2º',
  'Os crimes hediondos, a tortura, o tráfico de drogas e o terrorismo são insuscetíveis de anistia, graça, indulto, fiança e liberdade provisória.', 'E',
  'Art. 2º: a lei veda **anistia, graça, indulto e fiança**; a vedação da **liberdade provisória** saiu do texto com a Lei 11.464/2007 (cabe liberdade provisória **sem fiança**).',
  lei=[(HD + '2', 'I - anistia, graça e indulto;', None, 'Lei 8.072/1990, art. 2º, I'), (HD + '2', 'II - fiança.', None, 'Lei 8.072/1990, art. 2º, II')],
  peg='Incluir a liberdade provisória.', kw=['liberdade provisória', 'fiança'])
I(P, 1, 'Temporária nos hediondos',
  'Nos crimes hediondos e equiparados, a prisão temporária tem prazo de 30 dias, prorrogável por igual período em caso de extrema e comprovada necessidade.', 'C',
  'Art. 2º, § 4º. Nos demais crimes do rol da Lei 7.960/1989, o prazo é de 5 + 5 dias.',
  lei=[(HD + '2', 'terá o prazo de 30 (trinta) dias, prorrogável por igual período em caso de extrema e comprovada necessidade', None, 'Lei 8.072/1990, art. 2º, § 4º')],
  kw=['prisão temporária', '30 (trinta) dias'])
I(P, 1, 'Feminicídio',
  'O feminicídio, crime autônomo do art. 121-A do Código Penal, integra o rol dos crimes hediondos.', 'C',
  'Lei 8.072/1990, art. 1º, I-B (Lei 14.994/2024): o **feminicídio** deixou de ser qualificadora e virou tipo autônomo, hediondo, com pena de 20 a 40 anos.',
  lei=[('CP:121-A', 'Art. 121-A. Matar mulher por razões da condição do sexo feminino:', None, 'CP, art. 121-A, caput')],
  kw=['feminicídio', 'art. 121-A'])
I(P, 1, 'Tráfico privilegiado',
  'O tráfico de drogas privilegiado (art. 33, § 4º, da Lei 11.343/2006) é equiparado a hediondo, sujeitando-se aos percentuais mais rigorosos de progressão.', 'E',
  '**Súmula Vinculante 63** (2025) e LEP, art. 112, § 5º: o **tráfico privilegiado** **não** é hediondo nem equiparado. A antiga Súmula 512/STJ, em sentido contrário, foi **cancelada**.',
  lei=[(LEP + '112', 'Não se considera hediondo ou equiparado, para os fins deste artigo, o crime de tráfico de drogas previsto no § 4º do art. 33 da Lei nº 11.343, de 23 de agosto de 2006.', None, 'LEP, art. 112, § 5º')],
  juris=[J['SV63']], peg='Ressuscitar a Súmula 512/STJ.', kw=['Súmula Vinculante 63', 'tráfico privilegiado'])
I(P, 1, 'Tentativa',
  'Só o crime hediondo consumado recebe o tratamento da Lei 8.072/1990; a forma tentada fica fora do rol.', 'E',
  'Art. 1º, caput: são hediondos os crimes do rol, **consumados ou tentados**.',
  lei=[(HD + '1', 'todos tipificados no Decreto-Lei no 2.848, de 7 de dezembro de 1940 - Código Penal, consumados ou tentados', None, 'Lei 8.072/1990, art. 1º, caput')],
  peg='Excluir a tentativa.', kw=['consumados ou tentados'])
I(P, 1, 'Vicaricídio (2026)',
  'O vicaricídio (art. 121-B do Código Penal) foi incluído no rol dos crimes hediondos em 2026.', 'C',
  'Art. 1º, I-C (**Lei 15.384/2026**): o crime praticado contra descendente, ascendente ou pessoa ligada à mulher para atingi-la.',
  lei=[(HD + '1', 'I-C – vicaricídio (art. 121-B);', None, 'Lei 8.072/1990, art. 1º, I-C')],
  kw=['vicaricídio', 'Lei 15.384/2026'])
I(P, 1, 'Roubo hediondo',
  'O roubo majorado pelo concurso de duas ou mais pessoas é crime hediondo.', 'E',
  'Art. 1º, II: só é hediondo o roubo circunstanciado pela **restrição de liberdade** da vítima, pelo **emprego de arma de fogo** (ou de uso proibido ou restrito) e o qualificado por lesão grave ou morte.',
  lei=[(HD + '1', 'a) circunstanciado pela restrição de liberdade da vítima (art. 157, § 2º, inciso V);', None, 'Lei 8.072/1990, art. 1º, II, a')],
  peg='Tornar hediondo todo roubo majorado.', kw=['roubo', 'restrição de liberdade'])
# --- LPE-2 · Rodada 2
I(P, 2, 'Genocídio',
  'O genocídio, tentado ou consumado, é crime hediondo.', 'C',
  'Art. 1º, par. ún., I (Lei 13.964/2019): arts. 1º, 2º e 3º da Lei 2.889/1956.',
  lei=[(HD + '1', 'I - o crime de genocídio, previsto nos arts. 1º, 2º e 3º da Lei nº 2.889, de 1º de outubro de 1956;', None, 'Lei 8.072/1990, art. 1º, par. ún., I')],
  kw=['genocídio'])
I(P, 2, 'Organização criminosa',
  'O crime de organização criminosa é sempre hediondo, qualquer que seja a infração a que se destine.', 'E',
  'Art. 1º, par. ún., V: só quando **direcionado à prática de crime hediondo ou equiparado**. O domínio social estruturado (Lei 15.358/2026) é hediondo por si (inciso VIII).',
  lei=[(HD + '1', 'V - o crime de organização criminosa, quando direcionado à prática de crime hediondo ou equiparado.', None, 'Lei 8.072/1990, art. 1º, par. ún., V')],
  peg='Generalizar a hediondez.', kw=['organização criminosa', 'direcionado'])
I(P, 2, 'Associação para hediondos',
  'A associação criminosa para a prática de crimes hediondos tem pena de 3 a 6 anos de reclusão, e o associado que denunciar o grupo à autoridade, possibilitando seu desmantelamento, tem a pena reduzida de um a dois terços.', 'C',
  'Art. 8º e parágrafo único: forma especial do art. 288 do CP e **delação premiada** de origem.',
  lei=[(HD + '8', 'Será de três a seis anos de reclusão a pena prevista no art. 288 do Código Penal', None, 'Lei 8.072/1990, art. 8º'), (HD + '8', 'possibilitando seu desmantelamento, terá a pena reduzida de um a dois terços', None, 'Lei 8.072/1990, art. 8º, par. ún.')],
  kw=['art. 8º', 'desmantelamento'])
I(P, 2, 'Domínio social estruturado',
  'Os crimes de domínio social estruturado e de favorecimento ao domínio social estruturado, criados pelo marco legal do combate ao crime organizado, são hediondos.', 'C',
  'Art. 1º, par. ún., VIII (**Lei 15.358/2026**).',
  lei=[(HD + '1', 'VIII - os crimes de domínio social estruturado e de favorecimento ao domínio social estruturado', None, 'Lei 8.072/1990, art. 1º, par. ún., VIII')],
  kw=['domínio social estruturado', 'Lei 15.358/2026'])
I(P, 2, 'Crimes do ECA no rol',
  'Entre os crimes do ECA, só a produção de conteúdo de violência sexual contra criança ou adolescente (art. 240) é hedionda; a aquisição ou o armazenamento desse material (art. 241-B) não é.', 'E',
  'Art. 1º, par. ún., VII (redação da **Lei 15.487/2026**): também são hediondos os arts. 241, 241-A, **241-B (caput)**, 241-D e 244-A, nas formas indicadas.',
  lei=[(HD + '1', 'no caput do art. 241-B, no caput e nos §§ 1º e 2º do art. 241-D e no caput e no § 1º do art. 244-A', None, 'Lei 8.072/1990, art. 1º, par. ún., VII')],
  peg='Restringir o rol ao art. 240.', kw=['Lei 15.487/2026', 'art. 241-B'])

# ======================= LPE-3 · Lei 7.716/1989 =======================
P = 'DBA26-LPE-3'
I(P, 1, 'Injúria racial',
  'Injuriar alguém, ofendendo-lhe a dignidade ou o decoro, em razão de raça, cor, etnia ou procedência nacional é crime da Lei 7.716/1989, punido com reclusão, de 2 a 5 anos, e multa.', 'C',
  'Art. 2º-A (Lei 14.532/2023): a **injúria racial** passou a ser espécie de racismo.',
  lei=[(RC + '2-A', 'Injuriar alguém, ofendendo-lhe a dignidade ou o decoro, em razão de raça, cor, etnia ou procedência nacional.', None, 'Lei 7.716/1989, art. 2º-A'), (RC + '2-A', 'Pena: reclusão, de 2 (dois) a 5 (cinco) anos, e multa.', None, 'Lei 7.716/1989, art. 2º-A, pena')],
  kw=['injúria racial', 'art. 2º-A'])
I(P, 1, 'Injúria racial no CP',
  'A injúria em razão de raça ou cor continua tipificada no art. 140, § 3º, do Código Penal, com pena de reclusão de 1 a 3 anos.', 'E',
  'Desde a Lei 14.532/2023 a **injúria racial** está no **art. 2º-A da Lei 7.716/1989** (2 a 5 anos); o § 3º do art. 140 ficou com religião, condição de idoso ou de pessoa com deficiência.',
  lei=[(RC + '2-A', 'Injuriar alguém, ofendendo-lhe a dignidade ou o decoro, em razão de raça, cor, etnia ou procedência nacional.', None, 'Lei 7.716/1989, art. 2º-A')],
  peg='Manter a injúria racial no CP.', kw=['Lei 14.532/2023', 'injúria racial'])
I(P, 1, 'Racismo nas redes sociais',
  'Praticar, induzir ou incitar a discriminação racial por publicação em redes sociais ou na internet é forma qualificada do art. 20, punida com reclusão de 2 a 5 anos e multa.', 'C',
  'Art. 20, § 2º (redação da Lei 14.532/2023).',
  lei=[(RC + '20', 'de publicação em redes sociais, da rede mundial de computadores ou de publicação de qualquer natureza', None, 'Lei 7.716/1989, art. 20, § 2º')],
  kw=['redes sociais', 'art. 20, § 2º'])
I(P, 1, 'Racismo recreativo',
  'Quando os crimes da Lei 7.716/1989 ocorrem em contexto ou com intuito de descontração, diversão ou recreação, a pena é diminuída de um terço.', 'E',
  'Art. 20-A: o **racismo recreativo** **aumenta** a pena de **1/3 até a metade**.',
  lei=[(RC + '20-A', 'terão as penas aumentadas de 1/3 (um terço) até a metade, quando ocorrerem em contexto ou com intuito de descontração, diversão ou recreação', None, 'Lei 7.716/1989, art. 20-A')],
  peg='Tratar a "piada" como atenuante.', kw=['racismo recreativo', 'aumentadas'])
I(P, 1, 'Efeitos da condenação',
  'A perda do cargo do servidor e a suspensão do funcionamento do estabelecimento particular são efeitos automáticos da condenação por racismo.', 'E',
  'Art. 18: os efeitos dos arts. 16 e 17 **não são automáticos** e devem ser **motivadamente declarados** na sentença.',
  lei=[(RC + '18', 'Os efeitos de que tratam os arts. 16 e 17 desta Lei não são automáticos, devendo ser motivadamente declarados na sentença.', None, 'Lei 7.716/1989, art. 18')],
  peg='Tornar automáticos os efeitos.', kw=['não são automáticos'])
I(P, 1, 'Assistência à vítima',
  'Em todos os atos processuais, cíveis e criminais, a vítima dos crimes de racismo deverá estar acompanhada de advogado ou defensor público.', 'C',
  'Art. 20-D (Lei 14.532/2023).',
  lei=[(RC + '20-D', 'Em todos os atos processuais, cíveis e criminais, a vítima dos crimes de racismo deverá estar acompanhada de advogado ou defensor público.', None, 'Lei 7.716/1989, art. 20-D')],
  kw=['advogado ou defensor público', 'vítima'])
# --- LPE-3 · Rodada 2
I(P, 2, 'Injúria racial em concurso',
  'A pena da injúria racial é aumentada de metade se o crime for cometido mediante concurso de 2 ou mais pessoas.', 'C',
  'Art. 2º-A, parágrafo único.',
  lei=[(RC + '2-A', 'A pena é aumentada de metade se o crime for cometido mediante concurso de 2 (duas) ou mais pessoas.', None, 'Lei 7.716/1989, art. 2º-A, par. ún.')],
  kw=['concurso de 2', 'metade'])
I(P, 2, 'Suástica',
  'Veicular propaganda que utilize a cruz suástica ou gamada, para fins de divulgação do nazismo, é crime punido com reclusão de 2 a 5 anos e multa.', 'C',
  'Art. 20, § 1º: o tipo exige a **finalidade de divulgação do nazismo**.',
  lei=[(RC + '20', 'que utilizem a cruz suástica ou gamada, para fins de divulgação do nazismo', None, 'Lei 7.716/1989, art. 20, § 1º')],
  kw=['suástica', 'divulgação do nazismo'])
I(P, 2, 'Medidas cautelares do § 3º',
  'O recolhimento do material discriminatório veiculado pelos meios de comunicação só pode ser determinado após o trânsito em julgado da condenação.', 'E',
  'Art. 20, § 3º: o juiz pode determiná-lo, ouvido o MP ou a pedido deste, **ainda antes do inquérito policial**; a **destruição** do material é que é efeito da condenação transitada (§ 4º).',
  lei=[(RC + '20', 'ainda antes do inquérito policial, sob pena de desobediência', None, 'Lei 7.716/1989, art. 20, § 3º')],
  peg='Confundir recolhimento cautelar com destruição.', kw=['antes do inquérito', 'recolhimento'])
I(P, 2, 'Funcionário público',
  'O aumento de pena pela prática por funcionário público no exercício de suas funções aplica-se apenas ao crime do art. 20 da Lei 7.716/1989.', 'E',
  'Art. 20-B: alcança os crimes dos **arts. 2º-A e 20** (injúria racial e praticar, induzir ou incitar), com aumento de 1/3 até a metade.',
  lei=[(RC + '20-B', 'Os crimes previstos nos arts. 2º-A e 20 desta Lei terão as penas aumentadas de 1/3 (um terço) até a metade, quando praticados por funcionário público', None, 'Lei 7.716/1989, art. 20-B')],
  peg='Esquecer a injúria racial.', kw=['funcionário público', 'arts. 2º-A e 20'])

# ======================= LPE-4 · Abuso de autoridade =======================
P = 'DBA26-LPE-4'
I(P, 1, 'Elemento subjetivo especial',
  'As condutas da Lei 13.869/2019 só constituem abuso de autoridade quando praticadas com a finalidade específica de prejudicar outrem ou beneficiar a si mesmo ou a terceiro, ou por mero capricho ou satisfação pessoal.', 'C',
  'Art. 1º, § 1º: todos os crimes são **dolosos** e exigem esse **especial fim de agir**.',
  lei=[(AB + '1', 'com a finalidade específica de prejudicar outrem ou beneficiar a si mesmo ou a terceiro, ou, ainda, por mero capricho ou satisfação pessoal', None, 'Lei 13.869/2019, art. 1º, § 1º')],
  kw=['finalidade específica', 'mero capricho'])
I(P, 1, 'Crime de hermenêutica',
  'A divergência na interpretação de lei configura abuso de autoridade na modalidade culposa, se o agente devia conhecer a orientação dominante.', 'E',
  'Art. 1º, § 2º: a **divergência na interpretação** de lei ou na avaliação de fatos e provas **não configura** abuso (veda-se o "crime de hermenêutica"); e não há modalidade culposa.',
  lei=[(AB + '1', 'A divergência na interpretação de lei ou na avaliação de fatos e provas não configura abuso de autoridade.', None, 'Lei 13.869/2019, art. 1º, § 2º')],
  peg='Criar abuso culposo.', kw=['divergência na interpretação'])
I(P, 1, 'Ação penal',
  'Os crimes de abuso de autoridade são de ação penal pública condicionada à representação do ofendido.', 'E',
  'Art. 3º (veto derrubado): ação **pública incondicionada**, admitida a privada subsidiária.',
  lei=[(AB + '3', 'Art. 3º Os crimes previstos nesta Lei são de ação penal pública incondicionada.', None, 'Lei 13.869/2019, art. 3º')],
  peg='Exigir representação.', kw=['pública incondicionada'])
I(P, 1, 'Perda do cargo',
  'A inabilitação para o cargo e a perda do cargo, como efeitos da condenação por abuso de autoridade, dependem de reincidência em crime de abuso e devem ser declaradas motivadamente na sentença.', 'C',
  'Art. 4º, par. ún.: efeitos **não automáticos** e condicionados à **reincidência específica**.',
  lei=[(AB + '4', 'são condicionados à ocorrência de reincidência em crime de abuso de autoridade e não são automáticos', None, 'Lei 13.869/2019, art. 4º, par. ún.')],
  kw=['reincidência', 'não são automáticos'])
I(P, 1, 'Nota de culpa',
  'Comete crime de abuso de autoridade quem deixa de entregar ao preso, no prazo de 24 horas, a nota de culpa assinada pela autoridade, com o motivo da prisão e os nomes do condutor e das testemunhas.', 'C',
  'Art. 12, par. ún., III — mesma pena de deixar de comunicar o flagrante ao juiz (6 meses a 2 anos).',
  lei=[(AB + '12', 'deixa de entregar ao preso, no prazo de 24 (vinte e quatro) horas, a nota de culpa', None, 'Lei 13.869/2019, art. 12, par. ún., III')],
  kw=['nota de culpa', '24 (vinte e quatro) horas'])
I(P, 1, 'Interrogatório noturno',
  'É crime submeter o preso a interrogatório policial durante o repouso noturno, em qualquer hipótese, ainda que ele, assistido por advogado, consinta em prestar declarações.', 'E',
  'Art. 18: há duas ressalvas — captura em **flagrante** ou **consentimento** do preso **devidamente assistido**.',
  lei=[(AB + '18', 'salvo se capturado em flagrante delito ou se ele, devidamente assistido, consentir em prestar declarações', None, 'Lei 13.869/2019, art. 18')],
  peg='Apagar as ressalvas.', kw=['repouso noturno', 'devidamente assistido'])
I(P, 1, 'Mandado após as 21h',
  'Comete abuso de autoridade quem cumpre mandado de busca e apreensão domiciliar após as 21h ou antes das 5h.', 'C',
  'Art. 22, § 1º, III: a lei fixou o horário do "dia" para o cumprimento do mandado.',
  lei=[(AB + '22', 'cumpre mandado de busca e apreensão domiciliar após as 21h (vinte e uma horas) ou antes das 5h (cinco horas)', None, 'Lei 13.869/2019, art. 22, § 1º, III')],
  kw=['21h', '5h'])
I(P, 1, 'Violência institucional',
  'Na violência institucional, se o próprio agente público intimidar a vítima de crime violento, gerando revitimização, a pena é aumentada de 2/3; se permitir que terceiro a intimide, é aplicada em dobro.', 'E',
  'Art. 15-A (Lei 14.321/2022): inverteu — **permitir** que terceiro intimide: **+2/3** (§ 1º); o próprio agente **intimidar**: **em dobro** (§ 2º).',
  lei=[(AB + '15-A', 'Se o agente público intimidar a vítima de crimes violentos, gerando indevida revitimização, aplica-se a pena em dobro.', None, 'Lei 13.869/2019, art. 15-A, § 2º')],
  peg='Trocar as frações dos §§ 1º e 2º.', kw=['violência institucional', 'em dobro'])
I(P, 1, 'Sindicância',
  'Não há crime de abuso de autoridade na instauração de sindicância ou investigação preliminar sumária, devidamente justificada, ainda que sem indício prévio de infração.', 'C',
  'Art. 27, par. ún.: a ressalva protege a apuração preliminar.',
  lei=[(AB + '27', 'Não há crime quando se tratar de sindicância ou investigação preliminar sumária, devidamente justificada.', None, 'Lei 13.869/2019, art. 27, par. ún.')],
  kw=['sindicância', 'investigação preliminar sumária'])
# --- LPE-4 · Rodada 2
I(P, 2, 'Sujeito ativo',
  'Membros do Poder Judiciário e do Ministério Público podem ser sujeitos ativos de crime de abuso de autoridade.', 'C',
  'Art. 2º, IV e V: o conceito de agente público é amplo (par. ún.), alcançando quem exerce função ainda que transitoriamente ou sem remuneração.',
  lei=[(AB + '2', 'IV - membros do Poder Judiciário;', None, 'Lei 13.869/2019, art. 2º, IV'), (AB + '2', 'V - membros do Ministério Público;', None, 'Lei 13.869/2019, art. 2º, V')],
  kw=['sujeito ativo', 'agente público'])
I(P, 2, 'Suspensão do cargo',
  'A pena restritiva de suspensão do exercício do cargo, prevista na Lei de Abuso de Autoridade, é de 1 a 6 meses, mantidos os vencimentos.', 'E',
  'Art. 5º, II: suspensão de 1 a 6 meses **com a perda dos vencimentos e das vantagens**.',
  lei=[(AB + '5', 'pelo prazo de 1 (um) a 6 (seis) meses, com a perda dos vencimentos e das vantagens', None, 'Lei 13.869/2019, art. 5º, II')],
  peg='Manter a remuneração.', kw=['perda dos vencimentos'])
I(P, 2, 'Ação privada subsidiária',
  'A ação privada subsidiária nos crimes de abuso de autoridade deve ser exercida em 6 meses, contados da data em que se esgotar o prazo para oferecimento da denúncia.', 'C',
  'Art. 3º, § 2º.',
  lei=[(AB + '3', 'A ação privada subsidiária será exercida no prazo de 6 (seis) meses, contado da data em que se esgotar o prazo para oferecimento da denúncia.', None, 'Lei 13.869/2019, art. 3º, § 2º')],
  kw=['ação privada subsidiária', '6 (seis) meses'])
I(P, 2, 'Condução coercitiva',
  'É crime decretar a condução coercitiva de testemunha ou investigado manifestamente descabida ou sem prévia intimação de comparecimento ao juízo.', 'C',
  'Art. 10.',
  lei=[(AB + '10', 'Decretar a condução coercitiva de testemunha ou investigado manifestamente descabida ou sem prévia intimação de comparecimento ao juízo', None, 'Lei 13.869/2019, art. 10')],
  kw=['condução coercitiva', 'prévia intimação'])
I(P, 2, 'Produzir prova contra si',
  'Constranger o preso, mediante violência ou grave ameaça, a produzir prova contra si mesmo não é crime de abuso de autoridade, porque o inciso correspondente foi vetado.', 'E',
  'Art. 13, III: o **veto foi derrubado** e o inciso promulgado; a conduta é crime (detenção, de 1 a 4 anos, e multa).',
  lei=[(AB + '13', 'III - produzir prova contra si mesmo ou contra terceiro:', None, 'Lei 13.869/2019, art. 13, III')],
  peg='Ignorar a derrubada do veto.', kw=['veto derrubado', 'produzir prova contra si'])
I(P, 2, 'Antecipar atribuição de culpa',
  'O crime de antecipar atribuição de culpa só se configura se a comunicação for feita à imprensa, não alcançando a publicação em rede social.', 'E',
  'Art. 38: a comunicação é "**inclusive rede social**", antes de concluídas as apurações e formalizada a acusação.',
  lei=[(AB + '38', 'Antecipar o responsável pelas investigações, por meio de comunicação, inclusive rede social, atribuição de culpa', None, 'Lei 13.869/2019, art. 38')],
  peg='Excluir a rede social.', kw=['rede social', 'atribuição de culpa'])

# ======================= LPE-5 · Tortura =======================
P = 'DBA26-LPE-5'
I(P, 1, 'Tortura-prova',
  'Constitui tortura constranger alguém com emprego de violência ou grave ameaça, causando-lhe sofrimento físico ou mental, com o fim de obter informação, declaração ou confissão da vítima ou de terceira pessoa.', 'C',
  'Art. 1º, I, a: é crime **comum** — qualquer pessoa pode praticá-lo (sendo agente público, a pena aumenta).',
  lei=[(TT + '1', 'a) com o fim de obter informação, declaração ou confissão da vítima ou de terceira pessoa;', None, 'Lei 9.455/1997, art. 1º, I, a')],
  kw=['tortura-prova', 'confissão'])
I(P, 1, 'Tortura-castigo',
  'A tortura-castigo pode ser praticada contra qualquer pessoa, independentemente de vínculo de guarda, poder ou autoridade, bastando que a vítima sofra algum sofrimento físico.', 'E',
  'Art. 1º, II: a vítima deve estar **sob guarda, poder ou autoridade** do agente e o sofrimento deve ser **intenso**, como castigo pessoal ou medida preventiva — crime **próprio**.',
  lei=[(TT + '1', 'II - submeter alguém, sob sua guarda, poder ou autoridade, com emprego de violência ou grave ameaça, a intenso sofrimento físico ou mental', None, 'Lei 9.455/1997, art. 1º, II')],
  peg='Dispensar o vínculo e a intensidade.', kw=['tortura-castigo', 'sob sua guarda'])
I(P, 1, 'Tortura na violência doméstica (2026)',
  'Constitui tortura submeter mulher, reiteradamente, a intenso sofrimento físico ou mental, no contexto de violência doméstica e familiar, sem prejuízo das penas das demais infrações.', 'C',
  'Art. 1º, III (**Lei 15.410/2026**).',
  lei=[(TT + '1', 'III – submeter mulher, reiteradamente, a intenso sofrimento físico ou mental, no contexto de violência doméstica e familiar', None, 'Lei 9.455/1997, art. 1º, III')],
  kw=['Lei 15.410/2026', 'reiteradamente'])
I(P, 1, 'Omissão',
  'Quem se omite diante da tortura, tendo o dever de evitá-la ou apurá-la, responde com a mesma pena do torturador.', 'E',
  'Art. 1º, § 2º: a **omissão** tem pena própria e menor — **detenção, de 1 a 4 anos** — e não impõe o regime inicial fechado (§ 7º).',
  lei=[(TT + '1', 'Aquele que se omite em face dessas condutas, quando tinha o dever de evitá-las ou apurá-las, incorre na pena de detenção de um a quatro anos.', None, 'Lei 9.455/1997, art. 1º, § 2º')],
  peg='Igualar omissão e ação.', kw=['omissão', 'detenção de um a quatro anos'])
I(P, 1, 'Perda do cargo',
  'Pela letra da Lei 9.455/1997, a condenação por tortura acarreta a perda do cargo, função ou emprego público e a interdição para seu exercício pelo dobro do prazo da pena aplicada.', 'C',
  'Art. 1º, § 5º. Compare com a Lei 13.869/2019, em que a perda depende de reincidência e declaração motivada.',
  lei=[(TT + '1', 'A condenação acarretará a perda do cargo, função ou emprego público e a interdição para seu exercício pelo dobro do prazo da pena aplicada.', None, 'Lei 9.455/1997, art. 1º, § 5º')],
  kw=['perda do cargo', 'dobro do prazo'])
I(P, 1, 'Fiança',
  'O crime de tortura admite fiança, mas é insuscetível de graça e anistia.', 'E',
  'Art. 1º, § 6º: **inafiançável** e insuscetível de graça ou anistia (CF, art. 5º, XLIII; a Lei 8.072/1990 acrescenta o indulto).',
  lei=[(TT + '1', 'O crime de tortura é inafiançável e insuscetível de graça ou anistia.', None, 'Lei 9.455/1997, art. 1º, § 6º')],
  peg='Admitir fiança.', kw=['inafiançável'])
# --- LPE-5 · Rodada 2
I(P, 2, 'Regime inicial',
  'O condenado por tortura iniciará o cumprimento da pena em regime fechado, salvo na hipótese de omissão.', 'C',
  'Art. 1º, § 7º.',
  lei=[(TT + '1', 'O condenado por crime previsto nesta Lei, salvo a hipótese do § 2º, iniciará o cumprimento da pena em regime fechado.', None, 'Lei 9.455/1997, art. 1º, § 7º')],
  kw=['regime fechado', 'salvo a hipótese do § 2º'])
I(P, 2, 'Agente público',
  'Se a tortura é cometida por agente público, a pena é aumentada da metade.', 'E',
  'Art. 1º, § 4º, I: aumento de **um sexto até um terço** — mesma fração para vítima criança, gestante, pessoa com deficiência, adolescente ou maior de 60 anos, e para tortura mediante sequestro.',
  lei=[(TT + '1', 'Aumenta-se a pena de um sexto até um terço:', None, 'Lei 9.455/1997, art. 1º, § 4º'), (TT + '1', 'I - se o crime é cometido por agente público;', None, 'Lei 9.455/1997, art. 1º, § 4º, I')],
  peg='Trocar a fração.', kw=['agente público', 'um sexto até um terço'])
I(P, 2, 'Extraterritorialidade',
  'A Lei de Tortura aplica-se ainda que o crime não tenha sido cometido no território nacional, sendo a vítima brasileira ou encontrando-se o agente em local sob jurisdição brasileira.', 'C',
  'Art. 2º: extraterritorialidade própria da lei.',
  lei=[(TT + '2', 'sendo a vítima brasileira ou encontrando-se o agente em local sob jurisdição brasileira', None, 'Lei 9.455/1997, art. 2º')],
  kw=['extraterritorialidade', 'vítima brasileira'])
I(P, 2, 'Resultado morte',
  'Se da tortura resulta morte, a pena é de reclusão de 4 a 10 anos.', 'E',
  'Art. 1º, § 3º: lesão grave ou gravíssima, 4 a 10 anos; **morte, 8 a 16 anos** (resultado culposo — havendo dolo de matar, é homicídio qualificado pela tortura).',
  lei=[(TT + '1', 'se resulta morte, a reclusão é de oito a dezesseis anos', None, 'Lei 9.455/1997, art. 1º, § 3º')],
  peg='Usar a pena da lesão grave para a morte.', kw=['resultado morte', 'oito a dezesseis anos'])
