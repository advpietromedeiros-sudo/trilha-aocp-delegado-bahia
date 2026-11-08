# Pente Fino de Legislação Penal Extravagante — LPE-10 (sistema financeiro), LPE-11 (crimes eleitorais), LPE-12
# (crimes de trânsito), LPE-13 (execução penal) e LPE-14 (juizados especiais criminais) (08/11/2026).
from base import I
from lpe_juris import J

SF = 'L7492:'
CE = 'L4737:'
TE = 'L6091:'
LE = 'L9504:'
CT = 'L9503:'
EP = 'L7210:'
JE = 'L9099:'

# ======================= LPE-10 · Crimes contra o Sistema Financeiro Nacional =======================
P = 'DBA26-LPE-10'
I(P, 1, 'Pessoa natural equiparada',
  'Equipara-se a instituição financeira, para os fins da Lei 7.492/1986, a pessoa natural que exerça captação, intermediação ou aplicação de recursos de terceiros, ainda que de forma eventual.', 'C',
  'Art. 1º, par. ún., II.',
  lei=[(SF + '1', 'II - a pessoa natural que exerça quaisquer das atividades referidas neste artigo, ainda que de forma eventual.', None, 'Lei 7.492/1986, art. 1º, par. ún., II')],
  kw=['pessoa natural', 'ainda que de forma eventual'])
I(P, 1, 'Competência',
  'A ação penal nos crimes contra o Sistema Financeiro Nacional é promovida pelo Ministério Público estadual perante a Justiça Estadual, salvo se a vítima for banco público federal.', 'E',
  'Art. 26: a ação é promovida pelo **Ministério Público Federal**, perante a **Justiça Federal** (CF, art. 109, VI).',
  lei=[(SF + '26', 'A ação penal, nos crimes previstos nesta lei, será promovida pelo Ministério Público Federal, perante a Justiça Federal.', None, 'Lei 7.492/1986, art. 26')],
  peg='Levar o crime financeiro à Justiça Estadual.', kw=['Justiça Federal', 'Ministério Público Federal'])
I(P, 1, 'Gestão fraudulenta e temerária',
  'A gestão temerária de instituição financeira é punida mais gravemente que a gestão fraudulenta.', 'E',
  'Art. 4º: **fraudulenta**, reclusão de 3 a 12 anos; **temerária** (par. ún.), de 2 a 8 anos.',
  lei=[(SF + '4', 'Gerir fraudulentamente instituição financeira:', None, 'Lei 7.492/1986, art. 4º'), (SF + '4', 'Se a gestão é temerária:', None, 'Lei 7.492/1986, art. 4º, par. ún.')],
  peg='Inverter as penas.', kw=['gestão fraudulenta', 'gestão temerária'])
I(P, 1, 'Evasão de divisas',
  'Incorre nas penas da evasão de divisas quem mantém no exterior depósitos não declarados à repartição federal competente.', 'C',
  'Art. 22, par. ún. (reclusão de 2 a 6 anos e multa).',
  lei=[(SF + '22', 'ou nele mantiver depósitos não declarados à repartição federal competente', None, 'Lei 7.492/1986, art. 22, par. ún.')],
  kw=['evasão de divisas', 'depósitos não declarados'])
I(P, 1, 'Ativos virtuais',
  'Equipara-se a instituição financeira a pessoa jurídica que ofereça serviços de operações com ativos virtuais, inclusive intermediação, negociação ou custódia.', 'C',
  'Art. 1º, par. ún., I-A (Lei 14.478/2022 — marco dos criptoativos).',
  lei=[(SF + '1', 'I-A - a pessoa jurídica que ofereça serviços referentes a operações com ativos virtuais, inclusive intermediação, negociação ou custódia;', None, 'Lei 7.492/1986, art. 1º, par. ún., I-A')],
  kw=['ativos virtuais'])
# --- LPE-10 · Rodada 2
I(P, 2, 'Delação na Lei 7.492',
  'Nos crimes contra o Sistema Financeiro cometidos em quadrilha ou coautoria, o coautor ou partícipe que, por confissão espontânea, revelar à autoridade toda a trama delituosa terá a pena reduzida de um a dois terços.', 'C',
  'Art. 25, § 2º.',
  lei=[(SF + '25', 'revelar à autoridade policial ou judicial toda a trama delituosa terá a sua pena reduzida de um a dois terços', None, 'Lei 7.492/1986, art. 25, § 2º')],
  kw=['trama delituosa', 'um a dois terços'])
