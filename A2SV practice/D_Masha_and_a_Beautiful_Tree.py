
test = int(input())
for _ in range(test):
    n = int(input())
    nums = list(map(int, input().split()))

    def masha( nums):
        res = 0
        def mergeSort(left, right, arr):
            nonlocal res
            if left == right:
                return [arr[left]]
            mid = left + (right - left) // 2
            left_half = mergeSort(left, mid, arr)
            right_half = mergeSort(mid + 1, right, arr)

            return merge(left_half, right_half)

        def merge(num1, num2):
            nonlocal res
            nums = []
            if num1[0] > num2[0]:
                nums = num2 + num1
                res += 1
            else:
                nums = num1 + num2

            return nums
        temp = mergeSort(0, n-1, nums)
  
        if temp == sorted(nums):
            print(res)
        else:
            print(-1)
        
    masha(nums)