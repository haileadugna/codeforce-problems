test = int(input())

for _ in range(test):
    n = int(input())
    nums = list(map(int, input().split()))
    nums.sort()

    for index in range(n - 1):
        if nums[index] < 0 and abs(nums[index]) >= abs(nums[index + 1]):
            nums[index] = - nums[index]
            nums[index + 1] = - nums[index + 1]
    
    print(sum(nums))