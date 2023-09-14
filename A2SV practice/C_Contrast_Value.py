from collections import Counter


t = int(input())
while t > 0:
    n = int(input())
    a = list(map(int, input().split()))
    a = a[::-1]  # Truncate the list to size n
    a = list(Counter(a).keys())  # Remove duplicates
    n = len(a)
    ans = n
    for i in range(n - 2):
        ans -= (a[i] < a[i + 1] and a[i + 1] < a[i + 2])
        ans -= (a[i] > a[i + 1] and a[i + 1] > a[i + 2])
    print(ans)
    t -= 1
# from collections import Counter

# t = int(input())
# while t > 0:
#     n = int(input())
#     a = list(map(int, input().split()))
    # a = a[::-1]  # Truncate the list to size n
    # a = list(Counter(a).keys())  # Remove duplicates
    # n = len(a)
#     ans = n
#     for i in range(n - 2):
#         if (a[i] < a[i + 1] and a[i + 1] < a[i + 2]) or (a[i] > a[i + 1] and a[i + 1] > a[i + 2]):
#             ans -= 1
#     print(ans)
#     # print(a)
#     t -= 1