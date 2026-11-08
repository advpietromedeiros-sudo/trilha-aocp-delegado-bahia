# Pente Fino de Direito Penal (Parte Especial) — PEN-10 (crimes: visão de conjunto, hediondez, ação penal e as leis
# de 2024–2026) e PEN-10.1 (crimes contra a pessoa) (08/11/2026).
from base import I
from pen_juris import J

CP = 'CP:'
HED = 'L8072:1'

# ======================= PEN-10 · Crimes (visão de conjunto) =======================
P = 'DBA26-PEN-10'
I(P, 1, 'Vicaricídio',
  'O vicaricídio, crime autônomo incluído no Código Penal em 2026, consiste em matar descendente, ascendente, dependente, enteado ou pessoa sob guarda da mulher, com o fim de causar-lhe sofrimento, punição ou controle, no contexto de violência doméstica, e é hediondo.', 'C',
  'Art. 121-B (Lei 15.384/2026), pena de 20 a 40 anos, e **hediondo** pelo art. 1º, I-C, da Lei 8.072/1990.',
  lei=[(CP + '121-B', 'Matar descendente, ascendente, dependente, enteado ou pessoa sob guarda ou responsabilidade direta da mulher', 'no contexto de violência doméstica e familiar', 'CP, art. 121-B, caput'),
       (HED, 'I-C – vicaricídio (art. 121-B);', None, 'Lei 8.072/1990, art. 1º, I-C')],
  kw=['vicaricídio', 'Lei 15.384/2026'])
I(P, 1, 'Feminicídio autônomo',
  'Desde a Lei 14.994/2024, o feminicídio segue como qualificadora do homicídio, prevista no inciso VI do § 2º do art. 121 do Código Penal.', 'E',
  'A Lei 14.994/2024 **revogou o inciso VI** e criou o **crime autônomo** do art. 121-A, com pena de 20 a 40 anos.',
  lei=[(CP + '121', 'VI - (Revogado pela Lei nº 14.994, de 2024)', None, 'CP, art. 121, § 2º, VI'),
       (CP + '121-A', 'Art. 121-A. Matar mulher por razões da condição do sexo feminino:', None, 'CP, art. 121-A, caput')],
  peg='Tratar o feminicídio como qualificadora.', kw=['crime autônomo', 'revogou o inciso VI'])
I(P, 1, 'Roubo hediondo',
  'São hediondos o roubo circunstanciado pela restrição de liberdade da vítima, o circunstanciado pelo emprego de arma de fogo e o qualificado pelo resultado lesão corporal grave ou morte.', 'C',
  'Lei 8.072/1990, art. 1º, II, a a c (Lei 13.964/2019). O roubo com **arma branca** (art. 157, § 2º, VII) **não** está no rol.',
  lei=[(HED, 'a) circunstanciado pela restrição de liberdade da vítima (art. 157, § 2º, inciso V);', 'qualificado pelo resultado lesão corporal grave ou morte (art. 157, § 3º);', 'Lei 8.072/1990, art. 1º, II')],
  kw=['hediondos', 'arma branca'])
I(P, 1, 'Furto hediondo',
  'O furto qualificado pelo concurso de duas ou mais pessoas é crime hediondo.', 'E',
  'Só o furto qualificado pelo **emprego de explosivo** ou artefato análogo que cause perigo comum (art. 155, § 4º-A) é hediondo.',
  lei=[(HED, 'IX - furto qualificado pelo emprego de explosivo ou de artefato análogo que cause perigo comum (art. 155, § 4º-A).', None, 'Lei 8.072/1990, art. 1º, IX')],
  peg='Estender a hediondez a qualquer furto qualificado.', kw=['emprego de explosivo'])
I(P, 1, 'Ação penal nos crimes sexuais',
  'Nos crimes contra a liberdade sexual e nos crimes sexuais contra vulnerável, a ação penal é pública condicionada à representação quando a vítima é maior e capaz.', 'E',
  'Desde a Lei 13.718/2018, a ação é **pública incondicionada** em todos os crimes dos Capítulos I e II do Título VI (art. 225).',
  lei=[(CP + '225', 'Nos crimes definidos nos Capítulos I e II deste Título, procede-se mediante ação penal pública incondicionada.', None, 'CP, art. 225, caput')],
  peg='Cobrar a regra anterior a 2018.', kw=['pública incondicionada', 'Lei 13.718/2018'])
