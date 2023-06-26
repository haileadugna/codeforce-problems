n = int(input())
m = int(input())

benches = []
for _ in range(n):
    benches.append(int(input()))

max_k = max(benches) + m

sorted_benches = sorted(benches)

for _ in range(m):
    sorted_benches[0] += 1
    sorted_benches.sort()

min_k = max(sorted_benches)

print(min_k, max_k)


# import math

# n = int(input())
# m = int(input())
# benches = []

# for _ in range(n):
#     benches.append(int(input()))

# max_initial = max(benches)
# total_people = sum(benches)

# mix_k = math.ceil((total_people + m) / n)
# man_k = max_initial + math.ceil((total_people + m) / n)


# print(mix_k, man_k)
