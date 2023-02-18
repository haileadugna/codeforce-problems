n = input()
alist = input().split()
res1 = []
res2 = []
res3 = []
for i in range(int(n)):
    if int(alist[i]) < 0:
        res1.append(alist[i])
    elif int(alist[i]) == 0:
        res3.append(alist[i])
    else:
        res2.append(alist[i])
if len(res2) == 0:
    for j in range(2):
        res2.append(res1.pop())
if len(res1)%2 == 0:
    res3.append(res1.pop())
print(len(res1), " ".join(res1))
print(len(res2), " ".join(res2))
print(len(res3), " ".join(res3))