# https://leetcode.com/problems/all-paths-from-source-to-target

# Given a directed acyclic graph (DAG) of n nodes labeled from 0 to n - 1, 
# find all possible paths from node 0 to node n - 1 and return them in any order.

# The graph is given as follows: graph[i] is a list of all nodes you 
# can visit from node i (i.e., there is a directed edge from node i to node graph[i][j]).

from typing import List

class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        end_node = len(graph) - 1
        paths = []
        def dfs(node, path):
            if node == end_node:
                paths.append(path)
            for next_node in graph[node]:
                dfs(next_node, path + [next_node])
        
        dfs(0, [0])
        return paths




if __name__ == "__main__":
    graph = [[1,2], [3], [3], []]
    print(Solution().allPathsSourceTarget(graph))
    