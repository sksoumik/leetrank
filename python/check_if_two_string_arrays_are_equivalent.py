# https://leetcode.com/problems/check-if-two-string-arrays-are-equivalent/

# Given two string arrays word1 and word2, return true if the two arrays represent the same string, and false otherwise.
# A string is represented by an array if the array elements concatenated in order forms the string.


# Example 1:
# Input: word1 = ["ab", "c"], word2 = ["a", "bc"]
# Output: true
# Explanation:
# word1 represents string "ab" + "c" -> "abc"
# word2 represents string "a" + "bc" -> "abc"
# The strings are the same, so return true.

# Example 2:
# Input: word1 = ["a", "cb"], word2 = ["ab", "c"]
# Output: false

from typing import List


class Solution:
    def arrayStringsAreEqual(self, word1: List[str], word2: List[str]) -> bool:
        w1 = "".join(word1)
        w2 = "".join(word2)
        return w1 == w2


if __name__ == "__main__":
    s = Solution()
    print(s.arrayStringsAreEqual(["ab", "c"], ["a", "bc"]))  # True
    print(s.arrayStringsAreEqual(["a", "cb"], ["ab", "c"]))  # False
