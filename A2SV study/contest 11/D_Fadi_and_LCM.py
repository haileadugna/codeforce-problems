# x = int(input())

# def gcd(a, b):
#    if b == 0:
#        return a
#    return gcd(b, a % b)

# ans = []
# for i in range(1, int(x**0.5) + 1):
#     for j in range(int(x**0.5) -1, x + 1):
#         temp = gcd(j, i)
    
#         if temp * x == i * j:
#             ans.append([i, j])

# if x == 1:
#     print(*[1, 1])
#     exit()

# res = ans[0]
# prev = max(ans[0])
# for num in ans:
#     if prev > max(num):
#         res = num
#         prev = max(num)

# print(*res)

x = int(input())

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

res = []
for i in range(1, int(x**0.5) + 1):
    if x % i == 0:
        j = x // i
        temp = gcd(i, j)
        if temp * x == i * j:
            res.append([i, j])

if x == 1:
    print(*[1, 1])
    exit()

min_val = max(res[0])
ans = res[0]
for num in res:
    if max(num) < min_val:
        ans = num
        min_val = max(num)

print(*ans)
