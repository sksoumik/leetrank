# https://leetcode.com/problems/kth-largest-element-in-an-array/

# Given an integer array nums and an integer k, return the kth largest element in the array.
# Note that it is the kth largest element in the sorted order, not the kth distinct element.
# You must solve it in O(n) time complexity.


# Example 1:
# Input: nums = [3,2,1,5,6,4], k = 2
# Output: 5

# Example 2:
# Input: nums = [3,2,3,1,2,4,5,5,6], k = 4
# Output: 4

from typing import List
import random


class Solution:
    # naive solution
    def _findKthLargest(self, nums: List[int], k: int) -> int:
        nums.sort(reverse=True)  # [6, 5, 5, 4, 3, 3, 2, 1]
        return nums[k]  # read from backward

    # use quick select algorithm for time complexity O(n) on average
    def findKthLargest(self, nums: List[int], k: int) -> int:
        if not nums:
            return None

        # pivot = nums[0]
        pivot = random.choice(nums)

        # all numbers which are higher than pivot will be on high list
        high = [num for num in nums if num > pivot]
        # all numbers which are lower than pivot will be on low list
        low = [num for num in nums if num < pivot]
        # all numbers which are equal to pivot will be on equal list
        equal = [num for num in nums if num == pivot]

        # list lengths
        high_length = len(high)
        equal_length = len(equal)

        # if k is less than or equal to high list length, then kth largest element is in high list
        if k <= high_length:
            return self.findKthLargest(high, k)

        # If k is greater than high list length and equal list length, then kth largest element is in
        # low list.
        elif k > high_length + equal_length:
            return self.findKthLargest(low, k - high_length - equal_length)

        else:
            return pivot


if __name__ == "__main__":
    nums = [3, 2, 1, 5, 6, 4]
    k = 2
    sol = Solution()
    print(sol._findKthLargest(nums, k))

    nums = [3, 2, 3, 1, 2, 4, 5, 5, 6]
    k = 4
    print(sol.findKthLargest(nums, k))
