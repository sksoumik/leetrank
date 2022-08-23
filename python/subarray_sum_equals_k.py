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

    
    # solution 2: time O(n), space O(n)
    # First of all, the basic idea behind this code is that, whenever sums has 
    # increased by a value of k, we've found a subarray of sums=k.
    # I'll also explain why we need to initialise 0 in the hashmap.
    # Example: Let's say our elements are [1,2,1,3] and k = 3.
    # and our corresponding running sums = [1,3,4,7]
    # Now, if you notice the running sums array, from 1->4, there is increase of k and from 4->7, 
    # there is an increase of k. So, we've found 2 subarrays of sums=k.

    # But, if you look at the original array, there are 3 subarrays of sums==k. 
    # Now, you'll understand why 0 comes in the picture.

    # In the above example, 4-1=k and 7-4=k. Hence, we concluded that there are 2 subarrays.
    # However, if sums==k, it should've been 3-0=k. But 0 is not present in the array. 
    # To account for this case, we include the 0.
    # Now the modified sums array will look like [0,1,3,4,7]. Now, try to see for the increase of k.

    # 0->3
    # 1->4
    # 4->7
    # Hence, 3 sub arrays of sums=k

    def subarraySum2(self, nums: List[int], k: int) -> int:

        count = 0
        sums = 0
        running_sum = dict()
        running_sum[0] = 1

        for num in nums:
            sums += num
            count += running_sum.get(sums - k, 0)
            running_sum[sums] = running_sum.get(sums, 0) + 1
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
    