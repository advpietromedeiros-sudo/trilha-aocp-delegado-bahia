# Pente Fino de Medicina Legal — pontos MLE-4 e MLE-5 a MLE-5.5 (07/11/2026).
# Doutrina em redação própria; tempos de fenômenos cadavéricos variam entre autores — o comentário diz quando.
from base import I
from mle_juris import J

CPP = 'CPP:'
CP = 'CP:'
CC = 'L10406:'

# ======================= MLE-4 · Traumatologia: instrumentos e projéteis =======================
P = 'DBA26-MLE-4'
I(P, 1, 'Ação contundente',
  'O instrumento contundente age por pressão, percussão, compressão, tração ou atrito, e produz lesões como rubefação, escoriação, equimose, hematoma, ferida contusa e fratura.', 'C',
  'O agente **contundente** atua por superfície, sem gume nem ponta. A **escoriação** (atrito que arranca a epiderme) e a **ferida contusa** (bordas irregulares, pontes de tecido no fundo) são lesões típicas.',
  kw=['contundente', 'ferida contusa'])
I(P, 1, 'Trajetória do projétil',
  'A trajetória do projétil no interior do corpo pode desviar ao encontrar ossos e depende da posição da vítima, razão pela qual não coincide necessariamente com a linha de tiro.', 'C',
  'Distinga **trajetória** (percurso fora do corpo) e **trajeto** (percurso dentro dele). Ossos desviam e fragmentam o projétil; a postura da vítima muda a leitura.',
  kw=['trajetória', 'trajeto'])
I(P, 1, 'Ferida incisa',
  'A ferida incisa, de bordas regulares e comprimento maior que a profundidade, é produzida tipicamente por instrumento perfurante.', 'E',
  'A **ferida incisa** é produzida por instrumento **cortante** (gume que desliza): bordas regulares, sem pontes de tecido, extremidade final com **cauda de escoriação**.',
  peg='Trocar cortante por perfurante.',
  kw=['ferida incisa', 'cortante'])
I(P, 1, 'Instrumento perfurante',
  'Instrumentos perfurantes de pequeno calibre, como a agulha, produzem lesão puntiforme, em que a profundidade predomina sobre a abertura na pele.', 'C',
  'O **perfurante** age por ponta, afastando as fibras: ferida **punctória** (puntiforme), estreita e profunda.',
  kw=['perfurante', 'puntiforme'])
I(P, 1, 'Perfurocortante de um gume',
  'A faca de um só gume produz ferida perfuroincisa com as duas extremidades em ângulo agudo.', 'E',
  'Com **um gume**, a ferida perfuroincisa tem **uma extremidade aguda** (lado do gume) e **outra romba** (lado do dorso). Duas extremidades agudas sugerem **dois gumes**.',
  peg='Atribuir ao instrumento de um gume o desenho do de dois gumes.',
  kw=['perfuroincisa', 'um gume'])
I(P, 1, 'Cortocontundente',
  'Machado, foice e facão pesado são instrumentos cortocontundentes: agem pelo gume e pelo peso, produzindo feridas cortocontusas, muitas vezes com lesão óssea.', 'C',
  'O **cortocontundente** soma gume e massa: a ferida tem algo de incisa e de contusa, com fraturas e até amputações.',
  kw=['cortocontundente', 'cortocontusa'])
I(P, 1, 'Orifício de entrada',
  'No orifício de entrada típico de projétil de arma de fogo encontram-se a orla de escoriação (contusão) e a orla de enxugo, causada pela limpeza do projétil na borda da pele.', 'C',
  'Na **entrada**: orifício em regra menor, bordas invertidas, **orla de escoriação** e **orla de enxugo**, presentes a qualquer distância.',
  kw=['orifício de entrada', 'orla de enxugo'])
I(P, 1, 'Orifício de saída',
  'O orifício de saída típico apresenta orla de escoriação e orla de enxugo, com bordas invertidas.', 'E',
  'A **saída** típica é maior, irregular, de **bordas evertidas** e **sem orlas**. Exceção: saída apoiada em superfície rígida pode ter orla de escoriação ("saída falsa").',
  exc=['Saída com a pele apoiada em plano rígido (parede, cinto, encosto) pode exibir orla de escoriação'],
  peg='Transportar para a saída os sinais da entrada.',
  kw=['orifício de saída', 'bordas evertidas'])
I(P, 1, 'Tatuagem × esfumaçamento',
  'Nos disparos a curta distância, a zona de tatuagem, formada por grãos de pólvora, pode ser removida pela simples lavagem da pele.', 'E',
  'A **tatuagem** é feita por grãos **incrustados** na pele: não sai com lavagem. O que sai é o **esfumaçamento** (fuligem depositada).',
  peg='Trocar tatuagem por esfumaçamento.',
  kw=['tatuagem', 'esfumaçamento'])
I(P, 1, 'Tiro encostado',
  'No tiro encostado firmemente à pele, formam-se ao redor do orifício de entrada amplas zonas de tatuagem e esfumaçamento.', 'E',
  'No **tiro encostado**, gases e resíduos vão **para dentro** do ferimento: não há tatuagem nem esfumaçamento externos; sobre plano ósseo forma-se a **câmara de mina de Hoffmann** (orifício estrelado), às vezes com a marca do cano (**Werkgaertner**).',
  peg='Atribuir ao encostado o desenho do tiro a curta distância.',
  kw=['tiro encostado', 'câmara de mina'])

# --- MLE-4 · Rodada 2
I(P, 2, 'Leis de Filhos e de Langer',
  'Pela lei de Langer, a ferida por instrumento perfurante de médio calibre situada em região de cruzamento de linhas de força pode assumir forma triangular ou de ponta de seta.', 'C',
  'As **leis de Filhos** dizem que o perfurante de médio calibre deixa fenda em "botoeira" orientada pelas linhas de força da região; a **lei de Langer** trata das áreas em que essas linhas se cruzam, onde a ferida fica triangular ou em ponta de seta.',
  kw=['lei de Langer', 'leis de Filhos'])
