from collections import defaultdict, deque
from sys import stdin, stdout


n, m = map(int, stdin.readline().split())


graph = defaultdict(list)
edges = []
for _ in range(m):
   u, v = map(int, stdin.readline().split())
   edges.append((u, v))
   graph[u].append(v)
   graph[v].append(u)


colors = defaultdict(lambda: -1)
colors[1] = 0


queue = deque([1])
while queue:
   n = queue.popleft()


   for nei in graph[n]:
       if colors[nei] == -1:
           colors[nei] = 1 - colors[n]
           queue.append(nei)
       elif colors[nei] == colors[n]:
           print("NO")
           exit()


print("YES")
for (u, v) in edges:
   if colors[u] == 0:
       print(1, end="")
   else:
       print(0, end="")


print()