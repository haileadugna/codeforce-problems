length = input().split()
n = int(length[0])
m = int(length[1])

grid = []
for _ in range(n):
    grid.append(input())

arrs = []
for row in range(n):
    for col in range(m):
        if grid[row][col] == "S":
            loc_s = [row, col]
        if grid[row][col] == "T":
            loc_e = [row, col]

diff = abs(loc_s[0] - loc_e[0])
start = min(loc_e[0], loc_s[0])
count = 0
for i in range(m):

    cnt = 0
    for j in range(start, start + diff ) :
        if grid[j][i] == "*":
            break
        elif grid[i][j] == ".":
            count +=1
    count = max(cnt, count)

diff1 =abs( loc_s[1] - loc_e[1])
start = min(loc_e[1], loc_s[1])
count2 = 0
for i in range(n):
    
    cnt2 = 0
    for j in range(start, start + diff1 ) :
        if grid[i][j] == "*":
            break
        elif grid[i][j] == ".":
            count2 += 1
    count2 = max(cnt2, count2)

if count == diff +1 or count2 == diff1 +1 :
    print("YES")
else:
    print("NO")