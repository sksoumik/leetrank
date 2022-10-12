# https://leetcode.com/problems/minimum-deletions-to-make-character-frequencies-unique/

# A string s is called good if there are no two different characters in s that have the same frequency.
# Given a string s, return the minimum number of characters you need to delete to make s good.
# The frequency of a character in a string is the number of times it appears in the string.
# For example, in the string "aab", the frequency of 'a' is 2, while the frequency of 'b' is 1.

# Example 1:
# Input: s = "aab"
# Output: 0
# Explanation: s is already good.

from collections import Counter


class Solution:
    # time complexity: O(n)
    # space complexity: O(n)
    def minDeletions(self, s: str) -> int:
        c = Counter(s)
        unique = set()
        deletions = 0
        for k, frequency in c.items():
            while frequency > 0 and frequency in unique:
                frequency -= 1
                deletions += 1
            unique.add(frequency)
        return deletions


if __name__ == "__main__":
    s = Solution()
    print(s.minDeletions("aab"))
    print(s.minDeletions("aaabbbcc"))
