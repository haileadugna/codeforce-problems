n = int(input())

love = "codeforces"
for i in range(n):
    temp = input()
    res = 0
    for j in range(10):
        if love[j] != temp[j]:
            res += 1

    print(res)
