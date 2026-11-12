// Olho de Águia — monta os blocos de 100 assertivas CORRETAS, por ordem de importância (pedido do titular, 12/11/2026).
//
// "Vai de 100 em 100, por essa ordem de importância, em todas as matérias dentro das 100 assertivas":
//   - cada bloco mistura todas as disciplinas, na proporção do PESO de cada uma na prova (revisao/mapa_prioridade.json:
//     questões esperadas por disciplina, estimadas pelos 4 simulados DPC-BA);
//   - dentro de cada disciplina, primeiro o que é mais importante e atual: lei recente (2019+ e, mais ainda, 2023+),
//     núcleo do cargo de Delegado, letra de lei citada, jurisprudência batida (súmula, tese, repetitivo) e incidência AOCP.
// A assertiva aparece sempre na forma CORRETA: a certa como está; a errada pela correção (comentario.correcao.certo).
// A pegadinha: a do próprio item; se não houver e o item era errado, a versão errada original É a pegadinha.
//
// Entrada: discursiva/revisao_nfpss.js e discursiva/pente_fino_*.js  ·  Saída: discursiva/olho_aguia_assertivas.js
// (fora do Git: contém material de revisão de terceiro, D-022).
// Uso: node ferramentas/olho_de_aguia/montar_assertivas.cjs
'use strict';
const fs = require('fs'), path = require('path'), vm = require('vm');
const RAIZ = path.resolve(__dirname, '..', '..'), DISC = path.join(RAIZ, 'discursiva');
const ctx = { window: {} }; vm.createContext(ctx);
const arquivos = fs.readdirSync(DISC).filter(f => /^(pente_fino_[a-z]+|revisao_nfpss)\.js$/.test(f)).sort();
for (const f of arquivos) vm.runInContext(fs.readFileSync(path.join(DISC, f), 'utf8'), ctx, { filename: f });
const W = ctx.window;

// peso de cada disciplina na prova (questões esperadas em 100), do mapa de prioridade
const mapa = JSON.parse(fs.readFileSync(path.join(RAIZ, 'revisao', 'mapa_prioridade.json'), 'utf8'));
const NOME_MAPA = { ADM: 'DIREITO ADMINISTRATIVO', CON: 'DIREITO CONSTITUCIONAL', LEG: 'LEGISLAÇÃO GERAL', CPP: 'DIREITO PROCESSUAL PENAL',
  PEN: 'DIREITO PENAL', CIV: 'DIREITO CIVIL E EMPRESARIAL', LPE: 'LEGISLAÇÃO PENAL E PROCESSUAL PENAL EXTRAVAGANTE', CRI: 'CRIMINOLOGIA',
  MLE: 'MEDICINA LEGAL', IGR: 'PROMOÇÃO DA IGUALDADE RACIAL E DE GÊNERO', INF: 'INFORMÁTICA', AMB: 'DIREITO AMBIENTAL',
  CPC: 'DIREITO PROCESSUAL CIVIL', TRI: 'DIREITO TRIBUTÁRIO' };
const NOME = { ADM: 'Administrativo', CON: 'Constitucional', LEG: 'Legislação Geral', CPP: 'Processo Penal', PEN: 'Penal', CIV: 'Civil',
  LPE: 'Legislação Penal Especial', CRI: 'Criminologia', MLE: 'Medicina Legal', IGR: 'Igualdade Racial e de Gênero', INF: 'Informática',
  AMB: 'Ambiental', CPC: 'Processo Civil', TRI: 'Tributário' };
const peso = {}, incid = {};
for (const it of mapa.itens) { for (const [c, n] of Object.entries(NOME_MAPA)) if (it.disciplina === n) peso[c] = it.peso_disciplina; incid[it.id] = it.incidencia_aocp || 0; }
for (const c of Object.keys(NOME_MAPA)) if (!peso[c]) throw new Error('sem peso no mapa: ' + c);

