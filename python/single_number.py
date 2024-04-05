# https://leetcode.com/problems/single-number/

# Given a non-empty array of integers nums, every element appears twice except for one.
#  Find that single one.
# You must implement a solution with a linear runtime complexity and use only constant extra space.

# Input: nums = [2,2,1]
# Output: 1

from collections import Counter
from functools import reduce
from operator import xor
from typing import List


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

    # solution 2 using Counter
    def singleNumber_2(self, nums: List[int]) -> int:
        c = Counter(nums)
        for k, v in c.items():
            if v == 1:
                return k

    # solution 3 using count
    def singleNumber_3(self, nums: List[int]) -> int:
        for num in nums:
            if nums.count(num) == 1:
                return num


if __name__ == "__main__":
    s = Solution()
    print(s.singleNumber([2, 2, 1]))
