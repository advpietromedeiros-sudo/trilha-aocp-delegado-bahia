// Teste do caderno de revisão no Chrome/Edge headless, via CDP (sem dependências: fetch e WebSocket do Node).
// Uso: node ferramentas/testar_revisao_navegador.mjs ARQUIVO.html [PASTA_PRINTS]
//      node ferramentas/testar_revisao_navegador.mjs --autoteste ARQUIVO.html
//        → planta um erro de JS numa cópia e só sai 0 se o teste ACUSAR (REGRA CINCO)
// Confere: abre sem erro de JS; progresso "X de N pontos" marca e persiste; "Só o essencial" esconde o
// que deve; ficha errada volta em "Fichas que errei"; questão A–E revela o gabarito; leitura no celular
// sem rolagem horizontal. Com PASTA_PRINTS, tira 4 prints (desktop e celular).
import { spawn } from 'node:child_process';
import { writeFileSync, readFileSync, mkdirSync, existsSync } from 'node:fs';
import { pathToFileURL } from 'node:url';
import { tmpdir } from 'node:os';
import { join, resolve } from 'node:path';

const args = process.argv.slice(2), AUTO = args.includes('--autoteste');
const pos = args.filter(a => !a.startsWith('--'));
if (!pos.length) { console.log('uso: node ferramentas/testar_revisao_navegador.mjs [--autoteste] ARQUIVO.html [PASTA_PRINTS]'); process.exit(2); }
let APP = resolve(pos[0]);
const PRINTS = !AUTO && pos[1] ? resolve(pos[1]) : null;
if (PRINTS) mkdirSync(PRINTS, { recursive: true });
if (AUTO) {
  const s = readFileSync(APP, 'utf8'), alvo = 'function refreshDone(){';
  const sab = s.replace(alvo, alvo + 'variavelQueNaoExiste.x=1;');
  if (sab === s) { console.log('AUTOTESTE: não consegui plantar o erro'); process.exit(1); }
  APP = join(tmpdir(), 'revisao-sabotada-' + Date.now() + '.html'); writeFileSync(APP, sab);
}
const NAV = ['C:/Program Files/Google/Chrome/Application/chrome.exe', 'C:/Program Files (x86)/Microsoft/Edge/Application/msedge.exe', 'C:/Program Files/Microsoft/Edge/Application/msedge.exe'].find(existsSync);
if (!NAV) { console.log('FALHA: nem Chrome nem Edge encontrados'); process.exit(1); }
const porta = 9400 + Math.floor(Math.random() * 400);
const nav = spawn(NAV, ['--headless=new', `--remote-debugging-port=${porta}`, '--window-size=1366,900', '--no-first-run', `--user-data-dir=${join(tmpdir(), 'revisao-' + Date.now())}`, 'about:blank'], { stdio: 'ignore' });
const espera = ms => new Promise(r => setTimeout(r, ms));
let alvo; for (let i = 0; i < 60 && !alvo; i++) { await espera(250); try { alvo = (await (await fetch(`http://127.0.0.1:${porta}/json`)).json()).find(t => t.type === 'page'); } catch { } }
if (!alvo) { console.log('FALHA: o navegador não respondeu'); nav.kill(); process.exit(1); }
const ws = new WebSocket(alvo.webSocketDebuggerUrl); await new Promise(r => ws.addEventListener('open', r));
let id = 0; const pend = new Map(); const erros = [];
ws.addEventListener('message', ev => {
  const m = JSON.parse(ev.data);
  if (m.id && pend.has(m.id)) { pend.get(m.id)(m); pend.delete(m.id); }
  if (m.method === 'Runtime.exceptionThrown') erros.push(m.params.exceptionDetails.exception?.description || m.params.exceptionDetails.text);
  if (m.method === 'Runtime.consoleAPICalled' && m.params.type === 'error') erros.push('console.error: ' + m.params.args.map(a => a.value ?? a.description).join(' '));
  if (m.method === 'Log.entryAdded' && m.params.entry.level === 'error' && !/favicon/.test(m.params.entry.url || '')) erros.push('log: ' + m.params.entry.text);
});
const cdp = (method, params = {}) => new Promise(r => { const i = ++id; pend.set(i, r); ws.send(JSON.stringify({ id: i, method, params })); });
const avalia = async e => { const r = await cdp('Runtime.evaluate', { expression: e, returnByValue: true, awaitPromise: true }); if (r.result?.exceptionDetails) return { erro: r.result.exceptionDetails.exception?.description }; return r.result?.result?.value; };
const print = async n => { if (!PRINTS) return; const r = await cdp('Page.captureScreenshot', { format: 'png' }); writeFileSync(join(PRINTS, n), Buffer.from(r.result.data, 'base64')); console.log('      print: ' + join(PRINTS, n)); };
const abre = async () => { await cdp('Page.navigate', { url: pathToFileURL(APP).href }); await espera(1500); };
const res = []; const confere = (n, ok, d = '') => { res.push(!!ok); console.log(`${ok ? 'OK   ' : 'FALHA'} ${n}${d ? ' · ' + d : ''}`); };
const fim = code => { try { ws.close(); } catch { } nav.kill(); process.exit(code); };

