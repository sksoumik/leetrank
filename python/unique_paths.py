# https://leetcode.com/problems/unique-paths/

# There is a robot on an m x n grid. The robot is initially located at the 
# top-left corner (i.e., grid[0][0]). The robot tries to move to the 
# bottom-right corner (i.e., grid[m - 1][n - 1]). 
# The robot can only move either down or right at any point in time.

# Given the two integers m and n, return the number of 
# possible unique paths that the robot can take to reach the bottom-right corner.

# The test cases are generated so that the answer will be less than or equal to 2 * 109.


# Input: m = 3, n = 2
# Output: 3
# Explanation: From the top-left corner, there are a total of 3 ways to reach the bottom-right corner:
# 1. Right -> Down -> Down
# 2. Down -> Down -> Right
# 3. Down -> Right -> Down



class Solution:
    # time complexity: O(m*n)
    # space complexity: O(m*n)
    def uniquePaths(self, m: int, n: int) -> int:
        # Initialize a 2D array to store the number of paths to reach each cell
        # The array is initialized to 0
        path_count = [[0] * n for _ in range(m)]
        
        # There is only 1 way to reach the first cell
        path_count[0][0] = 1
        
        # Iterate through each cell in the grid
        for i in range(m):
            for j in range(n):
                # If we are not in the first row or column, the number of ways
                # to reach this cell is the sum of the number of ways to reach
                # the cell above and the cell to the left
                if i > 0 and j > 0:
                    path_count[i][j] = path_count[i-1][j] + path_count[i][j-1]
                # If we are in the first row, the number of ways to reach this cell
                # is the number of ways to reach the cell to the left
                elif i == 0 and j > 0:
                    path_count[i][j] = path_count[i][j-1]
                # If we are in the first column, the number of ways to reach this cell
                # is the number of ways to reach the cell above
                elif i > 0 and j == 0:
                    path_count[i][j] = path_count[i-1][j]
        
        # Return the number of ways to reach the bottom-right cell
        return path_count[m-1][n-1]


if __name__ == '__main__':
    # Test the solution
    m = 3
    n = 2
    print(Solution().uniquePaths(m, n))  # Output: 3

    m = 7
    n = 3
    print(Solution().uniquePaths(m, n))  # Output: 28

    m = 3
    n = 3
    print(Solution().uniquePaths(m, n))  # Output: 6

    m = 51
    n = 9
    print(Solution().uniquePaths(m, n))  # Output: 1916797311

