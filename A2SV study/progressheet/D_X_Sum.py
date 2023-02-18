test = int(input())

for _ in range(test):
    n, m = map(int, input().split())

    board = []
    for i in range(n):
        row = list(map(int, input().split()))
        board.append(row)

    # Calculate the sums of the two diagonals
    diag_1 = [0] * (n+m-1)
    diag_2 = [0] * (n+m-1)
    for i in range(n):
        for j in range(m):
            diag_1[i+j] += board[i][j]
            diag_2[i-j+m-1] += board[i][j]

    # Find the maximum sum over all possible placements of the bishop
    max_sum = 0
    for i in range(n):
        for j in range(m):
            sum_attacked = diag_1[i+j] + diag_2[i-j+m-1] - board[i][j]
            max_sum = max(max_sum, sum_attacked)

    print(max_sum)