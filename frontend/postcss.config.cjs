// frontend/postcss.config.cjs
module.exports = {
  plugins: {
    'postcss-import': {},        // handles your @import rules
    '@tailwindcss/postcss': {},  // ← the new Tailwind PostCSS plugin
    autoprefixer: {},
  },
}
