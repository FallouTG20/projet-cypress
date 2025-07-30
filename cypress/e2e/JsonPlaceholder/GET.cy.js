/// <reference types="cypress"/>


//recuperer des ressources de l'api
describe('on recupere des ressources de l\'api',() => {
    it('recuperer tous les posts',()=>{
        cy.request({
            method:'GET',
            url:'/posts'
        }).then((response)=> { 
           console.log(response.body); // ✅ Voir tous les posts dans la console
           expect(response.status).to.eq(200);
           expect(response.body[0]).to.have.property("id");
        });
    });

    it('recuperer le post 5',()=>{
        cy.request({
           method:'GET',
           url:'/posts/5'
        }).then((response)=>{
            expect(response.status).to.eq(200);
            expect(response.body.id).to.eq(5);
            expect(response.body).to.have.property("id");
            expect(response.body).to.have.property("title");
            expect(response.body).to.have.property("body");
        });
    });

    it('recuperer tt les comm de postId=5',()=>{
        cy.request({
            method:"GET",
            url:"/comments?postId=5",
        }).then((response)=>{
            console.log(response.body);
            expect(response.status).to.eq(200);
            // Vérifie que tous les commentaires sont bien liés au postId 5
            response.body.forEach(comment => {
            expect(comment.postId).to.eq(5);
            });
        });
    });
});
