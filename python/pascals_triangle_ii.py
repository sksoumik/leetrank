# https://leetcode.com/problems/pascals-triangle-ii

# Given an integer rowIndex, return the rowIndexth (0-indexed) row of the Pascal's triangle.
# In Pascal's triangle, each number is the sum of the two numbers directly above it as shown:

# Example 1:
# Input: rowIndex = 3
# Output: [1,3,3,1]

from typing import List


class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        output = [[1]]
        for r in range(1, rowIndex + 1):
            row = [1]
            for c in range(1, r):
                row.append(output[r - 1][c - 1] + output[r - 1][c])
            row.append(1)
            output.append(row)
        return output[rowIndex]


if __name__ == "__main__":
    rowIndex = 3
    print(Solution().getRow(rowIndex))  # [1, 3, 3, 1]
