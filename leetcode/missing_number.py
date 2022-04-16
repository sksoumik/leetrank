# https://leetcode.com/problems/missing-number/

# Given an array nums containing n distinct numbers in the range [0, n],
# return the only number in the range that is missing from the array.

from typing import List


class Solution:
    def missingNumber(self, nums: List[int]) -> int:

        # Creating a list of all the numbers from 0 to n.
        all_nums = []

        for i in range(len(nums) + 1):
            all_nums.append(i)

        # find the missing number
        # uncommon number between nums and all_nums
        missing_num = list(set(all_nums) ^ set(nums))

        # return the value of the list of missing_num
        return missing_num[0]


if __name__ == "__main__":
    nums = [0, 1, 3]
    print(Solution().missingNumber(nums))
    nums = [0, 1, 2, 4]
    print(Solution().missingNumber(nums))
