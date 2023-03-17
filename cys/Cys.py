from CoffeeMaker import CoffeeMaker
from Recipe import Recipe
from Screen import Screen

class Cys:
    '''Represents the CyS CoffeeMaker.'''

    def turn_on(self):
        '''Turn on the CyS CoffeeMaker.'''

        #Coffee recipes are created using the Recipe class    
        recipes = {
            'E': Recipe('Espresso', 7, 30, 25),
            'C': Recipe('Capuccino', 7, 30, 30, 125, 4),
            'L': Recipe('Latte Macciato', 7, 30, 35, 300),
            'A': Recipe('American', 14, 60, 20)
        }
            
        #The CoffeeMaker class is instantiated to create the CyS CoffeeMaker
        cys = CoffeeMaker()

        #The Screen class is instantiated to create the "screen" of the CyS CoffeeMaker
        screen = Screen()
        
        #Language input
        while True:
            screen.display_message('choose_language', 'E')
            language = input('>>> ')
            if language == 'E' or language == 'S':
                break
            screen.display_message('invalid_language', 'E')
            screen.wait(4)

        screen.display_message('welcome', language)
        screen.wait(4)

        #Menu
        while True:          
            screen.display_message('menu', language)
            user_choice = input('>>> ')

            if user_choice in ('E','C','L','A'): #Options to make coffee
                if cys.enough_amount(recipes[user_choice]): #Checks if there are enough ingredients
                    cys.make_coffee(recipes[user_choice]) #Makes the selected coffee
                    screen.chronometer(recipes[user_choice].get_time()) #Chronometer
                    screen.display_done_message(recipes[user_choice], language)
                else:
                    screen.display_message('not_enough_ingredients', language)
                        
            elif user_choice == 'R': #Option to refill deposit
                if cys.full(): #If the deposit is full, it is not necessary to refill
                    screen.display_message('is_full', language)
                else:
                    cys.refill() #Refills the deposit
                    screen.display_message('filled_in', language)
                            
            elif user_choice == 'S': #Option to show the status of the deposit
                screen.display_deposit_message(cys, language)
                            
            elif user_choice == 'X': #Option to exit
                screen.display_message('farewell', language)
                screen.wait(4)
                break

            else: #Invalid option
                screen.display_message('invalid_option', language)
                
            screen.wait(4)