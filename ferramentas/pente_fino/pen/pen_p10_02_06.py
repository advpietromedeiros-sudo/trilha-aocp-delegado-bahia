# Pente Fino de Direito Penal (Parte Especial) — PEN-10.2 (patrimônio), 10.3 (propriedade imaterial: propriedade
# industrial, Lei 9.279/1996), 10.4 (propriedade intelectual: direito autoral e programa de computador), 10.5
# (organização do trabalho) e 10.6 (sentimento religioso e respeito aos mortos) (08/11/2026).
from base import I
from pen_juris import J

CP = 'CP:'
LPI = 'L9279:'

# ======================= PEN-10.2 · Crimes contra o patrimônio =======================
P = 'DBA26-PEN-10.2'
I(P, 1, 'Pena do furto simples',
  'O furto simples é punido com reclusão de 1 a 4 anos, e multa.', 'E',
  'A **Lei 15.397/2026** elevou a pena do art. 155, caput, para **1 a 6 anos**, e multa. A pena de 1 a 4 anos é a antiga.',
  lei=[(CP + '155', 'Pena – reclusão, de 1 (um) a 6 (seis) anos, e multa.', None, 'CP, art. 155, caput (pena)')],
  peg='Cobrar a pena anterior a 2026.', kw=['Lei 15.397/2026', '1 a 6 anos'])
I(P, 1, 'Repouso noturno',
  'A pena do furto aumenta-se de metade se o crime é praticado durante o repouso noturno.', 'C',
  'Art. 155, § 1º, na redação da **Lei 15.397/2026** (antes, um terço).',
  lei=[(CP + '155', '§ 1º A pena aumenta-se de metade, se o crime é praticado durante o repouso noturno.', None, 'CP, art. 155, § 1º')],
  kw=['de metade', 'repouso noturno'])
I(P, 1, 'Furto privilegiado-qualificado',
  'É possível reconhecer o privilégio do § 2º do art. 155 no furto qualificado, se o agente é primário, a coisa é de pequeno valor e a qualificadora é de ordem objetiva.', 'C',
  '**Súmula 511/STJ**. Qualificadora subjetiva (abuso de confiança) afasta o privilégio.',
  lei=[(CP + '155', '§ 2º - Se o criminoso é primário, e é de pequeno valor a coisa furtada', 'ou aplicar somente a pena de multa.', 'CP, art. 155, § 2º')],
  juris=[J['S511']], kw=['Súmula 511/STJ', 'ordem objetiva'])
I(P, 1, 'Consumação do furto',
  'O furto só se consuma quando o agente obtém a posse mansa e pacífica da coisa, fora da esfera de vigilância da vítima.', 'E',
  '**Tema 934/STJ**: basta a **posse de fato**, ainda que por breve tempo e seguida de perseguição (teoria da *amotio*/*apprehensio*).',
  juris=[J['T934']], peg='Exigir posse mansa e pacífica.', kw=['Tema 934/STJ', 'posse de fato'])
I(P, 1, 'Vigilância eletrônica',
  'A existência de sistema de vigilância eletrônica ou de segurança no estabelecimento comercial não torna, por si só, impossível o crime de furto.', 'C',
  '**Súmula 567/STJ**: a ineficácia do meio é só relativa — cabe tentativa, não crime impossível (art. 17).',
  juris=[J['S567']], kw=['Súmula 567/STJ'])
I(P, 1, 'Concurso de pessoas no furto',
  'No furto qualificado pelo concurso de pessoas, aplica-se a majorante do roubo, por ser mais favorável ao réu.', 'E',
  '**Súmula 442/STJ**: é **inadmissível** aplicar ao furto qualificado pelo concurso de agentes a majorante do roubo.',
  lei=[(CP + '155', 'IV - mediante concurso de duas ou mais pessoas.', None, 'CP, art. 155, § 4º, IV')],
  juris=[J['S442']], peg='Combinar furto e roubo.', kw=['Súmula 442/STJ'])
