
n, val = map(int, input().split())
arr = list(map(int, input().split()))
arr = arr*2

for i in range(1, len(arr)):
    arr[i] += arr[i - 1]

temp = 0
if arr[-1] < val:
    
    temp = val // arr[-1]
    val = val % arr[-1]
# if arr[-1] > val:
res = float('inf')
l, r = 0, 0
ans = [0, 0]
while r < len(arr) :

    if arr[r] - arr[l] < val:
        r += 1
    elif arr[r] - arr[l] >= val:
        
        l += 1
        if res > r - l + 1:
            res = r - l + 1
            ans = [(l )%n, r%n]

# else:
#     res = 0
if ans[0] < n:
    fin = ans[0] + 1     
else:
    fin = ans[0]//2 
print(fin, temp* len(arr) + res)
# print(res, temp* len(arr), ans)      
# print(arr)