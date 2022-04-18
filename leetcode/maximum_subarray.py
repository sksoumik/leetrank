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
    max_sum = nums[0]
    curr_sum = 0
    for i in range(len(nums)):
        curr_sum += nums[i]
        if curr_sum > max_sum:
            max_sum = curr_sum
        if curr_sum < 0:
            curr_sum = 0
    print(curr_sum)
    return max_sum


if __name__ == "__main__":
    arr = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
    print(fn_max_subarray(arr))

    # arr2 = [1]
    # print(fn_max_subarray(arr2))

    # arr3 = [-2, -1]
    # print(fn_max_subarray(arr3))
