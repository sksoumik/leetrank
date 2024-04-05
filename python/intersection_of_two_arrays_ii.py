# https://leetcode.com/problems/intersection-of-two-arrays-ii/

# Given two integer arrays nums1 and nums2, return an array of their intersection.
# Each element in the result must appear as many times as it shows in both arrays
# and you may return the result in any order.


# Example 1:
# Input: nums1 = [1,2,2,1], nums2 = [2,2]
# Output: [2,2]

# Example 2:
# Input: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
# Output: [4,9]
# Explanation: [9,4] is also accepted.


from collections import Counter
from typing import List


class Solution:
    # pythonic way
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        c1 = Counter(nums1)
        c2 = Counter(nums2)
        return list((c1 & c2).elements())

    # brute force
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        result = []
        for i in nums1:
            if i in nums2:
                result.append(i)
                nums2.remove(i)
        return result


if __name__ == "__main__":
    s = Solution()
    print(s.intersect([1, 2, 2, 1], [2, 2]))  # [2, 2]
    print(s.intersect([4, 9, 5], [9, 4, 9, 8, 4]))  # [4, 9]
