num = int(input())
num += 1
factorization = []
d = 2
res = []
for n in range(2, num + 1):
    temp = []
    while d * d <= n:
        while n % d == 0:
            temp.append(d)
            n //= d
        d += 1
    if n > 1:
        temp.append(n)
    
    if len(temp) == 1:
        res.append(1)
    else:
        res.append(len(temp))

# for nu in range(2, num + 1):
#     if nu in factorization:
#         res.append(1)
#     else:
#         res.append(2)

print(max(res))
print(*res)