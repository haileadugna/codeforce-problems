n = int(input())
temp = []
for _ in range(n):

    given = input().split()
    price = given[0]
    quality = given[1]
    temp.append((price, quality))
res = "Poor Alex"

temp.sort()
for j in range(n-1):
    if temp[j][1] > temp[j+1][1]:
        res = "Happy Alex"
print(res)
