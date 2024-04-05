# https://leetcode.com/problems/contains-duplicate

# Given an integer array nums, return true if any value appears at least twice in
# the array, and return false if every element is distinct.

from typing import List


class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        """
        If the length of the list of unique values is not equal to the length of the original list, then
        there are duplicates

        :param nums: List[int] -> this is the list of numbers that we're going to be checking for
        duplicates
        :type nums: List[int]
        :return: A boolean value.
        """
        unique_values = list(set(nums))

        if len(unique_values) != len(nums):
            return True
        else:
            return False


if __name__ == "__main__":
    sol = Solution()
    print(sol.containsDuplicate([1, 2, 3, 1]))
    print(sol.containsDuplicate([1, 2, 3, 4]))
    print(sol.containsDuplicate([1, 1, 1, 3, 3, 4, 3, 2, 4, 2]))
