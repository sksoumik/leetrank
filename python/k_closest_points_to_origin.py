# https://leetcode.com/problems/k-closest-points-to-origin/

# Given an array of points where points[i] = [xi, yi] represents a point on
# the X-Y plane and an integer k, return the k closest points to the origin (0, 0).
# The distance between two points on the X-Y plane is the Euclidean distance (i.e., √(x1 - x2)2 + (y1 - y2)2).
# You may return the answer in any order. The answer is guaranteed to be unique (except for the order that it is in).

from typing import List

# import the heapq module
import heapq


class Solution:
    # time complexity: O(n log n)
    # brute force approach
    # n log n because of the sorting of the entire array
    def _kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        # sort the points by their distance from the origin
        points.sort(key=lambda point: point[0] ** 2 + point[1] ** 2)
        # return the first k points
        return points[:k]

    # time complexity: O(k log n)
    # heap approach
    # k log n because of the sorting of the first k elements
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:

        # mean heap
        min_heap = []

        # traverse the points
        for x, y in points:
            # calculate the distance, we don't need to calculate the square root
            # because we are only comparing the distances
            distance = (x**2) + (y**2)
            # push the distance with its coordinate to the meanheap
            min_heap.append([distance, x, y])

        # sort the heap
        heapq.heapify(min_heap)

        # create a list to store the k closest points
        k_closest_points = []
        while k > 0:
            dist, x, y = heapq.heappop(min_heap)
            k_closest_points.append([x, y])
            k -= 1

        return k_closest_points


if __name__ == "__main__":
    solution = Solution()
    print(solution.kClosest(points=[[1, 3], [-2, 2]], k=1))
    print(solution.kClosest(points=[[3, 3], [5, -1], [-2, 4]], k=2))
