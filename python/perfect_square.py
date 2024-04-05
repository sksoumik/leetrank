# https://leetcode.com/problems/perfect-squares/

# Given an integer n, return the least number of perfect square numbers that sum to n.
# A perfect square is an integer that is the square of an integer; in other words,
#  it is the product of some integer with itself. For example, 1, 4, 9, and 16
# are perfect squares while 3 and 11 are not.


# Example 1:
# Input: n = 12
# Output: 3
# Explanation: 12 = 4 + 4 + 4.

# Example 2:
# Input: n = 13
# Output: 2
# Explanation: 13 = 4 + 9.

from functools import lru_cache


class Solution:

    # using dfs, time limit exceeded
    # time complexity O(n^2), space complexity O(n)
    def numSquares(self, n: int) -> int:
        # create all perfect square numbers less than n
        squares = []
        i = 1
        while i * i <= n:
            squares.append(i * i)
            i += 1

        result = []

        def dfs(current_combination, current_sum, idx):
            if current_sum == n:
                result.append(current_combination)
                return

            elif current_sum > n:
                return

            for i in range(idx, len(squares)):
                dfs(current_combination + [squares[i]], current_sum + squares[i], i)

        dfs([], 0, 0)

        if not result:
            return -1

        min_length_array = min(result, key=len)
        return len(min_length_array)

    # dynamic programming
    # time complexity: O(n * sqrt(n))
    def numSquaresDP(self, n):
        # we will store the results of the subproblems in the dp array
        # size is going to be 0 to n so, n+1
        dp = [n] * (n + 1)
        # base case, target value is 0, we need to return 0
        dp[0] = 0

        for target in range(1, n + 1):
            for s in range(1, target + 1):
                square = s * s
                if target - square < 0:
                    break

                dp[target] = min(dp[target], dp[target - square] + 1)
                # +1 because we need to include the number itself

        return dp[n]

    # using recursion, and lru_cache
    def _numSquares(self, n: int) -> int:
        squares = []
        i = 1
        while i * i <= n:
            squares.append(i * i)
            i += 1

        @lru_cache(None)
        def dp(n):
            if n == 0:
                return 0

            ans = float("inf")
            for square in squares:
                if n >= square:
                    ans = min(ans, dp(n - square) + 1)
            return ans

        ans = dp(n)

        return ans if ans != float("inf") else -1


if __name__ == "__main__":
    s = Solution()
    print(s.numSquares(12))
    print(s.numSquares(12))
    print(s.numSquares(13))
    print(s.numSquaresDP(13))
