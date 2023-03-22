
def mergeSort(left, right, arr):
    if left == right:
        return [arr[left]]
    mid = left + (right - left) // 2
    left_half = mergeSort(left, mid, arr)
    right_half = mergeSort(mid + 1, right, arr)

    return merge(left_half, right_half)

def merge(num1, num2):
    l, r = 0, 0
    nums = []
    while l < len(num1) and r < len(num2):
        if num2[r] < num1[l]:
            nums.append(num2[r])
            r += 1
        else:
            nums.append(num1[l])
            l += 1
    nums.extend(num1[l:])
    nums.extend(num2[r:])
    return nums

def test():
    assert mergeSort(0, 6, [3, 0, 2, -5, 10, 0, 2]) == [-5, 1, 0, 2, 2, 3, 10], "Not Implemented Properly"
    assert mergeSort(0, 2, [1, 2, 3]) == [1, 2, 3], "Not ImplementedProperly"
    assert mergeSort(0, 2, [3, 2, 1]) == [1, 2, 3], "Not ImplementedProperly"
    print("Great Job !!!")
test()