I(P, 2, 'Fraude em financiamento',
  'A obtenção, mediante fraude, de financiamento em instituição financeira tem a pena aumentada de metade se praticada em detrimento de instituição financeira oficial.', 'E',
  'Art. 19, par. ún.: aumento de **1/3**.',
  lei=[(SF + '19', 'A pena é aumentada de 1/3 (um terço) se o crime é cometido em detrimento de instituição financeira oficial', None, 'Lei 7.492/1986, art. 19, par. ún.')],
  peg='Trocar a fração.', kw=['1/3 (um terço)', 'instituição financeira oficial'])
I(P, 2, 'Instituição clandestina',
  'Fazer operar instituição financeira sem a devida autorização só é crime quando a atividade é exercida por pessoa jurídica regularmente constituída.', 'E',
  'Art. 16 c/c art. 1º, par. ún., II: a "instituição" pode ser a própria **pessoa natural** que capta recursos de terceiros; a operação **clandestina** é o núcleo do tipo.',
  lei=[(SF + '16', 'Fazer operar, sem a devida autorização', None, 'Lei 7.492/1986, art. 16')],
  peg='Exigir pessoa jurídica formal.', kw=['sem a devida autorização', 'pessoa natural'])

# ======================= LPE-11 · Crimes eleitorais =======================
P = 'DBA26-LPE-11'
I(P, 1, 'Pena mínima no Código Eleitoral',
  'Quando o Código Eleitoral não indica o grau mínimo da pena, entende-se que é de quinze dias para a detenção e de um ano para a reclusão.', 'C',
  'Art. 284 — por isso tipos como o art. 299 trazem só o máximo ("reclusão até quatro anos").',
  lei=[(CE + '284', 'entende-se que será ele de quinze dias para a pena de detenção e de um ano para a de reclusão', None, 'Código Eleitoral, art. 284')],
  kw=['grau mínimo', 'quinze dias'])
I(P, 1, 'Ação penal eleitoral',
  'A calúnia praticada na propaganda eleitoral, por ofender a honra do candidato, é crime de ação penal privada.', 'E',
  'Art. 355: as infrações penais do Código Eleitoral são de **ação pública** — inclusive os crimes contra a honra na propaganda (arts. 324 a 326).',
  lei=[(CE + '355', 'As infrações penais definidas neste Código são de ação pública.', None, 'Código Eleitoral, art. 355')],
  peg='Transpor a regra do CP para o eleitoral.', kw=['ação pública'])
I(P, 1, 'Corrupção eleitoral',
  'O crime de corrupção eleitoral consuma-se com a oferta de vantagem para obter voto, ainda que a oferta não seja aceita.', 'C',
  'Art. 299: crime **formal**, nas modalidades ativa e passiva (dar, oferecer, prometer, solicitar ou receber).',
  lei=[(CE + '299', 'para obter ou dar voto e para conseguir ou prometer abstenção, ainda que a oferta não seja aceita', None, 'Código Eleitoral, art. 299')],
  kw=['corrupção eleitoral', 'ainda que a oferta não seja aceita'])
I(P, 1, 'Prazo da denúncia',
  'Verificada a infração penal eleitoral, o Ministério Público oferecerá a denúncia em 15 dias.', 'E',
  'Art. 357: **10 dias**.',
  lei=[(CE + '357', 'Verificada a infração penal, o Ministério Público oferecerá a denúncia dentro do prazo de 10 (dez) dias.', None, 'Código Eleitoral, art. 357')],
  peg='Trocar o prazo.', kw=['10 (dez) dias', 'denúncia'])
I(P, 1, 'Conexão com crime comum',
  'Havendo conexão entre crime eleitoral e crime comum, os processos devem ser separados, ficando o crime comum com a Justiça Federal ou Estadual.', 'E',
  '**Inq 4.435 AgR-quarto** (STF, Plenário, 14/03/2019): compete à **Justiça Eleitoral** julgar os crimes comuns **conexos** aos eleitorais, cabendo a ela verificar a conexão.',
  juris=[J['INQ4435']], peg='Cindir os processos.', kw=['Inq 4.435', 'Justiça Eleitoral'])
