# value_error_example.py

# This will throw a ValueError because 'abc' cannot be converted to an integer.
int("abc")  # ValueError: invalid literal for int() with base 10: 'abc'

# Fixed version using a valid string that can be converted to an integer.
int("123")
