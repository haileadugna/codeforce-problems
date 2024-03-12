t = int(input())

for _ in range(t):
    n = int(input())
    prices = list(map(int, input().split()))
    
    bad_days = 0
    min_price = prices[-1]
    
    for i in range(n - 1, -1, -1):
        if prices[i] > min_price:
            bad_days += 1
        else:
            min_price = prices[i]
    
    print(bad_days)
