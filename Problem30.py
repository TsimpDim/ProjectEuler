def main():

    valid_numbers = []
    for i in range(2, 295245):
        digits = [int(d) for d in str(i)]
        if sum([d**5 for d in digits]) == i: valid_numbers.append(i)
    print(sum(valid_numbers))



if __name__ == "__main__":
    main()