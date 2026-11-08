# Pente Fino de Direito Penal (Parte Especial) — PEN-10.7 (dignidade sexual), 10.8 (família), 10.9 (incolumidade
# pública) e 10.10 (paz pública) (08/11/2026).
from base import I
from pen_juris import J

CP = 'CP:'

# ======================= PEN-10.7 · Crimes contra a dignidade sexual =======================
P = 'DBA26-PEN-10.7'
I(P, 1, 'Estupro: tipo',
  'Comete estupro quem constrange alguém, mediante violência ou grave ameaça, a ter conjunção carnal ou a praticar ou permitir que com ele se pratique outro ato libidinoso.', 'C',
  'Art. 213 (Lei 12.015/2009): **tipo misto alternativo** que absorveu o antigo atentado violento ao pudor; pena de 6 a 10 anos.',
  lei=[(CP + '213', 'Art. 213. Constranger alguém, mediante violência ou grave ameaça, a ter conjunção carnal ou a praticar ou permitir que com ele se pratique outro ato libidinoso:', None, 'CP, art. 213, caput')],
  kw=['tipo misto alternativo'])
I(P, 1, 'Pena do estupro de vulnerável',
  'O estupro de vulnerável, na forma simples, é punido com reclusão de 8 a 15 anos.', 'E',
  'A **Lei 15.280/2025** elevou a pena do art. 217-A, caput, para **10 a 18 anos**, e multa (e também as do § 3º, 12 a 24, e do § 4º, 20 a 40).',
  lei=[(CP + '217-A', 'Pena – reclusão, de 10 (dez) a 18 (dezoito) anos, e multa.', None, 'CP, art. 217-A, caput (pena)')],
  peg='Cobrar a pena anterior a 2025.', kw=['Lei 15.280/2025', '10 a 18 anos'])
I(P, 1, 'Consentimento do menor de 14',
  'No estupro de vulnerável, são irrelevantes o consentimento da vítima menor de 14 anos, sua experiência sexual anterior ou a existência de relacionamento amoroso com o agente.', 'C',
  '**Súmula 593/STJ**, hoje também na letra do art. 217-A, § 5º (que inclui a gravidez resultante do crime).',
  lei=[(CP + '217-A', '§ 5º As penas previstas no caput e nos §§ 1º, 3º e 4º deste artigo aplicam-se independentemente do consentimento da vítima', 'da ocorrência de gravidez resultante da prática do crime.', 'CP, art. 217-A, § 5º')],
  juris=[J['S593']], kw=['Súmula 593/STJ'])
I(P, 1, 'Presunção de vulnerabilidade',
  'A presunção de vulnerabilidade do menor de 14 anos é relativa e pode ser afastada diante das circunstâncias do caso concreto.', 'E',
  'A **Lei 15.353/2026** incluiu o § 4º-A: a presunção é **absoluta** e **inadmissível sua relativização**.',
  lei=[(CP + '217-A', '§ 4º-A. É absoluta a presunção de vulnerabilidade da vítima e inadmissível sua relativização.', None, 'CP, art. 217-A, § 4º-A')],
  peg='Relativizar a vulnerabilidade.', kw=['absoluta', 'Lei 15.353/2026'])
I(P, 1, 'Importunação x estupro de vulnerável',
  'Presente o dolo de satisfazer a lascívia, o ato libidinoso praticado com menor de 14 anos configura estupro de vulnerável, ainda que superficial, sem possibilidade de desclassificação para importunação sexual.', 'C',
  '**Tema 1.121/STJ** (08/06/2022).',
  juris=[J['T1121']], kw=['Tema 1.121/STJ'])
I(P, 1, 'Importunação sexual',
  'A importunação sexual exige que o ato libidinoso seja praticado mediante violência ou grave ameaça.', 'E',
  'Art. 215-A: basta praticar o ato **sem a anuência** da vítima, para satisfazer a lascívia. Com violência ou grave ameaça, o fato é **estupro** (subsidiariedade expressa).',
  lei=[(CP + '215-A', 'Art. 215-A. Praticar contra alguém e sem a sua anuência ato libidinoso', None, 'CP, art. 215-A, caput')],
  peg='Exigir violência na importunação.', kw=['sem a anuência'])
