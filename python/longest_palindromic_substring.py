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
        result = ""
        for i in range(len(s)):
            # odd length palindrome
            odd_palindrome = self.check_palindrome(s, i, i)

            # even length palindrome
            even_palindrome = self.check_palindrome(s, i, i+1)

            # longest palindrome
            if len(odd_palindrome) > len(result):
                result = odd_palindrome
            if len(even_palindrome) > len(result):
                result = even_palindrome
        return result

    

    def check_palindrome(self, s, low, high):
        while low >= 0 and high < len(s) and s[low] == s[high]:
            low -= 1
            high += 1
        return s[low + 1:high]
        


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


        