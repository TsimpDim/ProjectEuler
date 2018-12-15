
def main():

    main_set = set()

    for a in range(2, 101):
        for b in range(2, 101):
            main_set.add(a**b)

    print(len(main_set))



if __name__=="__main__":
    main()