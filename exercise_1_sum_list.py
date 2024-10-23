def sum_list(numbers):
    total = 0
    for number in numbers:
        total += number
    return total

# Test case
print(sum_list([1, 2, '3', 4]))  # Should return 10
