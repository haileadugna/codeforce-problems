n = int(input())
nums = list(map(int, input().split()))
strings = [input().strip() for _ in range(n)]

total = nums[0]
minn = strings[0][::-1]  

for i in range(1, n):
    reversed = strings[i][::-1]  

    if strings[i] >= minn:
        minn = reversed
    elif reversed >= minn:
        total += nums[i]
    else:
        print(-1)
        exit()

print(total)
