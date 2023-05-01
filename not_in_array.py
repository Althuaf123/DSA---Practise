def distinct(arr):
    length = len(arr)
    total = (length*(length + 1))/2
    for i in range(len(arr)):
        total = total - arr[i]
    return total

arr = [2,3,4,5,0]
print(distinct(arr))