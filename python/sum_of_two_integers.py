# https://leetcode.com/problems/sum-of-two-integers

# Given two integers a and b, return the sum of the two integers without using the operators + and -.


# Example 1:

# Input: a = 1, b = 2
# Output: 3


class Solution:
    # using recursion
    def _getSum(self, a, b):
        # If b is zero, return a
        if b == 0:
            return a

        # Calculate the sum of a and b without considering the carry
        sum_w_carry = a ^ b

        # Calculate the carry
        carry = (a & b) << 1

        # Return the sum of a and b
        return self._getSum(sum_w_carry, carry)

    def getSum(self, a: int, b: int) -> int:

        # method 1: O (n) solution: bit manipulation
        # 32-bit integer max: 2147483647
        # 32-bit integer min: -2147483648
        # mask to get last 32 bits
        mask = 0xFFFFFFFF
        # iterate until there is no carry
        while b != 0:
            # carry now contains common set bits of x and y
            carry = (a & b) & mask
            # sum of bits of x and y where at least one of the bits is not set
            a = (a ^ b) & mask
            # carry is shifted by one so that adding it to x gives the required sum
            b = (carry << 1) & mask
        # if a is negative, get a's 32-bit complement positive first
        # then get a's 32-bit binary form by doing ~a
        # then get a's decimal form by doing ~(~a)
        return a if a <= 0x7FFFFFFF else ~(a ^ mask)


if __name__ == "__main__":
    # test case 1
    a = 1
    b = 2
    print(Solution().getSum(a, b))

    # test case 2
    a = 2
    b = 3
    print(Solution().getSum(a, b))

    # test case 3
    a = -2
    b = 3
    print(Solution().getSum(a, b))
