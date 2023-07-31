test = int(input())

for _ in range(test):
    a, b, c = map(int, input().split())

    if a == b == c == 0:
        print(0)
        continue
    
    elif a >3 and b >3 and c > 3:
        print(7)
        continue

    elif a == b == c == 3:
        print(6)
        continue

    elif a == b == 2 or a== c == 2 or b == c == 2:
        print(5)
        continue

    elif a == b== c== 2 or (min(a, b, c) == 1 and (a> 1 and b > 1 or c > 1 and b > 1 or a > 1 and c > 1 )):
        print(4)
        continue

    elif  a == b == c == 1:
        print(3)
        continue

    





    '''
    2 3 3
    1 2 2, 0 1 2, 0, 0 1, 222 111 001
    '''