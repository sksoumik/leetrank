# https://leetcode.com/problems/decode-ways/description/

# Given a string s containing only digits, return the number of ways to decode it.

# Input: s = "12"
# Output: 2
# Explanation: "12" could be decoded as "AB" (1 2) or "L" (12).

from functools import lru_cache


class Solution:
    def numDecodings(self, s: str) -> int:
        if len(s) == 0 or s is None:
            return 0

        @lru_cache(maxsize=None)
        def dfs(st):
            if len(st) == 0:
                return 1
            if st[0] == "0":
                return 0
            if len(st) == 1:
                return 1
            if int(st[:2]) <= 26:
                return dfs(st[1:]) + dfs(st[2:])
            else:
                return dfs(st[1:])

        return dfs(s)


if __name__ == "__main__":
    s = Solution()
    print(s.numDecodings("12"))
    print(s.numDecodings("226"))
    print(s.numDecodings("0"))
    print(s.numDecodings("06"))
