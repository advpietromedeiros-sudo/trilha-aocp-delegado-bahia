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
  let falhas = 0;
  for (const [desc, ok, det] of checks) {
    console.log(`  ${ok ? "✅" : "❌"} ${desc}${!ok && det ? " — " + det : ""}`);
    if (!ok) falhas++;
  }
  console.log(falhas ? `❌ ${falhas} falha(s)` : "✅ página verde");
  dom.window.close();
  process.exit(falhas ? 1 : 0);
}, 1500);
