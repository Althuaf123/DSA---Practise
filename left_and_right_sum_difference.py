def difference(arr):
    add = [0]
    for i in arr:
        add += [add[-1]+i]
    sub = []
    for i in range (1,len(add)):
        sub  += [abs(add[-1]-add[i]-add[i-1])]
    return sub

arr = [7,2,3,8,5]
print(difference(arr))