I(P, 2, 'Cauda de escoriação',
  'Na ferida incisa, a cauda de escoriação indica o ponto de início do corte.', 'E',
  'A **cauda de escoriação** marca o **fim** do corte: o gume entra mais fundo e sai superficial, arranhando a pele. Ajuda a saber o sentido do golpe.',
  peg='Trocar o final pelo início do movimento.',
  kw=['cauda de escoriação', 'fim do corte'])
I(P, 2, 'Sinal de Bonnet',
  'No crânio, o orifício de entrada do projétil mostra bisel na tábua interna, e o de saída, bisel na tábua externa, o que permite indicar o sentido do disparo.', 'C',
  'É o **sinal de Bonnet** (cone que se abre no sentido do trajeto): **entrada** — bisel **interno**; **saída** — bisel **externo**.',
  kw=['sinal de Bonnet', 'bisel'])
I(P, 2, 'Benassi × Werkgaertner',
  'O sinal de Benassi consiste na impressão da boca do cano e da massa de mira na pele, em tiro encostado.', 'E',
  'A marca do cano na pele é o **sinal de Werkgaertner**. **Benassi** é o halo de **fuligem no osso** subjacente, também no tiro encostado.',
  peg='Trocar os epônimos do tiro encostado.',
  kw=['Werkgaertner', 'Benassi'])
I(P, 2, 'Projéteis múltiplos',
  'Nos disparos com projéteis múltiplos, a dispersão dos balins (rosa de tiro de Cevidalli) tende a aumentar com a distância, mas a conversão em distância exata exige teste com a mesma arma e munição.', 'C',
  'Quanto mais longe, maior a **rosa de tiro**; o choke, a arma e a munição mudam a abertura — por isso a estimativa depende de **ensaio comparativo**.',
  kw=['rosa de tiro', 'balins'])
I(P, 2, 'Esgorjamento × degolamento',
  'Esgorjamento é a lesão cortante ou cortocontusa da região posterior do pescoço, também chamada nuca.', 'E',
  '**Esgorjamento** atinge a face **anterior** ou lateral do pescoço; **degolamento** é a lesão da região **posterior**; **decapitação** é a separação da cabeça.',
  peg='Trocar anterior por posterior.',
  kw=['esgorjamento', 'degolamento'])
I(P, 2, 'Energia do projétil e cavitação',
  'Projéteis de alta energia produzem cavidade temporária ampla ao atravessar os tecidos, lesando estruturas situadas fora do trajeto direto.', 'C',
  'A energia transferida depende sobretudo da **velocidade**; a **cavitação** temporária lesa órgãos à distância do trajeto, típica dos projéteis de alta energia.',
  kw=['cavitação', 'alta energia'])
I(P, 2, 'Espectro equimótico',
  'Pelo espectro equimótico clássico, a equimose passa de vermelha a violácea, azulada, amarelada e, por último, esverdeada.', 'E',
  'A sequência clássica é **vermelho → violáceo → azul → esverdeado → amarelado**, até desaparecer. Os prazos de cada cor variam entre autores e a cor isolada **não data** a lesão com precisão.',
  peg='Inverter as duas últimas cores.',
  kw=['espectro equimótico', 'esverdeado', 'amarelado'])

# ======================= MLE-5 · Conceito e diagnóstico da morte =======================
P = 'DBA26-MLE-5'
I(P, 1, 'Morte encefálica e transplante',
  'A retirada post mortem de órgãos para transplante deve ser precedida de diagnóstico de morte encefálica, constatada e registrada por dois médicos não participantes das equipes de remoção e transplante.', 'C',
  'Lei 9.434/1997, art. 3º: **dois médicos**, **fora das equipes** de remoção e transplante, com critérios do CFM.',
  lei=[('L9434:3', 'A retirada post mortem de tecidos', 'definidos por resolução do Conselho Federal de Medicina.', 'Lei 9.434/1997, art. 3º')],
  kw=['morte encefálica', 'dois médicos'])
I(P, 1, 'Médico da equipe de transplante',
  'A morte encefálica do doador pode ser constatada por médico integrante da equipe de transplante, desde que acompanhado de outro médico.', 'E',
  'A lei exige que os dois médicos sejam **não participantes** das equipes de **remoção e transplante** — conflito de interesse evidente.',
  lei=[('L9434:3', 'A retirada post mortem de tecidos', 'definidos por resolução do Conselho Federal de Medicina.', 'Lei 9.434/1997, art. 3º')],
  peg='Admitir um membro da equipe se "acompanhado".',
  kw=['não participantes', 'equipe de transplante'])
I(P, 1, 'Morte como processo',
  'A morte se desenrola como processo gradual, não como instante único; por isso a medicina adota critérios para fixar o momento a partir do qual ela é tida como irreversível.', 'C',
  'Os tecidos morrem em tempos diferentes; o Direito precisa de um marco — hoje, para fins de transplante, a **morte encefálica**, segundo resolução do CFM (Res. 2.173/2017).',
  kw=['processo', 'irreversível'])
I(P, 1, 'Sinais abióticos imediatos',
  'Perda da consciência, imobilidade, parada respiratória e parada circulatória são sinais abióticos imediatos e, por si sós, dão certeza da morte.', 'E',
  'Os **sinais abióticos imediatos** são de **probabilidade** (incerteza): aparecem também na morte aparente. **Certeza** dão os sinais **consecutivos** (livores, rigidez, resfriamento, desidratação) e os transformativos.',
  peg='Trocar probabilidade por certeza.',
  kw=['sinais abióticos imediatos', 'probabilidade'])
