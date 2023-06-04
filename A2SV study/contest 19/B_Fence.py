n, k = map(int, input().split())
nums = list(map(int, input().split()))

min_sum = sum(nums[:k])
min_index = 0

current_sum = min_sum
for i in range(1, n-k+1):
    current_sum += nums[i+k-1] - nums[i-1]
    if current_sum < min_sum:
        min_sum = current_sum
        min_index = i

print(min_index + 1)  