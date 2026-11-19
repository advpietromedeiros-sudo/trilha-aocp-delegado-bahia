// Protótipo "Lei na Íntegra" (19/11/2026, pedido do titular): um terceiro jeito de estudar a letra de lei no Treino
// de Letra de Lei — o ARTIGO INTEIRO (caput + incisos + parágrafos) com 3 modos de estudo, saindo todos do MESMO
// registro de dados. Esta story é só o VISUAL para aprovação (HARNESS: mockup se apresenta no Storybook). Nada de
// terceiro entra: a letra de lei é oficial/pública, o método (esconder-lembrar, modos, mnemônico) é técnica de estudo.
//
// Modelo de dados proposto (um registro por artigo; as palavras-chave vêm marcadas com {chaves}):
//   {d, art, titulo, rub, caput, incisos:[{n,t,imp,destaque}], paragrafos:[{rot,t}], mnem, base}
// Dos 3 modos: Esconder oculta os {}; Teste revela um {} por vez; Revisão apaga o secundário e grifa os {}.

const ARTIGO = {
  d: 'CF', art: '1º', titulo: 'DOS PRINCÍPIOS FUNDAMENTAIS', rub: 'Fundamentos da República',
  caput: 'A República Federativa do Brasil, formada pela {união indissolúvel dos Estados e Municípios e do Distrito Federal}, constitui-se em {Estado Democrático de Direito} e tem como fundamentos:',
  incisos: [
    { n: 'I', t: 'a {soberania}', imp: true },
    { n: 'II', t: 'a {cidadania}', imp: true },
    { n: 'III', t: 'a {dignidade da pessoa humana}', imp: true, destaque: true },
    { n: 'IV', t: 'os {valores sociais do trabalho e da livre iniciativa}' },
    { n: 'V', t: 'o {pluralismo político}' },
  ],
  paragrafos: [
    { rot: 'Parágrafo único.', t: 'Todo o poder emana do {povo}, que o exerce por meio de representantes eleitos ou diretamente, nos termos desta Constituição.', imp: true },
  ],
  mnem: 'SO-CI-DI-VA-PLU',
  base: 'CF, art. 1º',
};

