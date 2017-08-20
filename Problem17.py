FullUnits = ["","one","two","three","four","five","six","seven","eight","nine","ten","eleven","twelve","thirteen","fourteen","fifteen","sixteen","seventeen","eighteen","nineteen"]
FullDozens = ["","ten","twenty","thirty","forty","fifty","sixty","seventy","eighty","ninety"]

def Letters(text):
    letters = 0
    for i in range(0,len(text)):
        if(text[i] != ' ' and text[i] != '-'):
            letters += 1
    return letters


def ToWords(num):
    final = ""
    if(num == 1000):
        final = "one thousand"
    elif(num < 20):
        final = FullUnits[num]
    elif(num < 100):
        final = FullDozens[num//10]+" "+FullUnits[num%10]
    elif(num < 1000):
        final = FullUnits[num//100]+" hundred "
        if(num % 100 != 0):
            final +="and "+ToWords(num%100)

    #print(num,final,Letters(final))
    return final

sum = 0
for i in range(1,1001):
    sum += Letters(ToWords(i))

print(sum)

