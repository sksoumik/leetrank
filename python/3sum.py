# https://leetcode.com/problems/3sum/
# Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]]
# such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

# Notice that the solution set must not contain duplicate triplets.

# Example 1:

# Input: nums = [-1,0,1,2,-1,-4]
# Output: [[-1,-1,2],[-1,0,1]]

from collections import Counter
from itertools import combinations
from typing import List


class Solution:
    # time limit exceeds
    def threeSum_1(self, nums: List[int]) -> List[List[int]]:
        counter_results = []
        for comb in combinations(nums, 3):
            if sum(comb) == 0:
                c = Counter(comb)
                if c not in counter_results:
                    counter_results.append(c)

        return [list(i.elements()) for i in counter_results]

    # time limit exceeds
    def threeSum_2(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        combs = [list(i) for i in combinations(nums, 3) if sum(i) == 0]
        # remove lists that contain same elements
        result = [list(i) for i in set(tuple(i) for i in combs)]
        return result

    # Brute force solution: O(n^3)
    def threeSum_2(self, nums: List[int]) -> List[List[int]]:
        if len(nums) < 3:
            return []

        triplets = []

        for i in range(0, len(nums) - 2):
            for j in range(i + 1, len(nums) - 1):
                for k in range(j + 1, len(nums)):
                    if nums[i] + nums[j] + nums[k] == 0:
                        triplets.append(tuple(sorted([nums[i], nums[j], nums[k]])))

        return list(set(triplets))

    # accepted solution: O (n^2)
    # video explanation: https://youtu.be/hNRS81I1OZ8
    def threeSum_3(self, nums: List[int]) -> List[List[int]]:
        nums.sort()

        if len(nums) < 3:
            return []

        triplets = []

        for i in range(0, len(nums) - 2):
            left, right = i + 1, len(nums) - 1
            while left < right:
                three_sum = nums[i] + nums[left] + nums[right]
                if three_sum == 0:
                    triplets.append(
                        (nums[i], nums[left], nums[right])
                    )  # add as tuple, because set(List[List[]]) is not supported
                    left += 1
                    right -= 1
                elif three_sum < 0:
                    left += 1
                else:
                    right -= 1

        return list(set(triplets))


if __name__ == "__main__":
    sol = Solution()
    print(sol.threeSum_3([-1, 0, 1, 2, -1, -4]))
