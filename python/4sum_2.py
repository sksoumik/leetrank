# https://leetcode.com/problems/4sum-ii/

# Given four integer arrays nums1, nums2, nums3, and nums4 all of length n,
# return the number of tuples (i, j, k, l) such that:

# 0 <= i, j, k, l < n
# nums1[i] + nums2[j] + nums3[k] + nums4[l] == 0
# Example:

# Input: nums1 = [1,2], nums2 = [-2,-1], nums3 = [-1,2], nums4 = [0,2]
# Output: 2
# Explanation:
# The two tuples are:
# 1. (0, 0, 0, 1) -> nums1[0] + nums2[0] + nums3[0] + nums4[1] = 1 + (-2) + (-1) + 2 = 0
# 2. (1, 1, 0, 0) -> nums1[1] + nums2[1] + nums3[0] + nums4[0] = 2 + (-1) + (-1) + 0 = 0

from typing import List
from collections import defaultdict


class Solution:
    # brute force
    # time complexity: O(n^4)
    # space complexity: O(1)
    def _fourSumCount(
        self, nums1: List[int], nums2: List[int], nums3: List[int], nums4: List[int]
    ) -> int:

        result = 0
        for i in nums1:
            for j in nums2:
                for k in nums3:
                    for l in nums4:
                        if i + j + k + l == 0:
                            result += 1
        return result

    # time complexity: O(n^2)
    # space complexity: O(n^2)
    def fourSumCount(
        self, nums1: List[int], nums2: List[int], nums3: List[int], nums4: List[int]
    ) -> int:

        sums = defaultdict(int)
        result = 0

        for i in nums1:
            for j in nums2:
                sums[i + j] += 1

        for k in nums3:
            for l in nums4:
                result += sums[0 - (k + l)]

        return result


if __name__ == "__main__":
    s = Solution()
    print(s._fourSumCount([1, 2], [-2, -1], [-1, 2], [0, 2]))  # 2
    print(s.fourSumCount([1, 2], [-2, -1], [-1, 2], [0, 2]))  # 2
