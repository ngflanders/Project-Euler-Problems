"""
Nine
A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,

a**2 + b**2 = c**2
For example, 3**2 + 4**2 = 9 + 16 = 25 = 5**2.

There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.
"""
from math import sqrt
import sys

def SolveC(a, b):
    return sqrt(a**2 + b**2)


x = 10
while (x<1000):
    y = 10
    while (y < 1000):
        z = SolveC(x, y)
        if ((x + y + z).is_integer() == True):
            #print "Triple"
            #print (x, y, z)
            if (x + y + z == 1000.0):
                print(int(x * y * z))
                sys.exit()
        #print x + y + z
        y += 1
    x += 1
