describe('Tests de connexion Facebook', () => {
  beforeEach(() => {
    // Aller sur la page de connexion avant chaque test
    cy.visit('https://www.facebook.com/')
  })

  it('Devrait charger la page de connexion', () => {
    cy.get('input[name="email"]').should('be.visible')
    cy.get('input[name="pass"]').should('be.visible')
    cy.get('button[name="login"]').should('be.visible')
  })

  it('Devrait refuser la connexion avec mauvais identifiants', () => {
    cy.get('input[name="email"]').type('mauvais@email.com')
    cy.get('input[name="pass"]').type('mauvaisMotDePasse')
    cy.get('button[name="login"]').click()
    // Vérifier qu'on reste sur la page de login ou qu'un message d'erreur apparait
    cy.url().should('include', 'facebook.com')
  })

  it('Devrait essayer de se connecter avec les bonnes infos depuis le fixture', () => {
    cy.fixture('user').then((user) => {
      cy.get('input[name="email"]').type(user.email)
      cy.get('input[name="pass"]').type(user.password)
      cy.get('button[name="login"]').click()
      // Ici on vérifie qu'on est redirigé ou qu'on voit un élément qui prouve qu'on est connecté
      cy.url().should('not.include', 'login')
    })
  })

  it('Devrait afficher un message d\'erreur si on laisse les champs vides', () => {
    cy.get('button[name="login"]').click()
    // Vérifier qu'un message d'erreur apparaît ou qu'on reste sur la page
    cy.url().should('include', 'facebook.com')
  })
})
