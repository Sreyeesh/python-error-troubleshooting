# documentation_logging_example.py

import logging

# Setting up a basic logger to log error messages
logging.basicConfig(level=logging.INFO)

# Example function with documentation and logging
def divide(a: int, b: int) -> float:
    """
    Divides two numbers.
    
    Args:
        a (int): The numerator.
        b (int): The denominator.
    
    Returns:
        float: The result of the division.
    
    Raises:
        ZeroDivisionError: If b is zero.
    """
    if b == 0:
        logging.error("Attempted to divide by zero")
        raise ZeroDivisionError("Cannot divide by zero")
    return a / b

# Test the function
try:
    result = divide(10, 0)
except ZeroDivisionError as e:
    logging.error(f"Error occurred: {e}")
