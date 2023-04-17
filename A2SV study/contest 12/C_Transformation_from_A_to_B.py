a, b = map(int, input().split())

res = [b]

while b > a:
  
    if b % 2 == 0:
        b //= 2
        res.append(b)
    
    elif b % 10 == 1:
        b = (b - 1) // 10
        res.append(b)
    
    else:
        print("NO")
        exit()

res.reverse()
if b == a:
    print("YES")
    print(len(res))
    print(*res)

else:
    print("NO")