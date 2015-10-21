"""
Seven
By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.
What is the 10 001st prime number?
"""

def is_prime(x):
    for y in range(2, x):
        if x % y == 0:
            return False
    return True


x = 2
primecounter = 1
while primecounter <= 10001:
    if is_prime(x):
        primecounter += 1
        if primecounter % 1000 == 0:
            print(primecounter)
    x += 1
print(x-1)
