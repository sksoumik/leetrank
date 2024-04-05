# https://leetcode.com/problems/valid-sudoku

# Determine if a 9 x 9 Sudoku board is valid. Only the filled cells need to be validated according to the following rules:

# Each row must contain the digits 1-9 without repetition.
# Each column must contain the digits 1-9 without repetition.
# Each of the nine 3 x 3 sub-boxes of the grid must contain the digits 1-9 without repetition.
from typing import List


class Solution:
    # time complexity: O(n^2)
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        """
        [["5","3",".",".","7",".",".",".","."]
        ,["6",".",".","1","9","5",".",".","."]
        ,[".","9","8",".",".",".",".","6","."]
        ,["8",".",".",".","6",".",".",".","3"]
        ,["4",".",".","8",".","3",".",".","1"]
        ,["7",".",".",".","2",".",".",".","6"]
        ,[".","6",".",".",".",".","2","8","."]
        ,[".",".",".","4","1","9",".",".","5"]
        ,[".",".",".",".","8",".",".","7","9"]]

        """
        # rows as line
        for row in board:
            if not self.isValid(row):
                return False

        # cols as a line
        for col in zip(*board):
            if not self.isValid(list(col)):
                return False

        # 3*3 grid as line

        for i in range(0, 9, 3):
            for j in range(0, 9, 3):
                sub_boxes = []

                for k in range(3):
                    for l in range(3):
                        sub_boxes.append(board[i + k][j + l])

                if not self.isValid(sub_boxes):
                    return False
        return True

    def isValid(self, line):
        # line = [i for i in line if i != "."]
        line = list(filter(lambda x: x != ".", line))

        if len(line) != len(set(line)):
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
