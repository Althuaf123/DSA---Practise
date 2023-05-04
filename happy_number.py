def happy(n):
    check = []
    while n > 0:
        temp = 0
        while n > 0:
            r = n % 10

            temp += r*r
            n = n // 10
        if temp in check:
            return False
        else:
            check.append(temp)

        if temp == 1:
            return True
        
        n = temp
    return False

print(happy(15))
