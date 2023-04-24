n = int(input())

stack = []
for i in range(n):
    temp = input()

    ans = [0] * 26
    for j in temp:
        ans[ord(j) - 97] += 1

    odd_count = 0
    for num in ans:
 
        # checking condition
        if num % 2 != 0:
            odd_count += 1
    ans.append(odd_count)
    stack.append(ans)

res = 0
for i in range(n - 1):
    for j in range(i + 1, n):
        if stack[i][-1] == 0 and stack[j][-1] == 0:
            res += 1
        elif stack[i][-1] == 1 and stack[j][-1] == 0:
            res += 1
        # elif stack[i][-1] >= 1 and stack[j][-1] == 0:
        #     res += 1

print(stack)
