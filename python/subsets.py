# https://leetcode.com/problems/subsets

# Given an integer array nums of unique elements, return all possible subsets (the power set).
# The solution set must not contain duplicate subsets. Return the solution in any order.


# Example 1:
# Input: nums = [1,2,3]
# Output: [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]

from typing import List


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = []
        self.backtrack(result, [], nums, 0)
        return result

    def backtrack(self, result, subset, nums, start):
        result.append(subset)
        for i in range(start, len(nums)):
            self.backtrack(result, subset + [nums[i]], nums, i + 1)


if __name__ == "__main__":
    nums = [1, 2, 3]
    print(Solution().subsets(nums))
