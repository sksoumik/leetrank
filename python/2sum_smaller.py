# leetcode premium problem
# https://leetcode.com/problems/two-sum-less-than-k/

# Given some array of positive integers A,
# find the pair sum of two integers in A that is less than or equal to K,
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
        A.sort()

        pair_sum = -1
        left, right = 0, len(A) - 1
        while left < right:
            if A[left] + A[right] <= K:
                pair_sum = max(pair_sum, A[right] + A[left])
                left += 1
            else:
                # pair sum is greater than K
                right -= 1
        return pair_sum


if __name__ == "__main__":
    sol = Solution()
    A = [34, 23, 1, 24, 75, 33, 54, 8]
    K = 60
    print(sol.twoSumLessThanK(A, K))
