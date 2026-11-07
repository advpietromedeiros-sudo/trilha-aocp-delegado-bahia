# Pente Fino de Medicina Legal — pontos MLE-6, MLE-7, MLE-7.1, MLE-8 e MLE-9 (07/11/2026).
from base import I
from mle_juris import J

CPP = 'CPP:'
CP = 'CP:'

# ======================= MLE-6 · Local de crime; toxicomanias e embriaguez; energias físicas e químicas =======================
P = 'DBA26-MLE-6'
I(P, 1, 'Preservação do local',
  'Logo que tiver conhecimento da infração penal, a autoridade policial deverá dirigir-se ao local, providenciando para que não se alterem o estado e a conservação das coisas até a chegada dos peritos criminais.', 'C',
  'É o primeiro dever do art. 6º: **preservar o local** até a chegada dos peritos.',
  lei=[(CPP + '6', 'I - dirigir-se ao local', 'até a chegada dos peritos criminais;', 'CPP, art. 6º, I')],
  kw=['preservação do local', 'peritos criminais'])
I(P, 1, 'Apreensão de objetos',
  'A autoridade policial deve apreender os objetos que tiverem relação com o fato antes de os peritos criminais os examinarem, para evitar seu extravio.', 'E',
  'A apreensão se faz **após liberados pelos peritos** (art. 6º, II): retirar antes altera o local e compromete a prova.',
  lei=[(CPP + '6', 'II - apreender os objetos', 'após liberados pelos peritos criminais;', 'CPP, art. 6º, II')],
  peg='Trocar "após liberados" por "antes".',
  kw=['apreender os objetos', 'após liberados'])
I(P, 1, 'Cáusticos',
  'Entre os cáusticos, os coagulantes, como muitos ácidos, tendem a produzir escaras secas e endurecidas, e os liquefacientes, como os álcalis, escaras úmidas e moles.', 'C',
  'É a classificação clássica da **ação química** local: **coagulantes** (escara seca) × **liquefacientes** (escara úmida). A cor ou a forma não identificam, sozinhas, o produto.',
  kw=['cáusticos', 'escaras'])
I(P, 1, 'Embriaguez voluntária ou culposa',
  'A embriaguez voluntária ou culposa, pelo álcool ou substância de efeitos análogos, exclui a imputabilidade penal quando completa.', 'E',
  'O art. 28, II, é claro: a embriaguez **voluntária ou culposa não exclui** a imputabilidade, ainda que completa (teoria da *actio libera in causa*).',
  lei=[(CP + '28', 'Não excluem a imputabilidade penal', 'pelo álcool ou substância de efeitos análogos.', 'CP, art. 28, II')],
  peg='Somar "completa" para fazer parecer a hipótese do § 1º.',
  kw=['embriaguez voluntária', 'imputabilidade'])
I(P, 1, 'Dependência de drogas',
  'É isento de pena o agente que, em razão da dependência de droga, era, ao tempo da ação ou da omissão, qualquer que tenha sido a infração penal, inteiramente incapaz de entender o caráter ilícito do fato ou de determinar-se de acordo com esse entendimento.', 'C',
  'Na **toxicomania**, a **dependência** pode gerar inimputabilidade (Lei 11.343/2006, art. 45), apurada por perícia — e vale para qualquer infração.',
  lei=[('L11343:45', 'É isento de pena o agente que, em razão da dependência', 'de determinar-se de acordo com esse entendimento.', 'Lei 11.343/2006, art. 45')],
  kw=['dependência', 'isento de pena'])
I(P, 1, 'Fases da embriaguez',
  'Das fases clássicas da embriaguez — excitação, confusão e sono —, a de maior interesse médico-legal, por concentrar agressividade e crimes, é a do sono.', 'E',
  'A fase de maior interesse médico-legal é a da **confusão** (agressividade, incoordenação, crimes). A do **sono** (coma) é de inconsciência; a da **excitação** é de euforia e desinibição.',
  peg='Trocar confusão por sono.',
  kw=['fase de confusão', 'embriaguez'])
I(P, 1, 'Graus de queimadura',
  'Na classificação clássica das queimaduras, a flictena (bolha) caracteriza o segundo grau.', 'C',
  '**1º grau**: eritema; **2º**: **flictena**; **3º**: escara (necrose); **4º**: carbonização.',
  kw=['flictena', 'segundo grau'])
I(P, 1, 'Eletroplessão × fulminação',
  'Eletroplessão é a denominação da morte causada pela eletricidade natural, isto é, pelo raio.', 'E',
  '**Eletroplessão** é a morte por eletricidade **industrial** (artificial); a causada pelo **raio** é a **fulminação** (as lesões não mortais, fulguração).',
  peg='Trocar artificial por natural.',
  kw=['eletroplessão', 'fulminação'])
I(P, 1, 'Sinal de Lichtenberg',
  'A figura de Lichtenberg, desenho arborescente e transitório na pele, é característica das lesões por descarga elétrica atmosférica.', 'C',
  'A **figura de Lichtenberg** sugere **raio**; some em horas e pode faltar.',
  kw=['Lichtenberg', 'raio'])
