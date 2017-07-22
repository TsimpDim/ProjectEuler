result = -1
for i in range(999,101,-1):
    for j in range(i,101,-1):
        multi = str(i*j)
        k = 0
        isPal = True
        while k < len(multi) and isPal:
            if(multi[k] !=  multi[len(multi) - k -1]):
                isPal = False
            k += 1

        if isPal and int(multi) > result: result = int(multi)

print(result)
