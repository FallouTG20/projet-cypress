const { defineConfig } = require('cypress');

module.exports = defineConfig({
  e2e: {
    // ✅ On fixe le baseUrl sur le site de test public
    baseUrl: 'https://example.cypress.io',

    // ✅ Dossiers par défaut (tu peux les garder tels quels)
    fixturesFolder: 'cypress/fixtures',
    supportFile: 'cypress/support/e2e.js',
    specPattern: 'cypress/e2e/**/*.cy.{js,jsx,ts,tsx}',

    // ✅ Options supplémentaires pour éviter des erreurs fréquentes
    video: false,               // Pas de vidéo, plus rapide pour CI
    chromeWebSecurity: false    // Désactive la politique CORS stricte
  }
});
