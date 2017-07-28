from functools import reduce
num = range(1,21)

def gcd(a,b):
    if b == 0:
       return a
    else:
       return gcd(b, a%b)

def lcm(a,b):
    return a*b/gcd(a,b)

print(int(reduce(lcm,num)))

