# https://leetcode.com/problems/maximum-subarray/
# Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
# Output: 6
# Explanation: [4,-1,2,1] has the largest sum = 6.


def fn_max_subarray(nums):
    """
    We keep track of the current sum and the maximum sum. If the current sum is greater than the maximum
    sum, we update the maximum sum. If the current sum is less than 0, we reset the current sum to 0

    :param nums: the list of numbers
    :return: The maximum sum of a subarray.
    """
    max_sum = float("-inf")
    current_sum = 0

    for idx, item in enumerate(nums):
        current_sum += item

        if current_sum > max_sum:
            max_sum = current_sum

        if current_sum < 0:
            current_sum = 0

    return max_sum



if __name__ == "__main__":
    arr = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
    print(fn_max_subarray(arr))

    # arr2 = [1]
    # print(fn_max_subarray(arr2))

    # arr3 = [-2, -1]
    # print(fn_max_subarray(arr3))
