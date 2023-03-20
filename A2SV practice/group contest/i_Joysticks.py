joy1, joy2 = map(int, input().split())

res = 0
while not (joy1 == 1 and joy2 == 1) and (joy1 > 0 and joy2 > 0):
    if joy2 > joy1:
        joy1 += 1
        joy2 -= 2
    else:
        joy2 += 1
        joy1 -= 2
    res += 1

print(res)