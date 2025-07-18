/// <reference types="cypress"/>

describe('tester les fonctionnalités du client', () => {

  beforeEach(function() {
    cy.fixture('data_testC').as('DC');
  });

  beforeEach(function() {
    const usern = this.DC.username;
    const pass = this.DC.password;

    cy.visit('http://host.docker.internal:8000/comptes/login/')
    cy.get('input[name=username]').type(usern);
    cy.get('input[name=password]').type(pass);
    cy.get('button[type=submit]').click()
    cy.url().should('include', 'http://host.docker.internal:8000/')
  });

  it('Vérifier qu\'on est bien connecté', function() {
    cy.get('body').should('contain', 'Tu as faim my G!?')
    cy.contains('Tableau de bord')
  });

  it('Vérifier le tableau de bord et cliquer sur modifier le profil', function() {
    cy.visit('http://host.docker.internal:8000/comptes/dashboard/')
    cy.contains('Voir les menus').should('be.visible')
    cy.contains('Voir mes commande').should('be.visible')
    cy.contains('Modifier').should('be.visible')
    cy.get('#modifprofil').click()
    cy.url().should('include', 'http://host.docker.internal:8000/comptes/profile/')
  });

  it('verfier la page de modif du profil', function() {
    cy.visit('http://host.docker.internal:8000/comptes/profile/')
    cy.get('input[name=username]').clear()
    cy.get('input[name=username]').type('Michelle')
  });

  it('Vérifier la page des menus', function() {
    cy.visit('http://host.docker.internal:8000/menus/')
    cy.url().should('include', '/menus/')
    cy.contains('Spécialités Nos Menus').should('be.visible')
  });

  it('Vérifier que tout les categories sont presents sur la page menus', function() {
    cy.visit('http://host.docker.internal:8000/menus/')
    cy.contains('Entrées').should('be.visible')
    cy.contains('Plats de résistance').should('be.visible')
    cy.contains('Desserts').should('be.visible')
  });

  it('tester le bouton voir details et contenu', function() {
    cy.visit('http://host.docker.internal:8000/menus/')
    cy.get('button[id="id_detailsbuton"]').first().click()
    cy.get('.modal.show').should('exist') // verifier que la modal apparait 
    cy.get('.modal.show .modal-title').should('not.be.empty'); // veifier le contenu (le titre)
  });

  it('tester les fonctionnalites du panier vide', function(){
    cy.visit('http://host.docker.internal:8000/commandes/panier/')
    cy.contains('Votre panier est vide.')
    cy.contains('Ajouter un menu').should('be.visible');
  });

  describe('panier non vide', () => {
    beforeEach( function(){
      cy.visit('http://host.docker.internal:8000/menus/')
      cy.get('#id_ajoutpanier').first().click()
    });

    it('panier non vide doit s\'afficher', function() {
      cy.visit('http://host.docker.internal:8000/commandes/panier/')
      cy.contains('Mon Panier')
      cy.contains('Total')
      cy.contains('Prix unitaire')
      cy.contains('Passer la commande').should('be.visible');
    });

    it('doit pouvoir augmenter la quantite du menus', function() {
      cy.visit('http://host.docker.internal:8000/commandes/panier/')
      cy.contains('Mon Panier')
      cy.get('#AugQMenu').dblclick()
    });

    it('doit pouvoir diminuer la quantite du menus', function() {
      cy.visit('http://host.docker.internal:8000/commandes/panier/')
      cy.contains('Mon Panier')
      cy.get('#dimQMenu').click()
    });

    it('tester le bouton passer la commande', function() {
      cy.visit('http://host.docker.internal:8000/commandes/panier/')
      cy.get('.btn.btn-success').click()
      cy.url().should('include','http://host.docker.internal:8000/commandes/passer-commande/')
    });

    it('tester le bouton continuer mes acahts', function() {
      cy.visit('http://host.docker.internal:8000/commandes/panier/')
      cy.get('.btn.btn-primary').click()
      cy.url().should('include','http://host.docker.internal:8000/menus/')
    });

    it('passer la commande', function() {
      cy.visit('http://host.docker.internal:8000/commandes/passer-commande/')
      cy.contains('Confirmer la commande').should('be.visible')
      cy.get('.fa.fa-check').click() // clique sur le bouton valider la commande 
      cy.url().should('include','http://host.docker.internal:8000/commandes/mes-commandes/')
    });
  });

});
