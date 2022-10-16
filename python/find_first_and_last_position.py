# https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/

# Given an array of integers nums sorted in non-decreasing order,
# find the starting and ending position of a given target value.
# If target is not found in the array, return [-1, -1].
# You must write an algorithm with O(log n) runtime complexity.


# Example 1:
# Input: nums = [5,7,7,8,8,10], target = 8
# Output: [3,4]

from typing import List


class Solution:
    # pythonic way
    # time complexity: O(n)
    def _searchRange(self, nums: List[int], target: int) -> List[int]:
        last_idx = len(nums) - 1
        try:
            return [nums.index(target), last_idx - nums[::-1].index(target)]
        except ValueError:
            return [-1, -1]

    # modified binary search
    # time complexity: O(log(n))
    # space complexity: O(1)
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        result = [-1, -1]
        result[0] = self.find_starting_idx(nums, target)
        result[1] = self.find_ending_idx(nums, target)
        return result

    def find_starting_idx(self, nums, target):
        index = -1
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                index = mid
                # for first occurrence, we need to search on the left side
                right = mid - 1

            elif target < nums[mid]:
                # look into the left side
                right = mid - 1

            else:
                # look into the right half
                left = mid + 1

        return index

    def find_ending_idx(self, nums, target):
        index = -1
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                index = mid
                # for last occurrence, we need to search on the right side
                left = mid + 1

            # if the target is less than the mid, then we need to search on the left side
            elif target < nums[mid]:
                right = mid - 1

            # if the target is greater than the mid, then we need to search on the right side
            else:
                left = mid + 1

        return index


if __name__ == "__main__":
    solution = Solution()
    print(solution.searchRange([5, 7, 7, 8, 8, 10], 8))  # [3,4]
    print(solution.searchRange([5, 7, 7, 8, 8, 10], 6))  # [-1,-1]
    print(solution.searchRange([], 0))  # [-1,-1]
