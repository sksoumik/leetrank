# https://leetcode.com/problems/group-anagrams

# Given an array of strings strs, group the anagrams together.
# You can return the answer in any order.

# An Anagram is a word or phrase formed by rearranging the letters of
#  a different word or phrase, typically using all the original letters exactly once.


# Example 1:

# Input: strs = ["eat","tea","tan","ate","nat","bat"]
# Output: [["bat"],["nat","tan"],["ate","eat","tea"]]


from typing import List


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # use a hashmap to store the anagrams
        # key: sorted string, value: list of anagrams
        anagrams = {}
        for s in strs:  # O(n) time
            sorted_s = "".join(sorted(s))
            if sorted_s in anagrams:
                anagrams[sorted_s].append(s)
            else:
                anagrams[sorted_s] = [s]
        return list(anagrams.values())


if __name__ == "__main__":
    strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
    sol = Solution()
    print(sol.groupAnagrams(strs))
