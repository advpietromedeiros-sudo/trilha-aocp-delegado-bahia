// testar_discursivas_stories.cjs — prova o COMPORTAMENTO do módulo "Discursivas em Stories" em jsdom:
// dados íntegros (blocos por disciplina, cada questão com tema, enunciado, pontos e base), a home com os blocos,
// abrir um bloco no palco de Stories, tocar à direita revela um ponto por vez, avançar entre questões e o ✕ fecha;
// a posição fica salva para retomar.
// Uso: node docs/testar_discursivas_stories.cjs [--autoteste]  (0 = ok; --autoteste tira os pontos de uma questão e só sai 0 se ACUSAR)
let JSDOM, VirtualConsole;
try { ({ JSDOM, VirtualConsole } = require("jsdom")); } catch { console.log("⚠️ jsdom não instalado (npm ci): porta pulada"); process.exit(2); }
const fs = require("fs"), path = require("path");
const AUTO = process.argv.includes("--autoteste");
const dir = path.join(__dirname, "..", "discursiva");
let html = fs.readFileSync(path.join(dir, "Discursivas_Stories.html"), "utf8");
let dados = fs.readFileSync(path.join(dir, "discursivas_stories_dados.js"), "utf8");
const tag = '<script src="discursivas_stories_dados.js"></script>';
if (!html.includes(tag)) { console.log("falta a tag de discursivas_stories_dados.js"); process.exit(1); }
if (AUTO) {
  const s = dados.replace(/pontos:\s*\[[\s\S]*?\]/, "pontos:[]");  // esvazia os pontos da 1ª questão
  if (s === dados) { console.log("AUTOTESTE: não plantou"); process.exit(1); }
  dados = s;
}
html = html.replace(tag, () => "<script>" + dados + "</script>");

const vc = new VirtualConsole();
const dom = new JSDOM(html, { runScripts: "dangerously", url: "http://localhost/", pretendToBeVisual: true, virtualConsole: vc, beforeParse(w) { w.scrollTo = () => {}; } });
const w = dom.window, d = w.document;

let falhas = 0; const prova = (n, ok, det = "") => { console.log(`  ${ok ? "✅" : "❌"} ${n}${!ok && det ? " — " + det : ""}`); if (!ok) falhas++; };

const B = w.DISC_STORIES;
prova("os dados carregam com pelo menos 3 blocos por disciplina", Array.isArray(B) && B.length >= 3, String(B && B.length));

// integridade: cada questão tem tema, enunciado, base e ao menos 2 pontos
const qs = (B || []).flatMap(b => (b.itens || []).map(q => ({ ...q, bloco: b.bloco })));
prova("há pelo menos 12 questões discursivas no total", qs.length >= 12, String(qs.length));
const ruins = qs.filter(q => !q.tema || !q.enun || !q.base || !Array.isArray(q.pontos) || q.pontos.length < 2);
prova("toda questão tem tema, enunciado, base e pelo menos 2 pontos-chave", ruins.length === 0,
  ruins.slice(0, 3).map(q => (q.bloco || "") + " / " + (q.tema || "")).join(" | "));

// cada bloco tem id e nome
const blocosRuins = (B || []).filter(b => !b.id || !b.bloco || !Array.isArray(b.itens) || b.itens.length === 0);
prova("todo bloco tem id, nome e questões", blocosRuins.length === 0, blocosRuins.map(b => b.id || "?").join(","));

// home mostra os blocos
prova("a home mostra os blocos por disciplina", d.querySelectorAll("[data-bloco]").length >= 3, String(d.querySelectorAll("[data-bloco]").length));

// abrir o 1º bloco entra no palco de Stories com enunciado e barrinhas
d.querySelector('[data-bloco="0"]').click();
prova("abrir um bloco mostra o palco com enunciado, barrinhas e dica de toque",
  !!d.querySelector("#stage.on") && !!d.querySelector(".enun") && d.querySelectorAll("#segs .seg").length >= 1 && !!d.querySelector(".shint"));

// os pontos começam ocultos
prova("os pontos da resposta começam ocultos", d.querySelectorAll(".ponto.on").length === 0 && d.querySelectorAll(".ponto.hid").length >= 2,
  d.querySelectorAll(".ponto.hid").length + " ocultos");

// tocar à direita revela o 1º ponto
d.querySelector('[data-tap="next"]').click();
prova("tocar à direita revela um ponto-chave (.on com texto)",
  d.querySelectorAll(".ponto.on").length === 1 && d.querySelector(".ponto.on").textContent.length > 0);

// revelar todos os pontos e mais um toque avança para a 2ª questão
const nPontos = B[0].itens[0].pontos.length;
for (let i = 1; i < nPontos; i++) d.querySelector('[data-tap="next"]').click(); // revela os demais
d.querySelector('[data-tap="next"]').click();                                   // passa de questão
prova("após revelar todos os pontos, avança para a 2ª questão", /Questão\s*2\//.test(d.body.textContent), d.querySelector(".schip") && d.querySelector(".schip").textContent);

// posição salva para retomar
let salvo = {}; try { salvo = JSON.parse(w.localStorage.getItem("discstories:v1") || "{}"); } catch (e) {}
prova("o Stories salva a posição para retomar", salvo.last && salvo.last.b === 0 && salvo.last.q >= 1, JSON.stringify(salvo.last || {}));

// ✕ fecha o palco
d.querySelector('[data-close]').click();
prova("o ✕ fecha o Stories", !d.querySelector("#stage.on"));

// Modo celular
const fsb = d.getElementById("fsbtn");
if (fsb) fsb.click();
prova("o botão 📱 Modo celular adapta o layout (data-cel=1)", d.documentElement.getAttribute("data-cel") === "1");

if (AUTO) { console.log(falhas ? "AUTOTESTE OK: o defeito plantado foi acusado" : "AUTOTESTE FALHOU: o defeito passou"); process.exit(falhas ? 0 : 1); }
console.log(falhas ? `❌ ${falhas} falha(s)` : "✅ Discursivas em Stories verde"); process.exit(falhas ? 1 : 0);
