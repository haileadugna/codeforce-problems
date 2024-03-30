test = int(input())

for _ in range(test):
    num = int(input())
    while num % 2 == 0:
        num = num // 2
    if num == 1:
        print('NO')
    else:
        print('YES')
        