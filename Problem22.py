import csv
letters =['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

def AlphValue(name):
    sum = 0
    name = name.lower()
    for letter in name:
        sum+= letters.index(letter) + 1

    return sum


def MergeSort(mainlist):
    


def main():

    with open('p022_names.txt') as csvfile:
        reader = MergeSort(list(csv.reader(csvfile,delimiter =',')))
        res = 0
        for i in range(1,len(reader[0])):
            res += i*AlphValue(reader[0][i-1])

    print(res)




if __name__ == "__main__":
    main()