I(P, 1, 'Roubo impróprio',
  'Comete roubo impróprio quem, logo depois de subtraída a coisa, emprega violência ou grave ameaça para assegurar a impunidade do crime ou a detenção da coisa.', 'C',
  'Art. 157, § 1º: a violência vem **depois** da subtração; no roubo próprio, vem antes ou durante.',
  lei=[(CP + '157', '§ 1º - Na mesma pena incorre quem, logo depois de subtraída a coisa', 'a detenção da coisa para si ou para terceiro.', 'CP, art. 157, § 1º')],
  kw=['roubo impróprio', 'logo depois'])
I(P, 1, 'Pena do roubo',
  'O roubo simples é punido com reclusão de 4 a 10 anos, e multa.', 'E',
  'A **Lei 15.397/2026** elevou a pena mínima: o art. 157, caput, comina **6 a 10 anos**, e multa.',
  lei=[(CP + '157', 'Pena – reclusão, de 6 (seis) a 10 (dez) anos, e multa.', None, 'CP, art. 157, caput (pena)')],
  peg='Cobrar a pena anterior a 2026.', kw=['6 a 10 anos', 'Lei 15.397/2026'])
I(P, 1, 'Latrocínio consumado',
  'Há latrocínio consumado quando o homicídio se consuma, ainda que o agente não realize a subtração dos bens da vítima.', 'C',
  '**Súmula 610/STF**. Na redação da Lei 15.397/2026, a pena do latrocínio é de **24 a 30 anos** (art. 157, § 3º, II).',
  lei=[(CP + '157', 'II – morte, a pena é de reclusão, de 24 (vinte e quatro) a 30 (trinta) anos, e multa.', None, 'CP, art. 157, § 3º, II')],
  juris=[J['STF610']], kw=['Súmula 610/STF', '24 a 30 anos'])
I(P, 1, 'Latrocínio: competência',
  'Por envolver morte dolosa, o latrocínio é julgado pelo Tribunal do Júri.', 'E',
  '**Súmula 603/STF**: compete ao **juiz singular**. O latrocínio é crime contra o patrimônio, não crime doloso contra a vida.',
  juris=[J['STF603']], peg='Levar o latrocínio ao júri.', kw=['Súmula 603/STF', 'juiz singular'])
I(P, 1, 'Consumação da extorsão',
  'A extorsão só se consuma com a obtenção da vantagem econômica indevida.', 'E',
  '**Súmula 96/STJ**: crime **formal** — consuma-se com o constrangimento, independentemente da obtenção da vantagem.',
  lei=[(CP + '158', 'Constranger alguém, mediante violência ou grave ameaça, e com o intuito de obter para si ou para outrem indevida vantagem econômica', None, 'CP, art. 158, caput')],
  juris=[J['S96']], peg='Tratar a extorsão como crime material.', kw=['Súmula 96/STJ', 'formal'])
I(P, 1, 'Estelionato contra o INSS',
  'Ao estelionato em que figure como vítima entidade autárquica da Previdência Social aplica-se o aumento de um terço do § 3º do art. 171.', 'C',
  '**Súmula 24/STJ**: a autarquia previdenciária é entidade de direito público.',
  lei=[(CP + '171', '§ 3º - A pena aumenta-se de um terço, se o crime é cometido em detrimento de entidade de direito público', None, 'CP, art. 171, § 3º')],
  juris=[J['S24']], kw=['Súmula 24/STJ'])
# --- PEN-10.2 · Rodada 2
I(P, 2, 'Estelionato: ação penal',
  'O estelionato é, em regra, crime de ação penal pública condicionada à representação, nos termos do § 5º do art. 171.', 'E',
  'A **Lei 15.397/2026 revogou o § 5º** (incluído pela Lei 13.964/2019): o estelionato voltou à ação **pública incondicionada**, regra geral do art. 100.',
  lei=[(CP + '171', '§ 5º (Revogado). (Redação dada pela Lei nº 15.397, de 2026)', None, 'CP, art. 171, § 5º')],
  peg='Cobrar a representação do Pacote Anticrime.', kw=['revogou o § 5º', 'pública incondicionada'])
