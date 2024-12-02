def count_closed_figures(segments):
    # Step 1: Create a graph where each point (x, y) is a unique node.
    graph = {}
    for segment in segments:
        x1, y1, x2, y2 = segment
        if (x1, y1) not in graph:
            graph[(x1, y1)] = []
        if (x2, y2) not in graph:
            graph[(x2, y2)] = []
        
        # Add edges in both directions as it's an undirected graph.
        graph[(x1, y1)].append((x2, y2))
        graph[(x2, y2)].append((x1, y1))

    # Step 2: Count cycles (closed figures) using DFS/BFS.
    visited = set()
    closed_figures_count = 0
    
    def dfs(node, parent, path):
        # Detect cycle if we revisit a node that is in the current path but is not the parent.
        if node in visited:
            if node in path:
                # A cycle is found.
                return True
            return False

        visited.add(node)
        path.add(node)
        
        # Traverse neighbors
        cycle_found = False
        for neighbor in graph[node]:
            if neighbor == parent:
                continue
            if dfs(neighbor, node, path):
                cycle_found = True
        
        path.remove(node)
        return cycle_found

    # Iterate over all nodes in the graph and apply DFS to count unique cycles.
    for node in graph:
        if node not in visited:
            if dfs(node, None, set()):
                closed_figures_count += 1

    return closed_figures_count

# Input handling
n = int(input().strip())
segments = []
for _ in range(n):
    x1, y1, x2, y2 = map(int, input().strip().split())
    segments.append((x1, y1, x2, y2))

# Output the result
print(count_closed_figures(segments))