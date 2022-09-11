# https://leetcode.com/problems/product-of-array-except-self

# Given an integer array nums, return an array answer such that answer[i] is 
# equal to the product of all the elements of nums except nums[i].
# The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

# Constraints: 
# You must write an algorithm that runs in O(n) time and without using the division operation.
# Can you solve the problem in O(1) extra space complexity? 
# (The output array does not count as extra space for space complexity analysis.)

 

# Example 1:

# Input: nums = [1,2,3,4]
# Output: [24,12,8,6]
# Example 2:

# Input: nums = [-1,1,0,-3,3]
# Output: [0,0,9,0,0]

from turtle import left
from typing import List


class Solution:
    # most obvious solution: using the division but we are not allowed to use division
    # def productExceptSelf(self, nums: List[int]) -> List[int]:
    #     product = 1
    #     for num in nums:
    #         product *= num
        
    #     return [product // num for num in nums]

    # O(n) time and O(1) space complexity; result array is not counted as extra space
    # video explanation: https://youtu.be/bNvIQI2wAjk
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        result = [1] * len(nums)

        # prefix product
        prefix = 1
        for i in range(len(nums)):
            result[i] = prefix
            prefix *= nums[i]
        
        postfix = 1
        for i in range(len(nums) - 1, -1, -1):
            result[i] *= postfix
            postfix *= nums[i]
        
        return result
    # time O(n), space O(n)
    # video explanation: https://youtu.be/eQ3eEOh0nSk
    def _productExceptSelf(self, nums: List[int]) -> List[int]:
        left = []
        product = 1
        for num in nums:
            left.append(product)
            product *= num

        right = []
        product = 1
        for num in reversed(nums):
            right.append(product)
            product *= num

        right = list(reversed(right))

        result = []
        for i in range(len(nums)):
            result.append(left[i] * right[i])

        return result



if __name__ == "__main__":
    nums = [1,2,3,4]
    sol = Solution()
    print(sol.productExceptSelf(nums))
    print(sol._productExceptSelf(nums))

        