I(P, 1, 'Assédio sexual',
  'O assédio sexual exige que o agente se prevaleça da condição de superior hierárquico ou de ascendência inerentes ao exercício de emprego, cargo ou função.', 'C',
  'Art. 216-A: crime **próprio**; detenção de 1 a 2 anos, aumentada de até 1/3 se a vítima é menor de 18 (§ 2º).',
  lei=[(CP + '216-A', 'Art. 216-A. Constranger alguém com o intuito de obter vantagem ou favorecimento sexual', 'inerentes ao exercício de emprego, cargo ou função.', 'CP, art. 216-A, caput')],
  kw=['próprio'])
I(P, 1, 'Ação penal: liberdade sexual',
  'No estupro contra vítima maior e capaz, a ação penal é pública condicionada à representação.', 'E',
  'Art. 225 (Lei 13.718/2018): **pública incondicionada** em todos os crimes dos Capítulos I e II.',
  lei=[(CP + '225', 'Nos crimes definidos nos Capítulos I e II deste Título, procede-se mediante ação penal pública incondicionada.', None, 'CP, art. 225, caput')],
  peg='Ressuscitar a representação.', kw=['pública incondicionada'])
I(P, 1, 'Estupro qualificado pela idade',
  'O estupro é qualificado se a vítima é menor de 18 e maior de 14 anos.', 'C',
  'Art. 213, **§ 1º**: reclusão de 8 a 12 anos (também se resulta lesão grave). Menor de 14 é estupro de vulnerável.',
  lei=[(CP + '213', '§ 1o Se da conduta resulta lesão corporal de natureza grave ou se a vítima é menor de 18 (dezoito) ou maior de 14 (catorze) anos:', 'Pena - reclusão, de 8 (oito) a 12 (doze) anos.', 'CP, art. 213, § 1º')],
  kw=['§ 1º'])
I(P, 1, 'Registro da intimidade',
  'O crime de registro não autorizado da intimidade sexual (art. 216-B) só se consuma com a divulgação do conteúdo.', 'E',
  'Art. 216-B: basta **produzir, fotografar, filmar ou registrar** a cena íntima sem autorização. A divulgação é outro crime (art. 218-C).',
  lei=[(CP + '216-B', 'Art. 216-B. Produzir, fotografar, filmar ou registrar, por qualquer meio, conteúdo com cena de nudez', 'sem autorização dos participantes:', 'CP, art. 216-B, caput')],
  peg='Exigir a divulgação.', kw=['produzir, fotografar, filmar ou registrar'])
I(P, 1, 'Pornografia de vingança',
  'A pena da divulgação de cena de sexo ou nudez sem consentimento aumenta-se de um a dois terços se o agente mantém ou manteve relação íntima de afeto com a vítima ou age por vingança ou humilhação.', 'C',
  'Art. 218-C, **§ 1º** (Lei 13.718/2018). A pena base passou a 4 a 10 anos com a Lei 15.280/2025.',
  lei=[(CP + '218-C', '§ 1º A pena é aumentada de 1/3 (um terço) a 2/3 (dois terços) se o crime é praticado por agente que mantém ou tenha mantido relação íntima de afeto com a vítima', None, 'CP, art. 218-C, § 1º')],
  kw=['§ 1º', 'relação íntima de afeto'])
# --- PEN-10.7 · Rodada 2
I(P, 2, 'Corrupção de menores (art. 218)',
  'Induzir alguém menor de 14 anos a satisfazer a lascívia de outrem é punido com reclusão de 2 a 5 anos.', 'E',
  'A **Lei 15.280/2025** fixou **6 a 14 anos**, e multa (art. 218).',
  lei=[(CP + '218', 'Pena – reclusão, de 6 (seis) a 14 (quatorze) anos, e multa.', None, 'CP, art. 218 (pena)')],
  peg='Cobrar a pena anterior.', kw=['6 a 14 anos'])
