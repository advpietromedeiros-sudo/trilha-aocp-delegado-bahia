/* Paleta de grifos — FONTE ÚNICA (10/11/2026, pedido do titular: "sempre que eu apertar G aparece uma paleta de
   grifos... para eu grifar algum texto que eu queira, em todas as telas").
   ⚠️ Não se edita a cópia embutida nas telas: edita-se ESTE arquivo e roda-se
   "python ferramentas/embutir_grifa.py". O portão (--conferir) reprova cópia diferente desta.
   Como funciona:
   - G (sem Ctrl/Alt, fora de campo de texto) abre e fecha a paleta; Esc fecha.
   - Com a paleta aberta e uma cor escolhida, selecionar um texto já o grifa (como caneta marca-texto).
     Com texto já selecionado, clicar na cor grifa na hora.
   - Borracha: clicar num grifo o apaga. "Limpar esta tela" pede confirmação na própria paleta.
   - Os grifos ficam salvos neste navegador, por tela (localStorage "grifos:v1:<caminho>"), ancorados pelo TEXTO
     (o trecho + 32 caracteres de contexto de cada lado), e voltam sozinhos quando a tela se redesenha
     (troca de aba, próxima questão, recarregar a página). Trecho repetido sem o mesmo contexto não é grifado. */
(function () {
  'use strict';
  if (window.Grifa) return;
  var CORES = [
    { id: 'amarelo', nome: 'Amarelo', fundo: '#fff176' },
    { id: 'verde', nome: 'Verde', fundo: '#b9f6ca' },
    { id: 'azul', nome: 'Azul', fundo: '#b3e5fc' },
    { id: 'rosa', nome: 'Rosa', fundo: '#f8bbd0' },
    { id: 'laranja', nome: 'Laranja', fundo: '#ffcc80' }
  ];
  var CTX = 32;
  var CHAVE = 'grifos:v1:' + decodeURIComponent(location.pathname || '/');
  var PULAR = /^(SCRIPT|STYLE|NOSCRIPT|TEXTAREA|INPUT|SELECT|OPTION|TEMPLATE|svg|SVG)$/;
  var ferramenta = 'amarelo';
  var paleta = null, observador = null, agendado = 0, aplicando = false, confirmaLimpar = 0;

  function ler() {
    try { var d = JSON.parse(localStorage.getItem(CHAVE) || '[]'); return Array.isArray(d) ? d : []; }
    catch (e) { return []; }
  }
  function gravar(lista) {
    try { localStorage.setItem(CHAVE, JSON.stringify(lista)); return true; }
    catch (e) { aviso('Não deu para salvar o grifo neste navegador (armazenamento cheio ou bloqueado).'); return false; }
  }

  /* ---------- índice do texto visível da página ---------- */
  function fora(no) {
    for (var el = no.parentNode; el && el !== document.body; el = el.parentNode) {
      if (el.nodeType !== 1) continue;
      if (PULAR.test(el.nodeName) || el.id === 'grf-paleta' || el.isContentEditable) return true;
    }
    return false;
  }
  function indice() {
    var nos = [], inicios = [], partes = [], total = 0;
    if (!document.body) return { nos: nos, inicios: inicios, texto: '' };
    var w = document.createTreeWalker(document.body, NodeFilter.SHOW_TEXT, null);
    for (var n = w.nextNode(); n; n = w.nextNode()) {
      if (!n.nodeValue || fora(n)) continue;
      nos.push(n); inicios.push(total); partes.push(n.nodeValue); total += n.nodeValue.length;
    }
    return { nos: nos, inicios: inicios, texto: partes.join('') };
  }
  function posicao(ix, recipiente, desloc, fim) {
    if (recipiente.nodeType === 3) {
      var i = ix.nos.indexOf(recipiente);
      if (i >= 0) return ix.inicios[i] + desloc;
    }
    /* recipiente é elemento (ou texto fora do índice): procura o primeiro texto do índice depois do ponto */
    var alvo = recipiente.nodeType === 1 ? (recipiente.childNodes[desloc] || null) : recipiente;
    for (var k = 0; k < ix.nos.length; k++) {
      var no = ix.nos[k];
      if (alvo === null) {
        if (!recipiente.contains(no) && (recipiente.compareDocumentPosition(no) & Node.DOCUMENT_POSITION_FOLLOWING)) return ix.inicios[k];
      } else if (alvo === no || alvo.contains(no) || (alvo.compareDocumentPosition(no) & Node.DOCUMENT_POSITION_FOLLOWING)) {
        return ix.inicios[k];
      }
    }
    return fim ? ix.texto.length : -1;
  }

  /* ---------- envolver um intervalo [ini, fim) do índice em <mark> ---------- */
  function envolver(ix, ini, fim, g) {
    var feitos = 0;
    for (var k = ix.nos.length - 1; k >= 0; k--) {
      var no = ix.nos[k], a = ix.inicios[k], b = a + no.nodeValue.length;
      if (b <= ini || a >= fim) continue;
      var s = Math.max(ini, a) - a, e = Math.min(fim, b) - a;
      var pedaco = no.nodeValue.slice(s, e);
      if (!pedaco.trim()) continue; /* espaço entre células de tabela: não se envolve (quebraria a estrutura) */
      var alvo = no;
      if (e < alvo.nodeValue.length) alvo.splitText(e);
      if (s > 0) alvo = alvo.splitText(s);
      var m = document.createElement('mark');
      m.className = 'grf grf-' + g.cor; m.setAttribute('data-grf', g.id); m.title = 'Grifo (' + g.cor + ')';
      alvo.parentNode.insertBefore(m, alvo); m.appendChild(alvo); feitos++;
    }
    return feitos;
  }
  function achar(ix, g) {
    var t = ix.texto, melhor = -1, nota = -1, vistos = 0;
    for (var p = t.indexOf(g.t); p >= 0; p = t.indexOf(g.t, p + 1)) {
      vistos++;
      var antes = t.slice(Math.max(0, p - g.a.length), p), depois = t.slice(p + g.t.length, p + g.t.length + g.d.length);
      var n = (antes === g.a ? 2 : 0) + (depois === g.d ? 2 : 0);
      if (n > nota) { nota = n; melhor = p; }
      if (vistos > 500) break;
    }
    if (melhor < 0) return -1;
    if (vistos > 1 && nota < 2) return -1; /* repetido e sem o contexto: não arrisca grifar o lugar errado */
    return melhor;
  }
  function presente(id) { return !!document.querySelector('mark.grf[data-grf="' + id + '"]'); }

  function aplicar() {
    agendado = 0;
    var lista = ler(), falta = [];
    for (var i = 0; i < lista.length; i++) if (!presente(lista[i].id)) falta.push(lista[i]);
    if (!falta.length) return 0;
    aplicando = true; pausar();
    var n = 0;
    try {
      for (var j = 0; j < falta.length; j++) {
        var ix = indice(), p = achar(ix, falta[j]);
        if (p >= 0 && envolver(ix, p, p + falta[j].t.length, falta[j])) n++;
      }
    } finally { retomar(); aplicando = false; }
    contar();
    return n;
  }
  function agendar() { if (!agendado) agendado = setTimeout(aplicar, 250); }
  function pausar() { if (observador) observador.disconnect(); }
  function retomar() {
    if (!observador && window.MutationObserver) observador = new MutationObserver(function () { if (!aplicando) agendar(); });
    if (observador && document.body) observador.observe(document.body, { childList: true, subtree: true, characterData: true });
  }

  /* ---------- criar e apagar ---------- */
  function grifarSelecao(cor) {
    var sel = window.getSelection && window.getSelection();
    if (!sel || sel.isCollapsed || !sel.rangeCount) return false;
    var r = sel.getRangeAt(0);
    if (paleta && paleta.contains(r.commonAncestorContainer)) return false;
    var ix = indice();
    var ini = posicao(ix, r.startContainer, r.startOffset, false), fim = posicao(ix, r.endContainer, r.endOffset, true);
    if (ini < 0 || fim <= ini) return false;
    var trecho = ix.texto.slice(ini, fim);
    var esq = trecho.length - trecho.replace(/^\s+/, '').length, dir = trecho.length - trecho.replace(/\s+$/, '').length;
    ini += esq; fim -= dir;
    if (fim <= ini) return false;
    var g = { id: 'g' + Date.now().toString(36) + Math.random().toString(36).slice(2, 6), cor: cor,
      t: ix.texto.slice(ini, fim), a: ix.texto.slice(Math.max(0, ini - CTX), ini), d: ix.texto.slice(fim, fim + CTX),
      em: new Date().toISOString() };
    var lista = ler(); lista.push(g);
    if (!gravar(lista)) return false;
    pausar();
    try { envolver(ix, ini, fim, g); } finally { retomar(); }
    sel.removeAllRanges();
    contar();
    return true;
  }
  function desembrulhar(id) {
    pausar();
    try {
      var ms = document.querySelectorAll('mark.grf[data-grf="' + id + '"]');
      for (var i = 0; i < ms.length; i++) {
        var m = ms[i], pai = m.parentNode;
        while (m.firstChild) pai.insertBefore(m.firstChild, m);
        pai.removeChild(m); pai.normalize();
      }
    } finally { retomar(); }
  }
  function apagar(id) {
    gravar(ler().filter(function (g) { return g.id !== id; }));
    desembrulhar(id); contar();
  }
  function limparTela() {
    var lista = ler();
    for (var i = 0; i < lista.length; i++) desembrulhar(lista[i].id);
    gravar([]); contar();
  }

  /* ---------- a paleta ---------- */
  function estilo() {
    if (document.getElementById('grf-estilo')) return;
    var css = '' +
      'mark.grf{color:#111 !important;border-radius:2px;padding:0 1px;-webkit-print-color-adjust:exact;print-color-adjust:exact}' +
      CORES.map(function (c) { return 'mark.grf-' + c.id + '{background:' + c.fundo + ' !important}'; }).join('') +
      'body.grf-borracha mark.grf{cursor:pointer;outline:2px dashed #b71c1c;outline-offset:1px}' +
      '#grf-paleta{position:fixed;right:16px;bottom:16px;z-index:2147483000;background:#fff;color:#1b1b1b;' +
      'border:1px solid #9e9e9e;border-radius:12px;box-shadow:0 6px 24px rgba(0,0,0,.25);padding:10px 12px;' +
      'font:14px/1.35 system-ui,-apple-system,"Segoe UI",Roboto,sans-serif;max-width:calc(100vw - 32px);text-align:left}' +
      '#grf-paleta[hidden]{display:none}' +
      '#grf-paleta .grf-topo{display:flex;align-items:center;justify-content:space-between;gap:12px;margin-bottom:8px}' +
      '#grf-paleta .grf-titulo{font-weight:700}' +
      '#grf-paleta .grf-linha{display:flex;flex-wrap:wrap;gap:6px;align-items:center}' +
      '#grf-paleta button{font:inherit;cursor:pointer;border:1px solid #757575;border-radius:8px;background:#fafafa;color:#1b1b1b;min-height:36px;padding:4px 10px}' +
      '#grf-paleta button:focus-visible{outline:3px solid #0d47a1;outline-offset:2px}' +
      '#grf-paleta .grf-cor{width:36px;padding:0}' +
      '#grf-paleta button[aria-pressed="true"]{border:3px solid #0d47a1;font-weight:700}' +
      '#grf-paleta .grf-dica{margin:8px 0 0;font-size:12.5px;color:#424242;max-width:290px}' +
      '#grf-paleta .grf-limpar[data-confirma="1"]{background:#b71c1c;color:#fff;border-color:#b71c1c}' +
      '@media print{#grf-paleta{display:none !important}}';
    CORES.forEach(function (c) { css += 'body.grf-cor-' + c.id + ' ::selection{background:' + c.fundo + ';color:#111}'; });
    var s = document.createElement('style'); s.id = 'grf-estilo'; s.textContent = css;
    (document.head || document.documentElement).appendChild(s);
  }
  function montar() {
    if (paleta) return paleta;
    estilo();
    paleta = document.createElement('div');
    paleta.id = 'grf-paleta'; paleta.hidden = true;
    paleta.setAttribute('role', 'toolbar'); paleta.setAttribute('aria-label', 'Paleta de grifos');
    var h = '<div class="grf-topo"><span class="grf-titulo">🖍️ Grifos <span class="grf-conta" aria-live="polite"></span></span>' +
      '<button type="button" class="grf-fechar" aria-label="Fechar a paleta (G ou Esc)" title="Fechar (G ou Esc)">✕</button></div>' +
      '<div class="grf-linha">';
    CORES.forEach(function (c) {
      h += '<button type="button" class="grf-cor" data-ferramenta="' + c.id + '" aria-pressed="false" aria-label="Grifar em ' +
        c.nome.toLowerCase() + '" title="' + c.nome + '" style="background:' + c.fundo + '"></button>';
    });
    h += '<button type="button" data-ferramenta="borracha" aria-pressed="false" title="Clique num grifo para apagá-lo">🧽 Borracha</button>' +
      '</div><div class="grf-linha" style="margin-top:6px"><button type="button" class="grf-limpar">Limpar esta tela</button></div>' +
      '<p class="grf-dica">Escolha a cor e selecione o texto: ele fica grifado. Os grifos ficam salvos neste navegador. <b>G</b> abre e fecha.</p>';
    paleta.innerHTML = h;
    paleta.addEventListener('mousedown', function (e) { if (e.target.closest('button')) e.preventDefault(); }); /* não perde a seleção */
    paleta.addEventListener('click', function (e) {
      var b = e.target.closest('button'); if (!b) return;
      if (b.classList.contains('grf-fechar')) return fechar();
      if (b.classList.contains('grf-limpar')) {
        if (!ler().length) return;
        if (b.getAttribute('data-confirma') === '1') { clearTimeout(confirmaLimpar); limparTela(); rotuloLimpar(); return; }
        b.setAttribute('data-confirma', '1'); b.textContent = 'Confirmar: apagar ' + ler().length + ' grifo(s)';
        confirmaLimpar = setTimeout(rotuloLimpar, 4000); return;
      }
      var f = b.getAttribute('data-ferramenta');
      if (f) { escolher(f); if (f !== 'borracha') grifarSelecao(f); }
    });
    document.body.appendChild(paleta);
    escolher(ferramenta);
    return paleta;
  }
  function rotuloLimpar() {
    var b = paleta && paleta.querySelector('.grf-limpar'); if (!b) return;
    b.removeAttribute('data-confirma'); b.textContent = 'Limpar esta tela';
  }
  function escolher(f) {
    ferramenta = f;
    if (!paleta) return;
    var bs = paleta.querySelectorAll('[data-ferramenta]');
    for (var i = 0; i < bs.length; i++) bs[i].setAttribute('aria-pressed', bs[i].getAttribute('data-ferramenta') === f ? 'true' : 'false');
    marcarCorpo();
  }
  function marcarCorpo() {
    var c = document.body.classList, aberta = paleta && !paleta.hidden;
    CORES.forEach(function (x) { c.remove('grf-cor-' + x.id); });
    c.remove('grf-borracha');
    if (!aberta) return;
    if (ferramenta === 'borracha') c.add('grf-borracha'); else c.add('grf-cor-' + ferramenta);
  }
  function contar() {
    if (!paleta) return;
    var lista = ler(), vistos = 0;
    for (var i = 0; i < lista.length; i++) if (presente(lista[i].id)) vistos++;
    var fora = lista.length - vistos;
    paleta.querySelector('.grf-conta').textContent = lista.length
      ? '· ' + lista.length + ' nesta tela' + (fora ? ' (' + fora + ' fora da vista agora)' : '') : '';
  }
  function abrir() { montar().hidden = false; marcarCorpo(); contar(); }
  function fechar() { if (paleta) { paleta.hidden = true; rotuloLimpar(); } marcarCorpo(); }
  function alternar() { if (paleta && !paleta.hidden) fechar(); else abrir(); }
  function aviso(txt) { try { console.warn('[grifos] ' + txt); } catch (e) { /* sem console */ } if (paleta) paleta.querySelector('.grf-dica').textContent = txt; }
  function campo(el) {
    return !!el && (/^(INPUT|TEXTAREA|SELECT)$/.test(el.tagName) || el.isContentEditable);
  }

  /* ---------- eventos ---------- */
  document.addEventListener('keydown', function (e) {
    if (e.ctrlKey || e.metaKey || e.altKey || campo(e.target)) return;
    if (e.key === 'g' || e.key === 'G') { e.preventDefault(); alternar(); return; }
    if (e.key === 'Escape' && paleta && !paleta.hidden) fechar();
  });
  document.addEventListener('mouseup', function (e) {
    if (!paleta || paleta.hidden || ferramenta === 'borracha' || paleta.contains(e.target) || campo(e.target)) return;
    setTimeout(function () { grifarSelecao(ferramenta); }, 0);
  });
  document.addEventListener('click', function (e) {
    if (!paleta || paleta.hidden || ferramenta !== 'borracha') return;
    var m = e.target.closest && e.target.closest('mark.grf[data-grf]');
    if (!m) return;
    e.preventDefault(); e.stopPropagation();
    apagar(m.getAttribute('data-grf'));
  }, true);

  function iniciar() { estilo(); aplicar(); retomar(); }
  if (document.readyState === 'loading') document.addEventListener('DOMContentLoaded', iniciar); else iniciar();

  window.Grifa = { abrir: abrir, fechar: fechar, alternar: alternar, escolher: escolher, grifarSelecao: grifarSelecao,
    aplicar: aplicar, apagar: apagar, limparTela: limparTela, lista: ler, chave: CHAVE, cores: CORES };
})();
