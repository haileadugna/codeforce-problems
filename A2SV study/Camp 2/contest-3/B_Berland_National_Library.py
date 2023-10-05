n = int(input())
in_library = [False] * 10**7  
ans = state = 0  

for _ in range(n):
    event = input().split()
    ai = int(event[1])
    
    if event[0] == "+":
        state += 1
        in_library[ai] = True
        ans = max(ans, state)
    else:
        if in_library[ai]:
            state -= 1
        else:
            ans += 1
        in_library[ai] = False

print(ans)
