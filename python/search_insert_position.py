# https://leetcode.com/problems/search-insert-position

# Given a sorted array of distinct integers and a target value, return the index if
# the target is found. If not, return the index where it would be if it were inserted in order.
# You must write an algorithm with O(log n) runtime complexity.

from typing import List


class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        """
        If the target is in the array, return its index. Otherwise, return the index where the target
        would be if it were inserted in order

        :param nums: the list of numbers
        :type nums: List[int]
        :param target: the value we're looking for
        :type target: int
        :return: The index of the target if it is found in the list. If the target is not found, the
        index where the target would be if it were inserted in order.
        """
        # start index: left
        # end index: right
        # mid index: mid

        # base case
        if len(nums) == 0:
            return 0

        left, right = 0, len(nums) - 1

        while left <= right:
            mid = (left + right) // 2
            # target fall in the right side
            if target > nums[mid]:
                left = mid + 1
            # else: falls in the left side
            else:
                right = mid - 1

        return left

    # solution 2
    def searchInsert(self, nums: List[int], target: int) -> int:
        for idx, num in enumerate(nums):
            if num >= target:
                return idx
        return len(nums)


if __name__ == "__main__":
    s = Solution()
    print(s.searchInsert([1, 3, 5, 6], 5))
    print(s.searchInsert([1, 3, 5, 6], 2))
    print(s.searchInsert([1, 3, 5, 6], 7))
    print(s.searchInsert([1, 3, 5, 6], 0))
