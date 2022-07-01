# https://leetcode.com/problems/house-robber

# You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed,
# the only constraint stopping you from robbing each of them is that adjacent houses have security systems connected
# and it will automatically contact the police if two adjacent houses were broken into on the same night.

# Given an integer array nums representing the amount of money of each house, return the maximum
#  amount of money you can rob tonight without alerting the police.


# video explanation: https://youtu.be/73r3KWiEvyk


from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        """
        "rob1" is the maximum amount of money that can be robbed from the first i-1 houses, and "rob2"
        is the maximum amount of money that can be robbed from the first i houses

        :param nums: the list of houses
        :type nums: List[int]
        :return: The maximum amount of money that can be robbed from the houses.
        """
        rob1, rob2 = 0, 0
        for i in range(len(nums)):
            # swap the values of two variables.
            rob1, rob2 = rob2, max(rob1 + nums[i], rob2)
        return rob2


if __name__ == "__main__":
    s = Solution()
    print(s.rob([1, 2, 3, 1]))
    print(s.rob([2, 7, 9, 3, 1]))
