#program to sort an array

def sort_array(arr):
    for i in range(len(arr)):
        for j in range(0,len(arr)-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

print(sort_array([5,8,3,9,2,7,1]))