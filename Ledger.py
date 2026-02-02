# Import List type from typing for type definitions
from typing import List
# Import Expense call for type definitions
from Expense import Expense
# Import magic strings
from constants import (
    INCOME, 
    EXPENSES, 
    ESSENTIAL, 
    NON_ESSENTIAL, 
)
# Import validation utility functions
from is_non_empty_string import is_non_empty_string
from is_positive_number import is_positive_number

class Ledger:
    """ 
    A class to manage a financial ledger, storing income and categorised expenses.

    Attributes:
        __state (dict): A dictionary containing income and categorised expenses.
    """
    def __init__(self):
        """
        Initialises a new ledgers instance with an income of 0.0 
        and categorized expense lists for essential and non-essential expenses.
        """
        self.__state = {
            INCOME: 0.0,
            EXPENSES: {
                ESSENTIAL: [],
                NON_ESSENTIAL: [],
            }
        }

    def get_state(self) -> dict:
        """
        Retrieves a copy of the ledgers' internal state.

        Returns: 
            dict: A copy of the ledgers' internal state.
        """
        return self.__state.copy()

    def get_income(self) -> float:
        """
        Retrieves the ledger's income.

        Returns:
            float: The ledger's income.
        """
        return self.__state[INCOME]

    def set_income(self, amount: float) -> None:
        """
        Sets the income to the provided amount.

        Args: 
            amount (float): The income amount.
        
        Raises: 
            ValueError: If `amount` is not a positive number.
        """
        if not is_positive_number(amount):
            raise ValueError(
                "================================================\n" +
                "Error: income must be a number greater than 0.0\n" +
                "================================================\n"
            )
        # Set the ledger's income
        self.__state[INCOME] = amount

    def get_expense_categories(self) -> List[str]:
        """
        Retrieves the ledger's expense categories.

        Returns:
            List[str]: A list of expense categories.
        """
        return list(self.__state[EXPENSES].keys())

    def append_expense(self, expense: Expense) -> None:
        """
        Adds an expense to the category within the ledgers expenses
        based on the Expenses instance's category property.

        Args: 
            expense (Expense): An instance of the Expense class.

        Raises: 
            TypeError: If `expense` is not an instance of Expense.
            ValueError: If the expense's category is not a category
                        in the ledger.
        """
        if not isinstance(expense, Expense):
            raise TypeError(
                "=========================================================\n" +
                "Error: Cannot add expense, it must be of type 'Expense'.\n" +
                "==========================================================n"
            )

        if not self.is_valid_expense_category(expense.get_category()):
            raise ValueError(
                "========================================================================\n" +
                "Error: Cannot add expense, its category is not a valid expense category\n" +
                "========================================================================\n"
            )

        self.__state[EXPENSES][expense.get_category()].append(expense)

    def get_all_expenses(self) -> List[Expense]:
        """
        Returns a list of all of the expenses in all expense categories.
        """
        all_expenses = []
        for category in self.__state[EXPENSES].values():
            all_expenses.extend(category)

        return all_expenses

    def get_expenses_by_category(self, *categories: str) -> List[Expense]:
        """
        Returns a list of the expenses stored in the ledger's expenses 
        under the properties that matches the provided
        categories.

        Args:
            categories (*str): One or more expense categories.
        
        Returns: (list) The list of expenses found.
        """
        
        ''' 
        A temporary list variable to collect the expensed 
        under the provided categories.
        '''
        found_expenses = []
        '''
        Collect the expenses found under each expense category
        into the found_expenses list.
        '''
        for expense_category in self.get_expense_categories():
            if expense_category in categories:
                # Assuming get_expenses_by_category is a method that returns expenses by category
                found_expenses.extend(self.__state[EXPENSES][expense_category])

        # Return the found expenses
        return found_expenses

    def remove_expense(self, expense: Expense):
        """
        Removes the provided expense from the ledger's expenses.

        Args: expense (Expense): An instance of the Expense class.

        Raises: 
            ValueError: If the provided expense is not found.
            TypeError: If the provided expense is not an instance of Expense.
        """

        if not isinstance(expense, Expense):
            raise TypeError(
                "=============================================================================\n" +
                "Error: Cannot remove expense, the provided expense is not of type 'Expense'.\n" +
                "=============================================================================\n" 
            )

        # Search for the expense according to ita category
        if expense not in self.get_expenses_by_category(expense.get_category()):
            raise ValueError(
                "===========================================\n" +
                "Error: Cannot remove non existent expense. \n" +
                "===========================================\n"
            )
        else:
            self.__state[EXPENSES][expense.get_category()].remove(expense)

    def is_valid_expense_category(self, category: str) -> bool:
        """
        Checks if a the provided category exists in the ledgers' expenses.

        Args:
            category (str): The category to validate.

        Returns (bool): 
                True: if the category is valid.
                False: otherwise.
        """
        return category in self.__state[EXPENSES]

    def is_unique_expense_title(self, title: str) -> bool:
        """
        Checks that the provided expense title has
        not already been allocated to an expense 
        in all the expense category lists.

        Args: 
            title (str): The title to be validated.
        """
        '''
        Check the provided title against the all existing
        expense titles and return False if a match is found.
        '''
        for expense in self.get_all_expenses():
            if expense.get_title() == title:
                return False
        '''
        If no match was found
        the provided title is unique
        ''' 
        return True

ledger = Ledger();
