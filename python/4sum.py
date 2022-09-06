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
    # time complexity O(n^3)
    # space complexity O(n)
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        quadruplets = []

        for i in range(0, len(nums)):
            for j in range(i + 1, len(nums)):
                goal = target - nums[i] - nums[j]
                p1, p2 = j + 1, len(nums) - 1
                while p1 < p2:
                    two_sum = nums[p1] + nums[p2]
                    if two_sum == goal:
                        quadruplets.append((nums[i], nums[j], nums[p1], nums[p2]))
                        p1 += 1
                        p2 -= 1
                    elif two_sum < goal:
                        p1 += 1
                    else:
                        p2 -= 1

        return list(set(quadruplets))

    # brute force: using built-in combinations
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

    # brute force: time complexity O(n^4)
    # no external libraries
    def _fourSum(nums, target):
        quadruplets = []
        for i in range(0, len(nums) - 3):
            for j in range(i + 1, len(nums) - 2):
                for k in range(j + 1, len(nums) - 1):
                    for l in range(k + 1, len(nums)):
                        if nums[i] + nums[j] + nums[k] + nums[l] == target:
                            quadruplets.append([nums[i], nums[j], nums[k], nums[l]])

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
