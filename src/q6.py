def find_first_negative(lst):
    """
    Task 1:
    This function finds the first negative number in a list `lst`.

    Steps:
    1. Use a while loop to iterate through the list.
    2. If a negative number is found, return it immediately.
    3. If the loop completes without finding any, return "No negatives".
    """
    # Initialize index for while loop
    i = 0

    # Loop while index is within bounds of the list
    while i < len(lst):
        # Check if current element is negative
        if lst[i] < 0:
            return lst[i]  # Return the first negative number found
        i += 1  # Move to the next element

    # If loop completes with no negative found
    return "No negatives"


# Task 2
# Scenario 1: List with negatives: [3, 5, -1, 7, -2, 8]
result1 = find_first_negative([3, 5, -1, 7, -2, 8])
print(result1)  # Expected output: -1

# Scenario 2: List without negatives: [2, 10, 7, 0]
result2 = find_first_negative([2, 10, 7, 0])
print(result2)  # Expected output: "No negatives"
