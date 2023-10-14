k, n = map(int, input().split())
nums = list(map(int, input().split()))

prime = [2]

for num in nums:
    if num %2 != 0 and num > 1:
        prime.append(num)
# print(prime)
res = 0
for num in prime:
    temp = 0
    summ = k

    for i in nums:
        if i % num == 0:
            temp += 1
            
        elif summ < i:
            break
        else:
            summ -= i
            temp += 1
    # print(temp)
    res = max(res, temp)

print(res)
