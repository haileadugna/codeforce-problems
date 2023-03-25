n, k = map(int, input().split())
nums = list(map(int, input().split()))


def mergeSort(left, right):
    if left == right:
        return [left]
    mid = (right + left) // 2
    left_half = mergeSort(left, mid)
    right_half = mergeSort(mid + 1, right)

    return merge(left_half, right_half)

def merge(num1, num2):
    min_num1 = min([nums[ind] for ind in num1])
    min_num2 = min([nums[ind] for ind in num2])

    merged = []
    for i in range(len(num1)):
        if nums[num1[i]] > min_num2 or abs(min_num2 - nums[num1[i]]) <= k:
            merged.append(num1[i])
    for i in range(len(num2)):
        if nums[num2[i]] > min_num1 or abs(min_num1 - nums[num2[i]]) <= k:
            merged.append(num2[i])
  
    return merged

temp = mergeSort(0, len(nums) -1)
print(*[i + 1 for i in temp])
    
