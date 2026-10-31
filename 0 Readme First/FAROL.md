# FAROL — Trilha AOCP Delegado Bahia

> Estado, tarefas e o que ficou rodando. Atualizado a cada ~15 min de trabalho e no fechamento.

**Última atualização:** 31/10/2026, 17h37.

## Estado

- Git iniciado em 31/10/2026; remoto privado (D-001). Governança do roteiro de fundação adotada
  (harness, hooks, portão, CI) — CI verde no commit `4794a16`.
- Storybook 10.6.5 instalado; stories em `stories/`. Node 26.13.0 instalado na máquina.
- Revisão completa do código feita em 31/10/2026: 25 itens. Os de severidade alta estão abaixo.
- ✅ **31/10/2026, 17h31 — corrigidos no `index.html`, com assertiva no portão
  (`docs/verificar_regressoes.py`, que acusa os dois no código antigo):**
  - **R-01** "Refazer" apagava a resposta sem rastro: agora a tentativa vai para `state.attempts`
    (salvo no navegador e no backup JSON) e o rótulo diz "a tentativa fica no histórico";
  - **R-02** atalhos A–E ignoram Ctrl/Cmd/Alt e só valem na aba Estudar.
  - **R-03** (D-004, 17h37) o caderno de erros mostra as tentativas refeitas, marcadas com a data;
    a taxa de acerto não muda. O **dashboard** continua lendo só a resposta atual.
  - ⚠️ **Camada:** corrigido no **arquivo**; o titular vê a mudança ao **recarregar** a página do app
    (o `servidor.py` serve o `index.html` do disco).
- ✅ **31/10/2026, 17h37 — contraste e foco aplicados** (D-003): bloco
  `<style id="d003-contraste-foco">` no `index.html`; story em `Aprovados/Contraste e foco (D-003)`.

- ✅ **31/10/2026, 17h42 — espera pela geração corrigida** (R-04): a tela espera enquanto o
  servidor disser `generating` (teto de 25 min), encerra na hora em `missing`, mostra "Gerando há
  X min Y s" (anunciado ao leitor de tela) e mantém um laço por vez. Provado por comportamento:
  `docs/testar_espera.mjs` roda a função **real** contra servidor simulado — 3 de 3 no código novo,
  0 de 3 no antigo.

## Próximas tarefas, em ordem

1. Servidor: `X-Frame-Options`/CSP `frame-ancestors`, `do_HEAD` bloqueado, validar `Content-Length`.
2. Stories: alternativa com estado acessível, modal com foco, menu lateral no celular.
3. README: `.env.exemplo` inexistente; seção "Arquivos" desatualizada.
4. **Blocos de 30 questões** — viável (`docs/VIABILIDADE_BLOCOS_30.md`, 31/10/2026). Aguarda 3
   decisões do titular: baixa por correlação automática ou confirmada; arquivo acumulado só no app
   ou também HTML/PDF; manter a auditoria dupla. Primeiro passo técnico: indexar o acervo grande da
   pasta DELEGADO BA (7.034 páginas, somadas em 31/10/2026, que hoje não entram na geração — sem
   contar os 42 resumos dentro dos ZIPs PCPR).

## O que fica rodando

- Storybook (`npm run storybook`), porta 6006, iniciado pela sessão de 31/10/2026.
