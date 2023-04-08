

n, k = map(int, input().split())
nums = list(map(int, input().split()))

stack = []
for i in range(n):
    num = nums[i]
    factorization = []
    d = 2

    while d * d <= num:
        while num % d == 0:
            factorization.append(d)
            num //= d
        d += 1
    if num > 1:
        factorization.append(num)

    stack.append(factorization)
temp = []
for i in range(n):
    temp.append([len(stack[i]), stack[i]])

temp.sort()
# print(temp)
res = 0
j = 0
count = 1
for i in range(n-1):
    if temp[i][0] != temp[i+1][0]:
        j = max(j, i+1)
        count = 1
    else:
        count += 1
    while j < n and temp[j][0] <= (temp[i][0] * 2 // 3):
    
        if len(set(temp[i][1] + temp[j][1])) == (temp[i][0] + temp[j][0]) // 3:
            res += count
        j += 1

print(res)