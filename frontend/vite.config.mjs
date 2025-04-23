import { defineConfig } from 'vite'
import react from '@vitejs/plugin-react'

export default defineConfig({
  plugins: [
    react(),
    // (we dropped the ESM-only tailwindcss/vite plugin,
    //  your postcss.config.js is driving Tailwind already)
  ]
})
