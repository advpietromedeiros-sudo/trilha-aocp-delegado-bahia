/* blocos.js — transforma os blocos extraídos dos PDFs dos simulados em HTML legível (05/11/2026, pedido do titular).
   O importador marca como "pre" (texto de largura fixa) todo trecho recuado ou com colunas. Medido em 05/11/2026:
   239 blocos "pre", dos quais 150 com colunas e 89 de texto corrido (parágrafos, listas, contas) — esses 89 apareciam
   em letra de máquina, com rolagem lateral e o parágrafo partido ao meio. Aqui cada "pre" vira:
     · tabela HTML, quando há colunas de verdade (2+ espaços entre trechos em 2+ linhas);
     · linhas de fórmula centralizadas, quando há símbolos matemáticos;
     · parágrafos e itens de lista, nos demais casos.
   Depois, parágrafo que começa em minúscula e cujo anterior não terminou a frase é EMENDADO ao anterior (quebra de página
   do PDF). Nada do texto é descartado: só muda a forma. Uso: BLOCOS.html(lista[, { destacar: true }])  ·  BLOCOS.analisar(lista) (para teste).
   07/11/2026: BLOCOS.comentario(lista, { gab }) põe o comentário em QUADROS (porquê, lei, jurisprudência, atenção,
   alternativas), com a oração de exceção em vermelho e as palavras-chave em negrito; BLOCOS.marcado(texto) faz o mesmo
   num texto solto com **negrito** (Pente Fino). */
