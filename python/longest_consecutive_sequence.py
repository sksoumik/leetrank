# https://leetcode.com/problems/longest-consecutive-sequence/description/

# Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.
# You must write an algorithm that runs in O(n) time.


# Example 1:

# Input: nums = [100,4,200,1,3,2]
# Output: 4
# Explanation: The longest consecutive elements sequence is [1, 2, 3, 4]. Therefore its length is 4.
# Example 2:

# Input: nums = [0,3,7,2,5,8,4,6,0,1]
# Output: 9

from typing import List


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # Create a set to store the elements in the array
        num_set = set(nums)
        longest_seq = 0

        # Iterate through the array
        for num in nums:
            # Check if this element is the start of a consecutive sequence
            if num - 1 not in num_set:
                # Find the length of the consecutive sequence starting from this element
                cur_seq = 1
                while num + cur_seq in num_set:
                    cur_seq += 1
                # Update the longest consecutive sequence length if necessary
                longest_seq = max(longest_seq, cur_seq)

        return longest_seq


if __name__ == "__main__":
    # Test the solution
    nums = [100, 4, 200, 1, 3, 2]
    print(Solution().longestConsecutive(nums))  # Output: 4

    nums = [0, 3, 7, 2, 5, 8, 4, 6, 0, 1]
    print(Solution().longestConsecutive(nums))  # Output: 9
