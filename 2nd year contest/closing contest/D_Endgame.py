# Thanos wants to destroy the avengers base, but he needs to destroy the avengers along with their base.

# Let's represent their base with an array, where each position can be occupied by many avengers, but one avenger can occupy only one position. Length of their base is a perfect power of 2
# . Thanos wants to destroy the base using minimum power. He starts with the whole base and in one step he can do either of following:

# if the current length is at least 2
# , divide the base into 2
#  equal halves and destroy them separately, or
# burn the current base. If it contains no avenger in it, it takes A
#  amount of power, otherwise it takes his B⋅na⋅l
#  amount of power, where na
#  is the number of avengers and l
#  is the length of the current base.
# Output the minimum power needed by Thanos to destroy the avengers' base.
# Input
# The first line contains four integers n
# , k
# , A
#  and B
#  (1≤n≤30
# , 1≤k≤105
# , 1≤A,B≤104
# ), where 2n
#  is the length of the base, k
#  is the number of avengers and A
#  and B
#  are the constants explained in the question.

# The second line contains k
#  integers a1,a2,a3,…,ak
#  (1≤ai≤2n
# ), where ai
#  represents the position of avenger in the base.

# Output
# Output one integer — the minimum power needed to destroy the avengers base.

# Examples
# inputCopy
# 2 2 1 2
# 1 3
# outputCopy
# 6
# inputCopy
# 3 2 1 2
# 1 7
# outputCopy
# 8
# Note
# Consider the first example.

# One option for Thanos is to burn the whole base 1−4
#  with power 2⋅2⋅4=16
# .

# Otherwise he can divide the base into two parts 1−2
#  and 3−4
# .

# For base 1−2
# , he can either burn it with power 2⋅1⋅2=4
#  or divide it into 2
#  parts 1−1
#  and 2−2
# .

# For base 1−1
# , he can burn it with power 2⋅1⋅1=2
# . For 2−2
# , he can destroy it with power 1
# , as there are no avengers. So, the total power for destroying 1−2
#  is 2+1=3
# , which is less than 4
# .

# Similarly, he needs 3
#  power to destroy 3−4
# . The total minimum power needed is 6
# .


n,k,A,B = map(int, input().split())

arr = list(map(int, input().split()))

arr.sort()

def solve(arr, A, B):
    if len(arr) == 0:
        return 0
    if len(arr) == 1:
        return A
    mid = len(arr)//2
    left = []
    right = []
    for i in arr:
        if i <= mid:
            left.append(i)
        else:
            right.append(i)
    return min(A*len(arr), B) + solve(left, A, B) + solve(right, A, B)

print(solve(arr, A, B))