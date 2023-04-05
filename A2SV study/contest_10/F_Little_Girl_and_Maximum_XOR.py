import math
import bisect
l, r = map(int, input().split())

num = l ^ r
bit_k = bin(num)
le = len(bit_k)
ans = num
for i in range(2, len(bit_k)):
    if bit_k[i] == "0":
        ans += 2**(le - i - 1)

if l == r:
    print(num)
else:
    print(ans)
