"""
Five
2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
"""
x = 2520

while (x % 2 != 0 or x % 3 != 0 or x % 4 != 0 or x % 5 != 0 or x % 6 != 0 or x % 7 != 0 or x % 8 != 0 or x % 9 != 0 
       or x % 10 != 0 or x % 11 != 0 or x % 12 != 0 or x % 13 != 0 or x % 14 != 0 or x % 15 != 0 or x % 16 != 0 
      or x % 17 != 0 or x % 18 != 0 or x % 19 != 0 or x % 20 != 0):
    x += 1
print(x)

