test = int(input())
for _ in range(test):
    n = int(input())
    nums = list(map(int, input().split()))

    temp = []
    left = 0
    right = 6
    while right < n:
        summ = 0
        for i in range(left, right):
            summ += nums[i]

        temp.append(summ)
        left += 6
        right += 6
    if left < n:
        temp.append(sum(nums[left:]))
    temp.append(0)

    res = temp[0] + temp[1]
    low = 2
    high = 3
    while low < len(temp) and high < len(temp):
        res = min(res, temp[low] + temp[high])
        low += 1
        high += 1
    print(res)