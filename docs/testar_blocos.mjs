// testar_blocos.mjs — prova o COMPORTAMENTO dos blocos de 30, da baixa por correlação e do histórico
// (D-005, D-006, D-007; 31/10/2026).
//
// Extrai o script v8 REAL do index.html (HARNESS §A20) e o roda com o items.json de verdade, o
// estado do navegador simulado e um servidor falso — sem chamar API paga.
//
// Uso: node docs/testar_blocos.mjs   (0 = tudo certo, 1 = falha)
import { readFileSync } from "node:fs";

const html = readFileSync(new URL("../index.html", import.meta.url), "utf8");
const m = html.match(/<script>\s*\/\* v8 — blocos([\s\S]*?)<\/script>/);
if (!m) {
  console.log("❌ não achei o script v8 no index.html — o teste precisa ser revisto, não ignorado");
  process.exit(1);
}
const fonte = "/* v8 — blocos" + m[1];
const ITEMS = JSON.parse(readFileSync(new URL("../assets/items.json", import.meta.url), "utf8"));
const BY_ID = Object.fromEntries(ITEMS.map((x) => [x.id, x]));

let falhas = 0;
function prova(desc, ok, detalhe = "") {
  console.log(`  ${ok ? "✅" : "❌"} ${desc}${!ok && detalhe ? " — " + detalhe : ""}`);
  if (!ok) falhas++;
}

