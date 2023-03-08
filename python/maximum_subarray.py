# https://leetcode.com/problems/maximum-subarray/
# Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
# Output: 6
# Explanation: [4,-1,2,1] has the largest sum = 6.

from typing import List

# brute force
# time complexity: O(n^2)
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


class Solution:
    # Kadane's Algorithm
    # video explanation: https://youtu.be/6HntYGZyjZI
    def maxSubArray(self, nums: List[int]) -> int:
        current_sum = maximum_sum = nums[0]

        for num in nums:
            current_sum = max(num, current_sum + num)
            maximum_sum = max(maximum_sum, current_sum)

        return maximum_sum


if __name__ == "__main__":
    arr = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
    print(bf_max_subarray(arr))
    print(Solution().maxSubArray(arr))