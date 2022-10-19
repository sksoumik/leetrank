# https://leetcode.com/problems/pascals-triangle

# Given an integer numRows, return the first numRows of Pascal's triangle.
# In Pascal's triangle, each number is the sum of the two numbers directly above it as shown:

# Input: numRows = 5
# Output: [[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]]

from typing import List


class Solution:
    # Time Complexity should be O(N^2)
    # Space Complexity should be O(N^2)
    def generate(self, numRows: int) -> List[List[int]]:
        output = [[1]]
        for r in range(1, numRows):
            row = [1]
            for c in range(1, r):
                row.append(output[r - 1][c - 1] + output[r - 1][c])
            row.append(1)
            output.append(row)
        return output


if __name__ == "__main__":
    numRows = 5
    print(Solution().generate(numRows))