I(P, 1, 'Boca de urna',
  'A arregimentação de eleitor ou a propaganda de boca de urna, no dia da eleição, constituem crime previsto na Lei 9.504/1997.', 'C',
  'Lei 9.504/1997, art. 39, § 5º, II: **boca de urna** é crime no dia da eleição — detenção de seis meses a um ano, com alternativa de prestação de serviços à comunidade.',
  lei=[(LE + '39', 'II - a arregimentação de eleitor ou a propaganda de boca de urna;', None, 'Lei 9.504/1997, art. 39, § 5º, II')],
  kw=['boca de urna', 'dia da eleição'])
# --- LPE-11 · Rodada 2
I(P, 2, 'Violência política de gênero',
  'Assediar ou humilhar candidata a cargo eletivo, com menosprezo à condição de mulher, para impedir ou dificultar sua campanha, é punido com detenção de seis meses a dois anos.', 'E',
  'Art. 326-B (Lei 14.192/2021): **reclusão, de 1 a 4 anos**, e multa, aumentada de 1/3 se a vítima for gestante, maior de 60 anos ou com deficiência.',
  lei=[(CE + '326-B', 'Pena - reclusão, de 1 (um) a 4 (quatro) anos, e multa.', None, 'Código Eleitoral, art. 326-B, pena')],
  peg='Rebaixar a pena.', kw=['violência política', 'reclusão, de 1 (um) a 4 (quatro) anos'])
I(P, 2, 'Fatos inverídicos na internet',
  'A divulgação de fatos sabidamente inverídicos sobre candidatos, quando feita pela internet ou rede social, tem a pena aumentada de metade a dois terços.', 'E',
  'Art. 323, § 2º, I (Lei 14.192/2021): aumento de **1/3 até metade**.',
  lei=[(CE + '323', 'Aumenta-se a pena de 1/3 (um terço) até metade se o crime:', None, 'Código Eleitoral, art. 323, § 2º')],
  peg='Trocar a fração.', kw=['fatos inverídicos', '1/3 (um terço) até metade'])
I(P, 2, 'Funcionário público eleitoral',
  'Para os efeitos penais do Código Eleitoral, são considerados membros e funcionários da Justiça Eleitoral os cidadãos nomeados para as mesas receptoras ou juntas apuradoras.', 'C',
  'Art. 283, III.',
  lei=[(CE + '283', 'III - Os cidadãos que hajam sido nomeados para as mesas receptoras ou Juntas Apuradoras;', None, 'Código Eleitoral, art. 283, III')],
  kw=['mesas receptoras'])
I(P, 2, 'Transporte de eleitores',
  'Descumprir as proibições de transporte e de fornecimento de refeições a eleitores da Lei 6.091/1974 é crime eleitoral punido com reclusão de quatro a seis anos.', 'C',
  'Lei 6.091/1974, art. 11, III (remete à pena do art. 302 do Código Eleitoral).',
  lei=[(TE + '11', 'III - descumprir a proibição dos artigos 5º, 8º e 10º;', None, 'Lei 6.091/1974, art. 11, III'), (TE + '11', 'Pena - reclusão de quatro a seis anos e pagamento de 200 a 300 dias-multa', None, 'Lei 6.091/1974, art. 11, III, pena')],
  kw=['Lei 6.091/1974', 'transporte'])

# ======================= LPE-12 · Crimes de trânsito =======================
P = 'DBA26-LPE-12'
I(P, 1, 'Socorro e flagrante',
  'Ao condutor envolvido em sinistro de trânsito com vítima não se imporá prisão em flagrante nem se exigirá fiança, se prestar pronto e integral socorro a ela.', 'C',
  'Art. 301 (redação da Lei 14.599/2023, que trocou "acidente" por "sinistro").',
  lei=[(CT + '301', 'não se imporá a prisão em flagrante nem se exigirá fiança, se prestar pronto e integral socorro àquela', None, 'CTB, art. 301')],
  kw=['pronto e integral socorro', 'prisão em flagrante'])
I(P, 1, 'Homicídio culposo e embriaguez',
  'O homicídio culposo na direção de veículo sob influência de álcool é punido com detenção de 2 a 4 anos, aumentada da metade.', 'E',
  'Art. 302, § 3º (Lei 13.546/2017): **reclusão, de 5 a 8 anos**, além da suspensão ou proibição da habilitação.',
  lei=[(CT + '302', 'Penas - reclusão, de cinco a oito anos, e suspensão ou proibição do direito de se obter a permissão ou a habilitação para dirigir veículo automotor.', None, 'CTB, art. 302, § 3º')],
  peg='Tratar a embriaguez como majorante.', kw=['reclusão, de cinco a oito anos', 'art. 302, § 3º'])
