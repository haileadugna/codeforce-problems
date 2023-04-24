n, t = map(int, input().split())
nums = list(map(int, input().split()))


temp = 1
while temp < t:
    temp += nums[temp-1]
    print(temp)
    if temp == t:
        print("YES")
        exit()
    
print("NO")