I(P, 2, 'Estupro coletivo',
  'Nos crimes contra a dignidade sexual, a pena aumenta de um a dois terços se o crime é praticado mediante concurso de dois ou mais agentes.', 'C',
  'Art. 226, **IV, a** (estupro coletivo); a alínea b é o estupro corretivo.',
  lei=[(CP + '226', 'IV - de 1/3 (um terço) a 2/3 (dois terços), se o crime é praticado:', 'a) mediante concurso de 2 (dois) ou mais agentes;', 'CP, art. 226, IV, a')],
  kw=['estupro coletivo'])
I(P, 2, 'Gravidez resultante',
  'Nos crimes contra a dignidade sexual, se do crime resulta gravidez, a pena é aumentada de um sexto.', 'E',
  'Art. 234-A, **III**: aumento **de metade a 2/3**.',
  lei=[(CP + '234-A', 'III - de metade a 2/3 (dois terços), se do crime resulta gravidez;', None, 'CP, art. 234-A, III')],
  peg='Errar a fração.', kw=['de metade a 2/3'])
I(P, 2, 'Publicidade do condenado',
  'Embora os processos por crimes contra a dignidade sexual corram em segredo de justiça, o nome completo do réu e a tipificação passam a ser de acesso público a partir da condenação em primeira instância por crimes como estupro e estupro de vulnerável.', 'C',
  'Art. 234-B, **§ 1º** (Lei 15.035/2024), ressalvado o sigilo fundamentado; absolvido em grau recursal, restabelece-se o sigilo (§ 2º).',
  lei=[(CP + '234-B', '§ 1º O sistema de consulta processual tornará de acesso público o nome completo do réu', 'a partir da condenação em primeira instância', 'CP, art. 234-B, § 1º')],
  kw=['§ 1º', 'Lei 15.035/2024'])
I(P, 2, 'Vulnerável sem idade',
  'O estupro de vulnerável restringe-se às vítimas menores de 14 anos.', 'E',
  'O § 1º do art. 217-A alcança, em qualquer idade, quem **por enfermidade ou deficiência mental não tem discernimento** ou, **por qualquer outra causa, não pode oferecer resistência** (ex.: embriaguez completa).',
  lei=[(CP + '217-A', '§ 1o Incorre na mesma pena quem pratica as ações descritas no caput com alguém que, por enfermidade ou deficiência mental', 'não pode oferecer resistência.', 'CP, art. 217-A, § 1º')],
  peg='Esquecer o § 1º.', kw=['não pode oferecer resistência'])
I(P, 2, 'Cliente do adolescente explorado',
  'Incorre nas penas do favorecimento da exploração sexual de vulnerável quem pratica conjunção carnal ou outro ato libidinoso com maior de 14 e menor de 18 anos submetido à prostituição.', 'C',
  'Art. 218-B, **§ 2º, I** (pena de 7 a 16 anos desde a Lei 15.280/2025).',
  lei=[(CP + '218-B', 'I - quem pratica conjunção carnal ou outro ato libidinoso com alguém menor de 18 (dezoito) e maior de 14 (catorze) anos', None, 'CP, art. 218-B, § 2º, I')],
  kw=['§ 2º, I'])
I(P, 2, 'Casa de prostituição',
  'Manter estabelecimento em que ocorra exploração sexual só é crime se houver intuito de lucro.', 'E',
  'Art. 229: o crime existe **haja, ou não, intuito de lucro** ou mediação direta do proprietário ou gerente.',
  lei=[(CP + '229', 'Art. 229. Manter, por conta própria ou de terceiro, estabelecimento em que ocorra exploração sexual, haja, ou não, intuito de lucro', None, 'CP, art. 229')],
  peg='Exigir lucro.', kw=['haja, ou não, intuito de lucro'])

