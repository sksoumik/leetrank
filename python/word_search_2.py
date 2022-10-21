# https://leetcode.com/problems/word-search-ii/

# Given an m x n board of characters and a list of strings words, return all words on the board.

# Each word must be constructed from letters of sequentially adjacent cells,
# where adjacent cells are horizontally or
# vertically neighboring. The same letter cell may not be used more than once in a word.

# Input: board = [["o","a","a","n"],["e","t","a","e"],["i","h","k","r"],["i","f","l","v"]],
# words = ["oath","pea","eat","rain"]
# Output: ["eat","oath"]

from typing import List


class Solution:
    # GOT TLE
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        rows = len(board)
        cols = len(board[0])
        path = set()
        result = set()

        def dfs(r, c, w, word):
            if w == len(word):
                result.add(word)
                return
            if (
                r < 0
                or r >= rows
                or c < 0
                or c >= cols
                or (r, c) in path
                or word[w] != board[r][c]
            ):
                return

            path.add((r, c))

            dfs(r + 1, c, w + 1, word)
            dfs(r - 1, c, w + 1, word)
            dfs(r, c + 1, w + 1, word)
            dfs(r, c - 1, w + 1, word)

            path.remove((r, c))

        for r in range(rows):
            for c in range(cols):
                for word in words:
                    dfs(r, c, 0, word)
        return list(result)
