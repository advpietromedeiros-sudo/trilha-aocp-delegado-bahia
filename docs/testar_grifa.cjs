// testar_grifa.cjs — prova o COMPORTAMENTO da paleta de grifos (assets/grifa.js, 10/11/2026) em jsdom:
// G abre e fecha · G dentro de campo de texto e Ctrl+G não abrem · selecionar com a cor ativa grifa e salva ·
// a tela se redesenha e o grifo VOLTA sozinho · trecho repetido sem o mesmo contexto NÃO é grifado (não grifa o
// lugar errado) · borracha apaga · "Limpar esta tela" pede confirmação na própria paleta · Esc fecha ·
// e as telas reais (Treino de Discursiva e molde da Revisão) abrem a paleta com G.
// Uso: node docs/testar_grifa.cjs [--autoteste]
//   --autoteste planta 3 defeitos (contexto ignorado; grifo não volta após redesenho; G abre dentro de campo) e só
//   sai 0 se CADA um for acusado.
let JSDOM;
try { ({ JSDOM } = require("jsdom")); } catch { console.log("⚠️ jsdom não instalado (npm ci): porta pulada"); process.exit(2); }
const fs = require("fs"), path = require("path");
const RAIZ = path.join(__dirname, "..");
const FONTE = fs.readFileSync(path.join(RAIZ, "assets", "grifa.js"), "utf8");
const AUTO = process.argv.includes("--autoteste");
const espera = ms => new Promise(r => setTimeout(r, ms));
let conferidas = 0;

const PAGINA = `<!doctype html><html lang="pt-BR"><head><meta charset="utf-8"></head><body>
<main id="m"><p id="p1">A prescrição da pretensão punitiva regula-se pelo máximo da pena cominada ao crime.</p>
<p id="p2">Prazo de cinco anos para a Administração anular seus atos, salvo má-fé.</p>
<p id="p3">Outro parágrafo também fala em prazo de cinco anos, mas em outro contexto.</p></main>
<input id="campo" value="texto"></body></html>`;

function abrir(js) {
  const dom = new JSDOM(PAGINA, { runScripts: "dangerously", url: "http://localhost/tela-teste.html", pretendToBeVisual: true });
  const s = dom.window.document.createElement("script"); s.textContent = js; dom.window.document.body.appendChild(s);
  return dom;
}
function tecla(w, alvo, key, extra = {}) { alvo.dispatchEvent(new w.KeyboardEvent("keydown", { key, bubbles: true, ...extra })); }
function selecionar(w, no, ini, fim) {
  const d = w.document, r = d.createRange(); r.setStart(no, ini); r.setEnd(no, fim);
  const sel = w.getSelection(); sel.removeAllRanges(); sel.addRange(r);
  no.parentNode.dispatchEvent(new w.MouseEvent("mouseup", { bubbles: true }));
}
const textoDe = (d, sel) => [...d.querySelectorAll(sel)].map(m => m.textContent).join("|");

