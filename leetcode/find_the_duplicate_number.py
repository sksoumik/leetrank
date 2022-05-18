# https://leetcode.com/problems/find-the-duplicate-number

# Given an array of integers nums containing n + 1 integers where each integer is in the range [1, n] inclusive.

# There is only one repeated number in nums, return this repeated number.

# You must solve the problem without modifying the array nums and uses only constant extra space.

from typing import List


class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        """
        We iterate through the list, and if we see an element that we've seen before, we return it

        :param nums: List[int] -> This is the list of numbers that we're going to be searching through
        :type nums: List[int]
        :return: The first duplicate element in the list.
        """
        seen = set()

        for _, element in enumerate(nums):
            if element in seen:
                return element
            else:
                seen.add(element)

        return -1


if __name__ == "__main__":
    nums = [1, 3, 4, 2, 2]
    print(Solution().findDuplicate(nums))