I(P, 1, 'Morte aparente',
  'Na morte aparente, a atividade vital fica tão deprimida que escapa ao exame superficial, situação descrita, por exemplo, em eletroplessão, afogamento, catalepsia e intoxicação por barbitúricos.', 'C',
  'A **morte aparente** é estado de vida mínima; por isso os sinais imediatos não bastam e o diagnóstico exige sinais de certeza ou exames.',
  kw=['morte aparente', 'catalepsia'])
I(P, 1, 'Médico de confiança da família',
  'Na comprovação da morte encefálica para fins de transplante, é vedada a presença de médico de confiança da família do falecido.', 'E',
  'A lei **admite** a presença de **médico de confiança da família** no ato (art. 3º, § 3º).',
  lei=[('L9434:3', 'Será admitida a presença de médico de confiança da família', 'atestação da morte encefálica.', 'Lei 9.434/1997, art. 3º, § 3º')],
  peg='Trocar "admitida" por "vedada".',
  kw=['médico de confiança da família', 'admitida'])
I(P, 1, 'Evidência dos sinais de morte',
  'A autópsia pode ser feita antes de seis horas do óbito se os peritos, pela evidência dos sinais de morte, julgarem possível, o que declararão no auto.', 'C',
  'O prazo de **seis horas** existe para afastar a morte aparente; sinais evidentes de morte autorizam antecipar.',
  lei=[(CPP + '162', 'A autópsia será feita pelo menos seis horas depois do óbito', 'o que declararão no auto.', 'CPP, art. 162')],
  kw=['seis horas', 'evidência dos sinais de morte'])
I(P, 1, 'Protocolo de morte encefálica',
  'Para o diagnóstico de morte encefálica, basta um exame clínico realizado por um médico capacitado, sendo dispensáveis o teste de apneia e o exame complementar.', 'E',
  'A resolução do CFM em vigor exige **dois exames clínicos** por **médicos diferentes**, **teste de apneia** e **exame complementar** que mostre ausência de atividade encefálica (perfusão, metabolismo ou atividade elétrica).',
  peg='Reduzir o protocolo a um exame e um médico.',
  kw=['dois exames clínicos', 'teste de apneia'])

# --- MLE-5 · Rodada 2
I(P, 2, 'Observação mínima',
  'Pela resolução do CFM sobre morte encefálica, o paciente deve ser tratado e observado em hospital por no mínimo seis horas, prazo ampliado para vinte e quatro horas quando a causa for encefalopatia hipóxico-isquêmica.', 'C',
  'Pré-requisitos (Res. CFM 2.173/2017): lesão encefálica de causa conhecida e irreversível; ausência de fatores tratáveis que confundam; **6 horas** de observação (**24 horas** na encefalopatia hipóxico-isquêmica); parâmetros mínimos de temperatura, saturação e pressão.',
  kw=['seis horas', 'encefalopatia hipóxico-isquêmica'])
I(P, 2, 'Morte encefálica × estado vegetativo',
  'A morte encefálica corresponde à perda das funções do córtex cerebral com preservação do tronco encefálico.', 'E',
  'Perda do córtex com **tronco preservado** é o **estado vegetativo**, que não é morte. A **morte encefálica** é a perda irreversível de **todo o encéfalo, incluindo o tronco**.',
  peg='Descrever o estado vegetativo e chamá-lo de morte encefálica.',
  kw=['morte encefálica', 'tronco encefálico'])
I(P, 2, 'Prova de Icard',
  'Na prova de Icard, a injeção subcutânea de fluoresceína que não se difunde pelo organismo indica cessação da circulação.', 'C',
  'Na **prova de Icard**, com circulação a fluoresceína tinge pele e mucosas; sem difusão, a circulação cessou.',
  kw=['prova de Icard', 'fluoresceína'])
I(P, 2, 'Autorização para retirada',
  'A retirada de órgãos de pessoa falecida depende da autorização do cônjuge ou de parente maior de idade, na linha reta ou colateral até o terceiro grau.', 'E',
  'O limite é o **segundo grau**, inclusive, com documento subscrito por duas testemunhas presentes à verificação da morte.',
  lei=[('L9434:4', 'A retirada de tecidos, órgãos e partes do corpo de pessoas falecidas', 'presentes à verificação da morte.', 'Lei 9.434/1997, art. 4º')],
  peg='Trocar segundo por terceiro grau.',
  kw=['segundo grau', 'autorização'])
I(P, 2, 'Teste de apneia',
  'O teste de apneia integra obrigatoriamente o protocolo de determinação da morte encefálica.', 'C',
  'O **teste de apneia** verifica a ausência de estímulo respiratório do tronco com hipercapnia; é etapa obrigatória.',
  kw=['teste de apneia', 'tronco'])
I(P, 2, 'Sinais de Winslow e de Rebouillat',
  'O sinal de Winslow consiste em injetar éter no tecido subcutâneo da coxa e observar se ele reflui pelo orifício da agulha.', 'E',
  'A injeção de éter é o **sinal de Rebouillat**. **Winslow** é a prova do espelho ou da chama diante das narinas, para verificar a respiração.',
  peg='Trocar os epônimos.',
  kw=['Winslow', 'Rebouillat'])

# ======================= MLE-5.1 · Fenômenos cadavéricos =======================
P = 'DBA26-MLE-5.1'
I(P, 1, 'Abióticos consecutivos',
  'Desidratação, resfriamento, livores e rigidez são fenômenos cadavéricos abióticos consecutivos, também chamados mediatos.', 'C',
  'Os **abióticos consecutivos** surgem horas depois e dão **certeza** da morte; depois vêm os **transformativos** (destrutivos e conservadores).',
  kw=['abióticos consecutivos', 'livores'])
