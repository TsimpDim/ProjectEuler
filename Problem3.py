#Problem 3
from math import *
n = 600851475143
prime = 2

def isPrimeNumber(n):

    count = 0
    for i in range(1,n):
        if(n%i == 0):
            count += 1

    if count == 2 : 
        return True
    else:
        return False




def NextPrime(prime):
    num = prime + 1
    for p in range(num, 2*num):
        for i in range(2, p):
            if p % i == 0:
                break
        else:
            return p

i = 0
res = n%prime

while(n/prime != 1):
    if res == 0:
        n = n/prime
        res = n%prime
        continue

    prime = NextPrime(prime)
    res = n%prime
    


print(n)
