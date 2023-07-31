
test = int(input())

for _ in range(test):
    
    s = input()

    temp = []
    i = 0
    while i < len(s):
        if i + 1 < len(s) and s[i] == s[i+1]:
            i += 2
        else:
            temp.append(s[i])
            i += 1
    print(''.join(sorted(set(temp))))