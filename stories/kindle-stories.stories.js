// Protótipo "Kindle + Stories" (19/11/2026, pedido do titular a partir de fotos do Kindle Scribe):
// um layout/funções no estilo Kindle (home de e-reader: Retomar, Biblioteca em capas, barra inferior) somado a uma
// PEGADA DE STORIES DO INSTAGRAM para estudar a letra de lei (tela cheia, barrinhas de progresso no topo, toque
// para revelar/avançar). Só VISUAL para aprovação (HARNESS: mockup se apresenta no Storybook). Nada de terceiro:
// letra de lei oficial, método de estudo autoral, identidade própria (não copia marca do Kindle nem do Instagram).

// Diplomas "na estante" (capas) + alguns segmentos de Stories por diploma.
const DADOS = {
  diplomas: [
    { sigla:'CF',  nome:'Constituição Federal', arts:14, pct:35 },
    { sigla:'CP',  nome:'Código Penal',          arts:16, pct:20 },
    { sigla:'CPP', nome:'Código de Processo Penal', arts:10, pct:10 },
    { sigla:'CC',  nome:'Código Civil',          arts:10, pct:0 },
    { sigla:'CPC', nome:'Processo Civil',        arts:9,  pct:0 },
    { sigla:'CTN', nome:'Código Tributário',     arts:7,  pct:0 },
  ],
  retomar: [
    { dip:'CF', art:'5º', rub:'Direitos e garantias fundamentais', pct:35 },
    { dip:'CP', art:'18', rub:'Crime doloso e culposo', pct:20 },
  ],
  // segmentos de story (um "slide" por lacuna): antes {lacuna} depois
  stories: {
    CF: [
      { art:'1º', rub:'Fundamentos', ante:'A República constitui-se em', gap:'Estado Democrático de Direito', dep:'e tem como fundamentos…' },
      { art:'1º', rub:'Fundamentos', ante:'III - a', gap:'dignidade da pessoa humana', dep:'' },
      { art:'5º', rub:'Legalidade', ante:'II - ninguém será obrigado a fazer ou deixar de fazer senão em virtude de', gap:'lei', dep:'' },
      { art:'5º', rub:'Presunção de inocência', ante:'LVII - ninguém será considerado culpado até o', gap:'trânsito em julgado', dep:'de sentença penal condenatória' },
      { art:'5º', rub:'Prisão', ante:'LXI - ninguém será preso senão em', gap:'flagrante delito', dep:'ou por ordem escrita e fundamentada da autoridade judiciária' },
    ],
  },
};

