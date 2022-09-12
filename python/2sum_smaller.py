# leetcode premium problem
# https://leetcode.com/problems/two-sum-less-than-k/

# Given some array of positive integers A, 
# find the length of the longest subarray such that 
# the sum of all its values is less than or equal to some positive integer K.
# If no solution is found, return -1. 

# Example 1:
# Input: A = [34,23,1,24,75,33,54,8], K = 60
# Output: 58
# Explanation:
# We can use 34 and 24 to sum 58 which is less than 60.

# Example 2:
# Input: A = [10,20,30], K = 15
# Output: -1
# Explanation:
# In this case it's not possible to get a pair sum less that 15.


class Solution:
    def twoSumLessThanK(self, A, K):
        max_array = -1
        A.sort()
        left, right = 0, len(A) - 1
        while left < right:
            if A[left] + A[right] <= K:
                max_array = max(max_array, A[right] + A[left])
                left += 1
            else:
                right -= 1
        return max_array


if __name__ == "__main__":
    sol = Solution()
    A =  [34, 23, 1, 24, 75, 33, 54, 8]
    K = 60
    print(sol.twoSumLessThanK(A, K))