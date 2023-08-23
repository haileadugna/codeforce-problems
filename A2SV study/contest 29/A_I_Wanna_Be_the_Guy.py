n = int(input())

x = list(map(int, input().split()))
y = list(map(int, input().split()))

nums = y[1:] + x[1:]

if len(set(nums)) == n:
    print("I become the guy.")
else:
    print("Oh, my keyboard!")