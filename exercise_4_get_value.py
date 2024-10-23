def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

# Test case
print(factorial(-5))  # Should handle negative input
