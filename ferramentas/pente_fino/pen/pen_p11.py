# Pente Fino de Direito Penal — PEN-11 (jurisprudência aplicada dos tribunais superiores e legislação de cada tópico),
# tratado como ponto de FECHAMENTO: jurisprudência transversal, toda conferida em fonte oficial (pen_juris.py) (08/11/2026).
from base import I
from pen_juris import J

CP = 'CP:'
P = 'DBA26-PEN-11'
I(P, 1, 'Violência doméstica: bagatela e substituição',
  'Nos crimes ou contravenções praticados contra a mulher no âmbito das relações domésticas, é inaplicável o princípio da insignificância, e, havendo violência ou grave ameaça, não cabe substituir a pena privativa por restritiva de direitos.', 'C',
  '**Súmulas 589 e 588/STJ** — duas faces da mesma política de proteção (arts. 44, I, do CP e 41 da Lei 11.340/2006).',
  juris=[J['S589'], J['S588']], kw=['Súmulas 589 e 588/STJ'])
I(P, 1, 'Consumação do roubo',
  'O roubo só se consuma quando o agente obtém a posse mansa e pacífica do bem, fora da vigilância da vítima.', 'E',
  '**Súmula 582/STJ**: consuma-se com a **inversão da posse** mediante violência ou grave ameaça, ainda que por breve tempo e com perseguição imediata.',
  lei=[(CP + '157', 'Art. 157 - Subtrair coisa móvel alheia, para si ou para outrem, mediante grave ameaça ou violência a pessoa', None, 'CP, art. 157, caput')],
  juris=[J['S582']], peg='Exigir posse mansa e pacífica.', kw=['Súmula 582/STJ', 'inversão da posse'])
I(P, 1, 'Majorantes do roubo',
  'O aumento na terceira fase do roubo circunstanciado exige fundamentação concreta, não bastando a mera indicação do número de majorantes.', 'C',
  '**Súmula 443/STJ**: vale para escolher a fração entre 1/3 e metade do art. 157, § 2º.',
  lei=[(CP + '157', '§ 2º A pena aumenta-se de 1/3 (um terço) até metade:', None, 'CP, art. 157, § 2º')],
  juris=[J['S443']], kw=['Súmula 443/STJ'])
I(P, 1, 'Fraude à licitação: natureza',
  'O crime de fraude à licitação é material e exige prova do prejuízo ao erário.', 'E',
  '**Súmula 645/STJ**: é **formal** — dispensa prejuízo ou obtenção de vantagem.',
  juris=[J['S645']], peg='Exigir resultado naturalístico.', kw=['Súmula 645/STJ', 'formal'])
I(P, 1, 'Restituição e insignificância',
  'A restituição imediata e integral do bem furtado não constitui, por si só, motivo suficiente para a incidência do princípio da insignificância.', 'C',
  '**Tema 1.205/STJ** (24/10/2023). A restituição pode, quando muito, servir ao arrependimento posterior (art. 16) ou ao privilégio.',
  juris=[J['T1205']], kw=['Tema 1.205/STJ'])
I(P, 1, 'Cheque sem fundos pago',
  'O pagamento do cheque emitido sem provisão de fundos após o recebimento da denúncia obsta o prosseguimento da ação penal.', 'E',
  '**Súmula 554/STF**: o pagamento **após** o recebimento da denúncia **não obsta** a ação (a leitura *a contrario*, que a doutrina extrai do enunciado, dá relevância ao pagamento anterior ao recebimento).',
  lei=[(CP + '171', 'VI - emite cheque, sem suficiente provisão de fundos em poder do sacado, ou lhe frustra o pagamento.', None, 'CP, art. 171, § 2º, VI')],
  juris=[J['STF554']], peg='Dar efeito extintivo ao pagamento tardio.', kw=['Súmula 554/STF'])
# --- PEN-11 · Rodada 2
I(P, 2, 'Corrupção de menores (ECA)',
  'A configuração do crime de corrupção de menores do art. 244-B do ECA independe da prova da efetiva corrupção do menor, por se tratar de delito formal.', 'C',
  '**Súmula 500/STJ**.',
  juris=[J['S500']], kw=['Súmula 500/STJ'])
I(P, 2, 'Sinal clandestino de internet',
  'O princípio da insignificância aplica-se à transmissão clandestina de sinal de internet via radiofrequência, por ausência de lesão relevante.', 'E',
  '**Súmula 606/STJ**: **não se aplica** (art. 183 da Lei 9.472/1997).',
  juris=[J['S606']], peg='Aplicar a bagatela.', kw=['Súmula 606/STJ'])
I(P, 2, 'Vetores da insignificância',
  'Para o STF, a insignificância exige mínima ofensividade da conduta, nenhuma periculosidade social da ação, reduzidíssimo grau de reprovabilidade do comportamento e inexpressividade da lesão jurídica.', 'C',
  '**HC 84.412/SP** (Segunda Turma, 19/10/2004): vetores **cumulativos**, aplicados a todos os crimes da Parte Especial.',
  juris=[J['HC84412']], kw=['HC 84.412', 'cumulativos'])
I(P, 2, 'Arma com numeração raspada',
  'A abolitio criminis temporária do Estatuto do Desarmamento alcança a posse de arma de uso permitido com numeração raspada praticada a qualquer tempo.', 'E',
  '**Súmula 513/STJ**: só a posse praticada **até 23/10/2005**.',
  juris=[J['S513']], peg='Eternizar a vacatio.', kw=['Súmula 513/STJ', '23/10/2005'])
