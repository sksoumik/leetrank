# https://leetcode.com/problems/permutations/

# Given an array nums of distinct integers, return all the possible permutations.
# You can return the answer in any order.

# Example 1:
# Input: nums = [1,2,3]
# Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]

from typing import List
import itertools


class Solution:
    # Time Complexity should be O(N * N!),
    # because "res.append(subset)" action should be O(N)
    def permute(self, nums: List[int]) -> List[List[int]]:
        result = []
        visited = set()
        self.backtrack(result, visited, [], nums)
        return result

    def backtrack(self, result, visited, subset, nums):
        if len(subset) == len(nums):
            result.append(subset)

        for i in range(len(nums)):
            if i not in visited:
                visited.add(i)
                self.backtrack(result, visited, subset + [nums[i]], nums)
                # remove the current number from visited in order
                # to allow for the creation of new permutations
                visited.remove(i)

    # using library
    def permute2(self, nums: List[int]) -> List[List[int]]:
        # return list(itertools.permutations(nums))
        result = map(list, itertools.permutations(nums))
        return list(result)


if __name__ == "__main__":
    nums = [1, 2, 3]
    print(Solution().permute(nums))
    print(Solution().permute2(nums))
