from functools import reduce
from math import sqrt

# Same function from problem 21
def factorSum(n):
    facs = set(reduce(list.__add__,
                      ([i, n // i] for i in range(1, int(sqrt(n)) + 1) if not n % i)))
    sum = 0
    for i in facs:
        sum += i

    return sum - n


# Find all abudant numbers
abs = []
isSum = [0] * 28123
for i in range(12, 28124):  # 12 is the smallest abundant
    if i < factorSum(i):
        abs.append(i)

# Find which numbers CAN be written as a sum of two abundant numbers
for i in range(len(abs)):
    for j in range(i, len(abs)):
        if abs[i] + abs[j] < 28123:
            isSum[abs[i] + abs[j]] = 1
        else:
            break

# Find the sum
sum = 0
for i in range(28123):
    if not isSum[i]:
        sum += i

print(sum)