I(P, 1, 'Baropatias',
  'A doença descompressiva dos mergulhadores decorre da descida rápida, quando a pressão ambiente aumenta bruscamente.', 'E',
  'A **doença descompressiva** surge na **subida rápida** (descompressão): o nitrogênio dissolvido forma bolhas no sangue e tecidos. A baixa pressão das altitudes causa o mal das montanhas (hipobarismo).',
  peg='Trocar subida por descida.',
  kw=['doença descompressiva', 'baropatias'])

# --- MLE-6 · Rodada 2
I(P, 2, 'Embriaguez fortuita incompleta',
  'A pena pode ser reduzida de um a dois terços se o agente, por embriaguez proveniente de caso fortuito ou força maior, não possuía, ao tempo da conduta, a plena capacidade de entender o caráter ilícito do fato ou de determinar-se de acordo com esse entendimento.', 'C',
  'Embriaguez **acidental**: completa isenta (§ 1º); **incompleta reduz** de 1/3 a 2/3 (§ 2º).',
  lei=[(CP + '28', 'É isento de pena o agente que, por embriaguez completa', 'de determinar-se de acordo com esse entendimento.', 'CP, art. 28, § 1º'),
       (CP + '28', 'A pena pode ser reduzida de um a dois terços, se o agente, por embriaguez', 'de determinar-se de acordo com esse entendimento.', 'CP, art. 28, § 2º')],
  kw=['caso fortuito', 'embriaguez incompleta'])
I(P, 2, 'Embriaguez preordenada',
  'A embriaguez preordenada, em que o agente se embriaga para cometer o crime, é circunstância atenuante.', 'E',
  'A **embriaguez preordenada** é **agravante** genérica (art. 61, II, l).',
  lei=[(CP + '61', 'São circunstâncias que sempre agravam a pena', 'quando não constituem ou qualificam o crime:', 'CP, art. 61, caput'),
       (CP + '61', 'l) em estado de embriaguez preordenada.', None, 'CP, art. 61, II, l')],
  peg='Trocar agravante por atenuante.',
  kw=['embriaguez preordenada', 'agravante'])
I(P, 2, 'Sinal de Montalti',
  'Fuligem nas vias aéreas abaixo das cordas vocais, associada a carboxiemoglobina elevada no sangue, indica que a vítima respirava durante o incêndio.', 'C',
  'É o **sinal de Montalti** (fuligem na árvore respiratória) somado à **carboxiemoglobina**: reação vital no fogo.',
  kw=['Montalti', 'carboxiemoglobina'])
I(P, 2, 'Posição de pugilista',
  'A atitude de pugilista no carbonizado prova que a vítima estava viva quando exposta ao fogo.', 'E',
  'A **posição de pugilista** resulta da retração muscular pelo calor e ocorre **também no cadáver** queimado: **não prova** reação vital.',
  peg='Transformar achado térmico em sinal de vida.',
  kw=['pugilista', 'reação vital'])
I(P, 2, 'Marca elétrica de Jellinek',
  'A marca elétrica de Jellinek, no ponto de entrada da corrente industrial, é em regra lesão endurecida, de bordas elevadas, pouco dolorosa e de cor branco-amarelada.', 'C',
  'A **marca elétrica** marca o contato com a corrente artificial; pode ser discreta ou faltar, por isso o local e os equipamentos importam.',
  kw=['Jellinek', 'marca elétrica'])
I(P, 2, 'Classificação dos psicotrópicos',
  'Na classificação de Delay e Deniker, os psicolépticos são os estimulantes do sistema nervoso central, como a cocaína e as anfetaminas.', 'E',
  '**Psicolépticos** são **depressores** (álcool, barbitúricos, benzodiazepínicos, opiáceos); estimulantes são **psicoanalépticos**; perturbadores (alucinógenos) são **psicodislépticos**.',
  peg='Trocar depressores por estimulantes.',
  kw=['psicolépticos', 'psicoanalépticos'])
I(P, 2, 'Alcoolemia no trânsito',
  'O crime de embriaguez ao volante pode ser constatado por concentração igual ou superior a 6 decigramas de álcool por litro de sangue, ou 0,3 miligrama por litro de ar alveolar, ou por sinais de alteração da capacidade psicomotora.', 'C',
  'O art. 306 admite a prova **numérica** (alcoolemia ou etilômetro) ou por **sinais**, além de exame clínico, vídeo e testemunhas (§ 2º).',
  lei=[('L9503:306', 'As condutas previstas no caput serão constatadas por:', 'alteração da capacidade psicomotora.', 'CTB, art. 306, § 1º')],
  kw=['6 decigramas', 'capacidade psicomotora'])
I(P, 2, 'Violação do local isolado',
  'A entrada em local de crime isolado e a remoção de vestígios antes da liberação pelo perito responsável configuram mera infração administrativa.', 'E',
  'O CPP tipifica a conduta como **fraude processual** (art. 158-C, § 2º).',
  lei=[(CPP + '158-C', 'É proibida a entrada em locais isolados', 'tipificada como fraude processual a sua realização.', 'CPP, art. 158-C, § 2º')],
  peg='Rebaixar crime a infração administrativa.',
  kw=['fraude processual', 'local isolado'])

