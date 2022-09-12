# https://leetcode.com/problems/3sum-closest

# Given an integer array nums of length n and an integer target, 
# find three integers in nums such that the sum is closest to target.
# Return the sum of the three integers.
# You may assume that each input would have exactly one solution.

# Example 1:
# Input: nums = [-1,2,1,-4], target = 1
# Output: 2
# Explanation: The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).


from typing import List

class Solution:    

    # brute force: time complexity O(n^3)
    def _threeSumClosest(self, nums, target):
        nums.sort()
        min_diff = float("inf")
        min_sum = 0
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                for k in range(j + 1, len(nums)):
                    three_sum = nums[i] + nums[j] + nums[k]
                    diff = abs(three_sum - target)
                    if diff < min_diff:
                        min_diff = diff
                        min_sum = three_sum
        return min_sum

    # accepted solution
    # time complexity: O(n^2), space complexity: O(1)
    def threeSumClosest(self, nums, target):
        nums.sort()

        if len(nums) < 3:
            return []

        best_3sum_closest_to_target = float("inf")

        for i in range(0, len(nums) - 2):
            p1, p2 = i + 1, len(nums) - 1
            while p1 < p2:
                three_sum = nums[i] + nums[p1] + nums[p2]
                if three_sum == target:
                    return three_sum

                if abs(three_sum - target) < abs(best_3sum_closest_to_target - target):
                    best_3sum_closest_to_target = three_sum
                
                if three_sum < target:
                    p1 += 1
                else:
                    p2 -= 1

        return best_3sum_closest_to_target


if __name__ == "__main__":
    nums = [-1,2,1,-4] 
    target = 1
    print(Solution().threeSumClosest(nums, target))
        