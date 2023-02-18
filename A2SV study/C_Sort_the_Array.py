n = int(input())
arr = list(map(int, input().split()))

temp = sorted(arr)
left = 0
right = n-1



while left < n and arr[left] == temp[left]:
    left += 1
while right > 0 and arr[right] == temp[right]:
    right -= 1

check = arr[left:right+1]
check.reverse()

if temp == arr:
    print("yes")
    print(1,1)
elif check == temp[left:right+1]:
    print("yes")
    print(left+1, right+1)
else:
    print("no")




