test = int(input())

for _ in range(test):
    n = int(input())

    nums = list(map(int, input().split()))
    temp = []
    count = 0
    for num in nums:
        while num % 2 == 0:
            count += 1
            num = num//2
        temp.append(num)

    res = sum(temp) - max(temp) + (max(temp)* 2**count)
    print(res)
