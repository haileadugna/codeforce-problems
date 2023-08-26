string1 = input()
string2 = input()

l, r = 0, 0
res = 0

if string1 == string2:
    print(-1)

else:
    print(max(len(string1), len(string2)))