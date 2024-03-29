# The store sells n
#  items, the price of the i
# -th item is pi
# . The store's management is going to hold a promotion: if a customer purchases at least x
#  items, y
#  cheapest of them are free.

# The management has not yet decided on the exact values of x
#  and y
# . Therefore, they ask you to process q
#  queries: for the given values of x
#  and y
# , determine the maximum total value of items received for free, if a customer makes one purchase.

# Note that all queries are independent; they don't affect the store's stock.

# Input
# The first line contains two integers n
#  and q
#  (1≤n,q≤2⋅105
# ) — the number of items in the store and the number of queries, respectively.

# The second line contains n
#  integers p1,p2,…,pn
#  (1≤pi≤106
# ), where pi
#  — the price of the i
# -th item.

# The following q
#  lines contain two integers xi
#  and yi
#  each (1≤yi≤xi≤n
# ) — the values of the parameters x
#  and y
#  in the i
# -th query.

# Output
# For each query, print a single integer — the maximum total value of items received for free for one purchase.

# Example
# inputCopy
# 5 3
# 5 3 1 5 2
# 3 2
# 1 1
# 5 3
# outputCopy
# 8
# 5
# 6
# Note
# In the first query, a customer can buy three items worth 5,3,5
# , the two cheapest of them are 3+5=8
# .

# In the second query, a customer can buy two items worth 5
#  and 5
# , the cheapest of them is 5
# .

# In the third query, a customer has to buy all the items to receive the three cheapest of them for free; their total price is 1+2+3=6
# .

# Solution code correctly
# n, q = map(int, input().split())
# arr = list(map(int, input().split()))
# arr.sort()
# for i in range(q):
#     x, y = map(int, input().split())
#     print(sum(arr[(n-x):(n-x)+y]))


#  it says time limite exceeded optimize it and give me a new code
    
n, q = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort()

prefix_sum = [0] * (n + 1)
for i in range(1, n + 1):
    prefix_sum[i] = prefix_sum[i - 1] + arr[i - 1]

for i in range(q):
    x, y = map(int, input().split())
    print(prefix_sum[n-x+y] - prefix_sum[n - x])




