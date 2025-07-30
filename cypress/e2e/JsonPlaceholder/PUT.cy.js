/// <reference types="cypress"/>

// describe('modification de post',()=>{
//     it('on va modifier le post 10',()=>{
//         cy.request({
//             method:"PUT",
//             url:"/posts/10",
//             headers:{
//                 'content-type':'application/json; charset=UTF-8',
//             },
//             body:{
//                 id: 10,
//                 title: "modif post 10",
//                 body: "toujours dans cypress on va essayer de mosifier le post 10",
//                 userId: 10,
//             },
//         }).then((response)=>{
//             console.log(response.body);
//             expect(response.status).to.eq(200);
//             expect(response.body.id).to.be.eq(10);
//         });
//     });
// });

describe('update a post',()=>{
    it('we are going to update post=10 using fixture',()=>{
        cy.fixture('dtPUT').then((data)=>{
         cy.request({
            method:"PUT",
            url:"/posts/10",
            headers:{
                'content-type':'application/json; charset=UTF-8',
            },
            body:data,
         }).then((response)=>{
            console.log(response.body);
            expect(response.status).to.eq(200);
            expect(response.body).to.have.property('body');
            expect(response.body.id).to.eq(10);
         });
        });
    });
});