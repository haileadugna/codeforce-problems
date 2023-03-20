test = int(input())
for i in range(test):
    a, b, c = map(int, input().split())
    if a + b == c:
        print("+")
    else:
        print("-")