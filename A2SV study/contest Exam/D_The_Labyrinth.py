# import sys, threading

# def main():
#     n, m = map(int, input().split())

#     nums = []
#     for i in range(n):
#         nums.append(list(map(str, input().strip())))

#     def dfs(i, j, vis):
#         if i < 0 or i >= n or j < 0 or j >= m or (i, j) in vis or nums[i][j] != ".":
#             return 0

#         vis.add((i, j))
        
#         total_count = 1
#         total_count += dfs(i, j + 1, vis)
#         total_count += dfs(i, j - 1, vis)
#         total_count += dfs(i + 1, j, vis)
#         total_count += dfs(i - 1, j, vis)
        
#         return total_count

#     for i in range(n):
#         for j in range(m):
#             if nums[i][j] == "*":
#                 nums[i][j] = "."
#                 ans = dfs(i, j, set())
#                 nums[i][j] = str(ans%10)


#     for i in range(n):
#         temp = ""
#         for j in range(m):
#             temp += str(nums[i][j])

#         print(temp)


# sys.setrecursionlimit(1 << 30)

# threading.stack_size(1 << 27)

# main_thread = threading.Thread(target = main)

# main_thread.start()

# main_thread.join()

import sys
import threading
from collections import defaultdict

# def main():
    # n, m = map(int, input().split())

    # nums = []
    # for i in range(n):
    #     nums.append(list(map(str, input().strip())))

    # def dfs(i, j, vis):
    #     if i < 0 or i >= n or j < 0 or j >= m or (i, j) in vis or nums[i][j] != ".":
    #         return 0

    #     vis.add((i, j))

    #     total_count = 1
    #     total_count += dfs(i, j + 1, vis)
    #     total_count += dfs(i, j - 1, vis)
    #     total_count += dfs(i + 1, j, vis)
    #     total_count += dfs(i - 1, j, vis)

    #     return total_count

    # for i in range(n):
    #     for j in range(m):
    #         if nums[i][j] == "*":
    #             nums[i][j] = "."
    #             ans = dfs(i, j, set())
    #             nums[i][j] = str(ans % 10)

    # for i in range(n):
    #     temp = ""
    #     for j in range(m):
    #         temp += str(nums[i][j])

    #     print(temp)

from collections import defaultdict

def check(row, col, strings, label, store, n, m):
    visited = set([(row, col)])  
    stack = [(row, col)]
    while stack:
        row, col = stack.pop()
        direction = ((1, 0), (0, 1), (-1, 0), (0, -1))

        for x, y in direction:
            newR, newC = row + x, col + y
            if -1 < newR < n and -1 < newC < m and (newR, newC) not in visited:
                if type(strings[newR][newC]) == str and strings[newR][newC] == ".":
                    stack.append((newR, newC))
                    visited.add((newR, newC))
    store[label] = len(visited)  
    for row, col in visited: 
        strings[row][col] = label 

def fuct(n, m, strings):
    labelStore = defaultdict(int)
    label = 0
    for i in range(n):
        for j in range(m):
            if type(strings[i][j]) == str and strings[i][j] == ".":
                check(i, j, strings, label, labelStore, n, m)
                label += 1

    for i in range(n):
        for j in range(m):
            if type(strings[i][j]) == str and strings[i][j] == "*":
                friend = set()
                direction = ((1, 0), (0, 1), (-1, 0), (0, -1))
                for x, y in direction:
                    newR, newC = i + x, j + y
                    if -1 < newR < n and -1 < newC < m:
                        if type(strings[newR][newC]) == int:
                            friend.add(strings[newR][newC])
                ans = 0
                for val in friend:
                    ans += labelStore[val]
                strings[i][j] = str((ans + 1) % 10)
    for i in range(n):
        for j in range(m):
            if type(strings[i][j]) == int:
                strings[i][j] = "."
    for val in strings:
        print("".join(map(str, val))) 

n, m = map(int, input().split())
nums = []
for _ in range(n):
    nums.append(list(input()))

fuct(n, m, nums)



# sys.setrecursionlimit(1 << 30)
# threading.stack_size(1 << 27)
# # main_thread = threading.Thread(target=main)
# main_thread.start()
# main_thread.join()


# from collections import defaultdict


# def LI(): return list(map(int, input().split(" ")))
# def LS(): return input().split(" ")
# def LC(): return input().split()
# def I(): return int(input())
# def S(): return input()



# def expander(row, col, strings, label, labelStore, n, m):
#     store = set([(row, col)])
#     stack = [(row, col)]
#     while stack:
#         row, col = stack.pop()
#         direction = ((1,0), (0,1), (-1,0), (0,-1))
        
#         for x, y in direction:
#             newR, newC = row + x, col + y
#             if -1 <newR < n and -1 < newC < m and (newR, newC) not in store:
#                 if type(strings[newR][newC]) == str and strings[newR][newC] == ".":
#                     stack.append((newR, newC))
#                     store.add((newR, newC))
#     labelStore[label] = len(store)
#     for row, col in store:
#         strings[row][col] = label            
        
    
    
    


# def sol(n, m, strings):
#     labelStore = defaultdict(int)
#     label = 0
#     for i in range(n):
#         for j in range(m):
#             if type(strings[i][j]) == str and strings[i][j] == ".":
#                 expander(i, j, strings, label, labelStore, n, m)
#                 label += 1
                
#     for i in range(n):
#         for j in range(m):
#             if type(strings[i][j]) == str and strings[i][j] == "*":
#                 friend = set()
#                 direction = ((1,0), (0,1), (-1,0), (0,-1))
#                 for x, y in direction:
#                     newR, newC = i + x, j + y
#                     if -1 <newR < n and -1 < newC < m:
#                         if type(strings[newR][newC]) == int:
#                             friend.add(strings[newR][newC])
#                 ans = 0
#                 for val in friend:
#                     ans += labelStore[val]
#                 strings[i][j] = str( (ans + 1) % 10 )
#     for i in range(n):
#         for j in range(m):
#             if  type(strings[i][j]) == int:
#                 strings[i][j] = "."
#     for val in strings:
#         print("".join(val))
                
                    
                

# n, m = LI()
# strings = []
# for _ in range(n):
#     strings.append(list(S()))

# sol(n, m, strings)