#Write a function to print all unique numbers in a unsorted array

def unique(arr):
    unique_array = []
    for i in range(len(arr)):
        count = 0
        for j in range(len(arr)):
            if arr[i] == arr[j] and i!=j:
                count += 1
                break
            else:
                pass
        if count == 0:
            unique_array.append(arr[i])
            print(arr[i])
        else:
            pass
    print(unique_array)
arr = [1,2,3,2,1,1,4,5,3,6,5,7,8,96,7,9,3,1]
print(unique(arr))
