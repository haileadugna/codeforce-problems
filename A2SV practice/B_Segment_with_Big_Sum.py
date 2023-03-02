n, s = map(int, input().split())

nums = list(map(int, input().split()))

left = 0
summ = 0
res = n
    
for i in range(n):
    summ += nums[i]
    while summ >= s:
        res = min(res, i - left + 1)
        summ -= nums[left]
        left += 1
        
if sum(nums) < s:
    res = -1   
print(res)