I(P, 1, 'Lesão culposa e Lei 9.099',
  'Aplicam-se à lesão corporal culposa no trânsito a composição civil, a transação e a exigência de representação, salvo se o agente estava sob influência de álcool, em racha ou a mais de 50 km/h acima do limite.', 'C',
  'Art. 291, § 1º: nessas três hipóteses, instaura-se **inquérito policial** (§ 2º).',
  lei=[(CT + '291', 'Aplica-se aos crimes de trânsito de lesão corporal culposa o disposto nos arts. 74, 76 e 88 da Lei no 9.099', None, 'CTB, art. 291, § 1º')],
  kw=['arts. 74, 76 e 88', 'lesão corporal culposa'])
I(P, 1, 'Prova da embriaguez',
  'O crime de embriaguez ao volante só pode ser provado por exame de sangue ou etilômetro que indique a concentração mínima legal.', 'E',
  'Art. 306, § 2º: admite **teste de alcoolemia, exame clínico, perícia, vídeo, prova testemunhal** ou outros meios, com direito à contraprova; os sinais de alteração psicomotora bastam (§ 1º, II).',
  lei=[(CT + '306', 'mediante teste de alcoolemia ou toxicológico, exame clínico, perícia, vídeo, prova testemunhal ou outros meios de prova em direito admitidos', None, 'CTB, art. 306, § 2º')],
  peg='Exigir prova tarifada.', kw=['prova testemunhal', 'art. 306'])
I(P, 1, 'Entregar a direção a inabilitado',
  'O crime de entregar a direção de veículo a pessoa não habilitada é de perigo abstrato e independe de lesão ou de perigo concreto na condução.', 'C',
  '**Súmula 575/STJ** (art. 310 do CTB).',
  lei=[(CT + '310', 'Permitir, confiar ou entregar a direção de veículo automotor a pessoa não habilitada', None, 'CTB, art. 310')],
  juris=[J['S575']], kw=['Súmula 575/STJ', 'perigo abstrato'])
I(P, 1, 'Embriaguez e falta de habilitação',
  'Quem dirige embriagado e sem habilitação responde só pela embriaguez ao volante, que absorve a direção sem habilitação.', 'E',
  '**Súmula 664/STJ**: é **inaplicável a consunção** entre os arts. 306 e 309 do CTB.',
  juris=[J['S664']], peg='Aplicar a consunção.', kw=['Súmula 664/STJ', 'consunção'])
I(P, 1, 'Direção sem habilitação',
  'Dirigir sem habilitação em via pública só é crime se gerar perigo de dano; sem ele, há apenas infração administrativa.', 'C',
  'Art. 309 e **Súmula 720/STF**: o CTB derrogou o art. 32 da LCP quanto à direção sem habilitação em vias terrestres.',
  lei=[(CT + '309', 'sem a devida Permissão para Dirigir ou Habilitação ou, ainda, se cassado o direito de dirigir, gerando perigo de dano', None, 'CTB, art. 309')],
  juris=[J['STF720']], kw=['perigo de dano', 'Súmula 720/STF'])
I(P, 1, 'Substituição da pena',
  'Ao homicídio culposo e à lesão corporal culposa grave cometidos sob influência de álcool aplica-se normalmente a substituição por pena restritiva de direitos, pois são crimes culposos.', 'E',
  'Art. 312-B (Lei 14.071/2020): não se aplica a esses crimes (arts. 302, § 3º, e 303, § 2º) o **art. 44, I, do CP**.',
  lei=[(CT + '312-B', 'Aos crimes previstos no § 3º do art. 302 e no § 2º do art. 303 deste Código não se aplica o disposto no inciso I do caput do art. 44', None, 'CTB, art. 312-B')],
  peg='Usar a regra geral dos crimes culposos.', kw=['art. 312-B', 'art. 44'])
# --- LPE-12 · Rodada 2
I(P, 2, 'Duração da suspensão',
  'A suspensão ou proibição de se obter a permissão ou a habilitação, como pena, dura de seis meses a dois anos.', 'E',
  'Art. 293: de **dois meses a cinco anos**; não corre enquanto o condenado estiver preso (§ 2º).',
  lei=[(CT + '293', 'tem a duração de dois meses a cinco anos', None, 'CTB, art. 293')],
  kw=['dois meses a cinco anos'])