# ======================= PEN-10.8 · Crimes contra a família =======================
P = 'DBA26-PEN-10.8'
I(P, 1, 'Bigamia',
  'Comete bigamia quem, sendo casado, contrai novo casamento; quem, não sendo casado, casa com pessoa casada conhecendo essa circunstância, tem pena menor.', 'C',
  'Art. 235, caput (reclusão de 2 a 6 anos) e **§ 1º** (reclusão ou detenção de 1 a 3 anos).',
  lei=[(CP + '235', 'Art. 235 - Contrair alguém, sendo casado, novo casamento:', None, 'CP, art. 235, caput'),
       (CP + '235', '§ 1º - Aquele que, não sendo casado, contrai casamento com pessoa casada, conhecendo essa circunstância', None, 'CP, art. 235, § 1º')],
  kw=['bigamia', '§ 1º'])
I(P, 1, 'Anulação e bigamia',
  'Anulado o primeiro casamento, por qualquer motivo, subsiste o crime de bigamia já consumado.', 'E',
  'Art. 235, § 2º: anulado o primeiro casamento por qualquer motivo (ou o outro, por motivo que não a bigamia), **considera-se inexistente o crime**.',
  lei=[(CP + '235', '§ 2º - Anulado por qualquer motivo o primeiro casamento, ou o outro por motivo que não a bigamia, considera-se inexistente o crime.', None, 'CP, art. 235, § 2º')],
  peg='Manter o crime após a anulação.', kw=['inexistente o crime'])
I(P, 1, 'Abandono material',
  'Configura abandono material deixar, sem justa causa, de prover a subsistência do filho menor de 18 anos, faltando ao pagamento de pensão alimentícia judicialmente fixada.', 'C',
  'Art. **244**, caput (exige ausência de **justa causa**).',
  lei=[(CP + '244', 'faltando ao pagamento de pensão alimentícia judicialmente acordada, fixada ou majorada', None, 'CP, art. 244, caput')],
  kw=['244', 'justa causa'])
I(P, 1, 'Adoção à brasileira',
  'Registrar como seu o filho de outrem por motivo de reconhecida nobreza é fato atípico.', 'E',
  'Continua crime (art. 242), mas com **pena menor** (detenção de 1 a 2 anos) e possibilidade de **perdão judicial** (par. ún.).',
  lei=[(CP + '242', 'Parágrafo único - Se o crime é praticado por motivo de reconhecida nobreza:', 'podendo o juiz deixar de aplicar a pena.', 'CP, art. 242, par. ún.')],
  peg='Ver atipicidade no motivo nobre.', kw=['perdão judicial'])
I(P, 1, 'Induzimento a erro essencial',
  'No crime de induzimento a erro essencial e ocultação de impedimento para o casamento, a ação penal é pública incondicionada.', 'E',
  'Art. 236, par. ún.: depende de **queixa do contraente enganado**, só depois do trânsito da sentença que anula o casamento (ação privada **personalíssima**).',
  lei=[(CP + '236', 'Parágrafo único - A ação penal depende de queixa do contraente enganado', 'anule o casamento.', 'CP, art. 236, par. ún.')],
  peg='Ignorar a ação personalíssima.', kw=['personalíssima'])
# --- PEN-10.8 · Rodada 2
I(P, 2, 'Pai destituído',
  'O pai destituído do poder familiar que subtrai o filho de quem tem a guarda legal comete subtração de incapazes.', 'C',
  'Art. 249, **§ 1º**: ser pai, tutor ou curador **não exime** de pena se destituído ou privado do poder familiar, tutela, curatela ou guarda.',
  lei=[(CP + '249', '§ 1º - O fato de ser o agente pai ou tutor do menor ou curador do interdito não o exime de pena', None, 'CP, art. 249, § 1º')],
  kw=['não exime'])
