/// <reference types='cypress'/>

describe('supprimer un post',()=>{
    it('supp le post=1',()=>{
        cy.request({
            method:"DELETE",
            url:"/posts/1",
        }).then((response)=>{
            console.log(response.body)
            expect(response.status).to.eq(200);
        });
    });
});