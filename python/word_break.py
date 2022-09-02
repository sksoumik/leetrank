# https://leetcode.com/word-break/

# Given a string s and a dictionary of strings wordDict, return true if s can be
# segmented into a space-separated sequence of one or more dictionary words.
# Note that the same word in the dictionary may be reused multiple times in the segmentation.


# example 1:

# Input: s = "leetcode", wordDict = ["leet","code"]
# Output: true
# Explanation: Return true because "leetcode" can be segmented as "leet code".

# example 2:

# Input: s = "catsandog", wordDict = ["cats","dog","sand","and","cat"]
# Output: false

from typing import List


class Solution:
    # time limit exceeded
    def _wordBreak(self, s: str, wordDict: List[str]) -> bool:
        # recursive solution

        # if the string is empty, return True
        if not s:
            return True

        for i in range(len(s)):
            if s[: i + 1] in wordDict:
                if self._wordBreak(s[i + 1 :], wordDict):
                    return True

        return False

    # dynamic programming solution
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        if not s:
            return True

        # initialize every element in the array to False
        dp = [False] * (len(s) + 1)  # +1 is for our base case
        # base case
        dp[0] = True  # [True, False, False, False]

        for i in range(1, len(s) + 1):
            for j in range(i):
                if dp[j] and s[j:i] in wordDict:
                    dp[i] = True
                    break

        return dp[-1]


if __name__ == "__main__":
    sol = Solution()
    s = "leetcode"
    wordDict = ["leet", "code"]
    print(sol._wordBreak(s, wordDict))  # True

    s = "catsandog"
    wordDict = ["cats", "dog", "sand", "and", "cat"]
    print(sol._wordBreak(s, wordDict))  # False

    s = "applepenapple"
    wordDict = ["apple", "pen"]
    print(sol._wordBreak(s, wordDict))  # True

    s = "leetcode"
    wordDict = ["leet", "code"]
    print(sol.wordBreak(s, wordDict))  # True

    s = "catsandog"
    wordDict = ["cats", "dog", "sand", "and", "cat"]
    print(sol.wordBreak(s, wordDict))  # False

    s = "applepenapple"
    wordDict = ["apple", "pen"]
    print(sol.wordBreak(s, wordDict))  # True
