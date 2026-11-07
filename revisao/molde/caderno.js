/* Molde do caderno de revisão — Revisão Delegado PC-BA · Professor Pietro Medeiros.
   JS reaproveitado dos cadernos do próprio titular (apostilas-direito-penal/entregas, 05/11/2026):
   abas, índice, busca, temas, letra, zoom, foco, laser, quadro, cronômetro, slides, tela cheia e avatar.
   Acréscimos da revisão: pontos revisados (X de N), fichas C/E e questões A–E com memória,
   "Só o essencial", "Fichas que errei" e checklist marcável.
   A configuração do módulo chega em window.REV_CFG (injetada pelo gerador). */
(function(){
'use strict';
var CFG=window.REV_CFG||{};
var PFX=CFG.pfx||'rev_pcba_';
var mem={};
function sget(k){try{return window.localStorage.getItem(k);}catch(e){return mem.hasOwnProperty(k)?mem[k]:null;}}
function sset(k,v){try{window.localStorage.setItem(k,v);}catch(e){mem[k]=v;}}
function $(id){return document.getElementById(id);}
function qa(s,root){return Array.prototype.slice.call((root||document).querySelectorAll(s));}

/* ---------- Modal (substitui alert) ---------- */
function showModal(title,msg){
  $('modalTitle').textContent=title;$('modalMsg').textContent=msg;$('modalBg').className='modal-bg on';
}
$('modalOk').onclick=function(){$('modalBg').className='modal-bg';};

/* ---------- Abas ---------- */
var activeTab='conteudo';
function switchTab(name){
  activeTab=name;
  qa('.tab').forEach(function(t){t.className='tab'+(t.getAttribute('data-tab')===name?' active':'');});
  qa('.panel').forEach(function(p){p.className='panel'+(p.id==='panel-'+name?' active':'');});
  sset(PFX+'tab',name);
  window.scrollTo(0,0);
}
qa('.tab').forEach(function(t){t.onclick=function(){switchTab(t.getAttribute('data-tab'));};});
var savedTab=sget(PFX+'tab');if(savedTab&&$('panel-'+savedTab))switchTab(savedTab);

/* ---------- Progresso de leitura ---------- */
window.addEventListener('scroll',function(){
  var h=document.documentElement;var max=h.scrollHeight-h.clientHeight;
  $('progressBar').style.width=(max>0?(h.scrollTop/max*100):0)+'%';
  highlightToc();
});

/* ---------- Destaque do índice ---------- */
var tocTick=null;
function highlightToc(){
  if(tocTick)return;
  tocTick=setTimeout(function(){
    tocTick=null;
    var panel=$('panel-'+activeTab);if(!panel)return;
    var links=qa('.toc-links a',panel);var cur=null;
    for(var i=0;i<links.length;i++){
      var id=links[i].getAttribute('href').slice(1);var el=$(id);
      if(el&&el.getBoundingClientRect().top<160)cur=links[i];
    }
    links.forEach(function(l){l.classList.remove('current');});
    if(cur)cur.classList.add('current');
  },80);
}

/* ---------- Busca no índice ---------- */
qa('.toc-search').forEach(function(inp){
  inp.oninput=function(){
    var v=inp.value.toLowerCase();var nav=inp.parentNode;
    qa('.toc-links a',nav).forEach(function(a){a.style.display=(!v||a.textContent.toLowerCase().indexOf(v)>-1)?'':'none';});
    qa('.toc-group',nav).forEach(function(g){if(v)g.open=true;});
  };
});

/* ---------- Pontos revisados (X de N) ---------- */
function refreshDone(){
  var total=0,done=0;
  qa('#panel-conteudo .card[data-ponto]').forEach(function(c){
    total++;var d=sget(PFX+'revisado_'+c.id)==='1';
    if(d)done++;
    c.classList.toggle('done',d);
    var b=c.querySelector('.done-btn');if(b)b.textContent=d?'✓ revisado':'marcar revisado';
    qa('a[href="#'+c.id+'"]').forEach(function(l){l.classList.toggle('done',d);});
  });
  var txt=done+' de '+total+' pontos';
  $('studyCount').textContent=txt;
  if($('revProg'))$('revProg').textContent='✔ '+txt+' revisados';
  if($('revBarra'))$('revBarra').style.width=(total?done/total*100:0)+'%';
}
qa('#panel-conteudo .card[data-ponto]').forEach(function(c){
  var b=document.createElement('button');b.className='done-btn';b.type='button';
  b.onclick=function(){var k=PFX+'revisado_'+c.id;sset(k,sget(k)==='1'?'':'1');refreshDone();};
  c.insertBefore(b,c.firstChild);
});
refreshDone();

/* ---------- Fichas C/E e questões A–E (com memória do resultado) ---------- */
var score={ok:0,no:0};
function updScore(){$('quizScore').textContent='Fichas: '+score.ok+' ✓ · '+score.no+' ✗';}
function revela(q){var a=q.querySelector('.quiz-answer');if(a)a.classList.add('show');}
window.revealQuiz=function(id){var q=document.querySelector('.quiz-card[data-id="'+id+'"]');if(q)revela(q);};
function registra(q,ok){
  q.setAttribute('data-done','1');q.setAttribute('data-res',ok?'ok':'no');
  if(ok)score.ok++;else score.no++;
  sset(PFX+'ficha_'+q.getAttribute('data-id'),ok?'ok':'no');
  updScore();revela(q);
}
function montaCE(q){
  var ans=q.getAttribute('data-ans');
  var btns=document.createElement('div');btns.className='quiz-btns';
  ['C','E'].forEach(function(op){
    var b=document.createElement('button');b.type='button';b.className='quiz-btn';b.setAttribute('data-op',op);b.textContent=op==='C'?'CERTO':'ERRADO';
    b.onclick=function(){
      if(q.getAttribute('data-done'))return;
      var ok=op===ans;b.className='quiz-btn '+(ok?'right':'wrong');registra(q,ok);
    };
    btns.appendChild(b);
  });
  var st=q.querySelector('.quiz-statement');st.parentNode.insertBefore(btns,st.nextSibling);
}
function montaMC(q){
  var ans=q.getAttribute('data-ans');
  qa('.mc-btn',q).forEach(function(b){
    b.onclick=function(){
      if(q.getAttribute('data-done'))return;
      var ok=b.getAttribute('data-op')===ans;
      b.classList.add(ok?'right':'wrong');
      var g=q.querySelector('.mc-btn[data-op="'+ans+'"]');if(g)g.classList.add('gab');
      qa('.mc-btn',q).forEach(function(x){x.disabled=true;});
      registra(q,ok);
    };
  });
}
function zeraCard(q){
  q.removeAttribute('data-done');q.removeAttribute('data-res');
  var a=q.querySelector('.quiz-answer');if(a)a.classList.remove('show');
  qa('.quiz-btn',q).forEach(function(b){b.className='quiz-btn';});
  qa('.mc-btn',q).forEach(function(b){b.classList.remove('right','wrong','gab');b.disabled=false;});
}
qa('.quiz-card').forEach(function(q){
  if(q.getAttribute('data-tipo')==='mc')montaMC(q);else montaCE(q);
  var r=sget(PFX+'ficha_'+q.getAttribute('data-id'));
  if(r==='ok'||r==='no'){q.setAttribute('data-res',r);}
});
updScore();

/* ---------- Só o essencial ---------- */
function aplicaEssencial(on){
  document.body.classList.toggle('essencial',on);
  qa('.js-essencial').forEach(function(b){b.classList.toggle('on',on);b.setAttribute('aria-pressed',on?'true':'false');});
  sset(PFX+'essencial',on?'1':'');
}
qa('.js-essencial').forEach(function(b){b.onclick=function(){aplicaEssencial(!document.body.classList.contains('essencial'));};});
aplicaEssencial(sget(PFX+'essencial')==='1');

/* ---------- Fichas que errei ---------- */
function saiErros(){
  document.body.classList.remove('so-erros');
  qa('.js-erros').forEach(function(b){b.classList.remove('on');b.setAttribute('aria-pressed','false');});
  qa('.quiz-card.errei').forEach(function(q){q.classList.remove('errei');});
  qa('.card.tem-erro').forEach(function(c){c.classList.remove('tem-erro');});
}
function entraErros(){
  var erradas=qa('#panel-conteudo .quiz-card').filter(function(q){return sget(PFX+'ficha_'+q.getAttribute('data-id'))==='no';});
  if(!erradas.length){showModal('Fichas que errei','Nenhuma ficha errada guardada neste aparelho. Responda as fichas do módulo; as que você errar voltam aqui.');return;}
  if(activeTab!=='conteudo')switchTab('conteudo');
  erradas.forEach(function(q){zeraCard(q);q.classList.add('errei');var c=q.closest('.card');if(c)c.classList.add('tem-erro');});
  document.body.classList.add('so-erros');
  qa('.js-erros').forEach(function(b){b.classList.add('on');b.setAttribute('aria-pressed','true');});
  if($('errosN'))$('errosN').textContent=String(erradas.length);
  var p=erradas[0].closest('.card');if(p)p.scrollIntoView({block:'start'});
}
qa('.js-erros').forEach(function(b){b.onclick=function(){if(document.body.classList.contains('so-erros'))saiErros();else entraErros();};});
if($('errosSair'))$('errosSair').onclick=saiErros;

/* ---------- Checklist marcável ---------- */
qa('.checklist[data-ck] li').forEach(function(li,i){
  var k=PFX+'ck_'+li.parentNode.getAttribute('data-ck')+'_'+i;
  if(sget(k)==='1')li.classList.add('ok');
  li.setAttribute('role','checkbox');li.setAttribute('tabindex','0');
  li.setAttribute('aria-checked',li.classList.contains('ok')?'true':'false');
  function alterna(){var on=!li.classList.contains('ok');li.classList.toggle('ok',on);li.setAttribute('aria-checked',on?'true':'false');sset(k,on?'1':'');}
  li.onclick=alterna;li.onkeydown=function(e){if(e.key===' '||e.key==='Enter'){e.preventDefault();alterna();}};
});

/* ---------- Busca na lei seca ---------- */
var lsInput=$('lsSearch');
if(lsInput){
  var lsTimer=null;
  lsInput.oninput=function(){clearTimeout(lsTimer);lsTimer=setTimeout(runLs,180);};
}
function stripMarks(el){qa('mark.ls-hit',el).forEach(function(m){m.outerHTML=m.innerHTML;});}
function runLs(){
  var v=lsInput.value.trim().toLowerCase();var groups=qa('#lsContent .ls-art-group');var n=0;
  groups.forEach(function(g){
    stripMarks(g);
    if(!v){g.classList.remove('hidden-by-search');return;}
    var txt=g.textContent.toLowerCase();
    if(txt.indexOf(v)>-1){
      n++;g.classList.remove('hidden-by-search');
      qa('p,.ls-art-name',g).forEach(function(p){
        var re=new RegExp('('+v.replace(/[.*+?^${}()|[\]\\]/g,'\\$&')+')','gi');
        p.innerHTML=p.innerHTML.replace(/(<[^>]+>)|([^<]+)/g,function(m,tag,text){return tag?tag:text.replace(re,'<mark class="ls-hit">$1</mark>');});
      });
    }else g.classList.add('hidden-by-search');
  });
  qa('#lsContent .ls-titulo,#lsContent .ls-capitulo').forEach(function(h){h.style.display=v?'none':'';});
  $('lsCount').textContent=v?(n+' dispositivo(s) encontrado(s)'):'';
}

/* ---------- Temas ---------- */
var THEMES={
 classico:{n:'🖊️ Caneta Azul & Preta · Padrão',v:{bg2:'#f4f5f7',panel2:'#f8f9fb',gold:'#1f4fb4','gold-bright':'#173c8a','gold-dim':'#8fb0e8',ink:'#1b1b1f','ink-dim':'#3d3f47','ink-faint':'#7d808a',line:'rgba(27,27,31,.18)',red:'#c62828',green:'#2e7d32',teal:'#00796b',orange:'#e65100',blue:'#1f4fb4',hl:'#e9ff3b',rule:'rgba(90,130,200,.24)',margin:'rgba(31,79,180,.35)',spiral:'#9aa0aa','paper-white':'#ffffff','ink-on-gold':'#ffffff',bg:'#e9eaee',panel:'#fffefb','bg-trans':'rgba(233,234,238,.94)'}},
 creme:{n:'📒 Papel Creme',v:{bg2:'#f4f5f7',panel2:'#f8f9fb',gold:'#1f4fb4','gold-bright':'#173c8a','gold-dim':'#8fb0e8',ink:'#1b1b1f','ink-dim':'#3d3f47','ink-faint':'#7d808a',line:'rgba(27,27,31,.18)',red:'#c62828',green:'#2e7d32',teal:'#00796b',orange:'#e65100',blue:'#1f4fb4',hl:'#e9ff3b',rule:'rgba(90,130,200,.24)',margin:'rgba(31,79,180,.35)',spiral:'#9aa0aa','paper-white':'#ffffff','ink-on-gold':'#ffffff',bg:'#e7e1d6',panel:'#fdf8ec','bg-trans':'rgba(231,225,214,.94)',bg2:'#f5f0e4',panel2:'#f8f2e4'}},
 reciclado:{n:'♻️ Papel Reciclado',v:{bg2:'#f4f5f7',panel2:'#f8f9fb',gold:'#1f4fb4','gold-bright':'#173c8a','gold-dim':'#8fb0e8',ink:'#1b1b1f','ink-dim':'#3d3f47','ink-faint':'#7d808a',line:'rgba(27,27,31,.18)',red:'#c62828',green:'#2e7d32',teal:'#00796b',orange:'#e65100',blue:'#1f4fb4',hl:'#e9ff3b',rule:'rgba(90,130,200,.24)',margin:'rgba(31,79,180,.35)',spiral:'#9aa0aa','paper-white':'#ffffff','ink-on-gold':'#ffffff',bg:'#d9d6cf',panel:'#efebe2','bg-trans':'rgba(217,214,207,.94)',bg2:'#e9e5dc',panel2:'#ebe6dc'}},
 azulado:{n:'💧 Papel Azulado',v:{bg2:'#f4f5f7',panel2:'#f8f9fb',gold:'#1f4fb4','gold-bright':'#173c8a','gold-dim':'#8fb0e8',ink:'#1b1b1f','ink-dim':'#3d3f47','ink-faint':'#7d808a',line:'rgba(27,27,31,.18)',red:'#c62828',green:'#2e7d32',teal:'#00796b',orange:'#e65100',blue:'#1f4fb4',hl:'#e9ff3b',rule:'rgba(90,130,200,.24)',margin:'rgba(31,79,180,.35)',spiral:'#9aa0aa','paper-white':'#ffffff','ink-on-gold':'#ffffff',bg:'#dde6f2',panel:'#f6f9ff','bg-trans':'rgba(221,230,242,.94)',bg2:'#eef3fa',panel2:'#eef3fb'}},
 kraft:{n:'📦 Papel Kraft',v:{bg2:'#f4f5f7',panel2:'#f8f9fb',gold:'#1f4fb4','gold-bright':'#173c8a','gold-dim':'#8fb0e8',ink:'#1b1b1f','ink-dim':'#3d3f47','ink-faint':'#7d808a',line:'rgba(27,27,31,.18)',red:'#c62828',green:'#2e7d32',teal:'#00796b',orange:'#e65100',blue:'#1f4fb4',hl:'#e9ff3b',rule:'rgba(90,130,200,.24)',margin:'rgba(31,79,180,.35)',spiral:'#9aa0aa','paper-white':'#ffffff','ink-on-gold':'#ffffff',bg:'#5b4636',panel:'#e4d0ad','bg-trans':'rgba(91,70,54,.95)',bg2:'#d8c3a0',panel2:'#dcc6a0',ink:'#1e1710','ink-dim':'#3e3022','ink-faint':'#6e5b48',gold:'#1d3f80','gold-bright':'#132c5c',rule:'rgba(80,55,30,.18)',spiral:'#2a1d12','paper-white':'#fbf6ea'}},
 lousa:{n:'🖍️ Lousa · Projetor',v:{bg2:'#f4f5f7',panel2:'#f8f9fb',gold:'#1f4fb4','gold-bright':'#173c8a','gold-dim':'#8fb0e8',ink:'#1b1b1f','ink-dim':'#3d3f47','ink-faint':'#7d808a',line:'rgba(27,27,31,.18)',red:'#c62828',green:'#2e7d32',teal:'#00796b',orange:'#e65100',blue:'#1f4fb4',hl:'#e9ff3b',rule:'rgba(90,130,200,.24)',margin:'rgba(31,79,180,.35)',spiral:'#9aa0aa','paper-white':'#ffffff','ink-on-gold':'#ffffff',bg:'#0f1714',panel:'#1d2a25','bg-trans':'rgba(15,23,20,.95)',bg2:'#16211d',panel2:'#22322c',gold:'#8ec5ff','gold-bright':'#b9dbff','gold-dim':'#4f7aa6',ink:'#f2f0e6','ink-dim':'#cfd6cf','ink-faint':'#8fa097',line:'rgba(242,240,230,.2)',red:'#ff8a80',green:'#a5d6a7',teal:'#80deea',orange:'#ffcc80',blue:'#90caf9',hl:'rgba(233,255,59,.32)',rule:'rgba(255,255,255,.06)',margin:'rgba(142,197,255,.3)',spiral:'#8fa097','paper-white':'#fbfaf3','ink-on-gold':'#1d2a25'}},
 contraste:{n:'⬛ Alto Contraste',v:{bg2:'#f4f5f7',panel2:'#f8f9fb',gold:'#1f4fb4','gold-bright':'#173c8a','gold-dim':'#8fb0e8',ink:'#1b1b1f','ink-dim':'#3d3f47','ink-faint':'#7d808a',line:'rgba(27,27,31,.18)',red:'#c62828',green:'#2e7d32',teal:'#00796b',orange:'#e65100',blue:'#1f4fb4',hl:'#e9ff3b',rule:'rgba(90,130,200,.24)',margin:'rgba(31,79,180,.35)',spiral:'#9aa0aa','paper-white':'#ffffff','ink-on-gold':'#ffffff',bg:'#d9d9d9',panel:'#ffffff','bg-trans':'rgba(217,217,217,.96)',ink:'#000000','ink-dim':'#111111','ink-faint':'#444444',gold:'#0b3a99','gold-bright':'#062766',line:'rgba(0,0,0,.35)',hl:'#ffff00',rule:'rgba(0,0,0,.14)',spiral:'#000000'}}
};
function hexToRgba(h,a){if(h.charAt(0)!=='#')return h;var n=parseInt(h.slice(1),16);return 'rgba('+((n>>16)&255)+','+((n>>8)&255)+','+(n&255)+','+a+')';}
function applyTheme(k){
  var t=THEMES[k]||THEMES.classico;var r=document.documentElement.style;
  for(var key in t.v){if(t.v.hasOwnProperty(key))r.setProperty('--'+key,t.v[key]);}
  ['red','green','teal','orange','blue'].forEach(function(c){r.setProperty('--'+c+'-bg',hexToRgba(t.v[c],.1));r.setProperty('--'+c+'-line',hexToRgba(t.v[c],.38));});
  sset('cad_pen_theme2',k);
  qa('.theme-opt').forEach(function(o){o.classList.toggle('on',o.getAttribute('data-k')===k);});
}
var pop=$('themePop');
Object.keys(THEMES).forEach(function(k){
  var b=document.createElement('button');b.className='theme-opt';b.type='button';b.setAttribute('data-k',k);b.textContent=THEMES[k].n;
  b.onclick=function(){applyTheme(k);pop.className='theme-pop';};pop.appendChild(b);
});
function toggleThemePop(){pop.className=pop.className.indexOf('on')>-1?'theme-pop':'theme-pop on';}
$('themeBtn').onclick=toggleThemePop;$('tbTheme').onclick=toggleThemePop;
applyTheme(sget('cad_pen_theme2')||'classico');
/* ---------- Letra de caderno × letra de forma ---------- */
function applyFont(f){document.body.classList.toggle('forma',f==='forma');$('tbFont').textContent=f==='forma'?'🔤 Letra redonda':'✍️ Letra de caderno';sset('cad_pen_font',f);}
$('tbFont').onclick=function(){applyFont(document.body.classList.contains('forma')?'hand':'forma');};
applyFont(sget('cad_pen_font')||'hand');

/* ---------- Zoom (CSS zoom real) ---------- */
var TB={zoom:100,timer:null,remain:0,total:0,up:false};
function applyZoom(v){
  TB.zoom=Math.max(70,Math.min(180,v));var f=TB.zoom/100;
  qa('.panel main').forEach(function(m){m.style.zoom=f;});
  $('zoomDisplay').textContent=TB.zoom+'%';$('zoomSlider').value=TB.zoom;sset('da2_zoom',String(TB.zoom));
}
$('zoomIn').onclick=function(){applyZoom(TB.zoom+10);};
$('zoomOut').onclick=function(){applyZoom(TB.zoom-10);};
$('zoomSlider').oninput=function(){applyZoom(parseInt(this.value,10));};
applyZoom(parseInt(sget('da2_zoom')||'100',10));

/* ---------- Foco ---------- */
function toggleFocus(){document.body.classList.toggle('focus');$('tbFocus').classList.toggle('on',document.body.classList.contains('focus'));}
$('tbFocus').onclick=toggleFocus;

/* ---------- Laser ---------- */
function toggleLaser(force){
  var on=typeof force==='boolean'?force:!document.body.classList.contains('laser');
  document.body.classList.toggle('laser',on);$('tbLaser').classList.toggle('on',on);
}
$('tbLaser').onclick=function(){toggleLaser();};
document.addEventListener('mousemove',function(e){
  if(!document.body.classList.contains('laser'))return;
  var c=$('laserCursor');c.style.left=e.clientX+'px';c.style.top=e.clientY+'px';
  var o=$('laserOverlay');o.style.setProperty('--lx',e.clientX+'px');o.style.setProperty('--ly',e.clientY+'px');
});

/* ---------- Quadro ---------- */
function toggleQuadro(){
  var q=$('quadroOverlay');var on=q.className.indexOf('on')<0;
  q.className='quadro-overlay'+(on?' on':'');if(on)toggleLaser(false);$('tbQuadro').classList.toggle('on',on);
}
$('tbQuadro').onclick=toggleQuadro;$('quadroExit').onclick=toggleQuadro;

/* ---------- Timer ---------- */
function fmt(s){var m=Math.floor(Math.abs(s)/60),x=Math.abs(s)%60;return (m<10?'0':'')+m+':'+(x<10?'0':'')+x;}
function renderTimer(){
  var el=$('timerDisplay');el.className='tb-timer';
  if(TB.up){el.textContent=fmt(TB.remain);return;}
  el.textContent=fmt(TB.remain);
  if(TB.total>0){var r=TB.remain/TB.total;if(TB.remain<=0)el.className='tb-timer danger blink';else if(r<.1)el.className='tb-timer danger';else if(r<.33)el.className='tb-timer warn';}
}
function startTimer(){
  if(TB.timer)return;
  var p=parseInt($('timerPreset').value,10);
  if(TB.remain===0&&!TB.up){if(p>0){TB.total=p*60;TB.remain=TB.total;TB.up=false;}else{TB.up=true;TB.remain=0;TB.total=0;}}
  TB.timer=setInterval(function(){
    if(TB.up)TB.remain++;else{TB.remain--;if(TB.remain<=0){TB.remain=0;clearInterval(TB.timer);TB.timer=null;}}
    renderTimer();
  },1000);
  $('timerStart').textContent='⏸';
}
function pauseTimer(){clearInterval(TB.timer);TB.timer=null;$('timerStart').textContent='▶';}
$('timerStart').onclick=function(){if(TB.timer)pauseTimer();else startTimer();};
$('timerReset').onclick=function(){pauseTimer();TB.remain=0;TB.total=0;TB.up=false;renderTimer();};
$('timerPreset').onchange=function(){pauseTimer();var p=parseInt(this.value,10);TB.up=!(p>0);TB.total=p>0?p*60:0;TB.remain=TB.total;renderTimer();};
renderTimer();

/* ---------- Apresentação ---------- */
var SL={items:[],i:0};
function collectSlides(){var p=$('panel-'+activeTab);return qa('.hero,.card,.ls-art-group:not(.hidden-by-search)',p);}
function openSlides(){
  SL.items=collectSlides();if(!SL.items.length){showModal('Apresentação','Não há cards nesta aba.');return;}
  var start=0;
  for(var i=0;i<SL.items.length;i++){if(SL.items[i].getBoundingClientRect().top>-50){start=i;break;}}
  SL.i=start;$('slideOverlay').className='slide-overlay on';buildDots();renderSlide(false);
}
function closeSlides(){$('slideOverlay').className='slide-overlay';}
function buildDots(){
  var d=$('slideDots');d.innerHTML='';
  if(SL.items.length>30){d.style.display='none';return;}d.style.display='';
  SL.items.forEach(function(_,k){var i=document.createElement('i');i.onclick=function(){var b=k<SL.i;SL.i=k;renderSlide(b);};d.appendChild(i);});
}
function renderSlide(back){
  var st=$('slideStage');st.innerHTML='';
  var w=document.createElement('div');w.className='slide-inner'+(back?' back':'');
  var clone=SL.items[SL.i].cloneNode(true);clone.removeAttribute('id');
  qa('[id]',clone).forEach(function(n){n.setAttribute('data-oid',n.id);n.removeAttribute('id');});
  qa('.quiz-reveal-btn',clone).forEach(function(b){b.onclick=function(){var a=b.parentNode.querySelector('.quiz-answer');if(a)a.classList.add('show');};});
  qa('.quiz-btns',clone).forEach(function(bx){bx.parentNode.removeChild(bx);});
  w.appendChild(clone);st.appendChild(w);st.scrollTop=0;
  $('slideBar').style.width=((SL.i+1)/SL.items.length*100)+'%';
  $('slideCount').textContent=(SL.i+1)+' / '+SL.items.length;
  qa('#slideDots i').forEach(function(d,k){d.className=k===SL.i?'on':'';});
}
function nextSlide(){if(SL.i<SL.items.length-1){SL.i++;renderSlide(false);}}
function prevSlide(){if(SL.i>0){SL.i--;renderSlide(true);}}
$('tbSlides').onclick=openSlides;$('slidePrev').onclick=prevSlide;$('slideNext').onclick=nextSlide;$('slideClose').onclick=closeSlides;

/* ---------- Fullscreen ---------- */
function toggleFS(){
  var d=document,el=d.documentElement;
  if(!d.fullscreenElement&&!d.webkitFullscreenElement){(el.requestFullscreen||el.webkitRequestFullscreen||function(){}).call(el);}
  else{(d.exitFullscreen||d.webkitExitFullscreen||function(){}).call(d);}
}
$('tbFull').onclick=toggleFS;

/* ---------- Atalhos ---------- */
document.addEventListener('keydown',function(e){
  var tag=(e.target.tagName||'').toLowerCase();if(tag==='input'||tag==='textarea'||tag==='select')return;
  var slides=$('slideOverlay').className.indexOf('on')>-1;
  if(slides){
    if(e.key==='ArrowRight'||e.key===' '){e.preventDefault();nextSlide();return;}
    if(e.key==='ArrowLeft'){e.preventDefault();prevSlide();return;}
    if(e.key==='Escape'){closeSlides();return;}
    if(e.key==='f'||e.key==='F'){toggleFS();return;}
  }
  if(e.key==='+'||e.key==='='){applyZoom(TB.zoom+10);}
  else if(e.key==='-'){applyZoom(TB.zoom-10);}
  else if(e.key==='0'){applyZoom(100);}
  else if(e.key==='F9'){e.preventDefault();toggleFocus();}
  else if(e.key==='l'||e.key==='L'){toggleLaser();}
  else if(e.key==='q'||e.key==='Q'){toggleQuadro();}
  else if(e.key==='p'||e.key==='P'){openSlides();}
  else if(e.key==='Escape'){pop.className='theme-pop';$('modalBg').className='modal-bg';}
});


/* ---------- Professor Pietro Medeiros (avatar interativo) ---------- */
var AV_TIPS=CFG.dicas&&CFG.dicas.length?CFG.dicas:['Revise primeiro o que tem a maior prioridade: o índice do topo já está nessa ordem.'];
var AV_OK=['Acertou! 👏 Segue firme.','Isso mesmo! Esse ponto cai muito.','Perfeito. Leia o fundamento para fixar.'];
var AV_NO=['Quase! Leia o fundamento no verso da ficha.','Esse é dos traiçoeiros. Releia a lei seca do ponto.','Errar aqui é aprender antes da prova. Ela volta em “Fichas que errei”.'];
var AV_HI='Olá! Eu sou o <b>Professor Pietro Medeiros</b>. Clique em mim para uma dica ou peça para eu tomar a sua lição com uma ficha de certo ou errado.';
var avBtn=$('avBtn'),avBub=$('avBubble'),avTxt=$('avText'),avI=0,avT=null;
function avPick(a){return a[Math.floor(Math.random()*a.length)];}
function avSay(t,ms){avTxt.innerHTML=t;avBub.classList.add('on');avBtn.classList.remove('talk');void avBtn.offsetWidth;avBtn.classList.add('talk');clearTimeout(avT);if(ms)avT=setTimeout(avHide,ms);}
function avHide(){avBub.classList.remove('on');avBtn.classList.remove('talk');}
function avTip(){avSay(AV_TIPS[avI%AV_TIPS.length]);avI++;}
avBtn.onclick=function(){if(avBub.classList.contains('on'))avHide();else avTip();};
$('avNext').onclick=avTip;$('avClose').onclick=avHide;
$('avQuiz').onclick=function(){
  var qs=qa('#panel-conteudo .quiz-card:not([data-done])').filter(function(q){return q.offsetParent!==null||activeTab!=='conteudo';});
  if(!qs.length){avSay('Você já respondeu todas as fichas visíveis! Placar: '+score.ok+' acertos e '+score.no+' erros.');return;}
  if(activeTab!=='conteudo')switchTab('conteudo');
  var q=avPick(qs);q.scrollIntoView({behavior:'smooth',block:'center'});q.classList.add('pulse');
  setTimeout(function(){q.classList.remove('pulse');},2600);avSay('Responda esta ficha!',5000);
};
document.addEventListener('click',function(e){
  var b=e.target.closest?e.target.closest('.quiz-btn,.mc-btn'):null;if(!b)return;
  setTimeout(function(){if(b.classList.contains('right'))avSay(avPick(AV_OK),4500);else if(b.classList.contains('wrong'))avSay(avPick(AV_NO),6000);},0);
});
document.addEventListener('keydown',function(e){if(e.key==='Escape')avHide();});
setTimeout(function(){if(!sget(PFX+'av_ola')){avSay(AV_HI,8000);sset(PFX+'av_ola','1');}},1400);
window.revisaoAPI={pfx:PFX,score:function(){return {ok:score.ok,no:score.no};},refreshDone:refreshDone,entraErros:entraErros,saiErros:saiErros,essencial:aplicaEssencial};
})();
