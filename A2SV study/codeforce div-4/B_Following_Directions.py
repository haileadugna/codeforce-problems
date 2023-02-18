test = int(input())

for _ in range(test):
    n = int(input())
    temp = input()
    nums = [0,0]
    res = "no"
    for i in range(n):
        if nums == [1,1]:
            res = "yes"
        elif temp[i] == "U":
            nums[1] += 1
        elif temp[i] == "D":
            nums[1] -= 1
        elif temp[i] == "L":
            nums[0] -= 1
        elif temp[i] == "R":
            nums[0] += 1
    if nums == [1,1]:
        res = "yes"
    print(res)