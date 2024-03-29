# https://leetcode.com/problems/palindrome-partitioning

# Given a string s, partition s such that every substring of the partition is a palindrome.
# Return all possible palindrome partitioning of s.

# A palindrome string is a string that reads the same backward as forward.


# Example 1:

# Input: s = "aab"
# Output: [["a","a","b"],["aa","b"]]

# vid: https://youtu.be/xhEEpnn0x1U

from typing import List
from functools import lru_cache


class Solution:
    def partition(self, s: str) -> List[List[str]]:

        n = len(s)
        output = []

        def dfs(start: int, sofar: List):
            # base case
            if start == n:
                output.append(sofar)
                return

            for i in range(start, n):
                # check for palindromes
                if s[start : i + 1] == s[start : i + 1][::-1]:
                    dfs(i + 1, sofar + [s[start : i + 1]])

        dfs(0, [])
        return output

    # using lru_cache
    def _partition(self, s: str) -> List[List[str]]:
        # use tuple instead of list
        n = len(s)
        output = []

        @lru_cache(None)
        def dfs(start: int, sofar: tuple):
            # base case
            if start == n:
                output.append(sofar)
                return

            for i in range(start, n):
                # check for palindromes
                if s[start : i + 1] == s[start : i + 1][::-1]:
                    dfs(i + 1, sofar + (s[start : i + 1],))

        dfs(0, ())
        return output


if __name__ == "__main__":
    s = "aab"
    print(Solution().partition(s))  # [['a', 'a', 'b'], ['aa', 'b']]
