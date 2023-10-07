
n = int(input())
y = list(map(int, input().split()))
x = 0
sol = 0
energy = 0

for i in range(1, n + 1):
    
    energy += x - y[i - 1]

    if energy < 0:
        sol += abs(energy)
        energy = 0

    x = y[i - 1]

print(sol)


