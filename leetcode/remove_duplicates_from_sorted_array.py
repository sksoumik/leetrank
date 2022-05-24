# https://leetcode.com/problems/remove-duplicates-from-sorted-array

# Given an integer array nums sorted in non-decreasing order, 
# remove the duplicates in-place such that each unique element appears only once. 
# The relative order of the elements should be kept the same.

# Since it is impossible to change the length of the array in some languages,
#  you must instead have the result be placed in the first part of the array nums. 
#  More formally, if there are k elements after removing the duplicates, 
#  then the first k elements of nums should hold the final result. 
# It does not matter what you leave beyond the first k elements.

from typing import List

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        
        i = 0
        for j in range(1, len(nums)):
            if nums[i] != nums[j]:
                i += 1
                nums[i] = nums[j]
        return i + 1


if __name__ == "__main__":
    s = Solution()
    print(s.removeDuplicates([1,1,2]))
    print(s.removeDuplicates([0,0,1,1,1,2,2,3,3,4]))