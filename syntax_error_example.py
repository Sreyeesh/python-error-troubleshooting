# syntax_error_example.py

# This will throw a SyntaxError because the colon is missing.
for i in range(3)  # SyntaxError: invalid syntax
    print(i)

# Fixed version - Add the missing colon.
for i in range(3):
    print(i)
