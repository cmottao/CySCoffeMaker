from CoffeeMaker import CoffeeMaker
from Recipe import Recipe
from Screen import Screen

class Cys(CoffeeMaker):
    '''Represents the CyS CoffeeMaker.'''

    # Constructor method
    def __init__(self):
        '''Initializes the CyS CoffeeMaker.'''

        super().__init__()

        # Coffee recipes are created using the Recipe class  
        self.recipes = {
            'E': Recipe('Espresso', 7, 30, 25),
            'C': Recipe('Capuccino', 7, 30, 30, 125, 4),
            'L': Recipe('Latte Macciato', 7, 30, 35, 300),
            'A': Recipe('American', 14, 60, 20)
        }

        # The Screen class is instantiated to create the "screen" of the CyS CoffeeMaker
        self.screen = Screen()

    # Methods 
    def input_language(self):
        '''Prompts the user to choose the language for the CoffeeMaker's screen.'''

        while True:
            self.screen.display_message('choose_language', 'E')
            self.language = input('>>> ')
            if self.language == 'E' or self.language == 'S':
                break
            self.screen.display_message('invalid_language', 'E')
            self.screen.wait(4)

        self.screen.display_message('welcome', self.language)
        self.screen.wait(4)

    def option_make_coffee(self, user_choice):
        '''Processes the selected coffee option.'''

        if self.enough_amount(self.recipes[user_choice]): # Checks if there are enough ingredients
            self.make_coffee(self.recipes[user_choice]) # Makes the selected coffee
            self.screen.chronometer(self.recipes[user_choice].get_time()) # Chronometer
            self.screen.display_done_message(self.recipes[user_choice], self.language)
        else:
            self.screen.display_message('not_enough_ingredients', self.language)

    def option_refill(self):
        '''Refills the deposit of ingredients in the CoffeeMaker.'''
        
        if self.full(): # If the deposit is full, it is not necessary to refill
            self.screen.display_message('is_full', self.language)
        else:
            self.refill() # Refills the deposit
            self.screen.display_message('filled_in', self.language)

    def main_menu_loop(self):
        '''Displays the main menu and handles user input until the user chooses to exit.'''

        while True:          
            self.screen.display_message('menu', self.language)
            user_choice = input('>>> ')

            if user_choice in ('E','C','L','A'): # Options to make coffee
                self.option_make_coffee(user_choice)
                       
            elif user_choice == 'R': # Option to refill deposit
                self.option_refill()
                            
            elif user_choice == 'S': # Option to show the status of the deposit
                self.screen.display_deposit_message(self, self.language)
                            
            elif user_choice == 'X': # Option to exit
                self.screen.display_message('farewell', self.language)
                self.screen.wait(4)
                break

            else: # Invalid option
                self.screen.display_message('invalid_option', self.language)
                
            self.screen.wait(4)

    def turn_on(self):
        '''Turns on the CyS CoffeeMaker.'''

        self.input_language()
        self.main_menu_loop()