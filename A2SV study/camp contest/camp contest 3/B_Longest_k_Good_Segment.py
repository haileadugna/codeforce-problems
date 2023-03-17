from collections import defaultdict
n, k = map(int, input().split())

nums = list(map(int, input().split()))

dictt = defaultdict(int)
left, right = 0, 0
res = []
ans = 0
while right < len(nums):
    if nums[right] in dictt and len(dictt) <= k:
        dictt[nums[right]] += 1
        right += 1
    elif nums[right] not in dictt and len(dictt) == k:
        
        if dictt[nums[left]] > 1:
            dictt[nums[left]] -= 1
        else:
            del dictt[nums[left]]
        left += 1
    elif nums[right] not in dictt and len(dictt) < k:
        dictt[nums[right]] = 1
        right += 1
    if right - left > ans:
        ans = right - left
        res = [left, right]

print(res[0] + 1, res[1])









# stack = deque()
# que = deque()
# res = []
# for i in range(n):
#     while stack and nums[i] > nums[stack[-1]]:
#         stack.pop()
#     while que and nums[i] < nums[que[-1]]:
#         que.pop()
#     que.append(i)
#     stack.append(i)
#     while que and stack and que[0] > stack[0] and nums[stack[0]] - nums[que[0]] >= k :
#         stack.popleft()

#     while que and stack and que[0] < stack[0] and nums[stack[0]] - nums[que[0]] >= k :
#         que.popleft()
#     res.append([que[0], stack[-1]])
# let = 0
# ans = [0, 0]
# for num in res:
#     if num[1] - num[0] > let:
#         ans = num
#         let = num[1] - num[0]

# print(ans[0] + 1, ans[1] + 1)
    


