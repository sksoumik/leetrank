# https://leetcode.com/problems/valid-palindrome

import re


class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        s = re.sub(r"[^a-zA-Z0-9]", "", s)
        return s == s[::-1]


if __name__ == "__main__":
    sol = Solution()
    s = "A man, a plan, a canal: Panama"
    print(sol.isPalindrome(s))
    s = "race a car"
    print(sol.isPalindrome(s))