# ======================= MLE-7 · Crimes contra a dignidade sexual: aspectos médico-legais =======================
P = 'DBA26-MLE-7'
I(P, 1, 'Conjunção carnal e ato libidinoso',
  'Desde 2009, o estupro abrange tanto a conjunção carnal quanto outro ato libidinoso, e, para a perícia, conjunção carnal é a cópula vaginal com o pênis.', 'C',
  'O art. 213 fundiu estupro e atentado violento ao pudor; a perícia distingue **conjunção carnal** (cópula pênis-vagina) de outros **atos libidinosos**.',
  lei=[(CP + '213', 'Constranger alguém, mediante violência ou grave ameaça', 'outro ato libidinoso:', 'CP, art. 213')],
  kw=['conjunção carnal', 'ato libidinoso'])
I(P, 1, 'Ausência de lesões',
  'A ausência de lesões físicas e de ruptura himenal no exame afasta a ocorrência de estupro.', 'E',
  'O exame **negativo não exclui** violência sexual: hímen complacente, ato libidinoso sem contato genital, grave ameaça sem luta, intervalo longo até o exame.',
  peg='Transformar achado negativo em prova negativa.',
  kw=['ausência de lesões', 'hímen complacente'])
I(P, 1, 'Hímen complacente',
  'Hímen complacente é aquele que, por sua elasticidade, permite a conjunção carnal sem se romper.', 'C',
  'O **hímen complacente** explica por que a integridade himenal não prova ausência de relação.',
  kw=['hímen complacente', 'elasticidade'])
I(P, 1, 'Entalhe × rotura',
  'Os entalhes himenais são rupturas traumáticas que se estendem até a inserção do hímen na parede vaginal.', 'E',
  'Os **entalhes** são reentrâncias **congênitas**, que **não chegam** à borda de inserção e têm bordas regulares e simétricas. A **rotura** traumática vai até a inserção.',
  peg='Confundir variação anatômica com lesão.',
  kw=['entalhes', 'rotura himenal'])
I(P, 1, 'Espermatozoides na vagina',
  'A presença de espermatozoides na cavidade vaginal comprova a conjunção carnal recente, mas não demonstra, por si só, a violência nem a falta de consentimento.', 'C',
  'É **sinal de certeza** de conjunção carnal; **violência** e **consentimento** se provam pelo conjunto (lesões, relato, contexto).',
  kw=['espermatozoides', 'sinal de certeza'])
I(P, 1, 'Confissão no crime sexual',
  'No estupro que deixa vestígios, a confissão do acusado pode suprir o exame de corpo de delito.', 'E',
  'A regra do art. 158 vale também aqui: havendo vestígios, o exame é **indispensável** e a **confissão não o supre**. Desaparecidos os vestígios, a prova testemunhal pode supri-lo (art. 167).',
  lei=[(CPP + '158', 'Quando a infração deixar vestígios', 'não podendo supri-lo a confissão do acusado.', 'CPP, art. 158')],
  peg='Esquecer a regra geral do CPP no capítulo dos crimes sexuais.',
  kw=['exame de corpo de delito', 'confissão'])
I(P, 1, 'Consentimento do vulnerável',
  'No estupro de vulnerável, são irrelevantes o eventual consentimento da vítima menor de 14 anos, sua experiência sexual anterior e a existência de relacionamento amoroso com o agente.', 'C',
  'É a **Súmula 593/STJ**, hoje também no § 5º do art. 217-A.',
  lei=[(CP + '217-A', 'As penas previstas no caput e nos §§ 1º, 3º e 4º deste artigo', 'gravidez resultante da prática do crime.', 'CP, art. 217-A, § 5º')],
  juris=[J['S593']],
  kw=['estupro de vulnerável', 'consentimento'])
I(P, 1, 'PSA e azoospermia',
  'Se o agressor é vasectomizado ou azoospérmico, não há como demonstrar laboratorialmente a presença de sêmen, pois o antígeno prostático depende dos espermatozoides.', 'E',
  'O **antígeno prostático específico** (PSA, p30) e a **fosfatase ácida** vêm do líquido prostático e aparecem **mesmo sem espermatozoides**.',
  peg='Ligar o marcador prostático ao espermatozoide.',
  kw=['antígeno prostático', 'azoospérmico'])

# --- MLE-7 · Rodada 2
I(P, 2, 'Marcadores do sêmen',
  'A fosfatase ácida prostática e o antígeno prostático específico são marcadores do líquido seminal úteis inclusive quando não se encontram espermatozoides.', 'C',
  'São **testes de orientação** ou confirmação, conforme o método; o DNA identifica a fonte.',
  kw=['fosfatase ácida', 'antígeno prostático'])
