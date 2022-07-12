// https://leetcode.com/problems/best-time-to-buy-and-sell-stock/

// You are given an array prices where prices[i] is the price of a given stock on the ith day.
// You want to maximize your profit by choosing a single day to buy one stock and choosing
// a different day in the future to sell that stock.
// Return the maximum profit you can achieve from this transaction. If you cannot
// achieve any profit, return 0.

// Input: prices = [7,1,5,3,6,4]
// Output: 5
// Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.

/**
 * @param {number[]} prices
 * @return {number}
 */
var maxProfit = function (prices) {
  max_profit = 0;

  buy = 0;
  sell = 1;
  while (sell < prices.length) {
    current_profit = prices[sell] - prices[buy];

    // if the sell > buy: update the max profit
    if (prices[sell] > prices[buy]) {
      max_profit = Math.max(max_profit, current_profit);
    } else {
      // if the sell < buy: update the buy
      buy = sell;
    }
    sell++;
  }
  return max_profit;
};

// console.log(maxProfit([7, 1, 5, 3, 6, 4]));
