n, m = map(int, input().split())
arrone = list(map(int, input().split()))
arrtwo = list(map(int, input().split()))

left = 0
right = 0
while right < m:

    while left < n and arrone[left] < arrtwo[right]:
        left += 1
    arrtwo[right] = left
    right += 1
print(*arrtwo)