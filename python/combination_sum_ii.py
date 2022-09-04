# https://leetcode.com/problems/combination-sum-ii/

# Given a collection of candidate numbers (candidates) and a target number (target),
# find all unique combinations in candidates where the candidate numbers sum to target.
# Each number in candidates may only be used once in the combination.
# Note: The solution set must not contain duplicate combinations.


# Example 1:
# Input: candidates = [10,1,2,7,6,1,5], target = 8
# Output:
# [
# [1,1,6],
# [1,2,5],
# [1,7],
# [2,6]
# ]


# Example 2:
# Input: candidates = [2,5,2,1,2], target = 5
# Output:
# [
# [1,2,2],
# [5]
# ]
from typing import List


class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        # sort the candidates
        candidates.sort()

        result = []

        def dfs(current_combination, current_sum, idx):

            if current_sum > target:
                return None

            if current_sum == target:
                result.append(current_combination)
                return None

            for i in range(idx, len(candidates)):
                # avoid repeated combinations
                if i > idx and candidates[i] == candidates[i - 1]:
                    continue
                dfs(
                    current_combination + [candidates[i]],
                    current_sum + candidates[i],
                    i + 1,
                )

        dfs([], 0, 0)
        return result


if __name__ == "__main__":
    print(Solution().combinationSum2([10, 1, 2, 7, 6, 1, 5], 8))
    print(Solution().combinationSum2([2, 5, 2, 1, 2], 5))
