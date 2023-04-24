n, m, k  = map(int, input().split())

stack = []
for i in range(m + 1):
    tmp = int(input())
    stack.append(tmp)

fedor = stack.pop()
# print(fedor)
count = 0
for army in stack:
    diff = fedor ^ army  
    bits = bin(diff).count('1')  
    if bits <= k:
        count += 1

print(count)