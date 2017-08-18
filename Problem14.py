import time


def collatz(n,cc):
    t = 1

    while(n != 1):
        if(n in cc): #If we have already calculated the chain starting from n, add the length of the chain
            t += cc[n] - 1 #From the dictionary and exit
            break
        elif(n % 2 == 0):
            n = n // 2
            
        else:
            n = 3*n + 1

        t += 1
        
    
    return t



start_time = time.time()

calced_chains = dict()
max = -1
index = -1
for i in range(2,1000000):
    n = collatz(i,calced_chains)
    

    calced_chains[i] = n
    if(n > max):
        max = n
        index = i


end_time = time.time() - start_time
print(index," || ",max,"-> found in ",end_time,"ms")