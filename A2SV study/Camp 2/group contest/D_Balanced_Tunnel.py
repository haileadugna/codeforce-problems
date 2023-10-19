n = int(input())
enter = list(map(int, input().split()))
exit = list(map(int, input().split()))

exit_pos = {exit[i]: i for i in range(n)}

res = 0
max_exit_pos = -1

for i in range(n):
    car = enter[i]
    
    if exit_pos[car] < max_exit_pos:
        res += 1
    
    max_exit_pos = max(max_exit_pos, exit_pos[car])


print(res)
