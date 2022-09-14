# you are given a list of integers, find the median of them


def get_median(nums):
    nums = sorted(nums)
    # length of the list is even
    if len(nums) % 2 == 0:
        # get the two middle numbers
        middle_1 = len(nums) // 2
        middle_2 = middle_1 - 1
        # return the average of the two middle numbers
        return (nums[middle_1] + nums[middle_2]) / 2

    # length of the list is odd
    else:
        return nums[len(nums) // 2]


if __name__ == "__main__":
    print(get_median([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))
    print(get_median([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]))
    print(get_median([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]))