I(P, 2, 'Omissão de socorro',
  'Não há crime de omissão de socorro no trânsito se a vítima teve morte instantânea ou se terceiros a socorreram.', 'E',
  'Art. 304, par. ún.: o condutor responde **ainda que** a omissão seja suprida por terceiros ou se trate de vítima com **morte instantânea** ou ferimentos leves.',
  lei=[(CT + '304', 'ainda que a sua omissão seja suprida por terceiros ou que se trate de vítima com morte instantânea ou com ferimentos leves', None, 'CTB, art. 304, par. ún.')],
  peg='Criar exceções que a lei afasta.', kw=['morte instantânea'])
I(P, 2, 'Racha com morte',
  'Se do racha resultar morte e as circunstâncias demonstrarem que o agente não quis o resultado nem assumiu o risco, a pena é de reclusão de 5 a 10 anos.', 'C',
  'Art. 308, § 2º — forma preterdolosa; havendo dolo eventual, responde por homicídio.',
  lei=[(CT + '308', 'a pena privativa de liberdade é de reclusão de 5 (cinco) a 10 (dez) anos', None, 'CTB, art. 308, § 2º')],
  kw=['racha', 'reclusão de 5 (cinco) a 10 (dez) anos'])
I(P, 2, 'Recurso da suspensão cautelar',
  'Da decisão que decreta a suspensão cautelar da habilitação cabe apelação, com efeito suspensivo.', 'E',
  'Art. 294, par. ún.: cabe **recurso em sentido estrito**, **sem** efeito suspensivo.',
  lei=[(CT + '294', 'caberá recurso em sentido estrito, sem efeito suspensivo', None, 'CTB, art. 294, par. ún.')],
  peg='Trocar o recurso.', kw=['recurso em sentido estrito'])
I(P, 2, 'Faixa de pedestres',
  'No homicídio culposo de trânsito, a pena é aumentada de 1/3 à metade se o crime é praticado em faixa de pedestres ou na calçada.', 'C',
  'Art. 302, § 1º, II; a mesma fração vale para a lesão culposa (art. 303, § 1º).',
  lei=[(CT + '302', 'II - praticá-lo em faixa de pedestres ou na calçada;', None, 'CTB, art. 302, § 1º, II')],
  kw=['faixa de pedestres', '1/3 (um terço) à metade'])

# ======================= LPE-13 · Execução penal =======================
P = 'DBA26-LPE-13'
I(P, 1, 'Progressão: regra geral (2026)',
  'Pela redação vigente da LEP, a regra geral de progressão exige o cumprimento de ao menos 1/6 da pena no regime anterior e mérito do preso, ressalvadas as frações especiais dos incisos.', 'C',
  'Art. 112, caput (**Lei 15.402/2026**): 1/6 como regra, com frações maiores para crimes com violência, reincidência e hediondos.',
  lei=[(EP + '112', 'quando o preso tiver cumprido ao menos 1/6 (um sexto) da pena no regime anterior e seu mérito indicar a progressão', None, 'LEP, art. 112, caput')],
  kw=['1/6 (um sexto)', 'Lei 15.402/2026'])
I(P, 1, 'Hediondo primário (2026)',
  'O condenado primário por crime hediondo progride após cumprir 40% da pena.', 'E',
  'Art. 112, V (**Lei 15.358/2026**): **70%**. Os 40% eram a redação do Pacote Anticrime, superada.',
  lei=[(EP + '112', 'V - 70% (setenta por cento) da pena, se o apenado for condenado pela prática de crime hediondo ou equiparado, se for primário;', None, 'LEP, art. 112, V')],
  peg='Citar a fração revogada.', kw=['70%', 'hediondo'])
I(P, 1, 'Falta grave e progressão',
  'A falta grave durante a execução interrompe o prazo para a progressão, e a nova contagem tem como base a pena remanescente.', 'C',
  'Art. 112, § 6º, e **Súmula 534/STJ**. Já a falta grave não interrompe o prazo do livramento condicional (Súmula 441/STJ).',
  lei=[(EP + '112', 'O cometimento de falta grave durante a execução da pena privativa de liberdade interrompe o prazo para a obtenção da progressão', None, 'LEP, art. 112, § 6º')],
  juris=[J['S534']], kw=['falta grave', 'pena remanescente'])
