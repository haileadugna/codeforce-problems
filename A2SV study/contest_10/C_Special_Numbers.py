test = int(input())
for _ in range(test):

    n, k = map(int, input().split())

    bit_k = bin(k)
    le = len(bit_k)

    ans = 0
    for i in range(2, len(bit_k)):
        if bit_k[i] == "1":
            ans += n**(le - i - 1)
    print(ans % (10 ** 9 + 7))
