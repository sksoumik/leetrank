# https://leetcode.com/problems/largest-number/

# Given a list of non-negative integers nums, arrange them such that they form the largest number and return it.
# Since the result may be very large, so you need to return a string instead of an integer.


# Example 1:

# Input: nums = [10,2]
# Output: "210"


from typing import List


class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        # convert all numbers to string
        nums = [str(num) for num in nums]
        # sort the list of strings
        # lambda function should return a unique value for each element in the list.
        # Since the elements in the list are strings,
        # any mathematical operation on the string will return a unique value.
        nums.sort(key=lambda x: x * 10, reverse=True)
        return str(int("".join(nums)))


if __name__ == "__main__":
    print(Solution().largestNumber([10, 2]))
    print(Solution().largestNumber([3, 30, 34, 5, 9]))
    print(Solution().largestNumber([1]))
    print(Solution().largestNumber([10]))
