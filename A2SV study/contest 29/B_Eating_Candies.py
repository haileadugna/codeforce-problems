test = int(input())

for _ in range(test):

    n = int(input())
    nums = list(map(int, input().split()))
    left = nums[:]
    right = nums[::-1]
    

    ans = 0

    for i in range(1, n):
        left[i] += left[i -1]

    for j in range(1, n):
        right[j] += right[j -1]

    right.reverse()
    
    l, r = 0, n -1

    while l < r:
        if left[l] == right[r]:
            ans = l + n - r +1
            l +=1
            r -= 1

        elif left[l] > right[r]:
            r -= 1

        else:
            l += 1
    

            


    print(ans)

        
