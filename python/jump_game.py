# https://leetcode.com/problems/jump-game

# You are given an integer array nums. You are initially positioned at the
# array's first index, and each element in the array represents your maximum
# jump length at that position.

# Return true if you can reach the last index, or false otherwise.

# Input: nums = [2,3,1,1,4]
# Output: true
# Explanation: Jump 1 step from index 0 to 1, then 3 steps to the last index.

#  video explanation: https://youtu.be/EgMPjWliYGY

from typing import List


class Solution:
    # greedy approach
    # time complexity: O(n)
    def canJump(self, nums: List[int]) -> bool:
        goal = len(nums) - 1  # last index

        # for i in reversed(range(goal)):
        for idx in range(goal, -1, -1):
            if idx + nums[idx] >= goal:
                # we have added the current index to the jump length,
                # because at any given index, futhest we can reach is the current index + jump length
                goal = idx

        # return True if goal == 0 else False
        return goal == 0


if __name__ == "__main__":
    s = Solution()

    nums = [2, 3, 1, 1, 4]
    print(s.canJump(nums))
