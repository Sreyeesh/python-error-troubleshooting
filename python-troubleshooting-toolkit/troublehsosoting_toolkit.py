import logging

# Set up logging
logging.basicConfig(filename='troubleshooting.log', level=logging.INFO)

def sum_list(numbers):
    """Function to sum a list of numbers, with intentional bugs."""
    total = 0
    for number in numbers:
        total += number
    return total

def divide_numbers(num1, num2):
    """Function to divide two numbers, with intentional bugs."""
    return num1 / num2

def get_value(my_dict, key):
    """Function to retrieve a value from a dictionary."""
    return my_dict[key]

def factorial(n):
    """Function to calculate factorial, with intentional bugs."""
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

def is_palindrome(string):
    """Function to check if a string is a palindrome."""
    return string == string[::-1]

def main():
    print("Welcome to the Python Troubleshooting Toolkit!")
    print("You will be given functions with bugs. Your task is to fix them.")

    test_cases = {
        "Sum List": ([1, 2, '3', 4], sum_list),  # Intentional bug: '3' is a string
        "Divide Numbers": (10, 0, divide_numbers),  # Intentional bug: division by zero
        "Get Value": ({'a': 1, 'b': 2}, 'c', get_value),  # Intentional bug: key 'c' does not exist
        "Factorial": (-5, factorial),  # Intentional bug: negative input
        "Palindrome Check": ("Racecar", is_palindrome),  # Should be case-insensitive
    }

    for name, args in test_cases.items():
        try:
            if len(args) == 2:
                result = args[1](args[0])  # For single argument functions
            else:
                result = args[2](*args[:-1])  # For multi-argument functions
            print(f"{name} result: {result}")
        except Exception as e:
            print(f"{name} raised an error: {e}")
            logging.error(f"{name} error: {e}")

if __name__ == "__main__":
    main()