I(P, 2, 'Conta laranja',
  'Incorre nas penas do estelionato quem cede, gratuita ou onerosamente, conta bancária para que nela transitem recursos destinados ao financiamento de atividade criminosa ou dela provenientes.', 'C',
  'Art. 171, § 2º, **VII** (cessão de conta laranja), incluído pela Lei 15.397/2026.',
  lei=[(CP + '171', 'VII – cede, gratuita ou onerosamente, conta bancária para que nela transitem recursos', 'ou que dela sejam fruto.', 'CP, art. 171, § 2º, VII')],
  kw=['conta laranja', 'VII'])
I(P, 2, 'Pena da receptação',
  'A receptação simples é punida com reclusão de 1 a 4 anos, e multa.', 'E',
  'A **Lei 15.397/2026** fixou **2 a 6 anos**, e multa (art. 180, caput). A receptação qualificada (§ 1º) segue com 3 a 8 anos.',
  lei=[(CP + '180', 'Pena – reclusão, de 2 (dois) a 6 (seis) anos, e multa.', None, 'CP, art. 180, caput (pena)')],
  peg='Cobrar a pena anterior a 2026.', kw=['2 a 6 anos'])
I(P, 2, 'Autonomia da receptação',
  'A receptação é punível ainda que desconhecido ou isento de pena o autor do crime de que proveio a coisa.', 'C',
  'Art. 180, § 4º: **autonomia** da receptação em relação ao crime antecedente.',
  lei=[(CP + '180', '§ 4º - A receptação é punível, ainda que desconhecido ou isento de pena o autor do crime de que proveio a coisa.', None, 'CP, art. 180, § 4º')],
  kw=['autonomia'])
I(P, 2, 'Imunidade e roubo',
  'O filho que rouba o pai, com grave ameaça, fica isento de pena pela imunidade absoluta do art. 181 do Código Penal.', 'E',
  'Art. 183, I: as imunidades **não se aplicam** ao roubo, à extorsão ou a qualquer crime com violência ou grave ameaça (nem à vítima com 60 anos ou mais, III).',
  lei=[(CP + '183', 'I - se o crime é de roubo ou de extorsão, ou, em geral, quando haja emprego de grave ameaça ou violência à pessoa;', None, 'CP, art. 183, I')],
  peg='Estender a escusa absolutória ao roubo.', kw=['imunidades', 'não se aplicam'])
I(P, 2, 'Arma de uso restrito',
  'Se a violência ou grave ameaça do roubo é exercida com arma de fogo de uso restrito ou proibido, aplica-se em dobro a pena do caput.', 'C',
  'Art. 157, **§ 2º-B** (Lei 13.964/2019); arma de fogo de uso permitido aumenta de 2/3 (§ 2º-A, I).',
  lei=[(CP + '157', '§ 2º-B. Se a violência ou grave ameaça é exercida com emprego de arma de fogo de uso restrito ou proibido', None, 'CP, art. 157, § 2º-B')],
  kw=['§ 2º-B', 'em dobro'])
I(P, 2, 'Extorsão mediante sequestro com morte',
  'Na extorsão mediante sequestro, se resulta a morte, a pena é de reclusão de 20 a 30 anos.', 'E',
  'Art. 159, § 3º: **24 a 30 anos** — a maior pena do Código antes das reformas de 2024–2026.',
  lei=[(CP + '159', '§ 3º - Se resulta a morte:', 'Pena - reclusão, de vinte e quatro a trinta anos.', 'CP, art. 159, § 3º')],
  peg='Errar o mínimo da pena.', kw=['24 a 30 anos'])