I(P, 1, 'Localização dos livores',
  'Os livores cadavéricos formam-se nas partes mais elevadas do corpo, de acordo com a posição do cadáver.', 'E',
  'Os **livores** se formam nas **regiões de declive**: o sangue, ainda dentro dos vasos, desce pela gravidade.',
  peg='Trocar declive por partes elevadas.',
  kw=['livores', 'declive'])
I(P, 1, 'Áreas poupadas',
  'Os livores poupam as áreas do corpo comprimidas contra o plano de apoio, que permanecem pálidas.', 'C',
  'A **compressão** fecha os capilares e o sangue não se acumula ali: as áreas de apoio ficam claras.',
  kw=['compressão', 'livores'])
I(P, 1, 'Lei de Nysten',
  'A rigidez cadavérica instala-se em sentido podálico-cefálico, começando pelos membros inferiores e terminando na mandíbula.', 'E',
  'Pela **lei de Nysten**, a rigidez segue sentido **crânio-caudal**: mandíbula e nuca, membros superiores, tronco, membros inferiores — e se desfaz na **mesma ordem**.',
  peg='Inverter o sentido.',
  kw=['lei de Nysten', 'crânio-caudal'])
I(P, 1, 'Espasmo cadavérico',
  'O espasmo cadavérico fixa instantaneamente a última atitude do indivíduo no momento da morte, sem a fase de relaxamento muscular que precede a rigidez comum.', 'C',
  'O **espasmo cadavérico** (rigidez cataléptica) é raro, imediato e localizado ou geral; não passa pela flacidez inicial.',
  kw=['espasmo cadavérico', 'rigidez cataléptica'])
I(P, 1, 'Mancha verde abdominal',
  'A mancha verde abdominal, primeiro sinal da putrefação, surge em regra na fossa ilíaca esquerda.', 'E',
  'Surge na **fossa ilíaca direita**, onde está o **ceco**, rico em bactérias e gases.',
  peg='Trocar o lado.',
  kw=['mancha verde abdominal', 'fossa ilíaca direita'])
I(P, 1, 'Fases da putrefação',
  'A putrefação evolui pelos períodos cromático, gasoso, coliquativo e de esqueletização.', 'C',
  'Ordem: **cromático** (mancha verde) → **gasoso** (enfisema, circulação póstuma) → **coliquativo** (liquefação das partes moles) → **esqueletização**.',
  kw=['putrefação', 'período gasoso'])
I(P, 1, 'Saponificação × mumificação',
  'A saponificação é favorecida por ambiente seco, quente e bem arejado.', 'E',
  'Seco, quente e arejado favorece a **mumificação**. A **saponificação** (adipocera) exige ambiente **úmido**, pouco arejado, em geral solo argiloso.',
  peg='Trocar as condições dos dois fenômenos conservadores.',
  kw=['saponificação', 'mumificação'])
I(P, 1, 'Maceração',
  'A maceração ocorre em corpos submersos em meio líquido e no feto morto retido no útero.', 'C',
  '**Maceração** séptica (submersos) e asséptica (feto retido): a pele se descola e as partes moles amolecem.',
  kw=['maceração', 'feto retido'])

# --- MLE-5.1 · Rodada 2
I(P, 2, 'Livor × equimose',
  'À incisão, o sangue do livor escoa e a área pode ser lavada, ao passo que na equimose o sangue infiltra o tecido e não sai com a lavagem.', 'C',
  'O **livor** é sangue **dentro dos vasos**; a **equimose** é sangue **extravasado** e coagulado no tecido. É o teste prático para distingui-los.',
  kw=['livor', 'equimose'])
I(P, 2, 'Livores e hipóstases',
  'Os livores resultam do extravasamento de sangue para fora dos vasos, mecanismo idêntico ao das equimoses.', 'E',
  'Nos **livores** o sangue fica **intravascular**, acumulado pela gravidade. Os livores são as **hipóstases** da pele; nas vísceras o mesmo fenômeno se chama hipóstase visceral.',
  peg='Igualar o mecanismo de livor e equimose.',
  kw=['hipóstases', 'intravascular'])
I(P, 2, 'Mancha verde nos afogados',
  'Nos afogados, a mancha verde da putrefação começa, em regra, na fossa ilíaca direita, como nos demais cadáveres.', 'E',
  'Nos **afogados**, a mancha verde começa na **cabeça e no tórax** (parte alta do corpo), pela posição na água e pela flora aspirada.',
  exc=['No feto morto retido e nos afogados o início foge à fossa ilíaca direita'],
  peg='Aplicar a regra geral onde ela tem exceção.',
  kw=['afogados', 'mancha verde'])
I(P, 2, 'Circulação póstuma de Brouardel',
  'A circulação póstuma de Brouardel, desenho venoso arborizado na pele, é sinal do período gasoso da putrefação.', 'C',
  'Os **gases** empurram o sangue hemolisado pelas veias superficiais, que se desenham na pele.',
  kw=['circulação póstuma', 'período gasoso'])
I(P, 2, 'Cor dos livores',
  'Na intoxicação por monóxido de carbono, os livores podem apresentar cor vermelho-clara ou carminada.', 'C',
  'A **carboxiemoglobina** dá cor rosada/carminada; cianeto e frio também podem clarear os livores.',
  kw=['monóxido de carbono', 'carminada'])
I(P, 2, 'Adipocera',
  'A adipocera é um fenômeno transformativo destrutivo, pois decompõe a gordura do cadáver.', 'E',
  'A **adipocera** (saponificação) é fenômeno **conservador**: transforma a gordura em substância que preserva formas e até lesões.',
  regra='Conservadores: mumificação, saponificação, corificação, calcificação. Destrutivos: autólise, putrefação, maceração.',
  peg='Trocar conservador por destrutivo.',
  kw=['adipocera', 'conservador'])
