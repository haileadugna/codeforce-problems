from collections import defaultdict, deque


test = int(input())

for _  in range(test):
    n, m  = map(int, input().split())
    graph = defaultdict(list)
    incoming = [0]*n 
    for i in range(m):
        a, b = map(int, input().split())
        graph[a].append(b)
        graph[b].append(a)
        # incoming[b -1] += 1


    todo = deque([])
    visit = set()
    x = 0
    y = 0
    for i in range(n):
        if len(graph[i+ 1]) == 1:
            todo.append(i + 1)
            visit.add(i + 1)
            y += 1
        # if len(graph[i+ 1]) == 3:
        #     x += 1

    while todo:
        nod = todo.popleft()
        for i in graph[nod]:
            if i not in visit:
                x += 1
                visit.add(i)
    # print(graph)
    print(x, y//x)
    # print(todo)