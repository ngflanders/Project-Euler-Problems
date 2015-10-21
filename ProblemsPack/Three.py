"""
Three
The prime factors of 13195 are 5, 7, 13 and 29.
What is the largest prime factor of the number 600851475143 ?
"""
factors = []
def factor(x):
    for i in range(2, int(x/100000)):
        if x % i == 0:
            factors.append(i)
            x = x / i
            factor(x)
    return factors
    

print(factor(600851475143))
for i in factors:
    if factors.count(i) > 1:
        factors.remove(i)
print(factors)
for i in factors:
    if factors.count(i) > 1:
        factors.remove(i)
print(factors)

largest = 0
for i in range(len(factors)):
    if factors[i] > largest:
        largest = factors[i]
print(largest)
