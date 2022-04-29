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
    def maxProfit(self, prices: List[int]) -> int:
        """
        We start with a left pointer at the beginning of the array and a right pointer at the second
        element. We then check to see if the element to the right is greater than the element to the
        left. If it is, we calculate the current profit and update our max profit if the current profit
        is greater. If the element to the right is not greater, we move the left pointer to the right by
        one. We then increment the right pointer by one. We repeat this process until the right pointer
        is at the end of the array

        :param prices: List[int] -> This is the list of prices that we are given
        :type prices: List[int]
        :return: The max profit that can be made from buying and selling a stock
        """
        max_profit = 0

        # left pointer, idx of buying the stock
        buy = 0

        # right pointer, index of selling the stock
        sell = 1

        while sell < len(prices):
            current_profit = prices[sell] - prices[buy]

            # if the buy < sell: then update max profit
            if prices[buy] < prices[sell]:
                max_profit = max(current_profit, max_profit)
            else:
                # update pointers
                buy = sell
            sell += 1

        return max_profit


if __name__ == "__main__":
    prices = [7, 1, 5, 3, 6, 4]
    print(Solution().maxProfit(prices))
    prices = [1, 2, 3, 4, 5]
    print(Solution().maxProfit(prices))
    prices = [7, 6, 4, 3, 1]
    print(Solution().maxProfit(prices))
