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
    # vid: https://youtu.be/QQVCKkImH_s
    def maxProduct(self, nums: List[int]) -> int:
        """
        You have three choices to make at any position in array.

        1. You can get maximum product by multiplying the current element with
           maximum product calculated so far. (might work when current
           element is positive).

        2. You can get maximum product by multiplying the current element with
           minimum product calculated so far. (might work when current
           element is negative).

        3. Current element might be a starting position for maximum product sub
           array
        """
        max_product = nums[0]
        min_product = nums[0]
        result = nums[0]

        for i in range(1, len(nums)):
            positive_product = max(
                nums[i], max_product * nums[i], min_product * nums[i]
            )
            negative_product = min(
                nums[i], max_product * nums[i], min_product * nums[i]
            )
            max_product = positive_product
            min_product = negative_product
            result = max(result, max_product)
        return result


if __name__ == "__main__":
   sol = Solution()

   nums = [2, 3, -2, 4]
   print(sol.maxProduct(nums))

   nums = [-1, -2, -4]
   print(sol.maxProduct(nums))
