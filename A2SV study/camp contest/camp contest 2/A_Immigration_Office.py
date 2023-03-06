n = int(input())
people = list(map(str, input().split(" ")))
p = int(input())
list1 = []
for i in range(p):
    list1.append(input())
# print("Daniel" < "Duressa" )

for peo in list1:
    low = 0
    high = n
    while low < high:
        mid = (high + low )//2
        if people[mid] >= peo:
            high = mid - 1
        elif people[mid] < peo:
            low = mid + 1

    print(low)
        
