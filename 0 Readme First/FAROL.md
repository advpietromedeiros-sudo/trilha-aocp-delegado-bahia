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

## Próximas tarefas, em ordem

1. Espera da geração: o polling da tela (~240 s) é menor que a geração do servidor.
2. Servidor: `X-Frame-Options`/CSP `frame-ancestors`, `do_HEAD` bloqueado, validar `Content-Length`.
3. Stories: alternativa com estado acessível, modal com foco, menu lateral no celular.
4. README: `.env.exemplo` inexistente; seção "Arquivos" desatualizada.

## O que fica rodando

- Storybook (`npm run storybook`), porta 6006, iniciado pela sessão de 31/10/2026.
