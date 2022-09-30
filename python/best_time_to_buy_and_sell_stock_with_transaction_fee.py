# https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-transaction-fee

# You are given an array prices where prices[i] is the price of a given 
# stock on the ith day, and an integer fee representing a transaction fee.
# Find the maximum profit you can achieve. You may complete as many 
# transactions as you like, but you need to pay the transaction fee for each transaction.
# Note: You may not engage in multiple transactions simultaneously 
# (i.e., you must sell the stock before you buy again).
 

# Example 1:
# Input: prices = [1,3,2,8,4,9], fee = 2
# Output: 8
# Explanation: The maximum profit can be achieved by:
# - Buying at prices[0] = 1
# - Selling at prices[3] = 8
# - Buying at prices[4] = 4
# - Selling at prices[5] = 9
# The total profit is ((8 - 1) - 2) + ((9 - 4) - 2) = 8.


# Example 2:
# Input: prices = [1,3,7,5,10,3], fee = 3
# Output: 6

from typing import List
from functools import lru_cache

class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        @lru_cache(None)
        def recursion(time, stock):

            if time >= len(prices):
                return 0

            buy = -prices[time] + recursion(time + 1, stock + 1) if stock == 0 else float("-inf")
            sell = prices[time] - fee + recursion(time + 1, stock - 1) if stock == 1 else float("-inf")
            hold = 0 + recursion(time + 1, stock)

            return max(buy, sell, hold)

        return recursion(0, 0)


if __name__ == "__main__":
    prices = [1,3,2,8,4,9]
    fee = 2
    print(Solution().maxProfit(prices, fee))

    prices = [1,3,7,5,10,3]
    fee = 3
    print(Solution().maxProfit(prices, fee))