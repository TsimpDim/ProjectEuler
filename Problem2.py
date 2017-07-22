#Problem 2
p = 0
c = 1
n = p + c
sum = 0

while n <= 4*10**6:
    p = c
    c = n
    n = p + c

    if(n%2 == 0):
        sum += n


print(sum)
