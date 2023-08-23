test = int(input())

for _ in range(test):
    n = int(input())

    nums = []

    for i in range(n):
        nums.append(tuple(map(int, input().split())))


    list1 = set()
    list1.add(nums[i][0])
    list1.add(nums[i][1])
    list2 = set()

    for i in range(1, n):
        if nums[i][0] in list1 or nums[i][1] in list1:
            list2.add(nums[i][0])
            list2.add(nums[i][1])

        else:
            list1.add(nums[i][0])
            list1.add(nums[i][1])

    print(list1, 'set1')
    if len(list1) == n:
        print('YES')
    else:
        print("NO")
