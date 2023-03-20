test = int(input())
for _ in range(test):
    n = int(input())
    nums = list(map(int, input().split()))
    nums.sort()
    left, right = 0, 0
    summ = nums[right]

    while right < n and left <= right:
        if summ == nums[right]:
            summ += nums[right]
            right += 1
        elif summ > nums[right]:
            summ -= nums[left]
            left += 1
        else:
            if left > 0:
                summ += nums[left]
                left -= 1
            else:
                break
    if right == n and min(nums) <= 1:
        print("YES")
    else:
        print("NO")
        