await cdp('Runtime.enable'); await cdp('Page.enable'); await cdp('Log.enable');
await abre();
// N1 · abre sem erro de JS e o motor do caderno subiu
const n1 = await avalia("({api:typeof window.revisaoAPI,cont:document.getElementById('studyCount').textContent,pontos:document.querySelectorAll('.card[data-ponto]').length,fichas:document.querySelectorAll('.quiz-card').length,botoes:document.querySelectorAll('.quiz-btn,.mc-btn').length})");
confere('N1 · abre sem erro de JS e monta o caderno', erros.length === 0 && n1?.api === 'object' && n1.pontos > 0 && n1.botoes > 0, erros.length ? erros.slice(0, 3).join(' | ') : JSON.stringify(n1));
if (AUTO) { const acusou = res.some(x => !x); console.log(acusou ? 'AUTOTESTE OK: o erro de JS plantado foi acusado' : 'AUTOTESTE FALHOU: o erro plantado passou'); fim(acusou ? 0 : 1); }
await avalia("try{localStorage.clear()}catch(e){}"); await abre();
await print('revisao-1-desktop-capa.png');
// N2 · marcar ponto revisado: X de N, persiste depois de recarregar
const total = n1.pontos;
await avalia("document.querySelector('.card[data-ponto] .done-btn').click()");
const n2a = await avalia("document.getElementById('studyCount').textContent");
await abre();
const n2b = await avalia("({c:document.getElementById('studyCount').textContent,p:document.getElementById('revProg').textContent,done:document.querySelectorAll('.card.done').length})");
confere('N2 · ponto revisado conta e persiste', n2a === `1 de ${total} pontos` && n2b.c === `1 de ${total} pontos` && n2b.done === 1, JSON.stringify({ antes: n2a, depois: n2b }));
// N3 · Só o essencial: fica o que cai, a lei e as pegadinhas
await avalia("document.querySelector('.rev-btn.js-essencial').click()");
const n3 = await avalia(`(function(){const vis=s=>[...document.querySelectorAll(s)].filter(e=>e.offsetParent!==null).length;
 return {ess:document.body.classList.contains('essencial'),cai:vis('.sec-cai'),lei:vis('.sec-lei'),peg:vis('.sec-pegadinhas'),
  outros:vis('.sec.nao-essencial'),fichas:vis('.quiz-card')}})()`);
confere('N3 · Só o essencial esconde o resto', n3.ess && n3.cai === total && n3.lei > 0 && n3.peg > 0 && n3.outros === 0 && n3.fichas === 0, JSON.stringify(n3));
await avalia("document.querySelector('.rev-btn.js-essencial').click()");
// N4 · erra uma ficha C/E: ela volta em "Fichas que errei", zerada
const n4a = await avalia(`(function(){const q=document.querySelector('.quiz-card[data-tipo="ce"]');const a=q.getAttribute('data-ans');
 q.querySelector('.quiz-btn[data-op="'+(a==='C'?'E':'C')+'"]').click();return {res:q.getAttribute('data-res'),verso:q.querySelector('.quiz-answer').classList.contains('show'),id:q.getAttribute('data-id')}})()`);
