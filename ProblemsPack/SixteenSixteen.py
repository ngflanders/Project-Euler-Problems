'''
2**15 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.

What is the sum of the digits of the number 2**1000?
'''

from math import pow



def power(base,expo):
    mystri = "{a:9.3f}".format(a = pow(2, 1000))
    return mystri

def sumdigits(z):
    mystring = str(z)
    pull = 0
    total = 0
    while (len(mystring)>0):
        pull = mystring[-1:]
        if (pull != "."):
            total += int(pull)
        mystring = mystring[:-1]
    return total


print(power(2,1000))
print(pow(2, 1000))
print(sumdigits(power(2, 1000)))