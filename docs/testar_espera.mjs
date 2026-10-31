// testar_espera.mjs — prova o COMPORTAMENTO da espera pela geração (R-04, 31/10/2026).
//
// Extrai a função requestAndPoll REAL do index.html em tempo de execução (HARNESS §A20: conferir
// uma cópia não é conferir o original) e a roda contra um servidor simulado — sem chamar API paga.
// O relógio é simulado: cada espera de 2,4 s avança o tempo na hora.
//
// Uso: node docs/testar_espera.mjs   (0 = os 3 cenários passam, 1 = algum falhou)
import { readFileSync } from "node:fs";

const html = readFileSync(new URL("../index.html", import.meta.url), "utf8");
// Âncora que existe nas duas versões (antes e depois da correção): assim o teste também roda contra
// o código antigo e prova que FALHA nele — não apenas que "não achou" (REGRA CINCO).
const ancora = html.indexOf("let pollToken=0;");
const ini = ancora >= 0 ? ancora : html.indexOf("async function requestAndPoll");
const fim = html.indexOf("async function loadItem");
if (ini < 0 || fim < 0) {
  console.log("❌ não achei requestAndPoll no index.html — o teste precisa ser revisto, não ignorado");
  process.exit(1);
}
const fonte = html.slice(ini, fim);

async function cenario(nome, respostas, esperado) {
  let agora = 0;
  let consultas = 0;
  const eventos = { erro: null, pronta: false };
  const el = () => ({ innerHTML: "", textContent: "", querySelector: () => ({ insertAdjacentHTML() {} }) });
  const ctx = {
    isFile: false,
    state: { round: 1, current: "X", provider: "openai", gaps: {} },
    key: (i, r) => i + "|" + r,
    loaded: {},
    $: () => el(),
    showError: (titulo) => { eventos.erro = titulo; },
    renderQuestion: () => { eventos.pronta = true; },
    prefetchNext: () => {},
    loadItem: async () => {},
    Date: { now: () => agora },
    setTimeout: (fn, ms) => { agora += ms; fn(); },
    fetch: async (url) => {
      if (url === "/api/generate") return { json: async () => ({ status: "generating" }) };
      const r = respostas(consultas++);
      return { json: async () => r };
    },
  };
  const nomes = Object.keys(ctx);
  // eslint-disable-next-line no-new-func
  const fabrica = new Function(...nomes, fonte + "\nreturn requestAndPoll;");
  const requestAndPoll = fabrica(...nomes.map((n) => ctx[n]));
  await requestAndPoll("X");
  const ok = esperado(eventos, consultas, agora);
  const min = Math.round(agora / 60000);
  console.log(`  ${ok ? "✅" : "❌"} ${nome} — consultas: ${consultas}, tempo simulado: ${min} min, fim: ${eventos.pronta ? "questão pronta" : eventos.erro}`);
  return ok;
}

const resultados = [
  await cenario(
    "150 consultas 'generating' e depois 'ready': espera e mostra a questão (o código antigo desistia na 100ª)",
    (n) => (n < 150 ? { status: "generating" } : { status: "ready", question: { id: "X" } }),
    (e, n) => e.pronta && n === 151,
  ),
  await cenario(
    "'missing': encerra na 1ª consulta, com a mensagem de tarefa perdida",
    () => ({ status: "missing" }),
    (e, n) => !e.pronta && n === 1 && /perdeu/.test(e.erro ?? ""),
  ),
  await cenario(
    "'generating' para sempre: para no teto de 25 min",
    () => ({ status: "generating" }),
    (e, n, t) => !e.pronta && /Ainda não ficou pronta/.test(e.erro ?? "") && t >= 25 * 60000 && t < 26 * 60000,
  ),
];

const falhas = resultados.filter((ok) => !ok).length;
console.log(falhas ? `❌ ${falhas} cenário(s) falharam` : "✅ espera verde — 3 cenários");
process.exit(falhas ? 1 : 0);
