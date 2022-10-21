# https://leetcode.com/problems/word-search

# Given an m x n grid of characters board and a string word, return true if word exists in the grid.

# The word can be constructed from letters of sequentially adjacent cells, where adjacent cells are horizontally
# or vertically neighboring. The same letter cell may not be used more than once.

# Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCCED"
# Output: true

# Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "SEE"
# Output: true

# Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCB"
# Output: false

from importlib.resources import path
from typing import List


class Solution:
    # time complexity: O(m * n * 4^w)
    # where m * n is the dimension of the board and w is the length of the word
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows = len(board)
        cols = len(board[0])
        path = set()

        # @lru_cache(None)
        def dfs(r, c, w):
            if w == len(word):
                return True
            if (
                r < 0
                or r >= rows
                or c < 0
                or c >= cols
                or (r, c) in path
                or word[w] != board[r][c]
            ):
                return False

            path.add((r, c))

            res = (
                dfs(r + 1, c, w + 1)
                or dfs(r - 1, c, w + 1)
                or dfs(r, c + 1, w + 1)
                or dfs(r, c - 1, w + 1)
            )

            path.remove((r, c))
            return res

        for r in range(rows):
            for c in range(cols):
                if dfs(r, c, 0):
                    return True
        return False


if __name__ == "__main__":
    board = [["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]]
    word = "ABCCED"
    print(Solution().exist(board, word))  # True
