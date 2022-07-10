# https://leetcode.com/problems/longest-repeating-character-replacement

# You are given a string s and an integer k. You can choose any character of 
# the string and change it to any other uppercase English character. 
# You can perform this operation at most k times.

# Return the length of the longest substring containing the same letter 
# you can get after performing the above operations.

from collections import Counter


class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        
        


if __name__ == "__main__":
    s = "ABAB"
    k = 2
    print(Solution().characterReplacement(s, k))
    s = "AABABBA"
    k = 1
    print(Solution().characterReplacement(s, k))