I(P, 2, 'Devedor contumaz',
  'A extinção da punibilidade pelo pagamento espontâneo antes da ação fiscal, na apropriação indébita previdenciária, não se aplica ao agente declarado devedor contumaz e inscrito no Cadin.', 'C',
  'Art. 168-A, **§ 5º**, incluído pela Lei Complementar 225/2026 (o art. 337-A, § 5º, tem regra igual).',
  lei=[(CP + '168-A', '§ 5º A extinção de punibilidade de que trata o § 2º deste artigo não se aplica ao agente declarado devedor contumaz', None, 'CP, art. 168-A, § 5º')],
  kw=['devedor contumaz', '§ 5º'])

# ======================= PEN-10.3 · Propriedade imaterial (propriedade industrial) =======================
P = 'DBA26-PEN-10.3'
I(P, 1, 'Revogação no CP',
  'Os crimes contra o privilégio de invenção e contra as marcas de indústria e comércio do Código Penal foram revogados pela Lei 9.279/1996, que passou a tipificá-los.', 'C',
  'Arts. 187 a 196 do CP: **revogados** pela Lei de Propriedade Industrial (arts. 183 a 195). No Título III do CP sobrou o direito autoral (arts. 184 e 186).',
  lei=[(CP + '189', 'Art. 189. (Revogado pela Lei nº 9.279, de 14.5.1996)', None, 'CP, art. 189')],
  kw=['revogados', 'Lei de Propriedade Industrial'])
I(P, 1, 'Ação penal na LPI',
  'Nos crimes contra a propriedade industrial, a ação penal é, em regra, pública incondicionada.', 'E',
  'Art. 199 da Lei 9.279/1996: **somente se procede mediante queixa**, salvo o crime do art. 191 (armas, brasões e distintivos oficiais), de ação pública.',
  lei=[(LPI + '199', 'Art. 199. Nos crimes previstos neste Título somente se procede mediante queixa, salvo quanto ao crime do art. 191, em que a ação penal será pública.', None, 'Lei 9.279/1996, art. 199')],
  peg='Inverter a regra da queixa.', kw=['mediante queixa'])
I(P, 1, 'Crime contra marca',
  'Comete crime contra registro de marca quem reproduz, sem autorização do titular, no todo ou em parte, marca registrada, ou a imita de modo que possa induzir confusão.', 'C',
  'Lei 9.279/1996, art. **189, I**: detenção de 3 meses a 1 ano, ou multa.',
  lei=[(LPI + '189', 'I - reproduz, sem autorização do titular, no todo ou em parte, marca registrada', None, 'Lei 9.279/1996, art. 189, I')],
  kw=['189, I'])
I(P, 1, 'Violação parcial de patente',
  'O crime contra patente de invenção só se caracteriza se a violação atingir todas as reivindicações da patente.', 'E',
  'Art. 186 da LPI: o crime existe **ainda que** a violação **não atinja todas as reivindicações** ou se restrinja a meios equivalentes.',
  lei=[(LPI + '186', 'Art. 186. Os crimes deste Capítulo caracterizam-se ainda que a violação não atinja todas as reivindicações da patente', None, 'Lei 9.279/1996, art. 186')],
  peg='Exigir violação integral.', kw=['não atinja todas as reivindicações'])
I(P, 1, 'Concorrência desleal',
  'Comete crime de concorrência desleal quem emprega meio fraudulento para desviar, em proveito próprio ou alheio, clientela de outrem.', 'C',
  'Lei 9.279/1996, art. **195, III**.',
  lei=[(LPI + '195', 'III - emprega meio fraudulento, para desviar, em proveito próprio ou alheio, clientela de outrem;', None, 'Lei 9.279/1996, art. 195, III')],
  kw=['concorrência desleal'])
# --- PEN-10.3 · Rodada 2
I(P, 2, 'Brasões oficiais',
  'Reproduzir em marca, sem autorização, armas, brasões ou distintivos oficiais é crime de ação penal privada, como os demais crimes da Lei 9.279/1996.', 'E',
  'É justamente a **exceção** do art. 199: no crime do **art. 191**, a ação penal é **pública**.',
  lei=[(LPI + '191', 'Reproduzir ou imitar, de modo que possa induzir em erro ou confusão, armas, brasões ou distintivos oficiais', None, 'Lei 9.279/1996, art. 191, caput')],
  peg='Esquecer a exceção do art. 191.', kw=['art. 191', 'exceção'])
