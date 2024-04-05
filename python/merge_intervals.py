# https://leetcode.com/problems/merge-intervals/

# Given an array of intervals where intervals[i] = [starti, endi], merge all overlapping intervals,
# and return an array of the non-overlapping intervals that cover all the intervals in the input.


# Example 1:

# Input: intervals = [[1,3],[2,6],[8,10],[15,18]]
# Output: [[1,6],[8,10],[15,18]]
# Explanation: Since intervals [1,3] and [2,6] overlap, merge them into [1,6].

from typing import List


class Solution:
    # go through the intervals sorted by start coordinate and either combine the current
    # interval with the previous one if they overlap, or add it to the output by itself if they don't.
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # sort by start coordinate of intervals
        intervals.sort(key=lambda x: x[0])
        output = [intervals[0]]
        for i in range(1, len(intervals)):
            # intervals[i][0]  means the start/first coordinate of the current array
            # output[-1][1] means the end/last coordinate of the last array in the output
            if intervals[i][0] <= output[-1][1]:
                # intervals[i][1]  means the end/last/second coordinate of the current array
                output[-1][1] = max(output[-1][1], intervals[i][1])
            else:
                output.append(intervals[i])
        return output


if __name__ == "__main__":
    intervals = [[1, 3], [2, 6], [8, 10], [15, 18]]
    sol = Solution()
    print(sol.merge(intervals))
