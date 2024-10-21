# /code/index_error_example.py

# This will throw an IndexError because index 5 is out of range.
my_list = [1, 2, 3]
print(my_list[5])  # IndexError: list index out of range

# Fixed version - Check if the index exists before accessing it
if len(my_list) > 5:
    print(my_list[5])
else:
    print("Index out of range")
