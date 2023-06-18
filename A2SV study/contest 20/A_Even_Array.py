test = int(input())

for _ in range(test):
    n = int(input())

    nums = list(map(int, input().split()))

    even = 0
    odd = 0
    cor = 0
    for i in range(n):
        if i %2 == nums[i] % 2:
            cor += 1
        elif nums[i]% 2 == 0:
            even += 1
        else:
            odd += 1

    if cor == n :
        print(0)
    # elif n % 2 == 0:
    elif even == odd:
        print(odd)
    else:
        print(-1)

    # else:
    #     if abs(even - odd) == 1 and n > 1:
    #         print(max(even, odd) //2)
    #     else:
    #         print(-1)
    # print(even, odd)
