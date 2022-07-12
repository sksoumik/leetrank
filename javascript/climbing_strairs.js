// https://leetcode.com/problems/climbing-stairs

// You are climbing a staircase. It takes n steps to reach the top.
// Each time you can either climb 1 or 2 steps. In how many distinct
// ways can you climb to the top?

// Input: n = 2
// Output: 2
// Explanation: There are two ways to climb to the top.
// 1. 1 step + 1 step
// 2. 2 steps

/**
 * @param {number} n
 * @return {number}
 */

// dynamic programming solution
var climbStairs = function (n) {
  let table = [0, 1, 2];

  for (let i = 3; i <= n; i++) {
    table[i] = table[i - 1] + table[i - 2];
  }

  return table[n];
};

console.log(climbStairs(2));
