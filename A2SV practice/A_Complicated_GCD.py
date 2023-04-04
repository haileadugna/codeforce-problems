c, d = map(int, input().split())

a = max(c, d)
b = min(c, d)

if a - b > 0:
    print(1)
else:

    print(a)