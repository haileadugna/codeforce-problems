t = input()
for i in range(int(t)):
    # x = input()
    temp = []
    for l in range(8):
        temp.append(input())

    for i in range(1,7):
        for j in range(1,7):

            if temp[i][j] == "#":
                if temp[i-1][j-1] == "#" and temp[i+1][j+1] == "#" and temp[i-1][j+1] == "#" and temp[i+1][j-1] == "#" :
                    print(i+1,j+1)



