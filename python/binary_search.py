# https://leetcode.com/problems/binary-search/

# Given an array of integers nums which is sorted in ascending order,
# and an integer target, write a function to search target in nums.
# If target exists, then return its index. Otherwise, return -1.
# You must write an algorithm with O(log n) runtime complexity.
from typing import List


class Solution:
    def search(self, nums: List[int], target: int):
        i, j = 0, len(nums) - 1
        while i <= j:
            idx_of_mid = (i + j) // 2
            mid_element = nums[idx_of_mid]

            if target == mid_element:
                return idx_of_mid
            if target > mid_element:
                i = idx_of_mid + 1
            else:
                j = idx_of_mid - 1
        return -1


if __name__ == "__main__":
    obj = Solution()
    # test case 1
    nums = [-1, 0, 3, 5, 9, 12]
    target = 9
    print(obj.binary_search(nums, target))

    # test case 2
    nums = [-1, 0, 3, 5, 9, 12]
    target = 2
    print(obj.binary_search(nums, target))
