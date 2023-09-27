
n, m = map(int, input().split())
chairs = [[0] * 103 for _ in range(103)]

for _ in range(n):
    x, y = map(int, input().split())
    chairs[x][y] += 1


for x in range(101):
    for y in range(101):
        if x > 0:
            chairs[x][y] += chairs[x - 1][y]
        if y > 0:
            chairs[x][y] += chairs[x][y - 1]
        if x > 0 and y > 0:
            chairs[x][y] -= chairs[x - 1][y - 1]

for _ in range(m):
    sx, sy, ex, ey = map(int, input().split())
    total_chairs = chairs[ex][ey]
    if sx > 0:
        total_chairs -= chairs[sx - 1][ey]
    if sy > 0:
        total_chairs -= chairs[ex][sy - 1]
    if sx > 0 and sy > 0:
        total_chairs += chairs[sx - 1][sy - 1]
    
    print(total_chairs)