# --- PEN-10 · Rodada 2
I(P, 2, 'Marco do crime organizado',
  'Pela Lei 15.358/2026, o homicídio doloso cometido por integrante de organização criminosa ultraviolenta, grupo paramilitar ou milícia privada, no contexto de sua atuação, é punido com reclusão de 20 a 40 anos.', 'C',
  'Art. 121, **§ 2º-D**, incluído pela Lei 15.358/2026 ("marco legal do combate ao crime organizado"), que também criou formas próprias na lesão seguida de morte, no sequestro, no furto, no roubo, na extorsão e na receptação.',
  lei=[(CP + '121', '§ 2º-D. Se o homicídio doloso é cometido por integrante de organização criminosa ultraviolenta', 'Pena - reclusão, de 20 (vinte) a 40 (quarenta anos).', 'CP, art. 121, § 2º-D')],
  kw=['§ 2º-D', 'Lei 15.358/2026'])
I(P, 2, 'Sequestro de menor',
  'O sequestro e cárcere privado cometido contra menor de 18 anos não integra o rol dos crimes hediondos.', 'E',
  'É hediondo desde a **Lei 14.811/2024** (art. 1º, XI, da Lei 8.072/1990), junto com o tráfico de pessoas contra criança ou adolescente (XII).',
  lei=[(HED, 'XI - sequestro e cárcere privado cometido contra menor de 18 (dezoito) anos (art. 148, § 1º, inciso IV);', None, 'Lei 8.072/1990, art. 1º, XI')],
  peg='Ignorar a ampliação de 2024.', kw=['Lei 14.811/2024'])
I(P, 2, 'Furto: nova pena',
  'A Lei 15.397/2026 elevou a pena do furto simples para reclusão de 1 a 6 anos, e multa.', 'C',
  'Art. 155, caput, na redação da **Lei 15.397/2026** (antes, 1 a 4 anos). A mesma lei mexeu no roubo, no estelionato e na receptação.',
  lei=[(CP + '155', 'Pena – reclusão, de 1 (um) a 6 (seis) anos, e multa.', None, 'CP, art. 155, caput (pena)')],
  kw=['Lei 15.397/2026'])

# ======================= PEN-10.1 · Crimes contra a pessoa =======================
P = 'DBA26-PEN-10.1'
I(P, 1, 'Homicídio privilegiado',
  'Para o privilégio da violenta emoção no homicídio, o agente precisa agir dominado por ela, logo após injusta provocação da vítima.', 'C',
  'Art. 121, § 1º: **domínio** (não mera influência, que é atenuante do art. 65, III, c) e **logo em seguida** à injusta provocação.',
  lei=[(CP + '121', '§ 1º Se o agente comete o crime impelido por motivo de relevante valor social ou moral', 'o juiz pode reduzir a pena de um sexto a um terço.', 'CP, art. 121, § 1º')],
  kw=['domínio', 'logo em seguida'])
I(P, 1, 'Pena do feminicídio',
  'O feminicídio é punido com reclusão de 12 a 30 anos, a mesma pena do homicídio qualificado.', 'E',
  'O art. 121-A comina **20 a 40 anos** (Lei 14.994/2024). 12 a 30 é a pena do homicídio qualificado.',
  lei=[(CP + '121-A', 'Pena – reclusão, de 20 (vinte) a 40 (quarenta) anos.', None, 'CP, art. 121-A (pena)')],
  peg='Usar a pena do homicídio qualificado.', kw=['20 a 40 anos'])
I(P, 1, 'Razões da condição do sexo feminino',
  'Há razões da condição do sexo feminino quando o crime envolve violência doméstica e familiar ou menosprezo ou discriminação à condição de mulher.', 'C',
  'Art. 121-A, **§ 1º**, I e II — conceito que os arts. 129, § 13, 141, § 3º, e 147, § 1º, tomam emprestado.',
  lei=[(CP + '121-A', '§ 1º Considera-se que há razões da condição do sexo feminino quando o crime envolve:', 'menosprezo ou discriminação à condição de mulher.', 'CP, art. 121-A, § 1º')],
  kw=['§ 1º', 'violência doméstica e familiar'])
I(P, 1, 'Feminicídio e coautoria',
  'As circunstâncias pessoais elementares do feminicídio não se comunicam ao coautor ou partícipe.', 'E',
  'O art. 121-A, § 3º, manda **comunicar** ao coautor ou partícipe as circunstâncias pessoais elementares do § 1º — coerente com o art. 30 do CP.',
  lei=[(CP + '121-A', '§ 3º Comunicam-se ao coautor ou partícipe as circunstâncias pessoais elementares do crime previstas no § 1º deste artigo.', None, 'CP, art. 121-A, § 3º')],
  peg='Negar a comunicação.', kw=['comunicam-se'])
I(P, 1, 'Perdão judicial no culposo',
  'No homicídio culposo, o juiz pode deixar de aplicar a pena se as consequências da infração atingirem o próprio agente de forma tão grave que a sanção se torne desnecessária.', 'C',
  'Art. 121, § 5º: **perdão judicial** (sentença declaratória, Súmula 18/STJ). Vale também para a lesão culposa (art. 129, § 8º).',
  lei=[(CP + '121', '§ 5º - Na hipótese de homicídio culposo, o juiz poderá deixar de aplicar a pena', 'que a sanção penal se torne desnecessária.', 'CP, art. 121, § 5º')],
  kw=['perdão judicial'])
