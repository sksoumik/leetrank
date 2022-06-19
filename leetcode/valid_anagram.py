# https://leetcode.com/problems/valid-anagram

# Given two strings s and t, return true if t is an anagram of s, and false otherwise.

# An Anagram is a word or phrase formed by rearranging the letters of a different word or
# phrase, typically using all the original letters exactly once.

from collections import Counter

# Example 1:

# Input: s = "anagram", t = "nagaram"
# Output: true


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return len(s) == len(t) and Counter(s) == Counter(t)


if __name__ == "__main__":
    s = "anagram"
    t = "nagaram"
    print(Solution().isAnagram(s, t))
    s = "rat"
    t = "car"
    print(Solution().isAnagram(s, t))
