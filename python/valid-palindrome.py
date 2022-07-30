# https://leetcode.com/problems/valid-palindrome

# A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and
# removing all non-alphanumeric characters, it reads the same forward and backward. Alphanumeric
# characters include letters and numbers.

# Given a string s, return true if it is a palindrome, or false otherwise.

import re


class Solution:
    # solution 1
    def isPalindrome_1(self, s: str) -> bool:
        s = s.lower()
        # remove all non alphanumeric characters
        s = re.sub(r"[^a-zA-Z0-9]", "", s)
        return s == s[::-1]

    # solution 2
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        # remove all non alphanumeric characters using isalnum()
        s = [c for c in s if c.isalnum()]
        return s == s[::-1]


if __name__ == "__main__":
    sol = Solution()
    s = "A man, a plan, a canal: Panama"
    print(sol.isPalindrome(s))
    s = "race a car"
    print(sol.isPalindrome(s))
