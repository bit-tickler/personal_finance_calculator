from simple_term_menu import TerminalMenu
from Ledger import ledger
from format_expense import format_expense

def remove_expense() -> None:
    """
    Displays a menu listing the expenses in the ledger
    and prompts the user to select an expense to be removed.

    Once the user has made a selection, they are prompted 
    to confirm their choice.
    """

    # Get all of the expenses in the ledger
    expenses = ledger.get_all_expenses()

    '''
    Check that there is at least one expense in the ledger. 
    If there are no expenses:
    
        Display a message to the user letting them know that there
        are no expenses and request the user to acknowledge.

    Once the use has acknowledged, return to the 
    parent menu (Manage Expenses)
    '''
    if (len(expenses) == 0):
        print(
            "=======================================\n" + 
            "You don't have any expenses to remove.\n" +
            "=======================================\n"
        )

        # Wait for the user to acknowledge
        input(
            "----------------------------------------------------------\n" +
            "Press the ENTER key to return to the Manage Expenses Menu.\n" +
            "----------------------------------------------------------\n"
        )
        return None
    '''    
    Create a list of menu options by mapping the 
    list of expenses and create a string containing
    the expense's title, category and amount
    ''' 
    menu_options = map(format_expense, expenses)

    '''
    Create a terminal menu instance and
    provide the list of options to be displayed
    and a prompt as the title.
    '''    
    expenses_menu = TerminalMenu(
        menu_options,
        clear_screen=True,
        cycle_cursor=True,
        title=(
            "----------------------------------------------------\n" + 
            "Please select the expense you would like to remove:\n" +
            "----------------------------------------------------")
    )

    # Access the index of the menu option the user has selected
    selected_menu_option_index = expenses_menu.show()

    # Use the selected menu index to access the expense
    # that the user selected
    selected_expense = expenses[selected_menu_option_index]
    """
        Create a terminal menu instance prompting 
        the user to confirm that they want to remove 
        the selected expense.
    """
    confirmation_menu = TerminalMenu(
        ["Yes", "No"],
        clear_screen=True,
        cycle_cursor=True,
        title=(
            "===================================================\n"
            "Are you sure you want to remove this expense?\n" +
            "===================================================\n"
            f"{format_expense(selected_expense)}\n"
            "---------------------------------------------------\n"
        )
    )

    # Get the index of the menu option the user has selected
    selected_menu_option_index = confirmation_menu.show()

    # If the user has selected "Yes"
    if selected_menu_option_index == 0:
        ledger.remove_expense(selected_expense)
        print(f"Successfully removed: {format_expense(selected_expense)}\n")
        # Await confirmation from the user
        input(
            "-----------------------------------------------------------\n" +
            "Press the ENTER key to return to the Manage Expenses Menu.\n" +
            "-----------------------------------------------------------\n"
        )
        return None
    else: 
        return None
