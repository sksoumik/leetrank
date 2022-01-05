# find dupliate elements in an array
# Solution: O(n), because it only iterates the list once and set lookups are O(1)


def find_duplicate(a):
    seen = set()
    dupliates = []

    for _, element in enumerate(a):
        if element in seen:
            dupliates.append(element)
        else:
            seen.add(element)
    return dupliates


if __name__ == "__main__":
    a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    print(find_duplicate(a))

