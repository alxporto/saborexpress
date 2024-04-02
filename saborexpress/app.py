import os

restaurants = [{'name': 'Fogão Expresso', 'category': 'Italian', 'activation': False},
               {'name': 'Lig Lig', 'category': 'Chinese', 'activation': True},
               {'name': 'Cantina', 'category': 'Italian', 'activation': False}]

def show_program_name():
    """ Shows the stylized name of the program on the screen """
    print('''
░██████╗░█████╗░██████╗░░█████╗░██████╗░  ███████╗██╗░░██╗██████╗░██████╗░███████╗░██████╗░██████╗
██╔════╝██╔══██╗██╔══██╗██╔══██╗██╔══██╗  ██╔════╝╚██╗██╔╝██╔══██╗██╔══██╗██╔════╝██╔════╝██╔════╝
╚█████╗░███████║██████╦╝██║░░██║██████╔╝  █████╗░░░╚███╔╝░██████╔╝██████╔╝█████╗░░╚█████╗░╚█████╗░
░╚═══██╗██╔══██║██╔══██╗██║░░██║██╔══██╗  ██╔══╝░░░██╔██╗░██╔═══╝░██╔══██╗██╔══╝░░░╚═══██╗░╚═══██╗
██████╔╝██║░░██║██████╦╝╚█████╔╝██║░░██║  ███████╗██╔╝╚██╗██║░░░░░██║░░██║███████╗██████╔╝██████╔╝
╚═════╝░╚═╝░░╚═╝╚═════╝░░╚════╝░╚═╝░░╚═╝  ╚══════╝╚═╝░░╚═╝╚═╝░░░░░╚═╝░░╚═╝╚══════╝╚═════╝░╚═════╝░ 
''')

def show_options():
    """ Displays available options on the main menu """
    print('1. Sign up a restaurant\n')
    print('2. List restaurants\n')
    print('3. Switch the restaurant status\n')
    print('4. Sign out\n')

def terminate_app():
    """ Shows the application termination message """
    show_menu_subtitle('Terminating the program')

def back_to_main_menu():
    """ Requests a user to type a key to return to the main menu 
    
    Outputs:
        Return to the main menu
    
    """
    input('\nType a key to return to the main menu: ')
    main()

def show_menu_subtitle(text):
    """ Shows a stylized subtitle on the screen
     
    Arguments:
        text (str): The subtitle text
    
    """
    os.system('clear')
    line = '*' * (len(text))
    print(line)
    print(text)
    print(line)
    print()

def invalid_option():
    """ Displays a invalid option message and returns to the main menu
    
    Outputs:
        Return to the main menu
    
    """
    show_menu_subtitle('Invalid option!')
    back_to_main_menu()

def register_new_restaurant():
    ''' This function is responsible for resgistering a new restaurant
    
    Inputs:
        restaurant_name (str): The name of the desired restaurant
        restaurant_category (str): The desired restaurant category
    
    Outputs:
        adds a new restaurant to the restaurant`s list
    
    '''
    os.system('clear')
    show_menu_subtitle('Registration of the new restaurants')
    restaurant_name = input('Type the name of the restaurant you want to register: ')
    restaurant_category = input(f'Type the category`s name of the restaurant {restaurant_name}: ')
    restaurant_data = {'name': restaurant_name, 'category': restaurant_category, 'activation': False}
    restaurants.append(restaurant_data)
    print(f'The restaurant {restaurant_name} has been successfully registered!')
    back_to_main_menu()

def list_restaurants():
    """ List the restaurants on the list
    
    Outputs:
        Displays the list of restaurants on the screen
    
    """
    os.system('clear')
    show_menu_subtitle('Listing all the restaurants: ')
    print(f"{'Restaurant name'.ljust(22)} | {'Category'.ljust(20)} | Status")
    for restaurant in restaurants:
        restaurant_name = restaurant['name']
        restaurant_category = restaurant['category']
        restaurant_activation = 'activated' if restaurant['activation'] else 'deactivated'
        print(f'- {restaurant_name.ljust(20)} | {restaurant_category.ljust(20)} | {restaurant_activation}')
    back_to_main_menu()
    
def switch_restaurant_status():
    """ Change between the activated/deactivated status of a restaurant
    
    Outputs:
        Displays a message indicating the success of the operation
    
    """
    show_menu_subtitle('Switching the restaurant status')
    restaurant_name = input('Type the name of the restaurant you want to switch the status: ')
    restaurant_found = False
    for restaurant in restaurants: 
        if restaurant_name == restaurant['name']:
            restaurant_found = True
            restaurant['activation'] = not restaurant['activation']
            message = f'\nThe restaurant {restaurant_name} was successfully activated' if restaurant['activation'] else f'\nThe restaurant {restaurant_name} was successfully deactivated'
            print(message)
    if not restaurant_found:
        print('The restaurant was not found')
    back_to_main_menu()
           
def choose_option():
    """ Requests and executes the option chosen by the user
    
    Outputs:
        Executes the option chosen by the user
    
    """
    try:
        chosen_option = int(input('Choose an option: '))
        match chosen_option:
            case 1:   
                register_new_restaurant()
            case 2: 
                list_restaurants()
            case 3:
                switch_restaurant_status()
            case 4:
                terminate_app()
            case _:
                invalid_option()
            
    except:
        invalid_option()

def main():
    """ The main function that starts the program """
    os.system('clear')
    show_program_name()
    show_options()
    choose_option()

if __name__ == '__main__':
    main()

