// Storybook do Trilha AOCP. O app continua sendo o index.html: as stories o leem como texto
// (?raw) e o renderizam num iframe srcdoc. Nenhuma pasta do disco é servida — de propósito,
// para que o .env nunca fique ao alcance do servidor do Storybook (HARNESS §F59).
export default {
  framework: '@storybook/html-vite',
  stories: ['../stories/**/*.stories.js'],
};
