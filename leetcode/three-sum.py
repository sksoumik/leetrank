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

# time limit exceeds
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        if len(nums) < 3:
            return []

        nums = sorted(nums)

        counter_results = []
        for comb in combinations(nums, 3):
            if sum(comb) == 0:
                c = Counter(comb)
                if c not in counter_results:
                    counter_results.append(c)

        return [list(i.elements()) for i in counter_results]

        # result = []
        # for c in counter_results:
        #     result.append(list(c.elements()))
        # return result


if __name__ == "__main__":
    sol = Solution()
    print(sol.threeSum([-1, 0, 1, 2, -1, -4]))
    print(sol.threeSum([]))
    print(sol.threeSum([0]))
