# breadth first search bfs traversal of a graph

# 1. Pick any node, visit the adjacent unvisited vertex, mark it as visited, display it, and insert it in a queue.
# 2. If there are no remaining adjacent vertices left, remove the first vertex from the queue.
# 3. Repeat step 1 and step 2 until the queue is empty or the desired node is found.

# In queue, add elements to the right and remove from the leftmost side (pop(0))


def bfs(visited, graph, node, queue=[]):
    # visited is a set
    # graph is a dictionary
    # node is a string, starting node
    # queue is a list
    visited.add(node)
    queue.append(node)
    while queue:
        # remove leftmost element from queue
        s = queue.pop(0)
        print(s)
        # while removing the node from the queue, add its adjacent nodes to the queue
        for neighbour in graph[s]:
            if neighbour not in visited:
                visited.add(neighbour)
                queue.append(neighbour)


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
    bfs(visited, graph, "A")
