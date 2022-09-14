# you are given a list of integers, find the standard deviation of them

# A standard deviation (or σ) is a measure of how dispersed the data is in relation to the mean.
# Low standard deviation means data are clustered around the mean,
# and high standard deviation indicates data are more spread out.

import math


def get_std(nums):
    # get the mean
    mean = sum(nums) / len(nums)
    # get the variance
    square_nums = []
    for num in nums:
        square_nums.append((num - mean) ** 2)

    variance = sum(square_nums) / len(square_nums)
    std_value = math.sqrt(variance)
    return std_value


if __name__ == "__main__":
    print(get_std([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))
    print(get_std([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]))
    print(get_std([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]))
