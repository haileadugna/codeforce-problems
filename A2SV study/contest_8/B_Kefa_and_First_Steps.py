
n = int(input())

nums = list(map(int, input().split()))

left = 0
res = 1
cnt = 1
for i in range(1, n):
    if nums[i-1] > nums[i]:
        res = max(res, cnt)
        cnt = 1

    else:
        cnt += 1

print(max(res, cnt))

