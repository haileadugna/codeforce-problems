test = int(input())
for _ in range(test):
    n = int(input())
    nums = list(map(int, input().split()))

    for i in range(n):
        temp = 0
        for j in range(n):
            if i != j:
                temp = temp ^ nums[j]

        if temp in nums:
            print(temp)
            break
