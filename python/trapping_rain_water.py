# https://leetcode.com/problems/trapping-rain-water

# Given n non-negative integers representing an elevation map where the width of each bar is 1,
# compute how much water it can trap after raining.


# Example 1:

# Input: height = [0,1,0,2,1,0,1,3,2,1,2,1]
# Output: 6
# Explanation: The above elevation map (black section) is represented by array
#  [0,1,0,2,1,0,1,3,2,1,2,1]. In this case, 6 units of rain water (blue section) are being trapped.


# vid: https://youtu.be/ZI2z5pq0TqA

from typing import List


class Solution:
    # got TLE
    # time complexity: O(n)
    # space complexity: O(n)
    def _trap(self, height: List[int]) -> int:
        output = 0
        for i in range(1, len(height) - 1):
            left = max(height[:i])
            right = max(height[i + 1 :])
            if min(left, right) - height[i] >= 0:
                output += min(left, right) - height[i]
        return output

    # two pointer
    # time complexity: O(n)
    # Solution complexity: O(1)
    def trap(self, height: List[int]) -> int:
        output = 0
        left, right = 0, len(height) - 1
        left_max, right_max = 0, 0
        while left < right:
            # If height[left] < height[right], it means the water level is based on the
            # left side (the left bar is smaller) then move left side:
            if height[left] < height[right]:
                # we can't trap water If leftmax - height[left] < 0 means negative
                # so, we just shift the left pointer without updating the output
                if left_max - height[left] < 0:
                    left_max = height[left]
                else:
                    # it can trap an amount of water
                    output += left_max - height[left]
                left += 1
            else:
                # we can't trap water If right_max - height[right] < 0 means negative
                # so, we just shift the right pointer without updating the output
                if right_max - height[right] < 0:
                    right_max = height[right]
                else:
                    # it can trap an amount of water
                    output += right_max - height[right]
                right -= 1
        return output


if __name__ == "__main__":
    height = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
    print(Solution().trap(height))  # 6
