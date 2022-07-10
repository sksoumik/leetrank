# https://leetcode.com/problems/single-number/

# Given a non-empty array of integers nums, every element appears twice except for one.
#  Find that single one.
# You must implement a solution with a linear runtime complexity and use only constant extra space.

# Input: nums = [2,2,1]
# Output: 1

from typing import List
from operator import xor
from functools import reduce


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        """
        Reduce(function, iterable) applies function of two arguments cumulatively to the items of
        iterable, from left to right, so as to reduce the iterable to a single value
        
        :param nums: List[int]
        :type nums: List[int]
        :return: The reduce function is being used to apply a function of two arguments cumulatively to
        the items of an iterable, from left to right, so as to reduce the iterable to a single value.
        """
        return reduce(xor, nums)


if __name__ == "__main__":
    s = Solution()
    print(s.singleNumber([2, 2, 1]))
