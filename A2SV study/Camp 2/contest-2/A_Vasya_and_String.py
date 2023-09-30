n, k = map(int, input().split())
s = input()

res = 0
count_a = 0
count_b = 0
left = 0

for right in range(n):
    if s[right] == 'a':
        count_a += 1
    else:
        count_b += 1

    while min(count_a, count_b) > k:
        if s[left] == 'a':
            count_a -= 1
        else:
            count_b -= 1
        left += 1

    res = max(res, right - left + 1)

print(res)
