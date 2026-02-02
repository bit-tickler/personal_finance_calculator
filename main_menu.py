# Import magic strings
from constants import (
    MAIN_MENU_TITLE,
    ENTER_INCOME_OPTION,
    VIEW_BUDGET_OPTION,
    MANAGE_EXPENSES_OPTION,
    EXIT_PROGRAM_OPTION
)

# Import the clear_screen utility function.
from clear_screen import clear_screen
# Import the TerminalMenu class from the simple_term_menu package.
from simple_term_menu import TerminalMenu

# Import all of the main menu option subroutines
from view_budget import view_budget
from exit_program_menu import exit_program_menu
from manage_expenses_menu import manage_expenses_menu
from enter_income import enter_income

'''
Create a dictionary of all of the main menu option subroutines.
    property: menu option name
    value: menu option subroutine
'''
menu_option_functions = {
    ENTER_INCOME_OPTION: enter_income,
    MANAGE_EXPENSES_OPTION: manage_expenses_menu,
    VIEW_BUDGET_OPTION: view_budget,
    EXIT_PROGRAM_OPTION: exit_program_menu,
}

def main_menu() -> None:
    """
    Prompts the user to select a menu option and
    invokes the selected menu option's subroutine.
    """
    # Determine the list of available menu options
    options = list(menu_option_functions.keys())

    '''
    An infinite while loop responsible for persisting
    the main menu (and thus the application) until 
    the user selects the Exit Program option.
    '''
    while True:
        # Create a terminal menu instance
        menu = TerminalMenu(
            options, # Provide a list of menu options
            cycle_cursor=True,
            clear_screen=True,
            title= (
                    "=========================\n" 
                    f"{MAIN_MENU_TITLE}\n"  
                +   "=========================\n"  
                +   "Please choose an option:\n"  
                +   "-------------------------\n"
            ), 
        )
        # Access the index of the menu option the user has selected
        selected_menu_option_index = menu.show()   
        '''
        Use the selected menu option index to access the 
        subroutine associated with the selected menu option
        '''
        menu_option_subroutine = (
            menu_option_functions[
                options[selected_menu_option_index]
            ]
        )

        '''
        Invoke the subroutine associated with the 
        chosen menu option
        '''
        menu_option_subroutine()
