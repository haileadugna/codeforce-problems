test = int(input())
for _ in range(test):
    n = int(input())

    nums = input().split()
    res = []

    left = 0
    right = n -1
    while left < right:
        res.append(nums[left])
        res.append(nums[right])
        left += 1
        right -= 1
    if len(nums) % 2 == 1:
        res.append(nums[left])

    print(" ".join(res))