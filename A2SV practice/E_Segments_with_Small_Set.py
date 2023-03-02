from collections import defaultdict


n, k = map(int, input().split())
nums = list(map(int, input().split()))

left = 0
res = 0
dict_num = defaultdict(int)

for i in range(n):

    dict_num[nums[i]] += 1
    # print(dict_num)
    while len(dict_num) > k:

        if dict_num[nums[left]] > 1:
            dict_num[nums[left]] -= 1
        else:
            del dict_num[nums[left]]
        left += 1
    res += (i - left + 1)

print(res)