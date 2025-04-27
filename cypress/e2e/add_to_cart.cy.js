describe('Add to cart', () => {
    it('Adds a product to the cart', () => {
      cy.visit('/home')
  
      cy.get('form').first().submit()
  
      cy.contains('Mon Panier')
      cy.get('ul.list-group li').should('have.length', 1)
    })
  })
  