# https://leetcode.com/problems/combination-sum

# Given an array of distinct integers candidates and a target integer target,
# return a list of all unique combinations of candidates where the chosen numbers sum to target.
# You may return the combinations in any order.

# The same number may be chosen from candidates an unlimited number of times.
#  Two combinations are unique if the frequency of at least one of the chosen numbers is different.

# It is guaranteed that the number of unique combinations that
# sum up to target is less than 150 combinations for the given input.


# Example 1:
# Input: candidates = [2,3,6,7], target = 7
# Output: [[2,2,3],[7]]
# Explanation:
# 2 and 3 are candidates, and 2 + 2 + 3 = 7. Note that 2 can be used multiple times.
# 7 is a candidate, and 7 = 7.
# These are the only two combinations.

# Example 2:
# Input: candidates = [2,3,5], target = 8
# Output: [[2,2,2,2],[2,3,3],[3,5]]

# Example 3:
# Input: candidates = [2], target = 1
# Output: []

from typing import List


# We start with an empty list, and we add to it as we go
class Solution:
    # dfs:
    # time complexity: O(2^n), where n is the length of candidates
    # O(2^N) time because for each recursive call we are doing
    # 2 * (n - 1) operations due to constantly shrinking down the input list in each recursive call.
    # space complexity: O(n)
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        answer = []

        # try out each possible cases
        # maintain idx for avoiding repeated combinations
        def dfs(current_combination, current_sum, idx):
            # this is the case, cur_sum will never equal to target
            if current_sum > target:
                return
            # if equal, add to answer
            if current_sum == target:
                answer.append(current_combination)
                return
            for i in range(idx, len(candidates)):
                dfs(
                    current_combination + [candidates[i]],
                    current_sum + candidates[i],
                    i,
                )

        dfs([], 0, 0)
        return answer

    # dynamic programming
    def combinationSum_DP(self, candidates: List[int], target: int) -> List[List[int]]:
        dp = [[] for _ in range(target + 1)]

        for i in candidates:
            for j in range(i, target + 1):
                if j == i:
                    dp[j].append([i])
                else:
                    for k in dp[j - i]:
                        dp[j].append(k + [i])

        return dp[target]

    # using cache for dynamic programming
    @lru_cache(None)
    def combinationSum_DP_cache(
        self, candidates: List[int], target: int
    ) -> List[List[int]]:
        result = []

        def dfs(current_combination, current_sum, idx):
            if current_sum > target:
                return
            if current_sum == target:
                result.append(current_combination)
                return
            for i in range(idx, len(candidates)):
                dfs(
                    current_combination + [candidates[i]],
                    current_sum + candidates[i],
                    i,
                )

        dfs([], 0, 0)
        return result


if __name__ == "__main__":
    s = Solution()
    # print(s.combinationSum([2, 3, 5], 8))
    # print(s.combinationSum([2, 3, 5], 1))
    print(s.combinationSum([2, 3, 6, 7], 7))
    print(s.combinationSum_DP([2, 3, 6, 7], 7))
