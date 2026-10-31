// O app como está hoje: a referência contra a qual cada melhoria se compara.
import { appFrame } from './_app.js';

export default {
  title: 'Aguardando Análise/App atual',
  render: (args) => appFrame(args),
  argTypes: {
    view: { control: 'select', options: ['study', 'dashboard', 'errors', 'base'] },
    dark: { control: 'boolean' },
    width: { control: 'select', options: ['100%', '1280px', '768px', '390px'] },
  },
};

export const Estudar = { args: { view: 'study' } };
export const Dashboard = { args: { view: 'dashboard' } };
export const CadernoDeErros = { name: 'Caderno de erros', args: { view: 'errors' } };
export const LeiSecaESumulas = { name: 'Lei seca & Súmulas', args: { view: 'base' } };
export const TemaEscuro = { name: 'Tema escuro', args: { view: 'study', dark: true } };
export const Celular = { name: 'Celular (390 px)', args: { view: 'study', width: '390px' } };