function pagina(view0) {
  const sai = '</' + 'script>';
  const dados = JSON.stringify(DADOS);
  return `<!doctype html><html lang="pt-BR"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<style>
:root{
  --papel:#f7f6f2; --tinta:#222; --suave:#6b6b6b; --linha:#e2e0d9; --cartao:#fff;
  --acento:#2b2b2b; --barra:#111; --prog:#111; --progoff:#d9d6cd; --selo:#333;
}
*{box-sizing:border-box} html,body{margin:0;height:100%}
body{font:16px/1.5 "Iowan Old Style",Georgia,"Times New Roman",serif;color:var(--tinta);background:#cfccc4}
.fone{max-width:430px;margin:0 auto;height:860px;background:var(--papel);position:relative;overflow:hidden;display:flex;flex-direction:column}
.sbar{display:flex;justify-content:space-between;align-items:center;padding:8px 16px 4px;font:600 12px system-ui;color:#333}
/* ===== HOME ESTILO KINDLE ===== */
.search{margin:6px 14px 2px;display:flex;align-items:center;gap:8px;background:#fff;border:1px solid var(--linha);border-radius:999px;padding:10px 16px;color:var(--suave);font:400 15px system-ui}
.scroll{flex:1;overflow-y:auto;padding:4px 14px 70px}
.sec{font:700 15px system-ui;margin:16px 2px 8px;display:flex;align-items:center;gap:6px}
.sec .mais{margin-left:auto;color:var(--suave);font-weight:400;font-size:13px}
.retomar{display:grid;grid-template-columns:1fr 1fr;gap:10px}
.rcard{background:var(--cartao);border:1px solid var(--linha);border-radius:12px;padding:10px;display:flex;gap:10px;cursor:pointer}
.rcap{width:38px;height:52px;border-radius:4px;background:linear-gradient(135deg,#3a3a3a,#111);color:#fff;font:800 13px system-ui;display:flex;align-items:center;justify-content:center;flex:none}
.rcard .tt{font:700 13px system-ui;line-height:1.2}
.rcard .au{font:400 11px system-ui;color:var(--suave);margin-top:2px}
.rbar{height:4px;background:var(--progoff);border-radius:3px;margin-top:8px;overflow:hidden}
.rbar>i{display:block;height:100%;background:var(--prog)}
.estante{display:grid;grid-template-columns:repeat(3,1fr);gap:12px}
.cap{cursor:pointer}
.capimg{aspect-ratio:3/4;border-radius:6px;background:linear-gradient(160deg,#4a4a4a,#1a1a1a);color:#fff;position:relative;display:flex;flex-direction:column;justify-content:space-between;padding:10px;box-shadow:0 3px 10px rgba(0,0,0,.18)}
.capimg .sig{font:800 26px Georgia,serif}
.capimg .nm{font:600 11px system-ui;opacity:.92;line-height:1.15}
.capimg .pc{position:absolute;top:8px;right:8px;background:#fff;color:#111;border-radius:999px;font:700 10px system-ui;padding:2px 7px}
.cap .leg{font:400 11px system-ui;color:var(--suave);margin-top:5px;text-align:center}
.cta{margin:14px 0 2px;background:var(--barra);color:#fff;border:0;border-radius:12px;padding:14px;width:100%;font:700 15px system-ui;cursor:pointer;display:flex;align-items:center;justify-content:center;gap:8px}
/* barra inferior */
.nav{position:absolute;left:0;right:0;bottom:0;display:flex;background:var(--papel);border-top:1px solid var(--linha)}
.nav button{flex:1;border:0;background:none;padding:10px 4px 12px;font:600 11px system-ui;color:var(--suave);cursor:pointer;display:flex;flex-direction:column;align-items:center;gap:3px}
.nav button.on{color:#111}
.nav .ic{font-size:17px}
.nav .un{height:2px;width:22px;background:#111;border-radius:2px;margin-top:2px}
/* ===== STORIES ===== */
.stage{position:absolute;inset:0;background:#111;color:#fff;display:none;flex-direction:column;z-index:20}
.stage.on{display:flex}
.segs{display:flex;gap:4px;padding:12px 12px 6px}
.seg{flex:1;height:3px;background:rgba(255,255,255,.3);border-radius:3px;overflow:hidden}
.seg>i{display:block;height:100%;width:0;background:#fff}
.seg.done>i{width:100%}
.seg.cur>i{width:100%}
.shead{display:flex;align-items:center;gap:10px;padding:4px 16px 0}
.schip{background:rgba(255,255,255,.16);border-radius:999px;padding:4px 12px;font:800 13px system-ui}
.srub{font:400 13px system-ui;opacity:.85}
.sclose{margin-left:auto;background:none;border:0;color:#fff;font-size:22px;cursor:pointer;line-height:1}
.sbody{flex:1;display:flex;flex-direction:column;justify-content:center;padding:24px 28px;gap:4px;text-align:left}
.sart{font:700 13px system-ui;opacity:.6;letter-spacing:.08em;text-transform:uppercase;margin-bottom:10px}
.stext{font:500 26px/1.5 "Iowan Old Style",Georgia,serif}
.pill{display:inline-block;background:#fff;color:#111;border-radius:8px;padding:1px 10px;font-weight:800}
.pill.hid{color:transparent;background:rgba(255,255,255,.28);user-select:none;min-width:90px}
.shint{position:absolute;bottom:26px;left:0;right:0;text-align:center;font:600 13px system-ui;opacity:.7}
.taps{position:absolute;inset:44px 0 0;display:flex}
.taps .z{flex:1}
.taps .z.r{flex:2}
.sdone{text-align:center;padding:0 30px}
.sdone .big{font:800 30px system-ui;margin-bottom:8px}
.sdone .bt{margin-top:18px;background:#fff;color:#111;border:0;border-radius:10px;padding:12px 20px;font:700 15px system-ui;cursor:pointer}
</style></head><body>
<div class="fone">
  <!-- HOME -->
  <div class="sbar"><span>15:40</span><span>✈ 38% ▍</span></div>
  <div class="search">🔎 Pesquisar na trilha…</div>
  <div class="scroll">
    <div class="sec">Retomar</div>
    <div class="retomar" id="retomar"></div>
    <div class="sec">Biblioteca <span class="mais">tudo ›</span></div>
    <div class="estante" id="estante"></div>
    <button class="cta" data-stories="CF">▶ Treinar em Stories — Constituição</button>
  </div>
  <div class="nav">
    <button class="on"><span class="ic">🏠</span>Início<span class="un"></span></button>
    <button><span class="ic">📚</span>Biblioteca</button>
    <button data-stories="CF"><span class="ic">▶</span>Treinar</button>
    <button><span class="ic">⋯</span>Mais</button>
  </div>
  <!-- STORIES -->
  <div class="stage" id="stage">
    <div class="segs" id="segs"></div>
    <div class="shead"><span class="schip" id="schip">CF</span><span class="srub" id="srub"></span><button class="sclose" data-close="1">✕</button></div>
    <div class="sbody" id="sbody"></div>
    <div class="shint" id="shint">toque à direita para revelar ›</div>
    <div class="taps"><div class="z l" data-tap="prev"></div><div class="z r" data-tap="next"></div></div>
  </div>
</div>
<script>
var D=${dados};
var esc=function(s){return String(s).replace(/[&<>]/g,function(c){return{'&':'&amp;','<':'&lt;','>':'&gt;'}[c]});};
// HOME
(function(){
  document.getElementById('retomar').innerHTML=D.retomar.map(function(r){
    return '<div class="rcard" data-stories="'+r.dip+'"><div class="rcap">'+r.dip+'</div><div><div class="tt">Art. '+r.art+'</div>'
      +'<div class="au">'+esc(r.rub)+'</div><div class="rbar"><i style="width:'+r.pct+'%"></i></div></div></div>';
  }).join('');
  document.getElementById('estante').innerHTML=D.diplomas.map(function(d){
    return '<div class="cap" data-stories="'+d.sigla+'"><div class="capimg"><span class="pc">'+d.pct+'%</span>'
      +'<span class="sig">'+d.sigla+'</span><span class="nm">'+esc(d.nome)+'</span></div>'
      +'<div class="leg">'+d.arts+' artigos</div></div>';
  }).join('');
})();
// STORIES
var segs=[], idx=0, revelado=false, dipAtual='CF';
function abrirStories(dip){
  dipAtual=dip; segs=(D.stories[dip]||D.stories.CF); idx=0; revelado=false;
  document.getElementById('schip').textContent=dip;
  document.getElementById('segs').innerHTML=segs.map(function(_,i){return '<div class="seg" id="seg'+i+'"><i></i></div>';}).join('');
  document.getElementById('stage').classList.add('on');
  pinta();
}
function pinta(){
  if(idx>=segs.length){ // resumo final
    document.getElementById('srub').textContent='';
    document.getElementById('sbody').innerHTML='<div class="sdone"><div class="big">🎉 Fim do bloco</div>'
      +'<div>Você passou por '+segs.length+' pontos de '+dipAtual+'.</div>'
      +'<button class="bt" data-restart="1">↺ Rever de novo</button></div>';
    document.getElementById('shint').style.display='none';
    segs.forEach(function(_,i){var s=document.getElementById('seg'+i);if(s)s.className='seg done';});
    return;
  }
  document.getElementById('shint').style.display='';
  var s=segs[idx];
  document.getElementById('srub').textContent=s.rub;
  document.getElementById('shint').textContent=revelado?'toque à direita para continuar ›':'toque à direita para revelar ›';
  var pill=revelado?'<span class="pill">'+esc(s.gap)+'</span>':'<span class="pill hid">'+esc(s.gap)+'</span>';
  document.getElementById('sbody').innerHTML='<div class="sart">'+dipAtual+' · Art. '+esc(s.art)+'</div>'
    +'<div class="stext">'+esc(s.ante)+' '+pill+(s.dep?(' '+esc(s.dep)):'')+'</div>';
  for(var i=0;i<segs.length;i++){var el=document.getElementById('seg'+i);if(el)el.className='seg'+(i<idx?' done':(i===idx?' cur':''));}
}
function next(){ if(idx>=segs.length)return; if(!revelado){revelado=true;pinta();return;} idx++; revelado=false; pinta(); }
function prev(){ if(revelado){revelado=false;pinta();return;} if(idx>0){idx--;revelado=true;pinta();} }
document.addEventListener('click',function(e){
  var o=e.target.closest('[data-stories]'); if(o){abrirStories(o.getAttribute('data-stories'));return;}
  if(e.target.closest('[data-close]')){document.getElementById('stage').classList.remove('on');return;}
  if(e.target.closest('[data-restart]')){idx=0;revelado=false;pinta();return;}
  var t=e.target.closest('[data-tap]'); if(t){ t.getAttribute('data-tap')==='next'?next():prev(); return; }
});
${view0==='stories'?"abrirStories('CF');":""}
${sai}
</body></html>`;
}

function moldura(srcdoc, width) {
  const wrap = document.createElement('div');
  wrap.style.cssText = 'padding:16px;background:#e9e9e9';
  const frame = document.createElement('iframe');
  frame.title = 'Kindle + Stories — protótipo';
  frame.style.cssText = `width:${width};height:900px;border:0;background:#cfccc4;box-shadow:0 4px 24px rgba(0,0,0,.15)`;
  frame.srcdoc = srcdoc;
  wrap.appendChild(frame);
  return wrap;
}

export default {
  title: 'Aguardando Análise/Kindle + Stories (protótipo)',
  argTypes: { width: { control: 'select', options: ['430px', '100%', '390px'] } },
  args: { width: '430px' },
};

export const InicioKindle = {
  name: '🏠 Início estilo Kindle (Retomar + Biblioteca)',
  render: ({ width }) => moldura(pagina('home'), width),
};
export const ModoStories = {
  name: '▶ Modo Stories (estudo da lei, pegada Instagram)',
  render: ({ width }) => moldura(pagina('stories'), width),
};
