t=int(input())
for r in range(t):
    n,m=input().split()
    n,m=int(n),int(m)
    lst=[]
    for k in range(n):
        lst.append(list(input()))
    for a in range(m):
        temp=[]
        for b in range(n):
            if lst[b][a]=='*':
                temp.append([lst[b][a]])
                lst[b][a]="."
            elif lst[b][a]=='o':
                temp.append([lst[b][a],b])
                lst[b][a]="."
        # print(temp)
        idx=-1
        while idx >= -n and temp:
            t=temp.pop()
            if t[0]=='*':
            
                lst[idx][a]='*'
    
                idx-=1
            elif t[0]=='o':
                lst[t[1]][a]='o'
                idx=(t[1]-n)-1
    for elem in lst:
        print("".join(elem))
    print()
    