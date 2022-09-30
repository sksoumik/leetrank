# https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/

# You are given an integer array prices where prices[i] is the price
# of a given stock on the ith day.
# On each day, you may decide to buy and/or sell the stock.
# You can only hold at most one share of the stock at any time.
# However, you can buy it then immediately sell it on the same day.
# Find and return the maximum profit you can achieve.


# Example 1:
# Input: prices = [7,1,5,3,6,4]
# Output: 7
# Explanation: Buy on day 2 (price = 1) and sell on day 3 (price = 5), profit = 5-1 = 4.
# Then buy on day 4 (price = 3) and sell on day 5 (price = 6), profit = 6-3 = 3.
# Total profit is 4 + 3 = 7.

from typing import List
from functools import lru_cache

# vid: https://youtu.be/ymE9E-cDYOI

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        @lru_cache(None)
        def recursion(time, stock):

            if time >= len(prices):
                return 0

            buy = -prices[time] + recursion(time + 1, stock + 1) if stock == 0 else float("-inf")
            sell = prices[time] + recursion(time + 1, stock - 1) if stock == 1 else float("-inf")
            hold = 0 + recursion(time + 1, stock)

            return max(buy, sell, hold)

        return recursion(0, 0)


if __name__ == "__main__":
    prices = [7, 1, 5, 3, 6, 4]
    print(Solution().maxProfit(prices))
    prices = [1, 2, 3, 4, 5]
    print(Solution().maxProfit(prices))
    prices = [7, 6, 4, 3, 1]
    print(Solution().maxProfit(prices))