(function (raiz) {
  'use strict';
  const esc = s => String(s ?? '').replace(/[&<>"']/g, c => ({ '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;', "'": '&#39;' }[c]));
  const MAT = /[\u{1D400}-\u{1D7FF}∑∫√≤≥≠±∞]/u;
  const ITEM = /^([•●▪◦\-–*]\s|\d{1,2}[.)]\s|[a-z]\)\s|[IVX]{1,4}\s?[-–.)]\s|Passo\s\d|Alternativa\s[A-E]\b|[A-E]\)\s)/;
  const FIM = /[.!?:;]["”')\]]?$/;
  const EXCECOES = ['à exceção de', 'com exceção de', 'a não ser que', 'a menos que', 'desde que',
    'não se aplica', 'não incide', 'não cabe',
    'não autoriza', 'não constitui', 'não configura', 'não se confunde', 'não é obrigatório',
    'não impede', 'não podem', 'não pode', 'ressalvados', 'ressalvadas', 'ressalvado', 'ressalvada',
    'exclusivamente', 'incorretas', 'incorreta', 'dispensado', 'dispensada', 'proibida', 'proibido',
    'vedada', 'vedado', 'exceções', 'exceção', 'erradas', 'errada', 'falsas', 'falsa', 'somente',
    'apenas', 'exceto', 'salvo'];
  const CHAVES = ['reserva de jurisdição', 'concurso de pessoas', 'concurso material', 'concurso formal',
    'prisão preventiva', 'prova ilícita', 'ação penal', 'competências', 'competência', 'requisitos',
    'requisito', 'fundamentos', 'fundamento', 'qualificadoras', 'qualificadora', 'majorantes',
    'majorante', 'minorantes', 'minorante', 'prescrição', 'decadência', 'representação',
    'responsabilidade penal', 'excludente de ilicitude', 'legítima defesa', 'estado de necessidade',
    'consumado', 'tentativa', 'flagrante', 'prazos', 'prazo', 'tipicidade', 'necessária',
    'necessário', 'obrigatória', 'obrigatório', 'deverão', 'deverá', 'devem', 'deve',
    'exigem', 'exige', 'dolo', 'culpa'];
  const alternancia = termos => termos.slice().sort((a, b) => b.length - a.length)
    .map(x => x.replace(/[.*+?^${}()|[\]\\]/g, '\\$&')).join('|');
  const PADRAO_DESTAQUE = new RegExp(`(^|[^\\p{L}\\p{N}_])(${alternancia([...EXCECOES, ...CHAVES])})(?=$|[^\\p{L}\\p{N}_])`, 'giu');
  const PADRAO_EXCECAO = new RegExp(`^(?:${alternancia(EXCECOES)})$`, 'i');

  function textoHTML(valor, destacar) {
    const texto = String(valor ?? '');
    if (!destacar) return esc(texto);
    let html = '', cursor = 0, m;
    PADRAO_DESTAQUE.lastIndex = 0;
    while ((m = PADRAO_DESTAQUE.exec(texto))) {
      const inicio = m.index + m[1].length;
      html += esc(texto.slice(cursor, inicio));
      const classe = PADRAO_EXCECAO.test(m[2]) ? 'destaque-excecao' : 'destaque-chave';
      html += `<strong class="${classe}">${esc(m[2])}</strong>`;
      cursor = inicio + m[2].length;
    }
    return html + esc(texto.slice(cursor));
  }

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

  /* um item do analisar() em HTML; fmt formata cada trecho de texto (já escapando) */
  function itemHTML(r, fmt) {
    if (r.t === 'p') return `<p>${fmt(r.x)}</p>`;
    if (r.t === 'item') return `<p class="bl-item">${fmt(r.x)}</p>`;
    if (r.t === 'centro') return `<p class="bl-centro">${fmt(r.x)}</p>`;
    if (r.t === 'conta') return `<p class="bl-conta">${fmt(r.x)}</p>`;
    if (r.t === 'formula') return `<div class="bl-formula">${r.linhas.map(l => `<div>${fmt(l)}</div>`).join('')}</div>`;
    if (r.t === 'tab') {
      const cab = r.linhas.length > 1 && r.linhas[0].every(c => c.length <= 60);
      const tr = (c, tag) => `<tr>${c.map(x => `<${tag}>${fmt(x)}</${tag}>`).join('')}</tr>`;
      return `<div class="bl-tab"><table>${cab ? `<thead>${tr(r.linhas[0], 'th')}</thead>` : ''}<tbody>${r.linhas.slice(cab ? 1 : 0).map(c => tr(c, 'td')).join('')}</tbody></table></div>`;
    }
    return '';
  }

  function html(lista, opcoes = {}) {
    const destacar = Boolean(opcoes && opcoes.destacar);
    return analisar(lista).map(r => itemHTML(r, x => textoHTML(x, destacar))).join('');
  }

  /* ================= comentário em QUADROS (07/11/2026, pedido do titular) =================
     "Deixe as exceções em vermelho... faça quadros... bote as palavras chaves em negrito."
     Só muda a APRESENTAÇÃO: todo caractere do comentário continua na tela, na ordem. O que a tela ACRESCENTA (rótulo
     de quadro, selo "gabarito", resumo das exceções) vai entre <!--g--> e <!--/g-->, para o teste saber separar. */
  const L = '(?<![\\p{L}\\p{N}])', R = '(?![\\p{L}\\p{N}])';
  const NUM_EXT = 'cento e oitenta|cento e vinte|quarenta e oito|vinte e quatro|setenta e duas|noventa|sessenta|quarenta|trinta|vinte|quinze|doze|onze|dez|nove|oito|sete|seis|cinco|quatro|três|duas|dois|uma|um';
  const CHAVE_PARTES = [
    /* prazo: "15 dias", "10 (dez) dias", "48 horas", "cinco anos", "2 dias úteis" */
    `(?:\\d+(?:[.,]\\d+)?|${NUM_EXT})\\s*(?:\\([^()]{1,25}\\)\\s*)?(?:dias|dia|horas|hora|meses|mês|anos|ano|minutos|semanas|semana)(?:\\s+(?:úteis|corridos))?`,
    /* fração e percentual: "1/3", "dois terços", "metade", "30%", "10 por cento" */
    `(?<![\\d.,/])\\d{1,2}\\/\\d{1,2}(?![\\d/])`,
    `(?:um|dois|três|quatro)\\s+(?:terços|terço|quartos|quarto|quintos|quinto|sextos|sexto|oitavos|oitavo)`,
    `metade|dobro|triplo`, `\\d+(?:[.,]\\d+)?\\s*%`, `\\d+(?:[.,]\\d+)?\\s+por\\s+cento`,
    /* artigo: "art. 5º, § 2º", "arts. 312 e 313", "artigo 10", "§ 1º", "parágrafo único" */
    `(?:arts?\\.|artigos?)\\s*\\d+[º°o]?(?:-[A-Z])?(?:(?:\\s*,\\s*|\\s+e\\s+)(?:§{1,2}\\s*\\d+[º°o]?|incisos?\\s+[IVXLC]+|inc\\.\\s*[IVXLC]+|[IVXLC]+(?![\\p{L}])|caput|parágrafo único|\\d+[º°o]?(?:-[A-Z])?(?![\\p{L}\\p{N}/])))*`,
    `§{1,2}\\s*\\d+[º°o]?`, `parágrafo único`,
    /* número de lei: "Lei nº 13.105/2015", "LC 64/90", "Decreto-Lei 3.689", "EC 45" */
    `(?:Lei Complementar|Lei|LC|Decreto-Lei|Decreto|Emenda Constitucional|EC|Medida Provisória)(?:\\s+(?:Estadual|Federal|Municipal|Orgânica))?\\s*(?:n[º°o.]\\s*)?\\d+(?:\\.\\d+)*(?:\\/\\d{2,4})?`,
    /* jurisprudência: súmula, tema, informativo, classe processual com número, STF/STJ */
    `Súmulas?(?:\\s+Vinculantes?)?\\s*(?:n[º°.]\\s*)?\\d+(?:\\s+d[oa]\\s+(?:STF|STJ|TST|TSE))?`,
    `Tema\\s*(?:n[º°.]\\s*)?\\d+(?:\\.\\d+)*`, `Informativo\\s*(?:n[º°.]\\s*)?\\d+`,
    `(?:REsp|AREsp|EREsp|RE|ARE|HC|RHC|ADI|ADIs|ADC|ADO|ADPF|AgRg|MS|RMS|Rcl)\\s*(?:n[º°.]\\s*)?\\d+(?:\\.\\d+)*`, `STF|STJ`,
    /* comando da norma e quem age */
    `poderá|poderão|deverá|deverão|é obrigatória|é obrigatório|obrigatoriamente|é facultado|é facultada|facultativa|facultativo`,
    `legitimados|legitimadas|legitimado|legitimada|legitimidade|Ministério Público|Defensoria Pública|autoridade policial|Delegada de Polícia|Delegado de Polícia|querelante|ofendido`,
    `competências|competência|competente|compete`
  ];
  const RX_CHAVE = new RegExp(`${L}(?:${CHAVE_PARTES.join('|')})${R}`, 'giu');
  /* exceção e limite: o GATILHO abre a oração, que vai até a pontuação (vírgula, ponto, parêntese, aspas) */
  const GATILHOS = ['à exceção do', 'à exceção da', 'à exceção de', 'com exceção do', 'com exceção da', 'com exceção de',
    'a não ser que', 'a menos que', 'não se aplicam', 'não se aplica', 'não se admite', 'não incide', 'não cabe',
    'não admite', 'não poderão', 'não poderá', 'não podem', 'não pode', 'é vedada', 'é vedado', 'é proibida', 'é proibido',
    'vedadas', 'vedados', 'vedada', 'vedado', 'proibidas', 'proibidos', 'proibida', 'proibido',
    'ressalvadas', 'ressalvados', 'ressalvada', 'ressalvado', 'excetuadas', 'excetuados', 'excetuada', 'excetuado',
    'independentemente', 'exclusivamente', 'tão somente', 'somente', 'apenas', 'exceto', 'salvo', 'desde que',
    'inadmissível', 'jamais', 'nunca'];
  /* os gatilhos FORTES entram também no resumo "Não esqueça as exceções" (apenas/somente/desde que ficam só em vermelho) */
  const FORTES = /^(?:à exceção|com exceção|a não ser|a menos|não se aplica|não incide|não cabe|é vedad|vedad|é proibid|proibid|ressalvad|excetuad|independentemente|exceto|salvo)/i;
  const RX_EXC = new RegExp(`${L}(${alternancia(GATILHOS)})${R}`, 'giu');
  const LIMITE_ORACAO = 64; /* a oração, não a frase inteira */
  function fimOracao(t, i) {
    const max = Math.min(t.length, i + LIMITE_ORACAO);
    for (let j = i; j < max; j++) {
      const c = t[j];
      if (',;:!?()[]“”"'.includes(c)) return j;
      if ((c === '–' || c === '—') && t[j - 1] === ' ') return j - 1;
      /* ponto final de frase (não o de "art." ou "nº"): seguido de fim, ou de espaço e maiúscula/aspas */
      if (c === '.' && (j + 1 >= t.length || (/\s/.test(t[j + 1]) && /[A-ZÀ-Ý“"(]/.test(t[j + 2] || '')))) return j;
    }
    if (max >= t.length) return t.length;
    const sp = t.lastIndexOf(' ', max);
    return sp > i ? sp : max;
  }
  /* faixas [início, fim, fimDoGatilho] das orações de exceção */
  function faixasExcecao(t) {
    const out = []; let m;
    RX_EXC.lastIndex = 0;
    while ((m = RX_EXC.exec(t))) {
      const ini = m.index, fg = ini + m[1].length;
      let fim = fimOracao(t, fg);
      while (fim > fg && /\s/.test(t[fim - 1])) fim--;
      out.push([ini, fim, fg]);
      RX_EXC.lastIndex = Math.max(fim, fg);
    }
    return out;
  }
  function faixasChave(t) {
    const out = []; let m;
    RX_CHAVE.lastIndex = 0;
    while ((m = RX_CHAVE.exec(t))) { if (!m[0].length) { RX_CHAVE.lastIndex++; continue; } out.push([m.index, m.index + m[0].length]); }
    return out;
  }
  /* texto → HTML escapado, com palavras-chave em <strong class="cm-chave"> e a oração de exceção em <span class="cm-exc"> */
  function realcar(valor) {
    const t = String(valor ?? ''), chv = faixasChave(t);
    /* a oração não corta uma palavra-chave ao meio ("exceto nos casos do art. 129, I"): vai até o fim dela */
    const exc = faixasExcecao(t).map(([i, f, fg]) => { const k = chv.find(([a, b]) => a < f && f < b); return [i, k ? k[1] : f, fg]; });
    const comChaves = (a, b) => {
      let h = '', p = a;
      for (const [i, f] of chv) {
        if (f <= p || i >= b) continue;
        const i2 = Math.max(i, p), f2 = Math.min(f, b);
        h += esc(t.slice(p, i2)) + `<strong class="cm-chave">${esc(t.slice(i2, f2))}</strong>`; p = f2;
      }
      return h + esc(t.slice(p, b));
    };
    let h = '', pos = 0;
    for (const [i, f, fg] of exc) {
      h += comChaves(pos, i) + `<span class="cm-exc"><strong>${esc(t.slice(i, fg))}</strong>${comChaves(fg, f)}</span>`;
      pos = f;
    }
    return h + comChaves(pos, t.length);
  }
  /* texto com **negrito** (markdown simples do Pente Fino) → HTML com os mesmos realces */
  function marcado(valor) {
    return String(valor ?? '').split(/\*\*([^*]+)\*\*/).map((x, i) => i % 2 ? `<strong class="cm-chave">${esc(x)}</strong>` : realcar(x)).join('');
  }
  /* orações de exceção FORTES de um texto, para o quadro-resumo */
  function excecoesFortes(t) {
    return faixasExcecao(t).filter(([i, , fg]) => FORTES.test(t.slice(i, fg))).map(([i, f]) => t.slice(i, f).trim()).filter(x => x.length > 6);
  }

  /* cabeçalho de alternativa ("A – Correta.", "b) Errada.", "Alternativa C:") ou de assertiva ("1ª Assertiva (Correta)", "II – Incorreta") */
  const VEREDITO = '\\(?(?:incorret[ao]s?|corret[ao]s?|cert[ao]s?|errad[ao]s?|fals[ao]s?|verdadeir[ao]s?)\\)?';
  const RX_ALT = new RegExp(`^(\\s*(?:[-–•]\\s*)?)((?:(?:Alternativa|Letra)\\s+)?\\(?[A-Ea-e])(\\)\\s*|\\s*[-–—:]\\s*|\\.\\s+|\\s+(?=\\p{Lu}))(?:(${VEREDITO})(?![\\p{L}])(\\s*[.:;!–—-]?\\s*))?`, 'iu');
  const RX_ASSERT = new RegExp(`^(\\s*(?:[-–•]\\s*)?)(\\d+\\s*ª\\s+Assertiva|Assertiva\\s+(?:[IVX]+|\\d+)|Item\\s+(?:[IVX]+|\\d+)|[IVX]{1,4})(\\s*[-–—:.)]?\\s*)(${VEREDITO})(?![\\p{L}])(\\s*[.:;!–—-]?\\s*)`, 'iu');
  function cabecalho(tx) {
    let m = RX_ASSERT.exec(tx);
    if (m) return { tipo: 'assert', lead: m[1], rot: m[2], sep: m[3], ver: m[4], sep2: m[5], resto: tx.slice(m[0].length), letra: '' };
    m = RX_ALT.exec(tx);
    if (!m) return null;
    /* com /iu, \p{Lu} também casa minúscula: confere a maiúscula depois do espaço aqui */
    if (/^\s+$/.test(m[3]) && !/^[A-ZÀ-Ý“"]/.test(tx.slice(m[1].length + m[2].length + m[3].length))) return null;
    const letra = m[2].replace(/[^A-Ea-e]/g, '').slice(-1);
    return { tipo: 'alt', lead: m[1], rot: m[2], sep: m[3], ver: m[4] || '', sep2: m[5] || '', resto: tx.slice(m[0].length), letra: letra.toUpperCase(), maiuscula: letra === letra.toUpperCase(), fraco: /^\s+$/.test(m[3]) };
  }
  const RX_ATENCAO = /^\s*(?:[-–•]\s*)?(?:atenção|cuidado|observação|obs\.|importante|exceções|exceção|ressalva|pegadinha|dica)(?![\p{L}])/iu;
  const RX_JURIS = /(?<![\p{L}])(?:STF|STJ|Súmulas?|Tema\s+(?:n[º°.]\s*)?\d|Informativo|REsp|AREsp|RE\s+\d|HC\s+\d|RHC|ADIs?\s+\d|ADC\s+\d|ADPF|ARE\s+\d|AgRg|Plenário|Supremo Tribunal|Superior Tribunal|jurisprudência|repercussão geral|recursos? repetitivos?|precedentes?)(?![\p{L}])/u;
  const RX_LEI = /^\s*(?:[“"]|Art\.\s*\d|§|Parágrafo único)|^\s*(?:Conforme|Segundo|Nos termos d[oa]s?|De acordo com|Consoante|À luz d[oa]|O art\.|A Lei|O Código|A Constituição)[^.]{0,90}?(?:art(?:igo)?s?\.?\s*\d|Lei|Código|Constituição|CF|CPP|CPC|CP|CDC|ECA)(?![\p{L}])|“\s*Art\.\s*\d/iu;
  const funcao = tx => RX_ATENCAO.test(tx) ? 'atencao' : RX_JURIS.test(tx) ? 'juris' : RX_LEI.test(tx) ? 'lei' : 'porque';
  const ROTULO = { porque: '💡 Gabarito e porquê', lei: '📖 Fundamento legal', juris: '⚖️ Jurisprudência', atencao: '⚠️ Atenção · exceção', alts: '🔎 Análise das alternativas' };
  const gerado = h => `<!--g-->${h}<!--/g-->`;
  /* conta e fórmula ficam sem realce: vermelho e negrito atrapalhariam a leitura do cálculo */
  const fmtDe = r => (r.t === 'formula' || r.t === 'conta') ? esc : realcar;
  const textoDe = r => r.t === 'tab' ? r.linhas.flat().join(' ') : r.t === 'formula' ? r.linhas.join(' ') : r.x;

  /* quadros: lista dos blocos do PDF → grupos { tipo, itens } (porque, lei, juris, atencao, alt) */
  function quadros(lista) {
    const rs = analisar(lista);
    const cabs = rs.map(r => (r.t === 'p' || r.t === 'item') ? cabecalho(r.x) : null);
    /* alternativa sem a palavra "correta/errada" só conta se o comentário tiver 3+ letras maiúsculas distintas assim
       (evita tomar a alínea "a)" de uma lei citada por análise de alternativa) */
    const semVer = new Set(cabs.filter(c => c && c.tipo === 'alt' && !c.ver && !c.fraco).map(c => c.letra));
    /* "B Os Estados..." (letra e espaço, como na tabela do PDF): só com 4+ letras assim, entre elas B e D */
    const fracas = new Set(cabs.filter(c => c && c.tipo === 'alt' && c.fraco && c.maiuscula).map(c => c.letra));
    const fracoOk = fracas.size >= 4 && fracas.has('B') && fracas.has('D');
    const grupos = []; let alt = null;
    rs.forEach((r, k) => {
      const c = cabs[k], valido = c && (c.tipo === 'assert' || (c.fraco ? c.maiuscula && fracoOk : c.ver || semVer.size >= 4 || (c.maiuscula && semVer.size >= 3)));
      if (valido) { alt = { tipo: 'alt', cab: c, itens: [r] }; grupos.push(alt); return; }
      if (alt) { alt.itens.push(r); return; }
      const ult = grupos[grupos.length - 1];
      const tipo = (r.t === 'tab' || r.t === 'formula') && ult ? ult.tipo : funcao(textoDe(r));
      if (ult && ult.tipo === tipo) ult.itens.push(r); else grupos.push({ tipo, itens: [r] });
    });
    return grupos;
  }
  const RX_VER_OK = /^\(?(?:corret|cert|verdadeir)/i;
  function altHTML(g, gab) {
    const c = g.cab, primeiro = g.itens[0], ok = c.ver ? RX_VER_OK.test(c.ver) : null;
    const eGab = c.tipo === 'alt' && gab ? c.letra === gab : (c.tipo === 'alt' && !gab && ok === true);
    const classe = `cm-alt${eGab ? ' cm-alt-gab' : ''}${c.tipo === 'assert' ? ' cm-assert' : ''}${ok === true ? ' cm-ok' : ok === false ? ' cm-no' : ''}`;
    const cab = `<span class="cm-sep">${esc(c.lead)}</span><span class="cm-letra">${esc(c.rot)}</span><span class="cm-sep">${esc(c.sep)}</span>`
      + (c.ver ? `<span class="cm-ver ${ok ? 'cm-ver-ok' : 'cm-ver-no'}">${esc(c.ver)}</span><span class="cm-sep">${esc(c.sep2)}</span>` : '')
      + (eGab ? gerado('<span class="cm-gab">✔ gabarito</span>') : '');
    const corpo1 = c.resto ? itemHTML({ ...primeiro, x: c.resto }, fmtDe(primeiro)) : '';
    return `<div class="${classe}"><div class="cm-alt-cab">${cab}</div><div class="cm-alt-corpo">${corpo1}${g.itens.slice(1).map(r => itemHTML(r, fmtDe(r))).join('')}</div></div>`;
  }
  /* comentário inteiro em quadros. opcoes.gab = letra do gabarito (pinta a alternativa certa de verde) */
  function comentario(lista, opcoes = {}) {
    const gab = String((opcoes && opcoes.gab) || '').toUpperCase().slice(0, 1);
    const grupos = quadros(lista), out = [];
    let alts = [];
    const fechaAlts = () => { if (alts.length) out.push(`<section class="cm-q cm-alts">${gerado(`<header class="cm-rot">${ROTULO.alts}</header>`)}${alts.join('')}</section>`); alts = []; };
    let porqueVisto = false;
    for (const g of grupos) {
      if (g.tipo === 'alt') { alts.push(altHTML(g, gab)); continue; }
      fechaAlts();
      const rot = g.tipo === 'porque' && porqueVisto ? '💡 Por quê' : ROTULO[g.tipo];
      if (g.tipo === 'porque') porqueVisto = true;
      out.push(`<section class="cm-q cm-${g.tipo}">${gerado(`<header class="cm-rot">${rot}</header>`)}${g.itens.map(r => itemHTML(r, fmtDe(r))).join('')}</section>`);
    }
    fechaAlts();
    /* resumo das exceções fortes (cópia, marcada como gerada), quando o comentário não tem quadro de Atenção próprio */
    if (!grupos.some(g => g.tipo === 'atencao')) {
      const todas = [...new Set(grupos.flatMap(g => g.itens.flatMap(r => excecoesFortes(textoDe(r)))))].slice(0, 5);
      if (todas.length) out.push(gerado(`<section class="cm-q cm-resumo-exc"><header class="cm-rot">⛔ Não esqueça as exceções</header><ul>${todas.map(x => `<li><span class="cm-exc">${esc(x)}</span></li>`).join('')}</ul></section>`));
    }
    return `<div class="cm">${out.join('')}</div>`;
  }

  const API = { html, analisar, comentario, quadros, realcar, marcado, excecoesFortes };
  if (typeof module !== 'undefined' && module.exports) module.exports = API; else raiz.BLOCOS = API;
})(typeof window !== 'undefined' ? window : globalThis);
