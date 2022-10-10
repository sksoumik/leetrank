# https://leetcode.com/problems/jump-game-iii/

# Given an array of non-negative integers arr,
# you are initially positioned at start index of the array.
# When you are at index i, you can jump to i + arr[i] or i - arr[i], check if you can reach to any index with value 0.

# Notice that you can not jump outside of the array at any time.


# Example 1:

# Input: arr = [4,2,3,0,3,1,2], start = 5
# Output: true
# Explanation:
# All possible ways to reach at index 3 with value 0 are:
# index 5 -> index 4 -> index 1 -> index 3
# index 5 -> index 6 -> index 4 -> index 1 -> index 3

# vid: https://youtu.be/GFayd7xOLXg

from typing import List
from functools import lru_cache


class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:
        @lru_cache(None)
        def dfs(idx):
            if idx < 0 or idx >= len(arr) or arr[idx] < 0:
                return False

            if arr[idx] == 0:
                return True

            # before calling a recursive call we make data to negative,
            # so while backtracking we change data back to original
            # like change 1 to -1 then -1 to 1 again
            arr[idx] = -arr[idx]
            return dfs(idx + arr[idx]) or dfs(idx - arr[idx])

        return dfs(start)
