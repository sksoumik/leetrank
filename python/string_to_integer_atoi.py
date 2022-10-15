# https://leetcode.com/problems/string-to-integer-atoi

# Implement the myAtoi(string s) function, 
# which converts a string to a 32-bit signed integer (similar to C/C++'s atoi function).
# The algorithm for myAtoi(string s) is as follows:
# Read in and ignore any leading whitespace.

# Input: s = "42"
# Output: 42

# Input: s = "   -42"
# Output: -42

# Input: s = "4193 with words"
# Output: 4193


class Solution:
    def myAtoi(self, s: str) -> int:
        