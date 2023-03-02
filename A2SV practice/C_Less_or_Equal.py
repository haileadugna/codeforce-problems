n, k = map(int, input().split())
nums= list(map(int, input().split()))

nums.sort()
res = -1
if k == n  :
    res = max(nums)
elif nums[k-1] != nums[k]:
    res = nums[k - 1] 
print(res)
# for i in range(k):
