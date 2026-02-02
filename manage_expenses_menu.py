# Import magic strings
from constants import (MANAGE_EXPENSES_MENU_TITLE, ADD_EXPENSE_OPTION,
                       REMOVE_EXPENSE_OPTION, MAIN_MENU_OPTION)
# Import the Terminal menu class from the simple_term_menu package
from simple_term_menu import TerminalMenu
# Import the add_expense subroutine
from add_expense import add_expense
# Import the remove_expense subroutine
from remove_expense import remove_expense
'''
Create a dictionary of all of the main menu option subroutines.
    property: menu option name
    value: menu option subroutine
'''
menu_option_subroutines = {
    ADD_EXPENSE_OPTION: add_expense,
    REMOVE_EXPENSE_OPTION: remove_expense,
    MAIN_MENU_OPTION: None,
}

def manage_expenses_menu() -> None:
    """
    Displays a menu of options to the user and
    prompts the user to choose an option.

    If the user chooses to add an expense
    the `add_expense` subroutine will run

    If the user chooses to remove an expense
    the `remove_expense` subroutine will run

    If the user chooses to return to the main menu
    this function will return None.
    """
    
    '''
    Use the menu_option_subroutines dictionary to
    generate a list of options for the menu
    '''
    options = list(menu_option_subroutines.keys())
    
    '''
    An infinite loop responsible for persisting the
    manage expenses menu until the user chooses to
    exit and return to the main menu.
    '''
    # An infinite loop to persist the manage expenses menu
    while True:
        '''
        Create a terminal menu instance and provide
        the list of options for the menu
        '''
        menu = TerminalMenu(options,
                            clear_screen=True,
                            cycle_cursor=True,
                            title=("=========================\n" +
                                   f"{MANAGE_EXPENSES_MENU_TITLE}\n" +
                                   "=========================\n" +
                                   "Please choose an option: \n" +
                                   "-------------------------")
                           )

        # Access the index of the menu option the user has selected
        selected_menu_option_index = menu.show()

        if options[selected_menu_option_index] == MAIN_MENU_OPTION:
            return

        '''
        Use the selected menu option index to access the
        subroutine associated with the selected menu option
        '''
        menu_option_subroutine = (
            menu_option_subroutines[options[selected_menu_option_index]])

        '''
        Invoke the subroutine associated with the
        chosen menu option
        '''
        menu_option_subroutine()
