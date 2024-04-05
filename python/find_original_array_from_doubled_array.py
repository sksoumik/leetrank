# https://leetcode.com/problems/find-original-array-from-doubled-array

# An integer array original is transformed into a doubled array changed by appending twice the
# value of every element in original, and then randomly shuffling the resulting array.

# Given an array changed, return original if changed is a doubled array.
# If changed is not a doubled array, return an empty array.
# The elements in original may be returned in any order.


# Example 1:

# Input: changed = [1,3,4,2,6,8]
# Output: [1,3,4]
# Explanation: One possible original array could be [1,3,4]:
# - Twice the value of 1 is 1 * 2 = 2.
# - Twice the value of 3 is 3 * 2 = 6.
# - Twice the value of 4 is 4 * 2 = 8.
# Other original arrays could be [4,3,1] or [3,1,4].

from collections import Counter
from typing import List


class Solution:
    # time complexity: O(n log n)
    # space complexity: O(n)
    # video explanation: https://youtu.be/z40B-Mr9_qk
    def findOriginalArray(self, changed: List[int]) -> List[int]:
        if len(changed) % 2 != 0:
            return []

        changed.sort()
        original = []

        count = Counter(changed)

        for num in changed:
            if count[num] == 0:
                continue

            if count[num * 2] == 0:
                return []

            count[num] -= 1
            count[num * 2] -= 1
            original.append(num)

        return original


if __name__ == "__main__":
    print(Solution().findOriginalArray([1, 3, 4, 2, 6, 8]))
    print(Solution().findOriginalArray([6, 3, 0, 1]))
    print(Solution().findOriginalArray([1, 1, 1, 1, 1, 1]))
    print(Solution().findOriginalArray([1, 1, 1, 1, 1, 1, 1]))
