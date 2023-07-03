from collections import defaultdict

def find_vertex_cover(n, edges):
    adj_list = defaultdict(set)
    for u, v in edges:
        adj_list[u].add(v)
        adj_list[v].add(u)
    
    visited = [False] * (n+1)
    set_a, set_b = set(), set()
    
    for u in range(1, n+1):
        if not visited[u]:
            set_a.add(u)
            visited[u] = True
            for v in adj_list[u]:
                set_b.add(v)
                visited[v] = True
    
    for u in range(1, n+1):
        if not visited[u]:
            if u in set_a:
                for v in adj_list[u]:
                    if v in set_a:
                        return -1
                    set_b.add(v)
            else:
                for v in adj_list[u]:
                    if v in set_b:
                        return -1
                    set_a.add(v)
    
    return [len(set_a), sorted(list(set_a))], [len(set_b), sorted(list(set_b))]

n, m = map(int, input().split())
edges = [tuple(map(int, input().split())) for _ in range(m)]

result = find_vertex_cover(n, edges)

if result == -1:
    print("-1")
else:
    print(result[0][0])
    print(" ".join(map(str, result[0][1])))
    print(result[1][0])
    print(" ".join(map(str, result[1][1])))