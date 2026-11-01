// testar_pagina.cjs — o index.html REAL carrega sem erro de JavaScript (31/10/2026).
//
// 💥 O erro mais caro do app de arquivo único é a tela inteira em branco: um nome errado, ou o
// script v8 (blocos) rodando na ordem errada em relação ao principal, derruba tudo. Este teste abre
// a página num navegador simulado (jsdom), sem servidor (as chamadas /api/* falham, como no duplo
// clique), e exige: 0 erro de JavaScript, o painel de blocos montado e a árvore do edital desenhada.
//
// Uso: node docs/testar_pagina.cjs   (0 = ok, 1 = falha, 2 = jsdom ausente: porta pulada e dita)
let JSDOM, VirtualConsole;
try {
  ({ JSDOM, VirtualConsole } = require("jsdom"));
} catch {
  console.log("⚠️ jsdom não instalado (npm ci): página NÃO conferida — porta pulada");
  process.exit(2);
}
const fs = require("fs");
const path = require("path");
const html = fs.readFileSync(path.join(__dirname, "..", "index.html"), "utf8");
const erros = [];
const vc = new VirtualConsole();
vc.on("jsdomError", (e) => erros.push("jsdomError: " + (e.message || e)));
vc.on("error", (e) => erros.push("console.error: " + e));
const dom = new JSDOM(html, {
  runScripts: "dangerously", url: "http://127.0.0.1:8765/", virtualConsole: vc, pretendToBeVisual: true,
  beforeParse(w) {
    w.fetch = async () => ({ ok: false, status: 503, json: async () => ({ error: "sem servidor no teste" }) });
    w.scrollTo = () => {};
    w.HTMLElement.prototype.scrollIntoView = () => {};
    w.matchMedia = () => ({ matches: false, addEventListener() {}, removeEventListener() {} });
    w.confirm = () => true;
    w.addEventListener("error", (ev) => erros.push("window.error: " + ev.message));
    w.addEventListener("unhandledrejection", (ev) => erros.push("promessa: " + (ev.reason?.message || ev.reason)));
  },
});
setTimeout(() => {
  const d = dom.window.document;
  const card = d.getElementById("bloco-card");
  const disciplinas = d.querySelectorAll("#tree .disc-head").length;
  const reais = erros.filter((e) => !/sem servidor|503/.test(String(e)));
  const checks = [
    ["0 erro de JavaScript ao carregar", reais.length === 0, reais.slice(0, 3).join(" | ")],
    ["painel de blocos montado", !!card && /Blocos de 30|Bloco \d/.test(card.textContent), ""],
    ["árvore do edital com as 17 disciplinas", disciplinas === 17, `achadas ${disciplinas}`],
  ];

  // v9 — Certo ou Errado (31/10/2026): abre o comentário de uma questão no formato novo, na tela REAL.
  const w = dom.window;
  let ce = {};
  try {
    w.eval(`
      activeItem=ITEMS[0];
      const itensCE=[0,1,2,3,4,5,6,7].map(i=>({afirmacao:'Afirmação '+i+' <b>sem html vivo</b> para julgar.',
        gabarito:i%2?'C':'E',tipo:['doutrina','lei_seca','jurisprudencia'][i%3],
        comentario:'COMENTARIO-OCULTO-'+i,fundamento:'CP, art. 1º'}));
      window.__c={summary:'resumo',alternatives:{A:{veredito:'Correta',titulo:'t',explicacao:'e'}},
        certo_errado:itensCE,laws:[],jurisprudence:[],gaps:[],auditoria:null,
        lessons:[{title:'AULA-ANTIGA',blocks:[]}],traps:['PEGADINHA-SOLTA'],mindmap:[]};
      renderLesson(window.__c,[]);`);
    const card = d.getElementById("lesson-card");
    const antes = card.innerHTML;
    ce.itens = d.querySelectorAll("#ce-section .ce-item").length;
    ce.botoes = d.querySelectorAll("#ce-section [data-ce]").length;
    ce.ocultoAntes = !antes.includes("COMENTARIO-OCULTO-0");
    ce.semAula = !antes.includes("AULA-ANTIGA") && !antes.includes("PEGADINHA-SOLTA");
    ce.leiRecolhida = !!d.querySelector("details.ref-details #laws-section");
    ce.escapado = !antes.includes("<b>sem html vivo</b>");
    d.querySelector('#ce-section [data-ce="0"][data-v="E"]').click();
    const depois = card.innerHTML;
    ce.reveladoDepois = depois.includes("COMENTARIO-OCULTO-0") && !depois.includes("COMENTARIO-OCULTO-1");
    ce.placar = /1 de 8 julgadas • 1 acerto/.test(d.querySelector(".ce-placar")?.textContent || "");
    ce.semGrifo = !w.eval("emphasizeText('assinale a alternativa INCORRETA, EXCETO')").includes("study-keyword");
    // questão antiga (ainda não convertida): a aula antiga continua aparecendo, sem quebrar
    w.eval("const v=Object.assign({},window.__c);delete v.certo_errado;renderLesson(v,[]);");
    ce.antigaOk = !!d.getElementById("lesson-sections") && !d.getElementById("ce-section");
  } catch (e) {
    ce.erro = String(e && e.message);
  }
  checks.push(
    ["C/E: 8 itens, cada um com Certo e Errado", ce.itens === 8 && ce.botoes === 16, JSON.stringify(ce)],
    ["C/E: comentário oculto até o aluno julgar", ce.ocultoAntes === true, ce.erro || ""],
    ["C/E: julgou o item 1 → só o comentário dele aparece", ce.reveladoDepois === true, ""],
    ["C/E: placar conta 1 de 8 julgadas e 1 acerto", ce.placar === true, ""],
    ["C/E: sem aula antiga nem pegadinha solta na tela", ce.semAula === true, ""],
    ["C/E: lei seca e jurisprudência recolhidas para consulta", ce.leiRecolhida === true, ""],
    ["C/E: texto da IA escapado (nada de html vivo)", ce.escapado === true, ""],
    ["questão sem termo grifado de azul", ce.semGrifo === true, ""],
    ["questão antiga, ainda não convertida, mostra a aula antiga", ce.antigaOk === true, ""],
  );
  let falhas = 0;
  for (const [desc, ok, det] of checks) {
    console.log(`  ${ok ? "✅" : "❌"} ${desc}${!ok && det ? " — " + det : ""}`);
    if (!ok) falhas++;
  }
  console.log(falhas ? `❌ ${falhas} falha(s)` : "✅ página verde");
  dom.window.close();
  process.exit(falhas ? 1 : 0);
}, 1500);