I(P, 2, 'Mancha de Sommer-Larcher',
  'A mancha de Sommer-Larcher é a opacificação da córnea causada pela putrefação.', 'E',
  'A **mancha de Sommer-Larcher** é escurecimento da **esclerótica** por **desidratação** (fenômeno abiótico consecutivo), não sinal de putrefação.',
  peg='Trocar esclerótica por córnea e desidratação por putrefação.',
  kw=['Sommer-Larcher', 'desidratação'])

# ======================= MLE-5.2 · Cronotanatognose, comoriência e premoriência =======================
P = 'DBA26-MLE-5.2'
I(P, 1, 'Cronotanatognose',
  'A cronotanatognose estima o tempo decorrido desde a morte pela análise conjunta dos fenômenos cadavéricos, e o resultado é sempre aproximado.', 'C',
  'A **cronotanatognose** combina temperatura, livores, rigidez, putrefação, fauna e dados da cena; nenhum fenômeno isolado dá a hora exata.',
  kw=['cronotanatognose', 'aproximado'])
I(P, 1, 'Temperatura e hora exata',
  'A medida da temperatura retal permite fixar com exatidão a hora da morte, independentemente das condições do ambiente.', 'E',
  'O **resfriamento** depende de ambiente, roupas, massa corporal e causa da morte: dá só **estimativa**.',
  peg='Transformar estimativa em exatidão.',
  kw=['resfriamento', 'estimativa'])
I(P, 1, 'Comoriência',
  'Se dois ou mais indivíduos falecerem na mesma ocasião, não se podendo averiguar se algum precedeu aos outros, presumir-se-ão simultaneamente mortos.', 'C',
  'É a **comoriência** do art. 8º do Código Civil: entre comorientes não há transmissão de herança.',
  lei=[(CC + '8', 'Se dois ou mais indivíduos falecerem na mesma ocasião', 'simultaneamente mortos.', 'CC, art. 8º')],
  kw=['comoriência', 'simultaneamente mortos'])
I(P, 1, 'Premoriência',
  'Pela premoriência, presume-se que o mais idoso morreu antes dos demais.', 'E',
  '**Premoriência** é a situação em que se **prova** que um morreu antes do outro. O direito brasileiro **não presume** ordem por idade; sem prova, aplica-se a comoriência.',
  lei=[(CC + '8', 'Se dois ou mais indivíduos falecerem na mesma ocasião', 'simultaneamente mortos.', 'CC, art. 8º')],
  peg='Importar a presunção por idade de outros sistemas.',
  kw=['premoriência', 'comoriência'])
I(P, 1, 'Livores e corpo movido',
  'Livores fixos em regiões que não são de declive na posição em que o cadáver foi encontrado sugerem que o corpo foi movimentado depois da fixação.', 'C',
  'Livores **fixos** não migram: se não batem com a posição atual, o corpo foi **mudado de posição** depois de algumas horas.',
  kw=['livores fixos', 'corpo movimentado'])
I(P, 1, 'Mancha verde e tempo',
  'A mancha verde abdominal costuma surgir nas primeiras seis horas após a morte.', 'E',
  'A **mancha verde** aparece, em regra, por volta de **18 a 24 horas** (há autores que falam em 24 a 36 horas), conforme o clima.',
  peg='Antecipar muito o prazo.',
  kw=['mancha verde', '24 horas'])
I(P, 1, 'Cronologia da rigidez',
  'A rigidez cadavérica começa em regra pela mandíbula, nas primeiras horas, generaliza-se em torno de seis a oito horas e se desfaz com o início da putrefação.', 'C',
  'Faixas mais cobradas: início em 1–2 h (mandíbula e nuca), generalização em 6–8 h, resolução a partir de 24–36 h. Os números variam entre autores e com a temperatura.',
  kw=['rigidez cadavérica', 'mandíbula'])
I(P, 1, 'Ritmo do resfriamento',
  'Nas primeiras horas após a morte, o cadáver perde em média 3,5 °C por hora.', 'E',
  'A estimativa clássica é de cerca de **0,5 °C por hora** nas primeiras horas e por volta de **1 °C por hora** depois, até igualar o ambiente — números aproximados, que variam entre autores.',
  peg='Inflar o ritmo de queda da temperatura.',
  kw=['resfriamento', '0,5 °C por hora'])

# --- MLE-5.2 · Rodada 2
I(P, 2, 'Migração e fixação dos livores',
  'Antes de se fixarem, os livores mudam de lugar se o cadáver for movimentado; a fixação ocorre, segundo a doutrina mais cobrada, por volta de oito a doze horas.', 'C',
  'Os **livores** aparecem nas primeiras horas e **fixam-se** em torno de **8 a 12 h**; antes disso migram. Há autores que dão prazos um pouco diferentes.',
  kw=['livores', 'fixação'])
I(P, 2, 'Período de incerteza de Tourdes',
  'O período de incerteza de Tourdes corresponde aos primeiros quinze minutos após a morte, em que ainda há reação vital nos tecidos.', 'E',
  'O **período de incerteza de Tourdes** é a faixa de algumas horas **em torno da morte** (a doutrina costuma citar cerca de seis horas antes e depois) em que é difícil dizer se a lesão foi feita em vida ou após a morte.',
  peg='Encolher o intervalo e mudar sua natureza.',
  kw=['Tourdes', 'período de incerteza'])
I(P, 2, 'Reação vital',
  'Infiltração hemorrágica, coagulação do sangue, retração das bordas da ferida e reação inflamatória indicam que a lesão foi produzida em vida.', 'C',
  'São **sinais de reação vital**; lesões feitas após a morte não os têm (salvo no período de incerteza).',
  kw=['reação vital', 'infiltração hemorrágica'])
