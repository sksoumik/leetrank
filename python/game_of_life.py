# https://leetcode.com/problems/game-of-life/

# According to Wikipedia's article: "The Game of Life, also known simply as Life,
# is a cellular automaton devised by the British mathematician John Horton Conway in 1970."

# The board is made up of an m x n grid of cells, where each cell has an initial state:
# live (represented by a 1) or dead (represented by a 0). Each cell interacts with
# its eight neighbors (horizontal, vertical, diagonal) using the following four rules
# (taken from the above Wikipedia article):

# Any live cell with fewer than two live neighbors dies as if caused by under-population.
# Any live cell with two or three live neighbors lives on to the next generation.
# Any live cell with more than three live neighbors dies, as if by over-population.
# Any dead cell with exactly three live neighbors becomes a live cell, as if by reproduction.


# The next state is created by applying the above rules simultaneously to every cell in the current state,
# where births and deaths occur simultaneously. Given the current state of the m x n grid board, return the next state.


# Example 1:
# Input: board = [[0,1,0],[0,0,1],[1,1,1],[0,0,0]]
# Output: [[0,0,0],[1,0,1],[0,1,1],[0,1,0]]


# Example 2:
# Input: board = [[1,1],[1,0]]
# Output: [[1,1],[1,1]]

from typing import List


class Solution:
    # solution one, not caring about space complexity
    def gameOfLife(self, board: List[List[int]]) -> None:
        row, col = len(board), len(board[0])
        temp = [[0] * col for _ in range(row)]

        def helper(r, c):
            # live: 1, dies: 0

            # count live(1) neighbors
            count = 0
            for i in range(r - 1, r + 2):
                for j in range(c - 1, c + 2):
                    if i == r and j == c:
                        continue
                    if 0 <= i < row and 0 <= j < col and board[i][j] == 1:
                        count += 1

            # Any live cell with fewer than two live neighbors dies as if caused by under-population.
            if board[r][c] == 1 and count < 2:
                # then it dies
                temp[r][c] = 0
            # Any live cell with two or three live neighbors lives on to the next generation.
            elif board[r][c] == 1 and (count == 2 or count == 3):
                # then it lives
                temp[r][c] = 1
            # Any live cell with more than three live neighbors dies, as if by over-population.
            elif board[r][c] == 1 and count > 3:
                # then it dies
                temp[r][c] = 0
            # Any dead cell with exactly three live neighbors becomes a live cell, as if by reproduction.
            elif board[r][c] == 0 and count == 3:
                # then it becomes a live cell
                temp[r][c] = 1
            else:
                temp[r][c] = 0

        for r in range(row):
            for c in range(col):
                helper(r, c)

        for r in range(row):
            for c in range(col):
                board[r][c] = temp[r][c]

        # print(board)


if __name__ == "__main__":
    board = [[0, 1, 0], [0, 0, 1], [1, 1, 1], [0, 0, 0]]
    Solution().gameOfLife(board)
    print(board)

    board = [[1, 1], [1, 0]]
    Solution().gameOfLife(board)
    print(board)
