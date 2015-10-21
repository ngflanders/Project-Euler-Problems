"""
One
If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. 
The sum of these multiples is 23.
Find the sum of all the multiples of 3 or 5 below 1000.
"""


M = [x for x in range(1000) if x % 3 == 0 or x % 5 == 0]  # list comprehension for numbers divisible by 3 or 5 up to 1000
print(M)
total = 0
for i in range(len(M)):  # find the sum
    total += M[i]
print(total)
