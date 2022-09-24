# https://leetcode.com/problems/rotate-image/

# You are given an n x n 2D matrix representing an image, rotate the image by 90 degrees (clockwise).
# You have to rotate the image in-place, which means you have to modify the input 2D matrix directly.

# DO NOT allocate another 2D matrix and do the rotation.

from typing import List
import numpy as np

# matrix = np.array(matrix)
# print("Original matrix:")
# print(matrix)
# # clockwise rotate the matrix
# print("\nclockwise rotate")
# print(np.rot90(matrix, k=1, axes=(1, 0)))
# # counterclockwise rotate the matrix
# print("\ncounterclockwise rotate:")
# print(np.rot90(matrix, k=1, axes=(0, 1)))


class Solution:
    # accepted solution
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Reverse the matrix first, then swap the symmetric elements

        :param matrix: the matrix to be rotated
        :type matrix: List[List[int]]
        """
        # Do not return anything, modify matrix in-place instead.

        # clockwise rotate the matrix
        matrix.reverse()
        for i in range(len(matrix)):
            for j in range(i):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

        print(matrix)

    # second solution pythonic way
    def _rotate(self, matrix: List[List[int]]) -> None:
        # rotate the matrix by 90 degrees clockwise
        matrix[:] = zip(*matrix[::-1])

    # rotate the matrix by 90 degrees counterclockwise
    def _rotate(matrix):
        for i in range(len(matrix) - 1, -1, -1):
            for j in range(i):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
        matrix.reverse()


if __name__ == "__main__":
    matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    # Solution().rotate(matrix)

    m = [[1, 2, 3], [2, 3, 3], [5, 4, 3]]

    Solution().rotate_counterclockwise(matrix)
