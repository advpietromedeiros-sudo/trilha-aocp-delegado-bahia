# Jurisprudência do Pente Fino de Legislação Penal Extravagante (08/11/2026).
# REAPROVEITA, sem mudar uma letra, as entradas de pen/pen_juris.py e cpp/cpp_juris.py (conferidas em 08/11/2026) e
# acrescenta as abaixo, cada uma CONFERIDA em 08/11/2026:
#  STJ súmulas 108, 164, 265, 342, 439, 492, 520, 533, 575, 587, 600, 605, 607 e 639: processo.stj.jus.br/SCON/sumstj
#   (data = "julgado em"; nenhuma com indicação de cancelamento). A Súmula 512/STJ aparece no SCON como CANCELADA e
#   NÃO é usada (tráfico privilegiado: vale a SV 63 e o art. 112, § 5º, da LEP).
#  STJ súmulas 658, 660, 661 e 662: notícia oficial do STJ de 15/09/2023 (Terceira Seção, sessão de 13/09/2023).
#  STJ súmulas 667 e 668: notícia oficial do STJ de 22/04/2024 (sessão de 18/04/2024). Súmula 669: Livro de Súmulas
#   do STJ (stj.jus.br; julgada em 12/06/2024). Súmula 664: notícia oficial do STJ de 09/11/2023 (aprovada em 08/11/2023).
#  STF SV 24: portal.stf.jus.br/jurisprudencia/sumariosumulas.asp (publicação no DJe de 11/12/2009, a data que a página
#   traz). SV 63: notícia oficial do STF de 30/09/2025 e Informativo STF 1.193 (PSV 125, sessão virtual finalizada em
#   25/09/2025). No mesmo Informativo 1.193 consta o CANCELAMENTO da SV 9 (PSV 60): ela NÃO é usada.
#  STF súmulas 498, 703 e 720: PDF oficial "Enunciados das Súmulas do STF 1 a 736" (data = Sessão Plenária).
#  STF Tema 506/RG (RE 635.659): Informativo STF 1.143 (julgamento finalizado em 26/06/2024) e notícia oficial.
#  STF Inq 4.435 AgR-quarto: notícia oficial do STF (Plenário, 14/03/2019).
#  STF RE 548.181: Informativo STF 714 e notícia oficial (Primeira Turma, 06/08/2013).
import pathlib, sys
_AQUI = pathlib.Path(__file__).resolve().parent
for _p in ('pen', 'cpp'):
    if str(_AQUI.parent / _p) not in sys.path:
        sys.path.insert(0, str(_AQUI.parent / _p))
from base import _s
from pen_juris import J as _JPEN
from cpp_juris import J as _JCPP

