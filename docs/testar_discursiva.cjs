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
// condução, estudo completo e texto oficial dos artigos (03/11/2026, D-015)
for (const f of ["conducao.js", "estudo.js", "artigos.js", "blocos.js"]) { const src = fs.readFileSync(path.join(dir, f), "utf8"); const tag = `<script src="${f}"></script>`; if (!html.includes(tag)) { console.log("falta a tag de " + f); process.exit(1); } html = html.replace(tag, () => "<script>" + src + "</script>"); }
// arquivo único para envio (04/11/2026): DISC_UNICO=caminho prova a versão empacotada por ferramentas/empacotar_discursiva.py
// simulados objetivos (04/11/2026, D-017): dados de terceiro só no disco; sem eles a aba avisa e o resto funciona
const htmlSemSim = html;
const arqSim = path.join(dir, "simulados_delta.js"), TEM_SIM = fs.existsSync(arqSim);
const tagSim = '<script src="simulados_delta.js" data-local="terceiro"></script>';
if (!html.includes(tagSim)) { console.log("falta a tag de simulados_delta.js"); process.exit(1); }
if (TEM_SIM) html = html.replace(tagSim, () => "<script>" + fs.readFileSync(arqSim, "utf8") + "</script>");
if (process.env.DISC_UNICO) html = fs.readFileSync(process.env.DISC_UNICO, "utf8");
if (AUTO) { const s = html.replace("const tec=Math.round(40*f/Math.max(1,tot))", "const tec=Math.round(4*f/Math.max(1,tot))"); if (s === html) { console.log("AUTOTESTE: não plantou"); process.exit(1); } html = s; }
const erros = [], vc = new VirtualConsole();
vc.on("jsdomError", e => erros.push(String(e.message || e)));
const dom = new JSDOM(html, { runScripts: "dangerously", url: "http://localhost/", virtualConsole: vc, pretendToBeVisual: true,
  beforeParse(w) { w.scrollTo = () => {}; w.alert = () => {}; w.confirm = () => true; w.addEventListener("error", ev => erros.push(ev.message)); } });
const w = dom.window, d = w.document, A = w.discAPI;
let falhas = 0; const prova = (n, ok, det = "") => { console.log(`  ${ok ? "✅" : "❌"} ${n}${!ok && det ? " — " + det : ""}`); if (!ok) falhas++; };
const clicar = id => d.getElementById(id).click();

