import sys
import math
test = int(input())

for _ in range(test):
    n = int(input())

    nums = list(map(int, input().split()))
    ans = 0

    dictt = {}
    for i in range(math.ceil(math.log2(max(nums))) + 1):
        dictt[2**i] = []

    for j in range( n):
        tmp = int(math.log2(nums[j])) 
        dictt[2**tmp].append(nums[j])

    for num in list(dictt.keys()):
        if len(dictt[num]) < 2:
            continue
        elif len(dictt[num]) == 2:
            ans += 1
        else:
            n = len(dictt[num])
            ans += (n * n -n) // 2
    print(ans)