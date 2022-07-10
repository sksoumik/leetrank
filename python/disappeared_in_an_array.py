# https://leetcode.com/problems/find-all-numbers-disappeared-in-an-array/

# Given an array nums of n integers where nums[i] is in the range [1, n],
# return an array of all the integers in the range [1, n] that do not appear in nums.


# Example 1:

# Input: nums = [4,3,2,7,8,2,3,1]
# Output: [5,6]

from typing import List


class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        """
        We create a list of all numbers from 1 to n, and then find all uncommon numbers between all_nums
        and nums

        :param nums: List[int] -> The list of numbers that we are given
        :type nums: List[int]
        :return: A list of all numbers that are not in the input list.
        """

        # Creating a list of all numbers from 1 to n.
        all_nums = []

        for num in range(1, len(nums) + 1):
            all_nums.append(num)

        # find all uncommon numbers between all_nums and nums
        disapppeared_nums = list(set(all_nums) ^ set(nums))
        return disapppeared_nums


if __name__ == "__main__":
    nums = [4, 3, 2, 7, 8, 2, 3, 1]
    print(Solution().findDisappearedNumbers(nums))
