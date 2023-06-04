s = input().strip()

last_upper = -1
actions = 0

for i in range(len(s)):
    if s[i].isupper():
        last_upper = i
    elif last_upper != -1:
        actions += i - last_upper
        last_upper += 1

print(actions)
