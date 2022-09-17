# https://leetcode.com/problems/edit_distance

# Given two strings word1 and word2, return the minimum number of operations required to convert word1 to word2.

# You have the following three operations permitted on a word:

# Insert a character
# Delete a character
# Replace a character


# Example 1:
# Input: word1 = "horse", word2 = "ros"
# Output: 3
# Explanation:
# horse -> rorse (replace 'h' with 'r')
# rorse -> rose (remove 'r')
# rose -> ros (remove 'e')


from functools import lru_cache


class Solution:
    # recursive approach
    # time complexity: O(3^n)
    # video explanation: https://youtu.be/We3YDTzNXEk
    @lru_cache(maxsize=None)
    def minDistance(self, word1: str, word2: str) -> int:
        if not word1:
            return len(word2)
        if not word2:
            return len(word1)

        # if they are same on 2D grid, we just get the diagonal value from the 2D grid
        if word1[0] == word2[0]:
            return self.minDistance(word1[1:], word2[1:])

        return 1 + min(
            # previous row
            self.minDistance(word1[1:], word2),
            # previous column
            self.minDistance(word1, word2[1:]),
            # diagonal
            self.minDistance(word1[1:], word2[1:]),
        )

    # dynamic programming approach
    # time complexity: O(m * n)
    # space complexity: O(m * n)
    def _minDistance(self, word1: str, word2: str) -> int:
        m = len(word1)
        n = len(word2)

        # create a 2D array of size (m + 1) * (n + 1)
        dp = [[0] * (n + 1) for _ in range(m + 1)]

        for i in range(m + 1):
            for j in range(n + 1):
                # if word1 is empty, insert all characters of word2
                if i == 0:
                    dp[i][j] = j
                # if word2 is empty, remove all characters of word1
                elif j == 0:
                    dp[i][j] = i
                # if the characters are same
                elif word1[i - 1] == word2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1]
                # if the characters are different
                # get min(previous row, previous column and diagonal) + 1
                else:
                    dp[i][j] = 1 + min(dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1])

        return dp[m][n]


if __name__ == "__main__":
    sol = Solution()
    print(sol.minDistance("horse", "ros"))
    print(sol._minDistance("horse", "ros"))
