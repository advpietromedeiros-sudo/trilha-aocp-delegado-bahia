// testar_lei_seca_ba.cjs — prova o COMPORTAMENTO do "Treino de Letra de Lei — Delegado PC-BA" em jsdom:
// dados íntegros (cada carta com texto, lacunas == respostas, rubrica e base; sem duplicatas), a tela inicial
// com os blocos, abrir um bloco e ver o artigo com lacunas ocultas, revelar (preenche em vermelho e mostra a
// base) e marcar "Lembrei" salvando o progresso por carta.
// Uso: node docs/testar_lei_seca_ba.cjs [--autoteste]  (0 = ok; --autoteste tira uma resposta e só sai 0 se ACUSAR)
let JSDOM, VirtualConsole;
try { ({ JSDOM, VirtualConsole } = require("jsdom")); } catch { console.log("⚠️ jsdom não instalado (npm ci): porta pulada"); process.exit(2); }
const fs = require("fs"), path = require("path");
const AUTO = process.argv.includes("--autoteste");
const dir = path.join(__dirname, "..", "discursiva");
let html = fs.readFileSync(path.join(dir, "Lei_Seca_Delegado_BA.html"), "utf8");
let dados = fs.readFileSync(path.join(dir, "lei_seca_delegado_ba_dados.js"), "utf8");
const tag = '<script src="lei_seca_delegado_ba_dados.js"></script>';
if (!html.includes(tag)) { console.log("falta a tag de lei_seca_delegado_ba_dados.js"); process.exit(1); }
if (AUTO) { const s = dados.replace('g:["lei","cominação"]', 'g:["lei"]'); if (s === dados) { console.log("AUTOTESTE: não plantou"); process.exit(1); } dados = s; }
html = html.replace(tag, () => "<script>" + dados + "</script>");

const vc = new VirtualConsole();
const dom = new JSDOM(html, { runScripts: "dangerously", url: "http://localhost/", pretendToBeVisual: true, virtualConsole: vc, beforeParse(w) { w.scrollTo = () => {}; } });
const w = dom.window, d = w.document;

let falhas = 0; const prova = (n, ok, det = "") => { console.log(`  ${ok ? "✅" : "❌"} ${n}${!ok && det ? " — " + det : ""}`); if (!ok) falhas++; };

const B = w.LEI_SECA;
prova("os dados carregam com os 12 blocos (edital inteiro + Bahia local)", Array.isArray(B) && B.length === 12, String(B && B.length));
const b1 = B[0];
const todos = B.flatMap(b => b.itens);
prova("há pelo menos 300 artigos no total", todos.length >= 300, String(todos.length));
const blocoBA = B.find(b => /Bahia/i.test(b.titulo || ""));
prova("há um bloco local da Bahia com pelo menos 100 cartas", !!blocoBA && blocoBA.itens.length >= 100, String(blocoBA && blocoBA.itens.length));
prova("o bloco local tem forte presença baiana (>= 50 cartas 'ba')", !!blocoBA && blocoBA.itens.filter(i => i.ba).length >= 50, String(blocoBA && blocoBA.itens.filter(i => i.ba).length));

// integridade: cada carta tem texto, rubrica, base e lacunas == respostas
const ruins = todos.filter(i => !i.t || !i.rub || !i.base || !Array.isArray(i.g) ||
  (String(i.t).match(/___/g) || []).length !== i.g.length);
prova("toda carta tem texto, rubrica, base e nº de lacunas igual ao de respostas", ruins.length === 0,
  ruins.slice(0, 3).map(i => (i.d || "") + " " + (i.art || "")).join(" | "));

// sem duplicatas (mesmo diploma+artigo+rubrica)
const vistos = new Set(); let dup = 0;
for (const i of todos) { const k = (i.d + "|" + i.art + "|" + i.rub).toLowerCase(); if (vistos.has(k)) dup++; vistos.add(k); }
prova("não há cartas duplicadas", dup === 0, String(dup));

// foco pedido: forte presença de artigos novos/atualizados
const novos = todos.filter(i => i.novo).length;
prova("há artigos novos/atualizados sinalizados (>= 10)", novos >= 10, String(novos));

// comportamento da tela
prova("a tela inicial mostra os blocos", !!d.querySelector("[data-bloco]"));
d.querySelector("[data-bloco]").click();
prova("abrir um bloco mostra o 1º artigo com lacunas e o botão Revelar",
  !!d.querySelector(".lei") && d.querySelectorAll(".lac").length >= 1 && !!d.querySelector("[data-rev]"));

// antes de revelar, as lacunas estão ocultas (sem a classe .on)
prova("as lacunas começam ocultas", d.querySelectorAll(".lac.on").length === 0);

// revelar: preenche em vermelho (.on) e mostra a base
d.querySelector("[data-rev]").click();
prova("revelar preenche as lacunas e mostra a base legal",
  d.querySelectorAll(".lac.on").length >= 1 && !!d.querySelector(".base"));

// marcar "Lembrei" salva o progresso
d.querySelector('[data-marca="ok"]').click();
let salvo = {}; try { salvo = JSON.parse(w.localStorage.getItem("leiseca:v1") || "{}"); } catch (e) {}
prova("marcar salva o progresso no navegador (localStorage)",
  salvo.resp && Object.keys(salvo.resp).length >= 1 && salvo.resp[b1.id + ":0"] && salvo.resp[b1.id + ":0"].ok === true,
  JSON.stringify(salvo.resp || {}).slice(0, 80));

// voltar à home mostra o progresso
d.querySelector("[data-home]").click();
prova("a home mostra o progresso do bloco", /\d+\/\d+ treinadas/.test(d.body.textContent));

if (AUTO) { console.log(falhas ? "AUTOTESTE OK: o defeito plantado foi acusado" : "AUTOTESTE FALHOU: o defeito passou"); process.exit(falhas ? 0 : 1); }
console.log(falhas ? `❌ ${falhas} falha(s)` : "✅ treino de letra de lei verde"); process.exit(falhas ? 1 : 0);
