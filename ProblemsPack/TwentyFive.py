'''
The Fibonacci sequence is defined by the recurrence relation:

Fn = Fn-1 + Fn-2, where F1 = 1 and F2 = 1.
Hence the first 12 terms will be:

F1 = 1
F2 = 1
F3 = 2
F4 = 3
F5 = 5
F6 = 8
F7 = 13
F8 = 21
F9 = 34
F10 = 55
F11 = 89
F12 = 144
The 12th term, F12, is the first term to contain three digits.

What is the index of the first term in the Fibonacci sequence to contain 1000 digits?
'''
import math



def Fibon(numofdigits=1000):
    Fibn = [1, 2]  #declaring the list
    first = 1
    second = 2
    x = first + second   # add the two previous numbers together
    digits = 1
    while (digits) < numofdigits:  # Fib number up to 4 million
        Fibn.append(x)   # add Fib number to the list
        first = second
        second = x 
        x = first + second
        digits = int(math.log10(x))+1
    #print(Fibn)
    return(len(Fibn)+2)

print(Fibon())




















