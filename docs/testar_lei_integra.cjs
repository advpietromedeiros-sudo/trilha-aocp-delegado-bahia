// testar_lei_integra.cjs — prova o COMPORTAMENTO do módulo "Lei na Íntegra" (aba do Treino de Letra de Lei) em jsdom:
// dados íntegros (cada artigo com caput, título, base e ao menos uma palavra-chave {}), a home com os artigos, abrir
// um artigo e ver o leitor com a barra de 3 modos, o áudio e a base; Esconder revela a caixa clicada; Teste deixa
// UMA lacuna em foco; Revisão apaga o secundário, grifa o essencial e mostra o mnemônico; "Já domino" salva.
// Uso: node docs/testar_lei_integra.cjs [--autoteste]  (0 = ok; --autoteste tira as chaves de um artigo e só sai 0 se ACUSAR)
let JSDOM, VirtualConsole;
try { ({ JSDOM, VirtualConsole } = require("jsdom")); } catch { console.log("⚠️ jsdom não instalado (npm ci): porta pulada"); process.exit(2); }
const fs = require("fs"), path = require("path");
const AUTO = process.argv.includes("--autoteste");
const dir = path.join(__dirname, "..", "discursiva");
let html = fs.readFileSync(path.join(dir, "Lei_na_Integra.html"), "utf8");
let dados = fs.readFileSync(path.join(dir, "lei_integra_dados.js"), "utf8");
const tag = '<script src="lei_integra_dados.js"></script>';
if (!html.includes(tag)) { console.log("falta a tag de lei_integra_dados.js"); process.exit(1); }
if (AUTO) {
  const s = dados.replace("e {harmônicos} entre si, o {Legislativo}, o {Executivo} e o {Judiciário}",
                          "e harmônicos entre si, o Legislativo, o Executivo e o Judiciário");
  if (s === dados) { console.log("AUTOTESTE: não plantou"); process.exit(1); }
  dados = s;
}
html = html.replace(tag, () => "<script>" + dados + "</script>");

const vc = new VirtualConsole();
const dom = new JSDOM(html, { runScripts: "dangerously", url: "http://localhost/", pretendToBeVisual: true, virtualConsole: vc, beforeParse(w) { w.scrollTo = () => {}; } });
const w = dom.window, d = w.document;

let falhas = 0; const prova = (n, ok, det = "") => { console.log(`  ${ok ? "✅" : "❌"} ${n}${!ok && det ? " — " + det : ""}`); if (!ok) falhas++; };

const A = w.LEI_INTEGRA;
prova("os dados carregam com pelo menos 6 artigos", Array.isArray(A) && A.length >= 6, String(A && A.length));

// integridade: cada artigo tem d, art, titulo, caput, base, incisos[] e ao menos uma palavra-chave {}
const chaves = a => ((a.caput || "").match(/\{/g) || []).length
  + (a.incisos || []).reduce((s, i) => s + ((i.t || "").match(/\{/g) || []).length, 0)
  + (a.paragrafos || []).reduce((s, p) => s + ((p.t || "").match(/\{/g) || []).length, 0);
const ruins = (A || []).filter(a => !a.d || !a.art || !a.titulo || !a.caput || !a.base || !Array.isArray(a.incisos) || chaves(a) < 1);
prova("todo artigo tem d, art, título, caput, base, incisos e ao menos uma palavra-chave {}", ruins.length === 0,
  ruins.slice(0, 3).map(a => (a.d || "") + " " + (a.art || "")).join(" | "));

// as chaves {} são sempre fechadas (nenhuma { sem })
const desbalanceado = (A || []).filter(a => {
  const txt = [a.caput, ...(a.incisos || []).map(i => i.t), ...(a.paragrafos || []).map(p => p.t)].join(" ");
  return (txt.match(/\{/g) || []).length !== (txt.match(/\}/g) || []).length;
});
prova("as palavras-chave {} estão todas fechadas", desbalanceado.length === 0, desbalanceado.map(a => a.art).join(","));

// marca de incidência: há incisos com imp/destaque ("!")
const temImp = (A || []).some(a => (a.incisos || []).some(i => i.imp || i.destaque));
prova("há incisos marcados como mais cobrados (imp/destaque)", temImp);

// home mostra os artigos
prova("a home mostra a lista de artigos", d.querySelectorAll("[data-artigo]").length >= 6, String(d.querySelectorAll("[data-artigo]").length));

// abrir o art. 5º (o mais denso) — abre o leitor com barra de modos, áudio e base
const alvo = A.findIndex(a => a.art === "5º");
d.querySelector('[data-artigo="' + alvo + '"]').click();
prova("abrir um artigo mostra o leitor com os 3 modos, o áudio e a base legal",
  !!d.querySelector(".lei-full") && d.querySelectorAll("[data-modo]").length === 3 && !!d.querySelector("[data-som]") && !!d.querySelector(".base"));

// modo Esconder (padrão): lacunas presentes e começam ocultas
prova("no Esconder as lacunas aparecem e começam ocultas", d.querySelectorAll(".lac").length >= 3 && d.querySelectorAll(".lac.on").length === 0,
  d.querySelectorAll(".lac").length + " lac / " + d.querySelectorAll(".lac.on").length + " on");

// clicar numa lacuna revela (vira .on com o texto)
const primeira = d.querySelector(".lac");
primeira.click();
prova("clicar numa lacuna a revela (.on, com texto)", primeira.classList.contains("on") && primeira.textContent.length > 0, primeira.textContent);

// modo Teste: exatamente uma lacuna em foco
d.querySelector('[data-modo="teste"]').click();
prova("no Teste fica exatamente uma lacuna em foco", d.querySelectorAll(".lac.foco").length === 1, String(d.querySelectorAll(".lac.foco").length));

// modo Revisão: grifa o essencial e mostra o mnemônico
d.querySelector('[data-modo="revisao"]').click();
prova("no Revisão o essencial fica grifado e o mnemônico aparece", d.querySelectorAll(".gr").length >= 3 && !!d.querySelector(".mnem"),
  d.querySelectorAll(".gr").length + " grifos");

// "Já domino" salva o progresso no navegador
d.querySelector("[data-domino]").click();
let salvo = {}; try { salvo = JSON.parse(w.localStorage.getItem("leiintegra:v1") || "{}"); } catch (e) {}
prova("marcar \"Já domino\" salva o progresso (localStorage)", salvo.done && salvo.done["CF 5º"] === true, JSON.stringify(salvo.done || {}).slice(0, 60));

// voltar à home reflete o treinado
d.querySelector("[data-home]").click();
prova("a home mostra o artigo como treinado", /treinado/.test(d.body.textContent) && !!d.querySelector(".selo.feito"));

if (AUTO) { console.log(falhas ? "AUTOTESTE OK: o defeito plantado foi acusado" : "AUTOTESTE FALHOU: o defeito passou"); process.exit(falhas ? 0 : 1); }
console.log(falhas ? `❌ ${falhas} falha(s)` : "✅ Lei na Íntegra verde"); process.exit(falhas ? 1 : 0);