// núcleo do cargo de Delegado: leis e institutos que sempre caem
const NUCLEO = /inqu[ée]rito|delegad|flagrante|pris[ãa]o (tempor|preventiv|em flagrante)|temporária|cadeia de cust[óo]dia|intercepta[çc]|colabora[çc][ãa]o premiada|organiza[çc][ãa]o criminosa|12\.850|drogas|tr[áa]fico|11\.343|maria da penha|11\.340|viol[êe]ncia dom[ée]stica|feminic[íi]dio|abuso de autoridade|13\.869|tortura|9\.455|hediond|8\.072|arma de fogo|10\.826|desarmamento|lavagem|9\.613|ato infracional|juiz das garantias|acordo de n[ãa]o persecu|busca e apreens|identifica[çc][ãa]o criminal|termo circunstanciado|9\.099|12\.830|anticrime|13\.964|audi[êe]ncia de cust[óo]dia|medidas protetivas|estupro|latroc[íi]nio|roubo|homic[íi]dio/i;
const LEI_RECENTE_23 = /\b(?:Lei(?: Complementar)?|LC)\s*(?:n[ºo°.]*\s*)?1[45]\.\d{3}|\b(?:de|\/)\s*(?:2023|2024|2025|2026)\b|\(Inclu[íi]d[oa] pela.*?(?:2023|2024|2025|2026)\)|\(Reda[çc][ãa]o dada pela.*?(?:2023|2024|2025|2026)\)/i;
const LEI_RECENTE_19 = /\b(?:Lei(?: Complementar)?)\s*(?:n[ºo°.]*\s*)?13\.(?:9[6-9]\d)|\b(?:de|\/)\s*(?:2019|2020|2021|2022)\b|\(Inclu[íi]d[oa] pela.*?(?:2019|2020|2021|2022)\)|\(Reda[çc][ãa]o dada pela.*?(?:2019|2020|2021|2022)\)/i;
const JURIS = /s[úu]mula|tese|tema\s*\d|repetitiv|repercuss[ãa]o geral|STF|STJ|informativo|vinculante/i;

const limpa = s => String(s || '').replace(/\s+/g, ' ').trim();
// pegadinhas geradas para quem não tinha (revisao/material/olho/pegadinhas.json, fora do Git; juntar_pegadinhas.py)
const ARQ_PEG = path.join(RAIZ, 'revisao', 'material', 'olho', 'pegadinhas.json');
const PEG_GERADA = fs.existsSync(ARQ_PEG) ? JSON.parse(fs.readFileSync(ARQ_PEG, 'utf8')) : {};
const itens = [];
for (const [fonte, base] of [['PF', W.PENTE_FINO || {}], ['REV', W.REVISAO || {}]]) {
  for (const [disc, d] of Object.entries(base)) {
    if (!NOME[disc]) { console.warn('disciplina sem peso, ignorada:', fonte, disc); continue; }
    for (const r of d.rodadas || []) for (const i of r.itens || []) {
      const k = i.comentario || {}, errada = i.gabarito === 'E';
      const texto = errada ? limpa(k.correcao && k.correcao.certo) : limpa(i.assertiva);
      if (!texto) continue;
      let peg = limpa(k.pegadinha), pegOrig = false;
      if (!peg && errada) { peg = limpa(i.assertiva); pegOrig = true; }
      let pegGer = false;
      if (!peg && PEG_GERADA[i.id]) { peg = limpa(PEG_GERADA[i.id]); pegGer = true; }
      const leis = (k.lei || []).map(l => limpa(l.rotulo)).filter(Boolean);
      const juris = (k.juris || []).map(j => limpa(typeof j === 'string' ? j : (j.rotulo || j.tribunal || ''))).filter(Boolean);
      const tudo = [i.assertiva, texto, k.resumo, k.regra, k.pegadinha, ...(k.lei || []).map(l => l.rotulo + ' ' + (l.texto || '')), ...(k.juris || []).map(j => JSON.stringify(j))].join(' ');
      const tags = [];
      let s = 0;
      if (LEI_RECENTE_23.test(tudo)) { s += 3; tags.push('atual'); } else if (LEI_RECENTE_19.test(tudo)) { s += 2; tags.push('atual'); }
      if (NUCLEO.test(tudo)) { s += 2; tags.push('delegado'); }
      if (leis.length || /\bart\.\s*\d/i.test(k.resumo || '')) { s += 1; tags.push('lei'); }
      if (juris.length || JURIS.test(k.resumo || '')) { s += 1; tags.push('juris'); }
      if (fonte === 'PF') s += 0.5 + Math.min(2, (incid[i.ponto] || 0) / 2);
      itens.push({ id: i.id, d: disc, f: fonte, t: texto, e: errada ? 1 : 0, p: peg || '', po: pegOrig ? 1 : 0, pg: pegGer ? 1 : 0,
        b: [...leis, ...juris].slice(0, 4), m: limpa(k.memorize), tg: tags, s: Math.round(s * 100) / 100, tm: limpa(i.tema) });
    }
  }
}
// sem repetição de texto (Revisão e Pente Fino às vezes dizem a mesma coisa): fica a de maior escore
const porTexto = new Map();
for (const it of itens) { const c = it.d + '|' + it.t.toLowerCase(); const o = porTexto.get(c); if (!o || it.s > o.s) porTexto.set(c, it); }
const unicos = [...porTexto.values()];

