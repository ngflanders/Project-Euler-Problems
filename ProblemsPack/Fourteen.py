'''
The following iterative sequence is defined for the set of positive integers:

n : n/2 (n is even)
n : 3n + 1 (n is odd)

Using the rule above and starting with 13, we generate the following sequence:

13 : 40 : 20 : 10 : 5 : 16 : 8 : 4 : 2 : 1
It can be seen that this sequence (starting at 13 and finishing at 1) contains 10 terms.
Although it has not been proved yet (Collatz Problem), it is thought that all starting numbers finish at 1.

Which starting number, under one million, produces the longest chain?

NOTE: Once the chain starts the terms are allowed to go above one million.
'''


def isEven(n):
    return n/2
def isOdd(n):
    return 3*n+1


def createSeq(start):
    iCount = 2
    if (start % 2 == 0):
        nxt = isEven(start)
    else:
        nxt = isOdd(start)
    while (nxt != 1):
        if (nxt % 2 == 0):
            nxt = isEven(nxt)
        else:
            nxt = isOdd(nxt)
        iCount +=1
    return iCount

print(createSeq(13))

def seqrange(topend):
    longest = 0
    startnum = 0
    for i in range(1, topend):
        leng = createSeq(i)
        if leng > longest:
            longest = leng
            startnum = i
    return (longest,startnum)
    
print(seqrange(1000000))