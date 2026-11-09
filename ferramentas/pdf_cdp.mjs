// Imprime um HTML em PDF pelo Chrome/Edge headless via CDP (sem dependências: fetch e WebSocket do Node).
// Chamado por ferramentas/gerar_revisao.py (gerar_pdf). Nasceu em 07/11/2026: o --print-to-pdf da linha de
// comando terminava com rc=0 SEM gravar o PDF de um módulo de 316 páginas (memória). Aqui a impressão sai em
// partes (Page.printToPDF com pageRanges, transferMode ReturnAsStream, lido em pedaços de 4 MB) e o gerador
// junta as partes com o PyMuPDF.
// Uso: node ferramentas/pdf_cdp.mjs ENTRADA.html PREFIXO [PASSO=40]
//   grava PREFIXO.parte01.pdf, PREFIXO.parte02.pdf… e imprime "PARTES n PAGINAS_ULTIMA_FAIXA".
//   Sai 0 se gravou ao menos uma parte; 1 se não gravou nenhuma (nunca verde em silêncio).
import { spawn } from 'node:child_process';
import { writeFileSync, existsSync, mkdtempSync, rmSync } from 'node:fs';
import { pathToFileURL } from 'node:url';
import { tmpdir } from 'node:os';
import { join, resolve } from 'node:path';

const [ent, pre, passoArg] = process.argv.slice(2);
if (!ent || !pre) { console.log('uso: node ferramentas/pdf_cdp.mjs ENTRADA.html PREFIXO [PASSO]'); process.exit(2); }
const ENT = resolve(ent), PRE = resolve(pre), PASSO = Math.max(1, parseInt(passoArg || '40', 10));
const NAV = ['C:/Program Files (x86)/Microsoft/Edge/Application/msedge.exe', 'C:/Program Files/Google/Chrome/Application/chrome.exe', 'C:/Program Files/Microsoft/Edge/Application/msedge.exe'].find(existsSync);
if (!NAV) { console.log('FALHA: nem Edge nem Chrome encontrados'); process.exit(1); }
const perfil = mkdtempSync(join(tmpdir(), 'revisao-pdf-'));  // --user-data-dir próprio: não disputa com o navegador do titular
const porta = 9500 + Math.floor(Math.random() * 400);
const nav = spawn(NAV, ['--headless=new', '--disable-gpu', '--no-first-run', '--no-default-browser-check', '--disable-extensions',
  `--remote-debugging-port=${porta}`, `--user-data-dir=${perfil}`, 'about:blank'], { stdio: 'ignore' });
const espera = ms => new Promise(r => setTimeout(r, ms));
let ws;
const fim = async code => {
  try { ws?.close(); } catch { }
  try { nav.kill(); } catch { }
  await espera(1500);
  try { rmSync(perfil, { recursive: true, force: true }); } catch { }
  process.exit(code);
};
const prazo = setTimeout(() => { console.log('FALHA: tempo esgotado (15 min)'); fim(1); }, 15 * 60 * 1000);

let alvo;
for (let i = 0; i < 120 && !alvo; i++) { await espera(250); try { alvo = (await (await fetch(`http://127.0.0.1:${porta}/json`)).json()).find(t => t.type === 'page'); } catch { } }
if (!alvo) { console.log('FALHA: o navegador não respondeu'); await fim(1); }
ws = new WebSocket(alvo.webSocketDebuggerUrl); await new Promise(r => ws.addEventListener('open', r));
let id = 0; const pend = new Map(); let carregou = false;
ws.addEventListener('message', ev => {
  const m = JSON.parse(ev.data);
  if (m.id && pend.has(m.id)) { pend.get(m.id)(m); pend.delete(m.id); }
  if (m.method === 'Page.loadEventFired') carregou = true;
});
const cdp = (method, params = {}) => new Promise(r => { const i = ++id; pend.set(i, r); ws.send(JSON.stringify({ id: i, method, params })); });
await cdp('Page.enable'); await cdp('Runtime.enable');
await cdp('Page.navigate', { url: pathToFileURL(ENT).href });
for (let i = 0; i < 240 && !carregou; i++) await espera(250);
if (!carregou) { console.log('FALHA: a página não terminou de carregar em 60 s'); await fim(1); }
await cdp('Runtime.evaluate', { expression: 'document.fonts ? document.fonts.ready.then(()=>1) : 1', awaitPromise: true });
await espera(1500);

let ini = 1, n = 0, ultima = '';
for (;;) {
  const faixa = `${ini}-${ini + PASSO - 1}`;
  const r = await cdp('Page.printToPDF', { printBackground: true, displayHeaderFooter: false, preferCSSPageSize: true, transferMode: 'ReturnAsStream', pageRanges: faixa });
  if (!r.result) {
    // a faixa passou do fim do documento: acabou. Na 1ª faixa, é falha de verdade.
    if (n === 0) { console.log(`FALHA: Page.printToPDF recusou ${faixa}: ${JSON.stringify(r.error)}`); await fim(1); }
    break;
  }
  const partes = [];
  for (;;) {
    const c = await cdp('IO.read', { handle: r.result.stream, size: 4 * 1024 * 1024 });
    if (!c.result) { console.log(`FALHA: IO.read: ${JSON.stringify(c.error)}`); await fim(1); }
    partes.push(Buffer.from(c.result.data, c.result.base64Encoded ? 'base64' : 'utf8'));
    if (c.result.eof) break;
  }
  await cdp('IO.close', { handle: r.result.stream });
  const buf = Buffer.concat(partes); n++;
  writeFileSync(`${PRE}.parte${String(n).padStart(2, '0')}.pdf`, buf);
  console.log(`parte ${n}: páginas ${faixa} · ${buf.length} bytes`);
  ultima = faixa; ini += PASSO;
}
clearTimeout(prazo);
console.log(`PARTES ${n} ${ultima}`);
await fim(n > 0 ? 0 : 1);