I(P, 2, 'Restituição do incapaz',
  'Na subtração de incapazes, restituído o menor sem maus-tratos ou privações, extingue-se a punibilidade pelo perdão do ofendido.', 'E',
  'Art. 249, § 2º: o juiz **pode deixar de aplicar a pena** — perdão **judicial**, não perdão do ofendido (que é ato bilateral na ação privada).',
  lei=[(CP + '249', '§ 2º - No caso de restituição do menor ou do interdito, se este não sofreu maus-tratos ou privações, o juiz pode deixar de aplicar pena.', None, 'CP, art. 249, § 2º')],
  peg='Trocar perdão judicial por perdão do ofendido.', kw=['perdão judicial'])
I(P, 2, 'Pena do abandono material',
  'O abandono material é punido com reclusão de 1 a 4 anos.', 'E',
  'Art. 244: **detenção** de 1 a 4 anos e multa.',
  lei=[(CP + '244', 'Pena - detenção, de 1 (um) a 4 (quatro) anos e multa', None, 'CP, art. 244 (pena)')],
  peg='Trocar detenção por reclusão.', kw=['detenção'])

# ======================= PEN-10.9 · Crimes contra a incolumidade pública =======================
P = 'DBA26-PEN-10.9'
I(P, 1, 'Incêndio',
  'O crime de incêndio exige que a conduta exponha a perigo a vida, a integridade física ou o patrimônio de outrem, e a pena aumenta de um terço se o incêndio é em casa habitada.', 'C',
  'Art. 250, caput e § 1º, II, a: crime de **perigo concreto** e comum.',
  lei=[(CP + '250', 'Art. 250 - Causar incêndio, expondo a perigo a vida, a integridade física ou o patrimônio de outrem:', None, 'CP, art. 250, caput'),
       (CP + '250', 'a) em casa habitada ou destinada a habitação;', None, 'CP, art. 250, § 1º, II, a')],
  kw=['perigo concreto'])
I(P, 1, 'Perigo comum com morte',
  'Se do crime doloso de perigo comum resulta morte, a pena privativa de liberdade é aumentada de metade.', 'E',
  'Art. 258: lesão grave, **aumento de metade**; morte, pena **em dobro**.',
  lei=[(CP + '258', 'Art. 258 - Se do crime doloso de perigo comum resulta lesão corporal de natureza grave, a pena privativa de liberdade é aumentada de metade; se resulta morte, é aplicada em dobro.', None, 'CP, art. 258, 1ª parte')],
  peg='Trocar os resultados.', kw=['em dobro'])
I(P, 1, 'Medicamento falsificado',
  'A falsificação, corrupção, adulteração ou alteração de produto destinado a fins terapêuticos ou medicinais é crime hediondo.', 'C',
  'Lei 8.072/1990, art. 1º, **VII-B** (art. 273, caput e §§ 1º, 1º-A e 1º-B).',
  lei=[('L8072:1', 'VII-B - falsificação, corrupção, adulteração ou alteração de produto destinado a fins terapêuticos ou medicinais', None, 'Lei 8.072/1990, art. 1º, VII-B')],
  kw=['VII-B'])
I(P, 1, 'Importação sem registro',
  'Segundo o STF, a pena de 10 a 15 anos do art. 273 do Código Penal aplica-se integralmente a quem importa ou vende medicamento sem registro na vigilância sanitária.', 'E',
  '**Tema 1.003/RG** (RE 979.962): é **inconstitucional** essa pena para o § 1º-B, I; vale a pena originária, **1 a 3 anos**, e multa.',
  lei=[(CP + '273', 'I - sem registro, quando exigível, no órgão de vigilância sanitária competente;', None, 'CP, art. 273, § 1º-B, I')],
  juris=[J['RG1003']], peg='Aplicar a pena de 10 a 15 anos.', kw=['Tema 1.003/RG'])
I(P, 1, 'Exercício ilegal durante suspensão',
  'Pela redação de 2026, incorre no exercício ilegal da medicina o profissional que exerce a profissão durante a suspensão ou após o cancelamento da habilitação ou do registro.', 'C',
  'Art. 282, **§ 5º**, incluído pela Lei 15.425/2026 (que também passou a abranger o médico veterinário).',
  lei=[(CP + '282', '§ 5º Incorre na conduta prevista no caput deste artigo o agente que exerce a profissão durante o período de suspensão', None, 'CP, art. 282, § 5º')],
  kw=['§ 5º', 'Lei 15.425/2026'])
