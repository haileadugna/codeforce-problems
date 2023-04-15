n = int(input())

nums = list(map(int, input().split()))

res = "NO"
for num in nums:
    if nums[nums[nums[num - 1] -1] - 1] == num:
        res = "YES"
        break
print(res)
