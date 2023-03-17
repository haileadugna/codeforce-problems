n, m = map(int, input().split())

nums = []
for i in range(m):
    nums.append(list(map(int, input().split())))
res = [0] * (n + 1)
for num in nums:
    res[num[0]] += 1
    res[num[1] + 1] -= 1

for i in range(1, n):
    res[i] += res[i - 1]
    
ans = "NO"
for i in range(len(res) - 1):
    if i < n and 0 == res[i]:
        ans = "YES"
        break

print(ans)