I(P, 2, 'Presunção de vulnerabilidade',
  'Pela redação atual do Código Penal, a presunção de vulnerabilidade da vítima menor de 14 anos é relativa, podendo ser afastada pela prova de sua maturidade sexual.', 'E',
  'O § 4º-A do art. 217-A (Lei 15.353/2026) diz que a presunção é **absoluta** e **inadmissível sua relativização**.',
  lei=[(CP + '217-A', 'É absoluta a presunção de vulnerabilidade da vítima', 'inadmissível sua relativização.', 'CP, art. 217-A, § 4º-A')],
  juris=[J['S593']],
  peg='Trocar absoluta por relativa.',
  kw=['presunção absoluta', 'vulnerabilidade'])
I(P, 2, 'Aborto na gravidez por estupro',
  'Para o aborto de gravidez resultante de estupro, o Código Penal exige que seja praticado por médico e precedido do consentimento da gestante ou, se incapaz, de seu representante legal.', 'C',
  'O art. 128, II, pede **médico** e **consentimento**; o texto legal não exige autorização judicial nem laudo prévio.',
  lei=[(CP + '128', 'II - se a gravidez resulta de estupro', 'de seu representante legal.', 'CP, art. 128, II')],
  kw=['aborto', 'consentimento da gestante'])
I(P, 2, 'Exame himenal e atividade sexual',
  'O exame do hímen permite afirmar com segurança se a examinada já teve relações sexuais anteriores.', 'E',
  'Variações anatômicas, elasticidade e cicatrização tornam o hímen **inapto** para afirmar atividade sexual prévia ("virgindade"); o próprio conceito é rejeitado como critério técnico.',
  peg='Dar valor absoluto a achado de baixa especificidade.',
  kw=['hímen', 'atividade sexual'])
I(P, 2, 'DNA nos vestígios',
  'O perfil de DNA obtido de sêmen, saliva ou pelos identifica a fonte do material biológico, mas não demonstra, sozinho, a ausência de consentimento.', 'C',
  'O **DNA** responde "de quem é"; não responde "como" nem "se houve consentimento".',
  kw=['DNA', 'fonte do material'])
I(P, 2, 'Vítima que não pode resistir',
  'Quem pratica conjunção carnal com pessoa que, por embriaguez completa, não pode oferecer resistência comete apenas estupro simples, pois a vítima não é menor de 14 anos.', 'E',
  'O § 1º do art. 217-A equipara ao vulnerável quem, **por qualquer outra causa, não pode oferecer resistência** — a embriaguez completa entra aí: é **estupro de vulnerável**.',
  lei=[(CP + '217-A', 'Incorre na mesma pena quem pratica as ações descritas no caput', 'não pode oferecer resistência.', 'CP, art. 217-A, § 1º')],
  peg='Reduzir a vulnerabilidade à idade.',
  kw=['não pode oferecer resistência', 'estupro de vulnerável'])

# ======================= MLE-7.1 · Violência sexual, tipos penais e coleta de vestígios =======================
P = 'DBA26-MLE-7.1'
I(P, 1, 'Importunação sexual',
  'Pratica importunação sexual quem realiza contra alguém, sem a sua anuência, ato libidinoso com o objetivo de satisfazer a própria lascívia ou a de terceiro.', 'C',
  'É o art. 215-A: **sem anuência**, sem violência ou grave ameaça (com elas, seria estupro).',
  lei=[(CP + '215-A', 'Praticar contra alguém e sem a sua anuência', 'a própria lascívia ou a de terceiro:', 'CP, art. 215-A')],
  kw=['importunação sexual', 'sem a sua anuência'])
I(P, 1, 'Assédio sexual',
  'O assédio sexual exige o emprego de violência ou grave ameaça para obter vantagem ou favorecimento sexual.', 'E',
  'O **assédio sexual** se caracteriza pelo **prevalecimento** de superioridade hierárquica ou ascendência ligada a emprego, cargo ou função — não por violência ou ameaça.',
  lei=[(CP + '216-A', 'Constranger alguém com o intuito de obter vantagem ou favorecimento sexual', 'exercício de emprego, cargo ou função.', 'CP, art. 216-A')],
  peg='Trocar o meio típico pelo do estupro.',
  kw=['assédio sexual', 'superior hierárquico'])
I(P, 1, 'Estupro de vulnerável',
  'Configura estupro de vulnerável ter conjunção carnal ou praticar outro ato libidinoso com menor de 14 anos.', 'C',
  'Art. 217-A, caput: basta a idade; não se exige violência.',
  lei=[(CP + '217-A', 'Ter conjunção carnal ou praticar outro ato libidinoso', 'menor de 14 (catorze) anos:', 'CP, art. 217-A')],
  kw=['estupro de vulnerável', 'menor de 14'])
I(P, 1, 'Estupro qualificado pela idade',
  'O estupro é qualificado quando a vítima é menor de 18 e maior de 16 anos.', 'E',
  'A qualificadora do § 1º do art. 213 alcança vítima **menor de 18 e maior de 14** anos.',
  lei=[(CP + '213', 'Se da conduta resulta lesão corporal de natureza grave', 'maior de 14 (catorze) anos:', 'CP, art. 213, § 1º')],
  peg='Trocar 14 por 16.',
  kw=['maior de 14', 'estupro qualificado'])
