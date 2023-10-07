n, k = map(int, input().split())
arr = list(map(int, input().split()))

arr.sort()

sol = 0
cost = 0

start = 0
min_num = arr[start]

for end in range(1, n):
    cost += (arr[end] - arr[end - 1]) * (end - start)
    
    while cost > k:
        cost -= arr[end] - arr[start]
        start += 1
    
    if end - start + 1 >= sol:
        sol = end - start + 1
        min_num = arr[end]

print(sol, min_num)