prova("página carrega com as 6 abas e sem erro de JavaScript", d.querySelectorAll("#abas button").length === 6 && erros.length === 0, erros.join(" | "));
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
A.abrirPeca("preventiva", "escrever");
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
// peças complementares (03/11/2026): 18 peças, e a de inquérito usa cabeçalho e preâmbulo próprios
const novas = ["apf", "cautelar-diversa", "relatorio", "captacao", "sigilo-bancario", "localizacao-13b", "alienacao", "perfil-genetico", "internacao"];
prova("as 9 peças complementares estão na lista (18 no total; 12-C e 13-A viraram cartões)", A.PECAS.length === 18 && !A.PECAS.some(p => ["afastamento", "requisicao"].includes(p.id)) && novas.every(id => A.PECAS.some(p => p.id === id)), A.PECAS.map(p => p.id).join(","));
const intern = A.passosDe(A.PECAS.find(p => p.id === "internacao"));
prova("internação provisória: endereçada à Vara da Infância e com o passo dos direitos fundamentais", /INFÂNCIA E JUVENTUDE/.test(intern[0].modelo) && intern.some(s => /direito fundamental absoluto/.test(s.t)));
const apf = A.passosDe(A.PECAS.find(p => p.id === "apf"));
prova("despacho do flagrante: cabeçalho do APF (não de portaria) e checklist próprio do preâmbulo", /Auto de Prisão em Flagrante/.test(apf[0].modelo) && !/Portaria/.test(apf[0].modelo) && apf[1].check.some(c => /301 a 306/.test(c)));
A.abrirPeca("apf", "escrever");
for (let i = 0; i < apf.length; i++) { const tx = d.getElementById("txt"); tx.value = "Parte " + (i + 1) + " do despacho."; tx.dispatchEvent(new w.Event("input")); clicar("verModelo"); d.querySelectorAll("[data-chk]").forEach(c => { c.checked = true; c.dispatchEvent(new w.Event("change")); }); clicar("prox"); }
d.getElementById("lp").value = "10"; clicar("salvarNota");
prova("despacho do flagrante feito passo a passo até a nota 60/60", A.st().pecas.apf && A.st().pecas.apf.nota === 60, JSON.stringify(A.st().pecas.apf));
// condução "Entender o caso" (D-015): toda peça tem 5 etapas, cada pergunta com uma só alternativa certa, pistas que existem no enunciado
const semCond = A.PECAS.filter(p => { const c = A.CONDUCAO[p.id]; return !c || c.etapas.length !== 5 || c.etapas.some(e => !e.logica || !e.arts.length || e.qs.some(q => q.op.filter(o => o[1] === 1).length !== 1 || q.op.some(o => !o[2]))) || c.pistas.some(x => !p.enunciado.includes(x)); });
prova("toda peça tem condução em 5 etapas, perguntas com uma só certa e pistas tiradas do enunciado", semCond.length === 0, semCond.map(p => p.id).join(","));
const refs = [...new Set(Object.values(A.CONDUCAO).flatMap(c => c.etapas.flatMap(e => e.arts)).concat(Object.values(A.TEMAS).flatMap(t => (t.lei || []).concat(t.jur || []))))];
const semTexto = refs.filter(r => /^(SUM|SV)/.test(r) ? !A.JURIS[r] : !A.ARTIGOS[r]);
const semOficial = refs.filter(r => A.ARTIGOS[r] && A.ARTIGOS[r].falta);
prova(`${refs.length} artigos e súmulas citados: todos no artigos.js (${semOficial.length} só com link do Planalto)`, semTexto.length === 0, semTexto.join(","));
A.abrirPeca("preventiva");
prova("peça não conduzida abre na condução, com as pistas do enunciado em destaque", /Etapa 1 de 5/.test(d.body.textContent) && d.querySelectorAll(".enun mark").length === A.CONDUCAO.preventiva.pistas.length);
d.querySelector('[data-op="0.0:1"]').click();
prova("alternativa errada mostra o porquê e não libera a etapa", /Temporária|não decreta|Tente outra/.test(d.body.textContent) && d.querySelector(".op.errada") && d.getElementById("etProx").disabled);
for (let e = 0; e < 5; e++) { A.CONDUCAO.preventiva.etapas[e].qs.forEach((q, qi) => { const oi = q.op.findIndex(o => o[1] === 1); d.querySelector(`[data-op="${e}.${qi}:${oi}"]`).click(); }); if (e === 0) prova("acertando, aparece a lógica e o artigo oficial (CPP, art. 312, com a data do Planalto)", /A lógica:/.test(d.body.textContent) && /Redação oficial do Planalto, baixada em/.test(d.body.textContent) && /prisão preventiva poderá ser decretada/.test(d.body.textContent)); clicar("etProx"); }
prova("ao fim da condução, libera escrever a peça; e a peça já conduzida abre direto na escrita", /Você entendeu o caso/.test(d.body.textContent) && A.st().cond.preventiva.fim === 1 && (clicar("irEscrever"), !!d.getElementById("txt")) && (A.abrirPeca("preventiva"), !!d.getElementById("txt")));
const chip = d.querySelector('.arts [data-art]');
if (chip) chip.click();
prova("no passo da escrita, tocar no artigo abre o texto oficial", !!chip && /Redação oficial do Planalto/.test(d.querySelector(".lei-aberta").textContent));
// estudo completo
const semEstudo = A.PECAS.filter(p => !(A.ESTUDO[p.id] || []).length || A.ESTUDO[p.id].some(k => !A.TEMAS[k]));
const areas = new Set(Object.values(A.TEMAS).map(t => t.area));
prova("toda peça tem estudo completo, com temas existentes, e há Medicina Legal e Criminologia", semEstudo.length === 0 && areas.has("Medicina Legal") && areas.has("Criminologia"), semEstudo.map(p => p.id).join(","));
d.querySelector('[data-modo="estudo"]').click();
prova("estudo completo da peça: lei, doutrina, jurisprudência e objetiva, por área", ["Letra da lei", "Doutrina", "Jurisprudência", "Para a objetiva", "Medicina Legal", "Criminologia"].every(s => d.body.textContent.includes(s)) && /Súmula 676/.test(d.body.textContent));
clicar("estCartoes");
prova("do estudo, vai aos cartões e ao Certo/Errado da peça", /Memorize: Representação por prisão preventiva/.test(d.body.textContent));
prova("rótulos: 'CPP:312:§2' → CPP, art. 312, § 2º; 'CF:5:LXI' → CF, art. 5º, LXI; chave de 'Lei 9.296/96, art. 8º-A'", A.rotulo("CPP:312:§2") === "CPP, art. 312, § 2º" && A.rotulo("CF:5:LXI") === "CF, art. 5º, LXI" && A.chaveDe("Lei 9.296/96, art. 8º-A, I") === "L9296:8-A" && A.chaveDe("ECA, art. 108") === "L8069:108", [A.rotulo("CPP:312:§2"), A.rotulo("CF:5:LXI"), A.chaveDe("Lei 9.296/96, art. 8º-A, I")].join(" | "));
// Certo/Errado
A.ir("memoria"); clicar("ceTudo");
const item = d.querySelector(".flash .p").textContent, cart = A.CARTOES.find(c => c.ce[0] === item);
d.querySelector(`[data-ce="${cart.ce[1]}"]`).click();
prova("Certo/Errado: responder o gabarito certo mostra o comentário e o artigo", /Acertou/.test(d.getElementById("res").textContent) && d.getElementById("res").textContent.includes(cart.a));
// simulados objetivos comentados
if (process.env.DISC_UNICO) prova("arquivo único de envio NÃO leva os simulados (material de terceiro)", A.SIMS.length === 0 && !/const SIMULADOS\s*=/.test(html) && !/Projeto em Delta/.test(html.replace(/Fonte: Projeto em Delta/, "")));
else if (TEM_SIM) {
  const S = A.SIMS, mal = [];
  for (const sm of S) sm.questoes.forEach((q, i) => { if (q.n !== i + 1 || Object.keys(q.alts).join("") !== "ABCDE" || !"ABCDE".includes(q.gab) || !q.com.length || !q.disc || !q.enun.length) mal.push(sm.id + "#" + q.n); });
  prova(`${S.length} simulados × 100 questões: numeração, 5 alternativas, gabarito, comentário e disciplina`, S.length === 4 && mal.length === 0, mal.slice(0, 8).join(","));
  prova("nenhum número com forma de CPF nos dados (marca d'água retirada)", !/\d{3}\.?\d{3}\.?\d{3}-\d{2}/.test(JSON.stringify(S)));
  w.confirm = () => true;
  A.ir("simulados"); d.querySelector('[data-simabre="dpcba-1"][data-simmodo="prova"]').click();
  const q1 = S[0].questoes[0];
  d.querySelector(`[data-simalt="${q1.gab}"]`).click();
  prova("modo prova: marcar não mostra gabarito nem comentário", !d.querySelector(".com") && !!d.querySelector(".op.marcada"));
  const errada = "ABCDE".split("").find(k => k !== S[0].questoes[1].gab);
  clicar("simProx"); d.querySelector(`[data-simalt="${errada}"]`).click();
  clicar("entregar");
  const anul = S[0].questoes.filter(q => q.anulada).length;
  prova(`entregar: nota = 1 acerto + ${anul} anulada(s), no placar e no histórico`, d.getElementById("simNota").textContent === `${1 + anul}/100` && A.st().hist.some(h => h.t === "sim" && h.nota === 1 + anul), d.getElementById("simNota").textContent);
  clicar("revErros");
  prova("revisão só dos erros abre a questão 2 com gabarito e comentário", /Questão 2/.test(d.body.textContent) && !!d.querySelector(".com") && d.querySelector(".op.errada")?.dataset.simalt === errada);
  // tesoura (05/11/2026): elimina sem responder, a eliminada não se marca, e "Repor" desfaz; fica salva por questão
  A.abrirSim("dpcba-3", "prova"); const q3 = S[2].questoes[0], fora = "ABCDE".split("").find(k => k !== q3.gab);
  d.querySelector(`[data-simcut="${fora}"]`).click(); d.querySelector(`[data-simalt="${fora}"]`).click();
  prova("tesoura: alternativa eliminada fica riscada, não é marcada e o aviso diz como repor", d.querySelector(`[data-simalt="${fora}"]`).closest(".option-row").classList.contains("eliminated") && !A.st().sim["dpcba-3"].resp[1] && /eliminada/.test(d.getElementById("avisoSim").textContent));
  d.querySelector(`[data-simcut="${fora}"]`).click();
  prova("tesoura: 'Repor' devolve a alternativa", !d.querySelector(".option-row.eliminated") && JSON.stringify(A.st().sim["dpcba-3"].cut[1]) === "[]");
  prova("questão sem bloco de largura fixa (nenhum <pre> nos simulados)", !d.querySelector(".sq pre"));
  A.abrirSim("dpcba-2", "estudo"); const q2 = S[1].questoes[0];
  d.querySelector(`[data-simalt="${q2.gab}"]`).click();
  prova("modo estudo: escolher NÃO revela; só o botão Confirmar revela", !d.querySelector(".com") && !!d.getElementById("simConfirma"));
  clicar("simConfirma");
  { const red = S.flatMap(s => s.questoes.filter(q => q.atual && q.atual.nivel === "ajustada" && q.alt_orig).map(q => s.id + "#" + q.n));
    prova("auditoria de 04/11/2026: as 3 questões que a lei vigente deixou sem resposta única foram reescritas, com o original guardado", red.join(",") === "dpcba-1#85,dpcba-2#34,dpcba-4#94" && /multa consolidada/.test(S[0].questoes[84].alts.A) && /15\.487/.test(S[3].questoes[93].alts.C), red.join(",")); }
  A.abrirSim("dpcba-4", "estudo"); d.querySelector('[data-simir="94"]').click(); d.querySelector('[data-simalt="A"]').click(); clicar("simConfirma");
  prova("a nota de atualização aparece com o comentário (art. 241-D, Lei 15.487/2026)", /Questão atualizada para a lei vigente/.test(d.body.textContent) && /Texto original da alternativa C/.test(d.body.textContent));
  A.abrirSim("dpcba-2", "estudo"); d.querySelector('[data-simir="1"]').click();
  prova("modo estudo: responder mostra na hora o comentário e o gabarito", !!d.querySelector(".com") && d.querySelector(".fb.ok") && d.body.textContent.includes("Gabarito: " + q2.gab));
} else console.log("  ⚠️ simulados_delta.js ausente (material local): testes de conteúdo dos simulados pulados");
{
  const d2 = new JSDOM(htmlSemSim, { runScripts: "dangerously", url: "http://localhost/", pretendToBeVisual: true, beforeParse(w) { w.scrollTo = () => {}; } });
  d2.window.discAPI.ir("simulados");
  prova("sem os dados de terceiro, a aba Simulados avisa e não quebra", /não estão nesta cópia/.test(d2.window.document.body.textContent));
}
prova("nenhum erro de JavaScript em todo o fluxo", erros.length === 0, erros.join(" | "));

if (AUTO) { console.log(falhas ? "AUTOTESTE OK: o defeito plantado foi acusado" : "AUTOTESTE FALHOU: o defeito passou"); process.exit(falhas ? 0 : 1); }
console.log(falhas ? `❌ ${falhas} falha(s)` : "✅ treino de discursiva verde"); process.exit(falhas ? 1 : 0);
