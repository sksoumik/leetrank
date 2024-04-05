# https://leetcode.com/problems/find-center-of-star-graph

# There is an undirected star graph consisting of n nodes labeled from 1 to n.
# A star graph is a graph where there is one center node
# and exactly n - 1 edges that connect the center node with every other node.
# You are given a 2D integer array edges where each edges[i] = [ui, vi] indicates
# that there is an edge between the nodes ui and vi. Return the center of the given star graph.
from typing import List


class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        # we can consider this problem to be a non-graph problem
        # just getting the common element in all lists solves the problem.

        common_elements = set.intersection(*map(set, edges))
        # removes a top element from the set and returns it
        return common_elements.pop()


if __name__ == "__main__":
    edges = [[1, 2], [2, 3], [4, 2]]
    print(Solution().findCenter(edges))
    edges = [[1, 2], [5, 1], [1, 3], [1, 4]]
    print(Solution().findCenter(edges))