function ambiente() {
  const ctx = {
    state: { round: 1, answers: {}, gaps: {}, provider: "openai" },
    BY_ID, ITEMS, isFile: false,
    avisos: [], pedidos: [], historicos: [],
  };
  ctx.key = (i, r) => i + "|" + r;
  ctx.aOf = (it) => ctx.state.answers[ctx.key(it.id, ctx.state.round)];
  ctx.notify = (t) => ctx.avisos.push(t);
  ctx.save = () => {};
  ctx.esc = (s) => String(s).replace(/[&<>"']/g, (c) => ({ "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;", "'": "&#39;" })[c]);
  ctx.setView = () => {};
  ctx.loadItem = (id) => { ctx.carregado = id; };
  ctx.confirm = () => true;
  ctx.document = { addEventListener() {}, getElementById: () => null, querySelector: () => null };
  ctx.fetch = async (url, opt) => {
    const corpo = opt?.body ? JSON.parse(opt.body) : null;
    if (url === "/api/bloco") { ctx.pedidos.push(corpo.ids); ctx.modos = corpo.modos; return { ok: true, json: async () => ({ pedidos: corpo.ids.length }) }; }
    if (url === "/api/historico") { ctx.historicos.push(corpo.html); return { ok: true, json: async () => ({ arquivo: "historico/x.html" }) }; }
    if (url.startsWith("/api/question")) return { ok: true, json: async () => ({ status: "ready", question: { stem: "Enunciado <script>alert(1)</script>", options: { A: "a", B: "b", C: "c", D: "d", E: "e" } } }) };
    if (url === "/api/reveal") return { ok: true, json: async () => ({ commentary: { summary: "resumo", alternatives: { A: { veredito: "Correta", titulo: "t", explicacao: "e" } }, laws: [{ diploma: "CP", dispositivo: "art. 1º", texto_literal: "Não há crime sem lei anterior", explicacao: "x" }], jurisprudence: [], traps: ["p"], itens_correlatos: [] } }) };
    return { ok: false, json: async () => ({}) };
  };
  const nomes = Object.keys(ctx).filter((k) => !["avisos", "pedidos", "historicos", "carregado", "modos"].includes(k));
  // eslint-disable-next-line no-new-func
  const fab = new Function(...nomes, fonte + "\nreturn {aplicarCorrelatos,eCorrelato,pendentesParaBloco,criarBloco,progressoBloco,verificarGatilhoBloco,blocoAtual,secaoHistorico,montarHistoricoHTML,irAoProximoDoBloco};");
  return { ctx, f: fab(...nomes.map((n) => ctx[n])) };
}

const pen = ITEMS.filter((x) => x.discipline === "DIREITO PENAL");

// 1. baixa por correlação
{
  const { ctx, f } = ambiente();
  ctx.state.answers[ctx.key(pen[2].id, 1)] = { choice: "A", correct: "A", is_correct: true };
  const n = f.aplicarCorrelatos({ itens_correlatos: [pen[1].id, "INVENTADO-9", pen[0].id, pen[2].id, pen[1].id] }, pen[0].id);
  prova("correlação: só o id válido, nem o próprio ponto, nem o já respondido, nem repetição", n === 1 && f.eCorrelato(pen[1]) && !f.eCorrelato(pen[2]), `n=${n}`);
  prova("correlação avisa o titular", ctx.avisos.some((a) => /baixa por correlação/.test(a)));
  prova("comentário sem correlatos não quebra", f.aplicarCorrelatos({}, pen[0].id) === 0 && f.aplicarCorrelatos(undefined, pen[0].id) === 0);
}

// 2. blocos (modo sequencial: a ordem da trilha, como era até 01/11/2026)
{
  const { ctx, f } = ambiente();
  ctx.state.blocoIntercalar = false;
  ctx.state.answers[ctx.key(ITEMS[0].id, 1)] = { choice: "A", correct: "A", is_correct: true };
  ctx.state.correlatos = { [ctx.key(ITEMS[1].id, 1)]: { via: ITEMS[0].id } };
  const b1 = await f.criarBloco();
  prova("bloco 1 tem 30 pontos, na ordem da trilha, pulando respondido e correlato",
    b1.ids.length === 30 && b1.ids[0] === ITEMS[2].id && !b1.ids.includes(ITEMS[0].id) && !b1.ids.includes(ITEMS[1].id), b1.ids.slice(0, 3).join(","));
  // A regravação do histórico roda em segundo plano (não atrasa o bloco): espera as promessas pendentes.
  await new Promise((r) => setTimeout(r, 20));
  prova("o bloco é pedido ao servidor e o histórico é regravado", ctx.pedidos.length === 1 && ctx.historicos.length === 1, `pedidos=${ctx.pedidos.length} históricos=${ctx.historicos.length}`);
  const b2 = await f.criarBloco();
  prova("bloco 2 não repete nenhum ponto do bloco 1", b2.n === 2 && b2.ids.every((i) => !b1.ids.includes(i)) && b2.ids[0] === ITEMS[32].id);
  // pré-preparo aos 20
  const pedidosAntes = ctx.pedidos.length;
  for (const id of b2.ids.slice(0, 19)) ctx.state.answers[ctx.key(id, 1)] = { choice: "A", correct: "B", is_correct: false };
  f.verificarGatilhoBloco();
  prova("com 19 de 30 feitos, o próximo bloco ainda NÃO é preparado", ctx.pedidos.length === pedidosAntes);
  ctx.state.answers[ctx.key(b2.ids[19], 1)] = { choice: "A", correct: "A", is_correct: true };
  f.verificarGatilhoBloco(); f.verificarGatilhoBloco();
  await new Promise((r) => setTimeout(r, 0));
  prova("aos 20, o próximo bloco é preparado UMA vez (sem criar o bloco)", ctx.pedidos.length === pedidosAntes + 1 && f.blocoAtual().n === 2);
  const p = f.progressoBloco(f.blocoAtual());
  prova("progresso do bloco: 20 feitos (1 certo, 19 errados) de 30", p.feitos === 20 && p.ok === 1 && p.erro === 19 && p.total === 30, JSON.stringify(p));
  f.irAoProximoDoBloco();
  prova("'ir ao próximo do bloco' abre o 21º ponto", ctx.carregado === b2.ids[20]);
}

// 2b. 01/11/2026 — escolha de disciplina, assunto e modo; bloco intercalado (estudo horizontal)
{
  const { ctx, f } = ambiente();
  const discs = [...new Set(ITEMS.map((x) => x.discipline))];
  const b = await f.criarBloco();
  const d0 = b.ids.slice(0, Math.min(discs.length, 30)).map((i) => BY_ID[i].discipline);
  prova("intercalado por padrão: os primeiros pontos do bloco vêm de disciplinas diferentes", new Set(d0).size === d0.length && d0.length > 5, d0.slice(0, 4).join(" | "));
}
{
  const { ctx, f } = ambiente();
  const civ = ITEMS.filter((x) => x.discipline === discs0()[0]);
  ctx.state.modos = Object.fromEntries(ITEMS.filter((x) => x.discipline !== civ[0].discipline).map((x) => [x.id, "fora"]));
  ctx.state.modos[civ[1].id] = "ce";
  const b = await f.criarBloco();
  prova("'fora do bloco' tira os pontos; só a disciplina escolhida entra", b.ids.length === Math.min(30, civ.length) && b.ids.every((i) => BY_ID[i].discipline === civ[0].discipline), `${b.ids.length} pontos`);
  prova("o modo de cada ponto vai ao servidor (C/E rápido = 'ce', o resto 'obj')", ctx.modos && ctx.modos[civ[1].id] === "ce" && ctx.modos[civ[0].id] === "obj", JSON.stringify(ctx.modos && ctx.modos[civ[1].id]));
}
function discs0() { return [...new Set(ITEMS.map((x) => x.discipline))]; }

// 3. histórico
{
  const { ctx, f } = ambiente();
  ctx.state.answers[ctx.key(pen[0].id, 1)] = { choice: "B", correct: "A", is_correct: false, at: "2026-10-31T20:00:00Z" };
  const doc = await f.montarHistoricoHTML();
  prova("histórico é um HTML completo (o servidor exige <!doctype html>)", doc.startsWith("<!doctype html>") && doc.endsWith("</html>"));
  prova("histórico traz a questão, a resposta, o gabarito e a letra da lei",
    doc.includes(pen[0].number) && doc.includes("Sua resposta: <b>B</b>") && doc.includes("Não há crime sem lei anterior"));
  prova("texto do enunciado é ESCAPADO (nada de <script> vivo no arquivo)", !doc.includes("<script>alert(1)</script>") && doc.includes("&lt;script&gt;"));
}

console.log(falhas ? `❌ ${falhas} falha(s)` : "✅ blocos verdes — correlação, blocos, pré-preparo e histórico");
process.exit(falhas ? 1 : 0);
