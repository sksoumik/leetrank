# https://leetcode.com/problems/longest-common-prefix

# Write a function to find the longest common prefix string amongst an array of strings.
# If there is no common prefix, return an empty string "".

from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        """
        We zip the list of strings together, and then iterate through the zipped list.

        If the set of the characters in the zipped list is 1, then we add that character to the prefix.

        If the set of the characters in the zipped list is not 1, then we break out of the loop.

        :param strs: List[str]
        :type strs: List[str]
        :return: The longest common prefix of all the strings in the list.
        """
        prefix = ""

        for char in zip(*strs):
            if len(set(char)) == 1:
                prefix += char[0]
            else:
                break

        return prefix


if __name__ == "__main__":
    s = Solution()
    print(s.longestCommonPrefix(["flower", "flow", "flight"]))
    print(s.longestCommonPrefix(["dog", "racecar", "car"]))
