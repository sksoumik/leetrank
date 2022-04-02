# https://leetcode.com/problems/valid-palindrome-ii/

# Given a string s, return true if the s can be palindrome after deleting at most one character from it.


class Solution:
    def validPalindrome(self, s: str) -> bool:
        if len(s) <= 1:
            return True
        left = 0
        right = len(s) - 1
        while left < right:
            if s[left] != s[right]:
                return self.isPalindrome(s, left + 1, right) or self.isPalindrome(
                    s, left, right - 1
                )
            left += 1
            right -= 1
        return True

    def isPalindrome(self, s, left, right):
        while left < right:
            if s[left] != s[right]:
                return False
            left += 1
            right -= 1
        return True


if __name__ == "__main__":
    sol = Solution()
    print(sol.validPalindrome("aba"))
    print(sol.validPalindrome("abca"))
    print(sol.validPalindrome("abc"))
