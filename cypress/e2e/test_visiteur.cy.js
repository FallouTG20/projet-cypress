/// <reference types="cypress" /> 

describe('page d\'accueil viteur', () => {
    it('devrait affcher dans le navbar les boutons : Accueil,menus,se connecter,s\'inscrire', () => {
        cy.visit('http://host.docker.internal:8000/') // pour acceder au site 
        cy.contains('Accueil') // le bouton doit exister et etre visible 
        cy.contains('Menus') // le bouton doit exister et etre visible
        cy.contains('Se connecter') // le bouton doit exister et etre visible  
        cy.contains('Inscription') // le bouton doit exister et etre visible 
    })
})

/////////////////////////////////////////////////////////////////////////////////////////////////////

describe('les boutons fonctionnent ?', () =>{
    it('les boutons du navbar doivent fonctionner', () =>{
        cy.visit('http://host.docker.internal:8000/') // pour acceder au site 
        cy.get('#id_menus').should('not.be.visible').click({force : true})
        // cy.url().should('include','/menus')
    })
})

// /////////////////////////////////////////////////////////////////////////////////////////////////////

// describe('page de connexion', () => {
//     it ('doit pouvoir se connecter', () => {
//         cy.visit('http://127.0.0.1:8000/comptes/login/') // tester l'acces a la page 
//         cy.get('#id_username').should('be.visible') // verifier que le champ est visible
//         cy.get('#id_password').should('be.visible') // verifier que le champ est visible 
//         cy.get('#id_username').type('sona') // on simule une connexion --> nom d'utilisateur 
//         cy.get('#id_password').type('djangodjango') // on simule une connexion --> password 
//         cy.get ('#id_boutonS').click() // on test si le bouton se connecter fonctionne 
//         cy.url().should('include','http://127.0.0.1:8000/')
//     })

// })


// /////////////////////////////////////////////////////////////////////////////////////////////////////

// describe('test d\'inscriptions', () => {

//     it('doit pouvoir s\'inscrire', () => {
//         cy.visit('http://127.0.0.1:8000/comptes/register/')
//         cy.get('#id_username').type('test2')
//         cy.get('#id_first_name').type('galass2')
//         cy.get('#id_last_name').type('ttest2')
//         cy.get('#id_email').type('galass20@gmail.com')
//         cy.get('#id_password').type('djangodjango')
//         cy.get('#id_password2').type('djangodjango')
//         cy.get('#id_telephone').type('787638901')
//         cy.get('#yess_go').click()
//         cy.url().should('include','http://127.0.0.1:8000/')
//     })
// })


/////////////////////////////////////////////////////////////////////////////////////////////////////