I(P, 1, 'Violência sexual na Lei Maria da Penha',
  'Para a Lei Maria da Penha, é forma de violência sexual a conduta que impeça a mulher de usar qualquer método contraceptivo.', 'C',
  'O art. 7º, III, é amplo: inclui **impedir contracepção** e forçar casamento, gravidez, aborto ou prostituição.',
  lei=[('L11340:7', 'III - a violência sexual', 'que a impeça de usar qualquer método contraceptivo', 'Lei 11.340/2006, art. 7º, III')],
  kw=['violência sexual', 'método contraceptivo'])
I(P, 1, 'Embalagem de vestígios biológicos',
  'Roupas com manchas de sangue ou sêmen devem ser acondicionadas úmidas em sacos plásticos fechados, para preservar o material biológico.', 'E',
  'Material biológico deve **secar** e ir em **envelope ou saco de papel**: o plástico retém umidade, favorece fungos e bactérias e degrada o DNA. A lei manda que o recipiente siga a natureza do material.',
  lei=[(CPP + '158-D', 'O recipiente para acondicionamento do vestígio', 'natureza do material.', 'CPP, art. 158-D')],
  peg='Trocar papel por plástico e seco por úmido.',
  kw=['acondicionamento', 'papel'])
I(P, 1, 'Coleta por perito oficial',
  'A coleta dos vestígios deverá ser realizada preferencialmente por perito oficial, que dará o encaminhamento necessário para a central de custódia.', 'C',
  'Art. 158-C: **preferencialmente** perito oficial — não exclusivamente.',
  lei=[(CPP + '158-C', 'A coleta dos vestígios deverá ser realizada preferencialmente', 'central de custódia', 'CPP, art. 158-C')],
  kw=['perito oficial', 'coleta'])
I(P, 1, 'Pena da importunação',
  'A importunação sexual é crime punido com detenção, de três meses a um ano.', 'E',
  'A pena é de **reclusão, de 1 a 5 anos**, se o ato não constitui crime mais grave.',
  lei=[(CP + '215-A', 'Pena - reclusão, de 1 (um) a 5 (cinco) anos', 'se o ato não constitui crime mais grave.', 'CP, art. 215-A, pena')],
  peg='Rebaixar a pena para a de contravenção revogada.',
  kw=['reclusão', 'importunação sexual'])

# --- MLE-7.1 · Rodada 2
I(P, 2, 'Acondicionamento individualizado',
  'No acondicionamento, cada vestígio coletado é embalado de forma individualizada, de acordo com suas características físicas, químicas e biológicas, com anotação da data, hora e nome de quem realizou a coleta e o acondicionamento.', 'C',
  'É o art. 158-B, V: **um vestígio, uma embalagem**, com registro de quem e quando.',
  lei=[(CPP + '158-B', 'V - acondicionamento', 'quem realizou a coleta e o acondicionamento;', 'CPP, art. 158-B, V')],
  kw=['acondicionamento', 'individualizada'])
I(P, 2, 'Escuta especializada × depoimento especial',
  'Escuta especializada é o procedimento de oitiva da criança ou do adolescente vítima de violência perante a autoridade policial ou judiciária.', 'E',
  'Essa é a definição de **depoimento especial** (art. 8º). A **escuta especializada** é a entrevista perante a **rede de proteção**, limitada ao necessário (art. 7º).',
  lei=[('L13431:7', 'Escuta especializada é o procedimento de entrevista', 'cumprimento de sua finalidade.', 'Lei 13.431/2017, art. 7º'),
       ('L13431:8', 'Depoimento especial é o procedimento de oitiva', 'autoridade policial ou judiciária.', 'Lei 13.431/2017, art. 8º')],
  peg='Trocar as definições dos dois institutos.',
  kw=['escuta especializada', 'depoimento especial'])
I(P, 2, 'Prioridade do exame na violência contra criança',
  'A violência contra criança ou adolescente está entre as hipóteses legais de prioridade no exame de corpo de delito.', 'C',
  'Art. 158, parágrafo único, II: a demora apaga vestígios e revitimiza.',
  lei=[(CPP + '158', 'Dar-se-á prioridade à realização do exame de corpo de delito', 'idoso ou pessoa com deficiência.', 'CPP, art. 158, par. ún.')],
  kw=['prioridade', 'criança'])
I(P, 2, 'Aumento no assédio sexual',
  'A pena do assédio sexual é aumentada em até um terço se a vítima é menor de 14 anos.', 'E',
  'O aumento do § 2º do art. 216-A vale para vítima **menor de 18** anos.',
  lei=[(CP + '216-A', 'A pena é aumentada em até um terço', 'menor de 18 (dezoito) anos.', 'CP, art. 216-A, § 2º')],
  peg='Trocar 18 por 14.',
  kw=['menor de 18', 'assédio sexual'])
I(P, 2, 'Secagem dos suabes',
  'Os suabes com material biológico devem secar ao ar, protegidos de contaminação, antes de serem embalados, para preservar o DNA.', 'C',
  'A **umidade** degrada o DNA; secar e embalar em papel é a regra técnica, com registro na cadeia de custódia.',
  kw=['suabes', 'DNA'])
