x = 2**1000
x = str(x)
sum = 0     
for i in range(0,len(x)):
    sum += int(x[i])
    
print(sum)