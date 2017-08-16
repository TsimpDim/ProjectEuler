from math import *
from functools import reduce
import time


def factors(n):    
    return set(reduce(list.__add__, 
                ([i, n//i] for i in range(1, int(n**0.5) + 1) if n % i == 0)))




start = time.time()

i = 28
while True:
    triang = (i*(i+1))/2
    if(len(factors(triang)) > 500 ) : 
        break
    i+=1
    
t = (time.time() - start)
print(triang,"-> found in ",t,"seconds")
 