I(P, 2, 'Cristais de Westenhöffer-Rocha-Valverde',
  'Os cristais de Westenhöffer-Rocha-Valverde aparecem no sangue putrefeito já no primeiro dia após a morte.', 'E',
  'Esses cristais surgem a partir do **terceiro dia** e podem ser vistos por cerca de um mês; servem para datar mortes de alguns dias.',
  peg='Antecipar o surgimento.',
  kw=['cristais', 'terceiro dia'])
I(P, 2, 'Entomologia forense',
  'A entomologia forense estima o intervalo pós-morte pela sucessão de insetos que colonizam o cadáver.', 'C',
  'A **fauna cadavérica** chega em ondas previsíveis (as legiões descritas na doutrina clássica); o ciclo das larvas ajuda a datar mortes de dias ou semanas.',
  kw=['entomologia forense', 'fauna cadavérica'])
I(P, 2, 'Comoriência e lugar',
  'A comoriência só se aplica se os falecidos estiverem no mesmo lugar no momento da morte.', 'E',
  'O art. 8º fala em "**mesma ocasião**", não em mesmo lugar; a posição majoritária admite comoriência entre pessoas em locais diversos, se não se puder provar a ordem das mortes.',
  lei=[(CC + '8', 'Se dois ou mais indivíduos falecerem na mesma ocasião', 'simultaneamente mortos.', 'CC, art. 8º')],
  peg='Acrescentar requisito que a lei não traz.',
  kw=['mesma ocasião', 'comoriência'])

# ======================= MLE-5.3 · Exumação =======================
P = 'DBA26-MLE-5.3'
I(P, 1, 'Exumação para exame cadavérico',
  'Em caso de exumação para exame cadavérico, a autoridade providenciará para que, em dia e hora previamente marcados, se realize a diligência, da qual se lavrará auto circunstanciado.', 'C',
  '**Exumação** é o desenterramento (inumação é o sepultamento). O CPP exige **dia e hora marcados** e **auto circunstanciado**.',
  lei=[(CPP + '163', 'Em caso de exumação para exame cadavérico', 'auto circunstanciado.', 'CPP, art. 163')],
  kw=['exumação', 'auto circunstanciado'])
I(P, 1, 'Administrador do cemitério',
  'O administrador do cemitério pode recusar-se a indicar o lugar da sepultura, cabendo à autoridade apenas proceder a pesquisas.', 'E',
  'O administrador **indicará** a sepultura **sob pena de desobediência**; só na recusa ou falta de quem indique a autoridade faz as pesquisas.',
  lei=[(CPP + '163', 'O administrador de cemitério público ou particular', 'sob pena de desobediência.', 'CPP, art. 163, par. ún.')],
  peg='Transformar dever em faculdade.',
  kw=['desobediência', 'sepultura'])
I(P, 1, 'Identidade do exumado',
  'Havendo dúvida sobre a identidade do cadáver exumado, o reconhecimento pode ser feito pelo Instituto de Identificação ou pela inquirição de testemunhas, lavrando-se auto de reconhecimento e de identidade.', 'C',
  'Art. 166: **auto de reconhecimento e de identidade**, com a descrição do cadáver.',
  lei=[(CPP + '166', 'Havendo dúvida sobre a identidade do cadáver exumado', 'com todos os sinais e indicações.', 'CPP, art. 166')],
  kw=['auto de reconhecimento', 'identidade'])
I(P, 1, 'Prazo para exumar',
  'A exumação para exame cadavérico só pode ocorrer depois de seis meses do sepultamento.', 'E',
  'O CPP **não fixa prazo mínimo**: a exumação se faz quando a investigação precisar, em dia e hora marcados.',
  lei=[(CPP + '163', 'Em caso de exumação para exame cadavérico', 'auto circunstanciado.', 'CPP, art. 163')],
  peg='Inventar prazo que a lei não traz.',
  kw=['exumação', 'sem prazo mínimo'])
I(P, 1, 'Objetos do exumado',
  'Em qualquer caso, serão arrecadados e autenticados todos os objetos encontrados que possam ser úteis para a identificação do cadáver.', 'C',
  'Roupas, próteses, joias e documentos ajudam a **identificar**: a lei manda arrecadar e autenticar.',
  lei=[(CPP + '166', 'Em qualquer caso, serão arrecadados', 'identificação do cadáver.', 'CPP, art. 166, par. ún.')],
  kw=['arrecadados', 'objetos'])
I(P, 1, 'Consentimento da família',
  'A exumação determinada em investigação criminal depende do consentimento da família do morto.', 'E',
  'A exumação para fins criminais é **determinada pela autoridade**; não depende de concordância da família.',
  lei=[(CPP + '163', 'Em caso de exumação para exame cadavérico', 'auto circunstanciado.', 'CPP, art. 163')],
  peg='Condicionar o ato estatal à vontade de particulares.',
  kw=['autoridade', 'exumação'])

# --- MLE-5.3 · Rodada 2
I(P, 2, 'Cadáver fora de cemitério',
  'Se o cadáver estiver em lugar não destinado a inumações, a autoridade procederá às pesquisas necessárias, o que tudo constará do auto.', 'C',
  'Mesmo fora do cemitério (cova clandestina), o procedimento é documentado no **auto**.',
  lei=[(CPP + '163', 'No caso de recusa ou de falta de quem indique a sepultura', 'o que tudo constará do auto.', 'CPP, art. 163, par. ún.')],
  kw=['lugar não destinado a inumações', 'pesquisas'])
