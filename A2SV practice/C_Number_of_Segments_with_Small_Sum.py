n, s = map(int, input().split())

nums = list(map(int, input().split()))

left = 0
summ = 0
res = 0
for i in range(n):
    summ += nums[i]
    while summ > s:
        summ -= nums[left]
        left += 1
    res += (i - left + 1)

print(res)