I(P, 2, 'Marca de alto renome',
  'As penas dos crimes contra patentes, desenhos industriais e marcas aumentam-se de um terço à metade se a marca for de alto renome, notoriamente conhecida, de certificação ou coletiva.', 'C',
  'Lei 9.279/1996, art. **196, II** (o inciso I trata de representante, sócio ou empregado do titular).',
  lei=[(LPI + '196', 'II - a marca alterada, reproduzida ou imitada for de alto renome, notoriamente conhecida, de certificação ou coletiva.', None, 'Lei 9.279/1996, art. 196, II')],
  kw=['alto renome'])
I(P, 2, 'Desenho industrial',
  'A Lei 9.279/1996 só tipifica crimes contra patentes e marcas; a violação de desenho industrial registrado é ilícito apenas civil.', 'E',
  'O art. **187** da LPI pune fabricar, sem autorização, produto que incorpore **desenho industrial** registrado ou imitação substancial.',
  lei=[(LPI + '187', 'Art. 187. Fabricar, sem autorização do titular, produto que incorpore desenho industrial registrado', None, 'Lei 9.279/1996, art. 187')],
  peg='Negar a tutela penal do desenho industrial.', kw=['desenho industrial'])

# ======================= PEN-10.4 · Propriedade intelectual (direito autoral e software) =======================
P = 'DBA26-PEN-10.4'
I(P, 1, 'Violação simples',
  'A violação de direito autoral na forma simples do art. 184, caput, do Código Penal é punida com detenção, ou multa, e se procede mediante queixa.', 'C',
  'Art. 184, caput (detenção de 3 meses a 1 ano, ou multa) e art. 186, **I** (queixa): infração de menor potencial ofensivo.',
  lei=[(CP + '184', 'Pena – detenção, de 3 (três) meses a 1 (um) ano, ou multa.', None, 'CP, art. 184, caput (pena)'),
       (CP + '186', 'I – queixa, nos crimes previstos no caput do art. 184;', None, 'CP, art. 186, I')],
  kw=['queixa', 'menor potencial ofensivo'])
I(P, 1, 'Reprodução com lucro',
  'Na violação de direito autoral por reprodução com intuito de lucro (art. 184, § 1º), procede-se mediante queixa.', 'E',
  'Art. 186, **II**: nos §§ 1º e 2º do art. 184, a ação é **pública incondicionada**.',
  lei=[(CP + '186', 'II – ação penal pública incondicionada, nos crimes previstos nos §§ 1o e 2o do art. 184;', None, 'CP, art. 186, II')],
  peg='Estender a queixa às formas qualificadas.', kw=['pública incondicionada'])
I(P, 1, 'Venda de mídia pirata',
  'Presentes materialidade e autoria, é típica a conduta de expor à venda CDs e DVDs piratas, não sendo afastada pela tolerância social.', 'C',
  '**Súmula 502/STJ** (art. 184, § 2º). A adequação social não exclui a tipicidade.',
  lei=[(CP + '184', '§ 2o Na mesma pena do § 1o incorre quem, com o intuito de lucro direto ou indireto, distribui, vende, expõe à venda', None, 'CP, art. 184, § 2º')],
  juris=[J['S502']], kw=['Súmula 502/STJ', 'adequação social'])
I(P, 1, 'Perícia por amostragem',
  'A materialidade da violação de direito autoral exige perícia em todo o material apreendido e a identificação dos titulares dos direitos violados.', 'E',
  '**Súmula 574/STJ**: basta perícia **por amostragem**, nos aspectos externos, sendo **desnecessário** identificar os titulares.',
  juris=[J['S574']], peg='Exigir perícia integral e titular identificado.', kw=['Súmula 574/STJ', 'por amostragem'])
