def is_palindrome(string):
    return string == string[::-1]

# Test case
print(is_palindrome("Racecar"))  # Should ignore case
