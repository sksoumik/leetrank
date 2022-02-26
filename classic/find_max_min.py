# find the maximum number from a list of integers
def find_max(nums):
    max_num = float("-inf")
    for num in nums:
        if num > max_num:
            max_num = num
    return max_num


def find_min(nums):
    min_num = float("inf")
    for num in nums:
        if num < min_num:
            min_num = num
    return min_num


if __name__ == "__main__":
    nums = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    print(find_max(nums))
    print(find_min(nums))
