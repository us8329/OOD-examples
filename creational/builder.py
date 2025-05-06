'''
Purpose: Simplify construction of complex objects step by step, allowing different representations.
Key Points:
    1. Separate Builder (constructs) from Director (controls construction)
    2. Fluent interfaces often used for readability
'''

class Burger:
    def __init__(self):
        self.buns = None
        self.patty = None
        self.cheese = None

    def setBuns(self,bunStyle):
        self.buns = bunStyle
    
    def setPatty(self, pattyStyle):
        self.setPatty = pattyStyle
    
    def setCheese(self, cheeseStyle):
        self.setCheese = cheeseStyle
    

class BurgerBuilder:
    def __init__(self):
       self.burger = Burger() 
    
    def addBuns(self, bunStyle):
        self.burger.setBuns(bunStyle)
        return self
    
    def addPatty (self, pattyStyle):
        self.burger.setPatty(pattyStyle)
        return self
    
    def addCheese(self, cheeseStyle):
        self.burger.setCheese(cheeseStyle)
        return self
    
    def build(self):
        return self.burger
    

burger = BurgerBuilder()\
    .addBuns('sesame')\
        .addPatty('double beef')\
            .addCheese('parmesan')\
                .build()

