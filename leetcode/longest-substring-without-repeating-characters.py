# https://leetcode.com/problems/longest-substring-without-repeating-characters

# Given a string s, find the length of the longest substring without repeating characters. 

# Example 1:

# Input: s = "abcabcbb"
# Output: 3
# Explanation: The answer is "abc", with the length of 3.

# code explanation: https://www.youtube.com/watch?v=wiGpQwVHdE0
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        """
        We use a sliding window, and we keep expanding the window by moving the right pointer. 
        
        If the character at the right pointer is already in the hash set, we remove the leftmost
        character from the hash set, and then move the left pointer so that the sliding window contains
        only distinct characters. 
        
        By keeping a running count of the maximum size of the hash set, we can determine the length of
        the longest substring with distinct characters
        
        :param s: the string we're trying to find the longest substring of
        :type s: str
        :return: The length of the longest substring without repeating characters.
        """
        if len(s) <= 1:
            return len(s)
        
        