I(P, 1, 'Cópia privada',
  'A cópia de obra intelectual, em um só exemplar, para uso privado do copista e sem intuito de lucro direto ou indireto, configura a forma qualificada do art. 184, § 1º.', 'E',
  'Art. 184, **§ 4º**: as formas qualificadas **não se aplicam** à cópia única para uso privado, sem intuito de lucro, nem às exceções da Lei 9.610/1998.',
  lei=[(CP + '184', '§ 4o O disposto nos §§ 1o, 2o e 3o não se aplica', 'para uso privado do copista, sem intuito de lucro direto ou indireto.', 'CP, art. 184, § 4º')],
  peg='Punir a cópia privada única.', kw=['§ 4º', 'uso privado'])
# --- PEN-10.4 · Rodada 2
I(P, 2, 'Programa de computador',
  'A violação de direitos de autor de programa de computador é tipificada em lei especial, com pena de detenção de seis meses a dois anos ou multa.', 'C',
  'Lei **9.609/1998**, art. 12 (lei especial prevalece sobre o art. 184 do CP); reprodução para fins de comércio: reclusão de 1 a 4 anos (§ 1º).',
  lei=[('L9609:12', 'Art. 12. Violar direitos de autor de programa de computador:', 'Pena - Detenção de seis meses a dois anos ou multa.', 'Lei 9.609/1998, art. 12, caput')],
  kw=['Lei 9.609/1998'])
I(P, 2, 'Oferta sob demanda',
  'A violação de direito autoral por oferecimento ao público sob demanda (cabo, fibra ótica, satélite), com intuito de lucro, é de ação penal pública incondicionada.', 'E',
  'Art. 186, **IV**: no § 3º do art. 184, a ação é **pública condicionada à representação**.',
  lei=[(CP + '186', 'IV – ação penal pública condicionada à representação, nos crimes previstos no § 3o do art. 184.', None, 'CP, art. 186, IV')],
  peg='Igualar o § 3º aos §§ 1º e 2º.', kw=['condicionada à representação'])
I(P, 2, 'Software e sonegação',
  'Nos crimes contra programa de computador, a ação penal deixa de ser privada quando do ato delituoso resulta sonegação fiscal ou perda de arrecadação tributária.', 'C',
  'Lei 9.609/1998, art. 12, **§ 3º, II** (o inciso I trata de prejuízo a entidade pública).',
  lei=[('L9609:12', 'II - quando, em decorrência de ato delituoso, resultar sonegação fiscal, perda de arrecadação tributária', None, 'Lei 9.609/1998, art. 12, § 3º, II')],
  kw=['§ 3º, II', 'sonegação fiscal'])

# ======================= PEN-10.5 · Organização do trabalho =======================
P = 'DBA26-PEN-10.5'
I(P, 1, 'Liberdade de trabalho',
  'Constranger alguém, mediante violência ou grave ameaça, a exercer ou não exercer arte, ofício ou profissão configura atentado contra a liberdade de trabalho.', 'C',
  'Art. **197**, I, com pena cumulada com a da violência.',
  lei=[(CP + '197', 'Art. 197 - Constranger alguém, mediante violência ou grave ameaça:', 'a exercer ou não exercer arte, ofício, profissão ou indústria', 'CP, art. 197, caput e I')],
  kw=['liberdade de trabalho'])
I(P, 1, 'Abandono coletivo',
  'Para que se considere coletivo o abandono de trabalho, no crime do art. 200, basta o concurso de dois empregados.', 'E',
  'Art. 200, par. ún.: é indispensável o concurso de, pelo menos, **três** empregados.',
  lei=[(CP + '200', 'Parágrafo único - Para que se considere coletivo o abandono de trabalho é indispensável o concurso de, pelo menos, três empregados.', None, 'CP, art. 200, par. ún.')],
  peg='Reduzir o número mínimo.', kw=['três'])
