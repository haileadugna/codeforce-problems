queries = int(input())

for _ in range(queries):
    l, r = map(int, input().split())

    if l == 1:
        print(*[l, r])
    else:
        y = r - r%l
        print(*[l, y])