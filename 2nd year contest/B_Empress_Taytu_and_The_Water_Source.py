n = int(input())

for _ in range(n):
    m, h = map(int, input().split())
    cargo = list(map(int, input().split()))
    hours = list(map(int, input().split()))

    cargoHours = []
    for i in range(m):
        cargoHours.append([cargo[i], hours[i]])
    cargoHours.sort()
    for i in range(1, m):
        cargoHours[i][1] += cargoHours[i - 1][1]

    totalHours = sum(hours)
    h = h%totalHours
    rem = h - totalHours

    print(cargoHours)
    l, r = 0, m - 1

    while l <= r:
        mid = (l + r) // 2
        print('here', totalHours - cargoHours[mid][1])
        if rem <= totalHours - cargoHours[mid][1]:
            l = mid + 1
        else:
            r = mid - 1
    print(l, r)

