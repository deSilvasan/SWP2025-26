"""
Simulate the behavior of a set using list comprehension and create a dictionary comprehension mapping English characters
to their ASCII (Unicode) values.
"""

def simulate_set(lst):
    """
    Simulate set functionality using list comprehension. It removes duplicates while preserving the original order.
    """
    unique_elements = []
    # Append each element only if it is not already in the unique list
    [unique_elements.append(e) for e in lst if e not in unique_elements]
    return unique_elements


def create_ascii_dict(letters):
    """
    Create a dictionary where the given letters are keys and their ASCII (Unicode) values are the corresponding values.
    """
    # Dictionary comprehension: {letter: ASCII_value for each letter in the list}
    ascii_dict = {char: ord(char) for char in letters}
    return ascii_dict


if __name__ == "__main__":
    # Example list with duplicates
    lst = [1, 5, 8, 5, 9, 7, 6,5, 8,1, 3,2,9]

    # Simulate set behavior
    simulated_set = simulate_set(lst)
    print("Original list:", lst)
    print("Simulated set (duplicates removed):", simulated_set)

    # Example list of letters
    letter_list = ['A', 'B', 'C', 'a', 'b', 'c', 'x', 'y', 'z']

    # Create ASCII dictionary based on provided letters
    ascii_mapping = create_ascii_dict(letter_list)
    print("\nASCII dictionary for given letters:")
    print(ascii_mapping)
