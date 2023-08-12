n, t = map(int, input().split())
nums = list(map(int, input().split()))

left, right = 0, 0
total_time = 0
max_books = 0

while right < n:
    total_time += nums[right]
    while total_time > t:
        total_time -= nums[left]
        left += 1
    max_books = max(max_books, right - left + 1)
    right += 1



print(max_books)