I(P, 1, 'Duração do RDD',
  'O regime disciplinar diferenciado tem duração máxima de 360 dias, vedada a repetição.', 'E',
  'Art. 52, I (Lei 13.964/2019): até **2 anos**, sem prejuízo de repetição por nova falta grave da mesma espécie, e prorrogável por períodos de 1 ano (§ 4º).',
  lei=[(EP + '52', 'I - duração máxima de até 2 (dois) anos, sem prejuízo de repetição da sanção por nova falta grave de mesma espécie;', None, 'LEP, art. 52, I')],
  peg='Citar o limite antigo.', kw=['regime disciplinar diferenciado', '2 (dois) anos'])
I(P, 1, 'Saída temporária e crime violento',
  'Não tem direito à saída temporária nem a trabalho externo sem vigilância direta o condenado por crime hediondo ou com violência ou grave ameaça contra pessoa.', 'C',
  'Art. 122, § 2º (Lei 14.843/2024), que também reduziu as hipóteses de saída à frequência a curso.',
  lei=[(EP + '122', 'Não terá direito à saída temporária de que trata o caput deste artigo ou a trabalho externo sem vigilância direta o condenado que cumpre pena por praticar crime hediondo', None, 'LEP, art. 122, § 2º')],
  kw=['saída temporária', 'Lei 14.843/2024'])
I(P, 1, 'Perda dos dias remidos',
  'Cometida falta grave, o condenado perde todos os dias remidos, como afirma a Súmula Vinculante 9.', 'E',
  'Art. 127: o juiz pode revogar **até 1/3** do tempo remido. A **SV 9** foi **cancelada** pelo STF em 2025 (Informativo 1.193), por incompatível com essa redação.',
  lei=[(EP + '127', 'Em caso de falta grave, o juiz poderá revogar até 1/3 (um terço) do tempo remido', None, 'LEP, art. 127')],
  peg='Invocar súmula cancelada.', kw=['até 1/3', 'SV 9'])
I(P, 1, 'Saída temporária: competência',
  'A saída temporária é ato jurisdicional e não pode ser delegada à direção do estabelecimento prisional.', 'C',
  '**Súmula 520/STJ**.',
  juris=[J['S520']], kw=['Súmula 520/STJ', 'ato jurisdicional'])
I(P, 1, 'Procedimento da falta',
  'O reconhecimento de falta disciplinar dispensa defesa técnica, bastando a oitiva do preso pelo diretor do estabelecimento.', 'E',
  '**Súmula 533/STJ**: exige **procedimento administrativo** com defesa por **advogado constituído ou defensor público**.',
  juris=[J['S533']], peg='Dispensar a defesa técnica.', kw=['Súmula 533/STJ', 'defensor público'])
I(P, 1, 'Celular no presídio',
  'Ter em sua posse aparelho telefônico que permita a comunicação com o ambiente externo é falta grave, e a posse de componentes essenciais do aparelho também a configura.', 'C',
  'Art. 50, VII, e **Súmula 660/STJ**.',
  lei=[(EP + '50', 'tiver em sua posse, utilizar ou fornecer aparelho telefônico, de rádio ou similar', None, 'LEP, art. 50, VII')],
  juris=[J['S660']], kw=['Súmula 660/STJ', 'aparelho telefônico'])
# --- LPE-13 · Rodada 2
I(P, 2, 'Gestante ou mãe',
  'A mulher gestante ou mãe ou responsável por criança ou pessoa com deficiência pode progredir após 1/8 da pena, se atendidos cumulativamente os demais requisitos legais.', 'C',
  'Art. 112, § 3º (Lei 13.769/2018): sem violência ou grave ameaça, não contra o filho, primária, bom comportamento e sem integrar organização criminosa.',
  lei=[(EP + '112', 'III - ter cumprido ao menos 1/8 (um oitavo) da pena no regime anterior;', None, 'LEP, art. 112, § 3º, III')],
  kw=['1/8 (um oitavo)', 'gestante'])
I(P, 2, 'Visita no RDD (2026)',
  'A visita ao preso em regime disciplinar diferenciado será gravada em sistema de áudio ou de áudio e vídeo, com autorização judicial, e acompanhada por policial penal.', 'C',
  'Art. 52, § 6º (redação da **Lei 15.358/2026**).',
  lei=[(EP + '52', 'será gravada em sistema de áudio ou de áudio e vídeo, com autorização judicial, e acompanhada por policial penal', None, 'LEP, art. 52, § 6º')],
  kw=['Lei 15.358/2026', 'policial penal'])
