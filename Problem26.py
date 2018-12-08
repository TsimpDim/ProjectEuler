
def main():
    '''For 1/7 we have:
            1/7 = 0.14285714285

            10/7 = 1    --> div = 10*(10 - 1*7) = 30     | divs = [30]     | decs = [1]
            100/7 = 4   --> div = 10*(30 - 4*7) = 20     | divs = [30, 20] | decs = [1, 4]

            etc.

        If at some point e.g div = 30 then we know that the cycle has been restarted, we check for max and we go to the next number
    '''
            
    
    max_dec = []
    max_dec_num = 0
    for d in range(2, 1000): # We skip 1
        div = 10 # We skip 1
        decs = []
        divs = [10]

        while True:
            mod = div / d
            decs.append(int(mod))
            div = 10 * (div - int(mod) * d)

            if div in divs: break
            else: divs.append(div)


        if len(decs) > len(max_dec): 
            max_dec = decs
            max_dec_num = d

    print('_'*10)
    print("Number with max cycle:", max_dec_num)
    print("Max digits in cycle: ",len(max_dec))



if __name__ == "__main__":
    main()
