# https://leetcode.com/problems/jump-game

# You are given an integer array nums. You are initially positioned at the
# array's first index, and each element in the array represents your maximum
# jump length at that position.

# Return true if you can reach the last index, or false otherwise.

# Input: nums = [2,3,1,1,4]
# Output: true
# Explanation: Jump 1 step from index 0 to 1, then 3 steps to the last index.


from typing import List


class Solution:
    # https://youtu.be/Yan0cv2cLy8?t=606
    def canJump(self, nums: List[int]) -> bool:
        """
        greedy approach : O (n)
        we start from the end of the array
        if we can reach the end index from its previous index
        then we update the goal to its previous index and then look again
        wheather we can reach to the updated goal from its previous index
        we continue this and if we can make the goal to reach at index 0
        then we return True
        else False
        """
        goal = len(nums) - 1  # last index
        # iterate the array backwards
        for idx in range(goal, -1, -1):
            if idx + nums[idx] >= goal:
                goal = idx

        # return True if goal == 0 else False
        return goal == 0

    # second approach
    # time complexity O(n)
    # video explanation: https://youtu.be/muDPTDrpS28
    def _canJump(self, nums: List[int]) -> bool:
        reachable = 0

        for idx, num in enumerate(nums):
            if idx > reachable:
                return False
            reachable = max(reachable, idx + num)

        return True


if __name__ == "__main__":
    s = Solution()

    nums = [2, 3, 1, 1, 4]
    print(s.canJump(nums))
