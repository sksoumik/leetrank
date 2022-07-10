# https://leetcode.com/problems/implement-strstr/

# Implement strStr().

# Given two strings needle and haystack, return the index of the first occurrence of needle in haystack,
# or -1 if needle is not part of haystack.


class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if needle in haystack:
            return haystack.index(needle)
        else:
            return -1


if __name__ == "__main__":
    sol = Solution()
    print(sol.strStr("hello", "ll"))
    print(sol.strStr("aaaaa", "bba"))
    print(sol.strStr("aaaaa", "aaaa"))
    print(sol.strStr("aaaaa", "aaa"))