I(P, 2, 'Corificação',
  'A corificação é observada sobretudo em cadáveres sepultados em caixões de madeira, em solo úmido.', 'E',
  'A **corificação** (pele com aspecto de couro) é típica de corpos em **urnas metálicas hermeticamente fechadas**; o solo úmido e argiloso favorece a saponificação.',
  peg='Trocar a condição que produz o fenômeno.',
  kw=['corificação', 'urnas metálicas'])
I(P, 2, 'Utilidade da exumação',
  'Mesmo tardia, a exumação pode revelar fraturas e permitir exames toxicológicos, pois alguns venenos, como os metais, persistem em ossos, cabelos e unhas.', 'C',
  'Ossos guardam **fraturas** e projéteis; **metais** como arsênio e chumbo resistem à putrefação.',
  kw=['exumação', 'toxicológicos'])
I(P, 2, 'Embalsamamento × formolização',
  'O embalsamamento visa à conservação temporária do cadáver, enquanto a formolização busca a conservação permanente.', 'E',
  'É o inverso: **embalsamamento** — conservação **permanente**; **formolização** — **temporária** (para velório ou traslado).',
  peg='Inverter os dois métodos.',
  kw=['embalsamamento', 'formolização'])
I(P, 2, 'Finalidades',
  'A exumação pode ter finalidade judicial, como esclarecer a causa da morte ou a identidade, ou administrativa, como o traslado dos restos.', 'C',
  'A exumação **judicial** (ou criminal) e a **administrativa** (traslado, ossário) diferem pelo objetivo e por quem a determina.',
  kw=['finalidade judicial', 'administrativa'])

# ======================= MLE-5.4 · Causa jurídica da morte =======================
P = 'DBA26-MLE-5.4'
I(P, 1, 'Causa jurídica',
  'Quanto à causa jurídica, a morte é natural ou violenta, e esta pode decorrer de homicídio, suicídio ou acidente.', 'C',
  'A **causa jurídica** responde "por que, perante o Direito": natural ou **violenta** (homicida, suicida, acidental).',
  kw=['causa jurídica', 'morte violenta'])
I(P, 1, 'Morte violenta e homicídio',
  'Morte violenta é expressão sinônima de homicídio.', 'E',
  'Morte **violenta** é a de **causa externa**: abrange homicídio, **suicídio** e **acidente**.',
  peg='Reduzir o gênero a uma espécie.',
  kw=['morte violenta', 'suicídio'])
I(P, 1, 'Causa médica × jurídica',
  'A causa médica da morte, como a hemorragia aguda, não se confunde com a causa jurídica, como o homicídio por arma branca.', 'C',
  'A **causa médica** é a doença ou lesão (e o mecanismo fisiológico); a **causa jurídica** é a circunstância perante o Direito.',
  kw=['causa médica', 'causa jurídica'])
I(P, 1, 'Limites do perito',
  'Cabe ao perito, no laudo, afirmar a autoria e o dolo do agente, por serem conclusões técnicas da necropsia.', 'E',
  'O perito descreve achados e indica se são **compatíveis** com homicídio, suicídio ou acidente; **autoria e dolo** são juízos da investigação e do juiz.',
  peg='Entregar ao perito juízo que é jurídico.',
  kw=['autoria', 'dolo'])
I(P, 1, 'Exame externo na morte violenta',
  'Nos casos de morte violenta, bastará o simples exame externo do cadáver quando não houver infração penal a apurar, ou quando as lesões externas permitirem precisar a causa da morte e não houver necessidade de exame interno.', 'C',
  'É o art. 162, parágrafo único: a **necropsia completa** pode ser dispensada nessas duas hipóteses.',
  lei=[(CPP + '162', 'Nos casos de morte violenta, bastará o simples exame externo', 'verificação de alguma circunstância relevante.', 'CPP, art. 162, par. ún.')],
  kw=['exame externo', 'morte violenta'])
I(P, 1, 'Lesões de hesitação',
  'Lesões de hesitação superficiais e paralelas, em regiões acessíveis à própria mão, são achados que sugerem homicídio.', 'E',
  '**Lesões de hesitação** em regiões acessíveis sugerem **suicídio** (tentativas antes do golpe final). Sugerem, não provam: a cena e o conjunto decidem.',
  peg='Trocar suicídio por homicídio.',
  kw=['lesões de hesitação', 'suicídio'])

# --- MLE-5.4 · Rodada 2
I(P, 2, 'Causa básica',
  'Na declaração de óbito, a causa básica é a doença ou lesão que iniciou a cadeia de acontecimentos que levou diretamente à morte.', 'C',
  'A **causa básica** (conceito da OMS) é a que interessa à estatística e, na morte violenta, à investigação: a lesão que iniciou a cadeia.',
  kw=['causa básica', 'declaração de óbito'])
I(P, 2, 'Complicação tardia',
  'Se a vítima de acidente morre semanas depois por pneumonia contraída na internação, a causa jurídica da morte passa a ser natural.', 'E',
  'Mantido o **nexo causal** com o trauma, a morte continua **violenta** (acidental) e o caso é do IML.',
  peg='Romper o nexo pela complicação clínica.',
  kw=['nexo causal', 'violenta'])
I(P, 2, 'Elementos de suicídio por arma branca',
  'Feridas em região acessível, lesões de hesitação e vestes afastadas antes do golpe são elementos que, em conjunto, sugerem suicídio por arma branca.', 'C',
  'Nenhum elemento isolado decide; o **conjunto** (local acessível, hesitação, ausência de lesões de defesa, vestes afastadas) é que orienta.',
  kw=['suicídio', 'lesões de hesitação'])
