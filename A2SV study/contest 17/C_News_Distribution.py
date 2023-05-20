# from collections import defaultdict, deque
# n, m = map(int, input().split())


# graph = defaultdict(list)
# for i in range(m):
#     temp = list(map(int, input().split()))[1:]
#     for j in temp:
#         graph[j].extend(filter(lambda x: x != j, temp))


# res = [1] * n
# visited = [False] * n
# for i in range(n):
#     if not visited[i]:
#         todo = deque([i+1])
#         visit = set()
#         while todo:
#             node = todo.popleft()
#             if not visited[node-1]:
#                 visit.add(node)
#                 visited[node-1] = True
#                 todo.extend(graph[node])
#         for j in visit:
#             res[j-1] = len(visit)

# print(*res)

class UnionFind:
    def __init__(self, n):
        # initialize parent list and rank list
        self.parent = list(range(n))
        self.rank = [0] * n

    def find(self, x):
        # find the root of x and compress the path
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        # union the set containing x and the set containing y
        x_root = self.find(x)
        y_root = self.find(y)
        if x_root == y_root:
            return
        if self.rank[x_root] < self.rank[y_root]:
            self.parent[x_root] = y_root
        elif self.rank[x_root] > self.rank[y_root]:
            self.parent[y_root] = x_root
        else:
            self.parent[y_root] = x_root
            self.rank[x_root] += 1