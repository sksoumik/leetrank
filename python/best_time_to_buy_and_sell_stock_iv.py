# https://leetcode.com/problems/best-time-to-buy-and-sell-stock-iv

# You are given an integer array prices where prices[i] is the price of a given stock on the ith day, and an integer k.

# Find the maximum profit you can achieve. You may complete at most k transactions.
# Note: You may not engage in multiple transactions simultaneously (i.e., you must sell the stock before you buy again).


# Example 1:
# Input: k = 2, prices = [2,4,1]
# Output: 2
# Explanation: Buy on day 1 (price = 2) and sell on day 2 (price = 4), profit = 4-2 = 2.

from functools import lru_cache
from typing import List


class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        @lru_cache(None)
        def recursion(time, stock, count):

            if count >= k:
                return 0
            if time >= len(prices):
                return 0

            buy = (
                -prices[time] + recursion(time + 1, stock + 1, count)
                if stock == 0
                else float("-inf")
            )
            sell = (
                prices[time] + recursion(time + 1, stock - 1, count + 1)
                if stock == 1
                else float("-inf")
            )
            hold = 0 + recursion(time + 1, stock, count)

            return max(buy, sell, hold)

        return recursion(0, 0, 0)


if __name__ == "__main__":
    k = 2
    prices = [2, 4, 1]
    print(Solution().maxProfit(k, prices))
