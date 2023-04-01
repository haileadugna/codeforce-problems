test = int(input())

for _ in range(test):
    num = int(input())
    temp = []
    for i in range(1, 32):
        temp.append(2**i)
    if num in temp:
        print(num + 1)
    elif num == 1:
        print(3)
    else:

        # n = (num >> 1 & 1) == 1
        for i in range(64):
            if (num >> i & 1) == 1:
                print(2 ** i)
                break

