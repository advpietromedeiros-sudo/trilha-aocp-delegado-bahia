# FAROL — Trilha AOCP Delegado Bahia

> Estado, tarefas e o que ficou rodando. Atualizado a cada ~15 min de trabalho e no fechamento.

**Última atualização:** 31/10/2026, 17h31.

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
  - ⚠️ **Camada:** corrigido no **arquivo**; o titular vê a mudança ao **recarregar** a página do app
    (o `servidor.py` serve o `index.html` do disco). O caderno de erros e o dashboard ainda **não
    leem** `state.attempts` — a tentativa refeita fica guardada, mas não aparece na tela.

## Próximas tarefas, em ordem

1. Aguardar D-003 (proposta de contraste e foco) e aplicar no `index.html`.
2. Decidir com o titular se o caderno de erros deve mostrar as tentativas refeitas (`state.attempts`).
3. Espera da geração: o polling da tela (~240 s) é menor que a geração do servidor.
4. Servidor: `X-Frame-Options`/CSP `frame-ancestors`, `do_HEAD` bloqueado, validar `Content-Length`.
5. Stories: alternativa com estado acessível, modal com foco, menu lateral no celular.
6. README: `.env.exemplo` inexistente; seção "Arquivos" desatualizada.

## O que fica rodando

- Storybook (`npm run storybook`), porta 6006, iniciado pela sessão de 31/10/2026.
