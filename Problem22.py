import csv
letters =['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

def AlphValue(name):
    sum = 0
    name = name.lower()
    for letter in name:
        sum += letters.index(letter) + 1

    return sum



def main():
    with open('p022_names.txt') as csvfile:
        names = list(csv.reader(csvfile,delimiter =','))
        names = sorted(names[0],key=str.lower)
        res = 0
        for i in range(0,len(names)):
            res += (i+1)*AlphValue(names[i])
    

    print(res)




if __name__ == "__main__":
    main()