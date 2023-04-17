# n = int(input())

# # Read in the immediate manager for each employee
# managers = [int(x) for x in input().split()]

# # Create adjacency list to represent the hierarchy
# adj_list = [[] for _ in range(n+1)]
# for i in range(1, n+1):
#     if managers[i-1] != -1:
#         adj_list[managers[i-1]].append(i)


def dfs(node, graph, visited):
    """
    Performs a DFS traversal of the graph starting from the given node.
    Returns a set of all visited nodes.
    """
    visited.add(node)
    for neighbor in graph[node]:
        if neighbor not in visited:
            dfs(neighbor, graph, visited)

n = int(input())
managers = list(map(int, input().split()))

# Build the graph
graph = {i: [] for i in range(n)}
for i, manager in enumerate(managers):
    if manager != -1:
        graph[manager-1].append(i)

# Perform DFS starting from each root node and assign employees to groups
groups = 0
visited = set()
for i in range(n):
    if i not in visited and managers[i-1] == -1:
        dfs(i, graph, visited)
        groups += 1

print(groups)