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

        # we can do this using recursive approach
        # we can do this using iterative approach

        # recursive approach
        return matrix and list(matrix.pop(0)) + self.spiralOrder([*zip(*matrix)][::-1])

        # iterative approach
        # result = []

        # while matrix:
        #     result.extend(matrix.pop(0))
        #     matrix = [*zip(*matrix)][::-1]
        # return result


if __name__ == "__main__":
    sol = Solution()
    matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    print(sol.spiralOrder(matrix))
