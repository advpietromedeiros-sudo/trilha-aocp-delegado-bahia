// Paleta de grifos (10/11/2026, pedido do titular): a tecla G abre uma paleta para grifar qualquer texto, em todas
// as telas. A story roda a FONTE ÚNICA (assets/grifa.js) num iframe com um texto de exemplo — o mesmo código que
// ferramentas/embutir_grifa.py embute no index.html, no Treino de Discursiva e nos cadernos da Revisão.
import grifa from '../assets/grifa.js?raw';

const EXEMPLO = `
<h2>Prescrição da pretensão punitiva (exemplo)</h2>
<p>A prescrição, antes de transitar em julgado a sentença final, regula-se pelo <b>máximo da pena privativa de
liberdade</b> cominada ao crime (CP, art. 109). Se o máximo da pena é <b>igual a um ano</b>, o prazo é de
<b>quatro anos</b>; se é <b>inferior a um ano</b>, o prazo é de <b>três anos</b>.</p>
<p>Na prova, a banca costuma trocar "igual a" por "igual ou inferior a" — e a assertiva fica <b>errada</b>.</p>`;

function pagina(acao) {
  const sai = '</' + 'script>';
  return `<!doctype html><html lang="pt-BR"><head><meta charset="utf-8"><style>
body{font:17px/1.6 Georgia,serif;color:#1b1b1b;background:#fff;margin:0;padding:24px 28px 220px;max-width:760px}
p{text-align:justify;hyphens:auto}h2{font:700 20px system-ui,sans-serif}
</style></head><body>${EXEMPLO}<script>${grifa}${sai}<script>${acao}${sai}</body></html>`;
}

function moldura(srcdoc, width) {
  const wrap = document.createElement('div');
  wrap.style.cssText = 'padding:16px;background:#e9e9e9';
  const frame = document.createElement('iframe');
  frame.title = 'Paleta de grifos';
  frame.style.cssText = `width:${width};height:620px;border:0;background:#fff;box-shadow:0 4px 24px rgba(0,0,0,.15)`;
  frame.srcdoc = srcdoc;
  wrap.appendChild(frame);
  return wrap;
}

// grifa um trecho do exemplo como se o titular tivesse selecionado (para a story mostrar o resultado)
const GRIFAR = (trecho, cor, n = 0) => `(function(){var ps=document.querySelectorAll('p'),p=ps[${n}],
t=[].slice.call(p.childNodes).find(function(x){return x.nodeType===3&&x.nodeValue.indexOf(${JSON.stringify(trecho)})>=0})
||[].slice.call(p.querySelectorAll('b')).map(function(b){return b.firstChild}).find(function(x){return x.nodeValue.indexOf(${JSON.stringify(trecho)})>=0});
var i=t.nodeValue.indexOf(${JSON.stringify(trecho)}),r=document.createRange();r.setStart(t,i);r.setEnd(t,i+${trecho.length});
var s=getSelection();s.removeAllRanges();s.addRange(r);Grifa.escolher('${cor}');Grifa.grifarSelecao('${cor}');})();`;

export default {
  title: 'Aguardando Análise/Paleta de grifos (tecla G)',
  argTypes: { width: { control: 'select', options: ['100%', '1280px', '768px', '360px'] } },
  args: { width: '100%' },
};

export const PaletaAberta = {
  name: 'Paleta aberta (aperte G para abrir e fechar)',
  render: ({ width }) => moldura(pagina("try{localStorage.clear()}catch(e){};Grifa.abrir();"), width),
};
export const ComGrifos = {
  name: 'Com grifos em três cores',
  render: ({ width }) => moldura(pagina("try{localStorage.clear()}catch(e){};Grifa.abrir();" +
    GRIFAR('regula-se pelo', 'amarelo') + GRIFAR('cominada ao crime', 'verde') + GRIFAR('errada', 'rosa', 1) +
    "Grifa.escolher('amarelo');"), width),
};
export const Borracha = {
  name: 'Borracha escolhida (clique num grifo para apagar)',
  render: ({ width }) => moldura(pagina("try{localStorage.clear()}catch(e){};Grifa.abrir();" +
    GRIFAR('regula-se pelo', 'azul') + GRIFAR('cominada ao crime', 'laranja') + "Grifa.escolher('borracha');"), width),
};
export const Celular = {
  name: 'Celular (360 px)',
  args: { width: '360px' },
  render: ({ width }) => moldura(pagina("try{localStorage.clear()}catch(e){};Grifa.abrir();" + GRIFAR('regula-se pelo', 'amarelo')), width),
};
