#Quite honestly this just takes 10secs to just do the calculation in WolframAlpha with simple combinatorics
y = 20
x = 20

def fac(num):
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


result = fac(x+y)/(fac(x)*fac(y)) 
print(int(result))