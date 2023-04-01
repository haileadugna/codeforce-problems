import math
import bisect
num = int(input())

temp = []
for i in range(math.ceil(math.log2(10**9))):
    temp.append(2**i)

if num in temp:
    print(1)
else:
    # ind = bisect.bisect_left(temp, num)
    # print(num - temp[ind - 1] + 1)

    ans = 0
    while num > 0:
        ans += num % 2
        num //= 2
    print(ans)