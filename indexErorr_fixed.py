# index_error_solution.py

my_list = [1, 2, 3, 4]

# Let's try accessing index 3, which is valid, and index 5, which is out of range
index_to_access = 5

# Check if the index exists before accessing it
if index_to_access < len(my_list):
    print(f"Element at index {index_to_access}: {my_list[index_to_access]}")
else:
    print(f"Index {index_to_access} is out of range. The list has only {len(my_list)} elements.")
