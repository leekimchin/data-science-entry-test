def find_and_replace(lst, find_val, replace_val):
    """
    Task 1:
    This function searches for all occurrences of `find_val` in the given list `lst`
    and replaces them with `replace_val`.

    Steps:
    1. Iterate through the list.
    2. Replace each occurrence of `find_val` with `replace_val`.
    3. Return the modified list.
    """
    
    # Use list comprehension to replace values
    modified_list = [replace_val if item == find_val else item for item in lst]

    return modified_list


# Task 2:
# Scenario 1: Replace all 2s with 5 in the list [1, 2, 3, 4, 2, 2]
result1 = find_and_replace([1, 2, 3, 4, 2, 2], 2, 5)
print(result1)

# Scenario 2: Replace all "apple" with "orange" in the list ["apple", "banana", "apple"]
result2 = find_and_replace(["apple", "banana", "apple"], "apple", "orange")
print(result2)