I(P, 1, 'Curandeirismo e remuneração',
  'O curandeirismo só é crime se praticado mediante remuneração.', 'E',
  'A remuneração só **acrescenta multa** (art. 284, par. ún.); o crime existe também a título gratuito.',
  lei=[(CP + '284', 'Parágrafo único - Se o crime é praticado mediante remuneração, o agente fica também sujeito à multa.', None, 'CP, art. 284, par. ún.')],
  peg='Exigir remuneração.', kw=['acrescenta multa'])
# --- PEN-10.9 · Rodada 2
I(P, 2, 'Serviço telefônico',
  'Interromper ou perturbar serviço telefônico é punido com reclusão de 2 a 4 anos, e multa, aplicadas em dobro se cometido por ocasião de calamidade pública.', 'C',
  'Art. 266, caput e **§ 2º, I**, na redação da **Lei 15.397/2026** (antes, detenção de 1 a 3 anos).',
  lei=[(CP + '266', 'Pena – reclusão, de 2 (dois) a 4 (quatro) anos, e multa.', None, 'CP, art. 266, caput (pena)'),
       (CP + '266', '§ 2º Aplicam-se as penas em dobro se o crime é cometido:', 'I – por ocasião de calamidade pública;', 'CP, art. 266, § 2º, I')],
  kw=['Lei 15.397/2026'])
I(P, 2, 'Epidemia culposa',
  'Na epidemia culposa da qual resulta morte, a pena é aplicada em dobro.', 'E',
  'O dobro é da **dolosa** com morte (§ 1º). Na **culposa**, detenção de 1 a 2 anos, ou, se resulta morte, **2 a 4 anos** (§ 2º).',
  lei=[(CP + '267', '§ 2º - No caso de culpa, a pena é de detenção, de um a dois anos, ou, se resulta morte, de dois a quatro anos.', None, 'CP, art. 267, § 2º')],
  peg='Aplicar o dobro à forma culposa.', kw=['culposa'])
I(P, 2, 'Exercício ilegal com morte',
  'Se do exercício ilegal da medicina resulta morte, o agente responde também pelo crime de homicídio.', 'C',
  'Art. 282, **§ 3º** (Lei 15.425/2026); lesão grave ou gravíssima, art. 129, §§ 1º e 2º (§ 2º).',
  lei=[(CP + '282', '§ 3º Se do crime resulta morte, responde também o agente pelo crime de homicídio, nos termos do art. 121 deste Código.', None, 'CP, art. 282, § 3º')],
  kw=['§ 3º'])
I(P, 2, 'Charlatanismo',
  'O charlatanismo consiste em exercer o curandeirismo fazendo diagnósticos.', 'E',
  'Charlatanismo (art. 283) é **inculcar ou anunciar cura por meio secreto ou infalível**; fazer diagnósticos é uma das formas do curandeirismo (art. 284, III).',
  lei=[(CP + '283', 'Art. 283 - Inculcar ou anunciar cura por meio secreto ou infalível:', None, 'CP, art. 283')],
  peg='Confundir charlatanismo com curandeirismo.', kw=['meio secreto ou infalível'])

# ======================= PEN-10.10 · Crimes contra a paz pública =======================
P = 'DBA26-PEN-10.10'
I(P, 1, 'Associação criminosa',
  'Configura associação criminosa a associação de três ou mais pessoas para o fim específico de cometer crimes.', 'C',
  'Art. 288 (Lei 12.850/2013): crime **formal** e **permanente**, que independe da prática dos crimes visados.',
  lei=[(CP + '288', 'Art. 288. Associarem-se 3 (três) ou mais pessoas, para o fim específico de cometer crimes:', None, 'CP, art. 288, caput')],
  kw=['formal', 'permanente'])
