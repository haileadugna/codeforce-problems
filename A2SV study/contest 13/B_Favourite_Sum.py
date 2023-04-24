test = int(input())

for _ in range(test):

    n, m = map(int, input().split())
    nums = list(map(int, input().split()))

    temp = (m**2 + m)//2
    # print(nums)
    for i in nums:
        if i <= m:
            temp -= i * 2

    print(temp)