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


class Solution:
    # solution 1: O(n) time
    def maxProfit(self, prices: List[int]) -> int:
        """
        We keep track of the minimum price we've seen so far and the maximum profit we've seen so far.
        We update the minimum price and maximum profit as we iterate through the array.

        :param prices: the list of prices
        :return: The maximum profit that could be made by buying and selling a single share at the given
        prices.
        """
        max_profit = 0
        min_price_seen_so_far = float("inf") # float('inf') denotes an infinitly large number

        for current_price in prices:
            min_price_seen_so_far = min(min_price_seen_so_far, current_price)
            profit_if_sold_now = current_price - min_price_seen_so_far
            max_profit = max(max_profit, profit_if_sold_now)

        return max_profit

    # solution 2: dynamic programming
    def maxProfit_2(self, prices: List[int]) -> int:
        dp = [0] * len(prices)
        min_price = prices[0]

        for i in range(1, len(prices)):
            min_price = min(min_price, prices[i])
            dp[i] = max(dp[i - 1], prices[i] - min_price)

        return dp[-1]

        


if __name__ == "__main__":
    prices = [7, 1, 5, 3, 6, 4]
    print(Solution().maxProfit(prices))
    prices = [1, 2, 3, 4, 5]
    print(Solution().maxProfit(prices))
    prices = [7, 6, 4, 3, 1]
    print(Solution().maxProfit(prices))
