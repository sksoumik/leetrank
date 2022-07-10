# find dupliate elements in an array
# Solution: O(n), because it only iterates the list once and set lookups are O(1)


def find_duplicate(a):
    """
    "For each element in the array, if it's already in the set, add it to the duplicates list, otherwise
    add it to the set."
    
    The time complexity of this function is O(n) because we're iterating through the array once. The
    space complexity is O(n) because we're storing all n elements in the set
    
    :param a: the list of integers
    :return: The duplicates in the list
    """
    seen = set()
    dupliates = []

    for _, element in enumerate(a):
        if element in seen:
            dupliates.append(element)
        else:
            seen.add(element)
    return dupliates


if __name__ == "__main__":
    a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 2, 3, 4, 5, 6, 7, 8, 9, 10, 2]
    print(find_duplicate(a))

