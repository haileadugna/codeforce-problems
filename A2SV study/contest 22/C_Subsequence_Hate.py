def min_operations(s):
    n = len(s)
    cnt = 0
    for i in range(n-2):
        if s[i:i+3] == '010' or s[i:i+3] == '101':
            cnt += 1
            s = s[:i+2] + '1' if s[i:i+3] == '010' else s[:i+2] + '0' + s[i+3:]
    return cnt

t = int(input())
for _ in range(t):
    s = input()
    print(min_operations(s))