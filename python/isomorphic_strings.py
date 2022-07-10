# https://leetcode.com/problems/isomorphic-strings

# Given two strings s and t, determine if they are isomorphic.
# Two strings s and t are isomorphic if the characters in s can be replaced to get t.

# All occurrences of a character must be replaced with another character while
# preserving the order of characters. No two characters may map to the same character,
# but a character may map to itself.

# video explanation: https://youtu.be/7yF-U1hLEqQ


class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        map_st, map_ts = {}, {}

        for c1, c2 in zip(s, t):
            # This is checking if the character in s is already in the map_st dictionary.
            # If it is, then it checks if the value of the key is the same as the character in t.
            # If it is not, then it returns False.
            if c1 not in map_st:
                map_st[c1] = c2
            # if the character in t is already in the map_ts dictionary
            # then should map to the same element as the character
            # otherwise return False
            elif map_st[c1] != c2:
                return False

            # This is checking if the character in t is already in the map_ts dictionary.
            # If it is, then it checks if the value of the key is the same as the character in s.
            # If it is not, then it returns False.
            if c2 not in map_ts:
                map_ts[c2] = c1
            elif map_ts[c2] != c1:
                return False

        return True


if __name__ == "__main__":
    sol = Solution()
    print(sol.isIsomorphic("egg", "add"))
    print(sol.isIsomorphic("foo", "bar"))
    print(sol.isIsomorphic("paper", "title"))
