# https://leetcode.com/problems/longest-palindromic-substring

# Given a string s, return the longest palindromic substring in s.

# Example 1:

# Input: s = "babad"
# Output: "bab"
# Explanation: "aba" is also a valid answer.

from itertools import combinations

class Solution:
    # video explanation: https://youtu.be/XYQecbcd6_c
    def longestPalindrome(self, s: str) -> str:
        longest_palindrome = ""
        longest_palindrome_length = 0

        for i in range(len(s)):
            # odd length
            odd_len_palindrome = self.find_palindrome(s, i, i)
            if len(odd_len_palindrome) > longest_palindrome_length:
                longest_palindrome = odd_len_palindrome
                longest_palindrome_length = len(odd_len_palindrome)
            # even length
            even_len_palindrome = self.find_palindrome(s, i, i+1)
            if len(even_len_palindrome) > longest_palindrome_length:
                longest_palindrome = even_len_palindrome
                longest_palindrome_length = len(even_len_palindrome)
        return longest_palindrome

    def find_palindrome(self, s, i, j):
        while i >= 0 and j < len(s) and s[i] == s[j]:
            i -= 1
            j += 1
        return s[i+1:j]


    # time limit exceeds: O(n^3)
    def longestPalindrome_2(self, s: str) -> str:
        if len(s) == 0:
            return ""
        if len(s) == 1:
            return s
        # make all possible combinations of substring
        # all_substrings = [''.join(l) for i in range(len(s)) for l in combinations(s, i+1)]
        all_substrings = []
        for i in range(len(s)):
            for j in combinations(s, i+1):
                all_substrings.append(''.join(j))

        palindromes = [i for i in all_substrings if i == i[::-1]]
        # return the longest palindrome
        longest_palindrome = max(palindromes, key=len)
        return longest_palindrome


if __name__ == "__main__":
    s = "babad"
    sol = Solution()
    print(sol.longestPalindrome(s))
    s = "cbbd"
    print(sol.longestPalindrome(s))


        