
s = input()
n = len(s)
arr = [0]*n
for i in range(1, n):
    arr[i] = arr[i-1] + (s[i] == s[i-1])
m = int(input())
for _ in range(m):
    l, r = map(int, input().split())
    print(arr[r-1] - arr[l-1])
# optimized solution