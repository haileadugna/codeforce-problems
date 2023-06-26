def calculate_temperatures(n, c):
    L = [float('inf')] * n
    p = float('inf')
    for i in range(n):
        p = min(p + 1, c[i])
        L[i] = p
    
    R = [float('inf')] * n
    p = float('inf')
    for i in range(n-1, -1, -1):
        p = min(p + 1, c[i])
        R[i] = p
    
    temperatures = []
    for i in range(n):
        temperature = min(L[i], R[i])
        temperatures.append(temperature)
    
    return temperatures


q = int(input())

for _ in range(q):
    input()  # Read the empty line
    
    n, k = map(int, input().split())
    positions = list(map(int, input().split()))
    temperatures = list(map(int, input().split()))
    
    cell_temperatures = calculate_temperatures(n, temperatures)
    
    print(*cell_temperatures)
