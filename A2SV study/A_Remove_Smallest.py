testcase = int(input())

for _ in range(testcase):
    lenght = int(input())
    nums = list(map(int, input().split()))

    nums.sort()
    ind = 0
    res = "YES"
    for i in range(lenght-1):
        if abs(nums[i+1] - nums[i]) <= 1:
            ind += 1
        else:
            res = "NO"

    if lenght - ind > 1:
        res = "NO"
    print(res)
