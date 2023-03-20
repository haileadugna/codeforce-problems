test = int(input())
for i in range(test):
    n = int(input())
    nums = list(map(int, input().split()))
    odd = 0
    even = 0
    for num in nums:
        if num % 2 != 0:
            odd += num
        else:
            even += num
    if even > odd:
        print("YES")
    else:
        print("NO")