function pagina(modoInicial) {
  const sai = '</' + 'script>';
  const dados = JSON.stringify(ARTIGO);
  return `<!doctype html><html lang="pt-BR"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<style>
:root{
  --tinta:#15223a; --fundo:#fff; --azul:#1e56c8; --amarelo:#ffe86b; --amarelo-bd:#f2c200;
  --ciano:#5fe0df; --vermelho:#d62828; --vermelho-bg:#fdeaea; --caixa:#c9ced6; --caixa-bd:#aeb4bf;
  --apagado:#c2c7d0; --rosa:#ff4fa3; --rosa-bg:#ffe8f3; --foco:#ffb703; --barra:#101728;
}
*{box-sizing:border-box}
body{margin:0;background:#eef0f4;font:17px/1.62 system-ui,-apple-system,Segoe UI,Roboto,sans-serif;color:var(--tinta)}
.fone{max-width:430px;margin:0 auto;background:var(--fundo);min-height:100vh;padding:0 0 40px}
/* barra de modos */
.topo{position:sticky;top:0;background:var(--barra);color:#fff;padding:10px 12px;display:flex;gap:6px;align-items:center;z-index:5}
.modos{display:flex;gap:6px;flex:1}
.modo{flex:1;border:0;border-radius:999px;padding:9px 6px;font:700 13px system-ui,sans-serif;color:#cdd3e0;background:#263350;cursor:pointer;white-space:nowrap}
.modo.on{background:#fff;color:#101728}
.som{border:0;background:#263350;color:#fff;width:40px;height:40px;border-radius:999px;font-size:18px;cursor:pointer;flex:none}
.som.falando{background:var(--foco);color:#101728}
/* corpo */
.corpo{padding:18px 20px}
.titulo{color:var(--azul);font:800 15px system-ui,sans-serif;letter-spacing:.04em;text-align:center;margin:4px 0 16px}
.art{margin:0 0 12px;text-align:justify;hyphens:auto}
.art b.rot{font-weight:800}
.inc{display:flex;gap:8px;margin:9px 0;text-align:justify;hyphens:auto}
.inc .num{font-weight:800;flex:none;min-width:28px}
.bang{color:var(--vermelho);font-weight:900;flex:none;width:14px}
/* lacuna (modo esconder/teste) */
.lac{display:inline-block;min-width:54px;height:1.15em;vertical-align:-2px;background:var(--caixa);border-radius:5px;cursor:pointer;transition:.12s}
.lac.rev{background:transparent;color:var(--vermelho);font-weight:800;cursor:default;height:auto;vertical-align:baseline}
.lac.foco{outline:3px solid var(--foco);outline-offset:2px;background:#eef3ff}
/* grifo (modo revisão) */
.gr{background:var(--amarelo);border-radius:3px;padding:0 2px;box-shadow:0 0 0 1px var(--amarelo-bd) inset}
.gr.poder{background:var(--ciano)}
.apagado{color:var(--apagado)}
/* mnemônico */
.mnem{display:inline-flex;align-items:center;gap:8px;background:var(--rosa-bg);border-radius:999px;padding:7px 16px;margin:6px 0 2px;font-weight:800;color:#c01f74;letter-spacing:.06em}
.mnem small{color:#d98fbd;font-weight:700;letter-spacing:0}
.dica{margin:14px 20px 0;padding:10px 12px;background:#f4f6fa;border-radius:10px;color:#5a6373;font-size:13px}
.base{margin:16px 20px 0;color:#8a92a0;font-size:13px}
.hidden{display:none}
</style></head><body>
<div class="fone">
  <div class="topo">
    <div class="modos">
      <button class="modo" data-m="esconder">🙈 Esconder</button>
      <button class="modo" data-m="teste">🎯 Teste</button>
      <button class="modo" data-m="revisao">📖 Revisão</button>
    </div>
    <button class="som" id="som" title="Ouvir o artigo">🔊</button>
  </div>
  <div class="corpo" id="corpo"></div>
  <div class="dica" id="dica"></div>
  <div class="base" id="base"></div>
</div>
<script>
var A = ${dados};
var modo = ${JSON.stringify(modoInicial)};
var focoIdx = 0; // modo teste: qual lacuna está em foco
var esc = function(s){return String(s).replace(/[&<>]/g,function(c){return{'&':'&amp;','<':'&lt;','>':'&gt;'}[c]});};

// quebra um texto com {chaves} em partes {k:'t'|'gap', s:texto}
function partes(txt){
  var out=[], re=/\\{([^}]+)\\}/g, i=0, m;
  while((m=re.exec(txt))){ if(m.index>i) out.push({k:'t',s:txt.slice(i,m.index)}); out.push({k:'gap',s:m[1]}); i=m.index+m[0].length; }
  if(i<txt.length) out.push({k:'t',s:txt.slice(i)});
  return out;
}
// índice global de lacunas (para o modo teste)
var GAPS=[];
function montaTexto(txt, poder){
  var ps=partes(txt), h='';
  ps.forEach(function(p){
    if(p.k==='t'){ h+=esc(p.s); return; }
    if(modo==='revisao'){ h+='<span class="gr'+(poder?' poder':'')+'">'+esc(p.s)+'</span>'; return; }
    var gi=GAPS.length; GAPS.push(p.s);
    var cls='lac';
    if(modo==='teste'){ if(gi<focoIdx) cls+=' rev'; else if(gi===focoIdx) cls+=' foco'; }
    var w=Math.min(300,Math.max(54,p.s.length*9));
    var txtIn=(modo==='teste'&&gi<focoIdx)?esc(p.s):'';
    var st=(cls.indexOf('rev')<0)?(' style="width:'+w+'px"'):'';
    h+='<span class="'+cls+'" data-gi="'+gi+'"'+st+'>'+txtIn+'</span>';
  });
  return h;
}
function render(){
  GAPS=[];
  document.querySelectorAll('.modo').forEach(function(b){ b.classList.toggle('on', b.dataset.m===modo); });
  var h='<div class="titulo">'+esc(A.titulo)+'</div>';
  h+='<p class="art"><b class="rot">Art. '+esc(A.art)+'</b> '+montaTexto(A.caput)+'</p>';
  // mnemônico (só no modo revisão, como nas telas)
  if(modo==='revisao' && A.mnem) h+='<div class="mnem">🧠 '+esc(A.mnem)+' <small>mnemônico</small></div>';
  A.incisos.forEach(function(it){
    var apaga=(modo==='revisao' && !it.imp && !it.destaque);
    h+='<div class="inc'+(apaga?' apagado':'')+'">'
      +'<span class="bang">'+(it.imp||it.destaque?'!':'')+'</span>'
      +'<span class="num">'+esc(it.n)+' -</span>'
      +'<span>'+montaTexto(it.t)+'</span></div>';
  });
  (A.paragrafos||[]).forEach(function(pg){
    h+='<p class="art"><b class="rot">'+esc(pg.rot)+'</b> '+montaTexto(pg.t, true)+'</p>';
  });
  document.getElementById('corpo').innerHTML=h;
  var dica={esconder:'Toque em cada lacuna para revelar. Tente recitar antes.',
            teste:'Uma lacuna por vez. Toque na lacuna em foco (ou em qualquer parte) para avançar.',
            revisao:'O secundário fica apagado; o essencial, grifado. Use o mnemônico para fixar a ordem.'}[modo];
  document.getElementById('dica').textContent=dica;
  document.getElementById('base').textContent=A.base;
}
// interações
document.addEventListener('click', function(e){
  var mb=e.target.closest('.modo'); if(mb){ modo=mb.dataset.m; focoIdx=0; render(); return; }
  var lac=e.target.closest('.lac');
  if(lac && modo==='esconder'){ lac.classList.add('rev'); lac.textContent=GAPS[+lac.dataset.gi]; lac.style.width=''; return; }
  if(modo==='teste' && (lac || e.target.closest('.corpo'))){ if(focoIdx<GAPS.length){ focoIdx++; render(); } return; }
});
// áudio (Web Speech API nativo — sem dependência, sem terceiro)
document.getElementById('som').addEventListener('click', function(){
  var b=this;
  if(window.speechSynthesis && window.speechSynthesis.speaking){ window.speechSynthesis.cancel(); b.classList.remove('falando'); return; }
  if(!window.speechSynthesis){ b.textContent='🔇'; return; }
  var txt='Artigo 1º. '+A.caput.replace(/[{}]/g,'')+' '+A.incisos.map(function(i){return i.n+', '+i.t.replace(/[{}]/g,'');}).join('. ')+'. '+(A.paragrafos||[]).map(function(p){return p.rot+' '+p.t.replace(/[{}]/g,'');}).join(' ');
  var u=new SpeechSynthesisUtterance(txt); u.lang='pt-BR'; u.rate=.95;
  u.onend=function(){ b.classList.remove('falando'); };
  b.classList.add('falando'); window.speechSynthesis.speak(u);
});
render();
${sai}
</body></html>`;
}

function moldura(srcdoc, width) {
  const wrap = document.createElement('div');
  wrap.style.cssText = 'padding:16px;background:#e9e9e9';
  const frame = document.createElement('iframe');
  frame.title = 'Lei na Íntegra — protótipo';
  frame.allow = 'speaker';
  frame.style.cssText = `width:${width};height:720px;border:0;background:#eef0f4;box-shadow:0 4px 24px rgba(0,0,0,.15)`;
  frame.srcdoc = srcdoc;
  wrap.appendChild(frame);
  return wrap;
}

export default {
  title: 'Aguardando Análise/Lei na Íntegra (CF art. 1º)',
  argTypes: { width: { control: 'select', options: ['430px', '100%', '768px'] } },
  args: { width: '430px' },
};

export const Esconder = {
  name: '🙈 Esconder & lembrar',
  render: ({ width }) => moldura(pagina('esconder'), width),
};
export const Teste = {
  name: '🎯 Modo Teste (uma lacuna por vez)',
  render: ({ width }) => moldura(pagina('teste'), width),
};
export const Revisao = {
  name: '📖 Modo Revisão (apaga o secundário, grifa o essencial + mnemônico)',
  render: ({ width }) => moldura(pagina('revisao'), width),
};