I(P, 1, 'Infanticídio: tempo',
  'Configura infanticídio matar, sob a influência do estado puerperal, o próprio filho a qualquer tempo depois do parto.', 'E',
  'Art. 123: **durante o parto ou logo após**. Fora desse lapso, homicídio.',
  lei=[(CP + '123', 'Art. 123 - Matar, sob a influência do estado puerperal, o próprio filho, durante o parto ou logo após:', None, 'CP, art. 123')],
  peg='Esticar o elemento temporal.', kw=['durante o parto ou logo após'])
I(P, 1, 'Aborto sentimental',
  'Não se pune o aborto praticado por médico se a gravidez resulta de estupro e o aborto é precedido de consentimento da gestante ou, quando incapaz, de seu representante legal.', 'C',
  'Art. 128, II (aborto **sentimental** ou humanitário). O I é o aborto **necessário**.',
  lei=[(CP + '128', 'II - se a gravidez resulta de estupro e o aborto é precedido de consentimento da gestante', None, 'CP, art. 128, II')],
  kw=['sentimental', 'necessário'])
I(P, 1, 'Anencefalia',
  'A interrupção da gravidez de feto anencéfalo é punida como aborto, nos arts. 124 e 126 do Código Penal, salvo risco de vida para a gestante.', 'E',
  'Na **ADPF 54** (12/04/2012), o STF declarou inconstitucional enquadrar essa interrupção nos arts. 124, 126 e 128, I e II.',
  juris=[J['ADPF54']], peg='Punir a antecipação terapêutica do parto de anencéfalo.', kw=['ADPF 54'])
I(P, 1, 'Lesão grave: 30 dias',
  'A lesão corporal que resulta incapacidade para as ocupações habituais por mais de trinta dias é de natureza grave.', 'C',
  'Art. 129, **§ 1º, I**: reclusão de 1 a 5 anos (prova por exame complementar, CPP, art. 168, § 2º).',
  lei=[(CP + '129', 'I - Incapacidade para as ocupações habituais, por mais de trinta dias;', None, 'CP, art. 129, § 1º, I')],
  kw=['§ 1º, I', 'trinta dias'])
I(P, 1, 'Aborto como resultado',
  'Se da lesão corporal dolosa resulta aborto, a lesão é de natureza grave, com pena de reclusão de um a cinco anos.', 'E',
  'Aborto é resultado da lesão **gravíssima** (§ 2º, V: reclusão de 2 a 8 anos). No § 1º está a **aceleração de parto** (IV).',
  lei=[(CP + '129', '§ 2° Se resulta:', 'V - aborto:', 'CP, art. 129, § 2º, I a V')],
  peg='Trocar aborto por aceleração de parto.', kw=['gravíssima', 'aceleração de parto'])
I(P, 1, 'Lesão na violência doméstica',
  'A ação penal pela lesão corporal leve praticada com violência doméstica contra a mulher depende de representação da ofendida.', 'E',
  '**Súmula 542/STJ**: a ação é **pública incondicionada** (no mesmo sentido, o STF na ADI 4.424). Hoje, a lesão contra a mulher por razões da condição do sexo feminino tem pena de 2 a 5 anos (art. 129, § 13).',
  lei=[(CP + '129', '§ 13. Se a lesão é praticada contra a mulher, por razões da condição do sexo feminino', 'Pena – reclusão, de 2 (dois) a 5 (cinco) anos.', 'CP, art. 129, § 13')],
  juris=[J['S542']], peg='Exigir representação.', kw=['Súmula 542/STJ'])
I(P, 1, 'Calúnia contra os mortos',
  'É punível a calúnia contra os mortos.', 'C',
  'Art. 138, § 2º. Os ofendidos, na prática, são os familiares; não há previsão igual para difamação e injúria.',
  lei=[(CP + '138', '§ 2º - É punível a calúnia contra os mortos.', None, 'CP, art. 138, § 2º')],
  kw=['calúnia contra os mortos'])
# --- PEN-10.1 · Rodada 2
I(P, 2, 'Honra do servidor',
  'Na ofensa à honra de servidor público em razão de suas funções, é concorrente a legitimidade do ofendido, por queixa, e do Ministério Público, mediante representação.', 'C',
  '**Súmula 714/STF**, que conjuga o art. 145, par. ún., do CP com a liberdade do ofendido de oferecer queixa.',
  lei=[(CP + '145', 'Procede-se mediante requisição do Ministro da Justiça, no caso do inciso I do caput do art. 141 deste Código', 'no caso do inciso II do mesmo artigo', 'CP, art. 145, par. ún.')],
  juris=[J['STF714']], kw=['Súmula 714/STF', 'concorrente'])
