def string_reverse(s):
    """
    Task 1:
    This function reverses the given string `s`.

    Steps:
    1. Check if `s` is a string.
       - If not, return an empty string or handle it appropriately.
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
print(result1)  # Expected output: "dlroW olleH"

# Scenario 2: Reverse "Python"
result2 = string_reverse("Python")
print(result2)  # Expected output: "nohtyP"
