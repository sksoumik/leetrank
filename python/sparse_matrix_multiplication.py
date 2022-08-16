# https://leetcode.com/problems/sparse-matrix-multiplication
# leetcode premium problem

# Given two sparse matrices A and B, return the result of AB.

# You may assume that A's column number is equal to B's row number.

# Example:

# A = [
#   [ 1, 0, 0],
#   [-1, 0, 3]
# ]

# B = [
#   [ 7, 0, 0 ],
#   [ 0, 0, 0 ],
#   [ 0, 0, 1 ]
# ]


#      |  1 0 0 |   | 7 0 0 |   |  7 0 0 |
# AB = | -1 0 3 | x | 0 0 0 | = | -7 0 3 |
#                   | 0 0 1 |


from typing import List


class Solution:
    def multiply(self, A: List[List[int]], B: List[List[int]]) -> List[List[int]]:
        rowsA, colsA = len(A), len(A[0])
        rowsB, colsB = len(B), len(B[0])
        if colsA != rowsB:
            return []
        # Creating a matrix of zeros with the dimensions of rowsA and colsB.
        C = [[0 for _ in range(colsB)] for _ in range(rowsA)]

        # A naive approach to matrix multiplication.
        for i in range(rowsA):
            for j in range(colsB):
                for k in range(colsA):
                    C[i][j] += A[i][k] * B[k][j]
        return C


if __name__ == "__main__":
    A = [[1, 0, 0], [-1, 0, 3]]
    B = [[7, 0, 0], [0, 0, 0], [0, 0, 1]]
    sol = Solution()
    print(sol.multiply(A, B))
