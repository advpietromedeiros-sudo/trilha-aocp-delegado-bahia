// Treino de Discursiva (07/11/2026): a aba PENTE FINO e o comentário dos simulados em QUADROS, na página REAL.
// Os simulados (material de terceiro) não entram aqui: o comentário usa um exemplo inventado, no mesmo formato do PDF.
// O Pente Fino usa um exemplo pequeno, também inventado (a jurisprudência é marcada como fictícia).
import paginaHtml from '../discursiva/Treino_Discursiva.html?raw';
import conteudo from '../discursiva/conteudo.js?raw';
import leis from '../discursiva/leis.js?raw';
import complementares from '../discursiva/pecas_complementares.js?raw';
import conducao from '../discursiva/conducao.js?raw';
import estudo from '../discursiva/estudo.js?raw';
import artigos from '../discursiva/artigos.js?raw';
import blocos from '../discursiva/blocos.js?raw';

const EXEMPLO_PF = {
  disciplina: 'Direito Processual Civil (exemplo)', conferido_em: '07/11/2026', fontes: ['Lei 13.105/2015 (CPC)'],
  pontos: [{ id: 'P1', titulo: 'Normas fundamentais do processo civil' }, { id: 'P2', titulo: 'Prazos processuais' }],
  rodadas: [
    { n: 1, titulo: 'Rodada 1 · O essencial', itens: [
      { id: 'S-1', ponto: 'P1', tema: 'Vedação à decisão surpresa', gabarito: 'E',
        assertiva: 'O juiz pode decidir com base em fundamento sobre o qual as partes não se manifestaram, desde que se trate de matéria que deva conhecer de ofício.',
        comentario: { resumo: 'Está **errada**: a vedação à **decisão surpresa** vale **ainda que** a matéria seja conhecível de ofício.',
          regra: 'O juiz não decide com base em fundamento sobre o qual não ouviu as partes (CPC, art. 10).',
          excecoes: ['Tutela provisória de urgência (art. 9º, parágrafo único, I)'],
          lei: [{ lei: 'L13105', art: '10', rotulo: 'CPC, art. 10', texto: 'O juiz não pode decidir, em grau algum de jurisdição, com base em fundamento a respeito do qual não se tenha dado às partes oportunidade de se manifestar, ainda que se trate de matéria sobre a qual deva decidir de ofício.' }],
          juris: [{ tribunal: 'STJ', fonte: 'EXEMPLO FICTÍCIO', data: '01/01/2026', texto: 'Tese fictícia, só para mostrar o quadro.' }],
          pegadinha: 'A banca troca "ainda que" por "salvo quando".', palavras_chave: ['contraditório', 'decisão surpresa'] } },
      { id: 'S-2', ponto: 'P2', tema: 'Dias úteis', gabarito: 'E', assertiva: 'Na contagem de prazo em dias, computam-se os dias corridos.',
        comentario: { resumo: 'Está **errada**: computam-se **somente os dias úteis** (art. 219).', palavras_chave: ['dias úteis'] } }] },
    { n: 2, titulo: 'Rodada 2 · Aprofundamento', itens: [
      { id: 'S-3', ponto: 'P1', tema: 'Tutela da evidência', gabarito: 'C', assertiva: 'A tutela da evidência do art. 311, II, pode ser concedida sem ouvir o réu.',
        comentario: { resumo: 'Está **certa**: art. 9º, parágrafo único, II.' } }] }]
};
const EXEMPLO_COM = [
  ['p', 'A questão cobra o art. 25 da Lei nº 14.133/2021 e a Súmula 473 do STF: a Administração deverá anular seus atos ilegais no prazo de 5 (cinco) anos, salvo comprovada má-fé.'],
  ['p', 'A – Incorreta. A competência é da autoridade policial, exceto nos casos do art. 129, I, da CF.'],
  ['p', 'B – Correta. Somente o Ministério Público poderá propor a ação, e a pena é reduzida de 1/3 a 2/3.'],
  ['p', 'C – Incorreta. Não se aplica o prazo de 48 horas.'], ['p', 'D – Incorreta. É vedado ao juiz agir de ofício.'], ['p', 'E – Incorreta. O percentual é de 30%.'],
];

function pagina(aposCarregar) {
  const tags = { 'conteudo.js': conteudo, 'leis.js': leis, 'pecas_complementares.js': complementares, 'conducao.js': conducao, 'estudo.js': estudo, 'artigos.js': artigos, 'blocos.js': blocos };
  let h = paginaHtml.replace('<script src="simulados_delta.js" data-local="terceiro"></script>', '')
    .replace('<script src="pente_fino_cpc.js" data-opcional="1"></script>', `<script>window.PENTE_FINO={CPC:${JSON.stringify(EXEMPLO_PF)}};</script>`);
  for (const [nome, js] of Object.entries(tags)) h = h.replace(`<script src="${nome}"></script>`, () => `<script>${js}</script>`);
  h = h.replace('</body>', () => `<script>try{localStorage.removeItem('pente-fino:v1')}catch(e){}${aposCarregar}</script></body>`);
  return h;
}

function moldura(srcdoc, width) {
  const wrap = document.createElement('div');
  wrap.style.cssText = 'display:flex;justify-content:center;background:#d9dee5;min-height:100vh;padding:16px 0';
  const frame = document.createElement('iframe');
  frame.title = 'Treino de Discursiva — Pente Fino';
  frame.style.cssText = `width:${width};height:1100px;border:0;background:#fff;box-shadow:0 4px 24px rgba(0,0,0,.15)`;
  frame.srcdoc = srcdoc;
  wrap.appendChild(frame);
  return wrap;
}

export default {
  title: 'Nesta sessão/Pente Fino e comentários em quadros',
  argTypes: { width: { control: 'select', options: ['100%', '1280px', '768px', '360px'] } },
  args: { width: '100%' },
};

export const PenteFinoAntesDeResponder = { name: 'Pente Fino · antes de responder', render: ({ width }) => moldura(pagina("discAPI.ir('pente');"), width) };
export const PenteFinoComentario = { name: 'Pente Fino · comentário (errou)', render: ({ width }) => moldura(pagina("discAPI.ir('pente');discAPI.pente.responder('C');"), width) };
export const PenteFinoCelular = { name: 'Pente Fino · celular (360 px)', args: { width: '360px' }, render: ({ width }) => moldura(pagina("discAPI.ir('pente');discAPI.pente.responder('C');"), width) };
export const ComentarioDoSimulado = {
  name: 'Simulados · comentário em quadros (exemplo inventado)',
  render: ({ width }) => moldura(pagina(`discAPI.ir('simulados');document.getElementById('tela').innerHTML='<div class="card sq"><div class="fb ok">Você acertou. <b>Gabarito: B</b></div><div class="com"><div class="rot">Comentários</div>'+BLOCOS.comentario(${JSON.stringify(EXEMPLO_COM)},{gab:'B'})+'</div></div>';`), width),
};