I(P, 2, 'Prisão domiciliar no aberto',
  'Admite-se o recolhimento em residência particular do condenado em regime aberto maior de 60 anos.', 'E',
  'Art. 117, I: **maior de 70 anos**; também doença grave, condenada com filho menor ou deficiente e gestante.',
  lei=[(EP + '117', 'I - condenado maior de 70 (setenta) anos;', None, 'LEP, art. 117, I')],
  peg='Trocar 70 por 60.', kw=['maior de 70', 'regime aberto'])
I(P, 2, 'Perícia do celular',
  'O reconhecimento da falta grave pela posse de celular depende de perícia que comprove o funcionamento do aparelho.', 'E',
  '**Súmula 661/STJ**: a falta grave **prescinde da perícia** do celular ou de seus componentes.',
  juris=[J['S661']], peg='Exigir perícia.', kw=['Súmula 661/STJ', 'prescinde da perícia'])
I(P, 2, 'Monitoramento de encontros (2026)',
  'O monitoramento dos encontros no parlatório de presos ligados a organizações criminosas ultraviolentas, grupos paramilitares ou milícias pode ser requerido pelo delegado de polícia.', 'C',
  'Art. 41-A, § 1º (**Lei 15.358/2026**): também pelo MP ou pela administração penitenciária.',
  lei=[(EP + '41-A', 'O monitoramento poderá ser requerido pelo delegado de polícia, pelo Ministério Público ou pela administração penitenciária.', None, 'LEP, art. 41-A, § 1º')],
  kw=['Lei 15.358/2026', 'parlatório'])
I(P, 2, 'Exame criminológico',
  'Pela redação atual da LEP, o exame criminológico é facultativo para a progressão, cabendo ao juiz determiná-lo apenas pelas peculiaridades do caso.', 'E',
  'Art. 112, § 1º (Lei 14.843/2024): a progressão depende de boa conduta **e dos resultados do exame criminológico** "em todos os casos". A Súmula 439/STJ refletia a lei anterior.',
  lei=[(EP + '112', 'e pelos resultados do exame criminológico, respeitadas as normas que vedam a progressão', None, 'LEP, art. 112, § 1º')],
  peg='Aplicar o regime anterior à Lei 14.843/2024.', kw=['exame criminológico', 'Lei 14.843/2024'])

# ======================= LPE-14 · Juizados Especiais Criminais =======================
P = 'DBA26-LPE-14'
I(P, 1, 'Menor potencial ofensivo',
  'Consideram-se infrações de menor potencial ofensivo as contravenções penais e os crimes com pena máxima não superior a 2 anos, cumulada ou não com multa.', 'C',
  'Art. 61 (Lei 11.313/2006).',
  lei=[(JE + '61', 'as contravenções penais e os crimes a que a lei comine pena máxima não superior a 2 (dois) anos, cumulada ou não com multa', None, 'Lei 9.099/1995, art. 61')],
  kw=['menor potencial ofensivo', 'pena máxima'])
I(P, 1, 'Termo circunstanciado',
  'Ao autor do fato que, após a lavratura do termo circunstanciado, for encaminhado ao Juizado ou assumir o compromisso de comparecer, não se imporá prisão em flagrante nem se exigirá fiança.', 'C',
  'Art. 69, par. ún.',
  lei=[(JE + '69', 'não se imporá prisão em flagrante, nem se exigirá fiança', None, 'Lei 9.099/1995, art. 69, par. ún.')],
  kw=['termo circunstanciado', 'compromisso'])
I(P, 1, 'Composição civil',
  'Na ação penal pública condicionada à representação, o acordo de composição civil homologado acarreta a renúncia ao direito de representação.', 'C',
  'Art. 74, par. ún.; na pública incondicionada, a composição não impede a transação.',
  lei=[(JE + '74', 'o acordo homologado acarreta a renúncia ao direito de queixa ou representação', None, 'Lei 9.099/1995, art. 74, par. ún.')],
  kw=['composição dos danos civis', 'renúncia'])
I(P, 1, 'Transação: prazo de impedimento',
  'Não se admite proposta de transação penal ao autor beneficiado por transação anterior nos últimos 3 anos.', 'E',
  'Art. 76, § 2º, II: o prazo é de **cinco anos**.',
  lei=[(JE + '76', 'II - ter sido o agente beneficiado anteriormente, no prazo de cinco anos', None, 'Lei 9.099/1995, art. 76, § 2º, II')],
  peg='Trocar o prazo.', kw=['cinco anos', 'transação penal'])
