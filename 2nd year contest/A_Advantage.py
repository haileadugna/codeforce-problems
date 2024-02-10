n = int(input())
for _ in range(n):
    l = int(input())
    arr = list(map(int, input().split()))

    max_num = arr[0]
    temp = sorted(arr)
    ind = 0
    for i in range(1, l):
        if arr[i] > max_num:
            max_num = arr[i]
            ind = i
    res = []
    for i in range(l):
        if i != ind:
            res.append(arr[i] - max_num)
        else:
            res.append(arr[i] - temp[-2])

    print(*res)