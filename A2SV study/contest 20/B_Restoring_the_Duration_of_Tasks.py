test = int(input())

for _ in range(test):

    n = int(input())

    time = list(map(int, input().split()))
    dur = list(map(int, input().split()))

    res = []

    for i in range(n):
        if i == 0:
            res.append(dur[0] - time[0])

        else:
            if time[i] > dur[i - 1]:
                res.append( dur[i] - time[i])

            else:
                res.append(dur[i] - dur[i - 1])
        
    print(*res)