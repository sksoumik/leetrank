# Input: list1 = [1,2,4], list2 = [1,3,4]
# Output: [1,1,2,3,4,4]


def merge_sorted_array(list1, list2):
    """
    It takes two lists and returns a sorted list.

    :param list1: [1, 3, 5, 7, 9]
    :param list2: [1, 3, 4, 5]
    :return: A sorted list of the two lists combined.
    """
    res = list1 + list2
    sorted_res = sorted(res)
    return sorted_res


if __name__ == "__main__":
    list1 = [1, 2, 4]
    list2 = [1, 3, 4]
    print(merge_sorted_array(list1, list2))
