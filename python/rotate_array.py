# https://leetcode.com/explore/interview/card/top-interview-questions-easy/92/array/646/

# Given an array, rotate the array to the right by k steps, where k is non-negative.

# Example 1:

# Input: nums = [1,2,3,4,5,6,7], k = 3
# Output: [5,6,7,1,2,3,4]

from typing import List

class Solution:
    # solution 1
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # A base case. If k is 0, then we don't need to rotate the array.
        if k == 0:
            return
        k = k % len(nums)
        nums[:] = nums[-k:] + nums[:-k]


    # solution 2
    # time O(n) and space O(1)
    def rotate2(self, nums: List[int], k: int) -> None:
        # Original List                   : 1 2 3 4 5 6 7
        # After reversing all numbers     : 7 6 5 4 3 2 1
        # After reversing first k numbers : 5 6 7 4 3 2 1
        # After revering last n-k numbers : 5 6 7 1 2 3 4 --> Result

        k %= len(nums)

        # Reverse the whole list
        self.reverse(nums, 0, len(nums)-1)
        # reverse the first k numbers
        self.reverse(nums, 0, k-1)
        # reverse the last n-k numbers
        self.reverse(nums, k, len(nums)-1)

    def reverse(self, nums: List[int], start: int, end: int) -> None:
        while start < end:
            nums[start], nums[end] = nums[end], nums[start]
            start += 1
            end -= 1




if __name__ == "__main__":
    nums = [1,2,3,4,5,6,7]
    k = 3
    Solution().rotate(nums, k)
    print(nums)
    nums = [1,2,3,4,5,6,7]
    k = 9
    Solution().rotate(nums, k)
    print(nums)

    nums = [1,2,3,4,5,6,7]
    k = 9
    Solution().rotate2(nums, k)
    print(nums)
    