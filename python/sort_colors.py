# https://leetcode.com/problems/sort-colors

# Given an array nums with n objects colored red, white, or blue,
# sort them in-place so that objects of the same color are adjacent,
# with the colors in the order red, white, and blue.

# We will use the integers 0, 1, and 2 to represent the color red, white, and blue, respectively.

# You must solve this problem without using the library's sort function.


# Example 1:

# Input: nums = [2,0,2,1,1,0]
# Output: [0,0,1,1,2,2]


# Example 2:

# Input: nums = [2,0,1]
# Output: [0,1,2]


# Follow up: Could you come up with a one-pass algorithm using only constant extra space?

from typing import List

# it can be easily solved using sort(), but it's not allowed
# we must solve it in-place
# we must solve it using one pass
# we must solve it using constant extra space
# time O(n), space O(1)


class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        0 : red
        1 : white
        2 : blue

        Follwing dutch partitioning problem
        """
        red, white, blue = 0, 0, len(nums) - 1

        while white <= blue:
            if nums[white] == 0:
                nums[red], nums[white] = nums[white], nums[red]
                white += 1
                red += 1

            elif nums[white] == 1:
                white += 1

            else:
                nums[white], nums[blue] = nums[blue], nums[white]
                blue -= 1


if __name__ == "__main__":
    nums = [2, 0, 2, 1, 1, 0]
    sol = Solution()
    print(sol.sortColors(nums))
