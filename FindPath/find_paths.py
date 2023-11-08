from typing import Any, Dict, List, Optional, Tuple, Union


def find_paths(connection: List[List[int]], source: int, destination: int) -> List[List[int]]:
    # Create a dictionary to represent the graph
    graph = {}
    for u, v in connection:
        if u not in graph:
            graph[u] = []
        graph[u].append(v)

    # Initialize a list to store all the paths
    all_paths = []

    # Define a DFS function
    def dfs(current_vertex, destination_vertex, graph, path, all_paths):
        # If the current vertex is the destination vertex, append the current path to the list of all paths
        if current_vertex == destination_vertex:
            all_paths.append(path)
        # Otherwise, for each neighbor of the current vertex, if it has not been visited before, append it to the current path and call the DFS function recursively
        else:
            for neighbor in graph.get(current_vertex, []):
                if neighbor not in path:
                    dfs(neighbor, destination_vertex,
                        graph, path + [neighbor], all_paths)

    # Call the DFS function with the source vertex and an empty path
    dfs(source, destination, graph, [source], all_paths)

    # Return the list of all paths
    return all_paths
