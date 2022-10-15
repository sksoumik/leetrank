# https://leetcode.com/problems/divide-two-integers

# Given two integers dividend and divisor, divide two integers without
# using multiplication, division, and mod operator.
# The integer division should truncate toward zero, which means losing its fractional part.
# For example, 8.345 would be truncated to 8, and -2.7335 would be truncated to -2.

# Return the quotient after dividing dividend by divisor.


class Solution:
    # time complexity: O(log(n))
    # space complexity: O(1)
    # time limit exceeded
    def divide(self, dividend: int, divisor: int) -> int:
        # edge case
        if dividend == -(2**31) and divisor == -1:
            return 2**31 - 1

        # if either dividend or divisor is negative, then the result is negative
        sign = -1 if (dividend < 0) ^ (divisor < 0) else 1

        # convert to positive
        dividend, divisor = abs(dividend), abs(divisor)

        # get the quotient
        quotient = 0
        while dividend >= divisor:
            dividend -= divisor
            quotient += 1

        return sign * quotient


if __name__ == "__main__":
    solution = Solution()
    print(solution.divide(10, 3))  # 3
    print(solution.divide(7, -3))  # -2
    print(solution.divide(0, 1))  # 0
    print(solution.divide(1, 1))  # 1
    print(solution.divide(-2147483648, -1))  # 2147483647
