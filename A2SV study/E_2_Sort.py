t = int(input())
for _ in range(t):
    n,k = map(int, input().split())
    arr = list(map(int, input().split()))

    left = 0
    right = 1
    count = 0
    while right < n:
        if arr[right-1] < arr[right] * 2:
            if right - left == k:
                count += 1
                left += 1
                right += 1
            else:
                right += 1
        else:
            left = right
            right += 1
    print(count)
