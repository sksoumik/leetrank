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

        nums.sort()
        count = 0
        for i in range(len(nums) - 2):
            left, right = i + 1, len(nums) - 1
            while left < right:
                if nums[i] + nums[left] + nums[right] < target:
                    count += right - left
                    left += 1
                else:
                    right -= 1
        return count


if __name__ == "__main__":
    sol = Solution()
    print(sol.three_sum_smaller([-2, 0, 1, 3], 2))
    print(sol.three_sum_smaller([-2, 0, 1, 3], 4))
