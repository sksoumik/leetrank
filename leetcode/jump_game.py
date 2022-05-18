# https://leetcode.com/problems/jump-game

# You are given an integer array nums. You are initially positioned at the
# array's first index, and each element in the array represents your maximum
# jump length at that position.

# Return true if you can reach the last index, or false otherwise.

# Input: nums = [2,3,1,1,4]
# Output: true
# Explanation: Jump 1 step from index 0 to 1, then 3 steps to the last index.


# code explanation can be found here: https://youtu.be/Yan0cv2cLy8?t=606

from typing import List


class Solution:
    def canJump(self, nums: List[int]) -> bool:
        """
        If the last index is reachable from the first index, then return True, else return False

        :param nums: List[int] -> the array of integers
        :type nums: List[int]
        :return: The goal is to return True if the last index can be reached from the first index.
        """
        goal = len(nums) - 1  # last index
        # iterate the array backwards
        for idx in range(goal, -1, -1):
            if idx + nums[idx] >= goal:
                goal = idx

        # return True if goal == 0 else False
        return goal == 0


if __name__ == "__main__":
    s = Solution()

    nums = [2, 3, 1, 1, 4]
    print(s.canJump(nums))
