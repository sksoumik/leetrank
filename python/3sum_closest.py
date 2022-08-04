# https://leetcode.com/problems/3sum-closest

# Given an integer array nums of length n and an integer target, find three integers in nums such that the sum is closest to target.
# Return the sum of the three integers.
# You may assume that each input would have exactly one solution.

# Example 1:

# Input: nums = [-1,2,1,-4], target = 1
# Output: 2
# Explanation: The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).


from typing import List
from itertools import combinations

class Solution:
    # works but time limit exceeded
    def threeSumClosest_2(self, nums: List[int], target: int) -> int:
        nums.sort()
        # all 3 combinations
        combs = [list(c) for c in combinations(nums, 3)]
        # get the sum of each combination
        sums = [sum(c) for c in combs]
        # get the difference between the target and each sum
        diffs = [abs(target - s) for s in sums]
        print(diffs)
        # get the index of the minimum difference
        min_index = diffs.index(min(diffs))
        print(min_index)
        return sums[min_index]

    # accepted solution
    def threeSumClosest(self, nums: List[int]) -> List[List[int]]:
        nums.sort()

        if len(nums) < 3:
            return []

        triplets = []

        for i in range(0, len(nums) - 2):
            j, k = i + 1, len(nums) - 1
            while j < k:
                three_sum = nums[i] + nums[j] + nums[k]
                if three_sum == 0:
                    triplets.append(tuple(sorted([nums[i], nums[j], nums[k]])))
                    j += 1
                    k -= 1
                elif three_sum < 0:
                    j += 1
                else:
                    k -= 1

        return list(set(triplets))

if __name__ == "__main__":
    nums = [-1,2,1,-4] 
    target = 1
    print(Solution().threeSumClosest(nums, target))
        