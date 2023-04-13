num = int(input())
temp = [1 for i in range(num + 2)]
temp[1] = 1

d = 2

while d * d <= num + 2:
    for j in range(d * d, num + 2, d):
        temp[j] = 2
    d += 1

 
if num > 2:
    print(2)
else:
    print(1)

print(*temp[2:])
