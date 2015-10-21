'''
n! means n * (n - 1) * ... * 3 * 2 * 1

For example, 10! = 10 * 9 * ... * 3 * 2 * 1 = 3628800,
and the sum of the digits in the number 10! is 3 + 6 + 2 + 8 + 8 + 0 + 0 = 27.

Find the sum of the digits in the number 100!
'''

def factorial(y):
    result = 1
    for i in range(1,y+1):
        result = i * result
    print(result)
    return result

def sumdigits(z):
    mystring = str(z)
    pull = 0
    total = 0
    while (len(mystring)>0):
        pull = mystring[-1:]
        total += int(pull)
        mystring = mystring[:-1]
    return total
    '''
    total = 0
    pull = 0
    while (z > 9):
        pull = z % 10
        total += pull
        z = z / 10
       # z = floor(z)
    total += z 
    return total
    '''

print(sumdigits(factorial(100)))



