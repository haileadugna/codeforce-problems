import math
import bisect
l, r = map(int, input().split())

nums = []
for i in range(math.ceil(math.log2(10**18))):
    nums.append(2**i)

left = bisect.bisect_right(nums, l)
print(nums[left])