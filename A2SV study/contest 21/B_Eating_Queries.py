t = int(input())

for _ in range(t):
    n, q = map(int, input().split())
    candies = list(map(int, input().split()))

    prefix_sum = [0] * (n + 1)
    for i in range(1, n + 1):
        prefix_sum[i] = prefix_sum[i - 1] + candies[i - 1]

    for _ in range(q):
        x = int(input())

        low = 0
        high = n
        ans = -1

        while low <= high:
            mid = (low + high) // 2
            sugar = prefix_sum[mid]
            if sugar >= x:
                ans = mid
                high = mid - 1
            else:
                low = mid + 1

        if ans == -1:
            print(-1)
        else:
            print(ans)
