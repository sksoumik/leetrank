# https://leetcode.com/problems/find-the-duplicate-number

# Given an array of integers nums containing n + 1 integers where each integer is in the range [1, n] inclusive.

# There is only one repeated number in nums, return this repeated number.

# You must solve the problem without modifying the array nums and uses only constant extra space.

from typing import List


class Solution:
    # time complexity: O(n), space complexity O(n)
    def findDuplicate(self, nums: List[int]) -> int:
        """
        We iterate through the list, and if we see an element that we've seen before, we return it

        :param nums: List[int] -> This is the list of numbers that we're going to be searching through
        :type nums: List[int]
        :return: The first duplicate element in the list.
        """
        seen = set()

        for _, element in enumerate(nums):
            if element in seen:
                return element
            else:
                seen.add(element)

        return -1

    # time complexity: O(nlogn), space complexity O(1)
    def findDuplicate2(self, nums):
        nums.sort()
        for i in range(len(nums) - 1):
            if nums[i] == nums[i + 1]:
                return nums[i]
        return -1

    # floyd's cycle detection algorithm
    # vid: https://youtu.be/wjYnzkAhcNk
    # time complexity: O(n), space complexity O(1)
    def findDuplicate3(self, nums: List[int]) -> int:
        slow = nums[0]
        fast = nums[0]

        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break

        slow = nums[0]
        while slow != fast:
            slow = nums[slow]
            fast = nums[fast]

        return slow


if __name__ == "__main__":
    nums = [1, 3, 4, 2, 2]
    print(Solution().findDuplicate3(nums))  # 2