I(P, 1, 'Número mínimo',
  'A associação criminosa do art. 288 do Código Penal exige ao menos quatro integrantes.', 'E',
  'Bastam **três**. Quatro ou mais, com estrutura ordenada e divisão de tarefas, é a **organização criminosa** da Lei 12.850/2013.',
  lei=[(CP + '288', 'Art. 288. Associarem-se 3 (três) ou mais pessoas', None, 'CP, art. 288, caput')],
  peg='Confundir com a organização criminosa.', kw=['três', 'organização criminosa'])
I(P, 1, 'Associação armada',
  'A pena da associação criminosa aumenta-se até a metade se a associação é armada ou se houver participação de criança ou adolescente.', 'C',
  'Art. 288, **§ 1º** (renumerado pela Lei 15.245/2025).',
  lei=[(CP + '288', '§ 1º A pena aumenta-se até a metade se a associação é armada ou se houver a participação de criança ou adolescente.', None, 'CP, art. 288, § 1º')],
  kw=['§ 1º'])
I(P, 1, 'Incitação ao crime',
  'O crime de incitação ao crime só se consuma se alguém efetivamente praticar o crime incitado.', 'E',
  'Art. 286: basta **incitar publicamente**; é crime **formal** e de perigo, consumado com a incitação perceptível por número indeterminado de pessoas (doutrina).',
  lei=[(CP + '286', 'Art. 286 - Incitar, publicamente, a prática de crime:', None, 'CP, art. 286, caput')],
  peg='Exigir a prática do crime incitado.', kw=['incitar publicamente'])
I(P, 1, 'Milícia privada',
  'A constituição de milícia privada exige que o grupo se destine à prática de crimes hediondos.', 'E',
  'Art. 288-A: finalidade de praticar **qualquer dos crimes previstos neste Código**.',
  lei=[(CP + '288-A', 'Art. 288-A. Constituir, organizar, integrar, manter ou custear organização paramilitar', 'com a finalidade de praticar qualquer dos crimes previstos neste Código:', 'CP, art. 288-A')],
  peg='Restringir aos hediondos.', kw=['qualquer dos crimes previstos neste Código'])
# --- PEN-10.10 · Rodada 2
I(P, 2, 'Contratar a associação',
  'Incorre na pena da associação criminosa quem solicita ou contrata o cometimento de crime a integrante de associação criminosa, sem prejuízo da pena do crime encomendado.', 'C',
  'Art. 288, **§ 2º**, incluído pela Lei 15.245/2025.',
  lei=[(CP + '288', '§ 2º Incorre na pena prevista no caput deste artigo quem, de qualquer modo, solicitar ou contratar o cometimento de crime a integrante de associação criminosa', None, 'CP, art. 288, § 2º')],
  kw=['§ 2º', 'Lei 15.245/2025'])
I(P, 2, 'Apologia',
  'O crime de apologia exige que o elogio se refira a autor já condenado por sentença definitiva.', 'E',
  'Art. 287: apologia de **fato criminoso** ou de **autor de crime** — o tipo não exige condenação definitiva.',
  lei=[(CP + '287', 'Art. 287 - Fazer, publicamente, apologia de fato criminoso ou de autor de crime:', None, 'CP, art. 287')],
  peg='Exigir condenação.', kw=['fato criminoso'])
I(P, 2, 'Animosidade nas Forças Armadas',
  'Incorre na pena da incitação ao crime quem incita, publicamente, animosidade entre as Forças Armadas ou delas contra os poderes constitucionais.', 'C',
  'Art. 286, **par. ún.** (Lei 14.197/2021, que revogou a Lei de Segurança Nacional).',
  lei=[(CP + '286', 'Parágrafo único. Incorre na mesma pena quem incita, publicamente, animosidade entre as Forças Armadas', None, 'CP, art. 286, par. ún.')],
  kw=['par. ún.', 'Lei 14.197/2021'])
