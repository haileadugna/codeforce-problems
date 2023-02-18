test = int(input())
for _ in range(test):
    n = int(input())
    nums =  input()

    left = 0
    right = n -1
    while left <= right and nums[left] != nums[right]:

        left += 1
        right -= 1
    print(right - left + 1)