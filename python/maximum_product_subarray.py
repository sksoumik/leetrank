# https://leetcode.com/problems/maximum-product-subarray/

# Given an integer array nums, find a contiguous non-empty subarray within
# the array that has the largest product, and return the product.
# The test cases are generated so that the answer will fit in a 32-bit integer.
# A subarray is a contiguous subsequence of the array.


# Example 1:

# Input: nums = [2,3,-2,4]
# Output: 6
# Explanation: [2,3] has the largest product 6.

from typing import List


class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        """
        We keep track of the max and min product of the subarray that ends at the current number.
        The max product is either the current number itself or the max by far times the current number.
        The min product is either the current number itself or the min by far times the current number.
        We update the max and min product of the subarray that ends at the current number before moving on
        to the next number.

        The overall max product is the max we have seen so far

        :param nums: the list of numbers
        :type nums: List[int]
        :return: The max product of the subarray

        [2  3  -2  4]
        max = 2, 2*3, 2*3 = 6 | -2, 6*(-2), 2*(-2)
        min = 2, 2*3, 2*3 = 2 | 
        global = 6 

        """

        current_max_product = current_min_product = global_max_product = nums[0]

        for num in nums[1:]:
            # max product of the subarray that ends at the current number
            current_max_product, current_min_product = max(num, current_max_product * num, current_min_product * num),  \
                                                       min(num, current_max_product * num, current_min_product * num)
            global_max_product = max(global_max_product, current_max_product)

        return global_max_product
