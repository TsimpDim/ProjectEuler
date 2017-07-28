def isPrimeNumber(n):
    if n==2 or n==3: return True
    if n%2==0 or n<2: return False
    for i in range(3,int(n**0.5)+1,2):  
        if n%i==0:
            return False    

    return True

pr = 0
pr_num = 0
i = 3
while(pr_num < 10000):
    if isPrimeNumber(i):
       pr = i
       pr_num += 1
       #print(pr)
    i+=2

print(pr)