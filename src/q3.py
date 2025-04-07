def update_dictionary(dct, key, value):
    """
    Task 1:
    This function updates a dictionary with a new key-value pair.

    - If the key already exists in the dictionary:
        - Print the original value.
        - Update the value with the new one.
    - If the key doesn't exist:
        - Simply add the key-value pair to the dictionary.
    - Return the updated dictionary.
    """

    # Check if the key already exists in the dictionary
    if key in dct:
        # Print the original value before updating
        print(f"Original value for key '{key}': {dct[key]}")

    # Update the dictionary (either adds new key or updates existing one)
    dct[key] = value

    # Return the modified dictionary
    return dct


# Task 2
# Scenario 1: Adding a new key-value pair to an empty dictionary
result1 = update_dictionary({}, "name", "Alice")
print(result1)  # Expected output: {'name': 'Alice'}

# Scenario 2: Updating an existing key in a dictionary
result2 = update_dictionary({"age": 25}, "age", 26)
# Expected output:
# Original value for key 'age': 25
# {'age': 26}
print(result2)
