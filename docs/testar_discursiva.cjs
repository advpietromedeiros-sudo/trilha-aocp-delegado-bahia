// testar_discursiva.cjs — prova o COMPORTAMENTO do Treino de Discursiva (02/11/2026) no index REAL, em jsdom:
// conteúdo íntegro (toda peça com modelo e checklist, todo cartão com artigo e Certo/Errado válido), peça feita passo a
// passo até a nota da Tabela 7.3, estudo de caso até a nota da Tabela 7.4, repetição espaçada e contador de linhas.
// Uso: node docs/testar_discursiva.cjs [--autoteste]  (0 = ok; --autoteste estraga a nota técnica e só sai 0 se ACUSAR)
let JSDOM, VirtualConsole;
try { ({ JSDOM, VirtualConsole } = require("jsdom")); } catch { console.log("⚠️ jsdom não instalado (npm ci): porta pulada"); process.exit(2); }
const fs = require("fs"), path = require("path");
const AUTO = process.argv.includes("--autoteste");
const dir = path.join(__dirname, "..", "discursiva");
let html = fs.readFileSync(path.join(dir, "Treino_Discursiva.html"), "utf8");
const conteudo = fs.readFileSync(path.join(dir, "conteudo.js"), "utf8");
const leis = fs.readFileSync(path.join(dir, "leis.js"), "utf8");
const compl = fs.readFileSync(path.join(dir, "pecas_complementares.js"), "utf8");
html = html.replace('<script src="conteudo.js"></script>', () => "<script>" + conteudo + "</script>").replace('<script src="leis.js"></script>', () => "<script>" + leis + "</script>").replace('<script src="pecas_complementares.js"></script>', () => "<script>" + compl + "</script>");
if (AUTO) { const s = html.replace("const tec=Math.round(40*f/Math.max(1,tot))", "const tec=Math.round(4*f/Math.max(1,tot))"); if (s === html) { console.log("AUTOTESTE: não plantou"); process.exit(1); } html = s; }
const erros = [], vc = new VirtualConsole();
vc.on("jsdomError", e => erros.push(String(e.message || e)));
const dom = new JSDOM(html, { runScripts: "dangerously", url: "http://localhost/", virtualConsole: vc, pretendToBeVisual: true,
  beforeParse(w) { w.scrollTo = () => {}; w.alert = () => {}; w.confirm = () => true; w.addEventListener("error", ev => erros.push(ev.message)); } });
const w = dom.window, d = w.document, A = w.discAPI;
let falhas = 0; const prova = (n, ok, det = "") => { console.log(`  ${ok ? "✅" : "❌"} ${n}${!ok && det ? " — " + det : ""}`); if (!ok) falhas++; };
const clicar = id => d.getElementById(id).click();

prova("página carrega com as 5 abas e sem erro de JavaScript", d.querySelectorAll("#abas button").length === 5 && erros.length === 0, erros.join(" | "));
// conteúdo
const ruins = [];
for (const p of A.PECAS) A.passosDe(p).forEach((s, i) => { if (!s.t || !s.orient || !String(s.modelo || "").trim() || !Array.isArray(s.check) || !s.check.length) ruins.push(p.id + " passo " + (i + 1)); });
prova(`${A.PECAS.length} peças: todo passo tem orientação, modelo e checklist`, A.PECAS.length >= 8 && ruins.length === 0, ruins.join(", "));
const ids = new Set(A.CARTOES.map(c => c.id)), malCE = A.CARTOES.filter(c => !c.p || !c.r || !c.a || !Array.isArray(c.ce) || c.ce.length !== 3 || !["C", "E"].includes(c.ce[1]) || c.ce[2].length < 5);
prova(`${A.CARTOES.length} cartões com pergunta, resposta, artigo e Certo/Errado válidos, ids únicos`, A.CARTOES.length >= 60 && ids.size === A.CARTOES.length && malCE.length === 0, malCE.map(c => c.id).join(","));
const ceC = A.CARTOES.filter(c => c.ce[1] === "C").length;
prova("Certo/Errado equilibrado (pelo menos 25% de cada gabarito)", ceC >= A.CARTOES.length * .25 && A.CARTOES.length - ceC >= A.CARTOES.length * .25, `C=${ceC}`);
prova("cada estudo de caso tem espelho somando 15 pontos (Tabela 7.4)", A.CASOS.every(c => c.espelho.reduce((a, e) => a + e[1], 0) === 15), A.CASOS.map(c => c.id + "=" + c.espelho.reduce((a, e) => a + e[1], 0)).join(" "));
prova("contador de linhas: 72 caracteres = 1 linha; 73 = 2; vazio = 0", A.linhas("x".repeat(72)) === 1 && A.linhas("x".repeat(73)) === 2 && A.linhas("") === 0);

