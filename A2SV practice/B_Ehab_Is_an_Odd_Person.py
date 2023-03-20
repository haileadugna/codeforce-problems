n = int(input())
nums = list(map(int, input().split()))
temp = nums[:]
nums.sort()
cnt = 0
t = 0
for i in range(n):
    if int(nums[i]) % 2 == 1:
        cnt += 1
    else:
        t += 1
if cnt != 0 and t != 0:
    print(" ".join(map(str,nums)))
else:
    print(" ".join(map(str, temp)))
    