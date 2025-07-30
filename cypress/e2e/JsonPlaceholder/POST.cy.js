/// <reference types="cypress"/>

describe('creation de post',()=> {
    it('create a new post',()=>{
        cy.request({
            method:"POST",
            url:'/posts',
            headers:{
               'Content-type': 'application/json; charset=UTF-8',
            },
            body:{
                    title: 'test avec cypress',
                    body: 'voici notre premier post cree avec cypress',
                    userId: 3333,
            },
        }).then((response)=>{
            console.log(response.body); // afficher la reponse sur le console 
            expect(response.status).to.be.oneOf([200,201]);
            expect(response.body).to.have.property("id"); // gerer un id (simule)
        });
    });
});