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
        # we need 3 pointers.

        # Pointer (i) representing the index in our iteration over the array.
        # Pointer (p0) repesenting the index we have to replace into if we found a 0.
        # Pointer (p2) representing the index we have to replace into if we found a 2.
        # By placing 0's and 2's into correct positions, there is no need to specially reorder 1's.
        # All 1's will eventually be left in correct positions.
        # So we dont worry when we see a 1, we just move on to the next index in our iteration.

        # Since we are arranging the numbers in ascending order, p0 should be initialized to 0 and
        # p2 should be initialized to the last index of the array. So whenever we first find a 0,
        # it will be put into the leftmost position, and p0 will be incremented.
        # So the next time we find a 0, we place it into the index 1.
        # Similarly, whenever we first find a 2, it will be put into the rightmost position of the array,
        # and p2 will be decremented.

        p0 = 0
        p2 = len(nums) - 1
        i = 0

        count = 0
        while count < len(nums):
            # if we found a 0, we place it into the leftmost position, and p0 will be incremented.
            if nums[i] == 0:
                nums[i], nums[p0] = nums[p0], nums[i]
                p0 += 1
                i += 1

            # if we found a 1, do nothing and move on to the next index in our iteration.
            elif nums[i] == 1:
                i += 1

            # else it must be a 2, so we place it into the rightmost position, and p2 will be decremented.
            else:
                nums[i], nums[p2] = nums[p2], nums[i]
                p2 -= 1

            count += 1
        # return nums


if __name__ == "__main__":
    nums = [2, 0, 2, 1, 1, 0]
    sol = Solution()
    print(sol.sortColors(nums))