I(P, 2, 'Subsidiariedade da importunação',
  'Aplica-se a pena da importunação sexual ainda que o ato praticado constitua crime mais grave, por ser tipo especial.', 'E',
  'A importunação é **expressamente subsidiária**: só se aplica **se o ato não constitui crime mais grave**.',
  lei=[(CP + '215-A', 'Pena - reclusão, de 1 (um) a 5 (cinco) anos', 'se o ato não constitui crime mais grave.', 'CP, art. 215-A, pena')],
  peg='Inverter a subsidiariedade.',
  kw=['subsidiária', 'crime mais grave'])

# ======================= MLE-8 · Asfixias =======================
P = 'DBA26-MLE-8'
I(P, 1, 'Enforcamento',
  'No enforcamento, a constrição do pescoço é feita por laço acionado pelo peso do próprio corpo, ainda que a suspensão seja incompleta.', 'C',
  'O que define o **enforcamento** é a força: o **peso do corpo**. A suspensão pode ser incompleta (pés ou joelhos tocando o chão).',
  kw=['enforcamento', 'peso do corpo'])
I(P, 1, 'Estrangulamento',
  'No estrangulamento, o laço é acionado pelo peso do corpo da vítima.', 'E',
  'No **estrangulamento**, quem aperta o laço é uma **força ativa diversa do peso** do corpo (em regra, as mãos do agressor).',
  peg='Trocar a força que aciona o laço.',
  kw=['estrangulamento', 'força ativa'])
I(P, 1, 'Esganadura',
  'Esganadura é a constrição do pescoço feita diretamente pelas mãos, sendo sua etiologia praticamente sempre homicida.', 'C',
  'Na **esganadura** não há laço: são as **mãos**. Autoesganadura é inviável, pois a perda de consciência afrouxa as mãos.',
  kw=['esganadura', 'homicida'])
I(P, 1, 'Sulco do enforcamento',
  'O sulco do enforcamento é tipicamente horizontal, contínuo e de profundidade uniforme.', 'E',
  'O sulco do **enforcamento** é **oblíquo ascendente**, **interrompido** na altura do nó e mais profundo do lado oposto a ele. Horizontal e contínuo é o do **estrangulamento**.',
  peg='Dar ao enforcamento o sulco do estrangulamento.',
  kw=['sulco', 'oblíquo ascendente'])
I(P, 1, 'Sufocação indireta',
  'A compressão do tórax que impede os movimentos respiratórios é forma de sufocação indireta e pode produzir a máscara equimótica da face e do pescoço.', 'C',
  '**Sufocação indireta** (compressão torácica: soterramento parcial, multidões); a **máscara equimótica** (de Morestin) resulta da congestão venosa intensa.',
  kw=['sufocação indireta', 'máscara equimótica'])
I(P, 1, 'Afogamento na classificação',
  'O afogamento é asfixia por constrição, por impedir a passagem do ar pelas vias aéreas.', 'E',
  'O **afogamento** é asfixia por **modificação do meio** (o ar é substituído por líquido), ao lado do confinamento, do soterramento e dos gases irrespiráveis.',
  peg='Trocar o grupo da classificação.',
  kw=['afogamento', 'modificação do meio'])
I(P, 1, 'Sinais gerais de asfixia',
  'Cianose, petéquias subpleurais e subepicárdicas e sangue escuro e fluido são sinais gerais descritos nas asfixias, embora inespecíficos.', 'C',
  'As petéquias são as **manchas de Tardieu**; nenhum desses sinais é obrigatório nem exclusivo de asfixia.',
  kw=['manchas de Tardieu', 'inespecíficos'])
I(P, 1, 'Asfixia no homicídio',
  'O emprego de asfixia não qualifica o homicídio, servindo apenas como circunstância judicial na fixação da pena-base.', 'E',
  'A **asfixia** é meio que **qualifica** o homicídio (art. 121, § 2º, III).',
  lei=[(CP + '121', 'III - com emprego de veneno, fogo, explosivo, asfixia', 'ou de que possa resultar perigo comum;', 'CP, art. 121, § 2º, III')],
  peg='Rebaixar qualificadora a circunstância judicial.',
  kw=['asfixia', 'qualificadora'])
I(P, 1, 'Cogumelo de espuma',
  'O cogumelo de espuma na boca e nas narinas é sinal externo descrito no afogamento, formado pela mistura de ar, água e muco nas vias aéreas durante a respiração.', 'C',
  'O **cogumelo de espuma** pressupõe movimentos respiratórios no meio líquido; é sinal sugestivo de afogamento em vida.',
  kw=['cogumelo de espuma', 'afogamento'])
I(P, 1, 'Confinamento',
  'Confinamento é a asfixia em que a vítima fica imersa em meio sólido, como terra ou areia.', 'E',
  'Imersão em sólido pulverulento é **soterramento**. **Confinamento** é a permanência em **espaço fechado** sem renovação do ar.',
  peg='Trocar soterramento por confinamento.',
  kw=['confinamento', 'soterramento'])

