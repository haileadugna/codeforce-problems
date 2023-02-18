n = int(input())
nums = list(map(int, input().split()))

pos = []
neg = []
for i in range(n):
    if nums[i] < 0:
        neg.append(nums[i])
    else:
        pos.append(nums[i])
    
count = 0
for j in range(len(neg)):
    count += abs(neg[j] + 1)
for k in range(len(pos)):
    count += abs(pos[k] -1)
if len(neg) % 2 != 0:
    if len(pos) != 0:
        if abs(max(neg) -1) > abs(min(pos)-1):
            count += abs(min(pos)-1) +2
        else:
            count += abs(max(neg) -1) +2
    else:
        count += abs(max(neg) -1)
print(count)



