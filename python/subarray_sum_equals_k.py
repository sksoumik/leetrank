# https://leetcode.com/problems/subarray-sum-equals-k

# Given an array of integers nums and an integer k, return the total number of subarrays whose sum equals to k.
# A subarray is a contiguous non-empty sequence of elements within an array.
 

# Example 1:

# Input: nums = [1,1,1], k = 2
# Output: 2
# Example 2:

# Input: nums = [1,2,3], k = 3
# Output: 2

from typing import List

class Solution:
    # brute force approach: time O(n^2), space O(1)
    # time limit exceeded
    def subarraySum(self, nums: List[int], k: int) -> int:
        count = 0
        for i in range(len(nums)):
            for j in range(i, len(nums)):
                if sum(nums[i:j+1]) == k:
                    count += 1
        return count

    # time complexity: O(n)
    # space complexity: O(n)
    # vid: https://youtu.be/r1cwGocurtA
    def subarraySum2(self, nums: List[int], k: int) -> int:
        count = 0
        sums = 0
        d = {0: 1} # {running_sum: frequency}

        for num in nums:
            sums += num
            if sums - k in d:
                count += d[sums - k]
            # insert running sum into dictionary as key
            # and frequency 1 as value
            d[sums] = d.get(sums, 0) + 1

        return count


if __name__ == "__main__":
    nums = [1,1,1]
    k = 2
    print(Solution().subarraySum(nums, k))
    nums = [1,2,3]
    k = 3
    print(Solution().subarraySum(nums, k))
    nums = [1,1,1]
    k = 2
    print(Solution().subarraySum2(nums, k))
    