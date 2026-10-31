// Proposta 1 — contraste e foco (revisão de 31/10/2026, itens 5, 9 e 15).
// Contrastes medidos pela fórmula WCAG 2.1 em 31/10/2026; o mínimo AA para texto pequeno é 4,5:1.
// Os botões usam --accent como FUNDO com texto branco, então --accent não se clareia: a proposta
// cria --accent-fg, só para TEXTO, e o aplica onde o contraste reprovava.
import { appFrame } from './_app.js';

const PROPOSTA_CSS = `
:root{--muted:#56677d;--focus:#2466ce}                        /* 4,16 → 5,33 sobre --bg */
.flowfooter{color:#5f7085}                                    /* 2,47 → 4,68 */
body:not(.dark){--green:#0f6e5a;--red:#a83a3a}                /* 4,12 → 5,51 · 4,39 → 5,69 */
:focus-visible{outline:3px solid var(--focus)!important;outline-offset:2px} /* anel 2,35 → 5,43 */
.sidebar-search input:focus-visible{outline:3px solid #8db8ff!important}
body.dark{--focus:#8db8ff;--accent-fg:#8db8ff;--green:#6fdcb4;--red:#ff9fa6}
body.dark[data-palette="floresta"]{--accent-fg:#5fdcbf}
body.dark[data-palette="violeta"]{--accent-fg:#c4b1ff}
body.dark[data-palette="ambar"]{--accent-fg:#f2c27a}
body.dark .option-hint,body.dark .small-button,body.dark .verification,body.dark .cutoff-alert,
body.dark .aocp-hit,body.dark .reference-analysis strong{color:var(--accent-fg)}
`;

export default {
  title: 'Nesta sessão/Contraste e foco',
  render: ({ proposta, ...args }) => appFrame({ ...args, extraCss: proposta ? PROPOSTA_CSS : '' }),
  args: { proposta: true, view: 'study', dark: true, palette: 'oceano' },
  argTypes: {
    proposta: { control: 'boolean', name: 'Aplicar proposta (desligue para comparar)' },
    palette: { control: 'select', options: ['oceano', 'floresta', 'violeta', 'ambar'] },
    view: { control: 'select', options: ['study', 'dashboard', 'errors', 'base'] },
    dark: { control: 'boolean' },
  },
};

export const EscuroComProposta = { name: 'Escuro — com proposta' };
export const EscuroAtual = { name: 'Escuro — atual', args: { proposta: false } };
export const ClaroComProposta = { name: 'Claro — com proposta', args: { dark: false } };
export const ClaroAtual = { name: 'Claro — atual', args: { dark: false, proposta: false } };
