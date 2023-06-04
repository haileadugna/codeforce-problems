INF = 10**9  

n = int(input())
a = list(map(int, input().split()))

dp = [[INF]*3 for _ in range(n+1)]
dp[0][0] = 0

for i in range(1, n+1):
    if a[i-1] == 0 or a[i-1] == 1:
        dp[i][0] = dp[i-1][0] + 1
        dp[i][1] = dp[i][2] = INF
    elif a[i-1] == 2:
        dp[i][0] = min(dp[i-1][0], dp[i-1][1], dp[i-1][2]) + 1
        dp[i][1] = dp[i][2] = INF
    else:
        dp[i][0] = min(dp[i-1][0], dp[i-1][1], dp[i-1][2]) + 1
        dp[i][1] = min(dp[i-1][0], dp[i-1][2])
        dp[i][2] = min(dp[i-1][0], dp[i-1][1])
print(dp)
print(min(dp[n])) 