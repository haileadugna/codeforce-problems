import sys
test = int(input())
for _ in range(test):
    n = int(input())
    input = sys.stdin.readline
    nums = list(map(int, input().split()))

    if min(nums) > 1:
        print("NO")
    else:
        
        nums.sort()
        temp = nums[:]
        res = "YES"
        for i in range(1, len(nums)):
            nums[i] += nums[i - 1]

        for j in range(len(nums) - 1, 0, -1):
            if nums[j - 1] < nums[j] - nums[j - 1]:
                res = "NO"
                break
        print(res)
        
