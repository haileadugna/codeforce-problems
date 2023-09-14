test = int(input())

for _ in range(test):
    n, k = map(int, input().split())
    numsa = list(map(int, input().split()))
    numsb = list(map(int, input().split()))

    for i in range(n):
        numsa[i] = [numsa[i], i]

    numsa.sort()
    # print(numsa)
    numsb.sort()
    # print(numsb)
    res = [0]*n
    for j in range(n):
        res[numsa[j][1]] = numsb[j]

    print(*res)