class Recipe:
    '''Represents a coffee recipe.'''

    #Constructor method
    def __init__(self, name, coffee_amount, water_amount, time, milk_amount=0, sugar_amount=0):         
        '''Initializes an object of type Recipe.'''

        self._name = name
        self._milk_amount = milk_amount
        self._water_amount = water_amount
        self._coffee_amount = coffee_amount
        self._sugar_amount = sugar_amount
        self._time = time

    #Getters methods
    def get_name(self):
        return self._name
    
    def get_milk_amount(self):
        return self._milk_amount
    
    def get_water_amount(self):
        return self._water_amount
    
    def get_coffee_amount(self):
        return self._coffee_amount
    
    def get_sugar_amount(self):
        return self._sugar_amount
    
    def get_time(self):
        return self._time 