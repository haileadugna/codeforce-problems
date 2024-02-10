

n = int(input())
arr = list(map(int, input().split()))
arr = [(arr[i], i) for i in range(n)]
arr.sort()
ans = 0
time = 0
for i in range(n):
    if time <= arr[i][0]:
        time += arr[i][0]
        ans += 1
print(ans)

