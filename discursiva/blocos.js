/* blocos.js — transforma os blocos extraídos dos PDFs dos simulados em HTML legível (05/11/2026, pedido do titular).
   O importador marca como "pre" (texto de largura fixa) todo trecho recuado ou com colunas. Medido em 05/11/2026:
   239 blocos "pre", dos quais 150 com colunas e 89 de texto corrido (parágrafos, listas, contas) — esses 89 apareciam
   em letra de máquina, com rolagem lateral e o parágrafo partido ao meio. Aqui cada "pre" vira:
     · tabela HTML, quando há colunas de verdade (2+ espaços entre trechos em 2+ linhas);
     · linhas de fórmula centralizadas, quando há símbolos matemáticos;
     · parágrafos e itens de lista, nos demais casos.
   Depois, parágrafo que começa em minúscula e cujo anterior não terminou a frase é EMENDADO ao anterior (quebra de página
   do PDF). Nada do texto é descartado: só muda a forma. Uso: BLOCOS.html(lista)  ·  BLOCOS.analisar(lista) (para teste). */
(function (raiz) {
  'use strict';
  const esc = s => String(s ?? '').replace(/[&<>"']/g, c => ({ '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;', "'": '&#39;' }[c]));
  const MAT = /[\u{1D400}-\u{1D7FF}∑∫√≤≥≠±∞]/u;
  const ITEM = /^([•●▪◦\-–*]\s|\d{1,2}[.)]\s|[a-z]\)\s|[IVX]{1,4}\s?[-–.)]\s|Passo\s\d|Alternativa\s[A-E]\b|[A-E]\)\s)/;
  const FIM = /[.!?:;]["”')\]]?$/;

  function dedent(x) {
    const ls = String(x).replace(/\t/g, '    ').split('\n');
    const rec = Math.min(...ls.filter(l => l.trim()).map(l => l.match(/^ */)[0].length));
    return ls.map(l => l.slice(Number.isFinite(rec) ? rec : 0).replace(/\s+$/, ''));
  }
  /* trechos de uma linha separados por 2+ espaços, com a coluna onde cada um começa */
  function trechos(l) {
    const out = []; const re = /\S+(?: \S+)*/g; let m;
    while ((m = re.exec(l))) out.push({ i: m.index, x: m[0] });
    return out;
  }
  /* colunas de verdade: 2+ linhas com 2+ trechos, ou bloco de até 2 linhas com 2+ trechos */
  function temColunas(ls) {
    const cheias = ls.filter(l => l.trim()).length, multi = ls.filter(l => trechos(l).length >= 2).length;
    return multi >= 2 || (multi >= 1 && cheias <= 2);
  }

  function tabela(ls) {
    /* colunas: inícios de trecho que se repetem (tolerância de 2), sempre com a coluna 0 */
    const ini = [];
    for (const l of ls) for (const t of trechos(l)) ini.push(t.i);
    const grupos = [];
    for (const i of ini.sort((a, b) => a - b)) { const g = grupos.find(g => Math.abs(g.i - i) <= 2); if (g) g.n++; else grupos.push({ i, n: 1 }); }
    const maxT = Math.max(...ls.map(l => trechos(l).length));
    let cols = grupos.filter(g => g.i === 0 || g.n >= 2 || maxT === grupos.length).map(g => g.i);
    if (!cols.includes(0)) cols.unshift(0);
    cols = [...new Set(cols)].sort((a, b) => a - b);
    const colDe = i => { let k = 0; cols.forEach((c, j) => { if (c <= i + 2) k = j; }); return k; };
    const saida = []; let linhas = [];
    const fecha = () => { if (linhas.length) saida.push({ t: 'tab', linhas }); linhas = []; };
    const cheias = ls.filter(l => l.trim());
    cheias.forEach((l, n) => {
      const ts = trechos(l);
      /* linha corrida (título, frase) que atravessa as colunas: só no começo ou no fim sai da tabela; no meio,
         é uma linha da tabela cujas colunas o PDF juntou com espaço simples — fica na 1ª célula, sem partir a tabela */
      const corrida = ts.length === 1 && ts[0].i === 0 && cols.length > 1 && ts[0].x.length > cols[1] + 8;
      const depois = cheias.slice(n + 1).some(x => trechos(x).length >= 2);
      if (corrida && (!linhas.length || !depois)) { fecha(); saida.push({ t: 'p', x: ts[0].x }); return; }
      if (corrida) { const cel = Array(cols.length).fill(''); cel[0] = ts[0].x; linhas.push(cel); return; }
      const cel = Array(cols.length).fill('');
      for (const t of ts) { const k = colDe(t.i); cel[k] = cel[k] ? cel[k] + ' ' + t.x : t.x; }
      /* coluna 0 vazia = continuação da linha de cima */
      if (!cel[0] && linhas.length) { const ant = linhas[linhas.length - 1]; cel.forEach((c, k) => { if (c) ant[k] = ant[k] ? ant[k] + ' ' + c : c; }); return; }
      linhas.push(cel);
    });
    fecha();
    return saida;
  }

  function formula(ls) {
    return [{ t: 'formula', linhas: ls.filter(l => l.trim()).map(l => l.trim().replace(/ {2,}/g, '  ')) }];
  }

  function prosa(ls) {
    const out = []; let cur = null, recAnt = 0;
    for (const l0 of ls) {
      const l = l0.trim(), rec = l0.length - l0.trimStart().length;
      if (!l) { cur = null; continue; }
      const conta = /=/.test(l) && l.length < 80 && /\d/.test(l);
      /* recuo muito diferente da linha de cima = outro trecho (título centralizado, cálculo recuado) */
      const salto = cur && Math.abs(rec - recAnt) > 8;
      const novo = !cur || salto || ITEM.test(l) || conta || cur.conta || (FIM.test(cur.x) && /^[A-ZÀ-Ý“"(]/.test(l));
      recAnt = rec;
      if (novo) { cur = { t: ITEM.test(l) ? 'item' : conta ? 'conta' : (rec > 20 && l.length < 70 && !/^[a-zà-ý]/.test(l) && !/[.,;:)]$/.test(l) ? 'centro' : 'p'), x: l, conta }; out.push(cur); }
      else cur.x += (/-$/.test(cur.x) && /^[a-zà-ý]/.test(l) ? '' : ' ') + l;
    }
    return out;
  }

  function analisar(lista) {
    const res = [], juntos = [];
    /* blocos "pre" vizinhos são o mesmo trecho que o importador partiu (ex.: tabela em 3 pedaços): junta antes de ler */
    for (const b of lista || []) { const a = juntos[juntos.length - 1]; if (b[0] === 'pre' && a && a[0] === 'pre') a[1] += '\n' + b[1]; else juntos.push([...b]); }
    for (const b of juntos) {
      const [t, x] = b;
      if (t === 'p') { const y = String(x).replace(/\s+/g, ' ').trim(); res.push({ t: ITEM.test(y) ? 'item' : 'p', x: y }); continue; }
      if (t !== 'pre') continue;
      const ls = dedent(x);
      if (MAT.test(x)) res.push(...formula(ls));
      else if (temColunas(ls)) res.push(...tabela(ls));
      else res.push(...prosa(ls));
    }
    /* emenda o parágrafo partido pela quebra de página ou pela mudança de bloco */
    const fim = [];
    for (const r of res) {
      const ant = fim[fim.length - 1];
      if (ant && (r.t === 'p' || r.t === 'item') && (ant.t === 'p' || ant.t === 'item') && /^[a-zà-ý]/.test(r.x) && !FIM.test(ant.x)) { ant.x += ' ' + r.x; continue; }
      fim.push({ ...r });
    }
    return fim;
  }

  function html(lista) {
    return analisar(lista).map(r => {
      if (r.t === 'p') return `<p>${esc(r.x)}</p>`;
      if (r.t === 'item') return `<p class="bl-item">${esc(r.x)}</p>`;
      if (r.t === 'centro') return `<p class="bl-centro">${esc(r.x)}</p>`;
      if (r.t === 'conta') return `<p class="bl-conta">${esc(r.x)}</p>`;
      if (r.t === 'formula') return `<div class="bl-formula">${r.linhas.map(l => `<div>${esc(l)}</div>`).join('')}</div>`;
      if (r.t === 'tab') {
        const cab = r.linhas.length > 1 && r.linhas[0].every(c => c.length <= 60);
        const tr = (c, tag) => `<tr>${c.map(x => `<${tag}>${esc(x)}</${tag}>`).join('')}</tr>`;
        return `<div class="bl-tab"><table>${cab ? `<thead>${tr(r.linhas[0], 'th')}</thead>` : ''}<tbody>${r.linhas.slice(cab ? 1 : 0).map(c => tr(c, 'td')).join('')}</tbody></table></div>`;
      }
      return '';
    }).join('');
  }

  const API = { html, analisar };
  if (typeof module !== 'undefined' && module.exports) module.exports = API; else raiz.BLOCOS = API;
})(typeof window !== 'undefined' ? window : globalThis);
