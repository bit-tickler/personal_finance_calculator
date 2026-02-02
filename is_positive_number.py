def is_positive_number(value: float) -> bool:
    """
    Checks that the provided value argument is
    a positive number.

    Args:
        value (float): The value to be validated.
    
    Returns: 
        bool: 
            True: if the provided value is not a bolean and is
            a positive number.
            False: otherwise
    """
    # Check if value is not a boolean and is greater than 0
    return not isinstance(value, bool) and value > 0
