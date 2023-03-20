import sys

test = int(input())
for _ in range(test):
    input = sys.stdin.readline
    n, q = map(int, input().split())
    nums = list(map(int, input().split()))
    for j in range(1,n):
        nums[j] += nums[j - 1]
    for i in range(q):
        l, r, k = map(int, input().split())
        if l - 2 < 0:
            m = 0
        else:
            m = nums[l - 2]
        cur = nums[r - 1] - m
        res = (r - l + 1) * k + nums[-1] - cur

        if res % 2 == 1:
            print("YES")
        else:
            print("NO")
