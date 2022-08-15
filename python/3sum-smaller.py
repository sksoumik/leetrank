# leetcode premium
# https://leetcode.com/problems/3sum-smaller/

# Given an array of n integers nums and a target,
# find the number of index triplets i, j, k with 0 <= i < j < k < n
# that satisfy the condition nums[i] + nums[j] + nums[k] < target.

# Example1

# Input:  nums = [-2,0,1,3], target = 2
# Output: 2
# Explanation:
# Because there are two triplets which sums are less than 2:
# [-2, 0, 1]
# [-2, 0, 3]

from typing import List


class Solution:
    def three_sum_smaller(self, nums: List[int], target: int) -> int:
        if len(nums) < 3:
            return 0
        sums = 0
        nums.sort()
        for i in range(len(nums) - 2):
            sums += self.twoSumSmaller(nums[i + 1 :], target - nums[i])
        return sums

    def twoSumSmaller(self, nums, target):
        sums = 0
        left, right = 0, len(nums) - 1
        while left < right:
            if nums[left] + nums[right] < target:
                sums += right - left
                left += 1
            else:
                right -= 1
        return sums


if __name__ == "__main__":
    sol = Solution()
    print(sol.three_sum_smaller([-2, 0, 1, 3], 2))
    print(sol.three_sum_smaller([-2, 0, 1, 3], 4))
