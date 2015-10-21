'''
Ten
The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
Find the sum of all the primes below two million.
'''

"""
from math import sqrt
def sum_primes(limit):
    sieve = range(limit+1) 
    sieve[1] = 0
    for n in range(2, int(sqrt(limit))+1):
        if sieve[n] > 0:
            for i in range(n*n, limit+1, n): 
                sieve[i] = 0

    return sum(sieve)
    
print(sum_primes(2000000))
"""


def sieve(n):
    np1 = n + 1
    s = list(range(np1))
    s[1] = 0
    sqrtn = int(round(n**0.5))
    for i in range(2, sqrtn + 1):
        if s[i]:
            s[i*i, np1, i] = [0] * len(range(i*i, np1, i))
    return filter(None, s)


list(sieve(20)) 