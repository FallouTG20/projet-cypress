/// <reference types="cypress"/>

// describe('les fonctionnalites cotes client', () =>{
//     beforeEach(() =>{
//         cy.visit('http://127.0.0.1:8000/comptes/login/')
//         cy.get('input[name=username]').type('sona')
//         cy.get('input[name=password]').type('djangodjango')
//         cy.get('button[type=submit]').click()
//     });

//     it('doit etre rediriger vers la page d\'accueil', () =>{
//         cy.url().should('include','http://127.0.0.1:8000/')
//         cy.get('#id_deconnexion')
        
//     });

//     it ()
// })


describe('les fonctionnalites cotes client', () =>{
    beforeEach(function() {
        cy.fixture('data_testC').as('connex');

    });

    it('doit etre rediriger vers la page d\'accueil', function() {
        const usern=`${this.connex.username}`;
        const pass=`${this.connex.password}`;

        cy.visit('http://host.docker.internal:8000/comptes/login/')
        cy.get('input[name=username]').type(`${usern}`);
        cy.get('input[name=password]').type(`${pass}`);
        cy.get('button[type=submit]').click()
        cy.url().should('include','http://host.docker.internal:8000/')
        
    });

});