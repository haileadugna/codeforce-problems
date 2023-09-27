
q = int(input()) 
changes = {}  

for _ in range(q):
    old, new = input().split()
    changes[old] = new

res = []
for old, new in changes.items():
    while new in changes:
        new = changes[new]

    found = False
    for i in res:
        if new in i or old in i:
            found = True
            break
    if not found:
        res.append((old, new))
print(len(res))
for i in range(len(res)):
    print(res[i][0], res[i][1])

# Output the mapping between old and new handles
# for old, new in changes.items():
#     print(old, new)



# p = int(input())

# rev = {}
# d = {}
# for i in range(p):
#     a, b = input().split()
#     if a not in d:
#         d[a] = b
#     if b not in rev:
#         rev[b] = a

# # print(d)
# res = []
# for w in d.keys():
    
#     if d[w] not in d:
#         if w in rev:
#             temp = [rev[w]]
#         else:
#             temp = [w]
       
#         t = w

#         while d[t] in d:
#             t = d[t]

#         temp.append(d[t])
#         res.append(temp)


# # Output
# print(len(res))
# for r in res:
#     print(r[0], r[1])
