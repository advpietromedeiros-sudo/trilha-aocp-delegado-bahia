// testar_pente_fino.mjs — o Treino de Discursiva REAL no Chrome/Edge headless, via CDP (07/11/2026):
// (1) abre sem erro de JS, com 7 abas; (2) Simulados: comentário em quadros, alternativa do gabarito em verde, exceção em
// vermelho, chave em negrito, contraste AA e NENHUM caractere do comentário perdido na tela; (3) Pente Fino com o
// exemplo de .scratch/pente_fino/exemplo.js: responder, comentário com exceção vermelha, Rodada 2 bloqueada até
// concluir a 1 e liberada depois, atalhos C/E/setas, progresso que persiste ao recarregar, "rever as que errei",
// reiniciar com confirmação NA TELA (sem confirm()); (4) celular 360 px sem rolagem horizontal; (5) sem o arquivo de
// dados, a aba diz "conteúdo ainda não gerado".
// Uso: node docs/testar_pente_fino.mjs [PASTA_PRINTS]   ·   node docs/testar_pente_fino.mjs --autoteste
//   --autoteste planta 2 defeitos (Rodada 2 sempre liberada; exceção sem vermelho) e só sai 0 se CADA um for acusado.
// Um navegador por vez, fechado ao fim (a máquina tem pouca memória).
import { spawn } from 'node:child_process';
import { writeFileSync, readFileSync, mkdirSync, existsSync, rmSync } from 'node:fs';
import { pathToFileURL, fileURLToPath } from 'node:url';
import { tmpdir } from 'node:os';
import { join, resolve, dirname } from 'node:path';

const RAIZ = resolve(dirname(fileURLToPath(import.meta.url)), '..');
const DISC = join(RAIZ, 'discursiva'), PF = join(RAIZ, '.scratch', 'pente_fino');
const args = process.argv.slice(2), AUTO = args.includes('--autoteste');
const PRINTS = !AUTO && args.find(a => !a.startsWith('--')) ? resolve(args.find(a => !a.startsWith('--'))) : null;
mkdirSync(PF, { recursive: true }); if (PRINTS) mkdirSync(PRINTS, { recursive: true });
const EXEMPLO = join(PF, 'exemplo.js');
if (!existsSync(EXEMPLO)) { console.log('FALHA: falta o exemplo ' + EXEMPLO); process.exit(1); }
const TEM_SIM = existsSync(join(DISC, 'simulados_delta.js'));
const TAG_PF = '<script src="pente_fino_cpc.js" data-opcional="1"></script>';
const TAG_REV = '<script src="revisao_nfpss.js" data-local="terceiro"></script>';
const itRev = (id, ponto, pag, gab, extra = {}) => ({ id, ponto, pag, tema: 'Tema ' + id, gabarito: gab,
  assertiva: `Assertiva de revisão ${id}, do material, para julgar.`, comentario: { resumo: 'Por quê ' + id, ...extra } });
const EXEMPLO_REV = { TRI: { disciplina: 'Tributário', fontes: '4 assertivas de exemplo.', pontos: [{ id: 'imunidades', titulo: 'Imunidades' }, { id: 'icms', titulo: 'ICMS' }],
  rodadas: [{ n: 1, titulo: 'Bloco 1 · p. 61–72', itens: [itRev('TRI01-001', 'imunidades', 61, 'E', { divergencia: 'O material traz a regra anterior à EC 132/2023.',
      correcao: { erro: 'Diz que a imunidade alcança qualquer taxa.', certo: 'A imunidade recíproca alcança só impostos, não taxas.' },
      aprofundamento: 'A imunidade protege o **pacto federativo**: um ente não tributa o patrimônio do outro por meio de impostos.\n\nAs taxas remuneram serviço ou poder de polícia; por isso ficam fora da regra, salvo previsão expressa, e não pode ser outra a leitura.',
      memorize: 'Imunidade recíproca = só **impostos**.' }), itRev('TRI01-002', 'imunidades', 62, 'C')] },
    { n: 2, titulo: 'Bloco 2 · p. 73–83', itens: [itRev('TRI02-001', 'icms', 73, 'C'), itRev('TRI02-002', 'icms', 75, 'E')] }] } };
const original = readFileSync(join(DISC, 'Treino_Discursiva.html'), 'utf8');
if (!original.includes(TAG_PF)) { console.log('FALHA: a página não tem a tag do pente_fino_cpc.js'); process.exit(1); }

