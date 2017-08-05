#This finds the PRIMITIVE Pythagorean triple which builds the one with sum of 1000
#Therefore this solves an entirely different problem :/
#Also, this code has some clutter but it helps print the correct information neatly

def improper_to_mixed(whole:int,numerator:int,denominator:int):
    return [denominator,whole*denominator+numerator]

denom = 3
sum_1 = 0
sum_2 = 0
i = 1
results_1 = []
results_2 = []
while(sum_1 <= 1000 or sum_2 <= 1000):

    #Plato's family
    mixed = improper_to_mixed(i,i,denom)
    mixed.append(mixed[1]+1)
    sum_1 = mixed[0] + mixed[1] + mixed[2]
    results_1.append(sum_1)
    print(mixed[0],mixed[1],mixed[2])

    if 1000%sum_1 == 0: break
    
    denom += 2

    #Pythagoras' family
    mixed_2 = improper_to_mixed(i,4*i + 3,4*i + 4)
    mixed_2.append(mixed_2[1]+2)
    sum_2 = mixed_2[0] + mixed_2[1] + mixed_2[2]
    results_2.append(sum_2)
    print(mixed_2[0],mixed_2[1],mixed_2[2])
    
    if 1000%sum_2 == 0: break

    i+=1

    


print("\n\nPlato:",results_1)
print("Pythagoras:",results_2)
