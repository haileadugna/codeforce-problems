test = int(input())

for _ in range(test):
    n = int(input())
    stack01 = []
    stack10 = []
    res = float("inf")
    for i in range(n):
        val, temp = map(int, input().split(" "))
        if temp == 1:
            stack01.append(val)

        elif temp == 10:
            stack10.append(val)

        elif temp == 11:
            res = min(res, val)
        else:
            continue
    min01 = float("inf")
    min10 = float("inf")
    if stack01:
        min01 = min(stack01)
    if stack10:
        min10 = min(stack10)
    res = min(res, min01 + min10)

    if res == float("inf"):
        print(-1)
    else:
        print(res)


