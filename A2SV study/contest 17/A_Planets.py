from collections import defaultdict


t = int(input())

for _ in range(t):
    n, c = map(int, input().split())
    orbits = list(map(int, input().split()))
    graph = defaultdict(int)
    
    for orbit in orbits:
        graph[orbit] += 1

    res = 0
    temp = list(set(orbits))
    for t in temp:
        if graph[t] >= c:
            res += c
        else:
            res += graph[t]

    print(res)
    
