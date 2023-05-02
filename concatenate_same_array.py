def concatenate(arr):
    for i in range(len(arr)):
        arr.append(arr[i])
    return arr

arr = [1,2,3,5,6]
result = concatenate(arr)
print(result)