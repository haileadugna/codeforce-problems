def dfs(v, parent, count, cats, graph):
    if count > cats:
        return 0
    leaf = True  
    num_res = 0
    
    for neig in graph[v]:
        if neig != parent:
            leaf = False
            num_res += dfs(neig, v, count * graph[v][neig] + graph[neig][v], cats, graph)
    
    return num_res + leaf

n, m = map(int, input().split())
cats = [0] + list(map(int, input().split()))
graph = {i: {} for i in range(1, n + 1)}

for _ in range(n - 1):
    a, b = map(int, input().split())
    graph[a][b] = cats[b]
    graph[b][a] = cats[a]

res = dfs(1, -1, cats[1], m, graph)
print(res)