I(P, 1, 'Transação e reincidência',
  'A pena aplicada em transação penal gera reincidência e consta da certidão de antecedentes criminais.', 'E',
  'Art. 76, §§ 4º e 6º: **não importa em reincidência**, fica registrada só para impedir novo benefício em 5 anos e não consta da certidão.',
  lei=[(JE + '76', 'que não importará em reincidência', None, 'Lei 9.099/1995, art. 76, § 4º')],
  peg='Atribuir efeito de condenação.', kw=['não importará em reincidência'])
I(P, 1, 'Representação nas lesões',
  'Dependem de representação as ações penais por lesões corporais leves e lesões culposas.', 'C',
  'Art. 88 — exceto na violência doméstica contra a mulher, em que a lesão é de ação pública incondicionada (**Súmula 542/STJ**).',
  lei=[(JE + '88', 'dependerá de representação a ação penal relativa aos crimes de lesões corporais leves e lesões culposas', None, 'Lei 9.099/1995, art. 88')],
  juris=[J['S542']], kw=['lesões corporais leves', 'representação'])
I(P, 1, 'Suspensão condicional do processo',
  'A suspensão condicional do processo cabe nos crimes com pena máxima igual ou inferior a um ano, apenas se de competência do Juizado.', 'E',
  'Art. 89: a referência é a **pena mínima** igual ou inferior a um ano, **abrangidos ou não** pela Lei 9.099; período de prova de 2 a 4 anos.',
  lei=[(JE + '89', 'Nos crimes em que a pena mínima cominada for igual ou inferior a um ano, abrangidas ou não por esta Lei', None, 'Lei 9.099/1995, art. 89')],
  peg='Trocar pena mínima por máxima.', kw=['pena mínima', 'abrangidas ou não'])
I(P, 1, 'Justiça Militar',
  'As disposições da Lei 9.099/1995 aplicam-se aos crimes militares de menor potencial ofensivo.', 'E',
  'Art. 90-A: **não se aplicam** no âmbito da Justiça Militar.',
  lei=[(JE + '90-A', 'As disposições desta Lei não se aplicam no âmbito da Justiça Militar.', None, 'Lei 9.099/1995, art. 90-A')],
  peg='Estender à Justiça Militar.', kw=['Justiça Militar'])
# --- LPE-14 · Rodada 2
I(P, 2, 'Coisa julgada na transação',
  'A homologação da transação penal não faz coisa julgada material; descumpridas as cláusulas, o MP pode oferecer denúncia.', 'C',
  '**Súmula Vinculante 35**.',
  juris=[J['SV35']], kw=['Súmula Vinculante 35', 'coisa julgada material'])
I(P, 2, 'Maria da Penha',
  'Nos crimes sujeitos à Lei Maria da Penha cabe suspensão condicional do processo, embora não caiba transação penal.', 'E',
  '**Súmula 536/STJ**: **nem** suspensão condicional do processo **nem** transação (Lei 11.340/2006, art. 41).',
  juris=[J['S536']], peg='Admitir um dos institutos.', kw=['Súmula 536/STJ'])
I(P, 2, 'Prescrição na suspensão',
  'Não corre a prescrição durante o prazo de suspensão condicional do processo.', 'C',
  'Art. 89, § 6º.',
  lei=[(JE + '89', 'Não correrá a prescrição durante o prazo de suspensão do processo.', None, 'Lei 9.099/1995, art. 89, § 6º')],
  kw=['prescrição', 'suspensão do processo'])
I(P, 2, 'Concurso de crimes',
  'Para a suspensão condicional do processo em concurso de crimes, considera-se a pena mínima de cada delito isoladamente.', 'E',
  '**Súmula 243/STJ**: no concurso material, formal ou na continuidade, conta-se o **somatório** ou a **majorante**; se passar de 1 ano, não cabe.',
  juris=[J['S243']], peg='Isolar as penas.', kw=['Súmula 243/STJ', 'somatório'])
I(P, 2, 'Representação na audiência',
  'O não oferecimento da representação na audiência preliminar não implica decadência, podendo o direito ser exercido no prazo legal.', 'C',
  'Art. 75, par. ún.',
  lei=[(JE + '75', 'O não oferecimento da representação na audiência preliminar não implica decadência do direito', None, 'Lei 9.099/1995, art. 75, par. ún.')],
  kw=['audiência preliminar', 'decadência'])