await avalia("document.querySelector('.rev-btn.js-erros').click()");
const n4b = await avalia(`(function(){const vis=s=>[...document.querySelectorAll(s)].filter(e=>e.offsetParent!==null);
 const v=vis('.quiz-card');return {modo:document.body.classList.contains('so-erros'),visiveis:v.length,id:v[0]&&v[0].getAttribute('data-id'),zerada:v[0]&&!v[0].getAttribute('data-done'),cai:vis('.sec-cai').length}})()`);
confere('N4 · ficha errada volta em "Fichas que errei"', n4a.res === 'no' && n4a.verso && n4b.modo && n4b.visiveis === 1 && n4b.id === n4a.id && n4b.zerada && n4b.cai === 0, JSON.stringify({ n4a, n4b }));
await avalia("document.getElementById('errosSair').click()");
// N5 · questão A–E: marca, revela o gabarito e trava
const n5 = await avalia(`(function(){const q=document.querySelector('.quiz-card[data-tipo="mc"]');if(!q)return {sem:true};const a=q.getAttribute('data-ans');
 q.querySelector('.mc-btn[data-op="'+a+'"]').click();return {res:q.getAttribute('data-res'),verso:q.querySelector('.quiz-answer').classList.contains('show'),travou:[...q.querySelectorAll('.mc-btn')].every(b=>b.disabled)}})()`);
confere('N5 · questão A–E corrige e revela o comentário', n5.sem || (n5.res === 'ok' && n5.verso && n5.travou), JSON.stringify(n5));
// N6 · aba do fichário e busca na lei seca
const n6 = await avalia(`(async function(){document.querySelector('.tab[data-tab="leiseca"]').click();const i=document.getElementById('lsSearch');
 const g=document.querySelectorAll('#lsContent .ls-art-group').length;i.value='crime';i.oninput();await new Promise(r=>setTimeout(r,400));
 const vis=[...document.querySelectorAll('#lsContent .ls-art-group')].filter(e=>e.offsetParent!==null).length;i.value='';i.oninput();await new Promise(r=>setTimeout(r,300));
 document.querySelector('.tab[data-tab="conteudo"]').click();return {g,vis}})()`);
confere('N6 · fichário da lei seca abre e a busca filtra', n6.g > 0 && n6.vis > 0 && n6.vis <= n6.g, JSON.stringify(n6));
// prints de desktop: um ponto no meio
let OFF = 130;
const rola = sel => avalia(`(function(){document.documentElement.style.scrollBehavior='auto';const e=document.querySelector(${JSON.stringify(sel)});window.scrollTo(0,e.getBoundingClientRect().top+window.scrollY-${OFF});return window.scrollY})()`);
await rola('.card[data-ponto]'); await espera(500);
await print('revisao-2-desktop-ponto.png');
// N7 · celular (390 × 844): sem rolagem horizontal, sidebar escondida, índice por prioridade visível
await cdp('Emulation.setDeviceMetricsOverride', { width: 390, height: 844, deviceScaleFactor: 2, mobile: true });
await abre();
const n7 = await avalia("({larg:document.documentElement.scrollWidth,vw:window.innerWidth,side:getComputedStyle(document.querySelector('.sidebar')).display,prio:document.querySelector('.prio-lista').offsetParent!==null,fonte:parseFloat(getComputedStyle(document.querySelector('.card p')).fontSize)})");
confere('N7 · celular: sem rolagem horizontal e leitura confortável', n7.larg <= n7.vw + 1 && n7.side === 'none' && n7.prio && n7.fonte >= 15, JSON.stringify(n7));
await print('revisao-3-celular-capa.png');
OFF = 110; await rola('.card[data-ponto] .sec-lei'); await espera(500);
await print('revisao-4-celular-ponto.png');
confere('N8 · nenhum erro de JS em toda a jornada', erros.length === 0, erros.slice(0, 3).join(' | '));
const ok = res.every(Boolean);
console.log(ok ? `TUDO OK (${res.length} conferências)` : `REPROVADO (${res.filter(x => !x).length} de ${res.length})`);
fim(ok ? 0 : 1);