// peça passo a passo, do início ao fim
A.abrirPeca("preventiva");
const nPassos = A.passosDe(A.PECAS[0]).length;
for (let i = 0; i < nPassos; i++) {
  const t = d.getElementById("txt"); t.value = "Trecho " + (i + 1) + " da peça. ".repeat(3); t.dispatchEvent(new w.Event("input"));
  clicar("verModelo"); d.querySelectorAll("[data-chk]").forEach(c => { c.checked = true; c.dispatchEvent(new w.Event("change")); }); clicar("prox");
}
const final = d.querySelector(".peca-final")?.textContent || "";
d.getElementById("lp").value = "10"; clicar("salvarNota");
const notaPeca = A.st().pecas.preventiva.nota;
prova("peça feita passo a passo: texto montado, checklist completo → 60/60 na Tabela 7.3", final.includes("Trecho 1") && final.includes("Trecho " + nPassos) && notaPeca === 60, `nota=${notaPeca}`);
prova("ao registrar a nota, abre a memorização dos cartões da peça", /Memorize: Representação por prisão preventiva/.test(d.body.textContent) && !!d.getElementById("resp"));
// repetição espaçada: acertar sobe de caixa e agenda para o futuro; errar volta para a caixa 1, hoje
const c0 = A.CARTOES.find(c => c.id === "preventiva#0").id;
clicar("virar"); d.querySelector('[data-nota="2"]').click();
const k0 = A.st().cartoes[c0];
clicar("virar"); d.querySelector('[data-nota="0"]').click();
const k1 = A.st().cartoes["preventiva#1"];
prova("repetição espaçada: acertou → caixa 1 e volta amanhã; errou → caixa 1 e volta hoje", k0.caixa === 1 && k0.prox > Date.now() && k1.caixa === 1 && k1.prox <= Date.now(), JSON.stringify({ k0, k1 }));

// estudo de caso
A.abrirCaso("c-fianca");
const t = d.getElementById("txt"); t.value = Array.from({ length: 12 }, (_, i) => "Linha " + i + " da resposta com fundamento no art. 322 do CPP.").join("\n"); t.dispatchEvent(new w.Event("input"));
clicar("corrigir"); d.querySelectorAll("[data-esp]").forEach(c => { c.checked = true; c.dispatchEvent(new w.Event("change")); });
d.getElementById("lp").value = "5"; clicar("salvarNota");
prova("estudo de caso: 12 linhas, espelho completo → 20/20 na Tabela 7.4", A.st().casos["c-fianca"].nota === 20 && A.st().hist.some(h => h.t === "caso" && h.linhas === 12), JSON.stringify(A.st().casos["c-fianca"].nota));
// cartões por lei (leis.js, conferidos no texto legal)
prova(`${A.LEIS.length} leis do edital com cartões, e a peça da Lei Antifacção está na lista`, A.LEIS.length >= 8 && A.LEIS.every(l => l.cards.length >= 5) && A.PECAS.some(p => p.id === "faccao") && A.CASOS.some(c => c.id === "c-tco"));
A.ir("memoria"); d.querySelector('[data-lei="l15358"]').click();
prova("tocar numa lei abre a memorização só dela", /Memorize: Lei 15\.358/.test(d.body.textContent) && !!d.getElementById("resp"));
// peças complementares (03/11/2026): 14 peças, e a de inquérito usa cabeçalho e preâmbulo próprios
const novas = ["apf", "cautelar-diversa", "afastamento", "requisicao", "relatorio"];
prova("as 5 peças complementares estão na lista (14 no total)", A.PECAS.length === 14 && novas.every(id => A.PECAS.some(p => p.id === id)), A.PECAS.map(p => p.id).join(","));
const apf = A.passosDe(A.PECAS.find(p => p.id === "apf"));
prova("despacho do flagrante: cabeçalho do APF (não de portaria) e checklist próprio do preâmbulo", /Auto de Prisão em Flagrante/.test(apf[0].modelo) && !/Portaria/.test(apf[0].modelo) && apf[1].check.some(c => /301 a 306/.test(c)));
A.abrirPeca("apf");
for (let i = 0; i < apf.length; i++) { const tx = d.getElementById("txt"); tx.value = "Parte " + (i + 1) + " do despacho."; tx.dispatchEvent(new w.Event("input")); clicar("verModelo"); d.querySelectorAll("[data-chk]").forEach(c => { c.checked = true; c.dispatchEvent(new w.Event("change")); }); clicar("prox"); }
d.getElementById("lp").value = "10"; clicar("salvarNota");
prova("despacho do flagrante feito passo a passo até a nota 60/60", A.st().pecas.apf && A.st().pecas.apf.nota === 60, JSON.stringify(A.st().pecas.apf));
// Certo/Errado
A.ir("memoria"); clicar("ceTudo");
const item = d.querySelector(".flash .p").textContent, cart = A.CARTOES.find(c => c.ce[0] === item);
d.querySelector(`[data-ce="${cart.ce[1]}"]`).click();
prova("Certo/Errado: responder o gabarito certo mostra o comentário e o artigo", /Acertou/.test(d.getElementById("res").textContent) && d.getElementById("res").textContent.includes(cart.a));
prova("nenhum erro de JavaScript em todo o fluxo", erros.length === 0, erros.join(" | "));

if (AUTO) { console.log(falhas ? "AUTOTESTE OK: o defeito plantado foi acusado" : "AUTOTESTE FALHOU: o defeito passou"); process.exit(falhas ? 0 : 1); }
console.log(falhas ? `❌ ${falhas} falha(s)` : "✅ treino de discursiva verde"); process.exit(falhas ? 1 : 0);
