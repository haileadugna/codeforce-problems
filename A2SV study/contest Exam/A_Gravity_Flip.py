n = int(input())

nums = list(map(int, input().split()))

if nums == sorted(nums):
    print(*nums)

else:
    print(*sorted(nums))