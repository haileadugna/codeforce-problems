cases = int(input())
for _ in range(cases):
    nums = list(input())
    # print(set(nums))
    res = len(nums)
    i = 0
    for i in range(len(nums)-1):
        if nums[i] == nums[i + 1]:
            i +=1
            continue
        temp = []
        count = 0
        for j in range(i, len(nums)):

            if len(temp) == 3:
                break
            else:
                if nums[j] in temp:
                    count += 1
                    continue
                else:
                    temp.append(nums[j])
                    count += 1
            # print(count)
        if len(temp) == 3:
            res = min(res, count)

        if res == 3:
            break
    if len(list(set(nums))) <= 2:
        print(0)
    else:
        print(res)