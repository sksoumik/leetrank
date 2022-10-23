# https://leetcode.com/problems/kth-smallest-element-in-a-sorted-matrix/

# Given an n x n matrix where each of the rows and columns is sorted in
# ascending order, return the kth smallest element in the matrix.
# Note that it is the kth smallest element in the sorted order, not the kth distinct element.
# You must find a solution with a memory complexity better than O(n2).


# Example 1:

# Input: matrix = [[1,5,9],[10,11,13],[12,13,15]], k = 8
# Output: 13
# Explanation: The elements in the matrix are [1,5,9,10,11,12,13,13,15],
# and the 8th smallest number is 13

from typing import List


class Solution:
    # pythonic way
    # time complexity: O(n^2)
    # space complexity: O(n^2)
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        # flatten the matrix
        flat_matrix = sum(matrix, [])
        # sort the matrix
        flat_matrix.sort()
        # return the kth smallest element
        return flat_matrix[k - 1]


if __name__ == "__main__":
    matrix = [[1, 5, 9], [10, 11, 13], [12, 13, 15]]
    k = 8
    print(Solution().kthSmallest(matrix, k))
