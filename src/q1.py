def swap(x, y):
    """
    Task 1:
    This function swaps the values of x and y using only x and y as variables.
    
    Steps:
    1. Check if both x and y are numeric (either int or float).
       - If either is not numeric, return -1.
    2. Swap the values using tuple unpacking (x, y = y, x).
    3. Print the swapped values.
    """
    # Check if x and y are numeric using isinstance
    if not isinstance(x, (int, float)) or not isinstance(y, (int, float)):
        # If either x or y is not a number, return -1
        return -1

    # Swap the values of x and y using tuple unpacking
    x, y = y, x

    # Print the swapped values
    print(x, y)

# Task 2:
# Invoke the function with the given scenarios

# Scenario 1: Using "Apple" (a string) and 10 (a number)
result = swap("Apple", 10)
# Since "Apple" is not numeric, the function returns -1.
print(result)  # This will output: -1

# Scenario 2: Using 9 and 17 (both numbers)
swap(9, 17)
# The expected output is: 17 9, which is the swapped values of the provided numbers.
