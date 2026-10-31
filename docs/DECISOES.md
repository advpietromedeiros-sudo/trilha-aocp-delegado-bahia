# DECISÕES — Trilha AOCP Delegado Bahia

> Registro de decisões do titular. Cada uma traz data, autor e o que trava enquanto estiver aberta.
> Decisão caduca quando a medição em que se apoiou muda (HARNESS §F49).

## Em aberto

Nenhuma em 31/10/2026, 17h36.

## Tomadas

### D-001 — Repositório remoto privado (31/10/2026, titular)

Resposta do titular, escolhida entre opções, em 31/10/2026: *"Privado"*. O repositório
`advpietromedeiros-sudo/trilha-aocp-delegado-bahia` é **privado**. Motivo registrado no
`LEIA_PRIMEIRO.md`: o pacote não deve ser publicado.

### D-002 — Assets derivados de terceiros ficam fora do Git (31/10/2026, titular)

Resposta do titular, escolhida entre opções, em 31/10/2026: *"Deixar fora do Git"*. Os arquivos
`assets/fontes_paginas.json`, `assets/lei_seca_material.json`, `assets/juris_aocp.json` e
`assets/exemplo_aocp.json` ficam só no disco (`.gitignore`). Consequência: um clone do repositório
**não** tem a base local completa — ela se reconstrói com `ferramentas/` a partir dos materiais
originais, que também não estão no Git.

### D-003 — Contraste e foco aprovados (31/10/2026, titular)

Aberta às 15h47 de 31/10/2026; aprovada às 17h34, resposta textual do titular à pergunta *"Proposta
de contraste e foco (D-003): aprova como está no Storybook?"*: *"2- sim"*. Aplicada no
`index.html` (bloco `<style id="d003-contraste-foco">`) sem mudar uma cor da proposta; a story foi
para `Aprovados/Contraste e foco (D-003)`. Contrastes medidos pela fórmula WCAG 2.1: todos os pares
acusados na revisão passam de 4,5:1 (texto) e o anel de foco de 2,35 para 5,43:1. 🔑 **Caduca**
(§F49) se a paleta mudar: a medição é desta paleta.

### D-004 — O caderno de erros mostra as tentativas refeitas (31/10/2026, titular)

Resposta textual do titular, em 31/10/2026, 17h34, à pergunta *"Caderno de erros: quer que ele
passe a mostrar as tentativas refeitas?"*: *"1- sim"*. Os erros guardados em `state.attempts` pelo
botão Refazer entram no caderno, marcados *"Tentativa refeita em dd/mm/aaaa"*. **A taxa de acerto
não muda:** o placar continua sendo a resposta atual de cada item.
