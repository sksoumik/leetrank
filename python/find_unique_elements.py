# unique elements and appeared only once is not the same.
# unique is means, occurrence of the same element is 1.

# For example,

# nums = [1, 2, 3, 2, 3]
# unique elements (set) will return `[1, 2, 3]` but
# appeared only once will return `[1]`.


def get_unique(nums):
    """
    It takes a list as an argument, and returns a list of all the elements that occur only once in the
    argument list

    :param lst: the list to be filtered
    :return: A list of the elements that only appear once in the list.
    """
    counter = {}

    for i in nums:
        if i in counter:
            counter[i] += 1
        else:
            counter[i] = 1

    appeared_once = []
    for key, value in counter.items():
        if value == 1:
            appeared_once.append(key)

    return appeared_once


if __name__ == "__main__":
    print(get_unique([1, 2, 3, 2, 3]))  # [1]
