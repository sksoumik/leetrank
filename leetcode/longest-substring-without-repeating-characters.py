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

        char_set = set()
        max_len = 0

        left_ptr = 0

        for right_ptr in range(len(s)):
            # while the right pointer already exists in the hash set, we remove the leftmost character
            while s[right_ptr] in char_set:
                char_set.remove(s[left_ptr])
                # move the left pointer to the right
                left_ptr += 1

            # add the character at the right pointer to the hash set
            char_set.add(s[right_ptr])

            # update the max length
            max_len = max(max_len, len(char_set))
        return max_len


if __name__ == "__main__":
    sol = Solution()
    print(sol.lengthOfLongestSubstring("abcabcbb"))
    print(sol.lengthOfLongestSubstring("bbbbb"))
