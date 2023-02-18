n = int(input())
nums = input().split()
res = []

for i in range(n):

    start = i
    right = i + 1
    pev = nums[start]
    ind = start
    while right < n:
        if nums[right] < pev:
            pev = nums[right]
            ind = right
        right += 1
    if start != ind:
        nums[start], nums[ind] = nums[ind], nums[start]
        res.append([start, ind])
print(len(res))
for num in res:
    print(num[0], num[1])
