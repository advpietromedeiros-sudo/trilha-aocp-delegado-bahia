// testar_atualidades.cjs — prova o COMPORTAMENTO do módulo "Atualidades · Certo e Errado" em jsdom:
// dados íntegros (>=100 questões, cada uma com tema válido, assertiva, gabarito booleano e comentário),
// a home mostra os filtros de tema e as questões; no modo Treino, responder Certo/Errado revela o gabarito,
// o feedback e o comentário; o modo Estudo revela tudo; o 📱 Modo celular adapta o layout.
// Uso: node docs/testar_atualidades.cjs [--autoteste]  (0 = ok; --autoteste corrompe um gabarito e só sai 0 se ACUSAR)
let JSDOM, VirtualConsole;
try { ({ JSDOM, VirtualConsole } = require("jsdom")); } catch { console.log("⚠️ jsdom não instalado (npm ci): porta pulada"); process.exit(2); }
const fs = require("fs"), path = require("path");
const AUTO = process.argv.includes("--autoteste");
const dir = path.join(__dirname, "..", "discursiva");
let html = fs.readFileSync(path.join(dir, "Atualidades_CE.html"), "utf8");
let dados = fs.readFileSync(path.join(dir, "atualidades_dados.js"), "utf8");
const tag = '<script src="atualidades_dados.js"></script>';
if (!html.includes(tag)) { console.log("falta a tag de atualidades_dados.js"); process.exit(1); }
if (AUTO) {
  const s = dados.replace("g:true,", "g:1,");  // corrompe o 1º gabarito (deixa de ser booleano)
  if (s === dados) { console.log("AUTOTESTE: não plantou"); process.exit(1); }
  dados = s;
}
html = html.replace(tag, () => "<script>" + dados + "</script>");

const vc = new VirtualConsole();
const dom = new JSDOM(html, { runScripts: "dangerously", url: "http://localhost/", pretendToBeVisual: true, virtualConsole: vc, beforeParse(w) { w.scrollTo = () => {}; } });
const w = dom.window, d = w.document;

let falhas = 0; const prova = (n, ok, det = "") => { console.log(`  ${ok ? "✅" : "❌"} ${n}${!ok && det ? " — " + det : ""}`); if (!ok) falhas++; };

const A = w.ATUALIDADES;
prova("os dados carregam com info, temas e questões", !!A && Array.isArray(A.temas) && A.temas.length >= 5 && Array.isArray(A.questoes), A ? String(A.questoes && A.questoes.length) : "sem ATUALIDADES");

const QS = (A && A.questoes) || [], TEMAS = (A && A.temas) || [];
prova("há pelo menos 100 questões Certo/Errado", QS.length >= 100, String(QS.length));

// integridade: tema válido, assertiva, gabarito BOOLEANO e comentário
const idsTema = new Set(TEMAS.map(t => t.id));
const ruins = QS.filter(q => !q.t || !idsTema.has(q.t) || !q.a || typeof q.g !== "boolean" || !q.c);
prova("toda questão tem tema válido, assertiva, gabarito booleano e comentário", ruins.length === 0,
  ruins.slice(0, 3).map(q => (q.id || "?") + "/" + (q.t || "?") + "(g=" + typeof (q && q.g) + ")").join(" | "));

// ids únicos
const ids = QS.map(q => q.id), unico = new Set(ids);
prova("os ids das questões são únicos", unico.size === ids.length, String(ids.length - unico.size) + " repetido(s)");

// equilíbrio: há assertivas certas E erradas (não é tudo "Certo")
const nC = QS.filter(q => q.g === true).length, nE = QS.filter(q => q.g === false).length;
prova("há assertivas CERTAS e ERRADAS", nC > 0 && nE > 0, "C=" + nC + " E=" + nE);

// home: filtros de tema e questões
prova("a home mostra os filtros de tema", d.querySelectorAll("#temas button[data-tm]").length >= 3, String(d.querySelectorAll("#temas button[data-tm]").length));
prova("a home lista todas as questões (uma por card)", d.querySelectorAll(".q").length === QS.length, d.querySelectorAll(".q").length + " de " + QS.length);

// modo Treino começa sem gabarito revelado
prova("no modo Treino o gabarito começa oculto", d.querySelectorAll(".gab").length === 0, String(d.querySelectorAll(".gab").length));

// responder uma questão revela gabarito, feedback e comentário
const bt = d.querySelector('.ce button[data-id][data-r]');
prova("cada questão tem botões Certo/Errado", !!bt);
if (bt) bt.click();
prova("responder revela o gabarito, o feedback e o comentário",
  d.querySelectorAll(".gab").length === 1 && d.querySelectorAll(".fb").length === 1 && d.querySelectorAll(".com").length === 1);

// o comentário destaca termos-chave em vermelho (.k)
prova("o comentário traz termos-chave destacados (.k)", !!d.querySelector(".com .k"));

// o placar conta a resposta
prova("o placar registra a questão respondida", /Respondidas/.test(d.body.textContent) && !!d.querySelector("#placar"));

// modo Estudo revela tudo
d.getElementById("mEstudo").click();
prova("o modo Estudo revela gabarito e comentário de todas as questões",
  d.querySelectorAll(".gab").length === QS.length && d.querySelectorAll(".com").length === QS.length,
  d.querySelectorAll(".gab").length + "/" + QS.length);

// Modo celular
d.getElementById("bcel").click();
prova("o botão 📱 Modo celular adapta o layout (data-cel=1)", d.documentElement.getAttribute("data-cel") === "1");

if (AUTO) { console.log(falhas ? "AUTOTESTE OK: o defeito plantado foi acusado" : "AUTOTESTE FALHOU: o defeito passou"); process.exit(falhas ? 0 : 1); }
console.log(falhas ? `❌ ${falhas} falha(s)` : "✅ Atualidades Certo/Errado verde"); process.exit(falhas ? 1 : 0);
