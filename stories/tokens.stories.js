// Paleta lida do próprio index.html — nunca copiada — com o contraste WCAG medido na hora.
import { cssVars, contraste } from './_app.js';

export default { title: 'Aguardando Análise/Tokens atuais' };

function amostras(selector, fundoPadrao) {
  const vars = cssVars(selector);
  const fundo = vars['--surface'] || fundoPadrao;
  const el = document.createElement('div');
  el.style.cssText = 'font:14px system-ui,sans-serif;padding:24px;display:grid;grid-template-columns:repeat(auto-fill,minmax(200px,1fr));gap:12px';
  const cores = Object.entries(vars).filter(([, v]) => /^#[0-9a-f]{3,6}$/i.test(v));
  if (!cores.length) {
    el.textContent = `Nenhuma cor hexadecimal encontrada em "${selector}".`;
    return el;
  }
  for (const [nome, valor] of cores) {
    const r = contraste(valor, fundo);
    const veredito = r === null ? '—' : r >= 4.5 ? 'AA texto' : r >= 3 ? 'AA só texto grande' : 'reprova';
    const card = document.createElement('div');
    card.style.cssText = 'border:1px solid #ccd;border-radius:10px;overflow:hidden;background:#fff;color:#111';
    card.innerHTML = `<div style="height:56px;background:${valor}"></div>
      <div style="padding:8px 10px"><code>${nome}</code><br>${valor}<br>
      <small>contraste sobre ${fundo}: <b>${r ? r.toFixed(2).replace('.', ',') : '—'}</b> (${veredito})</small></div>`;
    el.appendChild(card);
  }
  return el;
}

export const TemaClaro = { name: 'Tema claro (:root)', render: () => amostras(':root', '#ffffff') };
export const TemaEscuro = { name: 'Tema escuro (body.dark)', render: () => amostras('body.dark', '#000000') };
