/// <reference types="cypress"/>

describe('on va modifier une carte',()=>{
    it('on modifie la carte 11',()=>{
        cy.fixture('DTPUTFAKEAPI').then((dtPUT)=>{
            cy.request({
                method:"PUT",
                url:"https://fakestoreapi.com/carts/11",
                headers:{
                    'content-type':'application/json; charset=UTF-8',
                },
                body:dtPUT,
            }).then((response)=>{
                console.log(response.body);
                expect(response.body).to.have.property("id");
            });
        });
    });
});