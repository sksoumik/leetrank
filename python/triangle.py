# https://leetcode.com/problems/triangle


# Given a triangle array, return the minimum path sum from top to bottom.
# For each step, you may move to an adjacent number of the row below.
# More formally, if you are on index i on the current row, you may move
# to either index i or index i + 1 on the next row.


# Example 1:
# Input: triangle = [[2],[3,4],[6,5,7],[4,1,8,3]]
# Output: 11
# Explanation: The triangle looks like:
#    2
#   3 4
#  6 5 7
# 4 1 8 3
# The minimum path sum from top to bottom is 2 + 3 + 5 + 1 = 11 (underlined above).

# Example 2:
# Input: triangle = [[-10]]
# Output: -10

from functools import lru_cache
from typing import List


class Solution:
    # Let dp(i, j) be the answer to the question: what is the minimum length of path,
    # ending in i-th line and j-th element of this line. Then we can have two options:

    # 1. If we reached the last line, we do not have options to go next, so we just return triangle[i][j].
    # 2. If we did not reached the last line, we can go either to (i + 1, j) or
    # to (i +1, j + 1), so we choose the minumum of two this values.

    # Time and Space complexity: O(n^2), where n is the number of lines in the triangle.
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        @lru_cache(None)
        def dp(i, j):
            if i == len(triangle) - 1:
                return triangle[i][j]

            else:
                return min(dp(i + 1, j), dp(i + 1, j + 1)) + triangle[i][j]

        return dp(0, 0)

    # iterative programming; time complexity O(n^2), space complexity O(1)
    def _minimumTotal(self, triangle: List[List[int]]) -> int:
        row = len(triangle)

        # bottom-up approach
        # row - 2 because we don't need to do anything for the last row
        for r in range(row - 2, -1, -1):
            for c in range(r + 1):
                triangle[r][c] += min(triangle[r + 1][c], triangle[r + 1][c + 1])

        # as this is a bottom-up approach, the first element is the minimum path sum
        return triangle[0][0]


if __name__ == "__main__":
    triangle = [[2], [3, 4], [6, 5, 7], [4, 1, 8, 3]]
    print(Solution().minimumTotal(triangle))  # 11

    triangle = [[-10]]
    print(Solution().minimumTotal(triangle))  # -10

    triangle = [[2], [3, 4], [6, 5, 7], [4, 1, 8, 3]]
    print(Solution()._minimumTotal(triangle))  # 11
