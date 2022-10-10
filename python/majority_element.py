# https://leetcode.com/problems/majority-element/
# Given an array of size n, find the majority element. 
# The majority element is the element that appears more than floor(n/2) times.
# You may assume that the array is non-empty and the majority element always exist in the array.

# Example :
# Input : [2, 1, 2]
# Return  : 2 which occurs 2 times which is greater than 3/2.


class Solution:
    # @param A : tuple of integers
    # @return an integer
    def majorityElement(self, nums):
        nums.sort()
        return nums[len(nums)//2]

if __name__ == "__main__":
    s = Solution()
    print(s.majorityElement([2, 1, 2]))
    

