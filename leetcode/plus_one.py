# https://leetcode.com/problems/plus-one/

# You are given a large integer represented as an integer array digits, where each digits[i]
#  is the ith digit of the integer. The digits are ordered from most significant
# to least significant in left-to-right order. The large integer does not contain any leading 0's.
from typing import List


class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        # convert array to int
        num = int("".join(str(x) for x in digits))
        # add 1
        num += 1
        # convert int to array
        return [int(x) for x in str(num)]


if __name__ == "__main__":
    s = Solution()
    print(s.plusOne([1, 2, 3]))
    print(s.plusOne([4, 3, 2, 1]))
    print(s.plusOne([9, 9, 9]))
    print(s.plusOne([9]))
