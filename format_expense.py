'''
Import the Expense class for defining the type of 
the function's expense argument
'''
from Expense import Expense
# Import the to_sterling utility function
from to_sterling import to_sterling

def format_expense(expense: Expense) -> str:
  """
  Formats the expense's title, category and amount
  to a string.

  Args:
    expense (Expense): The expense to be formatted.

  Raises:
    ValueError: If the provided argument is not an Expense instance.
  """
  '''
  Check if the provided argument is an Expense instance.
  '''
  if not isinstance(expense, Expense):
    # Raise a ValueError if the argument is not an Expense instance
    raise TypeError(
        "=======================================================================\n" +
        "Error: Cannot format the provided expense, it is not of type 'Expense'\n" +
        "=======================================================================\n"
    )
    
  # Return the formatted expense properties 
  return f"{expense.get_title()} ({expense.get_category()}): {to_sterling(expense.get_amount())}"
