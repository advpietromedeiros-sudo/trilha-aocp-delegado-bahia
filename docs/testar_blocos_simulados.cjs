// testar_blocos_simulados.cjs — prova o leitor discursiva/blocos.js (05/11/2026):
// (1) nenhum caractere do PDF se perde (multiconjunto de caracteres sem espaço, bloco a bloco);
// (2) texto corrido marcado como "pre" vira parágrafo, e o parágrafo partido é emendado (o caso da Medicina Legal, parecer);
// (3) tabela com colunas vira <table>; (4) nada sai em letra de largura fixa.
// Os dados reais (simulados_delta.js) são de terceiro e só existem na máquina do titular: sem eles, roda só os casos fixos.
// Uso: node docs/testar_blocos_simulados.cjs [--autoteste] [--previa arquivo.html]
const fs = require("fs"), path = require("path");
const AUTO = process.argv.includes("--autoteste");
// o projeto é "type": "module": carrega o arquivo como o navegador carrega (script comum), num contexto isolado
const vm = require("vm"), ctx = { window: {} };
vm.runInNewContext(fs.readFileSync(path.join(__dirname, "..", "discursiva", "blocos.js"), "utf8"), ctx);
const B = ctx.window.BLOCOS;
let falhas = 0; const prova = (n, ok, det = "") => { console.log(`  ${ok ? "✅" : "❌"} ${n}${!ok && det ? " — " + det : ""}`); if (!ok) falhas++; };
const sem = s => [...String(s).replace(/\s+/g, "")].sort().join("");
const texto = r => r.t === "tab" ? r.linhas.flat().join("") : r.t === "formula" ? r.linhas.join("") : r.x;
let html = B.html, analisar = B.analisar;
if (AUTO) analisar = l => B.analisar(l).map(r => r.t === "p" ? { ...r, x: r.x.slice(0, -1) } : r); // estraga: perde 1 caractere por parágrafo

// casos fixos (texto inventado para o teste, mesmo formato do importador)
const parte = [["p", "1. Preâmbulo. Nele, o parecerista qualifica a autoridade (juiz, delegado ou a parte interessada"],
  ["pre", "        que requereu a consulta) e os dados do processo.\n        2. Quesitos. Consiste na transcrição das perguntas\n        formuladas pela autoridade.\nErros das demais:"]];
const r1 = analisar(parte);
prova("parágrafo partido entre bloco normal e 'pre' é emendado", r1[0].x.includes("parte interessada que requereu a consulta)"), JSON.stringify(r1[0]));
prova("item numerado dentro do 'pre' vira item próprio, sem largura fixa", r1.some(r => r.t === "item" && r.x.startsWith("2. Quesitos") && r.x.includes("formuladas pela autoridade.")));
const tab = analisar([["pre", "Aspecto          Informação\nPrazo            Até 60 dias\n                 do recebimento\nEfeito           Arquivamento"]]);
prova("tabela de colunas vira <table>, com a linha de continuação na célula de cima", tab[0].t === "tab" && tab[0].linhas.length === 3 && tab[0].linhas[1][1] === "Até 60 dias do recebimento", JSON.stringify(tab));
prova("o HTML nunca usa <pre>", !/<pre/.test(html(parte)) && !/<pre/.test(html([["pre", "a  b\nc  d"]])));
prova("nenhum caractere perdido nos casos fixos", sem(parte.map(b => b[1]).join("")) === sem(r1.map(texto).join("")));

const arq = path.join(__dirname, "..", "discursiva", "simulados_delta.js");
if (fs.existsSync(arq)) {
  const t = fs.readFileSync(arq, "utf8"), S = JSON.parse(t.slice(t.indexOf("=") + 1).trim().replace(/;\s*$/, ""));
  const listas = [];
  for (const s of S) { for (const q of s.questoes) for (const c of ["enun", "com"]) if (q[c]) listas.push([s.id + "#" + q.n + ":" + c, q[c]]); for (const tb of s.textos) listas.push([s.id + ":texto" + tb.de, tb.blocos]); }
  const perdas = [], tipos = {}, previa = [];
  for (const [id, l] of listas) {
    const r = analisar(l);
    if (sem(l.filter(b => b[0] === "p" || b[0] === "pre").map(b => b[1]).join("")) !== sem(r.map(texto).join(""))) perdas.push(id);
    r.forEach(x => tipos[x.t] = (tipos[x.t] || 0) + 1);
    if (l.some(b => b[0] === "pre")) previa.push(`<h3>${id}</h3><div class="com">${html(l)}</div>`);
  }
  const nPre = listas.reduce((n, [, l]) => n + l.filter(b => b[0] === "pre").length, 0);
  console.log(`  ℹ️ ${listas.length} listas de blocos, ${nPre} blocos "pre" nos dados; saída por tipo: ${JSON.stringify(tipos)}`);
  prova(`nenhum caractere perdido em ${listas.length} listas de blocos dos 4 simulados`, perdas.length === 0, perdas.slice(0, 6).join(", "));
  const caso = S.flatMap(s => s.questoes).find(q => (q.com || []).some(b => b[0] === "pre" && /que requereu a consulta\)/.test(b[1])));
  if (caso) prova("o caso da imagem do titular (parecer médico-legal) sai emendado e sem largura fixa", analisar(caso.com).some(r => /parte interessada\s+que requereu a consulta\)/.test(r.x)));
  const i = process.argv.indexOf("--previa");
  if (i > 0) { fs.writeFileSync(process.argv[i + 1], `<!doctype html><meta charset="utf-8"><link rel="stylesheet" href="previa.css"><body>${previa.join("\n")}`); console.log("  prévia: " + process.argv[i + 1]); }
} else console.log("  ⚠️ simulados_delta.js ausente (material local): só os casos fixos rodaram");

if (AUTO) { console.log(falhas ? "AUTOTESTE OK: o defeito plantado foi acusado" : "AUTOTESTE FALHOU: o defeito passou"); process.exit(falhas ? 0 : 1); }
console.log(falhas ? `❌ ${falhas} falha(s)` : "✅ leitor de blocos verde"); process.exit(falhas ? 1 : 0);