// cópia da página com <base> na pasta discursiva/ (os scripts reais carregam de lá) e o Pente Fino trocado
const pagina = (nome, srcPF, sabotar = null) => {
  let h = original.replace('<head>', `<head><base href="${pathToFileURL(DISC).href}/">`).replace(TAG_PF, `<script src="${srcPF}"></script>`);
  // 07/11/2026: com mais de uma disciplina na página (pente_fino_civ.js...), as outras saem da cópia de teste,
  // para que a suíte veja só o exemplo (ou nenhum dado, no T23).
  h = h.replace(/<script src="pente_fino_[a-z]+\.js" data-opcional="1"><\/script>\n?/g, '');
  // 09/11/2026: a aba Revisão lê material de terceiro que só existe na máquina do titular; a cópia de teste usa o
  // exemplo fixo abaixo (sem ele, o 404 do arquivo local derrubava o T22).
  if (!h.includes(TAG_REV)) throw new Error('a página não tem a tag do revisao_nfpss.js');
  h = h.replace(TAG_REV, `<script>window.REVISAO=${JSON.stringify(EXEMPLO_REV)};</script>`);
  if (sabotar) { const h2 = sabotar(h); if (h2 === h) throw new Error('não plantou: ' + nome); h = h2; }
  const arq = join(PF, nome); writeFileSync(arq, h); return arq;
};
const SABOTAGENS = [
  ['Rodada 2 sempre liberada', s => s.replace('const pfLiberada=(D,e,n)=>!PF_FONTES[pfAba].trava||n<=1||pfConcluida(D,e,n-1);', 'const pfLiberada=()=>true;')],
  ['Revisão gravando no progresso do Pente Fino', s => s.replace("revisao:{chave:'revisao:v1'", "revisao:{chave:PF_CHAVE")],
  ['aprofundamento com vermelho automático', s => s.replace('.map(x=>`<p>${B(x.trim())}</p>`)', '.map(x=>`<p>${M(x.trim())}</p>`)')],
  ['Revisão com a trava de rodada', s => s.replace("titulo:'📚 Revisão',trava:false", "titulo:'📚 Revisão',trava:true")],
  ['tela não acompanha a assertiva', s => s.replace('function pfRolar(){', 'function pfRolar(){return;')],
  ['exceção sem vermelho',s => s.replace('.cm-exc{color:#a3211a;', '.cm-exc{color:inherit;')],
];

