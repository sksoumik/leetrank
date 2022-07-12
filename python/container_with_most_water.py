# https://leetcode.com/problems/container-with-most-water
# You are given an integer array height of length n. There are n vertical
# lines drawn such that the two endpoints of the ith line are (i, 0)
# and (i, height[i]).
# Find two lines that together with the x-axis form a container, such
# that the container contains the most water.
# Return the maximum amount of water a container can store.
# Notice that you may not slant the container.


# video explanation: https://youtu.be/Uj3gJjg6SXc

from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:
        max_area = 0
        left = 0
        right = len(height) - 1
        while left < right:
            # find the area of rectangle which is width * height
            # width is right - left
            # height is min(height[left], height[right]);
            # we have take the min height cause we don't want to slant the container
            area = min(height[left], height[right]) * (right - left)
            max_area = max(max_area, area)
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        return max_area
