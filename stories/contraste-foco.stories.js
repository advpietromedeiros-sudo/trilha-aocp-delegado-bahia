// Contraste e foco — APROVADO pelo titular em 31/10/2026 (D-003, docs/DECISOES.md) e aplicado no
// index.html, no bloco <style id="d003-contraste-foco">. A story mostra o app REAL: o CSS mora no
// app, não aqui. Mudou de aparência depois? Volta para "Aguardando Análise" (HARNESS §G6.5).
import { appFrame } from './_app.js';

export default {
  title: 'Aprovados/Contraste e foco (D-003)',
  render: (args) => appFrame(args),
  args: { view: 'study', dark: true, palette: 'oceano' },
  argTypes: {
    palette: { control: 'select', options: ['oceano', 'floresta', 'violeta', 'ambar'] },
    view: { control: 'select', options: ['study', 'dashboard', 'errors', 'base'] },
    dark: { control: 'boolean' },
  },
};

export const Escuro = { name: 'Escuro' };
export const Claro = { name: 'Claro', args: { dark: false } };