const NAV = ['C:/Program Files/Google/Chrome/Application/chrome.exe', 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe', 'C:/Program Files (x86)/Microsoft/Edge/Application/msedge.exe', 'C:/Program Files/Microsoft/Edge/Application/msedge.exe'].find(existsSync);
if (!NAV) { console.log('FALHA: nem Chrome nem Edge encontrados'); process.exit(1); }
const perfil = join(tmpdir(), 'pente-fino-' + Date.now());
const porta = 9400 + Math.floor(Math.random() * 400);
const nav = spawn(NAV, ['--headless=new', `--remote-debugging-port=${porta}`, '--window-size=1366,900', '--no-first-run', '--allow-file-access-from-files', `--user-data-dir=${perfil}`, 'about:blank'], { stdio: 'ignore' });
const espera = ms => new Promise(r => setTimeout(r, ms));
let alvo; for (let i = 0; i < 60 && !alvo; i++) { await espera(250); try { alvo = (await (await fetch(`http://127.0.0.1:${porta}/json`)).json()).find(t => t.type === 'page'); } catch { } }
if (!alvo) { console.log('FALHA: o navegador não respondeu'); nav.kill(); process.exit(1); }
const ws = new WebSocket(alvo.webSocketDebuggerUrl); await new Promise(r => ws.addEventListener('open', r));
let id = 0; const pend = new Map(); let erros = [], ignorar404 = false;
ws.addEventListener('message', ev => {
  const m = JSON.parse(ev.data);
  if (m.id && pend.has(m.id)) { pend.get(m.id)(m); pend.delete(m.id); }
  if (m.method === 'Runtime.exceptionThrown') erros.push(m.params.exceptionDetails.exception?.description || m.params.exceptionDetails.text);
  if (m.method === 'Runtime.consoleAPICalled' && m.params.type === 'error') erros.push('console.error: ' + m.params.args.map(a => a.value ?? a.description).join(' '));
  if (m.method === 'Log.entryAdded' && m.params.entry.level === 'error' && !/favicon/.test(m.params.entry.url || '') && !(ignorar404 && /ERR_FILE_NOT_FOUND/.test(m.params.entry.text))) erros.push('log: ' + m.params.entry.text + ' ' + (m.params.entry.url || ''));
});
const cdp = (method, params = {}) => new Promise(r => { const i = ++id; pend.set(i, r); ws.send(JSON.stringify({ id: i, method, params })); });
const avalia = async e => { const r = await cdp('Runtime.evaluate', { expression: e, returnByValue: true, awaitPromise: true }); if (r.result?.exceptionDetails) return { erro: r.result.exceptionDetails.exception?.description }; return r.result?.result?.value; };
const abre = async arq => { await cdp('Page.navigate', { url: pathToFileURL(arq).href }); await espera(TEM_SIM ? 2200 : 1200); };
const tecla = async (key, code, vk, text) => { await cdp('Input.dispatchKeyEvent', { type: 'keyDown', key, code, windowsVirtualKeyCode: vk, ...(text ? { text } : {}) }); await cdp('Input.dispatchKeyEvent', { type: 'keyUp', key, code, windowsVirtualKeyCode: vk }); await espera(150); };
const print = async (nome, sel) => {
  if (!PRINTS) return;
  let p = { format: 'png' };
  if (sel) { const r = await avalia(`(function(){const e=document.querySelector(${JSON.stringify(sel)});if(!e)return null;const b=e.getBoundingClientRect();return {x:Math.max(0,b.left+scrollX-8),y:Math.max(0,b.top+scrollY-8),w:b.width+16,h:Math.min(b.height+16,2600)}})()`); if (r) p = { format: 'png', captureBeyondViewport: true, clip: { x: r.x, y: r.y, width: r.w, height: r.h, scale: 1 } }; }
  const r = await cdp('Page.captureScreenshot', p); writeFileSync(join(PRINTS, nome), Buffer.from(r.result.data, 'base64')); console.log('      print: ' + join(PRINTS, nome));
};
const fim = code => { try { ws.close(); } catch { } nav.kill(); setTimeout(() => { try { rmSync(perfil, { recursive: true, force: true }); } catch { } process.exit(code); }, 400); };

// funções de página: contraste WCAG e texto do comentário sem o que a tela acrescenta (entre <!--g--> e <!--/g-->)
const AJUDA = `window.__t={
 rgb:c=>{const m=String(c).match(/[\\d.]+/g);return m?m.slice(0,4).map(Number):null},
 lum:a=>{const f=v=>{v/=255;return v<=.03928?v/12.92:((v+.055)/1.055)**2.4};return .2126*f(a[0])+.7152*f(a[1])+.0722*f(a[2])},
 fundo:e=>{for(let x=e;x;x=x.parentElement){const c=__t.rgb(getComputedStyle(x).backgroundColor);if(c&&(c.length<4||c[3]>0))return c}return [255,255,255]},
 contraste:e=>{const a=__t.lum(__t.rgb(getComputedStyle(e).color)),b=__t.lum(__t.fundo(e));return (Math.max(a,b)+.05)/(Math.min(a,b)+.05)},
 textoSemGerado:raiz=>{let s='',g=0;const w=document.createTreeWalker(raiz,NodeFilter.SHOW_TEXT|NodeFilter.SHOW_COMMENT);let n;while((n=w.nextNode())){if(n.nodeType===8){if(n.data==='g')g++;else if(n.data==='/g')g--;continue}if(!g)s+=n.data}return s},
 sem:s=>[...String(s).replace(/\\s+/g,'')].sort().join('')};`;

const res = []; let prefixo = '';
const confere = (n, ok, d = '') => { res.push(!!ok); console.log(`${ok ? 'OK   ' : 'FALHA'} ${prefixo}${n}${!ok && d ? ' · ' + d : ''}`); };

async function suite(arq, completo) {
  erros = [];
  await abre(arq); await avalia("try{localStorage.clear()}catch(e){}"); await abre(arq); await avalia(AJUDA);
  const t1 = await avalia("({abas:document.querySelectorAll('#abas button').length,pente:[...document.querySelectorAll('#abas button')].map(b=>b.textContent).join('|'),api:typeof window.discAPI,blocos:typeof BLOCOS.comentario})");
  confere('T1 · abre sem erro de JS, com 8 abas: Pente Fino ao lado de Simulados e Revisão ao lado do Pente Fino', erros.length === 0 && t1?.abas === 8 && /Simulados\|🔍 Pente Fino\|📚 Revisão/.test(t1.pente) && t1.blocos === 'function', erros.slice(0, 3).join(' | ') || JSON.stringify(t1));

  // ---------- Simulados: quadros, verde, vermelho, negrito, AA, nenhum caractere perdido ----------
  if (TEM_SIM) {
    const alvoQ = await avalia(`(function(){for(const s of discAPI.SIMS)for(const q of s.questoes){if(q.anulada)continue;const h=BLOCOS.comentario(q.com,{gab:q.gab});
      if(h.includes('cm-alt-gab')&&h.includes('cm-exc')&&/cm-chave">(?:art|Art)/.test(h))return {sim:s.id,n:q.n,gab:q.gab};}return null})()`);
    if (!alvoQ) confere('T2 · achou questão com alternativa do gabarito, exceção e artigo', false);
    else {
      await avalia(`discAPI.abrirSim(${JSON.stringify(alvoQ.sim)},'estudo');document.querySelector('[data-simir="${alvoQ.n}"]').click();document.querySelector('[data-simalt="${alvoQ.gab}"]').click();document.getElementById('simConfirma').click();`);
      await avalia(AJUDA);
      const t2 = await avalia(`(function(){const c=document.querySelector('.sq .com');if(!c)return {sem:true};const exc=c.querySelector('.cm-exc'),ch=c.querySelector('.cm-chave'),gab=c.querySelector('.cm-alt-gab');
        const q=discAPI.SIMS.find(s=>s.id===${JSON.stringify(alvoQ.sim)}).questoes.find(x=>x.n===${alvoQ.n});
        const orig=q.com.filter(b=>b[0]==='p'||b[0]==='pre').map(b=>b[1]).join('');const tela=__t.textoSemGerado(c).replace(/^\\s*Comentários/,'');
        const AA=[...c.querySelectorAll('.cm-exc,.cm-chave,.cm-sep,.cm-ver,.cm-rot,.cm-alt-corpo p,.cm-letra,.cm-gab')].map(e=>[e.className,__t.contraste(e)]).filter(([,r])=>r<4.5);
        return {quadros:c.querySelectorAll('.cm-q').length,alts:c.querySelectorAll('.cm-alt').length,gabLetra:gab&&gab.querySelector('.cm-letra').textContent.replace(/[^A-Ea-e]/g,'').slice(-1).toUpperCase(),
          excCor:exc&&getComputedStyle(exc).color,chPeso:ch&&+getComputedStyle(ch).fontWeight,gabFundo:gab&&getComputedStyle(gab).backgroundColor,
          perdidos:__t.sem(orig)===__t.sem(tela)?0:Math.abs(__t.sem(orig).length-__t.sem(tela).length)||-1,AA:AA.slice(0,4)}})()`);
      confere('T2 · Simulados: comentário em quadros, com a análise das alternativas', t2.quadros >= 1 && t2.alts >= 3, JSON.stringify(t2));
      confere('T3 · a alternativa do gabarito sai em verde', t2.gabLetra === alvoQ.gab && /rgb\(238, 248, 242\)/.test(t2.gabFundo), JSON.stringify({ g: t2.gabLetra, f: t2.gabFundo, gab: alvoQ.gab }));
      confere('T4 · exceção em vermelho e palavra-chave em negrito', t2.excCor === 'rgb(163, 33, 26)' && t2.chPeso >= 700, JSON.stringify({ c: t2.excCor, p: t2.chPeso }));
      confere('T5 · nenhum caractere do comentário perdido na tela', t2.perdidos === 0, 'diferença: ' + t2.perdidos);
      confere('T6 · contraste AA (≥ 4,5:1) nos textos do comentário', t2.AA.length === 0, JSON.stringify(t2.AA));
      if (completo) { await avalia("document.querySelector('.sq .com').scrollIntoView()"); await print('1-simulado-comentario-desktop.png', '.sq .com'); }
      // todas as 400 questões: nenhum caractere perdido no HTML montado (o mesmo da tela)
      const t7 = await avalia(`(function(){const box=document.createElement('div');let perdas=[],n=0;for(const s of discAPI.SIMS)for(const q of s.questoes){n++;box.innerHTML=BLOCOS.comentario(q.com,{gab:q.gab});
        const orig=q.com.filter(b=>b[0]==='p'||b[0]==='pre').map(b=>b[1]).join('');if(__t.sem(orig)!==__t.sem(__t.textoSemGerado(box)))perdas.push(s.id+'#'+q.n)}return {n,perdas:perdas.slice(0,5),np:perdas.length}})()`);
      confere(`T7 · ${t7.n} comentários montados no navegador: nenhum caractere perdido`, t7.n >= 400 && t7.np === 0, JSON.stringify(t7));
    }
  } else console.log('      (simulados_delta.js ausente: material local; T2–T7 pulados)');

  // ---------- Pente Fino ----------
  await avalia("discAPI.ir('pente')"); await avalia(AJUDA);
  const t8 = await avalia(`(function(){const r=[...document.querySelectorAll('[data-pfrod]')];return {rods:r.length,r1:r[0]&&!r[0].disabled,r2:r[1]&&r[1].disabled,r2txt:r[1]&&r[1].textContent,
    assert:(document.getElementById('pfAssertiva')||{}).textContent,ce:document.querySelectorAll('[data-pfr]').length,pontos:document.querySelectorAll('[data-pfponto]').length}})()`);
  confere('T8 · Pente Fino: Rodada 1 liberada, Rodada 2 com cadeado e "Conclua a Rodada 1"', t8.rods === 2 && t8.r1 && t8.r2 && /🔒/.test(t8.r2txt) && /Conclua a Rodada 1/.test(t8.r2txt) && t8.ce === 2 && t8.pontos === 3, JSON.stringify(t8));
  // tela baixa para a página precisar rolar; responder e trocar de assertiva põem o quadro no topo (pedido de 08/11/2026)
  await cdp('Emulation.setDeviceMetricsOverride', { width: 1000, height: 420, deviceScaleFactor: 1, mobile: false });
  await avalia('scrollTo(0,0)');
  const topoItem = async () => { await espera(900); return avalia("Math.round(document.querySelector('.pf-item').getBoundingClientRect().top)"); };
  await avalia(`document.querySelector('[data-pfr="C"]').click()`); // gabarito da 1ª é E: erra de propósito
  const r24a = await topoItem();
  await avalia("document.getElementById('pfProx').click()"); const r24b = await topoItem();
  await avalia('scrollTo(0,0)'); await avalia("document.getElementById('pfAnt').click()"); const r24c = await topoItem();
  await cdp('Emulation.clearDeviceMetricsOverride');
  confere('T24 · responder, Próxima e Anterior deixam o quadro da assertiva no topo da tela (comentário visível logo abaixo)', [r24a, r24b, r24c].every(t => t >= 0 && t <= 24), JSON.stringify({ responder: r24a, proxima: r24b, anterior: r24c }));
  await avalia(AJUDA);
  const t9 = await avalia(`(function(){const fb=document.querySelector('.pf-fb');const li=document.querySelector('.cm-exc-lista li');const ex=document.querySelector('.pf-com .cm-exc');
    return {fb:fb&&fb.textContent,quadros:[...document.querySelectorAll('.pf-com .cm-q .cm-rot')].map(x=>x.textContent.trim()),liCor:li&&getComputedStyle(li).color,excCor:ex&&getComputedStyle(ex).color,
      negrito:!!document.querySelector('.pf-com .cm-chave'),tags:document.querySelectorAll('.cm-tags span').length,lei:(document.querySelector('.cm-cit figcaption')||{}).textContent,
      jur:(document.querySelector('.cm-jur-fonte')||{}).textContent,travou:[...document.querySelectorAll('[data-pfr]')].every(b=>b.disabled),
      AA:[...document.querySelectorAll('.pf-com .cm-rot,.cm-exc-lista li,.cm-tags span,.cm-jur-fonte,.cm-cit figcaption,.pf-fb,.pf-com p')].map(e=>[e.className||e.tagName,__t.contraste(e)]).filter(([,r])=>r<4.5)}})()`);
  confere('T9 · responder: feedback, comentário em quadros (resumo, regra, exceções, lei, jurisprudência, pegadinha) e etiquetas', /Errou/.test(t9.fb) && /ERRADO/.test(t9.fb) && t9.quadros.length === 6 && t9.negrito && t9.tags === 3 && t9.lei === 'CPC, art. 10' && /STJ · .+ · 01\/01\/2026/.test(t9.jur) && t9.travou, JSON.stringify(t9));
  confere('T10 · exceções do comentário em vermelho (lista e oração)', /^rgb\(143, 29, 23\)/.test(t9.liCor) && t9.excCor === 'rgb(163, 33, 26)', JSON.stringify({ li: t9.liCor, ex: t9.excCor }));
  confere('T11 · contraste AA no comentário do Pente Fino', t9.AA.length === 0, JSON.stringify(t9.AA));
  if (completo) await print('2-pente-fino-comentario-desktop.png', '#tela');
  // atalhos: → vai à próxima; C responde
  await tecla('ArrowRight', 'ArrowRight', 39); await tecla('c', 'KeyC', 67, 'c');
  const t12 = await avalia(`({pos:document.querySelector('.pf-item .pf-meta b').textContent,fb:(document.querySelector('.pf-fb')||{}).textContent,st:JSON.parse(localStorage.getItem('pente-fino:v1')||'{}')})`);
  confere('T12 · atalhos: → leva à assertiva 2 e C responde (acerto)', /Assertiva 2 de 4/.test(t12.pos) && /Acertou/.test(t12.fb || ''), JSON.stringify({ pos: t12.pos, fb: t12.fb }));
  await tecla('ArrowLeft', 'ArrowLeft', 37);
  const t12b = await avalia("document.querySelector('.pf-item .pf-meta b').textContent");
  confere('T13 · atalho ← volta à assertiva 1', /Assertiva 1 de 4/.test(t12b), t12b);
  // recarregar: o progresso continua
  await abre(arq); await avalia("discAPI.ir('pente')");
  const t14 = await avalia(`({geral:[...document.querySelectorAll('.pf-meta span')].map(x=>x.textContent).join(' '),chave:!!localStorage.getItem('pente-fino:v1'),r2:document.querySelectorAll('[data-pfrod]')[1].disabled})`);
  confere('T14 · progresso salvo no localStorage (pente-fino:v1) e de volta ao recarregar', t14.chave && /2 de 4 respondidas · 1 acertos/.test(t14.geral) && t14.r2, JSON.stringify(t14));
  // ir para um ponto: o 3 (prazos recursais)
  await avalia(`document.querySelector('[data-pfponto="DBA26-CPC-3"]').click()`);
  const t15 = await avalia("({m:document.querySelector('.pf-item .pf-meta').textContent})");
  confere('T15 · ir para um ponto do edital abre a assertiva dele', /Ponto 3 · Recursos/.test(t15.m) && /Assertiva 4 de 4/.test(t15.m), t15.m);
  await avalia(`document.querySelector('[data-pfr="C"]').click()`);
  await avalia(`document.querySelector('[data-pfponto="DBA26-CPC-2"]').click()`); await avalia(`document.querySelector('[data-pfr="C"]').click()`); // erra (gabarito E)
  const t16 = await avalia(`(function(){const r=document.querySelectorAll('[data-pfrod]');return {r2:r[1].disabled,fim:(document.querySelector('.pf-fim')||{}).textContent,ponto:[...document.querySelectorAll('[data-pfponto] small')].map(x=>x.textContent)}})()`);
  confere('T16 · concluída a Rodada 1, a Rodada 2 libera, com aviso de conclusão e progresso por ponto', t16.r2 === false && /Rodada 1 · O essencial concluída/.test(t16.fim || '') && /Rodada 2 está liberada/.test(t16.fim || '') && t16.ponto.join('|') === '2 de 2|1 de 1|1 de 1', JSON.stringify(t16));
  await avalia(`document.querySelectorAll('[data-pfrod]')[1].click()`);
  const t17 = await avalia("({t:document.querySelector('.pf-rod.on b').textContent,a:document.getElementById('pfAssertiva').textContent})");
  confere('T17 · Rodada 2 abre as assertivas de aprofundamento', /Rodada 2/.test(t17.t) && /tutela da evidência/.test(t17.a), JSON.stringify(t17));
  // rever as que errei, na Rodada 1
  await avalia(`document.querySelectorAll('[data-pfrod]')[0].click()`); await avalia(`document.getElementById('pfSoErros').click()`);
  const t18 = await avalia("({m:document.querySelector('.pf-item .pf-meta').textContent})");
  confere('T18 · "rever as que errei" mostra só as 2 erradas', /Assertiva 1 de 2/.test(t18.m) && /só as que errei/.test(t18.m), t18.m);
  await avalia(`document.getElementById('pfSoErros').click()`);
  // reiniciar: confirmação na tela, sem confirm()
  await avalia("window.__confirmou=0;window.confirm=()=>{window.__confirmou++;return true};document.getElementById('pfReset').click()");
  const t19a = await avalia("({painel:!!document.querySelector('.pf-confirma'),txt:(document.querySelector('.pf-confirma')||{}).textContent,ainda:document.querySelectorAll('[data-pfrod]')[1].disabled})");
  await avalia("document.getElementById('pfResetNao').click()");
  const t19b = await avalia("({painel:!!document.querySelector('.pf-confirma'),geral:document.querySelector('.pf-meta span').textContent})");
  await avalia("document.getElementById('pfReset').click();document.getElementById('pfResetSim').click()");
  const t19c = await avalia("({geral:document.querySelector('.pf-meta span').textContent,r2:document.querySelectorAll('[data-pfrod]')[1].disabled,conf:window.__confirmou})");
  confere('T19 · reiniciar pede confirmação na tela; Cancelar mantém; Sim zera e a Rodada 2 volta ao cadeado', t19a.painel && /Apagar as 4 resposta/.test(t19a.txt) && !t19b.painel && /4 de 4/.test(t19b.geral) && /0 de 4/.test(t19c.geral) && t19c.r2 && t19c.conf === 0, JSON.stringify({ t19a, t19b, t19c }));

  // ---------- Revisão (09/11/2026): o mesmo motor, blocos todos abertos e progresso em chave própria ----------
  const pfAntes = await avalia("localStorage.getItem('pente-fino:v1')");
  await avalia("discAPI.ir('revisao')"); await avalia('scrollTo(0,0)');
  const t25 = await avalia(`(function(){const r=[...document.querySelectorAll('[data-pfrod]')];return {h:document.querySelector('#tela h2').textContent,rods:r.length,abertos:r.every(b=>!b.disabled),
    cad:/🔒|Conclua/.test(r.map(b=>b.textContent).join(' ')),meta:document.querySelector('.pf-item .pf-meta').textContent,sum:document.querySelector('.pf-pontos summary').textContent}})()`);
  confere('T25 · Revisão: abre com os blocos todos liberados (sem cadeado), seção e página do material', /📚 Revisão/.test(t25.h) && t25.rods === 2 && t25.abertos && !t25.cad && /Seção 1 · Imunidades/.test(t25.meta) && /p\. 61 do material/.test(t25.meta) && /seção do material/.test(t25.sum), JSON.stringify(t25));
  await tecla('c', 'KeyC', 67, 'c');
  const t26 = await avalia(`({fb:(document.querySelector('.pf-fb')||{}).textContent,div:[...document.querySelectorAll('.pf-com .cm-rot')].map(x=>x.textContent).join('|'),
    rev:JSON.parse(localStorage.getItem('revisao:v1')||'{}'),pf:localStorage.getItem('pente-fino:v1')})`);
  await avalia(AJUDA);
  const t28 = await avalia(`(function(){const c=document.querySelector('.pf-com');return {rot:[...c.querySelectorAll('.cm-rot')].map(x=>x.textContent.trim()),
    erro:(c.querySelector('.cm-cmp-erro')||{}).textContent,certo:(c.querySelector('.cm-cmp-certo')||{}).textContent,pars:c.querySelectorAll('.cm-aprof p').length,
    vermelho:!!c.querySelector('.cm-aprof .cm-exc'),neg:!!c.querySelector('.cm-aprof .cm-chave'),memo:(c.querySelector('.cm-memo')||{}).textContent,
    AA:[...c.querySelectorAll('.cm-cmp-erro,.cm-cmp-certo,.cm-cmp b,.cm-aprof p,.cm-memo b,.cm-memo span')].map(e=>[e.className||e.tagName,__t.contraste(e)]).filter(([,r])=>r<4.5)}})()`);
  confere('T28 · comentário aprofundado: o erro ao lado do certo, aprofundamento em parágrafos (só negrito, sem vermelho automático), "Para memorizar" e contraste AA',
    t28.rot.join('|') === '💡 Por quê|🔁 Onde está o erro|🔎 Aprofundando|⚠️ O material diverge' && /A assertiva diz.*qualquer taxa/.test(t28.erro) && /O correto.*não taxas/.test(t28.certo)
    && t28.pars === 2 && t28.neg && !t28.vermelho && /Para memorizar.*impostos/.test(t28.memo) && t28.AA.length === 0, JSON.stringify(t28));
  confere('T26 · Revisão: atalho C responde, o comentário mostra "O material diverge" e o progresso vai para revisao:v1 sem tocar no Pente Fino',
    /Errou/.test(t26.fb || '') && /O material diverge/.test(t26.div) && t26.rev?.d?.TRI?.resp?.['TRI01-001'] === 'C' && t26.pf === pfAntes, JSON.stringify({ fb: t26.fb, div: t26.div, rev: t26.rev?.d, igual: t26.pf === pfAntes }));
  await avalia(`document.querySelectorAll('[data-pfrod]')[1].click()`);
  const t27a = await avalia("({t:document.querySelector('.pf-rod.on b').textContent,a:document.getElementById('pfAssertiva').textContent})");
  await avalia("discAPI.ir('pente')");
  const t27b = await avalia("({h:document.querySelector('#tela h2').textContent,geral:document.querySelector('.pf-meta span').textContent})");
  await avalia("discAPI.ir('revisao')");
  const t27c = await avalia("document.querySelector('.pf-rod.on b').textContent");
  confere('T27 · Revisão: o bloco 2 abre sem concluir o 1; ir ao Pente Fino e voltar mantém cada aba no seu ponto',
    /Bloco 2/.test(t27a.t) && /TRI02-001/.test(t27a.a) && /🔍 Pente Fino/.test(t27b.h) && /0 de 4/.test(t27b.geral) && /Bloco 2/.test(t27c), JSON.stringify({ t27a, t27b, t27c }));
  await avalia("discAPI.ir('pente')");

  // ---------- celular 360 px ----------
  if (completo) {
    await cdp('Emulation.setDeviceMetricsOverride', { width: 360, height: 780, deviceScaleFactor: 2, mobile: true });
    await abre(arq); await avalia("discAPI.ir('pente')"); await avalia(`document.querySelector('[data-pfr="C"]').click()`);
    const t20 = await avalia("({larg:document.documentElement.scrollWidth,vw:innerWidth,bt:document.querySelector('[data-pfr]').getBoundingClientRect().height})");
    confere('T20 · celular 360 px: Pente Fino sem rolagem horizontal e botões grandes (≥ 56 px)', t20.larg <= t20.vw + 1 && t20.bt >= 56, JSON.stringify(t20));
    await avalia("scrollTo(0,0)"); await print('3-pente-fino-celular-topo.png');
    await avalia("document.querySelector('.pf-item').scrollIntoView()"); await print('4-pente-fino-celular-comentario.png', '.pf-item');
    if (TEM_SIM) {
      await avalia(AJUDA);
      const alvoQ = await avalia(`(function(){for(const s of discAPI.SIMS)for(const q of s.questoes){const h=BLOCOS.comentario(q.com,{gab:q.gab});if(!q.anulada&&h.includes('cm-alt-gab')&&h.includes('cm-exc')&&h.includes('bl-tab'))return {sim:s.id,n:q.n,gab:q.gab}}return null})()`);
      if (alvoQ) {
        await avalia(`discAPI.abrirSim(${JSON.stringify(alvoQ.sim)},'estudo');document.querySelector('[data-simir="${alvoQ.n}"]').click();document.querySelector('[data-simalt="${alvoQ.gab}"]').click();document.getElementById('simConfirma').click();`);
        const t21 = await avalia("({larg:document.documentElement.scrollWidth,vw:innerWidth})");
        confere('T21 · celular 360 px: comentário do simulado (com tabela) sem rolagem horizontal da página', t21.larg <= t21.vw + 1, JSON.stringify(t21));
        await avalia("document.querySelector('.sq .com').scrollIntoView()"); await print('5-simulado-comentario-celular.png', '.sq .com');
      }
    }
    await cdp('Emulation.clearDeviceMetricsOverride');
  }
  confere('T22 · nenhum erro de JS em toda a jornada', erros.length === 0, erros.slice(0, 3).join(' | '));
}

await cdp('Runtime.enable'); await cdp('Page.enable'); await cdp('Log.enable');
if (AUTO) {
  let todos = true;
  for (const [nome, f] of SABOTAGENS) {
    const ini = res.length; prefixo = `[sabotagem: ${nome}] `;
    await suite(pagina('_teste_sabotado.html', pathToFileURL(EXEMPLO).href, f), false);
    const acusou = res.slice(ini).some(x => !x);
    console.log(acusou ? `AUTOTESTE: "${nome}" foi ACUSADO` : `AUTOTESTE: "${nome}" PASSOU sem ser acusado`);
    if (!acusou) todos = false;
  }
  console.log(todos ? 'AUTOTESTE OK: os defeitos plantados foram acusados' : 'AUTOTESTE FALHOU: algum defeito passou'); fim(todos ? 0 : 1);
} else {
  await suite(pagina('_teste.html', pathToFileURL(EXEMPLO).href), true);
  // sem o arquivo de dados: "conteúdo ainda não gerado", sem erro de JS (o 404 do script opcional é esperado)
  erros = []; ignorar404 = true;
  await abre(pagina('_teste_sem_dados.html', 'pente_fino_que_nao_existe.js')); await avalia("discAPI.ir('pente')");
  const t23 = await avalia("document.getElementById('tela').textContent");
  confere('T23 · sem o arquivo do Pente Fino, a aba diz "Conteúdo ainda não gerado" e nada quebra', /Conteúdo ainda não gerado/.test(t23) && erros.length === 0, erros.join(' | ') || t23.slice(0, 120));
  if (PRINTS) await print('6-pente-fino-sem-dados.png');
  const ok = res.every(Boolean);
  console.log(ok ? `TUDO OK (${res.length} conferências)` : `REPROVADO (${res.filter(x => !x).length} de ${res.length})`);
  fim(ok ? 0 : 1);
}
