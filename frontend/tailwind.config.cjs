/** @type {import('tailwindcss').Config} */
module.exports = {
    // you can omit `content` entirely in v4; it will auto-detect,
    // but we’ll add a safelist for our custom classes:
    safelist: [
      'animate-aurora',
      'after:animate-aurora',
    ],
    theme: {
      extend: {
        keyframes: {
          aurora: {
            '0%':   { 'background-position': '50% 50%' },
            '100%': { 'background-position': '350% 50%' },
          },
        },
        animation: {
          'aurora': 'aurora 60s linear infinite',
        },
      },
    },
  }
  