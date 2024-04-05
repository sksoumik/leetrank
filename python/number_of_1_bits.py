# https://leetcode.com/problems/number-of-1-bits

# Write a function that takes an unsigned integer and returns the number
# of '1' bits it has (also known as the Hamming weight).

# Input: n = 00000000000000000000000000001011
# Output: 3
# Explanation: The input binary string 00000000000000000000000000001011 has a total of three '1' bits.


class Solution:
    def hammingWeight(self, n: int) -> int:
        # method 1: O (n) solution: bit manipulation
        count = 0
        while n != 0:
            count += n & 1
            n >>= 1
        return count

        # method 2: O (n) solution: built-in function
        # return bin(n).count('1')


if __name__ == "__main__":
    # test case 1
    n = 0b00000000000000000000000000001011
    print(Solution().hammingWeight(n))

    # test case 2
    n = 0b00000000000000000000000010000000
    print(Solution().hammingWeight(n))
