cases = int(input())
for _ in range(cases):
    string = input()
    if len(string) %2 == 1:
        string += " "
    string += " "
    
    l = 0
    r = 1
    res = ""
    while r < len(string):
        if string[l] != string[r]:
            res += string[l]
            l += 1
            r += 1
        else:
            l += 2
            r += 2
    temp = list(res)
    temp = list(set(temp))
    temp.sort()
    print("".join(temp))