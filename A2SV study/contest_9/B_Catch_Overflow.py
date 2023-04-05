n = int(input())
stack = [[1, 0]]

for _ in range(n):
    command = input().split()

    if command[0] == "add":
        stack[-1][1] += 1
    elif command[0] == "end":
        iterations, add = stack.pop()
        stack[-1][1] += iterations * add
    else:
        stack.append([int(command[1]), 0])

if stack[-1][1] > (2**32 - 1):
    print("OVERFLOW!!!")
else:
    print(stack[-1][1])