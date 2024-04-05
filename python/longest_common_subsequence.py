# https://leetcode.com/problems/longest-common-subsequence

# Given two strings text1 and text2, return the length of their longest common subsequence.
# If there is no common subsequence, return 0.
# A subsequence of a string is a new string generated from the original string
# with some characters (can be none) deleted without changing the relative order of the remaining characters.

# For example, "ace" is a subsequence of "abcde".
# A common subsequence of two strings is a subsequence that is common to both strings.


# Example 1:
# Input: text1 = "abcde", text2 = "ace"
# Output: 3
# Explanation: The longest common subsequence is "ace" and its length is 3.

# Example 2:
# Input: text1 = "abc", text2 = "abc"
# Output: 3
# Explanation: The longest common subsequence is "abc" and its length is 3.

from functools import lru_cache


class Solution:
    # recursive approach
    # time complexity: O(2^n)
    # video explanation: https://youtu.be/jHGgXV27qtk
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:

        @lru_cache(maxsize=None)
        def lcs_helper(i, j):
            if i == len(text1) or j == len(text2):
                return 0
            if text1[i] == text2[j]:
                return 1 + lcs_helper(i + 1, j + 1)
            return max(lcs_helper(i + 1, j), lcs_helper(i, j + 1))

        return lcs_helper(0, 0)

    # dynamic programming approach
    # time complexity: O(m * n)
    # space complexity: O(m * n)
    def _longestCommonSubsequence(self, text1: str, text2: str) -> int:
        # length of text1 and text2
        m = len(text1)
        n = len(text2)

        # create a 2D array of size (m + 1) * (n + 1)
        dp = [[0] * (n + 1) for _ in range(m + 1)]

        for i in range(m):
            for j in range(n):
                # if the characters are same
                if text1[i] == text2[j]:
                    dp[i + 1][j + 1] = 1 + dp[i][j]
                # if the characters are different
                else:
                    dp[i + 1][j + 1] = max(dp[i + 1][j], dp[i][j + 1])

        return dp[m][n]


if __name__ == "__main__":
    sol = Solution()
    print(sol.longestCommonSubsequence("abcde", "ace"))
    print(sol._longestCommonSubsequence("abcde", "ace"))
