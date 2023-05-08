test = int(input())

for _ in range(test):
    n = int(input())
    nums = list(map(int, input().split()))

    res = 0
    l , r = 0, 0
    while r < n:
        if nums[r] == 1:
            r += 1

        else:
            l = r
            while r < n and nums[r] == 0:
                r += 1

            res = max(res, r - l)


    print(res)
