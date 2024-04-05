# https://leetcode.com/problems/combination-sum-iv

# Given an array of distinct integers nums and a target integer target, return the number of
# possible combinations that add up to target.
# The test cases are generated so that the answer can fit in a 32-bit integer.


# Example 1:

# Input: nums = [1,2,3], target = 4
# Output: 7
# Explanation:
# The possible combination ways are:
# (1, 1, 1, 1)
# (1, 1, 2)
# (1, 2, 1)
# (1, 3)
# (2, 1, 1)
# (2, 2)
# (3, 1)

from typing import List


class Solution:
    # video explanation: https://youtu.be/dw2nMCxG0ik
    # bottom-up dp
    def combinationSum4(self, nums: List[int], target: int) -> int:
        dp = {0: 1}
        for i in range(1, target + 1):
            dp[i] = sum(dp.get(i - num, 0) for num in nums)
        return dp[target]

    # naive recursive solution
    # time limit exceeded
    def combinationSum4_recursive(self, nums: List[int], target: int) -> int:
        if target == 0:
            return 1

        result = 0
        for num in nums:
            if num <= target:
                result += self.combinationSum4_recursive(nums, target - num)
        return result


if __name__ == "__main__":
    nums = [1, 2, 3]
    target = 4
    sol = Solution()
    print(sol.combinationSum4(nums, target))
    print(sol.combinationSum4_recursive(nums, target))
