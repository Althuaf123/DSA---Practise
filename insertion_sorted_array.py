# Write a program to insert an element in sorted order into a sorted array

def insert_element(arr,target):
    i = len(arr)-1
    arr.append(target)
    while i>=0 and arr[i] > target:
        arr[i+1] = arr[i]
        i -=1
    arr[i+1] = target
    
    return arr

arr = [1,2,4,5,6]
target  = 0
print(insert_element(arr,target))
