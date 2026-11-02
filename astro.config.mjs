import { defineConfig } from 'astro/config';
export default defineConfig({
  srcDir: './astro/',
  publicDir: './.astro-input/static',
  outDir: './.astro-output/',
  output: 'static',
  base: '/hands-on-computer-networks',
  build: { format: 'file' },
  compressHTML: false,
  markdown: { syntaxHighlight: false }
});
