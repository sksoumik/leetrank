# https://leetcode.com/problems/valid-sudoku

# Determine if a 9 x 9 Sudoku board is valid. Only the filled cells need to be validated according to the following rules:

# Each row must contain the digits 1-9 without repetition.
# Each column must contain the digits 1-9 without repetition.
# Each of the nine 3 x 3 sub-boxes of the grid must contain the digits 1-9 without repetition.
from typing import List
import sys


class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # check row
        for row in board:
            if not self.isValidRow(row):
                return False
        # check column
        for i in range(9):
            column = [board[j][i] for j in range(9)]
            if not self.isValidRow(column):
                return False
        
        # check 3x3
        # Iterating through the 3x3 submatrices of the sudoku board.
        for i in range(0, 9, 3):
            for j in range(0, 9, 3):
                sub_matrix = [board[i + k][j + l] for k in range(3) for l in range(3)]
                # print(sub_matrix)
                if not self.isValidRow(sub_matrix):
                    return False
        return True

    def isValidRow(self, row: List[str]) -> bool:
        """
        It takes a row of a sudoku board, removes all the "."s, and checks if the length of the row is
        equal to the length of the set of the row
        
        :param row: List[str]
        :type row: List[str]
        :return: A boolean value
        """
        row = [i for i in row if i != "."]
        if len(row) != len(set(row)):
            return False
        return True


if __name__ == "__main__":

    board = [
        ["5", "3", ".", ".", "7", ".", ".", ".", "."],
        ["6", ".", ".", "1", "9", "5", ".", ".", "."],
        [".", "9", "8", ".", ".", ".", ".", "6", "."],
        ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
        ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
        ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
        [".", "6", ".", ".", ".", ".", "2", "8", "."],
        [".", ".", ".", "4", "1", "9", ".", ".", "5"],
        [".", ".", ".", ".", "8", ".", ".", "7", "9"],
    ]
    print(Solution().isValidSudoku(board))
