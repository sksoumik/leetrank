# https://leetcode.com/problems/interleaving-string

# Given strings s1, s2, and s3, find whether s3 is formed by an interleaving of s1 and s2.

# An interleaving of two strings s and t is a configuration where s and t
# are divided into n and m non-empty substrings respectively, such that:

# s = s1 + s2 + ... + sn
# t = t1 + t2 + ... + tm
# |n - m| <= 1
# The interleaving is s1 + t1 + s2 + t2 + s3 + t3 + ... or t1 + s1 + t2 + s2 + t3 + s3 + ...
# Note: a + b is the concatenation of strings a and b.

# vid: https://youtu.be/oRYUnwklC98

from functools import lru_cache


class Solution:
    # time complexity: len(s1) * len(s2)
    # space complexity: len(s1) * len(s2)
    def isInterleave(self, s1, s2, s3):
        L1, L2, L3 = len(s1), len(s2), len(s3)

        if L1 + L2 != L3:
            return False

        @lru_cache(None)
        def recursion(i, j, k):
            # base case
            if i == L1 and j == L2 and k == L3:
                return True

            r1, r2 = False, False

            if i < L1 and s1[i] == s3[k]:
                r1 = recursion(i + 1, j, k + 1)

            if j < L2 and s2[j] == s3[k]:
                r2 = recursion(i, j + 1, k + 1)

            return r1 or r2

        return recursion(0, 0, 0)


if __name__ == "__main__":
    s = Solution()
    print(s.isInterleave("aabcc", "dbbca", "aadbbcbcac"))
    print(s.isInterleave("aabcc", "dbbca", "aadbbbaccc"))
