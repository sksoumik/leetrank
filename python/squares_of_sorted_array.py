# https://leetcode.com/problems/squares-of-a-sorted-array

# Given an integer array nums sorted in non-decreasing order, return an array
# of the squares of each number sorted in non-decreasing order.

from typing import List


class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        """
        We are taking a list of numbers, squaring each number, and then sorting the list of squared
        numbers

        :param nums: List[int] -> this is the list of numbers that we are going to be squaring and
        sorting
        :type nums: List[int]
        :return: A list of the squares of the numbers in the list.
        """
        return sorted([x**2 for x in nums])


if __name__ == "__main__":
    sol = Solution()
    print(sol.sortedSquares([-4, -1, 0, 3, 10]))
    print(sol.sortedSquares([-7, -3, 2, 3, 11]))
