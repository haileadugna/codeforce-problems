# test = int(input())

# for _ in range(test):
#     n, time = map(int, input().split())
#     video = list(map(int, input().split()))
#     inter = list(map(int, input().split()))

#     if min(video ) > time:
#         print(-1)
#         continue

#     else:
        
#         for i in range(n):
#             video[i] += i

#         res = []
#         for i in range(n):
#             if video[i] == time:
#                 res.append([inter[i], i])

#         # print(res)
#         if res != []:
#             res.sort()
#             print(res[-1][1] + 1)

#         else:
#             print(-1)

test = int(input().strip())


for _ in range(test):
    n, t = map(int, input().strip().split())
    video = list(map(int, input().strip().split()))
    enter = list(map(int, input().strip().split()))

    max_enter = -1
    max_index = -1

    time_spent = 0
    for i in range(n):
        if time_spent + video[i] <= t:
            if enter[i] > max_enter:
                max_enter = enter[i]
                max_index = i + 1
        time_spent += 1
    print(max_index)