I(P, 2, 'Declaração de óbito por PAF no hospital',
  'Quando a vítima de disparo de arma de fogo morre no hospital, a declaração de óbito é emitida pelo Serviço de Verificação de Óbito.', 'E',
  'Morte por **arma de fogo** é **violenta**: necropsia e declaração de óbito pelo **IML**.',
  peg='Encaminhar ao SVO o que é do IML.',
  kw=['IML', 'declaração de óbito'])
I(P, 2, 'Causa indeterminada',
  'É vedado ao perito concluir pela causa jurídica indeterminada, devendo sempre afirmar se a morte foi homicida, suicida ou acidental.', 'E',
  'Quando os achados não permitem distinguir, o perito pode e deve registrar a causa jurídica como **indeterminada**; afirmar sem base é que seria erro.',
  peg='Impor certeza onde a técnica admite dúvida.',
  kw=['indeterminada', 'causa jurídica'])

# ======================= MLE-5.5 · Morte súbita e morte suspeita =======================
P = 'DBA26-MLE-5.5'
I(P, 1, 'Morte súbita',
  'Morte súbita é a que ocorre de forma inesperada em pessoa aparentemente saudável, sendo em regra de causa natural, com predomínio das causas cardiovasculares.', 'C',
  'A **morte súbita** é definida pelo **inesperado**; a maioria é natural (sobretudo cardíaca).',
  kw=['morte súbita', 'inesperada'])
I(P, 1, 'Morte súbita e causa violenta',
  'Toda morte súbita é presumida violenta e deve ser encaminhada ao instituto médico-legal.', 'E',
  'A morte súbita é, **em regra, natural**; vai ao **SVO** se não houver suspeita. Só a morte **suspeita** ou violenta vai ao IML.',
  peg='Confundir súbita com suspeita.',
  kw=['morte súbita', 'natural'])
I(P, 1, 'Morte suspeita',
  'Morte suspeita é aquela em que há dúvida se a causa foi natural ou violenta, e deve ser esclarecida por necropsia médico-legal.', 'C',
  'A **morte suspeita** (ex.: corpo achado sem testemunhas, circunstâncias estranhas) exige investigação e **necropsia** no IML.',
  kw=['morte suspeita', 'necropsia'])
I(P, 1, 'Comunicação à autoridade',
  'A morte suspeita dispensa comunicação à autoridade policial quando o médico que constatar o óbito não identificar lesões externas.', 'E',
  'Morte **suspeita** deve ser comunicada; a autoridade policial vai ao local, preserva-o e requisita o exame (CPP, art. 6º). A ausência de lesão externa não afasta envenenamento, asfixia ou trauma interno.',
  lei=[(CPP + '6', 'VII - determinar, se for caso', 'quaisquer outras perícias;', 'CPP, art. 6º, VII')],
  peg='Usar a falta de lesão externa como dispensa.',
  kw=['morte suspeita', 'autoridade policial'])
I(P, 1, 'Morte agônica',
  'Morte agônica é a que sobrevém lentamente, após período de agonia prolongada, em contraposição à morte rápida ou instantânea.', 'C',
  'A **morte agônica** deixa sinais de sofrimento prolongado (ex.: coágulos cardíacos organizados); a rápida não.',
  kw=['morte agônica', 'agonia'])
I(P, 1, 'Súbita × suspeita',
  'Morte súbita e morte suspeita são expressões sinônimas na Medicina Legal.', 'E',
  'São conceitos **diferentes**: **súbita** fala do tempo (inesperada); **suspeita** fala da dúvida sobre a causa (natural ou violenta).',
  peg='Fundir dois conceitos vizinhos.',
  kw=['morte súbita', 'morte suspeita'])

# --- MLE-5.5 · Rodada 2
I(P, 2, 'Morte súbita do lactente',
  'A morte súbita do lactente é diagnóstico de exclusão, que só se firma após necropsia completa, exame da cena e revisão da história clínica.', 'C',
  'Antes de rotular, é preciso afastar **sufocação**, maus-tratos e doenças — daí a necropsia e a investigação da cena.',
  kw=['morte súbita do lactente', 'diagnóstico de exclusão'])
I(P, 2, 'Médico assistente na morte suspeita',
  'Em morte suspeita, o médico assistente que conhecia o paciente pode emitir a declaração de óbito e dispensar a necropsia.', 'E',
  'Havendo **suspeita** de causa externa, a declaração de óbito cabe ao **IML**, após necropsia.',
  peg='Dar ao vínculo clínico força para afastar a perícia.',
  kw=['morte suspeita', 'IML'])
I(P, 2, 'SVO na morte natural',
  'Na morte natural sem assistência médica, em localidade que disponha de Serviço de Verificação de Óbito, a declaração de óbito é emitida pelo SVO.', 'C',
  'Morte **natural** sem diagnóstico → **SVO**; morte violenta ou suspeita → IML.',
  kw=['SVO', 'morte natural'])
I(P, 2, 'Necropsia na morte suspeita',
  'Na morte suspeita, a necropsia pode ser dispensada sempre que o corpo não apresentar lesões externas.', 'E',
  'A dispensa do art. 162, parágrafo único, é para **morte violenta** com **lesões externas** que **precisem a causa**. Sem lesão externa, o exame **interno** é que esclarece.',
  lei=[(CPP + '162', 'Nos casos de morte violenta, bastará o simples exame externo', 'verificação de alguma circunstância relevante.', 'CPP, art. 162, par. ún.')],
  peg='Inverter a lógica da dispensa.',
  kw=['necropsia', 'exame interno'])
I(P, 2, 'Envenenamento que simula morte natural',
  'Na investigação de morte súbita ou suspeita, a pesquisa toxicológica é relevante porque certos envenenamentos podem simular morte natural.', 'C',
  'A **toxicologia** afasta envenenamento que imita infarto ou mal súbito; deve ser colhida na necropsia, com cadeia de custódia.',
  kw=['toxicológica', 'envenenamento'])