I(P, 1, 'Frustração de direito trabalhista',
  'Frustrar, mediante fraude ou violência, direito assegurado pela legislação do trabalho é crime contra a organização do trabalho.', 'C',
  'Art. **203** (Lei 9.777/1998 aumentou a pena para detenção de 1 a 2 anos, e multa).',
  lei=[(CP + '203', 'Art. 203 - Frustrar, mediante fraude ou violência, direito assegurado pela legislação do trabalho:', None, 'CP, art. 203, caput')],
  kw=['203'])
I(P, 1, 'Aliciamento interno',
  'O aliciamento de trabalhadores de um local para outro do território nacional só é crime se praticado mediante fraude.', 'E',
  'O caput do art. **207** pune aliciar com o fim de levar trabalhadores de uma para outra localidade, **sem exigir fraude**; a fraude aparece no § 1º (recrutamento fora da localidade).',
  lei=[(CP + '207', 'Art. 207 - Aliciar trabalhadores, com o fim de levá-los de uma para outra localidade do território nacional:', None, 'CP, art. 207, caput')],
  peg='Exigir fraude no caput.', kw=['sem exigir fraude'])
I(P, 1, 'Emigração',
  'Recrutar trabalhadores, mediante fraude, com o fim de levá-los para território estrangeiro configura o aliciamento de trabalhadores de um local para outro do território nacional.', 'E',
  'É o crime do art. **206** (aliciamento para o fim de **emigração**). O art. 207 é o deslocamento dentro do território nacional.',
  lei=[(CP + '206', 'Art. 206 - Recrutar trabalhadores, mediante fraude, com o fim de levá-los para território estrangeiro.', None, 'CP, art. 206')],
  peg='Trocar o art. 206 pelo 207.', kw=['emigração'])
# --- PEN-10.5 · Rodada 2
I(P, 2, 'Vítima vulnerável',
  'No crime de frustração de direito assegurado por lei trabalhista, a pena aumenta de um sexto a um terço se a vítima é menor de dezoito anos, idosa, gestante, indígena ou portadora de deficiência.', 'C',
  'Art. 203, **§ 2º** (o art. 207, § 2º, tem aumento idêntico).',
  lei=[(CP + '203', '§ 2º A pena é aumentada de um sexto a um terço se a vítima é menor de dezoito anos, idosa, gestante, indígena', None, 'CP, art. 203, § 2º')],
  kw=['§ 2º', 'um sexto a um terço'])
I(P, 2, 'Trabalho escravo',
  'O crime de redução a condição análoga à de escravo está tipificado no título dos crimes contra a organização do trabalho.', 'E',
  'O art. **149** está no Título I (pessoa), capítulo dos crimes **contra a liberdade individual** — embora o tema seja trabalhista.',
  lei=[(CP + '149', 'Art. 149. Reduzir alguém a condição análoga à de escravo', None, 'CP, art. 149, caput')],
  peg='Confundir a topografia do art. 149.', kw=['contra a liberdade individual'])
I(P, 2, 'Decisão administrativa',
  'O crime do art. 205 do Código Penal exige que o impedimento de exercer a atividade decorra de decisão judicial.', 'E',
  'Art. 205: impedimento por **decisão administrativa**. Exercer função de que foi suspenso por **decisão judicial** é o art. 359 (administração da justiça).',
  lei=[(CP + '205', 'Art. 205 - Exercer atividade, de que está impedido por decisão administrativa:', None, 'CP, art. 205')],
  peg='Trocar decisão administrativa por judicial.', kw=['decisão administrativa'])

# ======================= PEN-10.6 · Sentimento religioso e respeito aos mortos =======================
P = 'DBA26-PEN-10.6'
I(P, 1, 'Ultraje a culto',
  'Escarnecer de alguém publicamente, por motivo de crença ou função religiosa, configura ultraje a culto.', 'C',
  'Art. **208**: três condutas — escarnecer, impedir ou perturbar cerimônia, vilipendiar publicamente ato ou objeto de culto.',
  lei=[(CP + '208', 'Art. 208 - Escarnecer de alguém publicamente, por motivo de crença ou função religiosa', None, 'CP, art. 208, caput')],
  kw=['ultraje a culto'])
