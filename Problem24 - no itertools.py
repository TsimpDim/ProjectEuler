def nextPermutation(numbers):
    i = len(numbers) - 1
    while(i > 0 and numbers[i - 1] >= numbers[i]): 
        i -= 1

    if i <= 0 : return False

    j = len(numbers) - 1
    while(numbers[j] <= numbers[i - 1]):
        j -= 1

    numbers[i - 1],numbers[j] = numbers[j],numbers[i - 1]

    
    numbers[i:] = reversed(numbers[i:])

    return True


nums = [0,1,2,3,4,5,6,7,8,9]
for i in range(10**6 - 1):
    nextPermutation(nums)

print(nums)