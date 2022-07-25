# https://leetcode.com/problems/merge-sorted-array

# You are given two integer arrays nums1 and nums2, sorted in non-decreasing order,
# and two integers m and n, representing the number of elements in nums1 and nums2 respectively.

# Merge nums1 and nums2 into a single array sorted in non-decreasing order.

# The final sorted array should not be returned by the function, but instead be
# stored inside the array nums1. To accommodate this, nums1 has a length of m + n,
#  where the first m elements denote the elements that should be merged, and the
#  last n elements are set to 0 and should be ignored. nums2 has a length of n.


# Example 1:

# Input: nums1 = [1,2,3,0,0,0], m = 3, nums2 = [2,5,6], n = 3
# Output: [1,2,2,3,5,6]
# Explanation: The arrays we are merging are [1,2,3] and [2,5,6].
# The result of the merge is [1,2,2,3,5,6] with the underlined elements coming from nums1.

from typing import List


class Solution:
    # easy solution but might not work for coding interviews
    # def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
    #
    #     nums1[m:] = nums2[:n]
    #     nums1.sort()

    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """

        # start merging from the ends of the lists
        p1, p2 = m - 1, n - 1
        last_idx = m + n - 1
        # destination d index to insert into nums1
        for d in range(last_idx, -1, -1):
            # if second list is empty, nothing more to merge
            if p2 < 0:
                return
            # only merge from nums1 if there are items left to merge
            # insert at d the larger of the two values from nums1 and nums2
            if p1 >= 0 and nums1[p1] > nums2[p2]:
                nums1[d] = nums1[p1]
                p1 -= 1
            else:
                nums1[d] = nums2[p2]
                p2 -= 1


if __name__ == "__main__":
    nums1 = [1, 2, 3, 0, 0, 0]
    m = 3
    nums2 = [2, 5, 6]
    n = 3
    Solution().merge(nums1, m, nums2, n)
