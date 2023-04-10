from collections import defaultdict
n = int(input())

graph = defaultdict(list)
for i in range(n):
    temp = list(map(int, input().split()))
    for j in range(n):
        if temp[j] == 1:
            graph[i + 1].append(j + 1)

for i in list(graph.keys()):
        
    print(len(graph[i]), *graph[i])