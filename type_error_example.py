# type_error_example.py

# This will throw a TypeError because you can't concatenate a string and an integer.
print("The number is " + 5)  # TypeError: can only concatenate str (not "int") to str

# Fixed version - Convert the integer to a string before concatenating.
print("The number is " + str(5))
