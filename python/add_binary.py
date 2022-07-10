# https://leetcode.com/problems/add-binary/
# Given two binary strings a and b, return their sum as a binary string.


class Solution:
    def addBinary(self, a: str, b: str) -> str:
        # Converting the binary string to an integer.
        a = int(a, 2)
        b = int(b, 2)
        # add a and b
        c = a + b
        # convert int to binary string
        return bin(c)[2:]


if __name__ == "__main__":
    s = Solution()
    print(s.addBinary("11", "1"))
    print(s.addBinary("1010", "1011"))
    print(s.addBinary("1010", "1010"))
    print(s.addBinary("1010", "101"))