# --- MLE-8 · Rodada 2
I(P, 2, 'Sinal de Amussat',
  'O sinal de Amussat, descrito no enforcamento, é a ruptura transversal da túnica íntima da artéria carótida.', 'C',
  '**Amussat**: ruptura da **íntima** carotídea por estiramento; **Friedberg**: sufusão hemorrágica na adventícia. Nenhum é patognomônico.',
  kw=['Amussat', 'carótida'])
I(P, 2, 'Afogado branco × azul',
  'O afogado branco de Parrot apresenta abundante água nos pulmões e cogumelo de espuma, por ter aspirado intensamente o líquido.', 'E',
  'O **afogado branco** morre por **inibição** (síncope) logo ao contato com a água, **sem aspiração** importante. O que aspira (cianose, espuma, pulmões encharcados) é o **afogado azul**, o afogamento verdadeiro.',
  peg='Dar ao afogado branco os sinais do azul.',
  kw=['afogado branco', 'afogado azul'])
I(P, 2, 'Manchas de Paltauf',
  'As manchas de Paltauf, hemorragias subpleurais descritas no afogamento, não são obrigatórias, e sua ausência não exclui o diagnóstico.', 'C',
  'Diagnóstico de afogamento é de **conjunto** (cena, necropsia, exclusão de outras causas); **Paltauf** pode faltar.',
  kw=['manchas de Paltauf', 'afogamento'])
I(P, 2, 'Esganadura suicida',
  'A esganadura é forma frequente de suicídio, pois a própria vítima consegue manter a compressão até a morte.', 'E',
  'Ao perder a consciência, as mãos **afrouxam**: a esganadura é, na prática, **sempre homicida**.',
  peg='Inverter a etiologia.',
  kw=['esganadura', 'homicida'])
I(P, 2, 'Diatomáceas',
  'O encontro de diatomáceas na medula óssea ou em órgãos distantes sugere que houve circulação ativa durante a imersão, embora o método tenha limitações de contaminação e interpretação.', 'C',
  'As **diatomáceas** entram pela aspiração e chegam aos órgãos pela circulação: sugerem afogamento em vida, mas pedem cautela técnica.',
  kw=['diatomáceas', 'circulação ativa'])
I(P, 2, 'Mãos de lavadeira',
  'As mãos de lavadeira provam que a vítima entrou viva na água.', 'E',
  'As **mãos de lavadeira** são **maceração** por permanência na água; ocorrem também em **cadáver** jogado na água. Indicam tempo de imersão, não vida.',
  peg='Transformar sinal de permanência em sinal de vida.',
  kw=['mãos de lavadeira', 'maceração'])
I(P, 2, 'Profundidade do sulco',
  'No enforcamento típico, o sulco é mais profundo no lado oposto ao nó, onde a pressão do laço é maior.', 'C',
  'O peso do corpo concentra a pressão **do lado oposto ao nó**; junto ao nó o sulco se interrompe ou se atenua.',
  kw=['sulco', 'oposto ao nó'])
I(P, 2, 'Valor das manchas de Tardieu',
  'As manchas de Tardieu são patognomônicas de asfixia mecânica.', 'E',
  'As **petéquias** surgem em várias mortes com congestão (cardíacas, convulsões, reanimação). São **sugestivas**, **não patognomônicas**.',
  peg='Transformar sinal sugestivo em patognomônico.',
  kw=['Tardieu', 'patognomônicas'])

# ======================= MLE-9 · Aborto, infanticídio e abandono de recém-nascido =======================
P = 'DBA26-MLE-9'
I(P, 1, 'Perícia no aborto',
  'Na perícia do aborto, interessa diagnosticar a gravidez anterior, a interrupção da gestação com morte do produto da concepção, o meio empregado e se houve provocação.', 'C',
  'O laudo responde: havia **gravidez**? houve **aborto**? foi **provocado**? por qual **meio**? Viabilidade fetal não é requisito do crime.',
  kw=['aborto', 'meio empregado'])
I(P, 1, 'Aborto necessário',
  'O aborto necessário, praticado por médico quando não há outro meio de salvar a vida da gestante, depende do consentimento desta.', 'E',
  'O inciso I do art. 128 exige só a **ausência de outro meio** de salvar a gestante; o **consentimento** é exigido no inciso **II** (gravidez por estupro).',
  lei=[(CP + '128', 'I - se não há outro meio de salvar a vida da gestante;', None, 'CP, art. 128, I')],
  peg='Levar ao inciso I o requisito do inciso II.',
  kw=['aborto necessário', 'consentimento'])
I(P, 1, 'Aborto na gravidez por estupro',
  'Não se pune o aborto praticado por médico se a gravidez resulta de estupro e o aborto é precedido de consentimento da gestante ou, quando incapaz, de seu representante legal.', 'C',
  'Literalidade do art. 128, II (aborto humanitário ou sentimental).',
  lei=[(CP + '128', 'II - se a gravidez resulta de estupro', 'de seu representante legal.', 'CP, art. 128, II')],
  kw=['gravidez resulta de estupro', 'aborto'])
