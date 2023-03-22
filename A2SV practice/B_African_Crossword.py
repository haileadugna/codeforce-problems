n, m = map(int, input().split())

dict_row = {}
dict_col = {}
alist = []
for row in range(n):
    temp = input()
    alist.append(temp)
    dict_row[row] = temp

for i in range(m):
    concar = ""
    for j in range(n):
        concar += alist[j][i]
    dict_col[i] = concar
ans = ""
for i in range(n):
    for j in range(m):
        cnt = 0
        for k in dict_col[j]:
            if alist[i][j] == k:
                cnt += 1
        for l in dict_row[i]:
            if alist[i][j] == l:
                cnt += 1
        
        if cnt <= 2:
            ans += alist[i][j]
print(ans)
