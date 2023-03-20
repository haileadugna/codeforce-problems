from collections import defaultdict
test = int(input())
for _ in range(test):
    n = int(input())
    string = input()

    dictt = defaultdict(list)
    for i in range(n):
        dictt[string[i]].append(i)
    res = "YES"
    temp = dictt.keys()
    for s in temp:
        num = dictt[s]
        t = num[0] % 2
        for j in num:
            if t != j % 2:
                res = "NO"
                break

    print(res)
