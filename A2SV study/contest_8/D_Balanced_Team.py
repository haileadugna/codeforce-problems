n = int(input())

nums = list(map(int, input().split()))

nums.sort()

left = 0
right = 0
res = 0

cnt = 1
while right < n :
    diff = nums[right] - nums[left]
    if left == right:
        right += 1
        cnt = 1
    elif diff <= 5 :
        right += 1
        cnt += 1
    else:
        res = max(res, cnt)
        left += 1
        cnt -= 1

print(max(res, cnt))
