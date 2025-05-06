'''
Purpose: Decouple client code from concrete class creation by defining an interface for object creation.
Key Points:
    1. Factory Method: Subclasses decide which concrete class to instantiate.
    2. Abstract Factory: Group of related factories for families of products.
'''

class Burger:
    def __init__(self, ingredients):
        self.ingredients = ingredients
    
    def print(self):
        print(self.ingredients)

 
class Burgerfactory:
    def createCheeseBurger(self):
        ingredients = ['bun' , 'cheese', 'beef-patty']
        return Burger(ingredients)
    
    def createDeluxeCheeseBurger(self):
        ingredients = ['bun', 'tomatoes', 'onion', 'lettuce', 'cheese','double beef-patty']
        return Burger(ingredients)
    
    def createVeganBurger(self):
        ingredients = ['bun' , 'sauce', 'vegge-patty']
        return Burger(ingredients)

burgerFactory = Burgerfactory()
burgerFactory.createCheeseBurger().print()
burgerFactory.createDeluxeCheeseBurger().print()
burgerFactory.createVeganBurger().print()
