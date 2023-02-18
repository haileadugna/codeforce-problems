n = int(input())
nums= list(map(int, input().split()))

left = 0
right = n-1
wube = []
henok  = []

while left <= right:
    if left < right and nums[left] > nums[right]:
        wube.append(nums[left])
        left += 1
    else:
        wube.append(nums[right])
        right -= 1
    if left <= right:
        if nums[left] > nums[right]:
            henok.append(nums[left])
            left += 1
        else:
            henok.append(nums[right])
            right -= 1

print(sum(wube), sum(henok))

