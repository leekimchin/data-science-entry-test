def check_divisibility(num, divisor):
    """
    Task 1:
    This function checks if `num` is divisible by `divisor`.

    Steps:
    1. Ensure both `num` and `divisor` are numeric (int or float).
    2. Return True if `num` is divisible by `divisor` (i.e., num % divisor == 0).
    3. Return False if not divisible or input is invalid.
    """

    # Check if both inputs are numeric
    if not isinstance(num, (int, float)) or not isinstance(divisor, (int, float)):
        return False  # Return False for invalid types

    # Check for division by zero
    if divisor == 0:
        return False  # Can't divide by zero

    # Check divisibility using modulus operator
    return num % divisor == 0


# Task 2
# Scenario 1: Check if 10 is divisible by 2
result1 = check_divisibility(10, 2)
print(result1)  # Expected output: True (because 10 % 2 == 0)

# Scenario 2: Check if 7 is divisible by 3
result2 = check_divisibility(7, 3)
print(result2)  # Expected output: False (because 7 % 3 != 0)
