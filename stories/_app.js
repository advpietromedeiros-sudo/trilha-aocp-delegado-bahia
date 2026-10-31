// Utilitários compartilhados pelas stories: o index.html real, lido como texto.
import appHtml from '../index.html?raw';

export { appHtml };

// Renderiza o app inteiro num iframe isolado. Sem o servidor Python, as chamadas /api/*
// falham e o app fica no modo "sem servidor" — o mesmo de abrir o index.html com duplo clique.
// extraCss: CSS de uma proposta, injetado depois do CSS do app — a melhoria vista sem tocar no app.
export function appFrame({ view = 'study', dark = false, palette = '', extraCss = '', width = '100%', height = '900px' } = {}) {
  const wrap = document.createElement('div');
  wrap.style.cssText = 'display:flex;justify-content:center;background:#d9dee5;min-height:100vh;padding:16px 0';
  const frame = document.createElement('iframe');
  frame.title = 'Trilha AOCP — app atual';
  frame.style.cssText = `width:${width};height:${height};border:0;background:#fff;box-shadow:0 4px 24px rgba(0,0,0,.15)`;
  frame.srcdoc = appHtml;
  frame.addEventListener('load', () => {
    const doc = frame.contentDocument;
    if (!doc) return;
    if (dark) doc.body.classList.add('dark');
    if (palette) doc.body.dataset.palette = palette;
    if (extraCss) {
      const st = doc.createElement('style');
      st.dataset.proposta = '';
      st.textContent = extraCss;
      doc.head.appendChild(st);
    }
    if (view !== 'study') doc.getElementById(`tab-${view}`)?.click();
  });
  wrap.appendChild(frame);
  return wrap;
}

// Extrai as variáveis CSS de cada bloco cujo seletor bate com o informado (ex.: ':root').
export function cssVars(selector) {
  const css = [...appHtml.matchAll(/<style[^>]*>([\s\S]*?)<\/style>/g)].map((m) => m[1]).join('\n');
  const vars = {};
  const esc = selector.replace(/[.*+?^${}()|[\]\\]/g, '\\$&');
  for (const bloco of css.matchAll(new RegExp(`(?:^|[}\\s,])${esc}\\s*\\{([^}]*)\\}`, 'g'))) {
    for (const [, nome, valor] of bloco[1].matchAll(/(--[\w-]+)\s*:\s*([^;]+)/g)) vars[nome] = valor.trim();
  }
  return vars;
}

// Razão de contraste WCAG 2.1 entre duas cores #rrggbb (ou #rgb). Devolve null se não for hex.
export function contraste(a, b) {
  const lum = (hex) => {
    let h = hex.replace('#', '');
    if (h.length === 3) h = [...h].map((c) => c + c).join('');
    if (!/^[0-9a-f]{6}$/i.test(h)) return null;
    const [r, g, bl] = [0, 2, 4].map((i) => {
      const c = parseInt(h.slice(i, i + 2), 16) / 255;
      return c <= 0.03928 ? c / 12.92 : ((c + 0.055) / 1.055) ** 2.4;
    });
    return 0.2126 * r + 0.7152 * g + 0.0722 * bl;
  };
  const la = lum(a), lb = lum(b);
  if (la === null || lb === null) return null;
  return (Math.max(la, lb) + 0.05) / (Math.min(la, lb) + 0.05);
}