// filas por disciplina, da mais importante para a menos
const filas = {};
for (const it of unicos) (filas[it.d] = filas[it.d] || []).push(it);
const ordemOriginal = new Map(itens.map((it, n) => [it, n]));
for (const f of Object.values(filas)) f.sort((a, b) => b.s - a.s || ordemOriginal.get(a) - ordemOriginal.get(b));

// blocos de 100: cotas por peso (maior resto), só entre as disciplinas que ainda têm itens
const blocos = [];
const pos = Object.fromEntries(Object.keys(filas).map(d => [d, 0]));
const resta = () => Object.keys(filas).filter(d => pos[d] < filas[d].length);
while (resta().length) {
  const ds = resta(), tot = ds.reduce((a, d) => a + peso[d], 0);
  const alvo = Math.min(100, ds.reduce((a, d) => a + filas[d].length - pos[d], 0));
  const cota = Object.fromEntries(ds.map(d => [d, Math.min(filas[d].length - pos[d], Math.floor(alvo * peso[d] / tot))]));
  let falta = alvo - Object.values(cota).reduce((a, b) => a + b, 0);
  const porResto = ds.slice().sort((a, b) => (alvo * peso[b] / tot % 1) - (alvo * peso[a] / tot % 1) || peso[b] - peso[a]);
  while (falta > 0) { let pos0 = false; for (const d of porResto) { if (falta && cota[d] < filas[d].length - pos[d]) { cota[d]++; falta--; pos0 = true; } } if (!pos0) break; }
  const bloco = [];
  for (const d of ds.slice().sort((a, b) => peso[b] - peso[a] || a.localeCompare(b))) { bloco.push(...filas[d].slice(pos[d], pos[d] + cota[d])); pos[d] += cota[d]; }
  blocos.push(bloco);
}

const total = blocos.reduce((a, b) => a + b.length, 0);
const semPeg = unicos.filter(i => !i.p).length;
const saida = {
  gerado_em: new Date().toLocaleString('pt-BR', { timeZone: 'America/Bahia' }),
  criterio: 'Cada bloco de 100 mistura as disciplinas na proporção do peso na prova (mapa de prioridade); dentro da disciplina: lei recente (2023+ vale 3, 2019+ vale 2), núcleo do Delegado (2), letra de lei (1), jurisprudência batida (1), Pente Fino com incidência AOCP do ponto (até 2,5).',
  disciplinas: Object.fromEntries(Object.keys(filas).map(d => [d, { nome: NOME[d], peso: peso[d], itens: filas[d].length }])),
  total, sem_pegadinha: semPeg, blocos
};
const destino = path.join(DISC, 'olho_aguia_assertivas.js');
fs.writeFileSync(destino, '/* GERADO por ferramentas/olho_de_aguia/montar_assertivas.cjs — NÃO edite à mão e NÃO suba ao Git (D-022: contém a Revisão, material de terceiro). */\nwindow.OLHO_ASSERTIVAS=' + JSON.stringify(saida) + ';\n');
console.log(`${total} assertivas únicas (de ${itens.length}) em ${blocos.length} blocos · ${semPeg} sem pegadinha · ${(fs.statSync(destino).size / 1024).toFixed(0)} KB`);
console.log('bloco 1 por disciplina:', Object.entries(blocos[0].reduce((a, i) => (a[i.d] = (a[i.d] || 0) + 1, a), {})).map(([d, n]) => d + ' ' + n).join(' · '));
console.log('bloco 1, com tag atual:', blocos[0].filter(i => i.tg.includes('atual')).length, '· delegado:', blocos[0].filter(i => i.tg.includes('delegado')).length);
