n, k = map(int, input().split())
nums= list(map(int, input().split()))
nums.sort()
if k == 0:
    ans = nums[0] - 1
else:
    ans = nums[k -1]

cnt = 0
for i in range(len(nums)):
    if nums[i] <= ans:
        cnt += 1

if cnt != k or not (1 <= ans and ans <= 1000**3):
    ans = -1
print(ans)

