# import validation utility functions
from is_positive_number import is_positive_number
from is_non_empty_string import is_non_empty_string
# import the clear screen utility function
from clear_screen import clear_screen
# import the ledger instance (singleton)
from Ledger import ledger
# import the Expense class
from Expense import Expense
# import the Terminal menu class from the simple_term_menu package
from simple_term_menu import TerminalMenu

def prompt_expense_title() -> str:
    """
    Prompts the user for, and validates the 
    title for the expense to be added to the ledger.

    Returns str: The validated title that the user provided.

    Raises:
        ValueError: If the provided title is not a non_empty string
    """
    
    '''
    Temporary variable to store the user's input and determine
    whether the while loop should continue to iterate
    '''
    expense_title = None
    
    while expense_title is None:
        # Prompt the user for a title for the expense.
        try:
            expense_title = input(
                "---------------------------------\n" +
                "Please enter the expense's title:\n" +
                "---------------------------------\n"
            )
            # Raise an exception if the title is not a non-empty string
            if not is_non_empty_string(expense_title):
                raise ValueError(
                    "=======================================================\n" +
                    "Error: The expense's title must be a non-empty string.\n" +
                    "=======================================================\n"
                )
        except ValueError as e:
            '''
            Reset expense title to None so that the
            while loop continues to iterate.
            Clear the terminal and print the error message.
            '''
            expense_title = None
            clear_screen()
            print(f"{e}")
    # Return the expense title
    return expense_title


def prompt_expense_category() -> str:
    """
    Prompts the user to select an existing expense 
    category for the expense to be added to the ledger
    from a menu of options.

    Returns str: The category that the user selected.
    """
    
    '''
    A temporary variable that stores the category that the user
    selected.
    '''
    expense_category = None
    '''
    Create a list of expense category options
    that exist in the ledger.
    '''
    menu_options = ledger.get_expense_categories()
    '''
    Create a terminal menu interface to
    prompt the user to select a category.
    '''
    menu = TerminalMenu(
        menu_options,
        cycle_cursor = True,
        clear_screen=True,
        title=(
            "----------------------------------\n" +
            "Please choose an expense category:\n" +
            "----------------------------------\n"
        ),
    )
    # Access the index of the user's selected option
    selected_index = menu.show()
    '''
    Use the selected_index to access the category
    in the list of options that the user selected
    ''' 
    expense_category = menu_options[selected_index]
    # return the category
    return expense_category

def prompt_expense_amount() -> float:
    """
    Prompts the user for an expense amount.

    Returns float: The amount that the user provided.

    Raises: 
        ValueError: 
            If the provided expense amount
            fails validation according to 
            the `is_positive_number` utility function.
    """
    
    # Track the provided expense amount
    expense_amount = None
    
    while expense_amount is None:
        # Prompt the user for the expense's amount.
        try:
            expense_amount = float(input(
                "---------------------------------\n" +
                "Please enter the expense's amount:\n" +
                "---------------------------------\n"
            ))
            # 
            if not is_positive_number(expense_amount):
                raise ValueError(
                    "================================================================\n" +
                    "Error: The expense's amount must be a number greater than zero.\n" +
                    "================================================================\n"
                ) 
        except ValueError as e:
            '''
            Reset expense amount to None so that the
            while loop continues to iterate.
            Clear the terminal and print the error message.
            '''
            clear_screen()
            expense_amount = None
            print(f"{e}")
    return expense_amount

def add_expense() -> None:
    """
    Appends a new expense to the ledger 
    using the prompt functions to set 
    the expenses amount, category and title.
    """

    ledger.append_expense(
        Expense(
            amount = prompt_expense_amount(),
            category = prompt_expense_category(),
            title = prompt_expense_title(),
        )
    )
