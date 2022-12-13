# https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/


from typing import List

class Solution:
    def findMin(self, nums: List[int]) -> int:
        # method 1: O (n) solution: linear search
        # min_num = nums[0]
        # for i in range(1, len(nums)):
        #     if nums[i] < min_num:
        #         min_num = nums[i]
        # return min_num

        # method 2: O (log n) solution: binary search
        left, right = 0, len(nums) - 1
        while left < right:
            mid = left + (right - left) // 2
            if nums[mid] > nums[right]:
                left = mid + 1
            else:
                right = mid
        return nums[left]


if __name__ == "__main__":
    # test case 1
    nums = [3, 4, 5, 1, 2]
    print(Solution().findMin(nums))