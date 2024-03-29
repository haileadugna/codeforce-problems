# Given an array a
#  of positive integers with length n
# , determine if there exist three distinct indices i
# , j
# , k
#  such that ai+aj+ak
#  ends in the digit 3
# .

# Input
# The first line contains an integer t
#  (1≤t≤1000
# ) — the number of test cases.

# The first line of each test case contains an integer n
#  (3≤n≤2⋅105
# ) — the length of the array.

# The second line of each test case contains n
#  integers a1,a2,…,an
#  (1≤ai≤109
# ) — the elements of the array.

# The sum of n
#  across all test cases does not exceed 2⋅105
# .

# Output
# Output t
#  lines, each of which contains the answer to the corresponding test case. Output "YES" if there exist three distinct indices i
# , j
# , k
#  satisfying the constraints in the statement, and "NO" otherwise.

# You can output the answer in any case (for example, the strings "yEs", "yes", "Yes" and "YES" will be recognized as a positive answer).

# Example
# inputCopy
# 6
# 4
# 20 22 19 84
# 4
# 1 11 1 2022
# 4
# 1100 1100 1100 1111
# 5
# 12 34 56 78 90
# 4
# 1 9 8 4
# 6
# 16 38 94 25 18 99
# outputCopy
# YES
# YES
# NO
# NO
# YES
# YES
# Note
# In the first test case, you can select i=1
# , j=4
# , k=3
# . Then a1+a4+a3=20+84+19=123
# , which ends in the digit 3
# .

# In the second test case, you can select i=1
# , j=2
# , k=3
# . Then a1+a2+a3=1+11+1=13
# , which ends in the digit 3
# .

# In the third test case, it can be proven that no such i
# , j
# , k
#  exist. Note that i=4
# , j=4
# , k=4
#  is not a valid solution, since although a4+a4+a4=1111+1111+1111=3333
# , which ends in the digit 3
# , the indices need to be distinct.

# In the fourth test case, it can be proven that no such i
# , j
# , k
#  exist.

# In the fifth test case, you can select i=4
# , j=3
# , k=1
# . Then a4+a3+a1=4+8+1=13
# , which ends in the digit 3
# .

# In the sixth test case, you can select i=1
# , j=2
# , k=6
# . Then a1+a2+a6=16+38+99=153
# , which ends in the digit 3
# .



# test = int(input())

# for _ in range(test):
#     n = int(input())
#     a = list(map(int, input().split()))
#     for i in range(n):
#         for j in range(i+1, n):
#             for k in range(j+1, n):
#                 if (a[i] + a[j] + a[k]) % 10 == 3:
#                     print("YES")
#                     break
    #         else:
    #             continue
    #         break
    #     else:
    #         continue
    #     break
    # else:
    #     print("NO")



# optimized solution

# test = int(input())

# for _ in range(test):
#     n = int(input())
#     arr = list(map(int, input().split()))
#     cnt = [0]*10
#     for i in range(n):
#         cnt[arr[i]%10] += 1

#     # print(cnt)
#     for i in range(10):
#         for j in range(i+1, 10):
#             for k in range(j+1, 10):
                
#                 if (i * cnt[i] + j * cnt[j] + k * cnt[k])%10 == 3 and (cnt[i] > 0 or cnt[j] > 0 or cnt[k] > 0) :
#                     print("YES")
#                     break
#             else:
#                 continue
#             break
#         else:
#             continue
#         break
#     else:
#         print("NO")

test = int(input())

for _ in range(test):
    n = int(input())
    arr = list(map(int, input().split()))
    cnt = [0] * 10
    for i in range(n):
        cnt[arr[i] % 10] += 1

    for i in range(10):
        for j in range(i + 1, 10):
            for k in range(j + 1, 10):
                if (i + j + k) % 10 == 3 and (cnt[i] > 0 or cnt[j] > 0 or cnt[k] > 0):
                    print("YES")
                    break
            else:
                continue
            break
        else:
            continue
        break
    else:
        print("NO")
