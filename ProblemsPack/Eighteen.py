'''
By starting at the top of the triangle below and moving to adjacent numbers on the row below,
 the maximum total from top to bottom is 23.

3
7 4
2 4 6
8 5 9 3

That is, 3 + 7 + 4 + 9 = 23.

Find the maximum total from top to bottom of the triangle below:

75
95 64
17 47 82
18 35 87 10
20 04 82 47 65
19 01 23 75 03 34
88 02 77 73 07 63 67
99 65 04 28 06 16 70 92
41 41 26 56 83 40 80 70 33
41 48 72 33 47 32 37 16 94 29
53 71 44 65 25 43 91 52 97 51 14
70 11 33 28 77 73 17 78 39 68 17 57
91 71 52 38 17 14 91 43 58 50 27 29 48
63 66 04 68 89 53 67 30 73 16 69 87 40 31
04 62 98 27 23 09 70 98 73 93 38 53 60 04 23

NOTE: As there are only 16384 routes, it is possible to solve this problem by trying every route.
However, Problem 67, is the same challenge with a triangle containing one-hundred rows;
it cannot be solved by brute force, and requires a clever method! ;)
'''
#import re
given = "3 7 4 2 4 6 8 5 9 3"
givendict = {1:[3], 2:[7,4], 3:[2,4,6],4:[8,5,9,3]}
given2 = "75 95 64 17 47 82 18 35 87 10 20 04 82 47 65 19 01 23 75 03 34 \
88 02 77 73 07 63 67 99 65 04 28 06 16 70 92 41 41 26 56 83 40 80 70 33 \
41 48 72 33 47 32 37 16 94 29 53 71 44 65 25 43 91 52 97 51 14 \
70 11 33 28 77 73 17 78 39 68 17 57 91 71 52 38 17 14 91 43 58 50 27 29 48 \
63 66 04 68 89 53 67 30 73 16 69 87 40 31 04 62 98 27 23 09 70 98 73 93 38 53 60 04 23"
given2dict = {1:[75],2:[95,64],3:[17,47,82],4:[18,35,87,10],5:[20, 4, 82, 47, 65],\
              6:[19, 1, 23, 75, 3, 34], 7:[88, 2, 77, 73, 7, 63, 67],8:[99, 65, 4, 28, 6, 16, 70, 92],
              9:[41, 41, 26, 56, 83, 40, 80, 70, 33], 10:[41, 48, 72, 33, 47, 32, 37, 16, 94, 29],
              11:[53, 71, 44, 65, 25, 43, 91, 52, 97, 51, 14], 12:[70, 11, 33, 28, 77, 73, 17, 78, 39, 68, 17, 57],
              13:[91, 71, 52, 38, 17, 14, 91, 43, 58, 50, 27, 29, 48], 
              14:[63, 66, 4, 68, 89, 53, 67, 30, 73, 16, 69, 87, 40, 31],
              15:[4, 62, 98, 27, 23, 9, 70, 98, 73, 93, 38, 53, 60, 4, 23]}



def findchildren(lvl, po, treedict):
    k1 = treedict[lvl+1][po]
    k1pos = po
    k2 = treedict[lvl+1][po+1]
    k2pos = po+1
    return k1, k1pos, k2, k2pos

def findpath(treedict):
    level = 1
    posi = x = 0
    totalsum = treedict[level][posi]
    kid1,kid1p, kid2,kid2p = findchildren(level, posi, treedict)
    height = len(treedict.keys())
    while (x < height-2):
        if (kid1 > kid2):
            totalsum += kid1
            level +=1
            kid1,kid1p, kid2,kid2p = findchildren(level,kid1p , treedict)
        else:
            totalsum += kid2
            level +=1
            kid1,kid1p, kid2,kid2p = findchildren(level, kid2p, treedict)
        x += 1
    if (kid1 > kid2):
        totalsum += kid1
    else:
        totalsum += kid2   
    return totalsum
        
    
print(findpath(givendict))
print(findpath(given2dict))

        
        

