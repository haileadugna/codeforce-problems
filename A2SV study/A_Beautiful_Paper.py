t = input()
for i in range(int(t)):
    nums = input().split()
    a1 = int(nums[0])
    b1 = int(nums[1])
    nums2 = input().split()
    a2 = int(nums2[0])
    b2 = int(nums2[1])
    res = "No"
    if (a1 == b2 and b1 + a2 == a1) or (a2 == b1 and (a1 + b2) == a2):
        res = "Yes"
    if (b2 == b1 and (a1 + a2) == b1) or (a2 == a1 and (b2 + b1) == a2):
        res = "Yes"
    print(res)