def fac(num): #Same function from Problem15
    fac = num
    
    if(num % 2 == 0 and num != 2):
        limit = 2
    else:
        limit = 3

    partial = num - 2
    toAdd = num
    while True:
        toAdd += partial
        fac *= toAdd
        partial -= 2 
        if partial < limit : break


    if(num % 2 != 0):
        fac*= int(num / 2) + (num % 2 > 0)

    return fac


res = str(fac(100))
sum = 0
for i in range(0,len(res)):
    sum += int(res[i])
    
print(sum)