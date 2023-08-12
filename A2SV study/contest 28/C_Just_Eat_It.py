test = int(input())

for _ in range(test):
    n = int(input())
    nums = list(map(int, input().split()))

    for i in range(1,n):
        nums[i] += nums[i -1]

    total_sum = nums[-1]
    ans = "YES"
    less = []
    for i in range(n):
        if nums[i] < 0:
            less.append(i)

        elif nums[i] >= total_sum and i != n - 1:
            ans = "NO"
            break

    if ans == "NO":
        print(ans)
        continue
    else:
        if len(less) == 0:
            print(ans)

        else:
            less.reverse()
            temp = n
            for i in less:
                summ = sum(nums[i+ 1, temp]) + abs(nums[i])

                if summ > total_sum:
                    ans = "NO"
                    break
                temp = i

            print(ans)




        

    