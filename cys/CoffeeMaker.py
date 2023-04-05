#Maximum capacities of the coffee maker
MAX_MILK = 300
MAX_WATER = 1500
MAX_COFFEE = 100
MAX_SUGAR = 50

class CoffeeMaker:
    '''Represents a coffee maker.'''
    
    #Constructor method
    def __init__(self): 
        '''Initializes an object of type coffee maker.'''
        
        self._milk = MAX_MILK
        self._water = MAX_WATER
        self._coffee = MAX_COFFEE
        self._sugar = MAX_SUGAR

    #Getters methods
    def get_milk(self):
        return self._milk
    
    def get_water(self):
        return self._water
    
    def get_coffee(self):
        return self._coffee
    
    def get_sugar(self):
        return self._sugar
    
    #Methods
    def make_coffee(self, recipe): 
        '''Makes the coffee and makes the changes in the deposit.'''
        
        self._milk -= recipe.get_milk_amount()
        self._water -= recipe.get_water_amount()
        self._coffee -= recipe.get_coffee_amount()
        self._sugar -= recipe.get_sugar_amount()

    def enough_amount(self, recipe):
        '''Returns if the quantities in the deposit are sufficient.'''

        return ((self._milk >= recipe.get_milk_amount()) and (self._water >= recipe.get_water_amount()) 
                and (self._coffee >= recipe.get_coffee_amount()) and (self._sugar >= recipe.get_sugar_amount()))

    def full(self): 
        '''Returns if the deposit is full.'''

        if ((self._milk == MAX_MILK) and (self._water == MAX_WATER) 
            and (self._coffee == MAX_COFFEE) and (self._sugar == MAX_SUGAR)):
            return True
        else:
            return False
        
    def refill(self): 
        '''Refills the deposit.'''

        self._milk = MAX_MILK
        self._water = MAX_WATER 
        self._coffee = MAX_COFFEE
        self._sugar = MAX_SUGAR

    def deposit(self):
        '''Returns a dictionary with the quantities of the deposit.'''

        return {'milk': self._milk, 'water': self._water, 'coffee': self._coffee, 'sugar': self._sugar}