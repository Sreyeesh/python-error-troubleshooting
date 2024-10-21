# /code/zero_division_error_example.py

# This will throw a ZeroDivisionError because we are dividing by zero.
def divide(a, b):
    return a / b

x = 10
y = 0
result = divide(x, y)  # ZeroDivisionError: division by zero

# Adding print statements to debug the issue.
def divide(a, b):
    print(f"a: {a}, b: {b}")  # This shows the values before the error occurs
    return a / b

result = divide(x, y)  # This will still raise the error, but now we see the values
