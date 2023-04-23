def move_zeroes(arr):
    j = 0
    for i in range(len(arr)):
        if arr[i] != 0:
            arr[i],arr[j] = arr[j],arr[i]
            j += 1
    return arr

print(move_zeroes([0,1,0,0,2,0,3,0,0,4,5,0]))
