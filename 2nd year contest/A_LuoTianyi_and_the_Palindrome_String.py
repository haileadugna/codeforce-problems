from collections import Counter


test = int(input())

for _ in range(test):
    string = input()

    count = Counter(string)
    if len(count) == 1:
        print(-1)
    else:
        print(len(string) -1)
        