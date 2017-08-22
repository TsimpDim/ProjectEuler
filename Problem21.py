from functools import reduce
from math import sqrt

def factorSum(n):    
    facs = set(reduce(list.__add__, 
                ([i, n//i] for i in range(1, int(sqrt(n)) + 1) if not n % i )))
    sum = 0
    for i in facs:
        sum += i
    
    return sum - n


sum = 0
amicables = []
for i in range(220,10000):
    f = factorSum(i)
    if(i == factorSum(f) and i!=f and i not in amicables and f not in amicables):
        amicables.append(f)
        amicables.append(i)
        sum += f + i

print(sum,amicables)