I(P, 2, 'Honra nas redes sociais',
  'Se o crime contra a honra é cometido ou divulgado em redes sociais, a pena é aumentada de um terço.', 'E',
  'Art. 141, § 2º (Lei 13.964/2019): aplica-se a pena **em triplo**. O aumento de 1/3 é o do caput (ex.: na presença de várias pessoas).',
  lei=[(CP + '141', '§ 2º Se o crime é cometido ou divulgado em quaisquer modalidades das redes sociais da rede mundial de computadores, aplica-se em triplo a pena.', None, 'CP, art. 141, § 2º')],
  peg='Trocar o triplo por 1/3.', kw=['em triplo'])
I(P, 2, 'Ameaça contra a mulher',
  'A ameaça contra a mulher por razões da condição do sexo feminino tem a pena aplicada em dobro e não depende de representação.', 'C',
  'Art. 147, §§ 1º e 2º (Lei 14.994/2024): **pena em dobro**; fora dessa hipótese, a ameaça segue condicionada à representação.',
  lei=[(CP + '147', '§ 1º Se o crime é cometido contra a mulher por razões da condição do sexo feminino', 'exceto na hipótese prevista no § 1º deste artigo.', 'CP, art. 147, §§ 1º e 2º')],
  kw=['pena em dobro'])
I(P, 2, 'Perseguição: ação penal',
  'O crime de perseguição (stalking) é de ação penal pública incondicionada.', 'E',
  'Art. 147-A, § 3º: **somente se procede mediante representação**.',
  lei=[(CP + '147-A', '§ 3º Somente se procede mediante representação.', None, 'CP, art. 147-A, § 3º')],
  peg='Dispensar a representação.', kw=['mediante representação', 'stalking'])
I(P, 2, 'Suicídio de vulnerável',
  'Se o suicídio se consuma e a vítima é menor de 14 anos ou não tem o necessário discernimento, o agente responde por homicídio.', 'C',
  'Art. 122, **§ 7º** (Lei 13.968/2019). Se o resultado é lesão gravíssima, responde pelo art. 129, § 2º (§ 6º).',
  lei=[(CP + '122', '§ 7º Se o crime de que trata o § 2º deste artigo é cometido contra menor de 14 (quatorze) anos', 'responde o agente pelo crime de homicídio, nos termos do art. 121 deste Código.', 'CP, art. 122, § 7º')],
  kw=['§ 7º', 'homicídio'])
I(P, 2, 'Retratação na injúria',
  'A retratação cabal do querelado antes da sentença isenta de pena nos crimes de calúnia, difamação e injúria.', 'E',
  'Art. 143: só **calúnia e difamação** (imputam fatos). Na injúria não há fato a desmentir.',
  lei=[(CP + '143', 'Art. 143 - O querelado que, antes da sentença, se retrata cabalmente da calúnia ou da difamação, fica isento de pena.', None, 'CP, art. 143, caput')],
  peg='Incluir a injúria.', kw=['calúnia e difamação'])
I(P, 2, 'Vítima do vicaricídio',
  'O vicaricídio exige que a vítima morta seja a própria mulher em situação de violência doméstica.', 'E',
  'No art. 121-B, a vítima morta é **outra pessoa** (descendente, ascendente, dependente, enteado ou pessoa sob guarda da mulher); a mulher é a destinatária do **sofrimento, punição ou controle**. Matar a mulher é feminicídio (art. 121-A).',
  lei=[(CP + '121-B', 'Matar descendente, ascendente, dependente, enteado ou pessoa sob guarda ou responsabilidade direta da mulher', 'com o fim específico de causar-lhe sofrimento, punição ou controle', 'CP, art. 121-B, caput')],
  peg='Confundir vicaricídio com feminicídio.', kw=['sofrimento, punição ou controle'])
I(P, 2, 'Injúria qualificada',
  'A injúria que utiliza elementos referentes a religião ou à condição de pessoa idosa ou com deficiência é punida com reclusão de 1 a 3 anos; a injúria racial passou à Lei 7.716/1989.', 'C',
  'Art. 140, § 3º, e Lei 7.716/1989, art. 2º-A, ambos na redação da **Lei 14.532/2023** (injúria racial: reclusão de 2 a 5 anos).',
  lei=[(CP + '140', '§ 3º Se a injúria consiste na utilização de elementos referentes a religião ou à condição de pessoa idosa ou com deficiência:', None, 'CP, art. 140, § 3º'),
       ('L7716:2-A', 'Injuriar alguém, ofendendo-lhe a dignidade ou o decoro, em razão de raça, cor, etnia ou procedência nacional.', None, 'Lei 7.716/1989, art. 2º-A')],
  kw=['Lei 14.532/2023', 'injúria racial'])
