n, k = map(int, input().split())
nums = list(map(int, input().split()))

for i in range(len(nums)):
    nums[i] = [nums[i], i]
def run(nums, n):
    if n == 0:
        return nums
    else:
        return run(check(nums), n - 1)
    
def check(nums):

    ans = []
    for i in range(0, len(nums) - 1, 2):
        if abs(nums[i][0] - nums[i + 1][0]) > k:
            ans.append(max(nums[i], nums[i + 1]))
        else:
            ans.append(nums[i])
            ans.append(nums[i + 1])
    if len(nums)%2 == 1:
        ans.append(nums[-1])
    return ans
temp = run(nums, n)
res = []
for num in temp:
    res.append(str(num[1] + 1))

print(" ".join(res))

