# error_prevention_example.py

# Example 1: Validating input to prevent a ValueError
user_input = input("Enter a number: ")
if user_input.isdigit():
    number = int(user_input)
    print(f"You entered the number: {number}")
else:
    print("Invalid input!")

# Example 2: Checking list bounds to prevent IndexError
my_list = [1, 2, 3]
index = 5

if index < len(my_list):
    print(my_list[index])
else:
    print("Index out of range")
