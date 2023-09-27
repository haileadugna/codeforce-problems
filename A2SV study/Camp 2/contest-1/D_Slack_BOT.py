def function(x, y):
    n = 0
    for i in range(min(len(x), len(y))):
        if x[i] == y[i]:
            n += 1
        else:
            break
    return n

N = int(input())
strings = [input() for _ in range(N)]

for i in range(N):
    max_n = 0
    for j in range(N):
        if i != j:
            n = function(strings[i], strings[j])
            max_n = max(max_n, n)
    print(max_n)
