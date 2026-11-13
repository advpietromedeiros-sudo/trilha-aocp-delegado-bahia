// testar_olho_de_aguia.cjs — prova o COMPORTAMENTO do Olho de Águia (12/11/2026, pedido do titular) em jsdom:
// simulados já resolvidos (correta marcada; trecho errado de cada alternativa errada grifado; nas que pedem a INCORRETA,
// só o gabarito grifado e as outras como verdadeiras), comentário esquematizado, blocos de 100 assertivas CORRETAS com
// pegadinha, metas do dia e "concluí o bloco". Com os dados reais no disco (fora do Git) prova também os 400 simulados e
// os blocos montados; sem eles (CI), usa um exemplo mínimo embutido aqui.
// Uso: node docs/testar_olho_de_aguia.cjs [--autoteste]  (0 = ok; --autoteste estraga o grifo e só sai 0 se ACUSAR)
let JSDOM, VirtualConsole;
try { ({ JSDOM, VirtualConsole } = require("jsdom")); } catch { console.log("⚠️ jsdom não instalado (npm ci): porta pulada"); process.exit(2); }
const fs = require("fs"), path = require("path");
const AUTO = process.argv.includes("--autoteste");
const dir = path.join(__dirname, "..", "discursiva");
let html = fs.readFileSync(path.join(dir, "Olho_de_Aguia.html"), "utf8");
const ARQ = { sim: "simulados_delta.js", marc: "olho_aguia_simulados.js", ass: "olho_aguia_assertivas.js" };
const REAL = !process.env.OLHO_EXEMPLO && Object.values(ARQ).every(f => fs.existsSync(path.join(dir, f)));  // OLHO_EXEMPLO=1 força o caminho da CI

