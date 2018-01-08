def EulerFormula(n,a,b):
    return n**2 + a*n + b

def sieve(limit):
    primes = []
    not_primes = []
    for i in range(2, limit+1):
        if i not in not_primes:
            primes.append(i)
            for j in range(i*i, limit+1, i):
                not_primes.append(j)
    return primes


def main():
    
    maximum = -1
    product = 0
    primes = sieve(1000)
    for a in range(-1000,1000):
        for b in primes:
            n = 0

            while abs(EulerFormula(n,a,b)) in primes:
                n += 1

            if n > maximum :
                maximum = n
                product = a * b
                maxa = a
                maxb = b

    print("Maximum count : " + str(maximum))
    print("Product : " + str(product))
    print("Max a : " + str(maxa))
    print("Max b : " + str(maxb))  


if __name__ == "__main__":
    main()