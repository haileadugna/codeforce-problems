testcases = int(input())
for _ in range(testcases):
    nums = input().split()
    num1 = int(nums[0])
    num2 = int(nums[1])
    num3 = int(nums[2])
    if num1 > num2 and num1 < num3 or (num1 < num2 and num1 > num3):
        print(num1)
    elif num2 > num1 and num2 < num3 or (num2 < num1 and num2 > num3):
        print(num2)
    else:
        print(num3)