

n = int(input())
arr = list(map(int, input().split()))
neg = 0
pos = 0
neg_count = 0
pos_count = 0
for i in range(n):
    if arr[i] < 0:
        neg_count, pos_count = pos_count, neg_count
        neg_count += 1
    else:
        pos_count += 1
    neg += neg_count
    pos += pos_count
print(neg, pos)