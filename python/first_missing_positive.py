# https://leetcode.com/problems/first-missing-positive

# Given an unsorted integer array nums, return the smallest missing positive integer.
# You must implement an algorithm that runs in O(n) time and uses constant extra space.


# Example 1:
# Input: nums = [1,2,0]
# Output: 3
# Explanation: The numbers in the range [1,2] are all in the array.

from typing import List


class Solution:
    # O(n) time and O(1) space
    def firstMissingPositive(self, nums: List[int]) -> int:
        exist = set(nums)
        for i in range(1, len(nums) + 2):  # +2 because we have one missing number
            if i not in exist:
                return i

    # second solution
    def _firstMissingPositive(self, nums: List[int]) -> int:
        for i in range(1, len(nums) + 2):  # +2 because we have one missing number
            if i not in nums:
                return i


if __name__ == "__main__":
    nums = [1, 2, 0]
    print(Solution().firstMissingPositive(nums))
