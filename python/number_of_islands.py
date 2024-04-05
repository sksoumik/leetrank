# https://leetcode.com/problems/number-of-islands

# Given an m x n 2D binary grid grid which represents a map of '1's (land) and '0's (water), return the number of islands.

# An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically.
# You may assume all four edges of the grid are all surrounded by water.

from typing import List


class Solution:
    # video explanation: https://youtu.be/ZixJexAaOAk?t=474
    def numIslands(self, grid: List[List[str]]) -> int:

        # number of rows
        rows = len(grid)
        # number of cols
        cols = len(grid[0])

        count = 0

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == "1":
                    self.dfs(i, j, rows, cols, grid)
                    count += 1
        return count

    def dfs(self, i, j, rows, cols, grid):
        # This is checking if the current index is out of bounds or if the current index is not a 1.
        if i >= rows or i < 0 or j >= cols or j < 0 or grid[i][j] == "0":
            return 0

        # Use # that modifies the input to ensure that the count isn't incremented where we could accidentally
        # traverse the same '1' cell multiple times and get into an infinite loop within an island
        # it's basically a implicit way of marking the visited square/nodes instead of putting the
        # visited nodes in an visited array
        grid[i][j] = "0"

        # top
        self.dfs(i, j + 1, rows, cols, grid)
        # bottom
        self.dfs(i, j - 1, rows, cols, grid)
        # left
        self.dfs(i - 1, j, rows, cols, grid)
        # right
        self.dfs(i + 1, j, rows, cols, grid)


if __name__ == "__main__":
    grid = [
        ["1", "1", "1", "1", "0"],
        ["1", "1", "0", "1", "0"],
        ["1", "1", "0", "0", "0"],
        ["0", "0", "0", "0", "0"],
    ]
    sol = Solution()
    print(sol.numIslands(grid))

    grid = [
        ["1", "1", "0", "0", "0"],
        ["1", "1", "0", "0", "0"],
        ["0", "0", "1", "0", "0"],
        ["0", "0", "0", "1", "1"],
    ]
    sol = Solution()
    print(sol.numIslands(grid))
