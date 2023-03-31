def recursive_dfs(graph, current_node, visited_nodes=[]):
    # Have we seen this node yet? Skip it if we have
    # and return the same visited nodes list that we got
    if current_node not in visited_nodes:
        # OK, we're here for the first time
        visited_nodes.append(current_node)
        if current_node not in graph:
            # Current node isn't a _key_ in graph (it has no
            # neighbors ∴ a leaf node): move on to the next branch
            return visited_nodes
        for neighbor in graph[current_node]:
            # Recurse into each 'neighbor'
            # Children for trees, but could loop back in a graph
            visited_nodes = recursive_dfs(graph, neighbor, visited_nodes)
    return visited_nodes


def main():
    graph = {
        "A": ["B", "C", "D"],
        "B": ["E"],
        "C": ["F", "G"],
        "D": ["H"],
        "E": ["I"],
        "F": ["J"],
    }
    path = recursive_dfs(graph, "A")
    print(" ".join(path))


if __name__ == "__main__":
    main()
