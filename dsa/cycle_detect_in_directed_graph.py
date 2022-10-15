# Return true if the directed graph contains a cycle, else return false.



def is_cyclic(graph):
    visited = [False] * len(graph)
    rec_stack = [False] * len(graph)
    for node in range(len(graph)):
        if is_cyclic_util(node, visited, rec_stack, graph):
            return True
    return False


def is_cyclic_util(node, visited, rec_stack, graph):
    visited[node] = True
    rec_stack[node] = True

    for neighbor in graph[node]:
        if not visited[neighbor]:
            if is_cyclic_util(neighbor, visited, rec_stack, graph):
                return True
        elif rec_stack[neighbor]:
            return True

    rec_stack[node] = False
    return False


# Driver code
if __name__ == "__main__":
    adj_list = {
        "A": ["C", "B"],
        "B": ["D"],
        "C": [],
        "D": ["A", "E"],
        "E": [],
    }

    print(is_cyclic(adj_list))
