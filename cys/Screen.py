import os
import time

class Screen:
    '''Represents the screen of the coffee maker.'''

    #Constructor method
    def __init__(self):
        '''Initializes an object of type Screen.'''

        #Default messages
        self._english_messages = {
            'choose_language': 'Choose a language \nE -> English \nS -> Spanish',
            'invalid_language': 'Please choose an available language',
            'welcome': 'Welcome to CyS CoffeeMaker',
            'menu': 'Menu \n \nE -> Espresso \nC -> Capuccino \nL -> Latte \nA -> American \n \nR -> Refill ingredients \nS -> See deposit \n \nX -> Exit', 
            'invalid_option': 'The selected option is not among the menu options', 
            'farewell': 'Good bye', 
            'not_enough_ingredients': 'Not enough ingredients to prepare the selected coffee. Please check the deposit', 
            'is_full': 'The deposit is full. It is not necessary to refill',
            'filled_in': 'The deposit has been refilled'
        }

        self._spanish_messages = {
            'welcome': 'Bienvenido a CyS CoffeeMaker',
            'menu': 'Menú \n \nE -> Espresso \nC -> Capuccino \nL -> Latte \nA -> American \n \nR -> Rellenar ingredientes \nS -> Ver depósito \n \nX -> Salir',
            'invalid_option': 'La opción seleccionada no está dentro de las opciones del menú', 
            'farewell': 'Hasta pronto', 
            'not_enough_ingredients': 'No hay suficientes ingredientes para preparar el café seleccionado. Por favor revise el depósito', 
            'is_full': 'El depósito está lleno. No es necesario rellenar',
            'filled_in': 'El depósito ha sido rellenado'
        }

    #Methods
    def display_message(self, message, language):
        '''Displays a message on the screen.'''

        os.system('cls')
        if language == 'E':
            print(self._english_messages[message])
        else:
            print(self._spanish_messages[message])

    def display_deposit_message(self, coffeeMaker, language):
        '''Displays the status of the coffee maker deposit on the screen'''

        os.system('cls')
        deposit = coffeeMaker.deposit()
        if language == 'E':
            print('Milk quantity:', deposit['milk'], 'ml \nWater quantity:', deposit['water'], 'ml \nCoffee quantity:', deposit['coffee'], 'gr \nSugar quantity:', deposit['sugar'], 'gr')
        else:
            print('Cantidad de leche:', deposit['milk'], 'ml \nCantidad de agua:', deposit['water'], 'ml \nCantidad de café:', deposit['coffee'], 'gr \nCantidad de azúcar:', deposit['sugar'], 'gr')

    def display_done_message(self, recipe, language):
        '''Displays the coffee made message on the screen.'''

        os.system('cls')
        if language == 'E':
            print('Your', recipe.get_name(), 'is done!')
        else:
            print('¡Su', recipe.get_name(), 'está listo!')
        
    def wait(self, seconds):
        '''Wait seconds received.'''

        time.sleep(seconds)

    def chronometer(self, seconds):
        '''Starts a chronometer with received seconds.'''

        for second in range(seconds, 0, -1):
            os.system('cls')
            print(second)
            time.sleep(1)