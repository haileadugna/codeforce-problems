n = int(input())

graph_start = []
graph_end = []
for i in range(n):
    temp = list(map(int, input().split()))

    for j in range(n):
        if temp[j] == 1:
            graph_start.append(i+1)
            graph_end.append(j + 1)

res_sources = []
for i in range(1, n + 1):
    if i not in graph_start:
        res_sources.append(i)
res_sinks = []
for i in range(1, n + 1):
    if i not in graph_end:
        res_sinks.append(i)
        
print(len(res_sinks), *res_sinks)
print(len(res_sources), *res_sources)