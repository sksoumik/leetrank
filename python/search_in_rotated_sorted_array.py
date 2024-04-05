# https://leetcode.com/problems/search-in-rotated-sorted-array

# There is an integer array nums sorted in ascending order (with distinct values).
# Prior to being passed to your function,
# nums is possibly rotated at an unknown pivot index k (1 <= k < nums.length)
# such that the resulting array is [nums[k], nums[k+1], ..., nums[n-1],
#  nums[0], nums[1], ..., nums[k-1]] (0-indexed). For example, [0,1,2,4,5,6,7] might be rotated at pivot index 3 and become [4,5,6,7,0,1,2].

# Given the array nums after the possible rotation and an integer target, r
# eturn the index of target if it is in nums, or -1 if it is not in nums.

# You must write an algorithm with O(log n) runtime complexity.


# Example 1:
# Input: nums = [4,5,6,7,0,1,2], target = 0
# Output: 4

# Example 2:
# Input: nums = [4,5,6,7,0,1,2], target = 3
# Output: -1

from typing import List


class Solution:
    # brute force approach
    def _search(self, nums: List[int], target: int) -> int:
        for idx, num in enumerate(nums):
            if num == target:
                return idx
        return -1

    # binary search approach
    # time complexity: O(log n)
    # space complexity: O(1)
    # video explanation: https://youtu.be/U8XENwh8Oy8
    def search(self, nums: List[int], target: int) -> int:
        # left pointer
        left = 0
        # right pointer
        right = len(nums) - 1

        while left <= right:
            # middle pointer
            mid = (left + right) // 2

            # if the middle element is the target
            if nums[mid] == target:
                return mid

            # if the left side is sorted | left rotated
            if nums[left] <= nums[mid]:
                # if the target is in the left side
                if nums[left] <= target <= nums[mid]:
                    right = mid - 1
                # if the target is in the right side
                else:
                    left = mid + 1
            # if the right side is sorted
            else:
                # if the target is in the right side
                if nums[mid] <= target <= nums[right]:
                    left = mid + 1
                # if the target is in the left side
                else:
                    right = mid - 1
        return -1


if __name__ == "__main__":
    nums = [4, 5, 6, 7, 0, 1, 2]
    target = 0
    print(Solution().search(nums, target))

    nums = [4, 5, 6, 7, 0, 1, 2]
    target = 3
    print(Solution().search(nums, target))
