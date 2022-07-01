# https://leetcode.com/problems/is-subsequence

# Given two strings s and t, return true if s is a subsequence of t, or false otherwise.

# A subsequence of a string is a new string that is formed from the original string by 
# deleting some (can be none) of the characters without disturbing the relative positions 
# of the remaining characters. (i.e., "ace" is a subsequence of "abcde" while "aec" is not).

# Example 1:

# Input: s = "abc", t = "ahbgdc"
# Output: true



class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        iterable = iter(t)
        # Checking if all the characters in s are in iterable.
        return all(c in iterable for c in s)
    
    # recursive solution
    def isSubsequence(self, s: str, t: str) -> bool:
        if not s:
            return True
        if not t:
            return False
        if s[0] == t[0]:
            return self.isSubsequence(s[1:], t[1:])
        return self.isSubsequence(s, t[1:])


if __name__ == '__main__':
    s = "abc"
    t = "ahbgdc"
    print(Solution().isSubsequence(s, t))

    s = "axc"
    t = "ahbgdc"
    print(Solution().isSubsequence(s, t))


        
        