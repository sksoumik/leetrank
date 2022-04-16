# https://leetcode.com/problems/single-number/

# Given a non-empty array of integers nums, every element appears twice except for one.
#  Find that single one.
# You must implement a solution with a linear runtime complexity and use only constant extra space.

# Input: nums = [2,2,1]
# Output: 1

from typing import List


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        """
        We iterate through the list, and if the count of the number is equal to 1,
        we return that number

        :param nums: List[int] -> this is the list of numbers that we are given
        :type nums: List[int]
        :return: The number that only appears once in the list.
        """
        for num in nums:
            if nums.count(num) == 1:
                return num


if __name__ == "__main__":
    s = Solution()
    print(s.singleNumber([2, 2, 1]))
