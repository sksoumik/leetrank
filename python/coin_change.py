# https://leetcode.com/problems/coin-change/

# You are given an integer array coins representing coins of different denominations
# and an integer amount representing a total amount of money.
# Return the fewest number of coins that you need to make up that amount.
# If that amount of money cannot be made up by any combination of the coins, return -1.
# You may assume that you have an infinite number of each kind of coin.

# Example 1:

# Input: coins = [1,2,5], amount = 11
# Output: 3
# Explanation: 11 = 5 + 5 + 1


# Example 2:
# Input: coins = [2], amount = 3
# Output: -1

# Example 3:
# Input: coins = [1], amount = 0
# Output: 0


from typing import List
import math
from functools import lru_cache


class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        @lru_cache(None)
        def dp(amount):
            if amount == 0:
                return 0

            ans = math.inf
            for coin in coins:
                if amount >= coin:
                    ans = min(ans, dp(amount - coin) + 1)
            return ans

        ans = dp(amount)
        return ans if ans != math.inf else -1

    # dfs
    def _coinChange(self, coins: List[int], amount: int) -> int:
        result = []
        # @lru_cache(None)
        def dfs(current_combination, current_sum, idx):
            if current_sum == amount:
                result.append(current_combination)
                return

            elif current_sum > amount:
                return

            for i in range(idx, len(coins)):
                dfs(current_combination + [coins[i]], current_sum + coins[i], i)

        dfs([], 0, 0)

        if not result:
            return -1

        min_length_array = min(result, key=len)

        return len(min_length_array)


if __name__ == "__main__":
    s = Solution()
    print(s.coinChange([1, 2, 5], 11))  # 3
    print(s.coinChange([2], 3))  # -1
    print(s.coinChange([1], 0))  # 0

    print(s._coinChange([1, 2, 5], 11))  # 3
