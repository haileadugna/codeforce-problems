
# from collections import Counter
# n = int(input())

# nums1 = list(map(int, input().split()))
# nums2 = list(map(int, input().split()))

# div = []

# for i in range(n):

#     if nums2[i] == 0:
#         div.append('b')
#     elif nums1[i] == 0:
#         div.append("a")
#     else:
#         div.append(nums1[i] / nums2[i])

# ans = Counter(div)

# res = 0
# for i in ans:
#     if i != "a":
#         res = max(res, ans[i])

# print(res)


from math import gcd
from collections import defaultdict

def check(arr):
    if arr[0] < 0:
        arr = (-arr[0], -arr[1])
    elif arr[0] == 0 and arr[1] < 0:
        arr = (arr[0], -arr[1])
    d = gcd(abs(arr[0]), abs(arr[1]))
    return (arr[0] // d, arr[1] // d)

n = int(input())
nums1 = list(map(int, input().split()))
nums2 = list(map(int, input().split()))

dictt = defaultdict(int)
ans = 0
cnt = 0

for i in range(n):
    if nums1[i] == 0:
        if nums2[i] == 0:
            cnt += 1
    else:
        arr = check((-nums2[i], nums1[i]))
        dictt[arr] += 1
        ans = max(ans, dictt[arr])

print(cnt + ans)