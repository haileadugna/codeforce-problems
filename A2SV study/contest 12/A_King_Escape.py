n = int(input())
ax, ay = map(int, input().split())
bx, by = map(int, input().split())
cx, cy = map(int, input().split())

if ax > bx and ax < cx or (ax < bx and ax > cx):
    print("NO")
    exit()

if ay > by and ay < cy or ( ay < by and ay > cy):
    print("NO")
    exit()

print("YES")
# if ax > bx and ax < cx:
#     print("YES")
#     exit()

# if ax > bx and ax < cx:
#     print("YES")
#     exit()