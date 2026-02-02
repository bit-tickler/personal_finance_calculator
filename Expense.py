# import validation utility functions
from is_positive_number import is_positive_number
from is_non_empty_string import is_non_empty_string
# import the Union type from the typing package
from typing import Union
# import magic string constants
from constants import AMOUNT, CATEGORY, TITLE

class Expense:
    """
    A class that represents a monetary expense.

    Attributes: 
        amount (int | None): 
            The amount of the expense.
        category (str | None): 
            The category of the expense, e.g., "Essential" or "Non Essential".
        title (str | None): 
            The title of the expense.
    """

    def __init__(
            self, 
            amount: float,
            category: str,
            title: str,
        ):
        '''
        Initializes a new Expense instance with specified attributes.

        Args:
            amount (float | None): 
                The amount of the expense.
            category (str | None): 
                The category of the expense.
            title (str | None): 
                The title of the expense.
        '''
        self.__state = {
            AMOUNT: amount,
            CATEGORY: category,
            TITLE: title,
        }

    def get_state(self) -> dict:
        """
        Retrieves a copy of the expense's internal state.

        Returns: 
            dict: A dictionary containing the expense's state.
        """
        return self.__state.copy()

    
    def set_amount(self, amount: float) -> None:
        """
        Sets the amount of the expense.

        Args: 
            amount (float): The expense's amount.

        Raises: 
            ValueError: If the provided `amount` is not a positive number.
        """
        if not is_positive_number(amount):
            raise ValueError(
                "=========================================================================\n" +
                "Error: The expense's amount can only be set to a number greater than 0.0\n" +
                "=========================================================================\n"
            )

        self.__state[AMOUNT] = float(amount)

    
    def get_amount(self) -> float:
        """
        Retrieves the expenses amount.

        Returns: 
            float: The amount of the expense.
        """
        return self.__state[AMOUNT]


    def set_category(self, category: str) -> None:
        """
        Sets the expenses category.

        Args: 
            category (str): The category of the expense.

        Raises:
            ValueError: If `category` is not a non-empty string.
        """
        if not is_non_empty_string(category):
            raise ValueError(
                "==========================================================\n" +
                "Error: The expense's category must be a non-empty string.\n" +
                "==========================================================\n"
            )
        
        self.__state[CATEGORY] = category
        

    def get_category(self) -> str:
        """
        Retrieves the expense's category.

        Returns: 
            str: The category of the expense.
        """
        return self.__state[CATEGORY]
    

    def set_title(self, title: str) -> None:
        """
        Sets the expense's title.

        Args:
            title (str): The title of the expense.

        Raises: 
            ValueError: If `title` is not a non-empty string.
        """
        if not is_non_empty_string(title):
            raise ValueError(
                "=======================================================\n" +
                "Error: The expense's title must be a non-empty string.\n" +
                "=======================================================\n"
            )    
        
        self.__state[TITLE] = title
    

    def get_title(self) -> str:
        """
        Retrieves the expense's title.

        Returns: 
            str: The title of the expense.
        """
        return self.__state[TITLE]