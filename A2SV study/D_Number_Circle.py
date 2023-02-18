n = int(input())
arr = list(map(int, input().split()))

arr.sort()
if arr[-1] < arr[-2] + arr[-3]:
    print("YES")
    temp = arr.pop()
    arr.insert(0, arr.pop())
    arr.insert(0, temp)
    print(" ".join(map(str,arr)))
else:
    print("NO")