// exemplo mínimo (CI): 1 simulado com uma questão comum e uma que pede a INCORRETA; 2 blocos de assertivas
const EX = {
  sim: `const SIMULADOS=[{"id":"dpcba-1","titulo":"Simulado 1 — DPC-BA","textos":[],"questoes":[
    {"n":1,"disc":"Direito Penal","tema":"Erro de proibição","enun":[["p","O erro de proibição:"]],"gab":"A","anulada":false,"com":[["p","CP, art. 21."]],
     "alts":{"A":"se escusável, isenta de pena.","B":"se escusável, torna atípica a conduta.","C":"se inescusável, isenta de pena.","D":"se inescusável, reduz pela metade.","E":"é irrelevante."}},
    {"n":2,"disc":"Legislação Penal Especial","tema":"Maria da Penha","enun":[["p","Assinale a INCORRETA."]],"gab":"D","anulada":false,"com":[["p","Súm. 589/STJ."]],
     "alts":{"A":"Verdade A.","B":"Verdade B.","C":"Verdade C.","D":"O STJ admite a insignificância nesses casos.","E":"Verdade E."}}]}];`,
  marc: `window.OLHO_SIM={"1":{"1":{"pede":"correta","alts":{"B":{"trecho":"torna atípica a conduta","certo":"isenta de pena","motivo":"CP, art. 21."},
    "C":{"trecho":"isenta de pena","certo":"reduz de 1/6 a 1/3","motivo":"CP, art. 21."},"D":{"trecho":"pela metade","certo":"de 1/6 a 1/3","motivo":"CP, art. 21."},
    "E":{"trecho":"é irrelevante","certo":"isenta ou reduz","motivo":"CP, art. 21."}},"esquema":{"ideia":"Erro sobre a **ilicitude**.","base":["CP, art. 21"],"pontos":["a","b"],"pegadinha":"p"}},
    "2":{"pede":"incorreta","alts":{"D":{"trecho":"admite a insignificância","certo":"não admite","motivo":"Súm. 589/STJ."},"A":{"verdadeira":true,"motivo":"ok"},
    "B":{"verdadeira":true,"motivo":"ok"},"C":{"verdadeira":true,"motivo":"ok"},"E":{"verdadeira":true,"motivo":"ok"}},"esquema":{"ideia":"i","base":[],"pontos":["a","b"]}}}};`,
  ass: `window.OLHO_ASSERTIVAS={"disciplinas":{"PEN":{"nome":"Penal","peso":7.25},"ADM":{"nome":"Administrativo","peso":8}},"blocos":[
    [{"id":"a1","d":"ADM","t":"Assertiva **correta** 1.","p":"Trocar X por Y.","po":0,"b":["Lei 1"],"m":"","tg":["lei"]},
     {"id":"a2","d":"PEN","t":"Assertiva correta 2.","p":"Versão errada original.","po":1,"b":[],"m":"","tg":["atual"]},
     {"id":"a3","d":"PEN","t":"Assertiva correta 3.","p":"","po":0,"b":[],"m":"Memorize isto.","tg":[]}],
    [{"id":"a4","d":"PEN","t":"Bloco dois.","p":"P.","po":0,"b":[],"m":"","tg":[]}]]};`
};
for (const [k, f] of Object.entries(ARQ)) {
  const tag = `<script src="${f}"></script>`;
  if (!html.includes(tag)) { console.log("falta a tag " + tag); process.exit(1); }
  html = html.replace(tag, () => "<script>" + (REAL ? fs.readFileSync(path.join(dir, f), "utf8") : EX[k]) + "</script>");
}
html = html.replace('<script src="../assets/grifa.js"></script>', () => "<script>" + fs.readFileSync(path.join(__dirname, "..", "assets", "grifa.js"), "utf8") + "</script>");
if (AUTO) {  // defeito plantado: o grifo do trecho errado some
  const s = html.replace("`<mark class=\"erro\">${esc(trecho)}</mark>`", "esc(trecho)");
  if (s === html) { console.log("AUTOTESTE: não plantou"); process.exit(1); }
  html = s;
}
const erros = [], vc = new VirtualConsole();
vc.on("jsdomError", e => erros.push(String(e.message || e)));
const dom = new JSDOM(html, { runScripts: "dangerously", url: "http://localhost/discursiva/Olho_de_Aguia.html", virtualConsole: vc, pretendToBeVisual: true,
  beforeParse(w) { w.scrollTo = () => {}; w.Element.prototype.scrollIntoView = () => {}; w.addEventListener("error", ev => erros.push(ev.message)); } });
const w = dom.window, d = w.document;
let falhas = 0; const prova = (n, ok, det = "") => { console.log(`  ${ok ? "✅" : "❌"} ${n}${!ok && det ? " — " + det : ""}`); if (!ok) falhas++; };
console.log(REAL ? "dados reais do disco" : "dados de exemplo (os reais ficam fora do Git)");

