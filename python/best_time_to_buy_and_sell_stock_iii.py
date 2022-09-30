# https://leetcode.com/problems/best-time-to-buy-and-sell-stock-iii

# You are given an array prices where prices[i] is the price of a given stock on the ith day.

# Find the maximum profit you can achieve. You may complete at most two transactions.
# Note: You may not engage in multiple transactions simultaneously 
# (i.e., you must sell the stock before you buy again).

 

# Example 1:
# Input: prices = [3,3,5,0,0,3,1,4]
# Output: 6
# Explanation: Buy on day 4 (price = 0) and sell on day 6 (price = 3), profit = 3-0 = 3.
# Then buy on day 7 (price = 1) and sell on day 8 (price = 4), profit = 4-1 = 3.

from typing import List
from functools import lru_cache


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        @lru_cache(None)
        def recursion(time, stock, count):
            if count >= k: return 0
            if time >= len(prices): return 0

            buy = -prices[time] + recursion(time + 1, stock + 1, count) if stock == 0 else float("-inf")
            sell = prices[time] + recursion(time + 1, stock - 1, count+1) if stock == 1 else float("-inf")
            hold = 0 + recursion(time + 1, stock, count)

            return max(buy, sell, hold)

        k = 2
        return recursion(0, 0, 0)