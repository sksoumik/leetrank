# https://leetcode.com/problems/two-sum-ii-input-array-is-sorted

# Given a 1-indexed array of integers numbers that is already sorted in non-decreasing order,
# find two numbers such that they add up to a specific target number.
# Let these two numbers be numbers[index1] and numbers[index2] where 1 <= index1 < index2 <= numbers.length.

# Return the indices of the two numbers, index1 and index2, added by one as an integer array [index1, index2] of length 2.
# The tests are generated such that there is exactly one solution. You may not use the same element twice.
# Your solution must use only constant extra space.

from typing import List


class Solution:
    # O(n) time
    # space: O(1)
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        """
        We start with two pointers, one at the beginning of the array and one at the end.
        If the sum of the two numbers at the pointers is equal to the target, we return the pointers.
        If the sum is less than the target, we move the left pointer up.

        If the sum is greater than the target, we move the right pointer down.

        We keep doing this until the pointers cross.

        If the pointers never cross, then we didn't find a pair that sums to the target

        :param numbers: the list of numbers
        :type numbers: List[int]
        :param target: the target number we're trying to find
        :type target: int
        :return: The indices of the two numbers such that they add up to a specific target.
        """
        left = 0
        right = len(numbers) - 1

        while left < right:
            if numbers[left] + numbers[right] == target:
                # add +1, cause the array is 1-indexed
                return [left + 1, right + 1]

            elif numbers[left] + numbers[right] < target:
                left += 1
            else:
                right -= 1
        return []

    # O(n): same as the two sum except it's 1-indexed
    # space: O(n)
    def twoSum_2(self, numbers: List[int], target: int) -> List[int]:
        hash_table = {}
        
        for idx, num in enumerate(numbers):
            comp = target - num
            
            if comp in hash_table:
                return [hash_table[comp] + 1, idx+1]
            
            hash_table[num] = idx

            


if __name__ == "__main__":
    numbers = [2, 7, 11, 15]
    target = 9
    print(Solution().twoSum(numbers, target))
    numbers = [3, 2, 4]
    target = 6
    print(Solution().twoSum(numbers, target))
    