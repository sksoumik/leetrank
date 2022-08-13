# https://leetcode.com/problems/4sum

# Given an array nums of n integers, return an array of all the unique quadruplets [nums[a], nums[b], nums[c], nums[d]] such that:

# 0 <= a, b, c, d < n
# a, b, c, and d are distinct.
# nums[a] + nums[b] + nums[c] + nums[d] == target
# You may return the answer in any order.


# Example 1:

# Input: nums = [1,0,-1,0,-2,2], target = 0
# Output: [[-2,-1,1,2],[-2,0,0,2],[-1,0,0,1]]
# Example 2:

# Input: nums = [2,2,2,2,2], target = 8
# Output: [[2,2,2,2]]

from typing import List


class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        """
        :param nums: the list of numbers
        :type nums: List[int]
        :param target: the target sum
        :type target: int
        :return: the list of quadruplets that sum to target
        :rtype: List[List[int]]
        """
        nums.sort()
        quadruplets = []
        for i in range(len(nums) - 3):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            for j in range(i + 1, len(nums) - 2):
                if j > i + 1 and nums[j] == nums[j - 1]:
                    continue
                left, right = j + 1, len(nums) - 1
                while left < right:
                    sum = nums[i] + nums[j] + nums[left] + nums[right]
                    if sum == target:
                        quadruplets.append([nums[i], nums[j], nums[left], nums[right]])
                        left += 1
                        right -= 1
                        while left < right and nums[left] == nums[left - 1]:
                            left += 1
                        while left < right and nums[right] == nums[right + 1]:
                            right -= 1
                    elif sum < target:
                        left += 1
                    else:
                        right -= 1
        return quadruplets

    # time limit exceeds
    def fourSum2(self, nums: List[int], target: int) -> List[List[int]]:
        # using itertools
        from itertools import combinations

        nums.sort()

        quadruplets = []

        all_combinations = combinations(nums, 4)
        for combination in list(set(all_combinations)):
            if sum(combination) == target:
                quadruplets.append(list(combination))

        return quadruplets


if __name__ == "__main__":
    nums = [1, 0, -1, 0, -2, 2]
    target = 0
    sol = Solution()
    print(sol.fourSum(nums, target))
    print(sol.fourSum2(nums, target))

    nums = [2, 2, 2, 2]
    target = 8
    print(sol.fourSum2(nums, target))
