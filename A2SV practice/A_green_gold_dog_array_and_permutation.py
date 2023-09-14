test = int(input())

for _ in range(test):
    n = int(input())
    arr = list(map(int, input().split()))
    
    res = []
    for i in range(n):
        res.append(i + 1)

    print(*res)