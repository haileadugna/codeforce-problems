# rows, cols = map(int, input().split())

# box = []
# for row in range(rows):
#     input_row = input()
#     res = ""
#     for i in range(cols):
#         if input_row[i] == ".":
#             res += "D"
#         else:
#             res += input_row[i]

#     print(res)
# read input
r, c = map(int, input().split())
pasture = [input() for _ in range(r)]

# iterate over each sheep cell and place a dog in each neighboring cell
for i in range(r):
    for j in range(c):
        if pasture[i][j] == 'S':
            if i > 0:
                if pasture[i-1][j] == '.':
                    pasture[i-1] = pasture[i-1][:j] + 'D' + pasture[i-1][j+1:]
                elif pasture[i-1][j] == 'W':
                    print("No")
                    exit()
            if i < r-1:
                if pasture[i+1][j] == '.':
                    pasture[i+1] = pasture[i+1][:j] + 'D' + pasture[i+1][j+1:]
                elif pasture[i+1][j] == 'W':
                    print("No")
                    exit()
            if j > 0:
                if pasture[i][j-1] == '.':
                    pasture[i] = pasture[i][:j-1] + 'D' + pasture[i][j:]
                elif pasture[i][j-1] == 'W':
                    print("No")
                    exit()
            if j < c-1:
                if pasture[i][j+1] == '.':
                    pasture[i] = pasture[i][:j+1] + 'D' + pasture[i][j+2:]
                elif pasture[i][j+1] == 'W':
                    print("No")
                    exit()

# print the pasture with dogs placed
print("Yes")
for row in pasture:
    print(row)