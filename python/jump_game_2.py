# https://leetcode.com/problems/jump-game-ii/

# Given an array of non-negative integers nums, you are initially positioned at the first index of the array.
# Each element in the array represents your maximum jump length at that position.
# Your goal is to reach the last index in the minimum number of jumps.
# You can assume that you can always reach the last index.


# Example 1:
# Input: nums = [2,3,1,1,4]
# Output: 2
# Explanation: The minimum number of jumps to reach the last index is 2.
# Jump 1 step from index 0 to 1, then 3 steps to the last index.

# video explanation: https://youtu.be/wLPdkLM_BWo

from typing import List


class Solution:
    # time complexity: O(n)
    def jump(self, nums: List[int]) -> int:
        jumps, curren_idx, furthest_idx = 0, 0, 0
        for i in range(len(nums) - 1):
            furthest_idx = max(furthest_idx, i + nums[i])
            if i == curren_idx:
                jumps += 1
                curren_idx = furthest_idx
        return jumps


if __name__ == "__main__":
    nums = [2, 3, 1, 1, 4]
    print(Solution().jump(nums))  # 2
