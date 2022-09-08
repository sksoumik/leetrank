# https://leetcode.com/problems/house-robber

# You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed,
# the only constraint stopping you from robbing each of them is that adjacent houses have security systems connected
# and it will automatically contact the police if two adjacent houses were broken into on the same night.

# Given an integer array nums representing the amount of money of each house, return the maximum
#  amount of money you can rob tonight without alerting the police.


from typing import List


class Solution:
    # time complexity: O(n)
    # space complexity: O(1)
    # video explanation: https://youtu.be/1NTYeyxiFPc
    def rob(self, nums):

        for i in range(1, len(nums)):
            if i == 1:
                nums[i] = max(nums[i], nums[i - 1])
            else:
                nums[i] = max(nums[i - 1], nums[i] + nums[i - 2])

        return nums[-1]

    # Time complexity: O(n)
    # Space complexity: O(1)
    # dynamic programming
    def rob(self, nums: List[int]) -> int:
        """
        "rob1" is the maximum amount of money that can be robbed from the first i-1 houses
               store the last maximum amount of money
        "rob2" is the maximum amount of money that can be robbed from the first i houses
            store the current maximum amount of money

        """
        rob1, rob2 = 0, 0
        for num in nums:
            rob1, rob2 = rob2, max(rob1 + num, rob2)
        return rob2


if __name__ == "__main__":
    s = Solution()
    print(s.rob([1, 2, 3, 1]))
    print(s.rob([2, 7, 9, 3, 1]))
