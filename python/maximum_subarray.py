# https://leetcode.com/problems/maximum-subarray/
# Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
# Output: 6
# Explanation: [4,-1,2,1] has the largest sum = 6.


# brute force
def bf_max_subarray(nums):
    """
    We check for all possible subarrays and find it's sum and update the maximum sum
    """
    max_sum = float("-inf")
    all_subarrays = []

    for i in range(len(nums)):
        for j in range(i, len(nums)):
            all_subarrays.append(nums[i:j + 1])

    for subarray in all_subarrays:
        max_sum = max(max_sum, sum(subarray))

    return max_sum



# approach 1
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


from typing import List


class Solution:
    # video explanation: https://youtu.be/6HntYGZyjZI
    def maxSubArray(self, nums: List[int]) -> int:
        current_sum = maximum_sum = nums[0]

        for num in nums:
            current_sum = max(num, current_sum + num)
            maximum_sum = max(maximum_sum, current_sum)

        return maximum_sum

    # brute force
    # time complexity O(n^2)
    # check for all possible subarrays and find it's sum and update the maximum sum
    def _maxSubArray(self, nums: List[int]) -> int:
        max_sum = float("-inf")

        for i in range(len(nums)):
            current_sum = 0
            for j in range(i, len(nums)):
                current_sum += nums[j]
                max_sum = max(max_sum, current_sum)

        return max_sum


if __name__ == "__main__":
    arr = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
    print(fn_max_subarray(arr))
    print(Solution().maxSubArray(arr))

    # arr2 = [1]
    # print(fn_max_subarray(arr2))

    # arr3 = [-2, -1]
    # print(fn_max_subarray(arr3))
