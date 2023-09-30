digit, summ = map(int, input().split())

if summ == 0 and digit == 1:
    print(0, 0)
elif summ == 0 or summ > digit * 9:
    print(-1, -1)
else:
    # Calculate the maximum possible number
    max_num = [9] * digit
    s = summ 

    for i in range(digit):
        if s >= 9:
            max_num[i] = 9
            s -= 9
        else:
            max_num[i] = s
            s = 0

    # Calculate the minimum possible number
    min_num = [0] * digit
    min_num[0] = 1
    sum2 = summ - 1

    for i in range(digit - 1, -1, -1):
        if sum2 >= 9:
            min_num[i] = 9
            sum2 -= 9
        else:
            min_num[i] += sum2
            break

    min_num_str = ''.join(map(str, min_num))
    max_num_str = ''.join(map(str, max_num))
    print(min_num_str, max_num_str)





# digit, summ = map(int, input().split())
# sum2 = summ

# if summ == 0 and digit == 1:
#     print(0, 0)
#     exit
# max_num = 10 ** digit - 1
# min_num = 10 ** (digit - 1)

# if summ == 0 or summ > digit * 9:
#     print(-1, -1)
#     exit()

# # temp = digit * 9 
# # i = 0
# # while summ > 0:
# #     if temp // summ > 1 or temp % summ >= 9:
# #         temp -= 9
# #         max_num -= 9 * (10 ** i)
# #         i += 1
# #         # temp -= 9
# #     else:
# #         max_num -= (temp%summ )* (10 ** i)
# #         summ = 0
#     # print(max_num, summ, temp, i)
# max_num = [9] * digit
# s = summ 

# for i in range(digit ):
#     if s >= 9:
#         max_num[i] = 9
#         s -= 9
#     else:
#         max_num[i] = s
#         s = 0

# # print(max_num)
# ####################
# min_num = [0] * digit
# min_num[0] = 1
# sum2 -= 1

# for i in range(digit - 1, -1, -1):
#     if sum2 >= 9:
#         min_num[i] = 9
#         sum2 -= 9
#     else:
#         min_num[i] += sum2
#         break

# min_num_str = ''.join(map(str, min_num))
# max_num_str = ''.join(map(str, max_num))
# print(min_num_str, max_num_str)


# m, s = map(int, input().split())

# if s == 0 and m == 1:
#     print(0, 0)
# elif s == 0 or s > 9 * m:
#     print(-1, -1)
# else:
#     min_num = [0] * m
#     min_num[0] = 1
#     s -= 1
    
#     for i in range(m - 1, -1, -1):
#         if s >= 9:
#             min_num[i] = 9
#             s -= 9
#         else:
#             min_num[i] += s
#             break

    # max_num = [9] * m
    # s = s % 9

    # for i in range(m):
    #     if s >= 9:
    #         max_num[i] = 9
    #         s -= 9
    #     else:
    #         max_num[i] += s
    #         break

#     min_num_str = ''.join(map(str, min_num))
#     max_num_str = ''.join(map(str, max_num))

#     print(min_num_str, max_num_str)
