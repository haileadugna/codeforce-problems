n, p = map(int, input().split())
nums = list(map(int, input().split()))

left = 0
summ = 0
res = 0
prev = float("inf")
count = 100000000

for i in range(n):
    cnt = 0
    while summ < p:
        summ += nums[left % n]
        left += 1
        cnt += 1
    
    dist = i - (left % n) + 1
    if dist < prev:
        prev = dist
        ans = i
    count = min(cnt, count)
    summ -= nums[i]
    # res = min(res, i - (left % n) + 1)

print(ans, count)
