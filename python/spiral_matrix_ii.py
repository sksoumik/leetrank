# https://leetcode.com/problems/spiral-matrix-ii

# Given a positive integer n, generate an n x n matrix filled with elements from 1 to n2 in spiral order.

# Input: n = 3
# Output: [[1,2,3],[8,9,4],[7,6,5]]

from typing import List


class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        # Start with the empty matrix,
        # add the numbers in reverse order until we added the number 1.
        # Always rotate the matrix clockwise and add a top row:

        matrix = [[n * n]]
        low = n * n
        while low > 1:
            low = low - len(matrix)
            high = low
            matrix = [[i for i in range(low, high)]] + [
                list(j) for j in zip(*matrix[::-1])
            ]
        return matrix


if __name__ == "__main__":
    sol = Solution()
    n = 3
    print(sol.generateMatrix(n))
