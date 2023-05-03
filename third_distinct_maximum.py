# Write a program to find the third distinct maximum from an array of integers. If the array doesn't have a third distinct maximum, return the largest number.

def third_distinct(arr):
    largest = arr[0]
    second_largest = float('-inf')
    third_largest = float('-inf')

    for i in range(len(arr)):
        if arr[i] > largest:
            third_largest = second_largest
            second_largest = largest
            largest = arr[i]
        elif arr[i] <= largest and arr[i] > second_largest and arr[i] >= third_largest:
            third_largest = second_largest
            second_largest = arr[i]
        
        elif arr[i] < largest and arr[i] < second_largest and arr[i] > third_largest:
            third_largest = arr[i]
    
    if third_largest != float('-inf'):
        return third_largest
    else:
        return largest

arr = [2,3,1,5,2,7,8,6,9,1,2]    
print(third_distinct(arr))