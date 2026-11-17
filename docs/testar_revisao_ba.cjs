// testar_revisao_ba.cjs — prova o COMPORTAMENTO do link "Revisão Dirigida — Delegado PC-BA" (15/11/2026), em jsdom:
// dados íntegros (cada assertiva com gabarito C/E válido, comentário e base legal; sem duplicatas), a tela inicial com
// os blocos, responder Certo/Errado mostrando o veredito e o comentário com a base, e o progresso salvo por bloco.
// Uso: node docs/testar_revisao_ba.cjs [--autoteste]  (0 = ok; --autoteste estraga um gabarito e só sai 0 se ACUSAR)
let JSDOM, VirtualConsole;
try { ({ JSDOM, VirtualConsole } = require("jsdom")); } catch { console.log("⚠️ jsdom não instalado (npm ci): porta pulada"); process.exit(2); }
const fs = require("fs"), path = require("path");
const AUTO = process.argv.includes("--autoteste");
const dir = path.join(__dirname, "..", "discursiva");
let html = fs.readFileSync(path.join(dir, "Revisao_Delegado_BA.html"), "utf8");
let dados = fs.readFileSync(path.join(dir, "revisao_delegado_ba_dados.js"), "utf8");
const tag = '<script src="revisao_delegado_ba_dados.js"></script>';
if (!html.includes(tag)) { console.log("falta a tag de revisao_delegado_ba_dados.js"); process.exit(1); }
if (AUTO) { const s = dados.replace('g:"C"', 'g:"X"'); if (s === dados) { console.log("AUTOTESTE: não plantou"); process.exit(1); } dados = s; }
html = html.replace(tag, () => "<script>" + dados + "</script>");

const vc = new VirtualConsole();
const dom = new JSDOM(html, { runScripts: "dangerously", url: "http://localhost/", pretendToBeVisual: true, virtualConsole: vc, beforeParse(w) { w.scrollTo = () => {}; } });
const w = dom.window, d = w.document;

let falhas = 0; const prova = (n, ok, det = "") => { console.log(`  ${ok ? "✅" : "❌"} ${n}${!ok && det ? " — " + det : ""}`); if (!ok) falhas++; };

const B = w.REV_DELBA;
prova("os dados carregam com os 6 blocos", Array.isArray(B) && B.length === 6, String(B && B.length));
const b1 = B[0];
const tamanhos = B.map(b => b.itens.length);
prova("os blocos têm 50, 50, 50, 50, 100 e 50 assertivas", JSON.stringify(tamanhos) === JSON.stringify([50, 50, 50, 50, 100, 50]), tamanhos.join(","));
const total = B.reduce((n, b) => n + b.itens.length, 0);
prova("o total é de 350 assertivas", total === 350, String(total));

// integridade de cada item (os dois blocos)
const todos = B.flatMap(b => b.itens);
const ruins = todos.filter(i => !i.a || !i.c || !i.base || (i.g !== "C" && i.g !== "E"));
prova("toda assertiva tem enunciado, gabarito C/E válido, comentário e base legal", ruins.length === 0, ruins.slice(0, 2).map(i => (i.a || "").slice(0, 40)).join(" | "));

// sem duplicatas (entre todos os 100)
const vistos = new Set(); let dup = 0;
for (const i of todos) { const k = (i.a || "").trim().toLowerCase(); if (vistos.has(k)) dup++; vistos.add(k); }
prova("não há assertivas duplicadas", dup === 0, String(dup));

// foco pedido: legislação local da Bahia e equilíbrio de gabaritos
const ba = b1.itens.filter(i => i.ba).length, err = b1.itens.filter(i => i.g === "E").length;
prova("há forte presença de legislação local da Bahia (>= 12 assertivas)", ba >= 12, String(ba));
prova("os gabaritos são variados (ao menos 12 'Errado')", err >= 12, String(err));
prova("os comentários funcionam como mini-aula (média de tamanho >= 180 caracteres)",
  b1.itens.reduce((s, i) => s + i.c.length, 0) / b1.itens.length >= 180);

// comportamento da tela
prova("a tela inicial mostra os blocos", !!d.querySelector("[data-bloco]"));
d.querySelector("[data-bloco]").click();
prova("abrir um bloco mostra a 1ª assertiva com os botões Certo e Errado", !!d.querySelector(".assert") && d.querySelectorAll("[data-ce]").length === 2);

// responder errado: veredito 'no', comentário e base aparecem
const it0 = b1.itens[0], marcaErrada = it0.g === "C" ? "E" : "C";
d.querySelector(`[data-ce="${marcaErrada}"]`).click();
prova("responder errado mostra o veredito negativo, o comentário e a base legal",
  !!d.querySelector(".fb.no") && !!d.querySelector(".com") && !!d.querySelector(".base"));

// navegar e responder certo: veredito 'ok' e progresso salvo
const nav = d.querySelector('[data-nav="1"]'); nav && nav.click();
const it1 = b1.itens[1]; d.querySelector(`[data-ce="${it1.g}"]`).click();
prova("responder certo mostra o veredito positivo", !!d.querySelector(".fb.ok"));
let salvo = {}; try { salvo = JSON.parse(w.localStorage.getItem("revdelba:v1") || "{}"); } catch (e) {}
prova("o progresso é salvo no navegador (localStorage)", salvo.resp && Object.keys(salvo.resp).length >= 2, JSON.stringify(Object.keys(salvo.resp || {})));

// voltar à home mostra o progresso do bloco
d.querySelector("[data-home]").click();
prova("a home mostra o progresso do bloco", /\d+\/50 feitas/.test(d.body.textContent));

if (AUTO) { console.log(falhas ? "AUTOTESTE OK: o defeito plantado foi acusado" : "AUTOTESTE FALHOU: o defeito passou"); process.exit(falhas ? 0 : 1); }
console.log(falhas ? `❌ ${falhas} falha(s)` : "✅ revisão Delegado-BA verde"); process.exit(falhas ? 1 : 0);
