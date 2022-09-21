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

    

    def check_palindrome(self, s, left, right):
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        return s[left +1 :right] # +1 with left because we want to exclude the leftmost character
        


    # time limit exceeds: O(n^3)
    def longestPalindrome_2(self, s: str) -> str:
        if len(s) == 0:
            return ""
        if len(s) == 1:
            return s
        # make all possible combinations of substring
        # all_substrings = [''.join(l) for i in range(len(s)) for l in combinations(s, i+1)]
        # all possible combinations of substring
        all_substrings = []
        for i in range(len(s)):
            for j in range(i, len(s)):
                all_substrings.append(s[i : j + 1])
        
        # print(all_substrings)
        # check if each substring is a palindrome
        # return the longest palindrome
        palindromic_substrings = []
        for substring in all_substrings:
            if substring == substring[::-1]:
                palindromic_substrings.append(substring)
        

        max_len_plalindrome = max(palindromic_substrings, key=len)
        return max_len_plalindrome
            


if __name__ == "__main__":
    s = "babad"
    sol = Solution()
    print(sol.longestPalindrome(s))
    s = "babad"
    print(sol.longestPalindrome_2(s))


        