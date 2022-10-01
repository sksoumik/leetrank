# https://leetcode.com/problems/best-time-to-buy-and-sell-stock/

# You are given an array prices where prices[i] is the price of a given stock on the ith day.

# You want to maximize your profit by choosing a single day to buy one stock and choosing
# a different day in the future to sell that stock.
# Return the maximum profit you can achieve from this transaction. If you cannot
# achieve any profit, return 0.


# Input: prices = [7,1,5,3,6,4]
# Output: 5
# Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.

from typing import List
from functools import lru_cache

# vid: https://youtu.be/ymE9E-cDYOI

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        @lru_cache(None)
        def recursion(time, stock, count):

            if count > k: return 0
            if time >= len(prices): return 0

            buy = -prices[time] + recursion(time + 1, stock + 1, count) if stock == 0 else float("-inf")
            sell = prices[time] + recursion(time + 1, stock - 1, count+1) if stock == 1 else float("-inf")
            hold = 0 + recursion(time + 1, stock, count)

            return max(buy, sell, hold)

        k = 1    
        return recursion(0, 0, 0)



if __name__ == "__main__":
    prices = [7, 1, 5, 3, 6, 4]
    print(Solution().maxProfit(prices))
    prices = [1, 2, 3, 4, 5]
    print(Solution().maxProfit(prices))
    prices = [7, 6, 4, 3, 1]
    print(Solution().maxProfit(prices))
