def sum_of_digits(n):
    return sum(int(d) for d in str(n))

k = int(input())
count = 0
i = 1

while True:
    if sum_of_digits(i) == 10:
        count += 1
        if count == k:
            print(i)
            break
    i += 1