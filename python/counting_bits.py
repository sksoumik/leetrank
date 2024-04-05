# https://leetcode.com/problems/counting-bits/

# Given an integer n, return an array ans of length n + 1 such that for
# each i (0 <= i <= n), ans[i] is the number of 1's in the binary representation of i.


# Input: n = 2
# Output: [0,1,1]
# Explanation:
# 0 --> 0
# 1 --> 1
# 2 --> 10

from typing import List


class Solution:
    def countBits(self, n: int) -> List[int]:
        # method 1: O (n) solution: bit manipulation
        ans = [0] * (n + 1)
        for i in range(1, n + 1):
            ans[i] = ans[i >> 1] + (i & 1)
        return ans

        # method 2: O (n) solution: built-in function
        # return [bin(i).count('1') for i in range(n + 1)]


if __name__ == "__main__":
    # test case 1
    n = 2
    print(Solution().countBits(n))

    # test case 2
    n = 5
    print(Solution().countBits(n))

    # test case 3
    n = 0
    print(Solution().countBits(n))
