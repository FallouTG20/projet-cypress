describe('Example Cypress Test', () => {
  it('tester la page d\'accueil', () => {
    cy.visit('https://example.cypress.io');
    cy.contains('Kitchen Sink').should('be.visible');
  });

  it('naviguer a la page querying', () => {
    cy.visit('https://example.cypress.io');
    cy.get('.home-list > li:first-child > a').click();
    cy.url().should('include', '/commands/querying');
    cy.contains('get').should('be.visible');
  });
});