async function suite(js) {
  const falhas = [], ok = (nome, cond, det = "") => { conferidas++; if (!cond) falhas.push(nome + (det ? " — " + det : "")); };
  const dom = abrir(js), w = dom.window, d = w.document;
  await espera(20);
  ok("expõe window.Grifa", !!w.Grifa);
  // 1) G abre; Ctrl+G e G no campo não abrem
  tecla(w, d.getElementById("campo"), "g");
  ok("G dentro de campo de texto NÃO abre a paleta", !d.getElementById("grf-paleta") || d.getElementById("grf-paleta").hidden);
  tecla(w, d.body, "g", { ctrlKey: true });
  ok("Ctrl+G NÃO abre a paleta", !d.getElementById("grf-paleta") || d.getElementById("grf-paleta").hidden);
  tecla(w, d.body, "g");
  const pal = d.getElementById("grf-paleta");
  ok("G abre a paleta", pal && !pal.hidden);
  ok("paleta com 9 cores, negrito, sublinhado e borracha", pal && pal.querySelectorAll(".grf-cor").length === 9 && !!pal.querySelector('[data-ferramenta="borracha"]') &&
    !!pal.querySelector('[data-ferramenta="negrito"]') && !!pal.querySelector('[data-ferramenta="sublinhado"]'));
  ok("aberta, a página reserva a faixa da barra (não cobre o conteúdo)", d.documentElement.classList.contains("grf-reserva"));
  ok("paleta é uma barra de ferramentas com nome", pal && pal.getAttribute("role") === "toolbar" && !!pal.getAttribute("aria-label"));
  // 2) selecionar com a cor ativa grifa e salva
  pal.querySelector('[data-ferramenta="verde"]').click();
  const t2 = d.getElementById("p2").firstChild, alvo = "cinco anos";
  const i2 = t2.nodeValue.indexOf(alvo);
  selecionar(w, t2, i2, i2 + alvo.length);
  await espera(20);
  ok("selecionar grifa o trecho na cor escolhida", textoDe(d, "#p2 mark.grf-verde") === alvo, textoDe(d, "#p2 mark.grf"));
  ok("o grifo fica salvo no navegador", w.Grifa.lista().length === 1 && w.Grifa.lista()[0].t === alvo);
  ok("o p3 (mesma frase, outro lugar) não é grifado junto", d.querySelectorAll("#p3 mark.grf").length === 0);
  // 3) a tela se redesenha: o grifo volta, no lugar certo
  const m = d.getElementById("m"), html = m.innerHTML.replace(/<mark[^>]*>|<\/mark>/g, "");
  m.innerHTML = html;
  ok("redesenho apaga o grifo da tela (pré-condição)", d.querySelectorAll("mark.grf").length === 0);
  await espera(400);
  ok("o grifo VOLTA sozinho depois do redesenho", textoDe(d, "#p2 mark.grf-verde") === alvo, textoDe(d, "mark.grf"));
  ok("e volta só no lugar certo (não no p3)", d.querySelectorAll("#p3 mark.grf").length === 0);
  // 4) recarregar a página (novo documento, mesmo navegador): volta
  const dom2 = new JSDOM(PAGINA, { runScripts: "dangerously", url: "http://localhost/tela-teste.html", pretendToBeVisual: true });
  dom2.window.localStorage.setItem(w.Grifa.chave, w.localStorage.getItem(w.Grifa.chave));
  const s2 = dom2.window.document.createElement("script"); s2.textContent = js; dom2.window.document.body.appendChild(s2);
  await espera(30);
  ok("ao reabrir a tela, o grifo salvo aparece", textoDe(dom2.window.document, "#p2 mark.grf-verde") === alvo);
  // 5) trecho repetido cujo contexto sumiu: não grifa em lugar nenhum
  m.innerHTML = '<p id="q1">Prazo de cinco anos aqui.</p><p id="q2">E prazo de cinco anos ali.</p>';
  await espera(400);
  ok("trecho repetido SEM o contexto salvo não é grifado (não arrisca o lugar errado)", d.querySelectorAll("mark.grf").length === 0, textoDe(d, "mark.grf"));
  m.innerHTML = html; await espera(400);
  // 6) borracha apaga
  pal.querySelector('[data-ferramenta="borracha"]').click();
  const mk = d.querySelector("#p2 mark.grf");
  ok("há grifo para apagar (pré-condição)", !!mk);
  if (mk) mk.dispatchEvent(new w.MouseEvent("click", { bubbles: true }));
  ok("borracha apaga da tela", d.querySelectorAll("mark.grf").length === 0);
  ok("borracha apaga do navegador", w.Grifa.lista().length === 0);
  ok("o texto volta inteiro, sem perder caractere", d.getElementById("p2").textContent === "Prazo de cinco anos para a Administração anular seus atos, salvo má-fé.");
  // 7) limpar a tela pede confirmação na paleta
  pal.querySelector('[data-ferramenta="amarelo"]').click();
  const t1 = d.getElementById("p1").firstChild; selecionar(w, t1, 2, 12); await espera(20);
  ok("segundo grifo criado (pré-condição)", w.Grifa.lista().length === 1);
  const lp = pal.querySelector(".grf-limpar"); lp.click();
  ok("1º clique em Limpar só pede confirmação", w.Grifa.lista().length === 1 && /Confirmar/.test(lp.getAttribute("aria-label") || ""));
  ok("o pedido de confirmação aparece na tela, ao lado da barra", !pal.querySelector(".grf-aviso").hidden && /Confirmar/.test(pal.querySelector(".grf-aviso").textContent));
  lp.click();
  ok("2º clique apaga todos", w.Grifa.lista().length === 0 && d.querySelectorAll("mark.grf").length === 0);
  // 7b) negrito e sublinhado (14/11/2026): marcam sem pintar o fundo e somam-se a uma cor no mesmo trecho
  w.Grifa.limparTela(); m.innerHTML = html; await espera(20);
  try {
  const t1b = () => d.getElementById("p1").firstChild;
  pal.querySelector('[data-ferramenta="lilas"]').click(); selecionar(w, t1b(), 2, 12); await espera(20);
  const corTxt = textoDe(d, "#p1 mark.grf-lilas");
  pal.querySelector('[data-ferramenta="negrito"]').click();
  const lil = d.querySelector("#p1 mark.grf-lilas").firstChild; selecionar(w, lil, 0, lil.nodeValue.length); await espera(20);
  const neg = d.querySelector("#p1 mark.grf-negrito");
  ok("negrito por cima de um grifo colorido: os dois ficam (cor + negrito no mesmo trecho)", !!neg && textoDe(d, "#p1 mark.grf-negrito") === corTxt && !!d.querySelector("#p1 mark.grf-lilas") && w.Grifa.lista().length === 2);
  ok("negrito não pinta o fundo e deixa a letra em negrito", !!neg && neg.classList.contains("grf-letra") && /mark\.grf\.grf-letra\{background:transparent/.test(d.getElementById("grf-estilo").textContent) && /mark\.grf-negrito\{font-weight:800/.test(d.getElementById("grf-estilo").textContent));
  pal.querySelector('[data-ferramenta="sublinhado"]').click();
  const t3 = d.getElementById("p2").firstChild; selecionar(w, t3, 0, 5); await espera(20);
  ok("sublinhado marca o trecho escolhido e fica salvo", !!d.querySelector("#p2 mark.grf-sublinhado") && /text-decoration:underline/.test(d.getElementById("grf-estilo").textContent) && w.Grifa.lista().some(g => g.cor === "sublinhado"));
  m.innerHTML = html; await espera(400);
  ok("negrito e sublinhado voltam depois do redesenho", !!d.querySelector("#p1 mark.grf-negrito") && !!d.querySelector("#p2 mark.grf-sublinhado"));
  w.Grifa.limparTela();
  ok("o texto volta inteiro depois de apagar negrito, cor e sublinhado", d.getElementById("p2").textContent === "Prazo de cinco anos para a Administração anular seus atos, salvo má-fé." && d.querySelectorAll("mark.grf").length === 0);
  } catch (e) { ok("negrito/sublinhado sem erro", false, String(e && e.message || e)); }
  // 8) Esc e G fecham
  tecla(w, d.body, "Escape"); ok("Esc fecha a paleta", pal.hidden);
  tecla(w, d.body, "G"); ok("G maiúsculo também abre", !pal.hidden);
  tecla(w, d.body, "g"); ok("G de novo fecha", pal.hidden);
  ok("fechada, a faixa reservada some", !d.documentElement.classList.contains("grf-reserva"));
  return falhas;
}

// as telas reais: o bloco embutido abre a paleta com G e não quebra a página
async function telasReais() {
  const falhas = [];
  const casos = [["discursiva/Treino_Discursiva.html", "http://localhost/discursiva/Treino_Discursiva.html"],
    ["revisao/molde/caderno.html", "http://localhost/revisao/molde/caderno.html"]];
  for (const [arq, url] of casos) {
    const h = fs.readFileSync(path.join(RAIZ, arq), "utf8");
    const i = h.indexOf("<!-- grifa:inicio"), f = h.indexOf("<!-- grifa:fim -->");
    if (i < 0 || f < i) { falhas.push(arq + ": sem o bloco embutido"); continue; }
    const pagina = "<!doctype html><html><body><p>Tela real</p>" + h.slice(i, f) + "</body></html>";
    const dom = new JSDOM(pagina, { runScripts: "dangerously", url, pretendToBeVisual: true });
    await espera(20);
    tecla(dom.window, dom.window.document.body, "g");
    const pal = dom.window.document.getElementById("grf-paleta");
    if (!pal || pal.hidden) falhas.push(arq + ": G não abriu a paleta com o bloco embutido");
  }
  return falhas;
}

const SABOTAGENS = [
  ["contexto ignorado (grifa o primeiro que achar)", s => s.replace("if (vistos > 1 && nota < 2) return -1;", "")],
  ["grifo não volta depois do redesenho", s => s.replace("function agendar() { if (!agendado) agendado = setTimeout(aplicar, 250); }", "function agendar() {}")],
  ["G abre dentro de campo de texto", s => s.replace("if (e.ctrlKey || e.metaKey || e.altKey || campo(e.target)) return;", "if (e.ctrlKey || e.metaKey || e.altKey) return;")],
];

(async () => {
  if (AUTO) {
    let todos = true;
    for (const [nome, f] of SABOTAGENS) {
      const js = f(FONTE);
      if (js === FONTE) { console.log("AUTOTESTE: não plantou — " + nome); process.exit(1); }
      const falhas = await suite(js);
      console.log(`  ${falhas.length ? "✅ acusou" : "❌ NÃO acusou"}: ${nome}${falhas.length ? " (" + falhas[0] + ")" : ""}`);
      if (!falhas.length) todos = false;
    }
    console.log(todos ? "AUTOTESTE OK: os 3 defeitos plantados foram acusados" : "AUTOTESTE FALHOU");
    process.exit(todos ? 0 : 1);
  }
  const falhas = [...await suite(FONTE), ...await telasReais()];
  if (falhas.length) { for (const f of falhas) console.log("  ❌ " + f); console.log(`FALHA: ${falhas.length} conferência(s)`); process.exit(1); }
  console.log(`OK: paleta de grifos — ${conferidas} conferências de comportamento e 2 telas reais`);
})();
