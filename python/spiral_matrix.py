# https://leetcode.com/problems/spiral-matrix

# Given an m x n matrix, return all elements of the matrix in spiral order.

# Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
# Output: [1,2,3,6,9,8,7,4,5]

from typing import List


class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        # extract first row
        # rotate the matrix 90 degrees anticlockwise
        # extract first row again
        # rotate the matrix 90 degrees anticlockwise
        # extract first row again

        # recursive approach
        # return matrix and list(matrix.pop(0)) + self.spiralOrder([*zip(*matrix)][::-1])

        # iterative approach
        result = []

        while matrix:
            # extract first row
            result.extend(matrix.pop(0))
            # rotate the matrix 90 degrees anticlockwise
            matrix = [*zip(*matrix)][::-1]
        return result

    def _spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        result = []

        while matrix:
            # extract first row
            result.extend(matrix.pop(0))
            # rotate the matrix 90 degrees clockwise
            for i in range(len(matrix)):
                for j in range(i):
                    matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
            matrix.reverse()

        return result




if __name__ == "__main__":
    sol = Solution()
    matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    print(sol.spiralOrder(matrix))
