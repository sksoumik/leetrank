# https://leetcode.com/problems/median-of-two-sorted-arrays

# Given two sorted arrays nums1 and nums2 of size m and n respectively,
# return the median of the two sorted arrays.
# The overall run time complexity should be O(log (m+n)).


# Example 1:
# Input: nums1 = [1,3], nums2 = [2]
# Output: 2.00000
# Explanation: merged array = [1,2,3] and median is 2.

from typing import List


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        merged_array = nums1 + nums2
        merged_array.sort()

        L = len(merged_array)

        # if the length of the merged array is even, return the middle
        # two elements divided by 2
        if len(merged_array) % 2 == 0:
            mid_left = merged_array[L // 2 - 1]
            mid_right = merged_array[L // 2]
            return (mid_left + mid_right) / 2
        # if the length of the merged array is odd, return the middle element
        else:
            return merged_array[L // 2]


if __name__ == "__main__":
    s = Solution()
    print(s.findMedianSortedArrays([1, 3], [2]))
    print(s.findMedianSortedArrays([1, 2], [3, 4]))
    print(s.findMedianSortedArrays([0, 0], [0, 0]))
    print(s.findMedianSortedArrays([], [1]))
    print(s.findMedianSortedArrays([2], []))
