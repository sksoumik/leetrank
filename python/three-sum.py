# https://leetcode.com/problems/3sum/
# Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]]
# such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

# Notice that the solution set must not contain duplicate triplets.

# Example 1:

# Input: nums = [-1,0,1,2,-1,-4]
# Output: [[-1,-1,2],[-1,0,1]]

from typing import List
from itertools import combinations
from collections import Counter


class Solution:
    # time limit exceeds
    def threeSum_1(self, nums: List[int]) -> List[List[int]]:
        counter_results = []
        for comb in combinations(nums, 3):
            if sum(comb) == 0:
                c = Counter(comb)
                if c not in counter_results:
                    counter_results.append(c)

        return [list(i.elements()) for i in counter_results]

    # time limit exceeds
    def threeSum_2(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        combs = [list(i) for i in combinations(nums, 3) if sum(i) == 0]
        # remove lists that contain same elements
        result = [list(i) for i in set(tuple(i) for i in combs)]
        return result

    # accepted solution
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        """
        We sort the array, and then iterate through the array, using the current element as the first
        element in the triplet.

        We then use a two pointer approach to find the other two elements.

        We use a set to avoid duplicates.

        :param nums: the list of numbers
        :type nums: List[int]
        :return: A list of lists of integers.
        """
        nums.sort()
        output = set()

        for k in range(len(nums)):
            target = -nums[k]
            i, j = k + 1, len(nums) - 1
            while i < j:
                sum_two = nums[i] + nums[j]
                if sum_two == target:
                    output.add((nums[k], nums[i], nums[j]))
                    i += 1
                    j -= 1
                elif sum_two < target:
                    i += 1
                else:
                    j -= 1

        return [list(i) for i in output]


if __name__ == "__main__":
    sol = Solution()
    print(sol.threeSum([-1, 0, 1, 2, -1, -4]))
    print(sol.threeSum([0, 1, 1]))
    print(sol.threeSum([0, 0, 0]))
