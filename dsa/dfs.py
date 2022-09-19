# depth first search dfs traversal of a graph

# 1. Pick any node. If it is unvisited, mark it as visited and recur on all its adjacent nodes.
# 2. Repeat until all the nodes are visited, or the node to be searched is found.


# https://www.educative.io/answers/how-to-implement-depth-first-search-in-python
def dfs(visited, graph, node):
    # visited is a set
    # graph is a dictionary
    # node is a string, starting node
    if node not in visited:
        print(node)
        visited.add(node)
        for neighbour in graph[node]:
            dfs(visited, graph, neighbour)


if __name__ == "__main__":
    graph = {
        "A": ["B", "C"],
        "B": ["D", "E"],
        "C": ["F"],
        "D": [],
        "E": ["F"],
        "F": [],
    }
    visited = set()
    dfs(visited, graph, "A")
