
test = int(input())

for _ in range(test):
    n = int(input())
    nums = list(map(int, input().split()))

    if len(set(nums)) == 1:
        print('NO')
        continue

    summ = nums[0]
    temp = True
    for i in range(1, n):
        if summ == nums[i]:
            temp = False
            break
        else:
            summ += nums[i]


    if temp:
        print('YES')
        print(*nums)

    else:
        print("YES")
        nums.sort(reverse=True)

        if n > 2 and nums[0] == nums[1]:
            nums[1], nums[-1] = nums[-1], nums[1]

        print(*nums)

