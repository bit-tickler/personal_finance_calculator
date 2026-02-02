# Import the Ledger instance (singleton).
from Ledger import ledger
# Import the clear_screen utility function.
from clear_screen import clear_screen

def enter_income():
    """
    Prompts the user to enter a float value
    for the income amount and sets the ledger's 
    income.
    """
    
    '''
    A temporary variable to store the user's input and
    determine whether the while loop should continue to
    iterate.
    '''
    income = None
    while income is None:        
        try:
            # Get the user's income
            income = float(input(
                "---------------------------------\n" +
                "Please enter your monthly income:\n" +
                "---------------------------------\n" 
            ))
            # Attempt to set the ledger's income
            ledger.set_income(income)
        
        except ValueError as e:
            '''
            Set the local income to None so that the while loop
            continues to iterate.
            Clear the screen and display the error message.
            '''
            clear_screen()
            print(str(e))        
            income = None
