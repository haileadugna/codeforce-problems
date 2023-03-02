test_cases = int(input())

for _ in range(test_cases):
    n = int(input())
    nums = list(map(int, input().split()))
    res = 0
    temp = nums[0]
    if nums[0] > 0:
        flag = True
    else:
        flag = False

    for i in range(1, n):
        if (nums[i] > 0) == flag:
            temp = max(temp, nums[i])
        else:
            res += temp
            temp = nums[i]
            flag = not flag
    res += temp
    print(res)
