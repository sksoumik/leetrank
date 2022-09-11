# https://leetcode.com/problems/minimum-path-sum

# Given a m x n grid filled with non-negative numbers,
# find a path from top left to bottom right, which minimizes the sum of all numbers along its path.
# Note: You can only move either down or right at any point in time.


# Example 1:
# Input: grid = [[1,3,1],[1,5,1],[4,2,1]]
# Output: 7
# Explanation: Because the path 1 → 3 → 1 → 1 → 1 minimizes the sum.

from typing import List


class Solution:
    # iterative programming; time complexity O(m*n), space complexity O(1)
    # video explanation: https://youtu.be/hwRWt-PH394
    def minPathSum(self, grid: List[List[int]]) -> int:
        """
        We can move right/down, so we can only move from the left or from the top.
        """
        row = len(grid)
        col = len(grid[0])

        for r in range(row):
            for c in range(col):
                # if it's the first cell, then we don't need to do anything
                # if it's the first row, then we can only add the left value, cause there's nothing above
                # if it's the first column, then we can only add the top value, cause there's nothing left
                # else, add the minimum of the left and top value with the current value
                if r == 0 and c == 0:
                    continue
                elif r == 0:
                    grid[r][c] += grid[r][c - 1]
                elif c == 0:
                    grid[r][c] += grid[r - 1][c]
                else:
                    grid[r][c] += min(grid[r - 1][c], grid[r][c - 1])

        return grid[row - 1][col - 1]


if __name__ == "__main__":
    grid = [[1, 3, 1], [1, 5, 1], [4, 2, 1]]
    print(Solution().minPathSum(grid))
