
def FirstNDigits(digits, print_limit):

    p = 0
    c = 1
    n = p + c
    index = 2

    print(c, n, sep='\n')
    while True:
        p = c
        c = n
        n = p + c
        index += 1
        print('F' + str(index), str(n)[:print_limit])

        if len(str(n)) == digits:
            break


FirstNDigits(1000, 0)
