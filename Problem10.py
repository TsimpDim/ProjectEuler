import time

def sieve(limit):
    sum = 2
    primes = list(range(2,limit+1))

    for i in range(2,limit-1): 
        primes[i] = True

    for p in range(3,len(primes),2):
        if primes[p] == True:
            cur = p
            sum +=p
            while cur+p < limit-1:
                cur += p
                primes[cur] = False
    return sum


start_time = time.time()
r = sieve(2000000) 
end_time = time.time() - start_time
print(end_time,"ms")
print(r,"--Correct is 142913828922")


