# https://leetcode.com/problems/intersection-of-two-arrays/

# Given two integer arrays nums1 and nums2, return an array of their intersection.
# Each element in the result must be unique and you may return the result in any order.

# Input: nums1 = [1,2,2,1], nums2 = [2,2]
# Output: [2]
from typing import List


class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        unique_nums1 = set(nums1)
        unique_nums2 = set(nums2)
        return list(unique_nums1 & unique_nums2)


# test cases
if __name__ == "__main__":
    s = Solution()
    print(s.intersection([1, 2, 2, 1], [2, 2]))
    print(s.intersection([4, 9, 5], [9, 4, 9, 8, 4]))
    print(s.intersection([1, 2, 2, 1], [2]))
    print(s.intersection([1, 2, 2, 1], [1]))
    print(s.intersection([1, 2, 2, 1], [3]))
    print(s.intersection([1, 2, 2, 1], []))
    print(s.intersection([], [1, 2, 2, 1]))
    print(s.intersection([], []))
