"""
Six
Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.
"""
SumOfSquares = [x**2 for x in range(101)]
print(SumOfSquares)
toOneHundred = [x for x in range(101)]
print(toOneHundred)

total1 = 0
for x in range(len(SumOfSquares)):
    total1 += SumOfSquares[x]
print(total1)
total2 = 0
for x in range(len(toOneHundred)):
    total2 += toOneHundred[x]
total2 = total2 ** 2
print(total2)
diff = 0
diff = total2 - total1
print(diff)
