/// <reference types="cypress"/>

//recuperer des ressources de 'api
describe('on recupere des ressources de l\'api',() => {
    it('recuperer tous les posts',()=>{
        cy.request({
            method:'GET',
            url:'/posts'
        }).then((response)=> { 
           expect(response.status).to.eq(200);
           expect(response.body[0]).to.have.property("id");
        });
    });
});
