# https://leetcode.com/problems/first-unique-character-in-a-string

# Given a string s, find the first non-repeating character in it
# and return its index. If it does not exist, return -1.

# Example 1:

# Input: s = "leetcode"
# Output: 0


class Solution:
    def firstUniqChar(self, s: str) -> int:
        if not s:
            return -1

        # create a hash table to store the characters and their counts
        hash = {}

        # iterate through the string and add the characters to the hash table
        for char in s:
            # if the character is not in the hash table, add it and set its count to 1
            if char not in hash:
                hash[char] = 1
            # if the character is in the hash table, increment its count
            else:
                hash[char] += 1

        # iterate through the hash table and return the index of the first character with a count of 1
        for i in range(len(s)):
            if hash[s[i]] == 1:
                return i
        # if no unique character is found, return -1
        return -1


if __name__ == "__main__":
    s = Solution()
    print(s.firstUniqChar("leetcode"))
    print(s.firstUniqChar("loveleetcode"))
    print(s.firstUniqChar("aabb"))
