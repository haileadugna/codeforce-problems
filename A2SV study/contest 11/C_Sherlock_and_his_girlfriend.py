num = int(input())
num += 1
factorization = set()
d = 2
 
for n in range(2, num + 1):
    while d * d <= n:
        while n % d == 0:
            factorization.add(d)
            n //= d
        d += 1
    if n > 1:
        factorization.add(n)
 
res = []
for nu in range(2, num + 1):
    if nu in factorization:
        res.append(1)
    else:
        res.append(2)

if num < 2:
    print(1)
    print(1)
else:
    print(max(res))
    print(*res)