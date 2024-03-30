n = int(input())
arr = list(map(int, input().split()))

for i in range(n):
    while arr[i] % 2 == 0:
        arr[i] = arr[i] // 2
    while arr[i] % 3 == 0:
        arr[i] = arr[i] // 3

if len(set(arr)) == 1:
    print('Yes')
else:
    print('No')