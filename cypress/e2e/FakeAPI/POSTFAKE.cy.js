/// <reference types="cypress"/>

describe('cree un utilisateur avec les fixtures',()=>{
    it('on cree un client',()=>{
        cy.fixture('dtPOSTFAKE').then((dtPF)=>{
            cy.request({
                method:"POST",
                url:"https://fakestoreapi.com/users",
                headers:{
                    'Content-type': 'application/json; charset=UTF-8',
                },
                body:dtPF,
            }).then((response)=>{
                console.log(response.body);
                expect(response.status).to.be.oneOf([200,201]);
                expect(response.body).to.have.property("id");
            });
        });
    });
});