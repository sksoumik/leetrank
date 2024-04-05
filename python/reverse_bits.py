# https://leetcode.com/problems/reverse-bits

# Reverse bits of a given 32 bits unsigned integer.

# Input: n = 00000010100101000001111010011100
# Output:    964176192 (00111001011110000010100101000000)
# Explanation: The input binary string 00000010100101000001111010011100 represents the unsigned integer 43261596,
# so return 964176192 which its binary representation is 00111001011110000010100101000000.


class Solution:
    def reverseBits(self, n: int) -> int:
        # method 1: O (1) solution: bit manipulation
        ans = 0
        for i in range(32):
            ans = (ans << 1) + (n & 1)
            n >>= 1
        return ans

        # method 2: O (1) solution: built-in function
        # return int(bin(n)[2:].zfill(32)[::-1], 2)


if __name__ == "__main__":
    # test case 1
    n = 43261596
    print(Solution().reverseBits(n))

    # test case 2
    n = 4294967293
    print(Solution().reverseBits(n))

    # test case 3
    n = 0
    print(Solution().reverseBits(n))
