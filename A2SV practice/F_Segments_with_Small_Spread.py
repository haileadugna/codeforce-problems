n, k = map(int, input().split())

nums = list(map(int, input().split()))

left = 0
maxx = nums[0]
minn = nums[0]
res = 0
for i in range(n):
    maxx = max(maxx, nums[i])

    while (maxx - minn ) > k:
        
        minn = nums[left]
        left += 1

    res += ( i - left + 1)  

print(res)
