import { defineConfig } from 'astro/config';
import mdx from '@astrojs/mdx';
import sitemap from '@astrojs/sitemap';

export default defineConfig({
  site: 'https://phillip-bruno.github.io',
  integrations: [mdx(), sitemap()],
});
