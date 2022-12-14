# https://leetcode.com/problems/longest-increasing-subsequence

# Given an integer array nums, return the length of the longest strictly increasing 
# subsequence. 

# Input: nums = [10,9,2,5,3,7,101,18]
# Output: 4
# Explanation: The longest increasing subsequence is [2,3,7,101], therefore the length is 4.

from typing import List
import bisect

class Solution:
    # method 1: binary search using bisect 
    def lengthOfLIS(self, nums: List[int]) -> int:
        # Initialize an empty list to store the longest increasing subsequences
        lis = []
        
        # Loop through each element in the input list
        for num in nums:
            # If the longest increasing subsequences list is empty,
            # or the current element is greater than the last element in the list,
            # append the current element to the list
            if not lis or num > lis[-1]:
                lis.append(num)

            # Otherwise, find the first element in the list that is greater than the current element
            # and replace it with the current element
            else:
                lis[bisect.bisect_left(lis, num)] = num

        # Return the length of the longest increasing subsequences list
        return len(lis)
        
    
    # method 2: binary search using binary search implementation
    def lengthOfLIS2(self, nums: List[int]) -> int:
        # find the index of the target in the array
        # if the target is not in the array, return the index where it should be inserted
        def binary_search(lis, target):
            left, right = 0, len(lis) - 1
            while left <= right:
                mid = (left + right) // 2
                if lis[mid] == target:
                    return mid
                elif lis[mid] < target:
                    left = mid + 1
                else:
                    right = mid - 1
            return left

        lis = []
        for num in nums:
            if not lis or num > lis[-1]:
                lis.append(num)
            else:
                lis[binary_search(lis, num)] = num

        return len(lis)

    # method 3: dynamic programming
    def lengthOfLIS3(self, nums: List[int]) -> int:
        # Initialize a list to store the length of the longest increasing subsequences
        # that ends with each element in the input list
        dp = [1] * len(nums)

        # Loop through each element in the input list
        for i in range(len(nums)):
            # Loop through each element before the current element
            for j in range(i):
                # If the current element is greater than the previous element,
                # update the length of the longest increasing subsequences that ends with the current element
                if nums[i] > nums[j]:
                    dp[i] = max(dp[i], dp[j] + 1)

        # Return the maximum length of the longest increasing subsequences
        return max(dp)


if __name__ == "__main__":
    nums = [10,9,2,5,3,7,101,18]
    print(Solution().lengthOfLIS(nums))
    print(Solution().lengthOfLIS2(nums))
    print(Solution().lengthOfLIS3(nums))


