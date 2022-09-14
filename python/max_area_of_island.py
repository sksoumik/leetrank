# https://leetcode.com/problems/max-area-of-island

# You are given an m x n binary matrix grid. An island is a 
# group of 1's (representing land) connected 4-directionally (horizontal or vertical.) 
# You may assume all four edges of the grid are surrounded by water.
# The area of an island is the number of cells with a value 1 in the island.
# Return the maximum area of an island in grid. If there is no island, return 0.


from typing import List


class Solution:
    # video explanation: https://youtu.be/ZixJexAaOAk?t=474
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        # number of rows
        rows = len(grid)
        # number of cols
        cols = len(grid[0])

        count = 0

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1:
                    count = max(count, self.dfs(i, j, rows, cols, grid))
        return count
    

    def dfs(self, i, j, rows, cols, grid):
        # This is checking if the current index is out of bounds or if the current index is not a 1.
        if i >= rows or i < 0 or j >= cols or j < 0 or grid[i][j] == 0:
            return 0

        # Use # that modifies the input to ensure that the count isn't incremented where we could accidentally
        # traverse the same '1' cell multiple times and get into an infinite loop within an island
        # it's basically a implicit way of marking the visited square/nodes instead of putting the
        # visited nodes in an visited array
        grid[i][j] = 0

        # top
        top = self.dfs(i, j + 1, rows, cols, grid)
        # bottom
        down = self.dfs(i, j - 1, rows, cols, grid)
        # left
        left = self.dfs(i - 1, j, rows, cols, grid)
        # right
        right = self.dfs(i + 1, j, rows, cols, grid)

        return top + down + left + right + 1

    


if __name__ == "__main__":
    grid = [
        [0,0,1,0,0,0,0,1,0,0,0,0,0],
        [0,0,0,0,0,0,0,1,1,1,0,0,0],
        [0,1,1,0,1,0,0,0,0,0,0,0,0],
        [0,1,0,0,1,1,0,0,1,0,1,0,0],
        [0,1,0,0,1,1,0,0,1,1,1,0,0],
        [0,0,0,0,0,0,0,0,0,0,1,0,0],
        [0,0,0,0,0,0,0,1,1,1,0,0,0],
        [0,0,0,0,0,0,0,1,1,0,0,0,0]]

    print(Solution().maxAreaOfIsland(grid))
        