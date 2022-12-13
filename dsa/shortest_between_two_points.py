def shortest_path_top_down(graph, start, end):
    # Store the solutions to the subproblems in a memo
    memo = {}

    # Define a recursive function to compute the shortest path between two points on a map
    def shortest_path_recursive(current):
    # If the current position is the end position, return 0
        if current == end:
            return 0

        # If the current position has already been visited, return the stored solution
        if current in memo:
            return memo[current]

        # Set the minimum path length to infinity
        min_path_length = float("inf")

        # Iterate over the adjacent positions
        for next_pos in graph[current]:
        # Compute the shortest path to the next position using the recursive solution
            path_length = 1 + shortest_path_recursive(next_pos)

            # Update the minimum path length
            min_path_length = min(min_path_length, path_length)

        # Store the minimum path length in the memo
        memo[current] = min_path_length

        # Return the minimum path length
        return min_path_length

  # Call the recursive function to compute the shortest path between the start and end points
    return shortest_path_recursive(start)


if __name__ == "__main__":
    # Define the map
    map = {
      "A": ["B", "C"],
      "B": ["D", "E"],
      "C": ["F"],
      "D": [],
      "E": ["F"],
      "F": []
    }

    # Define the start and end points
    start = "A"
    end = "F"

    # Compute the shortest path between the start and end points
    shortest_path_length = shortest_path_top_down(map, start, end)

    # Print the shortest path length
    print(shortest_path_length)  #
