// C:\aura-ai\frontend\aura-ai-ui\postcss.config.mjs
const config = {
  plugins: {
    // --- CRITICAL MODIFICATION: Use the correct PostCSS plugin package ---
    // 'tailwindcss' is the main package, but the PostCSS plugin is @tailwindcss/postcss
    '@tailwindcss/postcss': {}, // Correctly reference the PostCSS plugin for Tailwind CSS
    'autoprefixer': {},
    // --- END CRITICAL MODIFICATION ---
  },
};

export default config;