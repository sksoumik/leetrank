# https://leetcode.com/explore/interview/card/top-interview-questions-easy/92/array/646/

# Given an array, rotate the array to the right by k steps, where k is non-negative.

# Example 1:

# Input: nums = [1,2,3,4,5,6,7], k = 3
# Output: [5,6,7,1,2,3,4]

from typing import List

class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # A base case. If k is 0, then we don't need to rotate the array.
        if k == 0:
            return
        k = k % len(nums)
        nums[:] = nums[-k:] + nums[:-k]


if __name__ == "__main__":
    nums = [1,2,3,4,5,6,7]
    k = 3
    Solution().rotate(nums, k)
    print(nums)
    nums = [1,2,3,4,5,6,7]
    k = 0
    Solution().rotate(nums, k)
    print(nums)
    