
def union(arr1, arr2):
    arr3 = []
    for i in arr1:
        if i in arr3:
            continue
        for j in arr2:
            if i == j:
                arr3.append(i)
                break
    return arr3

print(union([1,2,3,1,2,2,2,3,4,5,6,7,8],[1,1,2,2,4,8,1]))
