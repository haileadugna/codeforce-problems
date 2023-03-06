test = int(input())

for _ in range(test):
    n, m = map(int, input().split())
    div = list(map(int, input().split()))
    div.sort(reverse=True)
    summ = 2
    ans = 0


    for num in div:
        if summ >= n:
            break
        else:
            summ += num - 1
            ans += 1
    if summ < n:
        ans = -1
        
    print(ans)
