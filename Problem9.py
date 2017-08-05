def factors(value):
    factors = []
    for i in range(1, int(value**0.5)+1):
        if value % i == 0:
            factors.append((i, int(value / i)))
    return factors


i = 1
triples = []
summ = 0
x,y,z=0,0,0
while summ != 1000:
    fac = factors(i*i/2)
    for pair in fac:
        x = i + pair[0]
        y = i + pair[1]
        z = i + pair[0] + pair[1]

        triples.append([x,y,z])
        if x+y+z == 1000: break
    
    summ = x+y+z
    i += 1
print(x*y*z)       
print(triples)