SCON = 'processo.stj.jus.br/SCON/sumstj'
STJNOT = 'stj.jus.br — notícia oficial da aprovação da súmula'
STFPDF = 'stf.jus.br — Enunciados das Súmulas do STF 1 a 736 (PDF oficial)'
SV = 'portal.stf.jus.br — Súmulas Vinculantes (data de publicação do enunciado no DJe)'
STFNOT = 'portal.stf.jus.br — notícia oficial do julgamento'
J = dict(_JCPP)
J.update(_JPEN)
J.update({
    # ---------------- STJ — súmulas (SCON)
    'S108': _s('STJ', 'Súmula 108/STJ', '16/06/1994', 'A aplicação de medidas socioeducativas ao adolescente, pela prática de ato infracional, é da competência exclusiva do juiz.', SCON),
    'S164': _s('STJ', 'Súmula 164/STJ', '14/08/1996', 'O prefeito municipal, após a extinção do mandato, continua sujeito a processo por crime previsto no art. 1º do Decreto-Lei 201/1967.', SCON),
    'S265': _s('STJ', 'Súmula 265/STJ', '22/05/2002', 'É necessária a oitiva do menor infrator antes de decretar-se a regressão da medida socioeducativa.', SCON),
    'S342': _s('STJ', 'Súmula 342/STJ', '27/06/2007', 'No procedimento para aplicação de medida socioeducativa, é nula a desistência de outras provas em face da confissão do adolescente.', SCON),
    'S439': _s('STJ', 'Súmula 439/STJ', '28/04/2010', 'Admite-se o exame criminológico pelas peculiaridades do caso, desde que em decisão motivada.', SCON),
    'S492': _s('STJ', 'Súmula 492/STJ', '08/08/2012', 'O ato infracional análogo ao tráfico de drogas, por si só, não conduz obrigatoriamente à imposição de medida socioeducativa de internação do adolescente.', SCON),
    'S520': _s('STJ', 'Súmula 520/STJ', '25/03/2015', 'O benefício de saída temporária no âmbito da execução penal é ato jurisdicional insuscetível de delegação à autoridade administrativa do estabelecimento prisional.', SCON),
    'S533': _s('STJ', 'Súmula 533/STJ', '10/06/2015', 'Para reconhecer falta disciplinar na execução penal, é imprescindível procedimento administrativo instaurado pelo diretor do estabelecimento, assegurada a defesa por advogado constituído ou defensor público nomeado.', SCON),
    'S575': _s('STJ', 'Súmula 575/STJ', '22/06/2016', 'Constitui crime permitir, confiar ou entregar a direção de veículo automotor a pessoa não habilitada, ou em qualquer das situações do art. 310 do CTB, independentemente de lesão ou de perigo de dano concreto na condução do veículo.', SCON),
    'S587': _s('STJ', 'Súmula 587/STJ', '13/09/2017', 'Para a majorante do art. 40, V, da Lei 11.343/2006, é desnecessária a efetiva transposição de fronteiras entre estados da Federação, bastando a demonstração inequívoca da intenção de realizar o tráfico interestadual.', SCON),
    'S600': _s('STJ', 'Súmula 600/STJ', '22/11/2017', 'Para a configuração da violência doméstica e familiar prevista no art. 5º da Lei 11.340/2006 não se exige a coabitação entre autor e vítima.', SCON),
    'S605': _s('STJ', 'Súmula 605/STJ', '14/03/2018', 'A superveniência da maioridade penal não interfere na apuração de ato infracional nem na aplicabilidade de medida socioeducativa em curso, inclusive na liberdade assistida, enquanto não atingida a idade de 21 anos.', SCON),
    'S607': _s('STJ', 'Súmula 607/STJ', '11/04/2018', 'A majorante do tráfico transnacional de drogas (art. 40, I, da Lei 11.343/2006) configura-se com a prova da destinação internacional das drogas, ainda que não consumada a transposição de fronteiras.', SCON),
    'S639': _s('STJ', 'Súmula 639/STJ', '27/11/2019', 'Não fere o contraditório e o devido processo decisão que, sem ouvida prévia da defesa, determine transferência ou permanência de custodiado em estabelecimento penitenciário federal.', SCON),
    # ---------------- STJ — súmulas (notícias oficiais e Livro de Súmulas)
    'S658': _s('STJ', 'Súmula 658/STJ', '13/09/2023', 'O crime de apropriação indébita tributária pode ocorrer tanto em operações próprias como em razão de substituição tributária.', STJNOT),
    'S660': _s('STJ', 'Súmula 660/STJ', '13/09/2023', 'A posse, pelo apenado, de aparelho celular ou de seus componentes essenciais constitui falta grave.', STJNOT),
    'S661': _s('STJ', 'Súmula 661/STJ', '13/09/2023', 'A falta grave prescinde da perícia do celular apreendido ou de seus componentes essenciais.', STJNOT),
    'S662': _s('STJ', 'Súmula 662/STJ', '13/09/2023', 'Para a prorrogação do prazo de permanência no sistema penitenciário federal, é prescindível fato novo; basta constar, em decisão fundamentada, a persistência dos motivos que ensejaram a transferência inicial do preso.', STJNOT),
    'S664': _s('STJ', 'Súmula 664/STJ', '08/11/2023', 'É inaplicável a consunção entre o delito de embriaguez ao volante e o de condução de veículo automotor sem habilitação.', STJNOT),
    'S667': _s('STJ', 'Súmula 667/STJ', '18/04/2024', 'Eventual aceitação de proposta de suspensão condicional do processo não prejudica a análise do pedido de trancamento de ação penal.', STJNOT),
    'S668': _s('STJ', 'Súmula 668/STJ', '18/04/2024', 'Não é hediondo o delito de porte ou posse de arma de fogo de uso permitido, ainda que com numeração, marca ou qualquer outro sinal de identificação raspado, suprimido ou adulterado.', STJNOT),
    'S669': _s('STJ', 'Súmula 669/STJ', '12/06/2024', 'O fornecimento de bebida alcoólica para criança ou adolescente, após a Lei 13.106/2015, configura o crime do art. 243 do ECA.', 'stj.jus.br — Livro de Súmulas do STJ'),
    # ---------------- STF
    'SV24': _s('STF', 'Súmula Vinculante 24 (publicada no DJe de 11/12/2009)', '11/12/2009', 'Não se tipifica crime material contra a ordem tributária, previsto no art. 1º, incisos I a IV, da Lei 8.137/1990, antes do lançamento definitivo do tributo.', SV),
    'SV63': _s('STF', 'Súmula Vinculante 63 (PSV 125, sessão virtual finalizada em 25/09/2025 — Informativo 1.193)', '25/09/2025', 'O tráfico privilegiado (art. 33, § 4º, da Lei 11.343/2006) não configura crime hediondo, afastando-se os parâmetros mais rigorosos de progressão de regime e de livramento condicional.', 'portal.stf.jus.br — notícia oficial de 30/09/2025 e Informativo STF 1.193'),
    'STF498': _s('STF', 'Súmula 498/STF', '03/12/1969', 'Compete à Justiça dos Estados, em ambas as instâncias, o processo e o julgamento dos crimes contra a economia popular.', STFPDF),
    'STF703': _s('STF', 'Súmula 703/STF', '24/09/2003', 'A extinção do mandato do prefeito não impede a instauração de processo pela prática dos crimes previstos no art. 1º do DL 201/1967.', STFPDF),
    'STF720': _s('STF', 'Súmula 720/STF', '24/09/2003', 'O art. 309 do CTB, que reclama decorra do fato perigo de dano, derrogou o art. 32 da Lei das Contravenções Penais no tocante à direção sem habilitação em vias terrestres.', STFPDF),
    'RG506': _s('STF', 'Tema 506/RG — RE 635.659/SP (julgamento finalizado em 26/06/2024; Informativo 1.143)', '26/06/2024', 'Não é infração penal adquirir, guardar, ter em depósito, transportar ou trazer consigo maconha para consumo pessoal (ilícito extrapenal, com advertência e medida educativa aplicadas pelo juiz, sem efeito penal); presume-se usuário quem tem até 40 g ou seis plantas-fêmeas, presunção relativa que a autoridade policial pode afastar fundamentadamente diante de indícios de tráfico.', 'stf.jus.br — Informativo 1.143 e notícia oficial'),
    'INQ4435': _s('STF', 'Inq 4.435 AgR-quarto, Plenário', '14/03/2019', 'Compete à Justiça Eleitoral processar e julgar os crimes comuns conexos aos crimes eleitorais, cabendo-lhe analisar, caso a caso, a existência da conexão e, se ausente, remeter os autos à Justiça competente.', STFNOT),
    'RE548181': _s('STF', 'RE 548.181/PR, Primeira Turma (Informativo 714)', '06/08/2013', 'A responsabilização penal da pessoa jurídica por crime ambiental (CF, art. 225, § 3º) não está condicionada à simultânea persecução de pessoa física: afastada a exigência da "dupla imputação".', 'stf.jus.br — Informativo 714 e notícia oficial'),
})
