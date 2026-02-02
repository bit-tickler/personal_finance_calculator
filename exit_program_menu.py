# import the TerminalMenu class from the simple_term_menu package
from simple_term_menu import TerminalMenu
# import sys to access the exit() function
import sys

def exit_program_menu() -> None:
    """
    Displays a menu of options to exit the program.
    Prompts the user to select an option.

    If the user chooses to resume, they will be redirected
    to the Main Menu. 

    If the user chooses to exit, the program will exit.
    """
    # Clear the screen and display the menu
    # clear_screen()
    menu = TerminalMenu(["Resume", "Exit"],
                        cycle_cursor=True,
                        clear_screen=True,
                        title=(
                            "-------------------------------\n" +
                            "Are you sure you want to quit?\n" +
                            "-------------------------------\n"
                        ))
    '''
    If the user chose to resume
    return to the main menu otherwise
    exit the program.
    '''
    if menu.show() == 0:
        return None
    else:
        print(
            "------------------------------------------------\n" +
            "Thank you for using Personal Finance Calculator\n" +
            "------------------------------------------------\n"
        )
        sys.exit()