prova("página carrega sem erro de JavaScript, com metas, simulados e assertivas", erros.length === 0 && d.getElementById("metas").textContent.includes("Meta de hoje") && d.querySelectorAll(".alt").length >= 5 && d.querySelectorAll(".as").length > 0, erros.join(" | "));
prova("§G6.6: texto justificado nas assertivas e alternativas", /p,li,\.txt\{text-align:justify/.test(html));

// percorre TODAS as questões: correta em verde e sem grifo; erradas com o trecho exato grifado; INCORRETA com só o gabarito grifado
const SIM = w.eval("SIM"), MARC = w.OLHO_SIM;
let questoes = 0, ruins = [], incorretas = 0, didatica = [];
for (let s = 0; s < SIM.length; s++) {
  w.eval(`st.sim=${s};st.q=0`);
  for (let i = 0; i < SIM[s].questoes.length; i++) {
    w.eval(`st.q=${i};mostrarQuestao()`);
    const q = SIM[s].questoes[i], m = (MARC[SIM[s].id.replace("dpcba-", "")] || {})[String(q.n)];
    if (q.anulada) continue;
    questoes++;
    const ok = [...d.querySelectorAll(".alt.ok")], marcas = [...d.querySelectorAll("#sim mark.erro")].map(x => x.textContent);
    if (ok.length !== 1 || !ok[0].textContent.includes(q.gab)) { ruins.push(`S${s + 1} q${q.n}: correta não marcada`); continue; }
    if (!m) { ruins.push(`S${s + 1} q${q.n}: sem marcação`); continue; }
    if (m.pede === "incorreta") {
      incorretas++;
      if (marcas.length !== 1 || marcas[0] !== m.alts[q.gab].trecho || !ok[0].querySelector("mark.erro")) ruins.push(`S${s + 1} q${q.n}: INCORRETA deve grifar só o gabarito`);
    } else {
      const esperado = Object.keys(q.alts).filter(L => L !== q.gab).map(L => m.alts[L].trecho);
      if (marcas.length !== esperado.length || esperado.some((t, k) => marcas[k] !== t)) ruins.push(`S${s + 1} q${q.n}: grifo ${marcas.length} de ${esperado.length}`);
      if (ok[0].querySelector("mark.erro")) ruins.push(`S${s + 1} q${q.n}: grifo na correta`);
    }
    if (!d.querySelector(".esq h3") || d.querySelector(".esq h3").textContent.includes("em preparo")) ruins.push(`S${s + 1} q${q.n}: sem esquema`);
    // comentário didático (12/11/2026): cada errada com "o certo é" e "por quê"; a INCORRETA com aviso
    const erradas = m.pede === "incorreta" ? [ok[0]] : [...d.querySelectorAll("#sim .alt.ruim")];
    erradas.forEach(el => { const L = (el.querySelector(".l").textContent.match(/[A-E]/) || [])[0], a = m.alts[L] || {};
      if (a.certo && !/O certo é/i.test(el.textContent)) didatica.push(`S${s + 1} q${q.n} ${L}: sem "o certo é"`);
      if (a.motivo && !/Por quê/i.test(el.textContent)) didatica.push(`S${s + 1} q${q.n} ${L}: sem "por quê"`); });
    if ((m.pede === "incorreta") !== !!d.querySelector("#sim .aviso")) didatica.push(`S${s + 1} q${q.n}: aviso da INCORRETA`);
  }
}
prova("comentário didático: toda alternativa errada com \"o certo é\" e \"por quê\" em linhas próprias, e aviso só nas que pedem a INCORRETA", didatica.length === 0, didatica.slice(0, 5).join(" | "));
prova(`todas as ${questoes} questões: correta marcada, trecho errado grifado exatamente, ${incorretas} que pedem a INCORRETA com só o gabarito grifado, esquema presente`, questoes > 0 && incorretas > 0 && ruins.length === 0, ruins.slice(0, 5).join(" | "));
prova("negrito do esquema vira <b> (sem asteriscos na tela)", !d.getElementById("sim").textContent.includes("**"));

// assertivas
const OA = w.OLHO_ASSERTIVAS;
const tamanhos = OA.blocos.map(b => b.length);
prova("todo bloco tem no máximo 100 assertivas" + (REAL ? " e os cheios têm exatamente 100" : ""), tamanhos.every(n => n <= 100) && (!REAL || tamanhos.slice(0, -1).every(n => n === 100)), tamanhos.join(","));
if (REAL) {
  const b1 = OA.blocos[0], discs = new Set(b1.map(i => i.d)), cont = b1.reduce((a, i) => (a[i.d] = (a[i.d] || 0) + 1, a), {});
  prova("bloco 1 mistura todas as disciplinas, na proporção do peso (ADM e CON ≥ TRI, CPC e AMB)", discs.size === Object.keys(OA.disciplinas).length && cont.ADM >= cont.TRI && cont.CON >= cont.CPC && cont.PEN >= cont.AMB, JSON.stringify(cont));
  const s1 = b1.filter(i => i.d === "PEN").map(i => i.s), sN = OA.blocos[OA.blocos.length - 1].map(i => i.s);
  prova("dentro da disciplina, o mais importante vem antes (escore do bloco 1 ≥ do último)", Math.min(...s1) >= Math.max(...OA.blocos.slice(-20).flat().filter(i => i.d === "PEN").map(i => i.s).concat([0])) || Math.min(...s1) >= Math.max(...sN.concat([0])));
  prova("pegadinha em todas as assertivas dos blocos 1 a 20", OA.blocos.slice(0, 20).flat().every(i => i.p), OA.blocos.slice(0, 20).flat().filter(i => !i.p).length + " sem");
}
w.eval("st.bloco=0;mostrarBloco()");
const cards = [...d.querySelectorAll("#ass .as")], b0 = OA.blocos[0];
prova("o bloco aparece por disciplina, cada assertiva com a pegadinha (ou o memorize, se não houver)", cards.length === b0.length && d.querySelectorAll("#ass .disc").length === new Set(b0.map(i => i.d)).size &&
  cards.every((c, k) => b0[k].p ? !!c.querySelector(".peg") : (!b0[k].m || !!c.querySelector(".mem"))));
const iOrig = b0.findIndex(i => i.po);
prova("assertiva que era errada mostra a versão errada da banca ao lado da certa", iOrig < 0 || (!!cards[iOrig].querySelector(".velho") && !!cards[iOrig].querySelector(".cmp .lado.cer")));
prova("\"Para memorizar\" aparece em toda assertiva que o tem, mesmo com pegadinha", cards.every((c, k) => !b0[k].m || !!c.querySelector(".mem")));
const antes = d.getElementById("metas").textContent;
d.getElementById("concluir").click();
prova("\"Concluí este bloco\" conta na meta de hoje e vai para o próximo bloco", d.getElementById("metas").textContent.includes("1/" + OA.blocos.length + " blocos") && w.eval("st.bloco") === 1 && antes !== d.getElementById("metas").textContent);
w.eval("st.sim=0;st.q=0;mostrarQuestao()");
d.dispatchEvent(new w.KeyboardEvent("keydown", { key: "ArrowRight", bubbles: true }));
prova("→ passa a questão e a conta como lida", w.eval("st.q") === 1 && Object.keys(w.eval("st.lidas")).length === 1);
// abas (pedido do titular, 12/11/2026, 08h12: "fica confuso em duas telas... coloque em abas, abre uma tela ou outra")
const abas = [...d.querySelectorAll("#abas button")], css = d.querySelector("style").textContent;
abas.find(b => b.dataset.painel === "ass").click();
const qAntes = w.eval("st.q");
d.dispatchEvent(new w.KeyboardEvent("keydown", { key: "ArrowRight", bubbles: true }));
prova("duas abas, uma tela por vez: na aba Assertivas, a de Simulados some e → não mexe nos simulados", abas.length === 2 && d.body.dataset.painel === "ass" &&
  /body\[data-painel=sim\] #pAss,body\[data-painel=ass\] #pSim\{display:none\}/.test(css) && w.eval("st.q") === qAntes && abas[1].classList.contains("on") && !abas[0].classList.contains("on"));
abas.find(b => b.dataset.painel === "sim").click();
prova("a aba escolhida fica guardada para a próxima vez", d.body.dataset.painel === "sim" && w.eval("st.aba") === "sim");
prova("tecla G: paleta de grifos presente", !!w.Grifa);
prova("nenhum erro de JavaScript em todo o fluxo", erros.length === 0, erros.join(" | "));

if (AUTO) { if (falhas) { console.log(`✅ AUTOTESTE: o teste ACUSOU o grifo estragado (${falhas} falha(s))`); process.exit(0); } console.log("❌ AUTOTESTE: o teste NÃO acusou o grifo estragado"); process.exit(1); }
console.log(falhas ? `❌ Olho de Águia: ${falhas} falha(s)` : "✅ Olho de Águia verde");
process.exit(falhas ? 1 : 0);
