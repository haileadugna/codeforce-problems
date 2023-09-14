# test = int(input())

# for _ in range(test):
#     n, m = map(int, input().split())

#     nums = list(map(int, input().split()))

#     nums.sort()

#     if nums[0] == nums[1] or nums[-2] == nums[-1]:
#         res = (nums[-1] - nums[0]) * (n* m - 1)
#     else:
#         temp = (nums[-2] - nums[0]) *(min( n - 1, m - 1))
#         temp2 = (nums[-1] - nums[0]) * (n * m - (max( n - 1, m - 1)) + 1)
#         res = temp + temp2

#     print(res)

def solve():
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    a.sort()
    if n > m:
        n, m = m, n
    if n == 1:
        print((m - 1) * (a[-1] - a[0]))
    else:
        ans1 = (n * m - 1) * a[-1] - a[0] * (n * (m - 1)) - (a[-1] * (n - 1))
        ans2 = ((a[-1] - a[0]) * (n * (m - 1))) + (a[-1] * (n - 1))
        print(max(ans1, ans2))

T = int(input())
for _ in range(T):
    solve()