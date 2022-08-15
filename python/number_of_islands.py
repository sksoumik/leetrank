# https://leetcode.com/problems/number-of-islands

# Given an m x n 2D binary grid grid which represents a map of '1's (land) and '0's (water), return the number of islands.

# An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically.
# You may assume all four edges of the grid are all surrounded by water.

from typing import List


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows, cols = len(grid), len(grid[0])
        count = 0
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == "1":
                    self.dfs(i, j, rows, cols, grid)
                    # dfs returns true means we found a new island
                    count += 1
        return count

    def dfs(self, i, j, rows, cols, grid):
        """
        We are checking if the current index is out of bounds or if the current index is a 0. If it is,
        we return false.

        If it isn't, we mark the current index as visited and then recursively call the function on the
        four adjacent indices

        :param i: The current row index
        :param j: The current column index
        :param rows: The number of rows in the grid
        :param cols: The number of columns in the grid
        :param grid: This is the grid that we are given
        :return: The number of islands.
        """
        if i >= rows or i < 0 or j >= cols or j < 0 or grid[i][j] == "0":
            return False

        # Marking the current index as visited.
        grid[i][j] = "0"

        self.dfs(i, j + 1, rows, cols, grid)
        self.dfs(i + 1, j, rows, cols, grid)
        self.dfs(i, j - 1, rows, cols, grid)
        self.dfs(i - 1, j, rows, cols, grid)
        return True


if __name__ == "__main__":
    grid = [
        ["1", "1", "1", "1", "0"],
        ["1", "1", "0", "1", "0"],
        ["1", "1", "0", "0", "0"],
        ["0", "0", "0", "0", "0"],
    ]
    sol = Solution()
    print(sol.numIslands(grid))
