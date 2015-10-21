"""
Four 
A palindromic number reads the same both ways. 
The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 * 99. 
Find the largest palindrome made from the product of two 3digit numbers.
"""

thousandtozero = []
thousandtozero2 = []
x = 1000
while x > 0:
    thousandtozero.append(x)
    thousandtozero2.append(x)
    x -= 1
    
def reverse(x):
    backwards = ""
    temp = str(x)
    x = len(temp)
    while x > 0:
        backwards += temp[x-1]
        x -= 1
    return backwards   

product = 0
answers = []
for x in range(len(thousandtozero)):
    for y in range(len(thousandtozero2)):
        product = thousandtozero[x] * thousandtozero2[y]
        if str(product) == reverse(product):
            answers.append(product)
            
largest = 0
for x in range(len(answers)):
    if answers[x] > largest:
        largest = answers[x]
print(largest)
