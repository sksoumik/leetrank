# https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-cooldown

# You are given an array prices where prices[i] is the price of a given stock on the ith day.
# Find the maximum profit you can achieve.


# You may complete as many transactions
# as you like (i.e., buy one and sell one share of the stock multiple times) with the following restrictions:
# After you sell your stock, you cannot buy stock on the next day
# (i.e., cooldown one day).
# Note: You may not engage in multiple transactions simultaneously
# (i.e., you must sell the stock before you buy again

# Example 1:
# Input: prices = [1,2,3,0,2]
# Output: 3
# Explanation: transactions = [buy, sell, cooldown, buy, sell]


from functools import lru_cache
from typing import List

# vid: https://youtu.be/ymE9E-cDYOI


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        @lru_cache(None)
        def recursion(time, stock):
            if time >= len(prices):
                return 0

            buy = (
                -prices[time] + recursion(time + 1, stock + 1)
                if stock == 0
                else float("-inf")
            )
            sell = (
                prices[time] + recursion(time + 2, stock - 1)
                if stock == 1
                else float("-inf")
            )
            hold = 0 + recursion(time + 1, stock)

            return max(buy, sell, hold)

        return recursion(0, 0)


if __name__ == "__main__":
    prices = [1, 2, 3, 0, 2]
    print(Solution().maxProfit(prices))
