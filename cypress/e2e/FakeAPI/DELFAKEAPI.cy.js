/// <reference types="cypress"/>

describe('supprimession des users',()=>{
    it('supprimer le user avec l\'id=10',()=>{
        cy.request({
            method:"DELETE",
            url:"https://fakestoreapi.com/users/10",
        }).then((response)=>{
            console.log(response.body);
            expect(response.status).to.eq(200);
        });
    });
});