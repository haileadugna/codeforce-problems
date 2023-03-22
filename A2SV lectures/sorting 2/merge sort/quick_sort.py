
def quickSort(left, right, arr):
    if right - left <= 1:
        return 
    read = left + 1
    write = left + 1
    while read < len(arr) :
        if arr[left] >= arr[read]:
            arr[write], arr[read] = arr[read], arr[write]
            write += 1
        read += 1

    arr[left], arr[write - 1] = arr[write - 1], arr[left]
    quickSort(left, write - 2, arr)
    quickSort(write, right, arr)
    
arr =  [3,4,1,2,1]
quickSort(0, 4, arr)
print(arr)


        