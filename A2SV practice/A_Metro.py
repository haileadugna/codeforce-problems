n, s = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

if a[0] == 0:
    print("NO")
    exit()

if a[s-1] == 1:
    print("YES")
    exit()

if b[s-1] == 0:
    print("NO")
    exit()

for i in range(s, n):
    if a[i] == 1 and b[i] == 1:
        print("YES")
        exit()

print("NO")