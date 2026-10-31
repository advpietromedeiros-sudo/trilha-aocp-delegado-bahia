export default {
  parameters: {
    layout: 'fullscreen',
    options: {
      // Ordem do HARNESS §G6.5: as stories se organizam por estado de aprovação.
      storySort: { order: ['Nesta sessão', 'Aguardando Análise', 'Aprovados'] },
    },
  },
};
