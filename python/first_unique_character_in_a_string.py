# https://leetcode.com/problems/first-unique-character-in-a-string

# Given a string s, find the first non-repeating character in it and return its index. If it does not exist, return -1.

 

# Example 1:

# Input: s = "leetcode"
# Output: 0
from collections import Counter

class Solution:
    def firstUniqChar(self, s: str) -> int:
        if not s:
            return -1

        cnt = Counter(s)
        
        for idx, char in enumerate(s):
            if cnt[char] == 1:
                return idx
        return -1


if __name__ == '__main__':
    s = Solution()
    print(s.firstUniqChar("leetcode"))
    print(s.firstUniqChar("loveleetcode"))
    print(s.firstUniqChar("aabb"))



            
        