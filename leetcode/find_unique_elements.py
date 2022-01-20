# unique is set elements are not same
# unique is means, occurrence of the same element is 1
# set returns all unique elements in the list but which has appeared more than once, or not
# doesn't care


def get_unique(lst):
    # lst: list of ints
    # return: list of ints
    filter_rule = filter(lambda x: lst.count(x) == 1, lst)
    return list(filter_rule)


if __name__ == "__main__":
    print(get_unique([1, 2, 3, 2, 3]))  # [1]

