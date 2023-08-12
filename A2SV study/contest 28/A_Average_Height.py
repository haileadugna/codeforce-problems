test = int(input())

for _ in range(test):
    n = int(input())
    nums = list(map( int, input().split()))

    even = []
    odd = []
    for i in nums:
        if i % 2 == 0:
            even.append(i)

        else:
            odd.append(i)

    ans = odd + even
    print(*ans)