I(P, 1, 'Ultraje com violência',
  'Se o ultraje a culto é praticado com emprego de violência, a pena é aplicada em dobro, absorvida a violência.', 'E',
  'Art. 208, par. ún.: aumento de **um terço**, **sem prejuízo** da pena correspondente à violência (cúmulo).',
  lei=[(CP + '208', 'Parágrafo único - Se há emprego de violência, a pena é aumentada de um terço, sem prejuízo da correspondente à violência.', None, 'CP, art. 208, par. ún.')],
  peg='Absorver a violência.', kw=['um terço', 'sem prejuízo'])
I(P, 1, 'Perturbação de enterro',
  'Impedir ou perturbar enterro ou cerimônia funerária é crime contra o respeito aos mortos.', 'C',
  'Art. **209** (Capítulo II do Título V).',
  lei=[(CP + '209', 'Art. 209 - Impedir ou perturbar enterro ou cerimônia funerária:', None, 'CP, art. 209, caput')],
  kw=['209'])
I(P, 1, 'Vilipêndio a cadáver',
  'O vilipêndio a cadáver ou a suas cinzas é punido com reclusão de um a três anos, e multa.', 'E',
  'Art. 212: **detenção** de 1 a 3 anos, e multa. Reclusão de 1 a 3 é a pena da violação de sepultura (210) e da destruição ou ocultação de cadáver (211).',
  lei=[(CP + '212', 'Art. 212 - Vilipendiar cadáver ou suas cinzas:', 'Pena - detenção, de um a três anos, e multa.', 'CP, art. 212')],
  peg='Trocar detenção por reclusão.', kw=['detenção'])
I(P, 1, 'Ocultação de cadáver',
  'Destruir, subtrair ou ocultar cadáver ou parte dele é crime punido com reclusão.', 'C',
  'Art. **211**: reclusão de 1 a 3 anos, e multa. A ocultação é crime **permanente** enquanto o corpo está escondido (doutrina).',
  lei=[(CP + '211', 'Art. 211 - Destruir, subtrair ou ocultar cadáver ou parte dele:', 'Pena - reclusão, de um a três anos, e multa.', 'CP, art. 211')],
  kw=['211', 'permanente'])
# --- PEN-10.6 · Rodada 2
I(P, 2, 'Violação de sepultura',
  'A violação ou profanação de sepultura ou urna funerária é punida com detenção.', 'E',
  'Art. 210: **reclusão** de 1 a 3 anos, e multa.',
  lei=[(CP + '210', 'Art. 210 - Violar ou profanar sepultura ou urna funerária:', 'Pena - reclusão, de um a três anos, e multa.', 'CP, art. 210')],
  peg='Trocar reclusão por detenção.', kw=['reclusão'])
I(P, 2, 'Violência no art. 209',
  'O crime de impedimento ou perturbação de cerimônia funerária exige emprego de violência.', 'E',
  'A violência não é elementar: é **causa de aumento** de um terço, somada à pena da violência (art. 209, par. ún.).',
  lei=[(CP + '209', 'Parágrafo único - Se há emprego de violência, a pena é aumentada de um terço, sem prejuízo da correspondente à violência.', None, 'CP, art. 209, par. ún.')],
  peg='Tratar a violência como elementar.', kw=['causa de aumento'])
I(P, 2, 'Vilipêndio de objeto de culto',
  'Vilipendiar publicamente ato ou objeto de culto religioso é uma das condutas do crime de ultraje a culto.', 'C',
  'Art. 208, parte final: exige **publicidade**.',
  lei=[(CP + '208', 'vilipendiar publicamente ato ou objeto de culto religioso', None, 'CP, art. 208, parte final')],
  kw=['publicidade'])
