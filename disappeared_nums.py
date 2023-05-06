# Given an array nums of n integers where nums[i] is in the range [1, n], return an array of all the integers in the range [1, n] that do not appear in nums.

def disappeared(arr):
    index = -1
    new_arr = []
    for i in range(len(arr)):
        if arr[i] < 0:
            index = (arr[i] *-1)-1
        else:
            index = arr[i]-1

        if arr[index] > 0:
            arr[index] = -arr[index]
        
    for i in range(len(arr)):
        if arr[i] > 0:
            new_arr.append(i+1)
    return new_arr
arr= [2,4,5,1,4]
print(disappeared(arr))