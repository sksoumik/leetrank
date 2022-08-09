# https://leetcode.com/problems/course-schedule/

# There are a total of numCourses courses you have to take, labeled from 0 to numCourses - 1.
# You are given an array prerequisites where prerequisites[i] = [ai, bi] indicates that you must
# take course bi first if you want to take course ai.

# For example, the pair [0, 1], indicates that to take course 0 you have to first take course 1.
# Return true if you can finish all courses. Otherwise, return false.

# Example 1:

# Input: numCourses = 2, prerequisites = [[1,0]]
# Output: true
# Explanation: There are a total of 2 courses to take.
# To take course 1 you should have finished course 0. So it is possible.

from typing import List


class Solution:
    # video explanation: https://youtu.be/EgI5nU9etnU
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # define a adjacency list to represent the graph and store the prerequisites
        # put empty list for each node initially
        adj_map = {i: [] for i in range(numCourses)}

        # add the prerequisites to the adjacency list
        for course, pre_req in prerequisites:
            # add course as key and pre_req as value
            adj_map[course].append(pre_req)

        # track the visited nodes to check if there is a cycle
        visited = set()

        # apply dfs to determine if there is a cycle
        # v: course, adj_map: adjacency list
        def hasCycle(v, stack):
            # if the node is already visited, return true
            if v in visited:
                if v in stack:
                    return True
                return False

            # mark the node as visited
            visited.add(v)
            # add the node to the stack
            stack.append(v)

            # check if there is a cycle in the graph
            # check for all values in the adjacency list of the node
            for pre_req in adj_map[v]:
                if hasCycle(pre_req, stack):
                    return True

            # remove the node from the stack
            stack.pop()
            return False

        # check if there is a cycle in the graph
        for v in range(numCourses):
            if hasCycle(v, []):
                return False

        return True


if __name__ == "__main__":
    s = Solution()
    print(s.canFinish(2, [[1, 0]]))
    print(s.canFinish(2, [[1, 0], [0, 1]]))
