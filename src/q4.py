def string_reverse(s):
    """
    Task 1
    - Create a function that reverses a given string (s).
    - s must be a string.
    - Return the reversed string.

    Steps:
    1. Check if `s` is a string.
       - If not, return an empty string.
    2. Reverse the string using slicing.
    3. Return the reversed string.
    """

    # Check if the input is a string
    if not isinstance(s, str):
        return ""  # Return empty string if input is not valid

    # Reverse the string using slicing [::-1]
    reversed_s = s[::-1]

    # Return the reversed string
    return reversed_s


# Task 2
# Scenario 1: Reverse "Hello World"
result1 = string_reverse("Hello World")
print(result1)

# Scenario 2: Reverse "Python"
result2 = string_reverse("Python")
print(result2)