I(P, 1, 'Momento do infanticídio',
  'O infanticídio pode ser praticado pela mãe, sob a influência do estado puerperal, até trinta dias após o parto.', 'E',
  'O tipo fala em "**durante o parto ou logo após**", sem prazo em dias; o critério é a persistência do **estado puerperal**.',
  lei=[(CP + '123', 'Matar, sob a influência do estado puerperal', 'durante o parto ou logo após:', 'CP, art. 123')],
  peg='Inventar prazo fixo.',
  kw=['estado puerperal', 'logo após'])
I(P, 1, 'Prova de vida extrauterina',
  'As docimásias são provas destinadas a verificar se o recém-nascido respirou, isto é, se teve vida extrauterina.', 'C',
  'Sem vida (nascimento com vida ou ao menos feto nascente vivo), não há infanticídio; daí as **docimásias**.',
  kw=['docimásias', 'vida extrauterina'])
I(P, 1, 'Docimásia de Galeno',
  'Na docimásia hidrostática de Galeno, os pulmões que afundam na água indicam que houve respiração.', 'E',
  'É o inverso: pulmão que **respirou** tem ar e **flutua**; o que **afunda** sugere que **não respirou**.',
  peg='Inverter flutuar e afundar.',
  kw=['docimásia de Galeno', 'flutua'])
I(P, 1, 'Abandono de recém-nascido',
  'Expor ou abandonar recém-nascido para ocultar desonra própria é crime específico, punido com detenção, com formas qualificadas se resultar lesão grave ou morte.', 'C',
  'É o art. 134: o elemento subjetivo especial é **ocultar desonra própria**.',
  lei=[(CP + '134', 'Expor ou abandonar recém-nascido', 'para ocultar desonra própria:', 'CP, art. 134')],
  kw=['abandono de recém-nascido', 'desonra própria'])
I(P, 1, 'Infanticídio intraparto',
  'O feto nascente, morto durante o parto, não pode ser vítima de infanticídio, pois ainda não há vida extrauterina.', 'E',
  'O tipo do art. 123 inclui matar "**durante o parto**": o **feto nascente** pode ser vítima. A perícia busca sinais de vida durante o parto (ex.: bossa serossanguínea).',
  lei=[(CP + '123', 'Matar, sob a influência do estado puerperal', 'durante o parto ou logo após:', 'CP, art. 123')],
  peg='Excluir do tipo a hipótese expressa "durante o parto".',
  kw=['feto nascente', 'durante o parto'])

# --- MLE-9 · Rodada 2
I(P, 2, 'Putrefação e Galeno',
  'A putrefação pode falsear a docimásia de Galeno, pois os gases fazem flutuar pulmões que nunca respiraram.', 'C',
  'É o **falso positivo** clássico: por isso a docimásia isolada não basta e se soma à histologia.',
  kw=['putrefação', 'docimásia de Galeno'])
I(P, 2, 'Sinal de Spalding',
  'O sinal de Spalding, cavalgamento dos ossos do crânio fetal, indica gravidez com feto vivo.', 'E',
  'O **sinal de Spalding** indica **morte fetal** com maceração (os ossos do crânio se sobrepõem).',
  peg='Inverter vida e morte.',
  kw=['sinal de Spalding', 'morte fetal'])
I(P, 2, 'Outras docimásias',
  'Além da pulmonar, há docimásias extrapulmonares, como a auricular, que pesquisa ar no ouvido médio, e a gastrintestinal, que pesquisa ar no tubo digestivo.', 'C',
  'Docimásia **auricular** (ouvido médio) e **gastrintestinal** (ar no estômago e intestinos) complementam a pulmonar; nenhuma é prova isolada.',
  kw=['docimásia auricular', 'gastrintestinal'])
I(P, 2, 'Aborto em gestante menor de 14',
  'No aborto provocado com o consentimento de gestante menor de 14 anos, aplica-se a pena do aborto consentido.', 'E',
  'Se a gestante **não é maior de 14 anos**, o consentimento é inválido e se aplica a pena do **aborto sem consentimento** (art. 125), por força do parágrafo único do art. 126.',
  lei=[(CP + '126', 'Aplica-se a pena do artigo anterior', 'grave ameaça ou violência', 'CP, art. 126, par. ún.'),
       (CP + '125', 'Provocar aborto, sem o consentimento da gestante:', None, 'CP, art. 125')],
  peg='Validar consentimento que a lei invalida.',
  kw=['menor de 14', 'sem o consentimento'])
I(P, 2, 'Litopédio',
  'Litopédio é o feto morto retido que sofre calcificação.', 'C',
  'O **litopédio** é fenômeno conservador raro (calcificação), em regra em gestação extrauterina.',
  kw=['litopédio', 'calcificação'])
I(P, 2, 'Maceração fetal',
  'O feto morto retido no útero sofre maceração séptica, pela ação de bactérias.', 'E',
  'No útero íntegro a maceração é **asséptica**; a **séptica** ocorre em corpos submersos em meio contaminado.',
  peg='Trocar asséptica por séptica.',
  kw=['maceração asséptica', 'feto retido'])
