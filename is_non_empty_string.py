def is_non_empty_string(value: str) -> bool:
    """
    Checks if the at the provided value is a non-empty string.
    
    Returns:
        bool: 
            Indicates whether the provided value is:
            - A string
            - A non-empty string with non-whitespace characters
    """
    '''
    Check that the provided value is a string.
    Check that the string is not empty by calling the string's strip method,
    which returns False if the string is empty.
    '''
    return isinstance(value, str) and bool(value.strip())
