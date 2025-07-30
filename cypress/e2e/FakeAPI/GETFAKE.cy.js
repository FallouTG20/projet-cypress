/// <reference types="cypress" />
describe('recuperer les sources de fake api',()=>{
    it('recuperer tous les produits',()=>{
      cy.request({
        method:"GET",
        url:"https://fakestoreapi.com/products"
      }).then((response)=>{
        console.log(response.body);
        expect(response.status).to.eq(200);
        expect(response.body[0]).to.have.property("title");
        expect(response.body[0]).to.have.property("price");
        expect(response.body).to.be.an('array');
      });
    });

    it('recuperer le produit 10',()=>{
        cy.request({
            method:"GET",
            url:"https://fakestoreapi.com/products/10"
        }).then((response)=>{
            console.log(response.body);
            expect(response.status).to.eq(200);
            expect(response.body.id).to.eq(10);
            expect(response.body).to.have.property("price");
            expect(response.body).to.have.property("image");
        });
    });

    it('recuperer tous les users',()=>{
        cy.request({
            method:"GET",
            url:"https://fakestoreapi.com/users"
        }).then((response)=>{
            console.log(response.body);
            expect(response.status).to.eq(200);
            expect(response.body[0]).to.have.property("username");
            expect(response.body[0]).to.have.property("password");
            expect(response.body[0]).to.have.property("email");
            expect(response.body[0].username).to.be.a("string");
            expect(response.body[0].email).to.be.a("string");
        });
    });

});